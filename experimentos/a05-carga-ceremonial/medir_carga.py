#!/usr/bin/env python3
"""Instrumento de A-05: carga ceremonial persistida de las entregas de metodo.

Mide, sobre la historia de git de un repositorio, que fraccion del texto que
escriben los commits de metodo es ceremonia persistida (lineas agregadas al
historial de metodo) y que fraccion es el cambio mismo. No lee prosa para
clasificar nada: la clasificacion sale solo de la ruta del archivo.

Definiciones (selladas en `EXPERIMENTO-A5-carga-ceremonial.md`, no se cambian
despues de ver datos):

- Commit de metodo: toca al menos un archivo de metodo o del historial, segun
  la definicion de cada repositorio vigente en el commit sellado.
- Ceremonia: caracteres no blancos de las lineas agregadas a un archivo del
  historial. Cambio: los de las lineas agregadas a cualquier otro archivo.
- Movimiento: una linea agregada cuyo texto, sin espacios en los extremos y de
  al menos MIN_MOVIMIENTO caracteres, coincide con una linea quitada en el mismo
  commit. No cuenta como ceremonia ni como cambio: mover no es escribir.
- Se excluye el commit raiz (importacion inicial) y los merges.

Uso:
    python medir_carga.py --selftest
    python medir_carga.py --repo <ruta> --head <commit> --perfil <propio|r40> [--detalle]
        [--repo2 <ruta> --head2 <commit> --perfil2 <propio|r40>]

Con el segundo corpus agrega el IC95 de la diferencia entre las dos razones
agregadas (primero menos segundo), remuestreando cada corpus por separado.

La salida es JSON con agregados. `--detalle` agrega una fila por commit con
numeros y hash, y MUST NOT usarse sobre el corpus de [R40] (fuente reservada:
solo agregados).
"""

from __future__ import annotations

import argparse
import json
import random
import re
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

MIN_MOVIMIENTO = 20
SEMILLA = 20261007
REMUESTREOS = 10000

PERFILES = {
    # Este repositorio: `METODO_FILES`/`METODO_DIRS` de `tools/check_docs.py` y
    # el historial con sus tomos (M-30).
    "propio": {
        "metodo_files": {"AGENTS.md", "CONSTITUTION.md", "SPECS_REGISTRY.md", "CONVENCIONES.md",
                         "REFERENCIAS.md", "CLAUDE.md"},
        "metodo_dirs": ("templates/", "tools/"),
        "historial": re.compile(r"^historial/sdd(-[^/]+)?\.md$"),
    },
    # Caso de campo 1 [R40]: las mismas constantes de su backstop.
    "r40": {
        "metodo_files": {"AGENTS.md", "SPECS_REGISTRY.md", "CONVENCIONES.md", "CONSTITUTION.md",
                         "CLAUDE.md", "historial/HISTORIAL.md"},
        "metodo_dirs": ("tools/", "agenda/", ".agents/", ".claude/", "normativa/utils/"),
        "historial": re.compile(r"^historial/sdd\.md$"),
    },
}


