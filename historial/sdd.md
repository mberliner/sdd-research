# Historial SDD

Registro de fases y mejoras completadas al sistema SDD del proyecto.

---

## Fase 10 — Backstop determinista de documentación, M-01 (2026-07-31) — COMPLETADA

**Acción**: implementar la primera capa de verificación mecánica del repositorio, portando a un repo documental la capa 2 del enforcement de tres capas del testigo (`docs/SDD-ENFORCEMENT.md`).

### Qué hace
`tools/check_docs.py`, stdlib pura, dos severidades (ERROR falla; WARN informa, o falla con `--strict`). Ocho checks: cobertura de spec con exenciones declaradas; el registro no apunta a archivos inexistentes; links internos; `[Rxx]` usadas contra el catálogo y sin duplicados; valores válidos de `ssot_level`/`estado` y coherencia de `deriva_de`; ciclos en la cadena `deriva_de`; alcance en un solo lugar (campos de spec fuera del registro); cadena de precedencia; emoticones.

Límite heredado y declarado en el propio docstring: **verifica presencia y forma, no adecuación**. Que un documento tenga spec no dice que la spec lo describa bien.

### Qué encontró la primera corrida
41 documentos, 6 ERROR y 22 WARN. Desglose honesto:
- **2 ERROR eran deriva real**, ambos de la misma clase y ambos de un día de antigüedad: `software/ANALISIS-SPEC-KIT.md` C4 decía «nuestra precedencia `SPECS_REGISTRY.md`» y `templates/RESULTADO-EXPERIMENTO.md` decía «Es precedencia 1» sobre el registro, que desde la Fase 8 es precedencia 2. Los dos documentos habían sido revisados a mano el mismo día, dentro de la propagación de la Fase 8, y los dos se escaparon.
- **1 ERROR era un hueco anterior**: `experimentos/PREREG-B7.md` sin spec registrada. Es un pre-registro autorado, no generado desde template, así que la exención de `experimentos/` no lo alcanza — el mismo criterio que el 2026-07-30 obligó a registrar los runbooks. Se le escribió spec (`derivado` de `PRUEBA-REGENERABILIDAD-B7.md`), con la advertencia explícita de que describe un documento sellado y MUST NOT usarse para reescribirlo.
- **3 ERROR eran falsos positivos** del check de precedencia: disparaba dentro de bloques de código, no reconocía «esta constitución» escrito en prosa, y usaba una ventana que no miraba hacia atrás. Corregido: se ignoran los fences, se acepta la palabra además del nombre de archivo, y la ventana va de −4 a +12 líneas.
- **20 WARN eran ruido de diseño**: «spec sin campo `owner`» en casi todas. En un repo de un solo equipo, escribir 25 veces el mismo owner es ruido; se declaró en el registro que `owner` ausente significa `proyecto SDD` y se quitó el check. Los 2 WARN restantes (specs sin `proposito` en bloques que declaran dos paths) se corrigieron escribiendo el campo.

Estado final: **0 ERROR, 1 WARN** — los emoticones de `PREREG-B7.md`, que quedan vivos a propósito porque son M-08, decisión pendiente sobre un documento sellado.

### Cómo se validó
La corrección de los falsos positivos se verificó contra los dos positivos verdaderos: tras afinar la heurística, ambos siguen detectándose. El check se corrió también con `--strict` para confirmar que la única diferencia es el WARN esperado.

### Deuda abierta
- El checker **no verifica su propio criterio de separación** método/investigación (Fase 9): nada impide dar de alta una tarea de método en el backlog de investigación.
- No está cableado a `pre-commit`; hay que acordarse de correrlo. Cablearlo depende de decidir M-02.
- Sigue sin cubrir adecuación: los dos positivos verdaderos de hoy fueron de forma. Una spec que describe mal a su documento pasa igual.

---

## Fase 9 — Separación de agenda de método y agenda de investigación (2026-07-31) — COMPLETADA

**Acción**: dar un hogar priorizado a las mejoras de método pendientes de la Fase 8, sin mezclarlas con las preguntas abiertas de investigación.

### Diagnóstico
La lista de mejoras existía solo como prosa en la Fase 8 y en la conversación que la produjo — el modo de fallo que el proyecto combate (deuda sin índice, que muere en silencio). El destino que parecía natural, `ROADMAP-MEJORAS-SDD.md`, no servía por dos razones independientes: está declarado **CERRADO / HISTÓRICO** desde 2026-06-01 con la advertencia de que su contenido en presente describe el estado previo a la Fase 1, y su `proposito` lo ata a una fuente única (proyecto "Transformacion AI-Native Org") que no es la nuestra. El otro candidato, `../agenda/BACKLOG-INVESTIGACION.md`, es agenda de **investigación**: mezclarle tareas de método contradice el Principio VI recién ratificado.

Además, la revisión del backlog encontró tres solapamientos reales con lo nuevo:
- Exploratoria #1 «evaluación automática parcial sin CI» **era** la mejora M-01, en estado exploratorio pese a estar aprobada — conflicto de estado.
- Transferencia Spec Kit #2 (marcador `[NEEDS CLARIFICATION]`) figuraba como candidato **y ya estaba adoptado** en `AGENTS.md`.
- Enriquecimientos R25/R30 #3 (modelo confirmado/inferido/gap) es una convención de escritura — método, no pregunta.

