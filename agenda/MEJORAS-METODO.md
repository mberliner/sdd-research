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

Ordenada por estado: **items abiertos primero**, por prioridad; cerrados después, por ID. El detalle de cada uno está más abajo, en la misma agrupación.

| ID | Mejora | Prioridad | Estado | Origen | Destino |
|---|---|---|---|---|---|
| M-22 | Lo que un experimento sella: eliminarlo como variable, verificarlo, o declararlo sin verificador | alta | Aprobada — piezas 1 y 2 hechas (2026-08-23), pieza 3 en otro repositorio | desviación observada en T2 de la pasada 1b de A-04 | `../templates/EXPERIMENTO.md` + scripts de preparación |
| M-25 | El sello MUST identificar el artefacto que constituye el tratamiento | alta | Aprobada — piezas 1 y 2 hechas (2026-08-23), pieza 3 en otro repositorio | un tratamiento vivo cambió durante A-04 sin que nada lo registrara | `../templates/EXPERIMENTO.md` (aplicación: runbooks vigentes) |
| M-31 | Un check puede quedar en no-op y el backstop sigue en verde | alta | Propuesta (2026-08-30) | [R40] (check `normativos`) + auditoría propia del 2026-08-30 | `../tools/check_docs.py` |
| M-35 | Las 195 casillas de `validacion` del registro nunca se marcaron y nada las mira | alta | Propuesta (2026-08-30) | auditoría propia del 2026-08-30 | `../SPECS_REGISTRY.md` + `../AGENTS.md` (bloque `[SDD-Check]`) |
| M-02 | Gate de autoría documental (`.sdd/current-doc` + hook) | media | Aprobada | testigo `../tools/sdd_gate.py` | script nuevo + `.claude/settings.json` |
| M-03 | Playbooks agnósticos de asistente (`analyze`, `clarify`) | media | Propuesta | testigo `docs/playbooks/` | `playbooks/` + wrappers |
| M-04 | Formato y compactación de documentos | media | Propuesta | testigo `docs/SPEC-FORMAT.md` | doc nuevo + migración |
| M-06 | Modelo de confianza confirmado/inferido/gap | media | Propuesta | [R25] | convención de Línea A |
| M-16 | Verificar `Derivados a revisar` contra el disco y la tabla SSOT | media | Propuesta | sdd-first [R39] (`../software/ANALISIS-SDD-FIRST.md` C2) | `../tools/check_docs.py` |
| M-17 | Portar el modelo de skills multi-asistente desde una fuente única | media | Propuesta | sdd-first [R39] (`../software/ANALISIS-SDD-FIRST.md` C5) | contraparte de M-03 |
| M-30 | `historial/sdd.md` crece sin techo y no tiene regla de rotación | media | Propuesta (2026-08-23) | deuda de M-29; medición del 2026-08-23 | `../SPECS_REGISTRY.md` + `../historial/` (tomos por período) |
| M-32 | Las decisiones evaluadas y descartadas no tienen dónde vivir | media | Propuesta (2026-08-30) | sdd-first [R39] (`docs/IDEAS.md` §Índice de descartes) | este documento |
| M-34 | Un check que clasifica no tiene tabla de regresión que lo pruebe | media | Propuesta (2026-08-30) | [R40] (check `gate-reglas`) | `../tools/check_docs.py` |
| M-36 | El grafo de propagación no ve 18 de los 22 SSOT, y M-16 lo lee | media | Propuesta (2026-08-30) | auditoría propia del 2026-08-30; lección de [R40] Fase 17 | `../SPECS_REGISTRY.md` (grafo) antes que `../tools/check_docs.py` |
| M-08 | Decidir qué hacer con los emoticones de `PREREG-B7.md` | baja | Propuesta | Fase 8 | decisión del usuario |
| M-21 | `metodo-historial` sobre-dispara en altas de contenido del registro | baja | Propuesta (2026-08-15) | fricción observada al registrar A-04 | `../tools/check_docs.py` (`metodo-historial`) |
| M-26 | «Qué decisión habilita» es un MUST sin casillero donde satisfacerse | baja | Propuesta (2026-08-22) | revisión de `../AGENTS.md` | `../AGENTS.md` (bloque `[SDD-Check]`) |
| M-33 | La tabla de estado agrupa por estado, y eso obliga a mover un ítem cuando cambia | baja | Propuesta (2026-08-30) | sdd-first [R39] (`docs/IDEAS.md` §Prioridades) | este documento |
| M-01 | Backstop determinista de documentación (`check_docs.py`) | alta | **Hecha** (Fase 10) | testigo `../tools/check_traceability.py` | `../tools/check_docs.py` + `../AGENTS.md` |
| M-05 | Limpiar encabezados que restatan su alcance | baja | **Hecha** (2026-08-23) | regla de alcance, Fase 8 | `../software/RELACION-SPEC-VS-EPICA.md` |
| M-07 | Revisar la premisa "sin CI" tras el versionado | baja | **Hecha** (2026-08-15) | Fase 8 | `../AGENTS.md`, `../comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md` |
| M-09 | Señales de duplicación entre SSOTs (`ssot-collision`, `sdd-check-fields`) | alta | **Hecha** (Fase 12) | Fase 11 | `../tools/check_docs.py` |
| M-10 | Verificar rutas escritas en backticks, no solo links markdown | alta | **Hecha** (Fase 12) | Fase 11 | `../tools/check_docs.py` |
| M-11 | Validar la tabla SSOT contra el disco y contra las specs | media | **Hecha** (Fase 13) | Fase 11 | `../tools/check_docs.py` |
| M-12 | Higiene de archivo: CRLF mezclado, BOM, newline final | media | **Hecha** (Fase 13) | Fase 11 | `../tools/check_docs.py` |
| M-13 | `deriva_de` apunta a documentos que no son SSOT | media | **Hecha** (2026-08-03) | relevamiento 2026-08-02, completado 2026-08-03 | `../SPECS_REGISTRY.md` + `../tools/check_docs.py` |
| M-14 | Índices de línea duplicaban `proposito`/`estado` fuera del registro | media | **Hecha** (2026-08-03) | auditoría de coherencia 2026-08-03 | `../SPECS_REGISTRY.md` + `../software/00-INDEX.md` |
| M-15 | Cada principio declara un verificador ejecutable, o declara que no tiene | alta | **Hecha** (2026-08-15) | sdd-first [R39] (`../software/ANALISIS-SDD-FIRST.md` C1) | `../CONSTITUTION.md` + `../tools/check_docs.py` |
| M-18 | Ningún documento `Activo` conserva un `[NEEDS CLARIFICATION]` abierto | alta | **Hecha** (2026-08-15) | resultado de M-15: Principio VII sin verificador | `../tools/check_docs.py` + `../CONSTITUTION.md` |
| M-19 | Cablear el backstop al commit, fail-closed y versionado | alta | **Hecha** (2026-08-15) | pendiente de M-01; `BACKLOG-INVESTIGACION.md` alta #4 | `../tools/githooks/pre-commit` + check `gate` |
| M-20 | Verificador del Principio VI (cambio de método ⇒ entrada de historial) | alta | **Hecha** (2026-08-15) | pendiente de M-01; resultado de M-15 | `../tools/check_docs.py` (`metodo-historial`) |
| M-23 | `excluded-field` escaneaba solo tablas, no listas | baja | **Hecha** (2026-08-23) | auditoría de índices de línea | `../tools/check_docs.py` |
| M-24 | `normative-block` cubría bastante menos de lo que su nombre prometía | media | **Hecha** (2026-08-23) | revisión de `../AGENTS.md`, alta de `../CONVENCIONES.md` | `../tools/check_docs.py` + `../AGENTS.md` + `../CONSTITUTION.md` |
| M-27 | `sdd-check-fields` no miraba `templates/`, que es donde una definición se propaga sola | baja | **Hecha** (2026-08-23) | lectura de la implementación al ejecutar M-24 | `../tools/check_docs.py` |
| M-28 | Encabezados que reproducen campos del registro (`estado`, `ssot_level`, `owner`, `deriva_de`) | media | **Hecha** (2026-08-23) | auditoría de encabezados 2026-08-23 | `../SPECS_REGISTRY.md` + `../tools/check_docs.py` + 6 documentos |
| M-29 | El backlog de método cargaba la narración de lo ya cerrado | media | **Hecha** (2026-08-23) | deriva doc-vs-spec detectada el 2026-08-23 | este documento |