def git(repo: Path, *args: str) -> str:
    out = subprocess.run(["git", *args], cwd=str(repo), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return out.stdout.decode("utf-8", errors="replace")


def chars(texto: str) -> int:
    return sum(1 for c in texto if not c.isspace())


def diff_commit(repo: Path, sha: str) -> dict[str, tuple[list[str], list[str]]]:
    """{ruta: (agregadas, quitadas)} del commit contra su padre."""
    salida = git(repo, "show", "--format=", "--no-color", "--no-renames", "--no-ext-diff", "-U0", sha)
    archivos: dict[str, tuple[list[str], list[str]]] = {}
    actual = None
    for ln in salida.splitlines():
        if ln.startswith("diff --git "):
            actual = None
            continue
        if ln.startswith("+++ "):
            ruta = ln[4:]
            actual = ruta[2:] if ruta.startswith("b/") else None
            if actual is not None:
                archivos.setdefault(actual, ([], []))
            continue
        if ln.startswith("--- "):
            ruta = ln[4:]
            if ruta.startswith("a/"):
                previo = ruta[2:]
                archivos.setdefault(previo, ([], []))
                actual = previo
            continue
        if actual is None or ln.startswith("@@"):
            continue
        if ln.startswith("+"):
            archivos[actual][0].append(ln[1:])
        elif ln.startswith("-"):
            archivos[actual][1].append(ln[1:])
    return archivos


def medir_commit(archivos: dict, perfil: dict) -> dict:
    tocados = set(archivos)
    es_metodo = any(
        p in perfil["metodo_files"] or p.startswith(perfil["metodo_dirs"]) or perfil["historial"].match(p)
        for p in tocados
    )
    quitadas = Counter(
        q.strip() for _, (_, qs) in archivos.items() for q in qs if len(q.strip()) >= MIN_MOVIMIENTO
    )
    cer = cam = mov = 0
    toca_historial = False
    for ruta, (agregadas, _) in sorted(archivos.items()):
        hist = bool(perfil["historial"].match(ruta))
        toca_historial = toca_historial or hist
        for a in agregadas:
            s = a.strip()
            if len(s) >= MIN_MOVIMIENTO and quitadas[s] > 0:
                quitadas[s] -= 1
                mov += chars(a)
                continue
            if hist:
                cer += chars(a)
            else:
                cam += chars(a)
    return {"metodo": es_metodo, "ceremonia": cer, "cambio": cam, "movido": mov, "toca_historial": toca_historial}


def razon(filas: list[dict]) -> float | None:
    tot = sum(f["ceremonia"] + f["cambio"] for f in filas)
    return sum(f["ceremonia"] for f in filas) / tot if tot else None


def bootstrap(filas: list[dict], rng: random.Random) -> list[float]:
    vals = []
    for _ in range(REMUESTREOS):
        r = razon([rng.choice(filas) for _ in filas])
        if r is not None:
            vals.append(r)
    return sorted(vals)


def ic(vals: list[float]) -> tuple[float, float]:
    return vals[int(0.025 * len(vals))], vals[int(0.975 * len(vals)) - 1]


def mediana(xs: list[float]) -> float | None:
    xs = sorted(xs)
    if not xs:
        return None
    m = len(xs) // 2
    return xs[m] if len(xs) % 2 else (xs[m - 1] + xs[m]) / 2


def medir(repo: Path, head: str, perfil: dict) -> tuple[list[dict], dict]:
    shas = git(repo, "rev-list", "--reverse", "--no-merges", head).split()
    raiz = set(git(repo, "rev-list", "--max-parents=0", head).split())
    filas = []
    for sha in shas:
        if sha in raiz:
            continue
        m = medir_commit(diff_commit(repo, sha), perfil)
        if m["metodo"]:
            filas.append({"commit": sha[:7], **m})
    validas = [f for f in filas if f["ceremonia"] + f["cambio"] > 0]
    por_commit = [f["ceremonia"] / (f["ceremonia"] + f["cambio"]) for f in validas]
    resumen = {
        "head": head,
        "commits_no_merge": len(shas),
        "commits_metodo": len(filas),
        "commits_metodo_sin_texto_nuevo": len(filas) - len(validas),
        "commits_metodo_sin_historial": sum(1 for f in filas if not f["toca_historial"]),
        "ceremonia": sum(f["ceremonia"] for f in filas),
        "cambio": sum(f["cambio"] for f in filas),
        "movido": sum(f["movido"] for f in filas),
        "razon_agregada": razon(validas),
        "razon_mediana_por_commit": mediana(por_commit),
    }
    return validas, resumen


def selftest() -> int:
    """Control conocido: tres commits con razon esperada, mas el raiz excluido."""
    perfil = PERFILES["propio"]
    with tempfile.TemporaryDirectory() as d:
        repo = Path(d)
        for args in (("init", "-q"), ("config", "user.email", "t@t"), ("config", "user.name", "t"),
                     ("config", "core.autocrlf", "false")):
            git(repo, *args)
        (repo / "historial").mkdir()
        (repo / "agenda").mkdir()

        def commit(msg: str) -> str:
            git(repo, "add", "-A")
            git(repo, "commit", "-q", "--no-verify", "-m", msg)
            return git(repo, "rev-parse", "HEAD").strip()

        planteo = "Este planteo es largo y se mueve del backlog al historial."
        (repo / "historial/sdd.md").write_text("# H\n", encoding="utf-8")
        (repo / "agenda/MEJORAS-METODO.md").write_text(f"# M\n{planteo}\n", encoding="utf-8")
        (repo / "AGENTS.md").write_text("# A\n", encoding="utf-8")
        commit("raiz")
        # 1. Cambio de metodo con entrada: 10 de ceremonia, 30 de cambio -> 0.25.
        (repo / "AGENTS.md").write_text("# A\n" + "x" * 30 + "\n", encoding="utf-8")
        (repo / "historial/sdd.md").write_text("# H\n" + "y" * 10 + "\n", encoding="utf-8")
        c1 = commit("uno")
        # 2. Solo movimiento: el planteo pasa del backlog al historial -> sin texto nuevo.
        (repo / "agenda/MEJORAS-METODO.md").write_text("# M\n", encoding="utf-8")
        (repo / "historial/sdd.md").write_text("# H\n" + "y" * 10 + "\n" + planteo + "\n", encoding="utf-8")
        c2 = commit("dos")
        # 3. Contenido, no metodo: no entra a la poblacion.
        (repo / "agenda/OTRO.md").write_text("z" * 50 + "\n", encoding="utf-8")
        commit("tres")
        # 4. Solo historial -> 1.0.
        (repo / "historial/sdd.md").write_text("# H\n" + "y" * 10 + "\n" + planteo + "\n" + "w" * 20 + "\n",
                                               encoding="utf-8")
        c4 = commit("cuatro")
        validas, resumen = medir(repo, "HEAD", perfil)
        esperado = {c1[:7]: (10, 30), c4[:7]: (20, 0)}
        obtenido = {f["commit"]: (f["ceremonia"], f["cambio"]) for f in validas}
        fallas = []
        if obtenido != esperado:
            fallas.append(f"commits validos: esperado {esperado}, obtenido {obtenido}")
        if resumen["commits_metodo"] != 3 or resumen["commits_metodo_sin_texto_nuevo"] != 1:
            fallas.append(f"poblacion: {resumen}")
        if resumen["movido"] != chars(planteo):
            fallas.append(f"movido: esperado {chars(planteo)}, obtenido {resumen['movido']}")
        if abs(resumen["razon_agregada"] - 30 / 60) > 1e-9:
            fallas.append(f"razon agregada: esperado 0.5, obtenido {resumen['razon_agregada']}")
        _ = c2
    for f in fallas:
        print("FALLA", f)
    print(f"selftest: {'VERDE' if not fallas else 'ROJO'}")
    return 1 if fallas else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--repo")
    ap.add_argument("--head")
    ap.add_argument("--perfil", choices=sorted(PERFILES))
    ap.add_argument("--detalle", action="store_true")
    ap.add_argument("--repo2")
    ap.add_argument("--head2")
    ap.add_argument("--perfil2", choices=sorted(PERFILES))
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.detalle and a.perfil == "r40":
        print("--detalle no se usa sobre [R40]: fuente reservada, solo agregados", file=sys.stderr)
        return 2
    validas, resumen = medir(Path(a.repo), a.head, PERFILES[a.perfil])
    vals = bootstrap(validas, random.Random(SEMILLA)) if validas else []
    resumen["ic95_razon_agregada"] = ic(vals) if vals else None
    salida = {"resumen": resumen}
    if a.repo2:
        validas2, resumen2 = medir(Path(a.repo2), a.head2, PERFILES[a.perfil2])
        rng = random.Random(SEMILLA)
        difs = []
        for _ in range(REMUESTREOS):
            r1 = razon([rng.choice(validas) for _ in validas])
            r2 = razon([rng.choice(validas2) for _ in validas2])
            if r1 is not None and r2 is not None:
                difs.append(r1 - r2)
        salida["resumen2"] = resumen2
        salida["ic95_diferencia"] = ic(sorted(difs)) if difs else None
    if a.detalle:
        salida["commits"] = validas
    print(json.dumps(salida, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
