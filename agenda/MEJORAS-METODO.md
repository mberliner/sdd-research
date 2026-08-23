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
| M-05 | Limpiar encabezados que restatan su alcance | baja | **Hecha** (2026-08-23) | regla de alcance, Fase 8 | `../software/RELACION-SPEC-VS-EPICA.md` |
| M-06 | Modelo de confianza confirmado/inferido/gap | media | Propuesta | [R25] | convención de Línea A |
| M-07 | Revisar la premisa "sin CI" tras el versionado | baja | **Hecha** (2026-08-15) | Fase 8 | `../AGENTS.md`, `../comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md` |
| M-08 | Decidir qué hacer con los emoticones de `PREREG-B7.md` | baja | Propuesta | Fase 8 | decisión del usuario |
| M-09 | Señales de duplicación entre SSOTs (`ssot-collision`, `sdd-check-fields`) | alta | **Hecha** (Fase 12) | Fase 11 | `../tools/check_docs.py` |
| M-10 | Verificar rutas escritas en backticks, no solo links markdown | alta | **Hecha** (Fase 12) | Fase 11 | `../tools/check_docs.py` |
| M-11 | Validar la tabla SSOT contra el disco y contra las specs | media | **Hecha** (Fase 13) | Fase 11 | `../tools/check_docs.py` |
| M-12 | Higiene de archivo: CRLF mezclado, BOM, newline final | media | **Hecha** (Fase 13) | Fase 11 | `../tools/check_docs.py` |
| M-13 | `deriva_de` apunta a documentos que no son SSOT | media | **Hecha** (2026-08-03) | relevamiento 2026-08-02, completado 2026-08-03 | `../SPECS_REGISTRY.md` + `../tools/check_docs.py` |
| M-14 | Índices de línea duplicaban `proposito`/`estado` fuera del registro | media | **Hecha** (2026-08-03) | auditoría de coherencia 2026-08-03 | `../SPECS_REGISTRY.md` + `../software/00-INDEX.md` |
| M-15 | Cada principio declara un verificador ejecutable, o declara que no tiene | alta | **Hecha** (2026-08-15) | sdd-first [R39] (`../software/ANALISIS-SDD-FIRST.md` C1) | `../CONSTITUTION.md` + `../tools/check_docs.py` |
| M-16 | Verificar `Derivados a revisar` contra el disco y la tabla SSOT | media | Propuesta | sdd-first [R39] (`../software/ANALISIS-SDD-FIRST.md` C2) | `../tools/check_docs.py` |
| M-17 | Portar el modelo de skills multi-asistente desde una fuente única | media | Propuesta | sdd-first [R39] (`../software/ANALISIS-SDD-FIRST.md` C5) | contraparte de M-03 |
| M-18 | Ningún documento `Activo` conserva un `[NEEDS CLARIFICATION]` abierto | alta | **Hecha** (2026-08-15) | resultado de M-15: Principio VII sin verificador | `../tools/check_docs.py` + `../CONSTITUTION.md` |
| M-19 | Cablear el backstop al commit, fail-closed y versionado | alta | **Hecha** (2026-08-15) | pendiente de M-01; `BACKLOG-INVESTIGACION.md` alta #4 | `../tools/githooks/pre-commit` + check `gate` |
| M-20 | Verificador del Principio VI (cambio de método ⇒ entrada de historial) | alta | **Hecha** (2026-08-15) | pendiente de M-01; resultado de M-15 | `../tools/check_docs.py` (`metodo-historial`) |
| M-21 | `metodo-historial` sobre-dispara en altas de contenido del registro | baja | Propuesta (2026-08-15) | fricción observada al registrar A-04 | `../tools/check_docs.py` (`metodo-historial`) |
| M-22 | Lo que un experimento sella: eliminarlo como variable, verificarlo, o declararlo sin verificador | alta | Propuesta (2026-08-19; reformulada 2026-08-23) | desviación observada en T2 de la pasada 1b de A-04 | `../templates/EXPERIMENTO.md` + scripts de preparación |
| M-23 | `excluded-field` escaneaba solo tablas, no listas | baja | **Hecha** (2026-08-23) | auditoría de índices de línea | `../tools/check_docs.py` |
| M-24 | `normative-block` cubría bastante menos de lo que su nombre prometía | media | **Hecha** (2026-08-23) | revisión de `../AGENTS.md`, alta de `../CONVENCIONES.md` | `../tools/check_docs.py` + `../AGENTS.md` + `../CONSTITUTION.md` |
| M-25 | El sello MUST identificar el artefacto que constituye el tratamiento | alta | Propuesta (2026-08-22; reformulada 2026-08-23) | un tratamiento vivo cambió durante A-04 sin que nada lo registrara | `../templates/EXPERIMENTO.md` (aplicación: runbooks vigentes) |
| M-26 | «Qué decisión habilita» es un MUST sin casillero donde satisfacerse | baja | Propuesta (2026-08-22) | revisión de `../AGENTS.md` | `../AGENTS.md` (bloque `[SDD-Check]`) |
| M-27 | `sdd-check-fields` no miraba `templates/`, que es donde una definición se propaga sola | baja | **Hecha** (2026-08-23) | lectura de la implementación al ejecutar M-24 | `../tools/check_docs.py` |
| M-28 | Encabezados que reproducen campos del registro (`estado`, `ssot_level`, `owner`, `deriva_de`) | media | Propuesta (2026-08-23) | auditoría de encabezados 2026-08-23 | `../SPECS_REGISTRY.md` + los documentos afectados |

---

## M-01 — Backstop determinista de documentación

Script local (sin CI) que verifica lo que hoy son checkboxes aspiracionales del campo `validacion`: todo `.md` autorado tiene spec registrada o cae en una exención declarada; el registro no apunta a archivos inexistentes; links internos vivos; `[Rxx]` usadas ⊆ `../REFERENCIAS.md`; `deriva_de` existe y no es circular; `estado` y `ssot_level` con valores válidos; cadena de precedencia coherente entre los documentos que la declaran.

Es la capa 2 del enforcement de tres capas del testigo (`docs/SDD-ENFORCEMENT.md`), portada a un repo documental. Límite heredado y explícito: verifica **presencia y forma, no adecuación** — que un documento tenga spec no dice que la spec lo describa bien.

Contraparte de investigación: `BACKLOG-INVESTIGACION` exploratoria «evaluación automática parcial sin CI», y prioridad alta «umbral de control manual a automatizado». Ejecutar M-01 produce dato para ambas; no las cierra.