---

## Items abiertos

### M-02 — Gate de autoría documental

Declaración de la spec que gobierna la edición (`.sdd/current-doc`) más un hook `PreToolUse` que bloquea editar un `.md` de contenido sin esa declaración, con chequeo de mtime: la spec MUST haberse editado después de declararse. Reusa `../tools/sdd_gate.py` del testigo, que ya separa decisión de transporte (stdin JSON / argv / env) y por lo tanto no queda atado a Claude Code.

**Requisito de diseño no negociable: fail-closed.** El gate del testigo terminaba en `[ -f "$PYBIN" ] || exit 0` y, sin intérprete, permitía la edición en silencio; durante todo B-07 el enforcement estuvo caído sin que nadie lo notara. Ver `BACKLOG-INVESTIGACION` prioridad alta #4, que es la pregunta de investigación asociada.

Reserva: en un repo documental la fricción puede ser desproporcionada. Conviene medirla, no asumirla.

**Corrección de diseño incorporada el 2026-08-15 (origen: sdd-first [R39], `../software/ANALISIS-SDD-FIRST.md` C3).** El chequeo de mtime del párrafo anterior MUST NOT implementarse: se implementó en sdd-first y falló en las dos direcciones —bloqueó flujo legítimo (una spec trabajada en varios commits, `git checkout`, `clone`, y el ciclo stash/restore del propio `pre-commit`, que renueva mtimes) y no detuvo a nadie, porque un `touch` lo satisfacía. El criterio que lo reemplazó es de **contenido**: la spec declarada debe existir, figurar en el registro con un estado que habilite trabajo, y tener al menos un requisito con texto propio además del keyword; los placeholders de la plantilla no cuentan. Se conserva el enunciado original arriba, tachado por esta nota y no borrado, porque el error es el dato. Tres modos de falla adicionales ya documentados por esa fuente y transferibles a `.sdd/current-doc`: el gate debe fallar cerrado incluso sobre un harness fail-open; la escritura por `Bash` escapa a todo hook `PreToolUse` y se cubre corriendo la capa al commit, no parseando la línea de comandos; un reset post-commit evita que una declaración quede vigente por descuido.

**Nota de diseño a investigar (2026-08-24).** El gate no puede exigir spec para todo `.md` editado: tiene que replicar el criterio de `../SPECS_REGISTRY.md` §Docs excluidos antes de bloquear, o corta flujo legítimo sobre material exento —`fuentes-externas/` (vendored, no autorado), `EXPERIMENTO-*.md`/`RESULTADO-EXPERIMENTO-*.md` generados desde template, notas de sesión sin estructura formal, archivos fuente originales. El caso fino es `experimentos/`: no alcanza con el prefijo de carpeta, porque un runbook de método (`PRUEBA-*.md`) vive ahí sin derivar de ningún template y sí necesita spec — el criterio real es «¿la estructura la fija un template del proyecto, o su autor?», ya escrito en esa sección y no re-derivable por regla de ruta simple. Sin este filtro, la primera vez que el gate corra sobre una edición a `fuentes-externas/` o a un experimento generado, el falso bloqueo lo va a descubrir por fricción — precedente ya vivido con M-21.

