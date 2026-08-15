#!/usr/bin/env python3
"""Backstop determinista de la documentacion del repositorio SDD (M-01, M-09, M-10, M-15).

Verifica presencia y forma, NO adecuacion: que cada documento autorado tenga
spec registrada, que las referencias existan y que las reglas del registro se
cumplan mecanicamente. Que una spec describa *bien* a su documento es juicio
humano y queda fuera del alcance de este script (mismo limite declarado por el
proyecto testigo en docs/SDD-ENFORCEMENT.md).

Dos checks son SEÑAL, no veredicto, y por eso emiten WARN: `ssot-collision` y
`normative-block` (M-09) marcan candidatos a duplicacion entre SSOTs para que un
humano los mire. Rozan el limite de arriba a proposito, pero no lo cruzan: no
afirman que haya duplicacion, solo que dos documentos se declaran dueños del
mismo tema. Ambos se validaron reproduciendo los dos casos reales que la Fase 11
corrigio, corriendolos contra el arbol anterior a esa fase.

El check `constitucion` (M-15) cierra el lazo sobre este mismo script: cada
principio de CONSTITUTION.md declara en `Verificador:` que checks lo cubren —o
`ninguno`— y el check falla si nombra uno que este script no emite. Los ids
validos se derivan de la fuente, no de una lista aparte que volveria a poder
divergir. Verifica que el verificador EXISTA, no que ALCANCE: al 2026-08-15
cubre tres de los siete principios, y los otros cuatro declaran `ninguno` a
proposito.

Uso (el nombre del interprete depende de la plataforma: `python`, `python3`
o `py -3`; en POSIX tambien `./tools/check_docs.py` por el shebang):

    <interprete> tools/check_docs.py            # ERROR y WARN, sale 1 si hay ERROR
    <interprete> tools/check_docs.py --strict   # WARN tambien hace salir 1
    <interprete> tools/check_docs.py --quiet    # solo el resumen

Sin dependencias externas: stdlib de Python 3.8+. Las rutas se resuelven contra
la raiz del repo, no contra el directorio de trabajo, asi que puede invocarse
desde cualquier lado.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = "SPECS_REGISTRY.md"
REFERENCIAS = "REFERENCIAS.md"
PROTOCOLO = "AGENTS.md"
CONSTITUCION = "CONSTITUTION.md"

# Directorios que nunca se auditan: material fuente externo y tooling.
SKIP_DIRS = ("fuentes-externas", "tools", ".git")

# Directorios de primer nivel de ESTE repositorio. Sirven para distinguir una ruta
# propia de una mencion a otro proyecto: el testigo tiene directorios homonimos
# (`docs/`, `specs/`, `memory/`) que no deben resolverse contra nuestro disco.
REPO_DIRS = frozenset(
    d.name for d in ROOT.iterdir() if d.is_dir() and not d.name.startswith(".")
)

# Exentos de spec propia por generarse desde un template del proyecto
# (SPECS_REGISTRY.md, seccion "Docs excluidos del registro").
EXEMPT_PATTERNS = (
    re.compile(r"^experimentos/EXPERIMENTO-[^/]+\.md$"),
    re.compile(r"^experimentos/RESULTADO-EXPERIMENTO-[^/]+\.md$"),
)

VALID_SSOT_LEVEL = {"SSOT", "derivado", "operativo"}
VALID_ESTADO = {"Activo", "Borrador", "Deprecado"}

# Claves de bloque de spec: MUST aparecer solo dentro del registro.
SPEC_FIELD_LINE = re.compile(r"^\s*-\s+`(proposito|incluye|excluye|validacion|deriva_de|ssot_level)`\s*:")

EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F0FF\U00002B00-\U00002BFF]"
)

PRECEDENCE_CHAIN = ["CONSTITUTION.md", "SPECS_REGISTRY.md", "AGENTS.md"]

# Spans de codigo inline: dentro de ellos no hay links markdown, pero si rutas.
CODE_SPAN = re.compile(r"`([^`\n]+)`")

# Una ruta escrita en backticks: sin espacios, sin comodines, terminada en .md.
BACKTICK_PATH = re.compile(r"^[\w./-]+\.md$")

# Un id de check tal como se pasa a `rep.error()` / `rep.warn()`: el primer
# argumento literal, que en las llamadas multi-linea cae en el renglon siguiente.
CHECK_ID_CALL = re.compile(r"rep\.(?:error|warn)\(\s*\n?\s*\"([a-z-]+)\"")

# Encabezado de principio en la constitucion: `### VII. Titulo`.
PRINCIPIO = re.compile(r"^###\s+([IVXLC]+)\.\s+(.+)$")

# Campo que declara con que se verifica un principio (M-15).
VERIFICADOR = re.compile(r"^-\s+\*\*Verificador:\*\*\s*(.+)$")

STOPWORDS = frozenset(
    "de del la el los las un una y o en por para con que su sus al es son no"
    " este esta esto sobre entre como cada".split()
)


class Report:
    def __init__(self) -> None:
        self.items: list[tuple[str, str, str, str]] = []

    def add(self, severity: str, check: str, where: str, msg: str) -> None:
        self.items.append((severity, check, where, msg))

    def error(self, check: str, where: str, msg: str) -> None:
        self.add("ERROR", check, where, msg)

    def warn(self, check: str, where: str, msg: str) -> None:
        self.add("WARN", check, where, msg)

    @property
    def errors(self) -> int:
        return sum(1 for i in self.items if i[0] == "ERROR")

    @property
    def warns(self) -> int:
        return sum(1 for i in self.items if i[0] == "WARN")


def docs() -> list[str]:
    """Todos los .md autorados del repo, en rutas relativas POSIX."""
    out = []
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        if rel.split("/")[0] in SKIP_DIRS:
            continue
        out.append(rel)
    return out


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def parse_registry() -> dict[str, dict]:
    """Devuelve {path_declarado: {campo: valor}} leyendo los bloques del registro.

    Los campos multi-linea (`incluye`, `excluye`, `validacion`) guardan ademas sus
    viñetas bajo la clave `<campo>_items`, que `ssot-collision` necesita.
    """
    specs: dict[str, dict] = {}
    current: list[str] = []
    field = ""
    for line in read(REGISTRY).splitlines():
        if line.startswith("### "):
            current, field = [], ""
            continue
        m = re.match(r"^-\s+`path`:\s+`([^`]+)`", line)
        if m:
            current.append(m.group(1))
            specs.setdefault(m.group(1), {})
            field = ""
            continue
        m = re.match(r"^-\s+`([a-z_]+)`:\s*(.*)$", line)
        if m and current:
            field, value = m.group(1), m.group(2).strip()
            for p in current:
                specs[p][field] = value
            continue
        m = re.match(r"^\s{2,}-\s+(.+)$", line)
        if m and current and field:
            for p in current:
                specs[p].setdefault(field + "_items", []).append(m.group(1).strip())
            continue
        if not line.strip():
            field = ""
    return specs


def parse_ssot_table() -> list[tuple[str, list[str]]]:
    """Devuelve [(concepto, [paths SSOT])] leyendo la tabla SSOT del registro."""
    rows: list[tuple[str, list[str]]] = []
    inside = False
    for line in read(REGISTRY).splitlines():
        if line.startswith("## "):
            inside = line.startswith("## Tabla SSOT")
            continue
        if not inside or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3 or cells[0].startswith("-") or cells[0] == "Linea":
            continue
        rows.append((cells[1], re.findall(r"`([^`]+\.md)`", cells[2])))
    return rows


def tokens(text: str) -> set[str]:
    """Palabras significativas, sin tildes ni stopwords, para comparar temas."""
    plain = unicodedata.normalize("NFKD", text.lower())
    plain = "".join(c for c in plain if not unicodedata.combining(c))
    return {t for t in re.findall(r"[a-z0-9]+", plain) if len(t) > 2 and t not in STOPWORDS}


def is_exempt(rel: str) -> bool:
    return any(p.match(rel) for p in EXEMPT_PATTERNS)


def check_spec_coverage(rep: Report, specs: dict, all_docs: list[str]) -> None:
    """Todo doc autorado tiene spec, o cae en una exencion declarada."""
    for rel in all_docs:
        if rel not in specs and not is_exempt(rel):
            rep.error("spec-coverage", rel, "documento autorado sin spec registrada ni exencion declarada")
    for path in specs:
        if not (ROOT / path).exists():
            rep.error("spec-coverage", REGISTRY, f"la spec declara `{path}`, que no existe en disco")


def check_spec_fields(rep: Report, specs: dict) -> None:
    """Valores validos de ssot_level/estado y coherencia de deriva_de."""
    for path, fields in specs.items():
        level = fields.get("ssot_level", "").strip("`")
        if level and level not in VALID_SSOT_LEVEL:
            rep.error("spec-fields", path, f"ssot_level invalido: {level!r}")
        estado = fields.get("estado", "")
        if estado:
            token = re.match(r"`?([A-Za-zñáéíóú]+)`?", estado)
            if token and token.group(1) not in VALID_ESTADO:
                rep.error("spec-fields", path, f"estado invalido: {token.group(1)!r}")
        if level == "derivado" and "deriva_de" not in fields:
            rep.error("spec-fields", path, "ssot_level derivado sin campo deriva_de")
        origen = fields.get("deriva_de", "").strip().strip("`")
        if origen:
            if not (ROOT / origen).exists():
                rep.error("spec-fields", path, f"deriva_de apunta a `{origen}`, que no existe")
            elif origen == path:
                rep.error("spec-fields", path, "deriva_de apunta al propio documento (ciclo)")
            elif origen not in specs:
                rep.error("spec-fields", path, f"deriva_de apunta a `{origen}`, que no tiene spec registrada")
            else:
                origen_level = specs[origen].get("ssot_level", "").strip("`")
                if origen_level not in ("SSOT", "derivado"):
                    rep.error(
                        "spec-fields",
                        path,
                        f"deriva_de apunta a `{origen}` con ssot_level `{origen_level or '(vacio)'}` "
                        "(MUST ser SSOT o derivado)",
                    )
        if "proposito" not in fields:
            rep.warn("spec-fields", path, "spec sin campo proposito")


def check_deriva_cycles(rep: Report, specs: dict) -> None:
    """La cadena deriva_de no puede tener ciclos."""
    edges = {p: f["deriva_de"].strip().strip("`") for p, f in specs.items() if f.get("deriva_de")}
    for start in edges:
        seen, node = [start], edges[start]
        while node in edges:
            if node in seen:
                rep.error("deriva-cycle", start, f"ciclo de deriva_de: {' -> '.join(seen + [node])}")
                break
            seen.append(node)
            node = edges[node]


def check_links(rep: Report, all_docs: list[str]) -> None:
    """Links markdown internos a .md que existan.

    Ignora bloques de codigo y spans inline: ahi un `[texto](destino.md)` es la
    sintaxis citada como ejemplo, no un link. Las rutas escritas en backticks las
    verifica `check_backtick_paths`, que sabe resolverlas.
    """
    for rel in all_docs:
        base = os.path.dirname(rel)
        body = "\n".join(strip_code_fences(read(rel).splitlines()))
        body = CODE_SPAN.sub(" ", body)
        for m in re.finditer(r"\]\(([^)\s]+\.md)(#[^)]*)?\)", body):
            target = m.group(1)
            if target.startswith(("http://", "https://")):
                continue
            resolved = os.path.normpath(os.path.join(base, target))
            if not (ROOT / resolved).exists():
                rep.error("links", rel, f"link roto: {target}")


def resolve_ref(rel: str, ref: str) -> tuple[str, bool]:
    """Resuelve una ruta citada en `rel`. Devuelve (ruta, verificable). Ver M-10.

    Tres casos: prefijo relativo explicito se resuelve contra el documento; primer
    segmento que es directorio de este repo, contra la raiz; cualquier otro primer
    segmento pertenece a otro repositorio y no se verifica.
    """
    if "fuentes-externas" in ref.split("/"):
        return ref, False
    if ref.startswith(("./", "../")):
        resolved = os.path.normpath(os.path.join(os.path.dirname(rel), ref))
        # Un `../` que sale de la raiz apunta a un repo hermano: no es nuestro.
        return resolved, not resolved.startswith("..")
    if ref.split("/")[0] in REPO_DIRS:
        return os.path.normpath(ref), True
    return ref, False


def check_backtick_paths(rep: Report, all_docs: list[str]) -> None:
    """Las rutas escritas en backticks existen (M-10).

    En este repositorio la mayoria de las referencias se escriben asi, no como link
    markdown, y hasta la Fase 11 nadie las verificaba. Un backtick sin barra es una
    mencion por nombre, no una ruta, y se ignora.
    """
    for rel in all_docs:
        body = "\n".join(strip_code_fences(read(rel).splitlines()))
        for m in CODE_SPAN.finditer(body):
            ref = m.group(1).strip()
            if "/" not in ref or not BACKTICK_PATH.match(ref):
                continue
            resolved, verifiable = resolve_ref(rel, ref)
            if verifiable and not (ROOT / resolved).exists():
                rep.error("rutas", rel, f"ruta inexistente: {ref}")


def check_ssot_collision(rep: Report, specs: dict, ssot_rows: list) -> None:
    """Señal: dos specs que se declaran dueñas del mismo tema (M-09).

    Cruza el concepto de cada fila de la tabla SSOT contra las viñetas de `incluye`
    de las demas specs. Es señal para revision humana, no veredicto: que una spec
    mencione un tema ajeno puede ser legitimo si lo referencia en vez de contenerlo.
    """
    for concepto, ssot_paths in ssot_rows:
        tema = tokens(concepto)
        if len(tema) < 2:
            continue
        for path, fields in specs.items():
            if path in ssot_paths:
                continue
            for item in fields.get("incluye_items", []):
                if tema <= tokens(item):
                    rep.warn(
                        "ssot-collision",
                        path,
                        f"`incluye` cubre «{concepto}», cuyo SSOT es {' / '.join(ssot_paths) or 'otro'}: "
                        f"«{item}»",
                    )
                    break


def normative_fields() -> set[str]:
    """Primeras palabras de los campos del bloque `[SDD-Check]`, leidas de AGENTS.md."""
    body = read(PROTOCOLO)
    block = re.search(r"\[SDD-Check\]\n(.*?)```", body, re.S)
    if not block:
        return set()
    heads = set()
    for line in block.group(1).splitlines():
        m = re.match(r"^-\s+([A-Za-zÁÉÍÓÚáéíóúñ/]+)", line)
        if m:
            heads |= tokens(m.group(1))
    return heads


def check_normative_block(rep: Report, all_docs: list[str], heads: set[str]) -> None:
    """Señal: la definicion del bloque `[SDD-Check]` reproducida fuera de su SSOT (M-09).

    Distingue instancia de definicion. Una entrega que cierra con el bloque lleno es
    legitima en cualquier documento y lleva el literal `[SDD-Check]` al lado; lo que
    no lo es, es enumerar los campos como definicion — el caso corregido en la Fase 11.
    """
    if len(heads) < 3:
        return
    for rel in all_docs:
        if rel == PROTOCOLO or rel.startswith(("templates/", "historial/")):
            continue
        lines = read(rel).splitlines()
        for n, line in enumerate(lines):
            m = re.match(r"^\s*-\s+([A-Za-zÁÉÍÓÚáéíóúñ/]+)", line)
            if not m or not (tokens(m.group(1)) & heads):
                continue
            window = lines[n : n + 10]
            found = {
                t
                for w in window
                for mm in [re.match(r"^\s*-\s+([A-Za-zÁÉÍÓÚáéíóúñ/]+)", w)]
                if mm
                for t in tokens(mm.group(1)) & heads
            }
            # La ventana hacia atras cubre un bloque entero: sus 8 campos mas el titulo.
            if len(found) >= 3 and not any("[SDD-Check]" in w for w in lines[max(0, n - 20) : n + 10]):
                rep.warn(
                    "normative-block",
                    f"{rel}:{n + 1}",
                    f"enumera campos del bloque `[SDD-Check]` fuera de {PROTOCOLO}: "
                    f"{', '.join(sorted(found))}",
                )
                break


def check_references(rep: Report, all_docs: list[str]) -> None:
    """Toda [Rxx] usada existe en el catalogo, y el catalogo no tiene duplicados."""
    catalog_text = read(REFERENCIAS)
    declared = re.findall(r"^-\s+\[(R\d{2})\]", catalog_text, re.M)
    dupes = {r for r in declared if declared.count(r) > 1}
    for r in sorted(dupes):
        rep.error("referencias", REFERENCIAS, f"id duplicado en el catalogo: [{r}]")
    known = set(declared)
    for rel in all_docs:
        if rel == REFERENCIAS:
            continue
        for r in sorted(set(re.findall(r"\[(R\d{2})\]", read(rel)))):
            if r not in known:
                rep.error("referencias", rel, f"cita [{r}] sin entrada en {REFERENCIAS}")


def check_excluded_fields_in_tables(rep: Report, specs: dict, all_docs: list[str]) -> None:
    """Un doc no reproduce en tabla un campo que su propia spec excluye (M-14 y su correccion).

    Generico: no hardcodea que documento aplica. Lee los `excluye_items` de cada
    spec, busca nombres de campo citados en backticks (ej. `estado`, `ssot_level`)
    y, si son `estado` o `ssot_level`, verifica que ninguna celda de tabla del
    documento sea un valor valido de ese campo (VALID_ESTADO / VALID_SSOT_LEVEL).
    """
    for path, fields in specs.items():
        if path not in all_docs:
            continue
        excluded = {
            token
            for item in fields.get("excluye_items", [])
            for token in re.findall(r"`([a-z_]+)`", item)
        }
        checks = [f for f in ("estado", "ssot_level") if f in excluded]
        if not checks:
            continue
        for n, line in enumerate(read(path).splitlines(), 1):
            if not line.strip().startswith("|"):
                continue
            for cell in (c.strip().strip("*") for c in line.strip().strip("|").split("|")):
                if "estado" in checks and cell in VALID_ESTADO:
                    rep.error("excluded-field", f"{path}:{n}", f"tabla anota `estado` ({cell}); excluido por su propia spec")
                if "ssot_level" in checks and cell in VALID_SSOT_LEVEL:
                    rep.error("excluded-field", f"{path}:{n}", f"tabla anota `ssot_level`/rol ({cell}); excluido por su propia spec")


def check_scope_single_home(rep: Report, all_docs: list[str]) -> None:
    """El alcance (campos de spec) vive solo en el registro (regla del Principio I)."""
    for rel in all_docs:
        if rel == REGISTRY:
            continue
        for n, line in enumerate(read(rel).splitlines(), 1):
            if SPEC_FIELD_LINE.match(line):
                rep.error("scope-home", f"{rel}:{n}", "campo de spec fuera de SPECS_REGISTRY.md")


def strip_code_fences(lines: list[str]) -> list[str]:
    """Reemplaza por vacio el contenido de los bloques ```...```."""
    out, inside = [], False
    for line in lines:
        if line.lstrip().startswith("```"):
            inside = not inside
            out.append("")
            continue
        out.append("" if inside else line)
    return out


def check_precedence(rep: Report, all_docs: list[str]) -> None:
    """Heuristica: quien invoca la precedencia MUST nombrar la constitucion.

    Atrapa la deriva de la Fase 8, donde cuatro documentos declaraban la cadena
    sin el eslabon nuevo. Es heuristica, no prueba: mira una ventana de texto
    alrededor de cada mencion, ignora bloques de codigo y acepta tanto el nombre
    de archivo como la palabra "constitucion".
    """
    for rel in all_docs:
        if rel.startswith("historial/"):  # registro cronologico: describe estados pasados
            continue
        lines = strip_code_fences(read(rel).splitlines())
        for n, line in enumerate(lines):
            if "recedencia" not in line:
                continue
            window = "\n".join(lines[max(0, n - 4) : n + 12])
            names_registry = PRECEDENCE_CHAIN[1] in window
            names_constitution = PRECEDENCE_CHAIN[0] in window or re.search(
                r"constituc", window, re.IGNORECASE
            )
            if names_registry and not names_constitution:
                rep.error(
                    "precedencia",
                    f"{rel}:{n + 1}",
                    "invoca la cadena de precedencia sin nombrar la constitucion",
                )


def emitted_check_ids() -> set[str]:
    """Los ids de check que este script realmente emite, leidos de su propia fuente.

    Se derivan en vez de mantenerse en una lista aparte a proposito: una lista a
    mano habria vuelto a introducir, un nivel mas arriba, la misma deriva que
    `constitucion` existe para detectar — un nombre declarado que ya no
    corresponde a nada que corra.
    """
    return set(CHECK_ID_CALL.findall(Path(__file__).read_text(encoding="utf-8")))


def check_constitucion(rep: Report) -> None:
    """Cada principio declara `Verificador:` con checks existentes o `ninguno` (M-15).

    Portado de sdd-first [R39] (`software/ANALISIS-SDD-FIRST.md`, C1), donde el
    principio declara el paso de pipeline que lo activa y el pipeline verifica
    que ese paso este cableado. Lo que produce no es enforcement universal —hay
    principios que un repositorio documental no puede mecanizar— sino
    visibilidad de cual tiene mecanismo y cual depende de que alguien se acuerde.

    Limite, en la linea del resto del script: verifica que el verificador
    declarado EXISTA, no que ALCANCE para sostener el principio. Que
    `spec-coverage` baste para «documento autorado, spec registrada» es juicio
    humano y queda fuera.
    """
    ids = emitted_check_ids()
    if len(ids) < 10:
        rep.error(
            "constitucion",
            "tools/check_docs.py",
            f"solo se derivaron {len(ids)} ids de check de la fuente; revisar CHECK_ID_CALL",
        )
        return

    lines = read(CONSTITUCION).splitlines()
    principios: list[tuple[str, int, str | None]] = []
    titulo, inicio, valor = "", 0, None
    for n, line in enumerate(lines, start=1):
        m = PRINCIPIO.match(line)
        if m:
            if titulo:
                principios.append((titulo, inicio, valor))
            titulo, inicio, valor = f"{m.group(1)}. {m.group(2)}", n, None
            continue
        if line.startswith("## ") and titulo:
            principios.append((titulo, inicio, valor))
            titulo, valor = "", None
            continue
        m = VERIFICADOR.match(line)
        if m and titulo:
            valor = m.group(1).strip()
    if titulo:
        principios.append((titulo, inicio, valor))

    if not principios:
        rep.error("constitucion", CONSTITUCION, "no se encontro ningun principio (`### N. Titulo`)")
        return

    for titulo, n, valor in principios:
        where = f"{CONSTITUCION}:{n}"
        if valor is None:
            rep.error("constitucion", where, f"principio «{titulo}» no declara `Verificador:`")
            continue
        # Solo el segmento anterior al em dash declara; lo que sigue es la nota
        # de alcance, prosa libre donde un backtick no nombra un check.
        declaracion = valor.split("—")[0]
        nombrados = [n for n in re.findall(r"`([a-z-]+)`", declaracion) if n != "ninguno"]
        declara_ninguno = re.search(r"\bninguno\b", declaracion, re.IGNORECASE) is not None
        if nombrados and declara_ninguno:
            rep.error("constitucion", where, f"principio «{titulo}» declara `ninguno` y checks a la vez")
            continue
        if not nombrados and not declara_ninguno:
            rep.error(
                "constitucion",
                where,
                f"principio «{titulo}»: `Verificador:` no nombra ningun check ni declara `ninguno`",
            )
            continue
        for nombre in nombrados:
            if nombre not in ids:
                rep.error(
                    "constitucion",
                    where,
                    f"principio «{titulo}» declara el check `{nombre}`, que este script no emite",
                )


def check_no_emoji(rep: Report, all_docs: list[str]) -> None:
    """Regla global: sin emoticones en documentos de contenido."""
    for rel in all_docs:
        hits = sorted(set(EMOJI.findall(read(rel))))
        if hits:
            rep.warn("emoji", rel, f"emoticones presentes: {' '.join(hits)}")


def check_ssot_table(rep: Report, specs: dict, ssot_rows: list) -> None:
    """Validar que los paths en la tabla SSOT existan y tengan spec (M-11)."""
    for concepto, paths in ssot_rows:
        for path in paths:
            if not (ROOT / path).exists():
                rep.error("ssot-table", REGISTRY, f"path en tabla SSOT no existe en disco; corregir path o crear archivo: {path}")
            elif path not in specs:
                rep.error("ssot-table", REGISTRY, f"path en tabla SSOT no tiene spec registrada; crear entrada en SPECS_REGISTRY.md: {path}")


def check_file_hygiene(rep: Report, all_docs: list[str]) -> None:
    """Higiene de archivo: sin CRLF, sin BOM, y con newline final (M-12)."""
    for rel in all_docs:
        path = ROOT / rel
        if not path.exists():
            continue
        with open(path, "rb") as f:
            content = f.read()
        if not content:
            continue
        if b"\r\n" in content:
            rep.error("higiene", rel, "tiene finales de linea CRLF; convertir a LF")
        if content.startswith(b"\xef\xbb\xbf"):
            rep.error("higiene", rel, "tiene BOM (Byte Order Mark); guardar como UTF-8 sin BOM")
        if not content.endswith(b"\n"):
            rep.error("higiene", rel, "no termina en salto de linea; agregar newline al final")


def main() -> int:
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true", help="los WARN tambien fallan")
    ap.add_argument("--quiet", action="store_true", help="solo el resumen")
    args = ap.parse_args()

    rep = Report()
    all_docs = docs()
    specs = parse_registry()

    check_spec_coverage(rep, specs, all_docs)
    check_spec_fields(rep, specs)
    check_deriva_cycles(rep, specs)
    check_links(rep, all_docs)
    check_backtick_paths(rep, all_docs)
    check_references(rep, all_docs)
    check_scope_single_home(rep, all_docs)
    check_excluded_fields_in_tables(rep, specs, all_docs)
    check_ssot_collision(rep, specs, parse_ssot_table())
    check_normative_block(rep, all_docs, normative_fields())
    check_precedence(rep, all_docs)
    check_constitucion(rep)
    check_no_emoji(rep, all_docs)
    check_ssot_table(rep, specs, parse_ssot_table())
    check_file_hygiene(rep, all_docs)

    if not args.quiet:
        for severity, check, where, msg in sorted(rep.items, key=lambda i: (i[0] != "ERROR", i[1], i[2])):
            print(f"{severity:5} [{check}] {where}: {msg}")
        if rep.items:
            print()

    print(f"{len(all_docs)} documentos, {len(specs)} specs — {rep.errors} ERROR, {rep.warns} WARN")
    if rep.errors or (args.strict and rep.warns):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