### Cambios aplicados
- **`../agenda/MEJORAS-METODO.md` (nuevo)**: criterio de separación explícito frente al backlog, tabla de estado con IDs `M-01`..`M-08` (prioridad, estado, origen, destino) y detalle por mejora. Estados: `Propuesta` / `Aprobada` / `Hecha` / `Descartada`; una mejora que se aprueba no cambia de documento, cambia de estado.
- **`../agenda/BACKLOG-INVESTIGACION.md`**: encabezado que declara su naturaleza (preguntas que se cierran con evidencia, no con una edición) y remite a `../agenda/MEJORAS-METODO.md`; exploratoria #1 reformulada como la pregunta que M-01 permite responder, con la construcción del script migrada; transferencia Spec Kit #2 marcada como adoptada; R25/R30 #3 migrado a M-06.
- **`SPECS_REGISTRY.md`**: spec de `../agenda/MEJORAS-METODO.md`; `incluye`/`excluye`/`validacion` del backlog reescritos con el criterio de separación; spec de `ROADMAP-MEJORAS-SDD.md` marcada como registro histórico cerrado que no recibe items nuevos; fila en la tabla SSOT.
- **`00-INDEX.md`** y **`README.md`**: alta del documento nuevo y rol de cada backlog diferenciado.

### Cómo se validó
Links internos: 0 rotos. Los tres solapamientos detectados quedaron con una sola representación cada uno: M-01 como tarea con su pregunta hermana en el backlog, el marcador `[NEEDS CLARIFICATION]` como adoptado, y M-06 en un solo documento. `BACKLOG-INVESTIGACION` alta #4 (gates que fallan abierto) se mantuvo del lado de investigación y se citó desde M-02 como requisito de diseño fail-closed, sin duplicar su contenido.

### Deuda abierta
- M-01 a M-08 sin ejecutar; M-01 es el próximo por valor.
- El criterio de separación es una regla escrita más, sin verificación: nada impide dar de alta una tarea de método en el backlog. Lo atraparía M-01 solo si se le agrega un check específico.

---

## Fase 8 — Versionado, constitución y alcance en un solo lugar (2026-07-31) — COMPLETADA

**Acción**: incorporar al repositorio de análisis las mejoras de método maduradas en el proyecto testigo `evaluador-flujo-intent`, empezando por las que no requieren tooling.

### Diagnóstico
Comparación del repo contra el testigo (HEAD `ded63e5`). La higiene documental estaba sana —0 links internos rotos, 36/36 referencias `[Rxx]` definidas—, pero faltaban tres piezas de método: (1) ninguna capa de invariantes por encima del registro, de modo que reglas duras (propagación, nacida del incidente B-07) convivían al mismo nivel que convenciones de forma; (2) el repo **no estaba versionado en ningún nivel**, sin baseline ni diff antes de tocar los documentos de mayor precedencia; (3) el alcance de cada documento estaba duplicado — medido: **11 filas de `00-INDEX.md` repetían el `proposito` del registro y 5 ya habían derivado**, perdiendo la procedencia de `ROADMAP-MEJORAS-SDD.md` y el alcance «contexto del repositorio» de `AGENTS.md`.

### Cambios aplicados
- **Versionado**: `git init` en `SDD/` con baseline `499c44a` (40 archivos) antes de cualquier edición. `.gitignore` excluye `fuentes-externas/` (material vendored con `.git` anidado; su versión sigue anclada en `REFERENCIAS.md`), caches y config local del asistente.
- **`CONSTITUTION.md` (nuevo, v0.1.0)**: siete invariantes con la anatomía del testigo —invariante autocontenido + `Enforcement` + `Detalle`— más governance semver, fase pre-1.0 y procedimiento de enmienda. Principios: I SSOT único por tema; II trazabilidad de afirmación a fuente; III propagación bidireccional; IV documento autorado, spec registrada; V integridad del registro experimental; VI separación método/contenido; VII preguntar antes que interpretar. Declara explícitamente su **límite honesto**: el enforcement es humano y a pedido.
- **Precedencia a cuatro niveles** (`CONSTITUTION.md` → `SPECS_REGISTRY.md` → `AGENTS.md` → criterio), con división de trabajo declarada: la constitución dice *qué nunca cede*, el registro *cómo se aplica hoy*.
- **Regla de alcance en un solo lugar** (`SPECS_REGISTRY.md` §Reglas globales, operativa del Principio I): `proposito`/`incluye`/`excluye`/`validacion` viven solo en el registro; el índice declara **rol**, no propósito; el encabezado de un doc puede llevar una línea de identidad pero no enumerar incluye/excluye. Migración oportunística para los encabezados preexistentes.
- **`00-INDEX.md` a navegación pura**: se eliminó la columna «Contenido» y también el «Mapa de SSOTs», que duplicaba la tabla SSOT del registro. La tabla quedó en el registro y no en el índice porque de ella depende la regla de propagación, y ahí tiene precedencia 2.
- **`AGENTS.md` reescrito** (119 → 118 líneas, con más contenido y menos duplicación): orden de lectura que arranca por la constitución, sección «Al cerrar una iteración» (registro, historial, commit), sección «Qué NO hacer» con cada ítem anclado a su principio. Se eliminó la reproducción de la regla de propagación —que el propio documento declaraba delegada al registro tres líneas antes— y las convenciones de forma, ahora referenciadas.
- **Propagación**: `software/ANALISIS-SPEC-KIT.md` (fila de autoridad del mapeo + nota fechada en C4: se adoptó la parte declarativa del patrón, no la ejecutable, y la pregunta de C4 sigue abierta); `software/00-INDEX.md` y `docs-y-investigacion/00-INDEX.md` (repetían la cadena de precedencia sin la constitución); `README.md`.