### M-22 — Lo que un experimento sella: eliminarlo como variable, verificarlo, o declararlo

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

**Aprobada y ejecutada por partes desde el 2026-08-23.** La pieza 1 está hecha: `../templates/EXPERIMENTO.md` §Sello, con la jerarquía, la tabla por componente y las tres reservas resueltas — el criterio de qué entra, el heartbeat que sobrevive al escalón 1, y el verificador que detiene sin elegir. Quedan dos, y la tercera no es de este repositorio:

- **Pieza 2 — aplicación a los runbooks vigentes**: hecha el 2026-08-23. `../experimentos/a04-conducta-agente/PRUEBA-PISO-RUIDO-A4.md` §Sello, como enmienda 4 pre-dato respecto de la pasada 2 y sin alterar las pasadas 1 y 1b, cerradas.
- **Pieza 3 — el verificador en corrida**: vive en el repositorio hermano `experimentosdd-a4` (`scripts/preparar_rep.sh`, `scripts/preparar_rep_cc.sh`), fuera del alcance de este protocolo. **M-22 no puede declararse `Hecha` desde acá**; su cierre depende de una entrega en ese repositorio.

### M-25 — El sello MUST identificar el artefacto que constituye el tratamiento

**Regla propuesta.** Cuando el tratamiento de un experimento es material versionado del propio repositorio, el sello MUST identificarlo por commit —no por ruta— y la corrida MUST entregarlo **extrayéndolo de ese commit**, no copiándolo del árbol de trabajo. Una pasada que necesite un tratamiento distinto es una **pasada distinta**, con su enmienda fechada.

Aplica la jerarquía de M-22, que es su SSOT y no se reproduce acá. Lo que agrega este ítem es el modo de falla propio del componente: el tratamiento no se mueve por accidente ni por auto-actualización, se mueve **porque el repositorio trabaja**. Editar el artefacto es la actividad normal y correcta; lo que falta es que la corrida deje de depender de que nadie lo edite.

Por eso acá el escalón 1 alcanza casi entero, y eso cambia el balance del ítem. Extraer de un commit fijo cuesta lo mismo que copiar y **no impone ninguna restricción sobre el repositorio**: el trabajo sigue, el artefacto sigue evolucionando, y la pasada sigue entregando lo sellado. No hay que congelar nada ni declarar la pasada corrida sobre dos versiones — esa disyuntiva era un artefacto de haber pensado el control como alerta en vez de como construcción.

Queda un residuo, que es de otra clase y MUST no confundirse con lo anterior: si el artefacto evoluciona durante una pasada larga, el resultado describe una versión que ya no es la vigente. Eso es vigencia externa, no atribución; se acepta declarándolo y ningún verificador lo arregla.

El escalón 2 sobrevive como heartbeat: comprobar que lo entregado corresponde al commit sellado y no a un árbol sucio o a una extracción que falló en silencio.

Forma de la mejora: la sección de sello de `../templates/EXPERIMENTO.md` (pieza 1 de M-22) exige commit para todo tratamiento que sea material del repositorio y extracción desde ese commit; el script de preparación comprueba la correspondencia. Aplicación a los runbooks vigentes al adoptarla.

**Aprobada y ejecutada por partes desde el 2026-08-23.** La pieza 1 está hecha, en la misma sección `§Sello` que M-22: el tratamiento que es material versionado se identifica por commit, se entrega extrayéndolo de ese commit, y el residuo de vigencia externa queda declarado aparte. La pieza 2 también está hecha, en la misma enmienda 4 del runbook de A-04: el tratamiento queda sellado por commit y se entrega extrayéndolo de él. Falta la misma pieza 3 que M-22 —el verificador de correspondencia, en el repositorio hermano `experimentosdd-a4`—, así que **tampoco puede declararse `Hecha` desde acá**.

**Caso que la originó** (evidencia, no alcance). El brazo tratamiento de A-04 entrega `../AGENTS.md` al workspace del agente; el runbook (`../experimentos/a04-conducta-agente/PRUEBA-PISO-RUIDO-A4.md`) sella el fixture por hash, audita ancestros y verifica ausencia de configuración de asistente, pero no fija con qué commit se entrega el tratamiento — la variable independiente era el único componente sin identificar. El 2026-08-22 `../AGENTS.md` cambió dos veces —alta de `../CONVENCIONES.md` y declaración de §Qué NO hacer como índice— y nada en el aparato lo registró. No se invalidó nada: ni la pasada 1 ni la 1b produjeron dato de `H1` válido, y la pasada 2 no corrió. Pero el mismo cambio entre dos tandas de una pasada 2 habría dejado el efecto medido sin a qué atribuirse.

### M-31 — Un check puede quedar en no-op y el backstop sigue en verde

`../tools/check_docs.py` deriva parte de sus insumos leyendo otros documentos: los campos reservados salen de una viñeta de `../SPECS_REGISTRY.md` §Reglas globales, los ids de check salen de la propia fuente del script, y la tabla SSOT sale de una sección del registro localizada por su título. Derivar en vez de enumerar es deliberado y correcto —una lista a mano vuelve a divergir—, pero le agrega al check una dependencia que puede romperse sin que nadie la nombre.

Dos de esas tres derivaciones ya tienen guarda: `emitted_check_ids()` falla si extrae menos de diez ids, y `check_excluded_fields` falla explícitamente con «este check quedaria vacio sin avisar» si no logra derivar los campos reservados. O sea: el patrón ya está en el repositorio, aplicado dos veces, y no está declarado en ningún lado.

