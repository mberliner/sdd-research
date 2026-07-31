#!/usr/bin/env python3
"""Backstop determinista de la documentacion del repositorio SDD (M-01).

Verifica presencia y forma, NO adecuacion: que cada documento autorado tenga
spec registrada, que las referencias existan y que las reglas del registro se
cumplan mecanicamente. Que una spec describa *bien* a su documento es juicio
humano y queda fuera del alcance de este script (mismo limite declarado por el
proyecto testigo en docs/SDD-ENFORCEMENT.md).

Uso:
    python3 tools/check_docs.py            # ERROR y WARN, sale 1 si hay ERROR
    python3 tools/check_docs.py --strict   # WARN tambien hace salir 1
    python3 tools/check_docs.py --quiet    # solo el resumen

Sin dependencias externas: stdlib de Python 3.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = "SPECS_REGISTRY.md"
REFERENCIAS = "REFERENCIAS.md"

# Directorios que nunca se auditan: material fuente externo y tooling.
SKIP_DIRS = ("fuentes-externas", "tools", ".git")

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


def parse_registry() -> dict[str, dict[str, str]]:
    """Devuelve {path_declarado: {campo: valor}} leyendo los bloques del registro."""
    specs: dict[str, dict[str, str]] = {}
    current: list[str] = []
    for line in read(REGISTRY).splitlines():
        if line.startswith("### "):
            current = []
            continue
        m = re.match(r"^-\s+`path`:\s+`([^`]+)`", line)
        if m:
            current.append(m.group(1))
            specs.setdefault(m.group(1), {})
            continue
        m = re.match(r"^-\s+`([a-z_]+)`:\s*(.*)$", line)
        if m and current:
            field, value = m.group(1), m.group(2).strip()
            for p in current:
                specs[p][field] = value
    return specs


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
    """Links markdown internos a .md que existan."""
    for rel in all_docs:
        base = os.path.dirname(rel)
        for m in re.finditer(r"\]\(([^)\s]+\.md)(#[^)]*)?\)", read(rel)):
            target = m.group(1)
            if target.startswith(("http://", "https://")):
                continue
            resolved = os.path.normpath(os.path.join(base, target))
            if not (ROOT / resolved).exists():
                rep.error("links", rel, f"link roto: {target}")


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


def check_no_emoji(rep: Report, all_docs: list[str]) -> None:
    """Regla global: sin emoticones en documentos de contenido."""
    for rel in all_docs:
        hits = sorted(set(EMOJI.findall(read(rel))))
        if hits:
            rep.warn("emoji", rel, f"emoticones presentes: {' '.join(hits)}")


def main() -> int:
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
    check_references(rep, all_docs)
    check_scope_single_home(rep, all_docs)
    check_precedence(rep, all_docs)
    check_no_emoji(rep, all_docs)

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