### Cómo se validó
Links internos: 0 rotos antes y después. Cadena de precedencia coherente en los cuatro documentos que la mencionan. La medición de divergencia del `proposito` se hizo con script contra el registry, no a ojo. La spec de `CONSTITUTION.md` se escribió en el mismo lote que el documento — inversión del Principio IV que se declara acá como excepción de bootstrap, no como precedente.

### Deuda abierta
- **P3 y P4 sin implementar**: backstop determinista (`check_docs.py`) y gate de autoría, las dos capas que convertirían el `validacion` de checkbox en verificable. Aprobadas como mejora de método, no como experimento. Mientras no existan, la constitución se cumple por disciplina.
- **P5 y P7 sin abrir**: playbooks agnósticos de asistente y formato/compactación de documentos.
- Los **encabezados de documento** que restatan su alcance (al menos `../comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md`) siguen duplicando: migración oportunística, no barrido.
- `AGENTS.md` e `../comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md` describen un contexto **sin CI**; sigue siendo cierto, pero ahora hay git, y eso habilita `pre-commit` como sustrato de P3/P4. Revisar ambos cuando se implementen.

---

## Fase 7 — Aparato de evaluación de B-07: R6, degradación de H2 y criterio reformulado (2026-07-29) — COMPLETADA

**Acción**: cerrar las deudas que el cierre de B-07 dejó en su propio aparato de medición, sin tocar ningún valor medido ni el veredicto.

### Cambios
- **Alta de `R6` (verificación funcional manual)** en el SSOT del experimento + §3.7 del runbook. Motivo: `R1` se automatizó con `pytest`, luego midió **sólo el subconjunto pytest-verificable**; la doctrina del propio testigo asigna los `FR` de UI y de consistencia documental a verificación visual (relación requisito↔verificador **N:M**). `R6` exige recorrido guionado pre-registrado y observación de **comportamiento, no de fuente** (el fuente des-ciega el formato). No se midió en B-07.
- **Medición exploratoria post-cierre, NO ciega**, de los 13 requisitos de `SPEC-013` que quedaron fuera del denominador: **9 eran mecanizables** (5 por gate objetivo del repo, 4 por suites que existen en `ENV-REF` pero quedaron fuera de `TESTS-F013`) y están **satisfechos en ambas celdas** ⇒ el espacio no medido no escondía señal. Sensibilidad al denominador: extendido 25→34, la brecha por requisito pasa de 100/64 a **100/74** — misma dirección, menor magnitud. Quedan **4 requisitos sin ningún dato**, todos de UI.
- **`H2` degradada a descriptiva.** Dos motivos independientes: su ratio upfront/reactivo **no es computable** (`[NEEDS CLARIFICATION]` no existe en la anatomía casero — es **`N/A`, no `0`**), y su variable de salida está **confundida con el tratamiento** (una práctica documental altera la visibilidad de su propio resultado; los conteos crudos van en dirección contraria a H2). Se conserva la lectura cualitativa.
- **Anti-patrón nuevo en `BACKLOG-INVESTIGACION` #6**: *variable de salida que es artefacto del propio tratamiento (confusión de visibilidad)*, con el corolario operativo **`N/A` ≠ 0** y el test de diseño «¿la variable de salida sobreviviría si el tratamiento no existiera?».
- **Criterio de éxito REFORMULADO** —la deuda que venía abierta desde la Fase 5— en **(a)** prueba de regenerabilidad contra `R1`–`R6` (unidad intra-feature; `R1` mayor + `R2` menor + **≥1 secundaria independiente** en el mismo sentido y ninguna en contra, admisibles `R4`/`R5`/`R6`, `R3` excluida por no ser independiente de `R1`; empate ⇒ no concluyente; veredicto global sólo con ≥2 features discriminantes; **guarda de confusión** con techo *"no atribuible al formato"*) y **(b)** corpus observacional contra **`H1`+`H3`** (sólo Tier A; no-solapamiento de rangos; techo **descriptivo**), más **regla de cierre a dos veredictos**. Ambos pasan la comprobación de satisfacibilidad.
- **§Propagacion escrita en `RESULTADO-EXPERIMENTO-B7.md`** —faltaba, y era la deuda 4.5 real— con los **tres checks efectivamente corridos** y triaje de 11 filas. Corregido también el encabezado stale *"(propuestas, NO aplicadas)"*: 3 de 4 cambios al marco **ya estaban aplicados**.

### Verificación
Aplicar el criterio (a) a la prueba ya ejecutada **reproduce el veredicto existente** (H4 no sostenida, F001 no concluyente, techo "no atribuible"): lo que cambia es que el criterio pasa de **no evaluable en bloque** a **evaluable**. Confirmado empíricamente que **ningún check de propagación basta solo**: los 4 archivos que devolvió el check 3 estaban ya cubiertos o justificados, y los 5 realmente afectados por estos cambios **no aparecen en el check 3**.