**La tercera derivación no tiene guarda, y se verificó el 2026-08-30.** Renombrando el título `## Tabla SSOT` del registro, `parse_ssot_table()` devuelve una lista vacía y los checks `ssot-table` y `ssot-collision` recorren cero filas. El backstop sale **0 ERROR** y ninguno de los dos ids aparece en la salida: no hay diferencia observable entre «la tabla está sana» y «nadie la miró».

Origen del encuadre: [R40] tiene un check `normativos` cuyo único trabajo es verificar que el módulo donde vive una regla de la que depende otro check siga siendo importable. Su motivo, escrito en el docstring, es exactamente éste: sin ese aviso, un import roto apagaría el check dependiente entero y el backstop seguiría en verde informando sobre una cobertura que ya no tiene.

Qué hace falta, en dos pasos:

1. **Guarda en `parse_ssot_table()`** — error si no encontró la sección o si devolvió cero filas. Es el hueco verificado y es barato.
2. **Auditar el resto de las derivaciones** y declarar la regla: todo insumo derivado de otro documento MUST fallar ruidosamente cuando la derivación no produce nada, en vez de degradar a no-op. Sin la regla escrita, la guarda número cuatro nace sin ella igual que nació ésta.

Es una instancia del patrón 1 de `../fuentes-externas/sdd-first/docs/PATRONES.md` («el mecanismo correcto que los casos nuevos no adoptan»): lo que sostiene el fix no es haber puesto dos guardas, es un barrido que falle nombrando a la que falta.

### M-35 — Las 195 casillas de `validacion` del registro nunca se marcaron y nada las mira

Cada entrada de `../SPECS_REGISTRY.md` declara una lista de validación en formato `- [ ]`. Medido el 2026-08-30: **195 casillas en las 46 entradas, ninguna marcada, y ninguna entrada sin el campo**. Es la promesa más repetida del registro y la única que no tiene ningún respaldo.

Ningún check las lee. `parse_registry()` guarda `validacion_items`, y su único consumidor es `ssot-collision`, que las usa como texto para comparar temas entre specs — no para verificar que se hayan corrido. El campo existe para el humano que escribe la entrega y depende enteramente de que se acuerde.

**El problema no es sólo que no se verifique: es que la forma miente.** Una casilla `- [ ]` afirma un estado —«pendiente»— y sugiere que en algún momento pasa a `- [x]`. Eso nunca ocurrió ni se espera que ocurra, porque las casillas no describen el estado de *un* documento sino el criterio permanente con que se lo revisa cada vez. La notación importada de una checklist de tarea se aplicó a algo que no es una tarea.

Tres salidas, y la primera es la tentadora y la peor:

1. **Mecanizar las casillas.** No aplica a la mayoría. «La procedencia concluye explícitamente que la fuente NO suma linaje» o «las descripciones no parafrasean el `proposito` registrado» son juicio editorial; automatizarlas produciría o falsos positivos o un check que aprueba cualquier cosa. Es además la salida que `../CONSTITUTION.md` §Límite honesto advierte contra: un verificador que no juzga adecuación no puede sostener un criterio de adecuación.
2. **Cablear el campo al bloque de salida.** Que `Validaciones aplicadas` del `[SDD-Check]` MUST nombrar las validaciones de la spec del documento tocado, y que un check verifique esa correspondencia **por presencia**: los nombres declarados aparecen, o falta trabajo. No juzga si la validación se hizo bien —nada puede—, pero convierte «me acordé» en «está escrito y se puede contrastar».
3. **Retirar la forma de casilla** y dejar la lista como criterios de revisión, sin `[ ]`. No pierde nada real y deja de afirmar un estado falso.

Las salidas 2 y 3 son compatibles y probablemente sean la respuesta juntas: la 3 corrige la notación, la 2 le da al campo el único enforcement honesto disponible.

Reservas antes de aprobarla:

- **La salida 2 tiene costo por entrega y hay que dimensionarlo.** Varias specs tienen diez u once validaciones; copiarlas todas al bloque de cada entrega lo vuelve ilegible. El alcance realista es nombrar las que la entrega ejercitó y declarar las que no aplicaron, no transcribir la lista.
- **La salida 3 toca las 46 entradas de un saque.** Es una edición mecánica y de bajo riesgo, pero conviene hacerla en su propio commit y no mezclada con cambios de contenido del registro.
- **Hay una cuarta salida que no propongo pero conviene nombrar para descartarla explícitamente:** dejar todo como está y anotar en el registro que las casillas son decorativas. Es peor que las tres, porque documenta la inconsistencia en vez de resolverla, y `../CONSTITUTION.md` ya declara sus límites en un lugar donde se leen.

Decisión pendiente del usuario: cuál de las salidas, o la 2 y la 3 juntas. El ítem no la anticipa.

### M-03 — Playbooks agnósticos de asistente

Procedimiento neutro en `playbooks/{analyze,clarify}.md`, envuelto por wrappers finos (`.claude/skills/`, `.opencode/command/`) que no duplican el contenido. Adaptados a documentos: `analyze` = consistencia doc↔SSOT, afirmaciones sin `[Rxx]`, contradicciones entre SSOTs activos; `clarify` = resolver `[NEEDS CLARIFICATION]` abiertos.

Cierra una incoherencia del proyecto: investiga SDD multi-asistente y en la práctica su tooling es Claude-only.

### M-04 — Formato y compactación de documentos

Convención de formato con resumen ejecutivo obligatorio a partir de cierto tamaño y migración oportunística. Candidatos por tamaño: `../SPECS_REGISTRY.md`, `../experimentos/b07-formato-hibrido/PRUEBA-REGENERABILIDAD-B7.md`, `../experimentos/b07-formato-hibrido/PRUEBA-OBSERVACIONAL-B7.md`. En el testigo la reescritura compacta de una spec dio −46% sin pérdida de contenido normativo.

### M-06 — Modelo de confianza confirmado/inferido/gap

