# Mejoras al método SDD del repositorio

Backlog de cambios al **método** —protocolo, registro, constitución, templates, tooling de verificación— del propio repositorio. No es agenda de investigación.

## Criterio de separación

Aplicación del Principio VI (`../CONSTITUTION.md`, separación método/contenido):

| | `MEJORAS-METODO.md` (este doc) | `BACKLOG-INVESTIGACION.md` |
|---|---|---|
| Naturaleza | cambio al método del repo | pregunta abierta sobre SDD |
| Se cierra con | una entrada en `../historial/sdd.md` | evidencia (experimento, análisis) |
| Estado posible | `Propuesta` / `Aprobada` / `Hecha` / `Descartada` | prioridad alta / media / exploratoria |

Un item puede tener contraparte del otro lado: implementar una mejora de método MAY producir dato para una pregunta de investigación, pero son entradas distintas y se cierran por separado. Una mejora `Propuesta` que se aprueba no se mueve de documento: cambia de estado.

## Estado

| ID | Mejora | Prioridad | Estado | Origen | Destino |
|---|---|---|---|---|---|
| M-01 | Backstop determinista de documentación (`check_docs.py`) | alta | **Hecha** (Fase 10) | testigo `../tools/check_traceability.py` | `../tools/check_docs.py` + `../AGENTS.md` |
| M-02 | Gate de autoría documental (`.sdd/current-doc` + hook) | alta | Aprobada | testigo `../tools/sdd_gate.py` | script nuevo + `.claude/settings.json` |
| M-03 | Playbooks agnósticos de asistente (`analyze`, `clarify`) | media | Propuesta | testigo `docs/playbooks/` | `playbooks/` + wrappers |
| M-04 | Formato y compactación de documentos | media | Propuesta | testigo `docs/SPEC-FORMAT.md` | doc nuevo + migración |
| M-05 | Limpiar encabezados que restatan su alcance | baja | Aprobada | regla de alcance, Fase 8 | docs varios, oportunística |
| M-06 | Modelo de confianza confirmado/inferido/gap | media | Propuesta | [R25] | convención de Línea A |
| M-07 | Revisar la premisa "sin CI" tras el versionado | baja | Aprobada | Fase 8 | `../AGENTS.md`, `../comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md` |
| M-08 | Decidir qué hacer con los emoticones de `PREREG-B7.md` | baja | Propuesta | Fase 8 | decisión del usuario |
| M-09 | Señales de duplicación entre SSOTs (`ssot-collision`, `normative-block`) | alta | **Hecha** (Fase 12) | Fase 11 | `../tools/check_docs.py` |
| M-10 | Verificar rutas escritas en backticks, no solo links markdown | alta | **Hecha** (Fase 12) | Fase 11 | `../tools/check_docs.py` |
| M-11 | Validar la tabla SSOT contra el disco y contra las specs | media | Aprobada (diferida) | Fase 11 | `../tools/check_docs.py` |
| M-12 | Higiene de archivo: CRLF mezclado, BOM, newline final | media | Aprobada (diferida) | Fase 11 | `../tools/check_docs.py` |
| M-13 | `deriva_de` apunta a documentos que no son SSOT | media | Propuesta | relevamiento 2026-08-02 | `../SPECS_REGISTRY.md` + `../tools/check_docs.py` |

---

## M-01 — Backstop determinista de documentación

Script local (sin CI) que verifica lo que hoy son checkboxes aspiracionales del campo `validacion`: todo `.md` autorado tiene spec registrada o cae en una exención declarada; el registro no apunta a archivos inexistentes; links internos vivos; `[Rxx]` usadas ⊆ `../REFERENCIAS.md`; `deriva_de` existe y no es circular; `estado` y `ssot_level` con valores válidos; cadena de precedencia coherente entre los documentos que la declaran.

Es la capa 2 del enforcement de tres capas del testigo (`docs/SDD-ENFORCEMENT.md`), portada a un repo documental. Límite heredado y explícito: verifica **presencia y forma, no adecuación** — que un documento tenga spec no dice que la spec lo describa bien.

Contraparte de investigación: `BACKLOG-INVESTIGACION` exploratoria «evaluación automática parcial sin CI», y prioridad alta «umbral de control manual a automatizado». Ejecutar M-01 produce dato para ambas; no las cierra.

**Hecha el 2026-07-31** (`../tools/check_docs.py`, Fase 10). Ocho checks, dos severidades, sin dependencias externas. Primera corrida sobre 41 documentos: 6 ERROR, de los cuales **2 eran deriva real** (`ANALISIS-SPEC-KIT.md` C4 y `../templates/RESULTADO-EXPERIMENTO.md`, ambos describiendo la precedencia sin la constitución, un día después de haberla creado) y 4 falsos positivos que obligaron a afinar la heurística. Queda 1 WARN vivo a propósito: los emoticones de `PREREG-B7.md`, que son M-08.

Pendiente evaluado y no hecho: cablearlo a `pre-commit` (requiere decidir M-02 primero) y un check del criterio de separación método/investigación, que hoy nada verifica.