### Deuda abierta
- **Camino crítico para cerrar B-07 integralmente**: reescribir `experimentos/PRUEBA-OBSERVACIONAL-B7.md` como runbook real (le faltan «Definicion operacional» y Fase 0 sellada; su corte debe fijarse en `3f1ed33` porque el ciclo de vida del corpus es **pre-git**) → **medir `H1` y `H3`** → cerrar con los dos veredictos.
- `R6` sin recorrido guionado pre-registrado; 4 requisitos de UI de `SPEC-013` sin dato.
- Desambiguar formato vs. procedencia (Hallazgo 2) **requiere corrida nueva**: es otro experimento, no una tarea de cierre.
- La reserva de método queda declarada: el criterio (a) se redactó conociendo los resultados; gobierna réplicas y no reabre el veredicto.

---

## Fase 6 — Propagación al cerrar un experimento (2026-07-29) — COMPLETADA

**Acción**: cerrar el hueco estructural que dejó ver el cierre de B-07 — un experimento produce conocimiento nuevo **sin modificar ningún SSOT**, así que la regla de propagación no se disparaba y la sincronización dependía del recuerdo de quien cerraba.

### Diagnóstico
Al cerrar B-07 (2026-07-28) el `[SDD-Check]` listó tres derivados y los tres se sincronizaron; la lista se había armado de memoria y omitió cuatro documentos —entre ellos `software/LINEAS-INVESTIGACION.md`, que es **SSOT** y quedó atrás de su propio derivado `PLAN-PRUEBAS.md`. Tres causas independientes:
1. `experimentos/` está exento de spec (`SPECS_REGISTRY.md` §Docs excluidos) ⇒ fuera del grafo SSOT ⇒ nada dispara.
2. La regla de propagación era **unidireccional** (SSOT → derivados), pero el conocimiento de una ejecución entra por abajo y tiene que subir. Contradecía la tesis bidireccional del propio proyecto (`../comun/SDD-ADAPTATIVO-VS-CASCADA.md`).
3. `Derivados a revisar` se poblaba de memoria, sin índice.

### Cambios aplicados
- **`templates/RESULTADO-EXPERIMENTO.md`**: sección **«Propagacion» obligatoria**, con **tres checks** y tabla de triaje. (1) grep del ID en `SPECS_REGISTRY.md` — las cláusulas `incluye`/`excluye` suelen justificarse con el estado del experimento; (2) el SSOT dueño de la hipótesis y sus derivados según la tabla SSOT — único check que ve a quien afirma el estado **sin declararlo como deuda**; (3) `grep -rl "Deuda arrastrada.*<ID>"` — captura documentos lejanos que ningún índice conecta con el experimento.
- **`templates/EXPERIMENTO.md`**: sección **«Documentos que esperan este resultado»**, contraparte del check 3 en el pre-registro.
- **`templates/RESULTADO-EXPERIMENTO.md` §Deuda arrastrada**: la deuda no resuelta MUST migrar a `../agenda/BACKLOG-INVESTIGACION.md` antes de cerrar. "Re-explicitarse en el siguiente cierre" ataba la deuda a que existiera otro experimento; si no lo hay, muere en silencio.
- **`AGENTS.md`**: regla de propagación **ascendente** en §Criterios de calidad mínima, y check de post-generación para el cierre de experimentos.
- **`SPECS_REGISTRY.md`**: la regla, donde tiene precedencia 1 — propagación ascendente y disparador por cierre de experimento, con la aclaración de que la exención de `experimentos/` es de **spec propia**, no de **propagación**. Se corrigió además la columna «Quien referencia» de ambos `PLAN-PRUEBAS.md`, que decía `templates/` (dirección invertida) siendo que el plan se apoya en esa columna como índice inverso.

### Cómo se validó
Prueba en seco de los tres checks contra el cierre real de B-07: reproducen exactamente los cuatro documentos corregidos a mano el 2026-07-29. **El check 3 aislado sólo encuentra dos** —`COMPARATIVA` y `DECISION`, que sí habían declarado deuda desde 2026-05-28— y no ve a `LINEAS-INVESTIGACION` ni al registry, que afirmaban el estado sin anotarlo como pendiente. Ese punto ciego, detectado por la propia verificación, es el motivo de que el mecanismo tenga tres checks y no uno.

### Deuda abierta
- Los tres checks son **manuales** (proyecto sin CI): nada impide cerrar un experimento salteándolos. Es el mismo modo de fallo que el anti-patrón *gate fail-open* que B-07 dejó registrado en `BACKLOG-INVESTIGACION` #4.
- Sin cobertura para documentos que afirman el estado de un experimento **y** no están en el registry **y** no declararon deuda. No hay caso conocido; el riesgo se declara.
- ~~Sigue abierto de la Fase 5: reformular el Criterio de éxito de B-07 (requiere decisión del usuario) y registrar el anti-patrón *fail-open* como regla del marco.~~ **CERRADO en la Fase 7 (2026-07-29)**: criterio reformulado en (a)/(b) y anti-patrón *fail-open* ya en `BACKLOG-INVESTIGACION` #4.