Clasificar cada afirmación como *confirmada* (evidencia directa), *inferida* (patrón, no certeza) o *gap* (requiere validación humana) [R25]. Es una graduación más fina que el binario actual (`[Rxx]` vs. `[NEEDS CLARIFICATION]`). Evaluar costo de mantenimiento antes de adoptar: la propia fuente advierte que la trazabilidad tiene costo. Migrado desde `BACKLOG-INVESTIGACION` §Enriquecimientos R25/R30, donde convivía con dos candidatos de contenido que se quedan allá.

### M-16 — Verificar `Derivados a revisar` contra el disco y la tabla SSOT

El bloque `[SDD-Check]` declara `Derivados a revisar` y `Cobertura` en prosa que escribe el autor de la entrega sobre sí mismo. Nada verifica que los derivados nombrados existan, ni que un cambio en un SSOT haya nombrado a los suyos.

Origen: sdd-first [R39] SPEC-024, que cerró el hueco equivalente del lado del código —un requisito «verde» sobre un test que prueba otra cosa— exigiendo que el ID del FR aparezca como token completo dentro del archivo de test, con el cuidado explícito de no usar substring (`FR-1` dentro de `FR-10`). Ver `../software/ANALISIS-SDD-FIRST.md` C2.

Reserva antes de aprobarla: en un repo documental el vínculo requisito→verificador no tiene análogo tan limpio como FR→test, así que el alcance realista es el par SSOT→derivado registrado en `../SPECS_REGISTRY.md`, no la adecuación de la revisión.

**Hay implementación de referencia, y es de la mitad descendente (agregado 2026-08-30).** [R40] corre desde el 2026-08-25 un check `propagacion` que hace exactamente el alcance que esta reserva declara realista: con contexto de commit, si el commit toca un documento del que otras specs derivan, emite **WARN** nombrando los derivados que quedaron fuera. Sus tres decisiones de diseño valen más que el código:

1. **WARN y nunca ERROR.** Tocar un SSOT es trabajo normal; bloquear el commit por eso enseña `--no-verify`, que es peor que no tener el check.
2. **Silencio si el derivado está en el mismo commit** — si ya se tocó, ya se propagó.
3. **Silencio si el cambio no altera ninguna palabra**, comparando las dos versiones normalizadas a secuencia de palabras (sin tildes, puntuación, mayúsculas ni espaciado). El punto fino: un filtro por **magnitud del diff** habría silenciado justo el cambio que más importa propagar. Su tabla de validación lo prueba con dos casos de diff idéntico y resultado opuesto — quitar una coma da silencio; cambiar un `30` por un `45` da WARN con los cuatro derivados.

Y declara su propio límite en el campo `Verificador:` del principio: es un **recordatorio**, no una verificación. Nombra derivados; no puede saber si alguien los revisó, y ningún script puede.

Consecuencia para este ítem: la mitad descendente (SSOT tocado → derivados nombrados) está resuelta y es portable casi tal cual — **pero el insumo no lo está**, y eso lo mide M-36: nuestro grafo declarado no ve 18 de los 22 SSOT, así que portar el check hoy produciría uno que corre y calla. M-36 es previo a este ítem. Lo que sigue abierto, y es lo que M-16 pide de más, es la mitad **ascendente**: cruzar esos nombres contra el campo `Derivados a revisar` del bloque `[SDD-Check]`, que hoy no se verifica contra nada. [R40] tampoco la implementó, y dejó escrito por qué: no quiso afinar un verificador recién nacido sin datos de uso.

### M-17 — Portar el modelo de skills multi-asistente desde una fuente única

Contraparte concreta de M-03, que declara la incoherencia (investigamos SDD multi-asistente y el tooling es Claude-only) pero no el mecanismo. sdd-first sirve siete skills a cuatro asistentes desde una fuente única: playbook agnóstico como SSOT del contenido, `SKILL.md` fuente como wrapper, y adaptadores generados y committeados con cabecera «NO EDITAR A MANO». Sin symlinks a propósito: se degradan en Windows sin Developer Mode. Detalle en `../fuentes-externas/sdd-first/docs/SKILLS-MULTITOOL.md`; lectura en `../software/ANALISIS-SDD-FIRST.md` C5.

Reserva: portarlo trae un generador en Python, dependencia que hoy solo tiene `check_docs.py`. Decidir M-03 primero — sin playbooks que servir, no hay nada que generar.

**Segunda implementación, y esta vez en un repositorio documental (agregado 2026-08-30).** La reserva de arriba pesa menos de lo que parecía: [R40] es un repositorio sin código de producto —el mismo perfil que éste— y aun así corre el modelo completo. Sirve skills y hooks a tres asistentes desde `.agents/skills/` como fuente única, con `tools/skills/gen_skill_adapters.py` generando `.claude/skills/` y `.opencode/command/`, y un check `skill-adapters` que emite ERROR si los generados divergen del SSOT. O sea: el generador en Python ya convive con un `check_docs.py` en un repo documental, y la pieza que evita el drift es un check más, no infraestructura nueva.

Aporta además un detalle que sdd-first no tiene y que su historial documenta como defecto encontrado: los nombres de herramienta **se traducen entre asistentes, no se capitalizan** (fase del 2026-08-26). Un generador que asume nomenclatura común produce adaptadores que parecen correctos y no lo son.

### M-30 — `historial/sdd.md` crece sin techo y no tiene regla de rotación

El archivo es append-only por diseño y nadie está obligado a leerlo entero: `../AGENTS.md` §Al cerrar una iteración sólo obliga a **escribir** al principio, que es O(1), y el resto de las referencias apuntan a una entrada puntual. Por eso su tamaño no es el problema que M-29 corrigió en el backlog, y **podarlo está prohibido**: el historial registra entregas pasadas y MUST NOT reescribirse hacia atrás.