## M-02 — Gate de autoría documental

Declaración de la spec que gobierna la edición (`.sdd/current-doc`) más un hook `PreToolUse` que bloquea editar un `.md` de contenido sin esa declaración, con chequeo de mtime: la spec MUST haberse editado después de declararse. Reusa `../tools/sdd_gate.py` del testigo, que ya separa decisión de transporte (stdin JSON / argv / env) y por lo tanto no queda atado a Claude Code.

**Requisito de diseño no negociable: fail-closed.** El gate del testigo terminaba en `[ -f "$PYBIN" ] || exit 0` y, sin intérprete, permitía la edición en silencio; durante todo B-07 el enforcement estuvo caído sin que nadie lo notara. Ver `BACKLOG-INVESTIGACION` prioridad alta #4, que es la pregunta de investigación asociada.

Reserva: en un repo documental la fricción puede ser desproporcionada. Conviene medirla, no asumirla.

## M-03 — Playbooks agnósticos de asistente

Procedimiento neutro en `playbooks/{analyze,clarify}.md`, envuelto por wrappers finos (`.claude/skills/`, `.opencode/command/`) que no duplican el contenido. Adaptados a documentos: `analyze` = consistencia doc↔SSOT, afirmaciones sin `[Rxx]`, contradicciones entre SSOTs activos; `clarify` = resolver `[NEEDS CLARIFICATION]` abiertos.

Cierra una incoherencia del proyecto: investiga SDD multi-asistente y en la práctica su tooling es Claude-only.

## M-04 — Formato y compactación de documentos

Convención de formato con resumen ejecutivo obligatorio a partir de cierto tamaño y migración oportunística. Candidatos por tamaño: `../SPECS_REGISTRY.md`, `../experimentos/PRUEBA-REGENERABILIDAD-B7.md`, `../experimentos/PRUEBA-OBSERVACIONAL-B7.md`. En el testigo la reescritura compacta de una spec dio −46% sin pérdida de contenido normativo.

## M-05 — Encabezados que restatan su alcance

La regla de alcance en un solo lugar (`../SPECS_REGISTRY.md` §Reglas globales) admite una línea de identidad en el encabezado, no la enumeración de `incluye`/`excluye`. Caso conocido: `../comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md`. Migración al tocar cada documento, sin barrido masivo.

## M-06 — Modelo de confianza confirmado/inferido/gap

Clasificar cada afirmación como *confirmada* (evidencia directa), *inferida* (patrón, no certeza) o *gap* (requiere validación humana) [R25]. Es una graduación más fina que el binario actual (`[Rxx]` vs. `[NEEDS CLARIFICATION]`). Evaluar costo de mantenimiento antes de adoptar: la propia fuente advierte que la trazabilidad tiene costo. Migrado desde `BACKLOG-INVESTIGACION` §Enriquecimientos R25/R30, donde convivía con dos candidatos de contenido que se quedan allá.

## M-07 — Revisar la premisa "sin CI"

`../AGENTS.md` e `../comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md` describen un contexto sin CI. Sigue siendo cierto, pero desde 2026-07-31 hay git, y eso habilita `pre-commit` como sustrato tool-agnóstico para M-01 y M-02. Revisar ambos documentos cuando esas mejoras se implementen, no antes.

## M-08 — Emoticones en `PREREG-B7.md`

El documento viola la regla global «sin emoticones» pero está **pre-registrado y sellado**. Editarlo post-sello tiene implicancias metodológicas (Principio V). Decisión pendiente del usuario: corregir con enmienda fechada, o declarar excepción permanente para documentos sellados.

## M-09 — Señales de duplicación entre SSOTs

Dos checks nuevos en el backstop, ambos WARN, ambos originados en la Fase 11: los dos casos serios de duplicación que esa fase corrigió habían pasado los ocho checks existentes sin ruido.

- `ssot-collision`: cruza la columna *Concepto* de la tabla SSOT contra los campos `incluye` de las demás specs. Detecta que dos specs se declaren dueñas del mismo tema. Habría señalado el caso D1 (la spec de `../comun/MARCO-COMPARATIVO-DOS-LINEAS.md` declaraba `incluye: metricas por linea` mientras la tabla SSOT asignaba esas métricas a los dos `NECESIDADES-Y-METRICAS.md`).
- `normative-block`: detecta que la definición de un bloque normativo —hoy el `[SDD-Check]`, cuyo SSOT es `../AGENTS.md`— se reproduzca enumerada fuera de su SSOT. Distingue *instancia* de *definición*: una entrega que cierra con el bloque lleno es legítima en cualquier documento; lo que no lo es, es listar los campos como definición. Habría señalado el caso D2.

**Límite: son señales para revisión humana, no veredictos.**
**Hecha el 2026-07-31** (Fase 12). Validados contra el árbol anterior a la Fase 11: corriendo el script nuevo sobre el commit previo, `ssot-collision` reproduce el caso D1 (dos filas, líneas A y B) y `normative-block` reproduce el D2. Es la única forma honesta de saber que un check detecta lo que dice detectar.