---

## Fase 5 — Ejecución y cierre de B-07 (prueba de regenerabilidad) (2026-07-11 → 2026-07-28) — COMPLETADA

**Acción**: ejecución completa del runbook `experimentos/PRUEBA-REGENERABILIDAD-B7.md` sobre el proyecto testigo, en un directorio de trabajo externo al repo (`/datum1/Descargas/Claudio/experimentosdd-b7/`, bitácora append-only propia). Cierre en `experimentos/RESULTADO-EXPERIMENTO-B7.md`.

### Qué se ejecutó
- **Fase 0** — pre-registro sellado en el tag `b7/prereg-v1`; 4 specs del 2×2 (2 auténticas + 2 traducidas spec→spec por un `Traductor` independiente); `SELLO-CIEGO` generado y custodiado por el usuario, nunca visible para el orquestador.
- **Fase 1** — dos baselines por sustracción (`b7/base-f001-v1`, `b7/base-f013-v2`), validados con gate objetivo (compila + frontera completa + verificación de ausencia).
- **Fase 2** — 4 regeneraciones one-shot en sesiones frescas, salidas en ramas ciegas `b7/run-a..d`. Tasa `VOID` 1/5.
- **Fase 3 y 3-bis** — métricas `R1`–`R5` en las 4 celdas, con *tooling* determinista y re-ejecutable; lazo de reparación acotado (`K=3`).
- **Fase 4** — des-ciego, proyección de `R1` a requisitos en F013 (mapeo construido a ciegas y congelado con hash antes de aplicarse), veredicto y resultado.

### Resultado
En la única feature que discriminó (F013) el formato **casero** superó al híbrido en `R1`, `R2` y `R5`; F001 empató en las cinco métricas. **H4 no queda sostenida, pero tampoco refutada**: en F013 el eje formato está perfectamente confundido con el eje spec auténtica/traducida, y una sola ronda de reparación borra la diferencia (las 4 celdas llegan a 100%). **Decisión: Ajustar** — no se adopta ni se descarta el formato híbrido.

### Cambios al sistema SDD aplicados a raíz del experimento
- **`templates/EXPERIMENTO.md`**: sección **«Definicion operacional» obligatoria** (denominador, aislamiento, validación del instrumento, granularidad, admisibilidad de reconciliaciones, regla de agregación, tratamiento del empate, independencia entre métricas, quién mide) y **«Criterio de exito» reforzado** con comprobación de satisfacibilidad. Origen: el pre-registro de B-07 fijaba *qué* medir pero no *cómo*, y acumuló **ocho enmiendas post-hoc** al runbook.
- **`SPECS_REGISTRY.md`**: la spec de los templates incorpora esos dos checks; se agregaron los campos `path` faltantes en las dos entradas combinadas (templates e índices de línea), que los hacían invisibles a cualquier verificación mecánica de cobertura.
- **`software/PLAN-PRUEBAS.md`** y **`experimentos/EXPERIMENTO-B7-formato-hibrido.md`**: estado de B-07 sincronizado (de "pre-registrado" a métrica primaria cerrada), con la distinción explícita entre la prueba de regenerabilidad (cerrada) y el corpus observacional de secundarias (sin medir).