**Hecha el 2026-07-31** (`../tools/check_docs.py`, Fase 10). Ocho checks, dos severidades, sin dependencias externas. Primera corrida sobre 41 documentos: 6 ERROR, de los cuales **2 eran deriva real** (`ANALISIS-SPEC-KIT.md` C4 y `../templates/RESULTADO-EXPERIMENTO.md`, ambos describiendo la precedencia sin la constitución, un día después de haberla creado) y 4 falsos positivos que obligaron a afinar la heurística. Queda 1 WARN vivo a propósito: los emoticones de `PREREG-B7.md`, que son M-08.

Pendiente evaluado y no hecho: cablearlo a `pre-commit` (requiere decidir M-02 primero) y un check del criterio de separación método/investigación, que hoy nada verifica.

**Ambos pendientes se cerraron el 2026-08-15 como M-19 y M-20**, y con ellos la dependencia declarada arriba, que resultó falsa: correr el backstop al commit es la capa 2 del enforcement (verificar la salida) y el gate de autoría `.sdd/current-doc` es la capa 3 (autorizar la entrada). La capa 2 no necesita saber qué spec gobierna la edición, así que no dependía de decidir M-02. Ver M-19.

## M-02 — Gate de autoría documental

Declaración de la spec que gobierna la edición (`.sdd/current-doc`) más un hook `PreToolUse` que bloquea editar un `.md` de contenido sin esa declaración, con chequeo de mtime: la spec MUST haberse editado después de declararse. Reusa `../tools/sdd_gate.py` del testigo, que ya separa decisión de transporte (stdin JSON / argv / env) y por lo tanto no queda atado a Claude Code.

**Requisito de diseño no negociable: fail-closed.** El gate del testigo terminaba en `[ -f "$PYBIN" ] || exit 0` y, sin intérprete, permitía la edición en silencio; durante todo B-07 el enforcement estuvo caído sin que nadie lo notara. Ver `BACKLOG-INVESTIGACION` prioridad alta #4, que es la pregunta de investigación asociada.

Reserva: en un repo documental la fricción puede ser desproporcionada. Conviene medirla, no asumirla.

**Corrección de diseño incorporada el 2026-08-15 (origen: sdd-first [R39], `../software/ANALISIS-SDD-FIRST.md` C3).** El chequeo de mtime del párrafo anterior MUST NOT implementarse: se implementó en sdd-first y falló en las dos direcciones —bloqueó flujo legítimo (una spec trabajada en varios commits, `git checkout`, `clone`, y el ciclo stash/restore del propio `pre-commit`, que renueva mtimes) y no detuvo a nadie, porque un `touch` lo satisfacía. El criterio que lo reemplazó es de **contenido**: la spec declarada debe existir, figurar en el registro con un estado que habilite trabajo, y tener al menos un requisito con texto propio además del keyword; los placeholders de la plantilla no cuentan. Se conserva el enunciado original arriba, tachado por esta nota y no borrado, porque el error es el dato. Tres modos de falla adicionales ya documentados por esa fuente y transferibles a `.sdd/current-doc`: el gate debe fallar cerrado incluso sobre un harness fail-open; la escritura por `Bash` escapa a todo hook `PreToolUse` y se cubre corriendo la capa al commit, no parseando la línea de comandos; un reset post-commit evita que una declaración quede vigente por descuido.

## M-03 — Playbooks agnósticos de asistente

Procedimiento neutro en `playbooks/{analyze,clarify}.md`, envuelto por wrappers finos (`.claude/skills/`, `.opencode/command/`) que no duplican el contenido. Adaptados a documentos: `analyze` = consistencia doc↔SSOT, afirmaciones sin `[Rxx]`, contradicciones entre SSOTs activos; `clarify` = resolver `[NEEDS CLARIFICATION]` abiertos.

Cierra una incoherencia del proyecto: investiga SDD multi-asistente y en la práctica su tooling es Claude-only.

## M-04 — Formato y compactación de documentos

Convención de formato con resumen ejecutivo obligatorio a partir de cierto tamaño y migración oportunística. Candidatos por tamaño: `../SPECS_REGISTRY.md`, `../experimentos/b07-formato-hibrido/PRUEBA-REGENERABILIDAD-B7.md`, `../experimentos/b07-formato-hibrido/PRUEBA-OBSERVACIONAL-B7.md`. En el testigo la reescritura compacta de una spec dio −46% sin pérdida de contenido normativo.

## M-05 — Encabezados que restatan su alcance

La regla de alcance en un solo lugar (`../SPECS_REGISTRY.md` §Reglas globales) admite una línea de identidad en el encabezado, no la enumeración de `incluye`/`excluye`. Caso conocido: `../comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md`. Migración al tocar cada documento, sin barrido masivo.

**Hecha el 2026-08-23.** Barrido de los encabezados de los 45 documentos autorados. El caso conocido ya cumplía: su encabezado es una línea de identidad más punteros a dónde vive lo que no cataloga, que es lo que la regla admite. Un solo caso vivo, corregido en la misma entrega: `../software/RELACION-SPEC-VS-EPICA.md` declaraba en su línea `Alcance:` una exclusión —la transferencia del razonamiento a Línea A— ausente del `excluye` registrado; la exclusión se trajo al registro y el encabezado quedó en identidad. Ningún otro encabezado enumera su alcance.

## M-06 — Modelo de confianza confirmado/inferido/gap

Clasificar cada afirmación como *confirmada* (evidencia directa), *inferida* (patrón, no certeza) o *gap* (requiere validación humana) [R25]. Es una graduación más fina que el binario actual (`[Rxx]` vs. `[NEEDS CLARIFICATION]`). Evaluar costo de mantenimiento antes de adoptar: la propia fuente advierte que la trazabilidad tiene costo. Migrado desde `BACKLOG-INVESTIGACION` §Enriquecimientos R25/R30, donde convivía con dos candidatos de contenido que se quedan allá.

## M-07 — Revisar la premisa "sin CI"

`../AGENTS.md` e `../comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md` describen un contexto sin CI. Sigue siendo cierto, pero desde 2026-07-31 hay git, y eso habilita `pre-commit` como sustrato tool-agnóstico para M-01 y M-02. Revisar ambos documentos cuando esas mejoras se implementen, no antes.

**Hecha el 2026-08-15**, junto con M-19. `../AGENTS.md` deja de decir que la verificación corre solo a pedido, y `../comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md` distingue lo que seguía siendo cierto de lo que ya no: no hay CI, pero **sin CI dejó de significar sin verificación automática**. El escalón que falta es el remoto, y su criterio ya estaba escrito en ese documento.

## M-08 — Emoticones en `PREREG-B7.md`