Pero el crecimiento es real y acelera. Medido el 2026-08-23: 34 entradas y ~890 líneas antes de la migración de M-29, con un costo por entrada estable (media 26 líneas, rango 15-42) y una distribución que va de 1 entrada en marzo a 20 en agosto. La migración de M-29 sumó otras ~156 de un saque.

Dos consumidores lo pagan, y ninguno es hipotético:

1. Un `Read` completo ya cuesta del orden de 15k tokens, así que el acceso pasa de ser una elección a ser sólo por grep.
2. El paso 3 de `../experimentos/b06-circuito-testigo/EXPERIMENTO-B6-circuito-testigo.md` exige barrerlo entero para extraer las secciones «Deuda arrastrada» y rastrear su destino. Es el único consumidor que lo lee completo, y es de investigación.

**Regla propuesta: rotar por período, no podar.** Al cerrar cada semestre, las entradas de ese semestre migran íntegras a `historial/sdd-<periodo>.md`; el archivo vivo conserva el período en curso y una línea al principio que apunta a los tomos cerrados. Hay precedente ya aplicado en el repositorio: `../historial/ROADMAP-MEJORAS-SDD.md` está declarado registro histórico cerrado y no recibe items nuevos.

**Mover un bloque intacto no es reescribir hacia atrás**, y esa distinción MUST quedar escrita en el registro al adoptarla, porque es la primera objeción que la regla va a recibir. Lo que el Principio VI prohíbe es alterar lo asentado, no reubicarlo con su texto intacto — el mismo criterio que ya se usó para migrar planteos en M-29, ahí como bloque añadido y fechado.

Qué toca: alta de spec para cada tomo cerrado en `../SPECS_REGISTRY.md`, una línea en `../00-INDEX.md`, y nada en `../tools/check_docs.py` — su constante `HISTORIAL` apunta al archivo vivo, que es lo que `metodo-historial` necesita.

Reservas antes de ejecutarla:

1. **El backstop por tamaño no tiene evidencia detrás.** La idea es rotar igual si el archivo vivo pasa cierto umbral antes del corte de período, para que el ritmo no desborde el calendario. Cualquier cifra concreta hoy sería una elección de diseño, no una medición, y MUST declararse como tal en vez de presentarse como derivada de algo.
2. **No ejecutarla todavía.** Al 2026-08-23 el archivo se sigue leyendo. Lo que vale es tener la regla escrita para que la rotación dispare sola y no se decida en caliente cuando ya duela.
3. **Rotar parte el grep en dos.** Quien hoy busca en un archivo tendrá que buscar en varios. Es aceptable con un glob, pero conviene que el archivo vivo declare dónde están los tomos.

**Dos datos ajenos que refuerzan la regla y descartan una variante (agregados 2026-08-30).** [R40] aplica este mismo método en otro dominio y llegó al mismo lugar sin coordinación:

1. **El problema se replica.** Su `historial/sdd.md` tiene 40 entradas y ~1800 líneas, y tampoco tiene regla de rotación. No es idiosincrasia de este repositorio: es del formato de historial, que es lo que la regla propuesta corrige.
2. **La variante «índice de entradas» ya falló, y es el resultado negativo que más vale.** Tenían un `HISTORIAL.md` declarado «índice vivo de entradas de cierre y decisiones». Llegó a estar **trece fases y dos decisiones atrasado**, y apuntaba a un archivo eliminado dos fases antes. La decisión fue **podarlo a navegación pura en vez de completarlo**, con dos motivos escritos: la tabla reproducía lo que ya está completo en el historial (Principio I) y era una obligación manual sin gate — el mismo mecanismo que había dejado vacío otro de sus historiales durante siete meses.

Consecuencia directa para la reserva 3: el puntero del archivo vivo a los tomos cerrados MUST ser derivable o estar cableado a un check. Una tabla de contenidos mantenida a mano es exactamente la variante que ya se probó y falló.

Instructivo de yapa, porque aplica igual acá: cuando ese defecto apareció, **ningún check lo vio**, y las dos razones son nuestras también. Su `propagacion` no lo detectó porque el índice no declaraba `deriva_de` de nada —un recordatorio de propagación es tan bueno como el grafo que lee—, y su check de rutas ignora las referencias en backticks sin `/`, que es la misma decisión de diseño que toma nuestro `check_backtick_paths`.

### M-34 — Un check que clasifica no tiene tabla de regresión que lo pruebe

Varios checks de `../tools/check_docs.py` no verifican una propiedad: **clasifican**. `excluded-field` decide si una celda es una anotación de campo o prosa legítima; `sdd-check-fields` decide si un texto es una definición o una instancia; `ssot-collision` decide si dos specs hablan del mismo tema; `metodo-historial` decide si un archivo es método. Todos tienen frontera difusa y todos la ajustaron al menos una vez (M-23, M-27, y M-21 sigue abierto).

Un clasificador mal calibrado no se manifiesta como un error: se manifiesta como **trabajo legítimo bloqueado**, y el remedio que la gente encuentra sola es desactivar el gate. Es el mismo razonamiento por el que el `propagacion` de [R40] emite WARN y no ERROR.

En [R40] el hueco se cerró con un check `gate-reglas`: el gate lleva su tabla de regresión al lado de sus propias reglas, expuesta como `--autotest`, y el backstop la corre en cada pasada. El invariante es que las reglas sigan clasificando como declaran, verificado por el mismo script que las usa.

Acá el hueco es doble y conviene no confundirlo: no hay tabla de casos **ni** hay quien la corra. `../tools/check_docs.py` no tiene tests de ningún tipo; su única verificación es correr sobre el árbol real, que sólo contiene los casos que hoy existen. Cada ajuste de frontera se validó a mano y esa validación no quedó ejecutable en ningún lado.

