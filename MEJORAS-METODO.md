# Mejoras al método SDD del repositorio

Backlog de cambios al **método** —protocolo, registro, constitución, templates, tooling de verificación— del propio repositorio. No es agenda de investigación.

## Criterio de separación

Aplicación del Principio VI (`CONSTITUTION.md`, separación método/contenido):

| | `MEJORAS-METODO.md` (este doc) | `06-BACKLOG-INVESTIGACION-FUTURA.md` |
|---|---|---|
| Naturaleza | cambio al método del repo | pregunta abierta sobre SDD |
| Se cierra con | una entrada en `historial/sdd.md` | evidencia (experimento, análisis) |
| Estado posible | `Propuesta` / `Aprobada` / `Hecha` / `Descartada` | prioridad alta / media / exploratoria |

Un item puede tener contraparte del otro lado: implementar una mejora de método MAY producir dato para una pregunta de investigación, pero son entradas distintas y se cierran por separado. Una mejora `Propuesta` que se aprueba no se mueve de documento: cambia de estado.

## Estado

| ID | Mejora | Prioridad | Estado | Origen | Destino |
|---|---|---|---|---|---|
| M-01 | Backstop determinista de documentación (`check_docs.py`) | alta | **Hecha** (Fase 10) | testigo `tools/check_traceability.py` | `tools/check_docs.py` + `AGENTS.md` |
| M-02 | Gate de autoría documental (`.sdd/current-doc` + hook) | alta | Aprobada | testigo `tools/sdd_gate.py` | script nuevo + `.claude/settings.json` |
| M-03 | Playbooks agnósticos de asistente (`analyze`, `clarify`) | media | Propuesta | testigo `docs/playbooks/` | `playbooks/` + wrappers |
| M-04 | Formato y compactación de documentos | media | Propuesta | testigo `docs/SPEC-FORMAT.md` | doc nuevo + migración |
| M-05 | Limpiar encabezados que restatan su alcance | baja | Aprobada | regla de alcance, Fase 8 | docs varios, oportunística |
| M-06 | Modelo de confianza confirmado/inferido/gap | media | Propuesta | [R25] | convención de Línea A |
| M-07 | Revisar la premisa "sin CI" tras el versionado | baja | Aprobada | Fase 8 | `AGENTS.md`, `IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md` |
| M-08 | Decidir qué hacer con los emoticones de `PREREG-B7.md` | baja | Propuesta | Fase 8 | decisión del usuario |

---

## M-01 — Backstop determinista de documentación

Script local (sin CI) que verifica lo que hoy son checkboxes aspiracionales del campo `validacion`: todo `.md` autorado tiene spec registrada o cae en una exención declarada; el registro no apunta a archivos inexistentes; links internos vivos; `[Rxx]` usadas ⊆ `REFERENCIAS.md`; `deriva_de` existe y no es circular; `estado` y `ssot_level` con valores válidos; cadena de precedencia coherente entre los documentos que la declaran.

Es la capa 2 del enforcement de tres capas del testigo (`docs/SDD-ENFORCEMENT.md`), portada a un repo documental. Límite heredado y explícito: verifica **presencia y forma, no adecuación** — que un documento tenga spec no dice que la spec lo describa bien.

Contraparte de investigación: `06-BACKLOG` exploratoria «evaluación automática parcial sin CI», y prioridad alta «umbral de control manual a automatizado». Ejecutar M-01 produce dato para ambas; no las cierra.

**Hecha el 2026-07-31** (`tools/check_docs.py`, Fase 10). Ocho checks, dos severidades, sin dependencias externas. Primera corrida sobre 41 documentos: 6 ERROR, de los cuales **2 eran deriva real** (`ANALISIS-SPEC-KIT.md` C4 y `templates/RESULTADO-EXPERIMENTO.md`, ambos describiendo la precedencia sin la constitución, un día después de haberla creado) y 4 falsos positivos que obligaron a afinar la heurística. Queda 1 WARN vivo a propósito: los emoticones de `PREREG-B7.md`, que son M-08.