El documento viola la regla global «sin emoticones» pero está **pre-registrado y sellado**. Editarlo post-sello tiene implicancias metodológicas (Principio V). Decisión pendiente del usuario: corregir con enmienda fechada, o declarar excepción permanente para documentos sellados.

## M-09 — Señales de duplicación entre SSOTs

Dos checks nuevos en el backstop, ambos WARN, ambos originados en la Fase 11: los dos casos serios de duplicación que esa fase corrigió habían pasado los ocho checks existentes sin ruido.

- `ssot-collision`: cruza la columna *Concepto* de la tabla SSOT contra los campos `incluye` de las demás specs. Detecta que dos specs se declaren dueñas del mismo tema. Habría señalado el caso D1 (la spec de `../comun/MARCO-COMPARATIVO-DOS-LINEAS.md` declaraba `incluye: metricas por linea` mientras la tabla SSOT asignaba esas métricas a los dos `NECESIDADES-Y-METRICAS.md`).
- `sdd-check-fields` (así desde M-24; se llamó `normative-block` hasta el 2026-08-23): detecta que la definición de un bloque normativo —hoy el `[SDD-Check]`, cuyo SSOT es `../AGENTS.md`— se reproduzca enumerada fuera de su SSOT. Distingue *instancia* de *definición*: una entrega que cierra con el bloque lleno es legítima en cualquier documento; lo que no lo es, es listar los campos como definición. Habría señalado el caso D2.

**Límite: son señales para revisión humana, no veredictos.**
**Hecha el 2026-07-31** (Fase 12). Validados contra el árbol anterior a la Fase 11: corriendo el script nuevo sobre el commit previo, `ssot-collision` reproduce el caso D1 (dos filas, líneas A y B) y `sdd-check-fields` reproduce el D2. Es la única forma honesta de saber que un check detecta lo que dice detectar.

En su primera corrida sobre el árbol actual `sdd-check-fields` encontró **un caso vivo que la Fase 11 no había auditado**: `../docs-y-investigacion/PLAN-PRUEBAS.md` A-02 reproducía los mismos cuatro campos del bloque. Corregido en la misma entrega. Calibración necesaria: la ventana hacia atrás que distingue instancia de definición pasó de 6 a 20 líneas, porque un bloque lleno tiene ocho campos y los últimos quedaban fuera del alcance del literal `[SDD-Check]`.
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

**Hecha el 2026-08-03.** Relevamiento completo, remediación y cierre — detalle en `../historial/sdd.md`. Emparentada con `M-11`, que también toca coherencia del registro contra sí mismo.

Resumen: de 7 specs `derivado` vigentes, 6 violaban la definición literal en tres patrones (destino `operativo`, derivado-de-derivado, destino sin entrada) y 1 (`RELACION-SPEC-VS-EPICA.md`) resultó ser un error de modelado distinto — relación forzada, no síntesis real — remediado quitándole `deriva_de`. Los 6 restantes se resolvieron combinando: `deriva_de` ahora permite cadena (origen `SSOT` o `derivado`, nunca `operativo` ni sin registrar); `ANALISIS-SPEC-KIT.md` promovido a `SSOT`; `EXPERIMENTO-B7-formato-hibrido.md` dado de alta en el registro con entrada mínima. `check_docs.py` valida la regla nueva.

## M-14 — Índices de línea duplicaban `proposito`/`estado`

**Hecha el 2026-08-03.** Una auditoría de coherencia encontró que `software/00-INDEX.md` anotaba "Estado: Borrador" para `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` mientras el registro ya declaraba `estado: Activo` desde el 2026-06-06 — contradicción directa entre el índice y su SSOT. Causa raíz: la spec de `docs-y-investigacion/00-INDEX.md` y `software/00-INDEX.md` (`../SPECS_REGISTRY.md`) no prohibía explícitamente que las descripciones junto a cada link parafrasearan el `proposito` registrado ni que anotaran `estado`, a diferencia de la regla ya vigente para el `00-INDEX.md` de raíz.

Se corrigió: `SPECS_REGISTRY.md` suma `excluye`/`validacion` explícitos para ambos índices de línea (sin parafraseo de `proposito`, sin anotación de `estado`); `software/00-INDEX.md` se recortó a punteros breves y se quitaron las dos anotaciones de `Estado`. `docs-y-investigacion/00-INDEX.md` ya cumplía (lista sin descripciones ni estado) y no requirió cambios de contenido.

## M-11 — Validar la tabla SSOT

Hoy la tabla SSOT se verifica mecánicamente: `check_docs.py` asegura que sus paths existan en disco y que coincidan con un `path` registrado. Implementada junto con M-12 en la Fase 13.

## M-12 — Higiene de archivo

CRLF mezclado, BOM y ausencia de newline final. Origen concreto: en la Fase 11 un barrido de referencias convirtió CRLF a LF en `../docs-y-investigacion/GUIA-INICIO-PROYECTO-INVESTIGACION.md`, único archivo del repo con ese final de línea, inflando su diff de 3 a 418 líneas. Se detectó por el diffstat, no por el backstop. Implementada en la Fase 13: `check_docs.py` ahora fuerza `LF`, prohíbe `BOM` y requiere newline final. El repositorio fue convertido masivamente a `LF`.

## M-15 — Cada principio declara un verificador ejecutable, o declara que no tiene

Los siete principios de `../CONSTITUTION.md` declaran `Enforcement:` y los siete nombran prosa: «checks de post-generación de `AGENTS.md`», «revisión editorial», «campo `validacion` de cada spec». `../tools/check_docs.py` existe y cubre parte de eso, pero ningún principio lo nombra y nada verifica que la relación entre principio y verificador sea otra cosa que una intención escrita.

Propuesta: que cada principio nombre el check de `check_docs.py` que lo cubre, o `ninguno` cuando nada lo cubra, y que `check_docs.py` verifique que los nombrados existen. Lo que produce no es enforcement universal —un repositorio documental sin CI no puede mecanizar «no formular una hipótesis después de ver el resultado»— sino **visibilidad de qué principio tiene mecanismo y cuál depende de que alguien se acuerde**.

Origen: sdd-first [R39] declara ese vínculo en el config y verifica que el paso esté cableado y haya corrido; su SPEC-020 nació justamente al descubrir que un principio nuevo obtenía «enforcement decorativo» sin aviso (`../software/ANALISIS-SDD-FIRST.md` C1). Contraparte de investigación: `BACKLOG-INVESTIGACION.md` prioridad alta #4 (gates que fallan abierto) y #3 (umbral de control manual a automatizado).