Reserva antes de aprobarla: sumar una suite de tests es una dependencia nueva y un cambio de naturaleza — hoy `tools/` está declarado «no es pieza documental autorada» y vive sin infraestructura. El alcance mínimo que lo evita es el de [R40]: casos declarados como datos dentro del propio script, corridos por un check más, sin framework.

### M-32 — Las decisiones evaluadas y descartadas no tienen dónde vivir

Este documento define `Descartada` como estado posible en §Criterio de separación, y ningún ítem lo usa. Tampoco hay lugar donde escribir **por qué** se descartó algo: una alternativa que se evaluó y se dejó afuera desaparece del registro, y vuelve a discutirse desde cero la próxima vez que a alguien se le ocurra.

sdd-first [R39] resolvió esto con un §Índice de descartes: una tabla de dos columnas —qué se descartó, dónde está escrito el motivo— cuyo encabezado declara que existe «para no re-litigarlas» y que el razonamiento **no se reproduce ahí**. Es una aplicación literal del Principio I: el índice apunta, el motivo vive en el ítem que lo produjo.

El repositorio ya tiene descartes reales sin registrar. Dos que se pueden nombrar hoy sin investigar nada: la opción «bajar el MUST a SHOULD» de M-26, si la decisión se resuelve por la otra vía; y la salida «lista de exenciones» para specs que un check nuevo pone en rojo, que M-13 y M-28 descartaron migrando en la misma iteración.

Costo: una sección de este documento. Reserva: un índice de descartes que nadie actualiza es peor que no tenerlo, porque afirma completitud. Conviene que la entrada se cree en la misma entrega que produce el descarte, no en un barrido retroactivo.

### M-36 — El grafo de propagación no ve 18 de los 22 SSOT, y M-16 lo lee

M-16 propone un recordatorio de propagación, y [R40] ya mostró cuál es su modo de falla: el defecto que su check `propagacion` **no** vio fue el de un documento que no declaraba `deriva_de` de nada. Un recordatorio de propagación es tan bueno como el grafo que lee. Este ítem mide el nuestro antes de implementar el de M-16, no después.

**Medición del 2026-08-30 sobre `../SPECS_REGISTRY.md`** (46 entradas, 48 paths):

| | |
|---|---|
| Specs por nivel | 22 `SSOT`, 16 `operativo`, 8 `derivado` |
| Aristas `deriva_de` declaradas | **8** |
| SSOT con al menos un derivado declarado | **4 de 22** |
| SSOT que no dispararían nada al cambiar | **18** |

Los 18 mudos incluyen a `../CONSTITUTION.md`, `../AGENTS.md`, `../SPECS_REGISTRY.md`, `../REFERENCIAS.md` y `../CONVENCIONES.md` — es decir, los cinco documentos más referenciados del repositorio. Un recordatorio construido hoy sobre este grafo callaría exactamente cuando más importa hablar.

**La causa es estructural, no de higiene.** `deriva_de` está definido sólo para `ssot_level: derivado` (§Campo ssot_level del registro). Los 16 documentos `operativo` —que incluyen los cinco análisis de framework y los índices de línea— **no pueden** llevar arista por definición, aunque dependan demostrablemente de otros documentos: `../software/ANALISIS-SDD-FIRST.md` depende de `../REFERENCIAS.md` y alimenta a este documento, y el grafo no tiene forma de representarlo.

**Hay un segundo grafo, ya declarado y sin usar.** La columna «Quien referencia» de la tabla SSOT del registro declara **40 aristas**, de las cuales sólo 5 coinciden con una arista `deriva_de`. Está escrita en paths con backticks, o sea que es parseable hoy. En la otra dirección hay 3 aristas `deriva_de` que no figuran en esa tabla, porque su origen no es una fila de la tabla.

O sea: el repositorio declara su estructura de dependencias **en dos lugares con semánticas distintas** —«sintetiza un origen» y «usa este SSOT»— y ningún consumidor lee ninguno de los dos.

Tres salidas:

1. **Ampliar `deriva_de` a `operativo`.** Cambia el significado del campo, que hoy dice «sintetiza un origen verificable» y no «lo usa». Es la más limpia conceptualmente y la más cara: obliga a revisar la definición del campo y las 16 specs `operativo`.
2. **Leer la columna «Quien referencia» como grafo débil.** Cubre 40 aristas, no requiere tocar ninguna spec y es parseable sin cambios. Es la barata.
3. **Las dos, con las aristas tipadas**: `deriva_de` como relación fuerte y la tabla SSOT como débil, y que el recordatorio distinga qué está diciendo.

Reservas, y la primera es la que puede invalidar la salida 2:

- **«Quien referencia» se mantiene a mano y nadie verifica que esté completa.** `ssot-table` (M-11) verifica que los paths de la tabla existan, no que la columna liste a todos los que efectivamente referencian. Usarla como grafo sin auditarla primero repite el modo de falla de [R40] Fase 17: un índice manual que se atrasa y del que nadie sospecha porque está escrito con autoridad.
- **Más aristas es más ruido, y el ruido tiene un ítem propio.** Pasar de 8 a 40 aristas multiplica los avisos por cinco, y si el aviso se vuelve paisaje el recordatorio deja de significar algo. Esa es exactamente la pregunta abierta de `BACKLOG-INVESTIGACION.md` #17. Quien decida entre las tres salidas MUST mirar ese ítem antes.
- **Este ítem no propone implementar nada de M-16.** Mide el insumo. Si la conclusión es que el grafo no alcanza, la consecuencia puede ser postergar M-16 en vez de acelerarlo, y eso también es un resultado.

### M-08 — Emoticones en `PREREG-B7.md`