Pendiente evaluado y no hecho: cablearlo a `pre-commit` (requiere decidir M-02 primero) y un check del criterio de separación método/investigación, que hoy nada verifica.

## M-02 — Gate de autoría documental

Declaración de la spec que gobierna la edición (`.sdd/current-doc`) más un hook `PreToolUse` que bloquea editar un `.md` de contenido sin esa declaración, con chequeo de mtime: la spec MUST haberse editado después de declararse. Reusa `tools/sdd_gate.py` del testigo, que ya separa decisión de transporte (stdin JSON / argv / env) y por lo tanto no queda atado a Claude Code.

**Requisito de diseño no negociable: fail-closed.** El gate del testigo terminaba en `[ -f "$PYBIN" ] || exit 0` y, sin intérprete, permitía la edición en silencio; durante todo B-07 el enforcement estuvo caído sin que nadie lo notara. Ver `06-BACKLOG` prioridad alta #4, que es la pregunta de investigación asociada.

Reserva: en un repo documental la fricción puede ser desproporcionada. Conviene medirla, no asumirla.

## M-03 — Playbooks agnósticos de asistente

Procedimiento neutro en `playbooks/{analyze,clarify}.md`, envuelto por wrappers finos (`.claude/skills/`, `.opencode/command/`) que no duplican el contenido. Adaptados a documentos: `analyze` = consistencia doc↔SSOT, afirmaciones sin `[Rxx]`, contradicciones entre SSOTs activos; `clarify` = resolver `[NEEDS CLARIFICATION]` abiertos.

Cierra una incoherencia del proyecto: investiga SDD multi-asistente y en la práctica su tooling es Claude-only.

## M-04 — Formato y compactación de documentos

Convención de formato con resumen ejecutivo obligatorio a partir de cierto tamaño y migración oportunística. Candidatos por tamaño: `SPECS_REGISTRY.md`, `experimentos/PRUEBA-REGENERABILIDAD-B7.md`, `experimentos/PRUEBA-OBSERVACIONAL-B7.md`. En el testigo la reescritura compacta de una spec dio −46% sin pérdida de contenido normativo.

## M-05 — Encabezados que restatan su alcance

La regla de alcance en un solo lugar (`SPECS_REGISTRY.md` §Reglas globales) admite una línea de identidad en el encabezado, no la enumeración de `incluye`/`excluye`. Caso conocido: `ESCENARIOS-QUE-JUSTIFICAN-SDD.md`. Migración al tocar cada documento, sin barrido masivo.

## M-06 — Modelo de confianza confirmado/inferido/gap

Clasificar cada afirmación como *confirmada* (evidencia directa), *inferida* (patrón, no certeza) o *gap* (requiere validación humana) [R25]. Es una graduación más fina que el binario actual (`[Rxx]` vs. `[NEEDS CLARIFICATION]`). Evaluar costo de mantenimiento antes de adoptar: la propia fuente advierte que la trazabilidad tiene costo. Migrado desde `06-BACKLOG` §Enriquecimientos R25/R30, donde convivía con dos candidatos de contenido que se quedan allá.

## M-07 — Revisar la premisa "sin CI"

`AGENTS.md` e `IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md` describen un contexto sin CI. Sigue siendo cierto, pero desde 2026-07-31 hay git, y eso habilita `pre-commit` como sustrato tool-agnóstico para M-01 y M-02. Revisar ambos documentos cuando esas mejoras se implementen, no antes.

## M-08 — Emoticones en `PREREG-B7.md`

El documento viola la regla global «sin emoticones» pero está **pre-registrado y sellado**. Editarlo post-sello tiene implicancias metodológicas (Principio V). Decisión pendiente del usuario: corregir con enmienda fechada, o declarar excepción permanente para documentos sellados.