**Hecha el 2026-08-15.** `../CONSTITUTION.md` v0.2.0: cada principio suma un campo `Verificador:` con los checks que lo cubren o `ninguno`, y una nota de alcance cuando la cobertura es parcial. `../tools/check_docs.py` suma el check `constitucion`, que falla si un principio no declara el campo, si declara `ninguno` y checks a la vez, o si nombra un check que el script no emite. Los ids válidos **se derivan de la propia fuente** del script y no de una lista mantenida a mano: una lista habría reintroducido, un nivel más arriba, la misma deriva que el check existe para detectar.

Resultado de la primera pasada, que es el dato que la mejora buscaba: **tres de los siete principios tienen verificador**, y solo uno de forma sustantiva. I (SSOT único) y II (trazabilidad a fuente) quedan parciales —el check confirma que la `[Rxx]` citada existe, no que la afirmación esté citada—; IV (documento autorado, spec registrada) es el único bien cubierto. III, V, VI y VII declaran `ninguno`: la propagación bidireccional es M-16, el sellado experimental es una promesa sobre el orden entre pensar y ver que nada mecánico observa, el criterio método/contenido quedó pendiente al cerrar M-01, y nada verifica que un `[NEEDS CLARIFICATION]` se resuelva antes de declarar activo un documento.

Actualización 2026-08-15: el último de esos cuatro dejó de ser cierto el mismo día — VII pasó a tener verificador con `M-18`, que salió directamente de leer este párrafo. El conteo vigente es **cuatro de siete**; quedan III, V y VI.

Efecto colateral saldado: `../AGENTS.md` afirmaba que no había verificación determinista, lo que era falso desde M-01. Corregido en la misma entrega — es parte de M-07, que sigue abierta por `../comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md`.

Validación: el check se probó en rojo antes de escribir el campo (7 ERROR, uno por principio) y contra dos deformaciones deliberadas —un check inexistente y un campo renombrado—, ambas detectadas; el árbol se restauró y quedó en 0 ERROR.

## M-16 — Verificar `Derivados a revisar` contra el disco y la tabla SSOT

El bloque `[SDD-Check]` declara `Derivados a revisar` y `Cobertura` en prosa que escribe el autor de la entrega sobre sí mismo. Nada verifica que los derivados nombrados existan, ni que un cambio en un SSOT haya nombrado a los suyos.

Origen: sdd-first [R39] SPEC-024, que cerró el hueco equivalente del lado del código —un requisito «verde» sobre un test que prueba otra cosa— exigiendo que el ID del FR aparezca como token completo dentro del archivo de test, con el cuidado explícito de no usar substring (`FR-1` dentro de `FR-10`). Ver `../software/ANALISIS-SDD-FIRST.md` C2.

Reserva antes de aprobarla: en un repo documental el vínculo requisito→verificador no tiene análogo tan limpio como FR→test, así que el alcance realista es el par SSOT→derivado registrado en `../SPECS_REGISTRY.md`, no la adecuación de la revisión.

## M-17 — Portar el modelo de skills multi-asistente desde una fuente única

Contraparte concreta de M-03, que declara la incoherencia (investigamos SDD multi-asistente y el tooling es Claude-only) pero no el mecanismo. sdd-first sirve siete skills a cuatro asistentes desde una fuente única: playbook agnóstico como SSOT del contenido, `SKILL.md` fuente como wrapper, y adaptadores generados y committeados con cabecera «NO EDITAR A MANO». Sin symlinks a propósito: se degradan en Windows sin Developer Mode. Detalle en `../fuentes-externas/sdd-first/docs/SKILLS-MULTITOOL.md`; lectura en `../software/ANALISIS-SDD-FIRST.md` C5.

Reserva: portarlo trae un generador en Python, dependencia que hoy solo tiene `check_docs.py`. Decidir M-03 primero — sin playbooks que servir, no hay nada que generar.

## M-18 — Ningún documento `Activo` conserva un `[NEEDS CLARIFICATION]` abierto

Origen: el resultado de M-15, que dejó al Principio VII declarando `Verificador: ninguno` con esta frase — «el marcador es grep-able, pero nada verifica que se haya resuelto antes de declarar un documento activo». Las dos piezas necesarias ya existían por separado: el marcador es grep-able desde que se adoptó de Spec Kit [R10], y el registro ya declara `estado` por documento. La mejora es cruzarlas.

**Hecha el 2026-08-15.** `../tools/check_docs.py` suma el check `clarificacion` (ERROR): un documento cuya spec declara `Activo` —incluido el default, que es no escribir el campo— no puede conservar un marcador con su pregunta escrita. `../CONSTITUTION.md` v0.2.1 lo declara en el Principio VII.

Dos límites, declarados en el propio check y elegidos contra un corpus que discute la convención en unos treinta lugares sin tener un solo marcador vivo:

1. **Marcador vs. mención.** Cuenta como marcador lo que trae `:` y una pregunta propia; la elipsis y el metavariable entre ángulos son como este repositorio cita el instrumento cuando habla de él. Los backticks **no** eximen a propósito: un marcador vivo escrito entre backticks sigue estando abierto.
2. **Hueco conocido: los documentos exentos de spec.** `EXPERIMENTO-*` y `RESULTADO-EXPERIMENTO-*` no tienen `estado` que consultar, y la obligación del protocolo está enunciada contra ese campo — así que quedan fuera justo donde los marcadores reales más aparecen (`../experimentos/b07-formato-hibrido/PRUEBA-REGENERABILIDAD-B7.md` llegó a tener cuatro). Cerrarlo exige decidir antes qué significa `Activo` para un documento exento, que es una pregunta sobre el registro y no sobre el check.