El documento viola la regla global «sin emoticones» pero está **pre-registrado y sellado**. Editarlo post-sello tiene implicancias metodológicas (Principio V). Decisión pendiente del usuario: corregir con enmienda fechada, o declarar excepción permanente para documentos sellados.

### M-21 — `metodo-historial` sobre-dispara en altas de contenido del registro

Observado el 2026-08-15 al dar de alta A-04: registrar dos specs nuevas en `../SPECS_REGISTRY.md` disparó la exigencia de entrada de historial, aunque la entrega **sólo agrega contenido registrado** y no cambia ninguna regla del registro.

El check es fiel al texto: el Principio VI nombra literalmente «registro de specs» entre las piezas de método. El que está grueso es el texto, no el verificador.

**Recomendación: no ajustar el check todavía.** Aflojar un verificador recién entregado para que la tarea siguiente sea más cómoda, sin un dato que lo justifique, es exactamente la clase de deriva que el proyecto existe para no cometer. Si en tres o cuatro entregas el falso positivo se repite, ahí hay caso — y la distinción a implementar sería entre cambiar las **reglas** del registro (método) y agregar **entradas** al registro (contenido), que no es trivial de decidir por diff.

Costo actual: una entrada de historial de más por alta de spec. Barato. Se acepta la fricción y se cuenta.

### M-26 — «Qué decisión habilita» es un MUST sin casillero donde satisfacerse

`../AGENTS.md` §Criterios de calidad mínima exige que cada cambio indique qué decisión habilita. A diferencia de `Derivados a revisar` o `Deuda arrastrada`, no tiene campo en el bloque `[SDD-Check]`: no hay lugar donde escribirlo ni dónde verificar que se escribió.

Detectado el 2026-08-22 en la revisión de `../AGENTS.md`. No es contradicción —nada lo prohíbe—, es un MUST que en la práctica se cumple o no según se acuerde el asistente.

Dos salidas, y la elección no es obvia:

1. **Campo nuevo** en el bloque. Le da lugar mecánico y lo vuelve verificable por presencia. Costo: una línea más en **cada** entrega, para una exigencia que muchas veces se responde con una obviedad («habilita seguir escribiendo el documento»), y el bloque ya tiene siete campos.
2. **Bajar el MUST a SHOULD**, reconociendo que es un criterio de juicio y no una casilla. Costo: pierde fuerza justo en los cambios donde importa, que son los que no habilitan nada y nadie nota.

Ninguna es claramente mejor. Conviene decidirla junto con cualquier otra revisión del bloque `[SDD-Check]`, no sola.

### M-33 — La tabla de estado agrupa por estado, y eso obliga a mover un ítem cuando cambia

§Estado ordena «items abiertos primero, por prioridad; cerrados después, por ID», y §Items abiertos / §Items cerrados replican esa partición en el cuerpo. La consecuencia es que cerrar un ítem obliga a moverlo dos veces —fila y sección—, y ese movimiento es lo que M-29 tuvo que pagar en bloque el 2026-08-23.

sdd-first [R39] eligió lo contrario y escribió el motivo: los títulos de sección agrupan por **tanda de origen**, que no cambia nunca, y la prioridad se declara **sólo** en la tabla, «para que recalibrar un ítem no obligue a moverlo de lugar». Agrega además un valor de prioridad que acá no existe: `—`, que significa «sin triage», con la aclaración de que no es «menos que P3» sino «sin medir».

Aplicado acá el cambio sería: mantener la partición abierto/cerrado sólo en la tabla —barata de reordenar, es una fila— y ordenar el cuerpo por ID, que es estable. Ganancia: cerrar un ítem pasa a ser editar dos celdas.

Prioridad baja a propósito: M-29 ya pagó la migración grande y el dolor no vuelve hasta el próximo lote de cierres. Vale registrarlo ahora para que la decisión no se tome otra vez en caliente.

---

## Items cerrados

Cada uno vive entero en `../historial/sdd.md` —planteo, ejecucion, validacion y limites—; aca queda el puntero y nada mas (M-29, regla en `../SPECS_REGISTRY.md`). El titulo y la prioridad de cada uno estan en la tabla de estado.

| ID | Entrada en `../historial/sdd.md` |
|---|---|
| M-01 | «Fase 10 — Backstop determinista de documentación, M-01» |
| M-05 | «Barrido de encabezados: M-05 cerrada, M-28 abierta» |
| M-07 | «M-19 — Cablear el backstop al commit, fail-closed y versionado» |
| M-09 | «Fase 12 — El backstop aprende a ver duplicación y rutas, M-09 y M-10» |
| M-10 | «Fase 12 — El backstop aprende a ver duplicación y rutas, M-09 y M-10» |
| M-11 | «Fase 13 — Higiene de archivo y validación de SSOTs, M-11 y M-12» |
| M-12 | «Fase 13 — Higiene de archivo y validación de SSOTs, M-11 y M-12» |
| M-13 | «M-13 — `deriva_de` apunta a documentos que no son SSOT» |
| M-14 | «M-14 — Índices de línea duplicaban `proposito`/`estado` fuera del registro» |
| M-15 | «M-15 — Cada principio declara un verificador ejecutable, o declara que no tiene» |
| M-18 | «M-18 — Ningún documento `Activo` conserva un `[NEEDS CLARIFICATION]` abierto» |
| M-19 | «M-19 — Cablear el backstop al commit, fail-closed y versionado» |
| M-20 | «M-20 — Verificador ejecutable para el Principio VI» |
| M-23 | «`excluded-field` deja de mirar solo tablas» |
| M-24 | «`normative-block` pasa a llamarse `sdd-check-fields`» |
| M-27 | «`sdd-check-fields` pasa a mirar `templates/`» |
| M-28 | «`excluded-field` verifica la regla del registro, no el `excluye` de cada spec» |
| M-29 | «El backlog de metodo se poda a puntero y se reordena por estado» |