En su primera corrida sobre el árbol actual `normative-block` encontró **un caso vivo que la Fase 11 no había auditado**: `../docs-y-investigacion/PLAN-PRUEBAS.md` A-02 reproducía los mismos cuatro campos del bloque. Corregido en la misma entrega. Calibración necesaria: la ventana hacia atrás que distingue instancia de definición pasó de 6 a 20 líneas, porque un bloque lleno tiene ocho campos y los últimos quedaban fuera del alcance del literal `[SDD-Check]`.
 El script conserva su límite declarado —presencia y forma, no adecuación— y por eso los dos checks emiten WARN: marcan candidatos a mirar, no violaciones probadas. Ampliar el límite del script a *adecuación* sería otra decisión y no se toma acá.

## M-10 — Verificar rutas escritas en backticks

`check_links` valida solo la sintaxis markdown `[texto](destino.md)`, pero este repositorio referencia sobre todo con backticks (`` `../comun/X.md` ``). Esas rutas no se verificaban, así que la reorganización de la Fase 11 pudo haber dejado referencias muertas sin que el backstop dijera nada.

Regla de resolución en tres casos, elegida para no producir falsos positivos con el proyecto testigo, cuya estructura de directorios es homónima de la nuestra:

1. Ruta con prefijo relativo explícito (`../`, `./`): se resuelve contra el directorio del documento. Es intención de navegación inequívoca.
2. Ruta cuyo primer segmento es un directorio **de este repositorio**: se resuelve contra la raíz.
3. Cualquier otro primer segmento (`docs/`, `specs/`, `memory/`, `.b7/`): es de otro repositorio, se ignora.

Un backtick sin barra es una mención por nombre, no una ruta, y no se verifica.

Se agregó un cuarto caso durante la implementación: una ruta relativa que **sale de la raíz** apunta a un repositorio hermano y tampoco se verifica.

**Hecha el 2026-07-31** (Fase 12). Encontró en su primera corrida una ruta que la propia Fase 11 había roto sin darse cuenta: `agenda/BACKLOG-INVESTIGACION.md` citaba `../investigaIA/...`, correcto mientras el archivo vivía en la raíz y falso al bajarlo un nivel. El barrido de referencias de la Fase 11 no podía verlo porque solo reescribía nombres de archivos movidos. De paso se corrigió `check_links`, que no ignoraba bloques ni spans de código y marcaba como roto cualquier ejemplo de sintaxis markdown citado en un documento.

## M-13 — `deriva_de` apunta a documentos que no son SSOT

El registro define `derivado` como "sintetiza un SSOT" y `deriva_de` como "el archivo **SSOT** de origen". En la práctica, de las declaraciones vigentes de `deriva_de`, varias apuntan a documentos que no son SSOT: tres a `../software/ANALISIS-SPEC-KIT.md`, declarado `operativo`, y una —`../software/DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md`— a `../software/COMPARATIVA-SPECKIT-VS-TESTIGO.md`, que es a su vez `derivado`, o sea un derivado de un derivado.

El backstop no lo vio nunca porque `check_deriva` verifica solo que el destino **exista** y que la cadena no tenga ciclos, no el `ssot_level` del destino. Detectado al decidir la naturaleza de `../software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md` (2026-08-02), que por esta razón se registró como SSOT propio en vez de sumar un caso más.

Dos salidas posibles, y la decisión es cuál antes de tocar nada:

1. **Ajustar la definición al uso**: `deriva_de` pasa a significar "documento del que este sintetiza", sin exigir que sea SSOT. Es lo que el repositorio hace hoy; el costo es que la trazabilidad de propagación deja de garantizar que la cadena termine en un SSOT.
2. **Ajustar el uso a la definición**: reclasificar los cuatro casos, lo que probablemente implique promover `ANALISIS-SPEC-KIT.md` a SSOT de algún tema o cambiar el `ssot_level` de sus derivados.

En cualquiera de las dos, el check correspondiente se agrega al backstop; hoy la regla no está verificada por nada. Emparentada con `M-11`, que también toca coherencia del registro contra sí mismo.

## M-11 — Validar la tabla SSOT

Hoy la tabla SSOT no se verifica en absoluto: ni que sus paths existan en disco, ni que coincidan con un `path` registrado. Los paths de la Fase 11 se actualizaron a mano y un olvido habría pasado limpio. Diferida a la iteración siguiente de M-09/M-10.

## M-12 — Higiene de archivo

CRLF mezclado, BOM y ausencia de newline final. Origen concreto: en la Fase 11 un barrido de referencias convirtió CRLF a LF en `../docs-y-investigacion/GUIA-INICIO-PROYECTO-INVESTIGACION.md`, único archivo del repo con ese final de línea, inflando su diff de 3 a 418 líneas. Se detectó por el diffstat, no por el backstop. Diferida junto con M-11.