Lo que el check **no** cubre del principio: el caso en que el asistente interpretó en silencio y nunca hubo marcador. Eso sigue sin observador mecánico, y es la mitad que la contraparte de investigación mide sobre conducta (`BACKLOG-INVESTIGACION.md` prioridad alta #8).

Validación: verde sobre el árbol actual sin un solo falso positivo entre las menciones existentes, y cinco deformaciones deliberadas con el comportamiento esperado — marcador vivo en documento `Activo` y el mismo entre backticks, ambos detectados; marcador dentro de un bloque de código y marcador en un documento `Borrador`, ninguno detectado; y el check renombrado en el script, detectado por `constitucion`, que es el lazo de M-15 cerrándose sobre la declaración nueva. Árbol restaurado y 0 ERROR.

## M-19 — Cablear el backstop al commit, fail-closed y versionado

La incoherencia más cara del repositorio: investiga gates que fallan abierto (`BACKLOG-INVESTIGACION.md` prioridad alta #4, hallazgo de B-07) y su propia verificación fallaba abierta por diseño — `check_docs.py` corría solo si alguien se acordaba, así que nada distinguía un commit verificado de uno que nadie miró.

**Hecha el 2026-08-15.** `../tools/githooks/pre-commit`, versionado en el árbol y activado con `git config core.hooksPath tools/githooks`, corre el backstop en modo `--staged` y bloquea el commit si hay ERROR. Tres decisiones de diseño, cada una contra un modo de falla ya observado:

1. **Fail-closed en la resolución del intérprete.** Si no encuentra `python3`/`python`/`py`, bloquea. El gate del testigo terminaba en `[ -f "$PYBIN" ] || exit 0` y resolvía contra un `.venv` no versionado: en los cuatro workspaces de B-07 salió 0 sin correr nada.
2. **Versionado, no copiado a `.git/hooks/`.** `core.hooksPath` apunta al árbol, así que el gate se versiona con el repositorio en vez de vivir en un directorio que ningún clon trae.
3. **Heartbeat propio: el check `gate`.** Verifica que el hook exista, que `core.hooksPath` lo apunte y que tenga permiso de ejecución — las tres formas de quedar desconectado sin aviso. Un clon fresco sin instalar da ERROR, que es la respuesta correcta: el enforcement no está.

Dos límites, ambos declarados en el propio hook: verifica el **árbol de trabajo, no el índice** (un `git add -p` puede pasar el gate con el índice en rojo; no se hace stash/restore a propósito, que es el ciclo con el que sdd-first se ganó falsos bloqueos), y el flag de bypass de git lo saltea, que es la excepción de `../AGENTS.md` §Excepciones ejercida por el operador. Nada detecta el bypass; el check `gate` detecta la desconexión.

Contraparte de investigación: `BACKLOG-INVESTIGACION.md` alta #4 pedía «cómo detectar que un gate está caído (heartbeat / self-test)». El check `gate` es una respuesta parcial y ejecutada, no la cierra: detecta el gate desconectado, no el gate presente que no verifica lo que dice verificar.

## M-20 — Verificador del Principio VI

El Principio VI declaraba `Verificador: ninguno` con el diagnóstico escrito desde M-01: «un check del criterio de separación método/investigación quedó pendiente y sigue sin darse de alta». `../AGENTS.md` §Al cerrar una iteración obliga desde siempre a asentar el cambio de método en el historial, más reciente arriba, y nada lo miraba.

**Hecha el 2026-08-15.** Check `metodo-historial` (ERROR): si el commit toca método —`AGENTS.md`, `CONSTITUTION.md`, `SPECS_REGISTRY.md`, `CLAUDE.md`, `templates/`, `tools/`— entonces `../historial/sdd.md` MUST traer una entrada nueva y MUST quedar arriba. `agenda/` no dispara a propósito: proponer una mejora no es adoptarla, y el historial asienta adopciones. `tools/` sí dispara, porque cambiar el verificador de un principio es cambiar el método tanto como cambiar el principio.

Decisión que la mejora tuvo que tomar y estaba pendiente: **el backstop puede depender de git**, en un modo opcional que degrada. El check corre solo con `--staged`, que es lo que invoca el gate de M-19; en un árbol sin git no dice nada y el principio vuelve a no tener verificador. Era la pregunta que M-18 dejó abierta al declarar M-16 «bloqueada por la decisión de si el backstop puede depender de git», y con esto M-16 se desbloquea.

Límite del mismo tipo que el resto del script: verifica que la entrada exista y quede arriba, no que **clasifique bien**. Que un cambio sea método y no hallazgo, y la dirección simétrica del principio —que un hallazgo no mueva el método sin decisión explícita y fechada— siguen siendo juicio humano.

## M-21 — `metodo-historial` sobre-dispara en altas de contenido del registro

Observado el 2026-08-15 al dar de alta A-04: registrar dos specs nuevas en `../SPECS_REGISTRY.md` disparó la exigencia de entrada de historial, aunque la entrega **sólo agrega contenido registrado** y no cambia ninguna regla del registro.

El check es fiel al texto: el Principio VI nombra literalmente «registro de specs» entre las piezas de método. El que está grueso es el texto, no el verificador.

**Recomendación: no ajustar el check todavía.** Aflojar un verificador recién entregado para que la tarea siguiente sea más cómoda, sin un dato que lo justifique, es exactamente la clase de deriva que el proyecto existe para no cometer. Si en tres o cuatro entregas el falso positivo se repite, ahí hay caso — y la distinción a implementar sería entre cambiar las **reglas** del registro (método) y agregar **entradas** al registro (contenido), que no es trivial de decidir por diff.

Costo actual: una entrada de historial de más por alta de spec. Barato. Se acepta la fricción y se cuenta.

## M-22 — Lo que un experimento sella: eliminarlo como variable, verificarlo, o declararlo

**Regla propuesta.** Por cada componente que un experimento declara sellado, el diseño MUST resolver, **en este orden**:

1. **Eliminarlo como variable.** ¿Puede construirse la corrida de modo que el desvío sea imposible, no sólo improbable? Si sí, se hace acá y no hay nada que vigilar después.
2. **Verificarlo en corrida.** Lo que no se pudo eliminar MUST tener un verificador que lo comprueba en cada rep y aborta ante divergencia.
3. **Declararlo sin verificador.** Lo que no admite ninguna de las dos MUST quedar escrito como límite del experimento, con su motivo. No es un cajón de derrota: es la diferencia entre un límite conocido y una sorpresa.

El orden no es decorativo. Un desvío eliminado por construcción no puede ocurrir; uno vigilado ocurre y se detecta después de ocurrido, que en una tanda ya corrida puede significar re-correrla entera. Además, la pregunta «¿qué puede cambiar mientras esto corre?» pertenece al momento en que se fija la hipótesis, no al momento en que se descubre que algo cambió — decidirla al diseñar es lo que el Principio V pide.

Es la mitad mecanizable de ese principio, que hoy declara `Verificador: ninguno` (`../CONSTITUTION.md`; ver M-15). Su mitad difícil —el orden entre pensar y ver— no es observable por un script. Su mitad fácil sí: que el objeto sellado siga siendo el mismo objeto. La mejora es de método y no de un experimento porque el hueco se abre cada vez que un runbook escribe un sello y sigue.

Componentes conocidos que el sello alcanza, y hasta qué escalón llega cada uno:

- **Tratamiento** —el artefacto que constituye la variable independiente. Cuando es material versionado, el escalón 1 lo resuelve casi entero. Es **M-25**, que aplica esta jerarquía a ese componente y no la reenuncia.
- **Entorno de ejecución.** Cambia *solo*, sin intervención: un harness que se auto-actualiza, una dependencia que resuelve a la última versión. El escalón 1 llega hasta donde llegue el control sobre esa pieza —pinneo, auto-actualización desactivada, corrida sin red, ventana temporal corta— y **no llega hasta el final** cuando el objeto de estudio es la conducta bajo una herramienta de terceros: blindarla del todo puede cambiar lo que se está midiendo. Por eso acá el escalón 2 es esencial y no cosmético.
- **Fixture y workspace.** Ya en el escalón 2 hoy, por hash y auditoría de ancestros: son el ejemplo de lo que la regla generaliza, no un pendiente.

Forma de la mejora, en dos piezas:

1. `../templates/EXPERIMENTO.md` suma una sección de sello donde cada componente declarado responde los tres escalones. Es el mismo movimiento que M-15 hizo sobre `../CONSTITUTION.md`: no mecaniza lo inmecanizable, hace visible qué está cubierto y qué depende de que alguien se acuerde.
2. El script de preparación de cada rep implementa el escalón 2 donde corresponda: lee el valor efectivo y aborta si no coincide con lo sellado, en el mismo lugar donde ya vive el chequeo de hashes del fixture.

**La prevención no vuelve prescindible el verificador; le cambia el rol.** Un mecanismo de eliminación es en sí mismo algo sellado: una variable de entorno que una versión nueva deja de respetar, un tag de imagen que se movió, una extracción que salió de un árbol sucio. Sin comprobación, no se distingue «funcionó» de «dejó de funcionar en silencio», que es exactamente el modo de falla que M-19 documentó — el gate del testigo salía 0 sin correr nada y nadie lo notó durante todo B-07. Donde el escalón 1 alcanza, el escalón 2 sobrevive como heartbeat barato.

Tres reservas antes de darla por diseñada:

1. **Qué componentes entran.** Enumerar de más convierte el check en fuente de falsos bloqueos; enumerar de menos lo deja donde está hoy. El criterio candidato es «lo que el artefacto de sello declara explícitamente», que no necesita una lista aparte y crece solo cuando alguien decide sellar algo nuevo.
2. **Qué hacer cuando el escalón 2 dispara.** Abortar es lo correcto para un rep suelto; para una tanda a mitad de camino la decisión —re-correr la pasada, o contarla con la confusión declarada— es de diseño y no la toma un script. El verificador MUST detener y explicitar, MUST NOT elegir.
3. **Retorno decreciente del escalón 1.** Cada mecanismo de prevención es otra cosa sellada que alguien debería verificar. Regla práctica: prevenir donde el mecanismo cueste menos que el check —el caso del tratamiento, donde extraer de un commit cuesta lo mismo que copiar un archivo— y verificar donde no. No construir una fortaleza para proteger diez reps.

**Caso que la originó** (evidencia, no alcance). Pasada 1b de A-04: el sello fijaba «Claude Code 2.1.233»; T1 corrió el 2026-08-16 bajo esa versión y T2 corrió el 2026-08-19 bajo 2.1.234 en los reps 01-06 y bajo **2.1.235** en los 07-10 —la CLI se auto-actualizó entre tandas y otra vez a mitad de tanda—. Ningún rep de T2 corrió bajo el entorno sellado, y la desviación se descubrió tres días después, al preparar la Fase 4, porque el barajado obligó a mirar los campos del transcript que delatan la tanda (`../../experimentosdd-a4/T2-1B.md`). Lo instructivo es la asimetría: el script ya abortaba por hash del fixture, por configuración de asistente presente y por ancestros, y el único componente del sello que podía cambiar sin intervención era justo el que nadie miraba. El verificador propuesto habría abortado en el rep 01, con la pasada dentro de la ventana de 12-72 h y con 2.1.233 aún instalable.

Contraparte de investigación: caso concreto de `BACKLOG-INVESTIGACION.md` prioridad alta #4, «cómo detectar que un gate está caído». Acá el gate no estaba caído — nunca existió, y lo que lo hizo visible fue un procedimiento posterior que necesitaba el mismo dato por otro motivo. Vale como observación sobre qué hace visible un hueco de verificación, distinta de la que M-19 ya registró.

## M-23 — `excluded-field` escaneaba solo tablas, no listas

El check (`M-09`) solo escanea líneas que empiezan con `|` — filas de tabla markdown. `../software/00-INDEX.md` reproducía el rol (`ssot_level`) de tres documentos en una lista con guiones (`- [link] — SSOT de...`, `- [link] — ... Deriva de X.`), forma que la spec de ese índice prohíbe igual que una tabla, pero que el check no reconoce por no ser tabla.

Detectado el 2026-08-22 en una auditoría de los tres `00-INDEX.md` contra `../SPECS_REGISTRY.md`: cobertura de specs completa (0 archivo sin registrar, 0 spec sin archivo), pero esta anotación de rol en prosa pasó los checks existentes sin ruido — mismo patrón que motivó `M-09` (duplicación de SSOT no detectada por los checks de entonces). Corregido a mano en la misma auditoría.

Forma de la mejora: generalizar el escaneo de `check_excluded_fields_in_tables` a cualquier línea de contenido (no solo `|...|`), buscando los valores válidos de `estado`/`ssot_level` como palabra completa cerca de un link, no solo dentro de celdas de tabla. Riesgo a evitar: falsos positivos con menciones legítimas de la palabra "SSOT" fuera de una anotación de rol (por ejemplo, en prosa explicativa).

**Hecha el 2026-08-23.** `excluded-field` deja de escanear líneas y pasa a escanear **ranuras de anotación**, extraídas por un reconocedor propio (`annotation_slots`): una celda de tabla, comparada por igualdad exacta como hasta ahora, o el texto que sigue a un link markdown dentro de un ítem de lista, comparado por palabra completa. La función se renombró a `check_excluded_fields`: ya no es «in_tables», y dejar el nombre viejo habría reincidido en lo que M-24 acababa de corregir.

**El diseño enunciado arriba se ejecutó más angosto, y el corpus dio la razón.** «Cualquier línea de contenido» habría marcado `../docs-y-investigacion/00-INDEX.md:17` —«Un modelo operativo SDD liviano, sin CI obligatorio…»—, que es prosa suelta bajo «Resultado esperado» y no anota el rol de nadie. Exigir el link no es un filtro conservador cualquiera: es lo que distingue una entrada de índice de una frase que menciona la palabra. El campo `validacion` de esa spec ya lo decía así —«ningún link ni tabla anota `ssot_level`/rol»—, de modo que el check ahora verifica la regla escrita en vez de una versión ensanchada de ella.

Límite declarado en el propio docstring: detecta el **valor** del campo, no su paráfrasis. De las tres anotaciones que el índice de línea B tenía el 2026-08-22, el check nuevo reproduce la primera (`— SSOT de convergencia…`) y **no** ve las otras dos (`Deriva de X.md`), porque `derivado` no aparece como palabra. Es el mismo límite de `scope-home`, que sólo matchea el campo escrito literal. Cerrarlo exige decidir antes qué paráfrasis cuentan como anotación, y esa es una pregunta sobre el registro, no sobre el check.

Validación, con la técnica del worktree histórico que ya usó la Fase 12: sobre el árbol de `b24549a` —anterior a la corrección manual— el check reproduce el caso real (`software/00-INDEX.md:20`, `link anota ssot_level/rol (SSOT)`). Sobre el árbol actual, cuatro deformaciones deliberadas en el mismo índice: un `Activo` junto a un link, detectado; un `Deriva de X.md`, no detectado —el límite declarado, comportándose como se declara—; una frase con «operativo» y «SSOT» sin link, no detectada; y una anotación dentro de un bloque de código, no detectada. Árbol restaurado, 0 ERROR.


## M-24 — `normative-block` cubría bastante menos de lo que su nombre prometía

`../AGENTS.md` lo describía como «la definición de un bloque normativo reproducida fuera de su SSOT». La implementación detecta una sola cosa: enumeraciones de los campos del bloque `[SDD-Check]`. Las dos descripciones no son la misma, y la ancha era la que el asistente leía.

Detectado el 2026-08-22: una revisión de `../AGENTS.md` encontró cinco reglas re-enunciadas ahí en vez de referenciadas —la regla de propagación, el léxico normativo, el formato de commit, el límite del verificador y la disambiguación—, y **ninguna de las cinco es detectable por el check**, porque ninguna es una enumeración de campos del `[SDD-Check]`. El repositorio estaba en 0 ERROR y no dijo nada. Es el mismo patrón que M-23 y que el propio M-09: el hueco no está en lo que el check hace, sino entre lo que hace y lo que se cree que hace.

Dos formas posibles, y no son la misma mejora:

1. **Barata y honesta**: ajustar la descripción de `../AGENTS.md` y el docstring para que digan lo que el check realmente hace. Cierra la falsa confianza sin tocar código. Es el piso, y conviene hacerlo aunque se haga también lo otro.
2. **Cara y de valor incierto**: ampliar el check a otros bloques normativos. Requiere primero decidir qué es un «bloque normativo» de forma mecánica —el `[SDD-Check]` lo es porque tiene delimitadores y campos con nombre; la regla de propagación es prosa— y sin esa definición no hay qué implementar. Riesgo alto de falsos positivos: toda referencia legítima menciona el tema que referencia.

**Recomendación: hacer (1) y dejar (2) sin aprobar** hasta que exista un criterio mecánico de «bloque normativo» que no sea una lista a mano —que es exactamente la deriva que `emitted_check_ids()` evita un nivel más arriba. La regla de disparadores del registro (§Reglas globales) cubre hoy este terreno por vía humana, y la spec de `../AGENTS.md` ya tiene el check de validación correspondiente.

**Hecha el 2026-08-23, con (1) ampliada y (2) sin aprobar.** La forma (1) fue un paso más allá de corregir la descripción: **el check se renombró a `sdd-check-fields`**. Razón, decidida al ejecutar: la descripción se lee una vez y el identificador se lee cada vez que alguien mira qué cubre un principio — y `../CONSTITUTION.md` lo declaraba como verificador del Principio I, que es donde una promesa ancha hace más daño. Tocó cuatro lugares: el script (id, función y docstring), el campo `Verificador:` del Principio I, la descripción de `../AGENTS.md` §Al cerrar una iteración, y las menciones de M-09 en este documento.

Lo que el renombre **no** arregla y quedó escrito donde se lee: el campo `Verificador:` del Principio I ahora declara que ningún check cubre la reproducción de una regla en prosa fuera de su SSOT —que es la forma más común de violar ese principio, y la que las cinco duplicaciones del 2026-08-22 tomaron—; el docstring del check declara su alcance exacto y sus tres puntos ciegos (tabla, `templates/`, `historial/`).

Validación: el renombre se corrió en rojo a propósito antes de tocar la constitución, y `constitucion` falló con «declara el check `normative-block`, que este script no emite» — el lazo que M-15 dejó armado, funcionando sobre un caso real y no sobre una deformación deliberada. Después de propagar, 0 ERROR.

`../historial/sdd.md` conserva el nombre viejo en las entradas de la Fase 12 y del 2026-08-22, a propósito: el historial registra lo que pasó cuando pasó y MUST NOT reescribirse hacia atrás.

Dos hallazgos del mismo trabajo que **no** entran acá: el punto ciego simétrico de `excluded-field` (escaneaba sólo tablas, mientras este escanea sólo listas), que es M-23 y se cerró al día siguiente; y la exención de `templates/`, que no tiene ítem propio y quedó anotada en el docstring a la espera de decisión.

## M-27 — `sdd-check-fields` no miraba `templates/`

El check saltea tres orígenes: `../AGENTS.md`, que es el SSOT del bloque y por eso no puede violarse a sí mismo; `../historial/sdd.md`; y `../templates/`. Los dos primeros están bien. El tercero era el peor lugar posible para no mirar: un template **es** método, se copia en cada experimento, y una definición reproducida ahí se propaga sola a cada instancia futura sin volver a pasar por ninguna revisión.

Detectado el 2026-08-23 leyendo la implementación al ejecutar M-24, no por un caso vivo. Se abrió y se cerró el mismo día porque medirlo costó menos que discutirlo.

La reserva razonable era que un template legítimamente muestra la forma de lo que se llena, así que quitar la exención podría inundar de falsos positivos. No ocurre, por dos motivos independientes: los templates de hoy hablan del bloque en prosa y no enumeran sus campos —quitar la exención no cambió nada en el árbol—, y la regla instancia/definición que el check ya tenía cubre el caso hipotético: un template que muestre el bloque para llenar lleva el literal `[SDD-Check]` al lado y no dispara.

`../historial/sdd.md` conserva la exención con motivo propio, ahora escrito en el código: el historial registra entregas pasadas y MUST NOT reescribirse hacia atrás, así que un WARN ahí no sería accionable.

**Hecha el 2026-08-23.** Validación en las dos direcciones sobre `../templates/EXPERIMENTO.md`: una enumeración de cuatro campos del bloque dispara el WARN, y la misma enumeración precedida del literal `[SDD-Check]` no dispara. Árbol restaurado, 0 ERROR.

Lo que este ítem **no** cierra es lo que M-24 dejó dicho: el check sigue viendo sólo enumeraciones de campos del `[SDD-Check]`. Ampliar el origen no amplía la clase detectada.

## M-28 — Encabezados que reproducen campos del registro

`estado`, `ssot_level`, `owner` y `deriva_de` son campos que `../SPECS_REGISTRY.md` declara para **todo** documento. Cuando un documento los repite en su encabezado crea una segunda fuente del mismo dato, que puede desincronizarse sin que nada lo señale. No depende de que el documento sea original o derivado: el registro es dueño de esos cuatro campos en los dos casos.

Casos vivos, detectados en la auditoría de encabezados del 2026-08-23:

1. `../docs-y-investigacion/GUIA-INICIO-PROYECTO-INVESTIGACION.md` abre con una tabla que trae columnas `ssot_level` y `owner`. Mezcla dos campos del registro con dos que no lo son (`Creacion`, `Version`), así que el arreglo es recortar columnas, no borrar la tabla.
2. `../software/SDD-EN-LEGACY-Y-BROWNFIELD.md` abre con «Estado: Borrador».
3. Cuatro documentos de línea B abren con «Deriva de: X». Tres coinciden con el registro; el cuarto —`../software/RELACION-SPEC-VS-EPICA.md`— afirmaba una derivación que el registro había borrado el 2026-08-03, y se corrigió el 2026-08-23. Ese caso es la evidencia de que la clase no es teórica: el registro cambió, el encabezado no, y la divergencia sobrevivió cinco meses sin que nada la marcara.

Los casos 1 y 2 coinciden hoy con el registro. Eso no los vuelve correctos, los vuelve **todavía no divergentes** — el estado exacto en que estaba `../software/00-INDEX.md` antes de la auditoría de M-14, que lo encontró diciendo «Borrador» sobre un documento ya `Activo`.

Forma de la mejora, y su parte barata: `excluded-field` ya sabe detectar esto —incluida la forma de tabla del caso 1 y la anotación junto a un link— pero sólo dispara cuando la propia spec del documento declara el campo en `excluye`. Hoy esa exclusión está escrita únicamente para los dos índices de línea. Escribirla en las specs de los documentos afectados los pone bajo verificación **sin código nuevo**; queda después limpiar los encabezados, que es trabajo de edición.

Reserva: la exclusión no debería escribirse documento por documento a mano si termina aplicando a todos. Si el barrido confirma que la regla es general —ningún documento anota campos del registro en su encabezado—, conviene decidir antes si se declara como regla global del registro en vez de repetirla en cada spec, que sería reintroducir la duplicación un nivel más arriba.

## M-25 — El sello MUST identificar el artefacto que constituye el tratamiento

**Regla propuesta.** Cuando el tratamiento de un experimento es material versionado del propio repositorio, el sello MUST identificarlo por commit —no por ruta— y la corrida MUST entregarlo **extrayéndolo de ese commit**, no copiándolo del árbol de trabajo. Una pasada que necesite un tratamiento distinto es una **pasada distinta**, con su enmienda fechada.

Aplica la jerarquía de M-22, que es su SSOT y no se reproduce acá. Lo que agrega este ítem es el modo de falla propio del componente: el tratamiento no se mueve por accidente ni por auto-actualización, se mueve **porque el repositorio trabaja**. Editar el artefacto es la actividad normal y correcta; lo que falta es que la corrida deje de depender de que nadie lo edite.

Por eso acá el escalón 1 alcanza casi entero, y eso cambia el balance del ítem. Extraer de un commit fijo cuesta lo mismo que copiar y **no impone ninguna restricción sobre el repositorio**: el trabajo sigue, el artefacto sigue evolucionando, y la pasada sigue entregando lo sellado. No hay que congelar nada ni declarar la pasada corrida sobre dos versiones — esa disyuntiva era un artefacto de haber pensado el control como alerta en vez de como construcción.

Queda un residuo, que es de otra clase y MUST no confundirse con lo anterior: si el artefacto evoluciona durante una pasada larga, el resultado describe una versión que ya no es la vigente. Eso es vigencia externa, no atribución; se acepta declarándolo y ningún verificador lo arregla.

El escalón 2 sobrevive como heartbeat: comprobar que lo entregado corresponde al commit sellado y no a un árbol sucio o a una extracción que falló en silencio.

Forma de la mejora: la sección de sello de `../templates/EXPERIMENTO.md` (pieza 1 de M-22) exige commit para todo tratamiento que sea material del repositorio y extracción desde ese commit; el script de preparación comprueba la correspondencia. Aplicación a los runbooks vigentes al adoptarla.

**Caso que la originó** (evidencia, no alcance). El brazo tratamiento de A-04 entrega `../AGENTS.md` al workspace del agente; el runbook (`../experimentos/a04-conducta-agente/PRUEBA-PISO-RUIDO-A4.md`) sella el fixture por hash, audita ancestros y verifica ausencia de configuración de asistente, pero no fija con qué commit se entrega el tratamiento — la variable independiente era el único componente sin identificar. El 2026-08-22 `../AGENTS.md` cambió dos veces —alta de `../CONVENCIONES.md` y declaración de §Qué NO hacer como índice— y nada en el aparato lo registró. No se invalidó nada: ni la pasada 1 ni la 1b produjeron dato de `H1` válido, y la pasada 2 no corrió. Pero el mismo cambio entre dos tandas de una pasada 2 habría dejado el efecto medido sin a qué atribuirse.

## M-26 — «Qué decisión habilita» es un MUST sin casillero donde satisfacerse

`../AGENTS.md` §Criterios de calidad mínima exige que cada cambio indique qué decisión habilita. A diferencia de `Derivados a revisar` o `Deuda arrastrada`, no tiene campo en el bloque `[SDD-Check]`: no hay lugar donde escribirlo ni dónde verificar que se escribió.

Detectado el 2026-08-22 en la revisión de `../AGENTS.md`. No es contradicción —nada lo prohíbe—, es un MUST que en la práctica se cumple o no según se acuerde el asistente.

Dos salidas, y la elección no es obvia:

1. **Campo nuevo** en el bloque. Le da lugar mecánico y lo vuelve verificable por presencia. Costo: una línea más en **cada** entrega, para una exigencia que muchas veces se responde con una obviedad («habilita seguir escribiendo el documento»), y el bloque ya tiene siete campos.
2. **Bajar el MUST a SHOULD**, reconociendo que es un criterio de juicio y no una casilla. Costo: pierde fuerza justo en los cambios donde importa, que son los que no habilitan nada y nadie nota.

Ninguna es claramente mejor. Conviene decidirla junto con cualquier otra revisión del bloque `[SDD-Check]`, no sola.