### Deuda abierta
- **Reformular el Criterio de éxito de B-07** en `EXPERIMENTO-B7-formato-hibrido.md` (SSOT): resultó **no evaluable** — no define agregación y su cláusula "≥2 secundarias" mezcla las del corpus observacional con las de la prueba. Nota fechada ya inscrita en el doc; la reformulación **requiere decisión del usuario**.
- **Desambiguar formato vs. procedencia**: es el límite principal del resultado y no es reparable con los datos existentes.
- **Hallazgos transferibles** ya registrados en `../agenda/BACKLOG-INVESTIGACION.md`: gates de gobernanza que fallan abierto (#4) y régimen de permisos en experimentos de regeneración (#5).

---

## Verificación en fuente completa de R25/R30/R33/R34 (2026-07-10)

**Acción**: lectura completa de las cuatro fuentes vendored en `fuentes-externas/` (LaTeX arXiv) que estaban sin verificar en fuente completa; auditoría de todas las citas `[Rxx]` que dependen de ellas.

### Veredicto: las cuatro siguen siendo relevantes; ninguna cita requirió corrección
- **[R25] Reversa** (`arXiv-2605.18684v1/`): el uso en `software/SDD-EN-LEGACY-Y-BROWNFIELD.md` (existe trabajo formal en retro-specs legacy para agentes) es fiel y modesto. Anotada su naturaleza en `REFERENCIAS.md`: caso exploratorio único COBOL→Go incompleto (9/11 tareas; sin paridad final ni cutover), sin comparación controlada — no citar como evidencia de efectividad.
- **[R30] Piskala** (`arXiv-2602.00180v1/`): technical report de autor único, no peer-reviewed. Las tres citas en `../comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md` (intent drift, contrato multi-agente, regeneración reduce divergencia) están respaldadas textualmente. Anotado: su cifra "hasta 50 % menos errores" viene de secundarias — no usar como dato primario. Bonus para B-07: taxonomía spec-first/spec-anchored/**spec-as-source** (la regenerabilidad primaria de B-07 es su nivel spec-as-source).
- **[R33] Rosa et al.** (`arXiv-2601.03878v1/`): confirmado todo lo citado en `experimentos/EXPERIMENTO-B7-formato-hibrido.md` (tarea aislada between-subjects, endpoint/prompts/parámetros fijos, métricas, TaskId como blocking factor). Precisión anotada: es protocolo Stage 1 **sin resultados aún**; el modelo se elegirá open-weight en ejecución.
- **[R34] RepoExec** (`arXiv-2406.11927v4/`): confirmado literal en abstract ("smaller context sizes can be misleading", 18 modelos, pretrained vs instruction-tuned, DIR). Autor primero corregido: Le Hai et al. (no Nguyen). Hallazgo adicional anotado: correlación pass@1↔DIR y riesgo de reimplementar dependencias en vez de invocarlas.

### Actualizaciones en positivo aplicadas (aprobadas por el usuario)
- `experimentos/EXPERIMENTO-B7-formato-hibrido.md`: (1) H4 encuadrada en la taxonomía spec-first/spec-anchored/spec-as-source [R30] — la regenerabilidad primaria es el test operativo del nivel spec-as-source, lo que da escala graduada al resultado; (2) métrica **R4 nueva** (invocación vs. reimplementación de contratos de la frontera in-spec, análogo del DIR [R34]) — captura el modo de fallo "verde en R1, limpio en R2, pero mal integrado al sistema"; (3) precisión de fidelidad: [R33] fija endpoint/prompts/parámetros (no seed; modelo a elegir en ejecución; Stage 1 sin resultados).
- `../agenda/BACKLOG-INVESTIGACION.md`: sección nueva "Enriquecimientos diferidos desde verificación de fuentes R25/R30" (regla de rigor mínimo y pitfalls de [R30]; modelo confirmado/inferido/gap de [R25] como convención candidata de Línea A).

---

## Actualización clon Spec Kit [R10]: v0.8.13 → v0.12.11.dev0 (2026-07-10)

**Acción**: `git pull` deliberado del clon vendored `fuentes-externas/spec-kit/` (`a08af08` 2026-05-22 → `983a87f` 2026-07-10; 374 commits, 4 versiones menores 0.9→0.12).

### Diff dirigido contra `software/ANALISIS-SPEC-KIT.md` (basado en snapshot v0.8.13)
- **Ninguna conclusión invalidada.** Tesis "Power Inversion", coverage mapping de `/speckit.analyze` (C1), C2 y C3 siguen vigentes.
- **Cambio conceptual 1 — Artículos IV, V y VI ahora explícitamente *project-defined governance*** (`spec-driven.md` upstream; CHANGELOG 0.11.6). Refuerza, no contradice, el enfoque del testigo (gate de integridad de la constitución). La estructura de 9 artículos se mantiene estable.
- **Cambio conceptual 2 — comando nuevo `/speckit.converge`** (0.11.2, documentado 0.11.10). No cubierto por el análisis; candidato a incorporar si se re-analiza el set de comandos.
- **Resto = infraestructura, no conceptual**: script types Python en templates, `specify self upgrade` / `specify bundle`, git como extensión opt-in (0.10.0, elimina `--no-git`), `/speckit.analyze` en subagente forkeado (0.11.3), múltiples integraciones de agentes y presets de governance.

### Pendiente (deuda arrastrada)
- `ANALISIS-SPEC-KIT.md` sigue anclado a v0.8.13; incorporar `/speckit.converge` y la aclaración de artículos project-defined requiere edición aprobada (no ejecutada en esta actualización).

---

## Fase 4 — Catálogo de escenarios que justifican SDD (2026-06-06) — COMPLETADA

**Alcance**: consolidar, con investigación web, el catálogo de problemas/escenarios que hacen necesario SDD hoy, separando modos de fallo (cualitativo) de cifras (cuantitativo).

### Archivos creados
- `../comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md` (SSOT, común): causas raíz transversales; escenarios por línea A, B y transversales; mapa escenario → eje SDD. Referencia `ESTADISTICAS` (cifras) y `SDD-ADAPTATIVO-VS-CASCADA` (cascada) sin duplicarlos.

### Archivos modificados
- `REFERENCIAS.md`: alta de [R28] (dplooy, marcada como secundaria), [R29] (Red Hat Developer), [R30] (arXiv "From Code to Contract").
- `../comun/ESTADISTICAS-TENDENCIAS-EVOLUCION.md` (SSOT): nueva subsección "Calidad del código generado por IA y señal de adopción SDD" con cifras secundarias [R28] marcadas como tales.
- `SPECS_REGISTRY.md`: spec nueva para `../comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md`; alta en tabla SSOT.
- `00-INDEX.md`: ruta recomendada, estructura y mapa de SSOTs.

### Reserva
Las cifras de [R28] son de fuente divulgativa (secundaria); marcadas como tales y pendientes de verificar contra fuente primaria antes de elevar su peso argumental. Deuda arrastrada hasta esa verificación.

---

## Fase 3 — Aplicacion de mejoras B-06 y comparativa Spec Kit/testigo (2026-06-01) — COMPLETADA

**Alcance**: cierre de la "Decision pendiente" de Fase 2 (dos propuestas de B-06 aprobadas y aplicadas), formalizacion del experimento B-07 y de la comparativa Spec Kit vs. testigo.

### Decisiones aplicadas (propuestas de B-06, antes pendientes)
1. **"Deuda arrastrada" formalizada como artefacto del marco.** Campo `Deuda arrastrada` anadido al bloque `[SDD-Check]` (`CLAUDE.md`) y seccion homonima en `templates/RESULTADO-EXPERIMENTO.md`. Mecanismo anti-cascada: re-explicitar lo diferido hasta resolverlo.
2. **Umbral de cascada reformulado de absoluto a relativo.** `../comun/SDD-ADAPTATIVO-VS-CASCADA.md` (SSOT) reemplazo "30 dias absolutos" por "2-3 iteraciones o ciclos de cierre"; los 30 dias quedan solo como equivalencia de referencia. Derivados revisados: implicaciones por linea y senales de salud, ya alineadas.

### Archivos creados
- `software/COMPARATIVA-SPECKIT-VS-TESTIGO.md` — comparacion en 5 dimensiones (derivado de `ANALISIS-SPEC-KIT.md`); enlazada desde `software/00-INDEX.md`.
- `experimentos/EXPERIMENTO-B7-formato-hibrido.md` — pre-registro del experimento de formato hibrido (Spec Kit vs. casero) sobre el testigo.

### Archivos modificados
- `CLAUDE.md`: campos `Cobertura` y `Deuda arrastrada` en el bloque `[SDD-Check]`; convencion `[NEEDS CLARIFICATION]`.
- `../comun/SDD-ADAPTATIVO-VS-CASCADA.md` (SSOT): ventana de inactividad relativa; mecanismo "Deuda arrastrada"; aclaracion regenerabilidad vs. adaptatividad.
- `software/LINEAS-INVESTIGACION.md` y `software/PLAN-PRUEBAS.md`: alta de hipotesis/experimento B7.
- `SPECS_REGISTRY.md`: specs nuevas para `COMPARATIVA-SPECKIT-VS-TESTIGO.md`.

### Revision de consistencia (este mismo cierre)
- `ROADMAP-MEJORAS-SDD.md` marcado como **CERRADO/HISTORICO**: sus mejoras 1-10 ya vivian en `SPECS_REGISTRY.md`/`CLAUDE.md` desde Fase 1; el doc se conserva como registro pero ya no se lee en presente.
- `../comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md` (SSOT): GitHub Spec Kit recategorizado de Linea A a **Linea B (software)**, coherente con su caracterizacion "Linea-B-nativo" en `ANALISIS-SPEC-KIT.md`.
- `REFERENCIAS.md`: alta de `[R19]` (Karpathy LLM Wiki) para resolver una colision de ID en `BACKLOG-INVESTIGACION` (citaba el gist como `[R01]`).
- Correcciones menores: renumeracion de la ruta en `00-INDEX.md`; conteo de archivos en Fase 1.

---

## Fase 2 — Analisis de GitHub Spec Kit (2026-05-24) — COMPLETADA

**Alcance**: Investigacion del repositorio GitHub Spec Kit (v0.8.13, [R10]), creacion del analisis comparativo para Linea B y reordenamiento del material fuente externo.

### Decision: separar material fuente externo
Se introduce el directorio `fuentes-externas/` para repositorios externos clonados (vendored), separandolos de los docs autorados por el proyecto. El clon `software/spec-kit/` se movio a `fuentes-externas/spec-kit/` (con su `.git` intacto para `git pull` en re-analisis). Registrado como exclusion en `SPECS_REGISTRY.md`.

### Archivos creados
- `software/ANALISIS-SPEC-KIT.md` — analisis del flujo de Spec Kit, mapeo contra nuestro protocolo y conclusiones C1-C5 para Linea B. Linea A diferida.

### Archivos modificados
- `SPECS_REGISTRY.md`: exclusion de `fuentes-externas/`; spec nueva para `software/ANALISIS-SPEC-KIT.md`.
- `REFERENCIAS.md`: [R10] anclado a version v0.8.13 (consultada 2026-05-21) + ruta del clon vendored y politica de actualizacion.
- `../comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md` (SSOT): entrada Spec Kit enriquecida con flujo de comandos y link al analisis.
- `software/00-INDEX.md`: seccion "Analisis de frameworks" con link al doc.
- `../agenda/BACKLOG-INVESTIGACION.md`: item "Transferencia de conceptos de Spec Kit a Linea A" (diferido).

### Hallazgo principal
Convergencia alta entre Spec Kit y nuestro protocolo (lenguaje normativo, gate de autoridad, manejo explicito de ambiguedad, validacion de consistencia continua). `/speckit.analyze` valida empiricamente el diseno de nuestro bloque `[SDD-Check]`. Tension abierta: la "Power Inversion" (spec ejecutable que genera codigo) es mas radical que nuestra posicion actual (spec como representacion del conocimiento) — conecta con el backlog de umbral manual->automatizado.

### Continuacion: compatibilidad documental + proyecto testigo

**Bloque 1 (compatibilidad, solo docs)** — aplicado en `CLAUDE.md`:
- Convencion `[NEEDS CLARIFICATION: ...]` para marcar incertidumbre en borradores (candidato C2 del analisis).
- Campo `Cobertura` anadido al bloque `[SDD-Check]`, espejando el coverage mapping de `/speckit.analyze` (candidato C1).

**Decision: proyecto testigo oficial de Linea B.**
Se designa `agent-test-suite` (`../../../test_circuito_intents/agent_test_suite/`) como sujeto experimental. Es un proyecto Python real que adopto nuestra variante SDD (derivada de este proyecto). Razon: este repo es meta/docs y no puede ejecutar su propio Plan de Pruebas (metricas DORA, defectos) — `experimentos/` estaba vacio por falta de sujeto. Registrado en `software/PLAN-PRUEBAS.md`.

**Primer experimento ejecutado y cerrado (observacional):** `experimentos/EXPERIMENTO-B6-circuito-testigo.md` + `experimentos/RESULTADO-EXPERIMENTO-B6.md`. Veredicto: hipotesis B6 SOSTENIDA en este caso (circuito de aprendizaje activo). Metrica primaria 40% (estricta) / 60% (amplia) de specs activas revisadas tras ejecucion; deuda arrastrada re-explicitada sin abandono; `[SDD-Check]` en 100% de iteraciones. Caveats: muestra minima (estudio de caso), sesgo de confirmacion (el testigo derivo su SDD de este proyecto), umbral de 30 dias no informativo a esta velocidad. Dos mejoras candidatas al marco propio surgidas del experimento (ver "Decision pendiente").

**Decision pendiente (del usuario):** _[RESUELTA en Fase 3, 2026-06-01: ambas propuestas fueron aprobadas y aplicadas.]_ dos propuestas de cambio al marco SDD derivadas de B-06:
1. Formalizar "Deuda arrastrada" como artefacto del marco (template de resultado y/o `[SDD-Check]`).
2. Reformular el umbral de cascada de "30 dias absolutos" a un criterio relativo a la velocidad del proyecto — toca el SSOT `../comun/SDD-ADAPTATIVO-VS-CASCADA.md`, requiere aprobacion y revision de derivados.

### Archivos modificados/creados (continuacion)
- `CLAUDE.md` (modificado): Bloque 1.
- `software/PLAN-PRUEBAS.md` (modificado): seccion "Proyecto testigo" + experimento B-06.
- `experimentos/EXPERIMENTO-B6-circuito-testigo.md` (creado): diseno del experimento (excluido del registry — generado desde template).

---

## Fase 1 — Consolidacion del sistema (2026-03-01) — COMPLETADA

**Alcance**: Unificacion de archivos de protocolo, cobertura completa de specs, eliminacion de duplicacion SSOT y enriquecimiento del registro.

### Archivos eliminados
- `AGENTS.md` — absorbido por `CLAUDE.md`
- `PROTOCOLO_ASISTENTES.md` — absorbido por `CLAUDE.md`

### Archivos creados
- `ROADMAP-MEJORAS-SDD.md` — analisis comparativo con proyecto "Transformacion AI-Native Org"
- `historial/sdd.md` — este archivo

### Archivos modificados

**`CLAUDE.md`** (reescrito):
- Absorbe contenido unico de `AGENTS.md` (comandos, convenciones de commits) y `PROTOCOLO_ASISTENTES.md` (pasos durante generacion, criterios de calidad, excepciones)
- Agrega `MUST NOT` al paso 4 del protocolo (no proponer alternativas sin aprobacion)
- Agrega seccion "Disambiguacion" (MUST preguntar, MUST NOT anticipar)
- Agrega checks genericos de post-generacion (refs, no duplicacion, no contradiccion SSOT, derivados)
- Agrega seccion "Ciclo de vida de specs" (proponer spec antes de doc, senalar divergencias, marcar deprecados)
- Elimina tabla SSOT y niveles ssot_level (ahora solo en `SPECS_REGISTRY.md`)

**`SPECS_REGISTRY.md`**:
- Agrega campo `deriva_de` al bloque de ssot_level (trazabilidad de derivados)
- Agrega seccion "Campo `estado`" (Activo / Borrador / Deprecado)
- Agrega seccion "Profundidad de spec" con 3 niveles (minima / estandar / extendida)
- Agrega seccion "Docs excluidos del registro"
- Tabla SSOT: columna "Derivados/Referencias" renombrada a "Quien referencia" con datos precisos
- Reglas globales: referencia tabla de profundidad en lugar de listar campos fijos
- 4 specs nuevas: `SPECS_REGISTRY.md`, `CLAUDE.md`, `../agenda/BACKLOG-INVESTIGACION.md`, `ROADMAP-MEJORAS-SDD.md`

**`REFERENCIAS.md`**:
- Elimina R19, R20, R21 (referencias a proyecto externo "Transformacion AI-Native Org")
- Elimina seccion "Fuentes internas (proyecto origen)"

**5 archivos con referencias actualizadas** (de `PROTOCOLO_ASISTENTES.md` a `CLAUDE.md`):
- `00-INDEX.md`, `README.md`, `SPECS_REGISTRY.md`, `software/00-INDEX.md`, `docs-y-investigacion/00-INDEX.md`

### Decision: SSOT unico para tabla y niveles ssot_level
`SPECS_REGISTRY.md` es el SSOT autoritativo de la tabla SSOT y la definicion de niveles. `CLAUDE.md` referencia en lugar de repetir. Detectado como contradiccion del principio SSOT — resuelto en esta fase.
