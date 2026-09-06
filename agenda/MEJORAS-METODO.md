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
| M-31 | Un check reporta salud sobre lo que no mira: dos formas verificadas | alta | Propuesta (2026-08-30) | [R40] (check `normativos`) + dos auditorías propias del 2026-08-30 | `../tools/check_docs.py` |
| M-35 | Las 195 casillas de `validacion` del registro nunca se marcaron y nada las mira | alta | Propuesta (2026-08-30) | auditoría propia del 2026-08-30 | `../SPECS_REGISTRY.md` + `../AGENTS.md` (bloque `[SDD-Check]`) |
| M-36 | M-16 no tiene grafo viable: el declarado es 17 veces más fino que el real, y el real es demasiado denso para avisar | alta | Propuesta (2026-08-30) | medición propia del 2026-08-30; lección de [R40] Fase 17 | bloquea M-16; destino por definir |
| M-40 | La enumeración de «qué es método» del Principio VI deja afuera a `CONVENCIONES.md`, y el verificador la copia fiel | alta | Propuesta (2026-09-05) | sdd-first [R39] (`../software/analisis/ANALISIS-SDD-FIRST.md` C8, patrón 2); sonda propia del 2026-09-05 | `../CONSTITUTION.md` Principio VI + `../tools/check_docs.py` (`METODO_FILES`) |
| M-02 | Gate de autoría documental (`.sdd/current-doc` + hook) | media | Aprobada | testigo `../tools/sdd_gate.py` | script nuevo + `.claude/settings.json` |
| M-03 | Playbooks agnósticos de asistente (`analyze`, `clarify`) | media | Propuesta | testigo `docs/playbooks/` | `playbooks/` + wrappers |
| M-04 | Formato y compactación de documentos | media | Propuesta | testigo `docs/SPEC-FORMAT.md` | doc nuevo + migración |
| M-06 | Modelo de confianza confirmado/inferido/gap | media | Propuesta | [R25] | convención de Línea A |
| M-16 | Verificar `Derivados a revisar` contra el disco y la tabla SSOT | media | Propuesta | sdd-first [R39] (`../software/analisis/ANALISIS-SDD-FIRST.md` C2) | `../tools/check_docs.py` |
| M-17 | Portar el modelo de skills multi-asistente desde una fuente única | media | Propuesta | sdd-first [R39] (`../software/analisis/ANALISIS-SDD-FIRST.md` C5) | contraparte de M-03 |
| M-30 | `historial/sdd.md` crece sin techo y no tiene regla de rotación | media | Propuesta (2026-08-23) | deuda de M-29; medición del 2026-08-23 | `../SPECS_REGISTRY.md` + `../historial/` (tomos por período) |
| M-32 | Las decisiones evaluadas y descartadas no tienen dónde vivir | media | Propuesta (2026-08-30) | sdd-first [R39] (`docs/IDEAS.md` §Índice de descartes) | este documento |
| M-34 | Un check que clasifica no tiene tabla de regresión que lo pruebe | media | Propuesta (2026-08-30) | [R40] (check `gate-reglas`) | `../tools/check_docs.py` |
| M-39 | Qué MUST del protocolo se sostienen sólo por disciplina no está escrito en ningún lado | media | Propuesta (2026-08-30) | [R40] Fase 37; barrido propio del 2026-08-30 | `../CONSTITUTION.md` §Límite honesto o documento nuevo |
| M-41 | Un diff dirigido que lee sólo el CHANGELOG no ve un documento agregado sin línea de changelog | media | Propuesta (2026-09-05) | Spec Kit [R10] (`spec-persistence.md` invisible al diff del 2026-07-10) | `../AGENTS.md` o procedimiento propio de re-consulta de fuentes |
| M-42 | El marcador `[NEEDS CLARIFICATION]` registra la pregunta y no lo que se asumió ni lo que cuesta si está mal | media | Propuesta (2026-09-05) | Superpowers [R37] v6.3.0 (forma del `Ruling:`; `../software/analisis/ANALISIS-SUPERPOWERS.md` C7) | `../AGENTS.md` §Disambiguación |
| M-08 | Decidir qué hacer con los emoticones de `PREREG-B7.md` | baja | Propuesta | Fase 8 | decisión del usuario |
| M-21 | `metodo-historial` sobre-dispara en altas de contenido del registro | baja | Propuesta (2026-08-15) | fricción observada al registrar A-04 | `../tools/check_docs.py` (`metodo-historial`) |
| M-26 | «Qué decisión habilita» es un MUST sin casillero donde satisfacerse | baja | Propuesta (2026-08-22) | revisión de `../AGENTS.md` | `../AGENTS.md` (bloque `[SDD-Check]`) |
| M-33 | La tabla de estado agrupa por estado, y eso obliga a mover un ítem cuando cambia | baja | Propuesta (2026-08-30) | sdd-first [R39] (`docs/IDEAS.md` §Prioridades) | este documento |
| M-37 | El nivel «Extendida» y el campo `refresh` están declarados y no los usa ninguna spec | baja | Propuesta (2026-08-30) | auditoría propia del 2026-08-30 | `../SPECS_REGISTRY.md` |
| M-38 | Seis encabezados del registro escriben un directorio que no existe | baja | Propuesta (2026-08-30) | auditoría propia del 2026-08-30 | `../SPECS_REGISTRY.md` + `../tools/check_docs.py` |
| M-01 | Backstop determinista de documentación (`check_docs.py`) | alta | **Hecha** (Fase 10) | testigo `../tools/check_traceability.py` | `../tools/check_docs.py` + `../AGENTS.md` |
| M-05 | Limpiar encabezados que restatan su alcance | baja | **Hecha** (2026-08-23) | regla de alcance, Fase 8 | `../software/RELACION-SPEC-VS-EPICA.md` |
| M-07 | Revisar la premisa "sin CI" tras el versionado | baja | **Hecha** (2026-08-15) | Fase 8 | `../AGENTS.md`, `../comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md` |
| M-09 | Señales de duplicación entre SSOTs (`ssot-collision`, `sdd-check-fields`) | alta | **Hecha** (Fase 12) | Fase 11 | `../tools/check_docs.py` |
| M-10 | Verificar rutas escritas en backticks, no solo links markdown | alta | **Hecha** (Fase 12) | Fase 11 | `../tools/check_docs.py` |
| M-11 | Validar la tabla SSOT contra el disco y contra las specs | media | **Hecha** (Fase 13) | Fase 11 | `../tools/check_docs.py` |
| M-12 | Higiene de archivo: CRLF mezclado, BOM, newline final | media | **Hecha** (Fase 13) | Fase 11 | `../tools/check_docs.py` |
| M-13 | `deriva_de` apunta a documentos que no son SSOT | media | **Hecha** (2026-08-03) | relevamiento 2026-08-02, completado 2026-08-03 | `../SPECS_REGISTRY.md` + `../tools/check_docs.py` |
| M-14 | Índices de línea duplicaban `proposito`/`estado` fuera del registro | media | **Hecha** (2026-08-03) | auditoría de coherencia 2026-08-03 | `../SPECS_REGISTRY.md` + `../software/00-INDEX.md` |
| M-15 | Cada principio declara un verificador ejecutable, o declara que no tiene | alta | **Hecha** (2026-08-15) | sdd-first [R39] (`../software/analisis/ANALISIS-SDD-FIRST.md` C1) | `../CONSTITUTION.md` + `../tools/check_docs.py` |
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

### M-31 — Un check reporta salud sobre lo que no mira: dos formas verificadas

`../tools/check_docs.py` deriva parte de sus insumos leyendo otros documentos: los campos reservados salen de una viñeta de `../SPECS_REGISTRY.md` §Reglas globales, los ids de check salen de la propia fuente del script, y la tabla SSOT sale de una sección del registro localizada por su título. Derivar en vez de enumerar es deliberado y correcto —una lista a mano vuelve a divergir—, pero le agrega al check una dependencia que puede romperse sin que nadie la nombre.

Dos de esas tres derivaciones ya tienen guarda: `emitted_check_ids()` falla si extrae menos de diez ids, y `check_excluded_fields` falla explícitamente con «este check quedaria vacio sin avisar» si no logra derivar los campos reservados. O sea: el patrón ya está en el repositorio, aplicado dos veces, y no está declarado en ningún lado.

**La tercera derivación no tiene guarda, y se verificó el 2026-08-30.** Renombrando el título `## Tabla SSOT` del registro, `parse_ssot_table()` devuelve una lista vacía y los checks `ssot-table` y `ssot-collision` recorren cero filas. El backstop sale **0 ERROR** y ninguno de los dos ids aparece en la salida: no hay diferencia observable entre «la tabla está sana» y «nadie la miró».

Origen del encuadre: [R40] tiene un check `normativos` cuyo único trabajo es verificar que el módulo donde vive una regla de la que depende otro check siga siendo importable. Su motivo, escrito en el docstring, es exactamente éste: sin ese aviso, un import roto apagaría el check dependiente entero y el backstop seguiría en verde informando sobre una cobertura que ya no tiene.

Qué hace falta, en dos pasos:

1. **Guarda en `parse_ssot_table()`** — error si no encontró la sección o si devolvió cero filas. Es el hueco verificado y es barato.
2. **Auditar el resto de las derivaciones** y declarar la regla: todo insumo derivado de otro documento MUST fallar ruidosamente cuando la derivación no produce nada, en vez de degradar a no-op. Sin la regla escrita, la guarda número cuatro nace sin ella igual que nació ésta.

Es una instancia del patrón 1 de `../fuentes-externas/sdd-first/docs/PATRONES.md` («el mecanismo correcto que los casos nuevos no adoptan»): lo que sostiene el fix no es haber puesto dos guardas, es un barrido que falle nombrando a la que falta.

#### Segunda forma, verificada el mismo día: el alcance más angosto que el nombre

`check_backtick_paths` se llama «las rutas escritas en backticks existen» y su docstring dice lo mismo. Lo que hace es más chico: `BACKTICK_PATH` es `^[\w./-]+\.md$`, o sea que **sólo verifica rutas Markdown**. Toda ruta a un `.py`, un `.sh`, un `.yaml` o un archivo sin extensión conocida se ignora en silencio.

Medido: **105 rutas no-`.md` citadas en backticks y resolubles contra este repositorio, de las cuales 42 no existen** (15 pares documento→ruta distintos).

La lectura honesta de ese 42 es más interesante que el número. La mayoría **no son errores**: son herramientas del proyecto testigo —`tools/sdd_gate.py`, `tools/check_traceability.py`, `tools/pipeline_local.sh`, `tools/check_constitution.py`— citadas sin ningún prefijo que diga que son de otro repositorio, así que se leen como si fueran nuestras. Eso no es un link roto sino una **ambigüedad de procedencia**, y es un defecto distinto que hoy no tiene ni nombre ni convención. El caso que sí es error liso: `../historial/sdd.md` cita `./tools/check_docs.py`, que resuelve a `historial/tools/check_docs.py`.

Se descubrió intentando verificar que `../tools/sdd_gate.py`, citado dos veces en M-02, existiera. No existe, y el backstop está en verde.

#### Por qué las dos formas son el mismo ítem

Una derivación que no produce nada y un reconocedor más angosto que su nombre producen el mismo efecto observable: el check corre, sale limpio, y la limpieza no significa lo que su nombre promete. En los dos casos el consumidor —una persona leyendo `0 ERROR`— no tiene forma de distinguir «está sano» de «no lo miró».

Qué hace falta, actualizado a tres pasos:

1. **Guarda en `parse_ssot_table()`** — error si no encontró la sección o devolvió cero filas.
2. **Decidir el alcance real de `check_backtick_paths`** y hacer que el nombre y el docstring lo digan. Dos salidas: ampliarlo a toda ruta resoluble —lo que exige antes una convención para citar herramientas de otro repositorio, o los 42 entran como falsos positivos—, o dejarlo en `.md` y renombrarlo para que no prometa de más. La segunda es honesta y cuesta una línea; la primera cierra el hueco pero arrastra un problema de convención que no está resuelto.
3. **Auditar el resto de las derivaciones y de los reconocedores**, y declarar la regla: todo insumo derivado MUST fallar ruidosamente cuando no produce nada, y todo check MUST nombrar el alcance que efectivamente cubre. Sin la regla escrita, el próximo nace igual.

**Cuatro decisiones de diseño ajenas, verificadas (2026-09-05).** OpenSpec [R38] v1.11.0 corrigió un caso de esta misma clase —`openspec validate` aprobaba un `## Purpose` que seguía siendo el placeholder que `archive` escribe, porque el placeholder supera el piso de brevedad— y las cuatro decisiones con que lo cerró son transferibles a este ítem sin traer código: la detección es **angosta a propósito** (reconoce el placeholder por la misma definición que lo escribe, y fuera de eso sólo un `TBD`/`TODO` que abra el texto); es **WARN y no ERROR**, para que un repositorio con placeholders ya en disco siga validando y sólo `--strict` falle; el texto **entre backticks no cuenta**, porque un documento que cita el marcador no lo está usando; y un hallazgo de placeholder **no se reporta además como «demasiado breve»**, para que un caso produzca un mensaje y no dos. Detalle en `../software/analisis/ANALISIS-OPENSPEC.md` §Nota menor.

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

### M-36 — M-16 no tiene grafo viable: el declarado es 17 veces más fino que el real, y el real es demasiado denso para avisar

M-16 propone un recordatorio de propagación. [R40] ya lo implementó y su lección es que un recordatorio de propagación es tan bueno como el grafo que lee. Este ítem midió el nuestro antes de portar nada, y el resultado bloquea a M-16 en vez de habilitarlo.

**Corrección de la primera versión de este ítem (2026-08-30, escrita y medida el mismo día).** La primera redacción decía que la causa era estructural: `deriva_de` está definido sólo para `ssot_level: derivado`, así que los 16 documentos `operativo` no pueden llevar arista. Eso es cierto y es un síntoma. La causa está un nivel más abajo y la medición la expuso.

#### Los tres grafos que el repositorio ya tiene

| Estructura | Aristas | Relación que declara | Cómo se mantiene |
|---|---|---|---|
| `deriva_de` en el registro | **8** | «sintetiza a» | a mano, atada al rol |
| Columna «Quien referencia» de la tabla SSOT | **40** | «usa este SSOT» | a mano, sin auditar |
| Citación en el texto (links + rutas en backticks) | **385** | «menciona a» | derivable, completa por construcción |

Precisión alta y recall nulo en un extremo; recall total y precisión nula en el otro; nada declarado en el medio. Y el hueco de fondo: **la pregunta que la propagación hace nunca se definió**. Esa pregunta es «si esto cambia sustantivamente, ¿qué hay que releer?», y no está escrita como definición en ningún lado. `deriva_de` nació para clasificar roles; la tabla SSOT nació porque alguien necesitó la otra relación y abrió un segundo lugar en vez de arreglar el primero. Ninguna de las dos tuvo nunca un consumidor, y por eso derivar salía gratis.

#### La medición que decide

De las 385 aristas de citación, 241 son de contenido a contenido tras excluir clases estructurales: origen o destino en `../historial/` (registro del pasado), destino en gobernanza o protocolo, y origen en índices o en el README.

Sobre esas 241 se corrió una muestra con el criterio, la población, el tamaño, la semilla y la regla de decisión **fijados por escrito antes de generar un solo par** (Principio V):

- **Muestra:** n = 30, aleatoria sin reemplazo, `random.seed(20260830)`.
- **Regla de puntuación:** para cada par, leyendo la línea donde aparece la cita, ¿un cambio sustantivo en el destino obligaría a releer el origen? `DUDOSO` cuenta como NO.
- **Regla de decisión, fijada antes del dato:** ≤ 15 % de SI → hay un árbol escondido y la solución declarativa alcanza; ≥ 30 % → hay malla y declarar a mano no va a funcionar; entre ambos, NO CONCLUYENTE.

**Resultado: 17 SI, 10 NO, 3 DUDOSO — 56,7 % de SI.** Da malla, por el doble del umbral. Quitando los tres SI más discutibles —el registro citando a los documentos que registra, que es una clase sistemática que quizá debió excluirse de la población, y uno escrito dentro de un bloque de cierre— queda **51,9 %**. El resultado no depende de las llamadas dudosas.

**Extrapolado: ~137 aristas reales sobre las 241 candidatas.** Contra las 8 declaradas, un factor de **17**.

#### Los dos resultados, y se cancelan entre sí

1. **La solución declarativa no es viable acá.** El grafo declarado no está incompleto por descuido: está incompleto por un orden de magnitud, y ningún esfuerzo de disciplina cierra un factor de 17. Por eso el arreglo de [R40] —que funciona sobre siete aristas— no es portable: su corpus es un árbol, con 4 de sus 7 aristas colgando de un mismo origen. El nuestro es una malla sin raíz, donde ningún documento tiene cero citas entrantes.
2. **El grafo real es inservible como disparador.** 137 aristas sobre 51 documentos es un aviso en casi cada commit, que es exactamente el patrón «el aviso que suena siempre enseña que el verde no significa nada» (`../fuentes-externas/sdd-first/docs/PATRONES.md`, 3).

Juntos dejan a M-16 sin salida por la vía que tenía planteada: **no le falta trabajo, le falta una idea distinta**. Un grafo mejor no la desbloquea, porque el problema deja de ser el grafo apenas el grafo es bueno.

#### Qué queda abierto

Lo que la medición **no** contestó es cuál sería un disparador más selectivo que un aviso por arista. Cuatro direcciones, ninguna evaluada y ninguna preferida:

- Disparar sólo sobre la relación fuerte —el `deriva_de` actual— y aceptar que cubre poco, declarándolo.
- Disparar por **sección** y no por documento, para que el aviso nombre qué parte cambió y no el archivo entero.
- Disparar sobre un subconjunto de documentos elegido por criterio explícito, no sobre todos.
- **Descartar M-16** y aceptar que la propagación en un repositorio con esta forma es humana. Es una salida legítima y hoy es la que menos supuestos requiere.

La pregunta #17 de `BACKLOG-INVESTIGACION.md` —si un recordatorio automático se vuelve paisaje— dejó de ser curiosidad y pasó a ser bloqueante para elegir entre las cuatro.

#### Descartado con motivo

Las tres salidas que proponía la primera redacción de este ítem quedan descartadas por la misma medición, y se registran para no re-litigarlas:

| Descarte | Motivo |
|---|---|
| Ampliar `deriva_de` a `operativo` | resuelve la forma, no el factor de 17 |
| Leer «Quien referencia» como grafo débil | 40 aristas contra ~137 reales: sigue subrepresentando, y encima sin auditar |
| Poblar por sustracción desde las 385 candidatas | produciría el grafo correcto y con él un recordatorio inservible por ruido |

#### Reproducibilidad, y un límite deliberado

La muestra se reproduce exactamente con la población y la semilla declaradas arriba. Los veredictos par por par **no se transcriben acá a propósito**: quien la rehaga debe puntuar sin ver los míos, para no quedar anclado. El desacuerdo entre dos puntuadores sobre los mismos 30 pares es a su vez un dato sobre si la regla de puntuación es aplicable, y hoy no existe.

Limitación que no tiene mitigación: el puntuador fue quien propuso el diseño que la muestra evaluaba. El resultado terminó siendo contrario a esa propuesta, lo cual reduce la preocupación pero no la elimina.

### M-40 — La enumeración de «qué es método» del Principio VI deja afuera a `CONVENCIONES.md`, y el verificador la copia fiel

El Principio VI de `../CONSTITUTION.md` enumera qué cuenta como método: «protocolo del asistente, registro de specs, templates, esta constitución». Su verificador `metodo-historial` deriva de ahí su lista, y el comentario de `../tools/check_docs.py` lo dice sin rodeos: «La enumeracion sale literal del Principio VI [...] mas `tools/`, porque un check ES metodo».

`../CONVENCIONES.md` no está en esa enumeración. Y es el SSOT del léxico normativo (qué significa MUST, SHOULD, MAY en este repositorio), de la forma de los documentos, de los nombres de archivo y del formato de los mensajes de commit. `../AGENTS.md` le delega esas cuatro cosas por remisión explícita.

**Sonda corrida el 2026-09-05.** Se agregó una línea a `../CONVENCIONES.md`, se la dejó staged y se corrió `./tools/check_docs.py --staged`, que es el modo que invoca el gate de commit: **0 ERROR**, sin pedir entrada de historial. Un commit que redefine qué significa MUST en este repositorio pasa sin dejar rastro en `../historial/sdd.md`.

Lo que hace a este ítem distinto de M-31 —con el que comparte familia— es dónde está el defecto. En M-31 el check miraba mal. Acá **el check mira exactamente lo que le dijeron**: la lista es fiel, la fuente está incompleta. Arreglar `METODO_FILES` sin tocar el Principio VI deja la constitución diciendo una cosa y el verificador otra, que es justo la divergencia que la fidelidad de la lista evitaba.

Es una instancia de la clase 2 de `../fuentes-externas/sdd-first/docs/PATRONES.md` («la lista duplicada que nada ata») en su variante menos visible: las dos enumeraciones **no** divergieron —una deriva de la otra— y el defecto viajó entero desde el original.

Qué hace falta, en este orden:

1. **Decidir si `CONVENCIONES.md` es método.** Es la pregunta real y es del usuario, no del backstop. Si lo es, el Principio VI se enmienda con su procedimiento completo (es cambio de constitución, no de check).
2. **Barrer el resto de la enumeración** con el mismo criterio antes de enmendar, para no pagar dos enmiendas: `../REFERENCIAS.md` y `../00-INDEX.md` son los otros dos candidatos, y ninguno de los dos es obvio. `agenda/` e `historial/` ya están razonados y quedan afuera.
3. **Recién entonces** actualizar `METODO_FILES`, que sigue siendo la copia fiel.

Prioridad alta y no media: mientras esté abierto, la única garantía mecánica del Principio VI tiene un agujero del tamaño del SSOT del léxico, y el repositorio no lo sabe.

### M-02 — Gate de autoría documental

Declaración de la spec que gobierna la edición (`.sdd/current-doc`) más un hook `PreToolUse` que bloquea editar un `.md` de contenido sin esa declaración, con chequeo de mtime: la spec MUST haberse editado después de declararse. Reusa `../tools/sdd_gate.py` del testigo, que ya separa decisión de transporte (stdin JSON / argv / env) y por lo tanto no queda atado a Claude Code.

**Requisito de diseño no negociable: fail-closed.** El gate del testigo terminaba en `[ -f "$PYBIN" ] || exit 0` y, sin intérprete, permitía la edición en silencio; durante todo B-07 el enforcement estuvo caído sin que nadie lo notara. Ver `BACKLOG-INVESTIGACION` prioridad alta #4, que es la pregunta de investigación asociada.

Reserva: en un repo documental la fricción puede ser desproporcionada. Conviene medirla, no asumirla.

**Corrección de diseño incorporada el 2026-08-15 (origen: sdd-first [R39], `../software/analisis/ANALISIS-SDD-FIRST.md` C3).** El chequeo de mtime del párrafo anterior MUST NOT implementarse: se implementó en sdd-first y falló en las dos direcciones —bloqueó flujo legítimo (una spec trabajada en varios commits, `git checkout`, `clone`, y el ciclo stash/restore del propio `pre-commit`, que renueva mtimes) y no detuvo a nadie, porque un `touch` lo satisfacía. El criterio que lo reemplazó es de **contenido**: la spec declarada debe existir, figurar en el registro con un estado que habilite trabajo, y tener al menos un requisito con texto propio además del keyword; los placeholders de la plantilla no cuentan. Se conserva el enunciado original arriba, tachado por esta nota y no borrado, porque el error es el dato. Tres modos de falla adicionales ya documentados por esa fuente y transferibles a `.sdd/current-doc`: el gate debe fallar cerrado incluso sobre un harness fail-open; la escritura por `Bash` escapa a todo hook `PreToolUse` y se cubre corriendo la capa al commit, no parseando la línea de comandos; un reset post-commit evita que una declaración quede vigente por descuido.

**Nota de diseño a investigar (2026-08-24).** El gate no puede exigir spec para todo `.md` editado: tiene que replicar el criterio de `../SPECS_REGISTRY.md` §Docs excluidos antes de bloquear, o corta flujo legítimo sobre material exento —`fuentes-externas/` (vendored, no autorado), `EXPERIMENTO-*.md`/`RESULTADO-EXPERIMENTO-*.md` generados desde template, notas de sesión sin estructura formal, archivos fuente originales. El caso fino es `experimentos/`: no alcanza con el prefijo de carpeta, porque un runbook de método (`PRUEBA-*.md`) vive ahí sin derivar de ningún template y sí necesita spec — el criterio real es «¿la estructura la fija un template del proyecto, o su autor?», ya escrito en esa sección y no re-derivable por regla de ruta simple. Sin este filtro, la primera vez que el gate corra sobre una edición a `fuentes-externas/` o a un experimento generado, el falso bloqueo lo va a descubrir por fricción — precedente ya vivido con M-21.

**Tres convergencias con el relevamiento del 2026-08-30, y una pregunta sin responder.** La nota de arriba toca tres cosas que ese relevamiento midió, y ninguna estaba disponible cuando el ítem se escribió:

1. **Replicar §Docs excluidos es el patrón de M-31.** La propia nota dice que el criterio **no es re-derivable por regla de ruta simple**, así que lo que va a haber es una reimplementación, no una derivación. Eso lo deja peor que los dos casos que el backstop ya resuelve bien —`emitted_check_ids()` y `registry_spec_fields()`, que derivan y fallan ruidosamente si la derivación no produce nada—: acá va a haber dos enumeraciones del mismo hecho sin nada que las ate. Si el registro cambia su criterio, el gate sigue excluyendo por el viejo y nadie se entera. El remedio disponible no es derivar sino un test de paridad, que es la forma de M-34.
2. **El gate es un clasificador y M-34 aplica.** El caso fino que la nota identifica —«¿la estructura la fija un template del proyecto, o su autor?»— es juicio codificado, con frontera difusa. Un error de clasificación no aparece como error sino como trabajo legítimo bloqueado. M-02 MUST NOT entregarse sin la tabla de regresión que M-34 propone.
3. **La reserva «conviene medirla, no asumirla» ya tiene método.** M-36 dejó el molde ejercitado: criterio, población, umbral y regla de decisión por escrito antes del dato, muestra con semilla, decisión contra el umbral. La fricción de M-02 se mide igual y **antes** de construir: barrer commits pasados, contar cuántas ediciones de `.md` habría bloqueado el gate y qué proporción de ésas era legítima. Es la respuesta más barata a una reserva abierta desde que el ítem existe.

**Y la pregunta que el ítem no responde: por qué bloquea en vez de avisar.** M-02 es hoy el único mecanismo propuesto en este backlog que **bloquea**. Todo lo relevado apunta en contra: el `propagacion` de [R40] emite WARN y nunca ERROR, con el motivo escrito de que bloquear por trabajo normal enseña `--no-verify` y eso es peor que no tener el check; M-16 hereda esa decisión; M-21 ya registró un verificador de método sobre-disparando sobre altas legítimas; y M-36 midió que la estructura de este repositorio es más densa y menos regular de lo que los mecanismos asumían.

Nada de eso prueba que M-02 vaya a sobre-disparar —la superficie es otra: cobertura de spec, no densidad de citación— y por eso se enuncia como **prior a declarar, no como resultado**. Pero son tres observaciones independientes en la misma dirección sobre el único mecanismo que no degrada a aviso. Bloquear puede seguir siendo la decisión correcta; lo que no puede seguir es no estar escrita.
### M-03 — Playbooks agnósticos de asistente

Procedimiento neutro en `playbooks/{analyze,clarify}.md`, envuelto por wrappers finos (`.claude/skills/`, `.opencode/command/`) que no duplican el contenido. Adaptados a documentos: `analyze` = consistencia doc↔SSOT, afirmaciones sin `[Rxx]`, contradicciones entre SSOTs activos; `clarify` = resolver `[NEEDS CLARIFICATION]` abiertos.

Cierra una incoherencia del proyecto: investiga SDD multi-asistente y en la práctica su tooling es Claude-only.

### M-04 — Formato y compactación de documentos

Convención de formato con resumen ejecutivo obligatorio a partir de cierto tamaño y migración oportunística. Candidatos por tamaño: `../SPECS_REGISTRY.md`, `../experimentos/b07-formato-hibrido/PRUEBA-REGENERABILIDAD-B7.md`, `../experimentos/b07-formato-hibrido/PRUEBA-OBSERVACIONAL-B7.md`. En el testigo la reescritura compacta de una spec dio −46% sin pérdida de contenido normativo.

### M-06 — Modelo de confianza confirmado/inferido/gap

Clasificar cada afirmación como *confirmada* (evidencia directa), *inferida* (patrón, no certeza) o *gap* (requiere validación humana) [R25]. Es una graduación más fina que el binario actual (`[Rxx]` vs. `[NEEDS CLARIFICATION]`). Evaluar costo de mantenimiento antes de adoptar: la propia fuente advierte que la trazabilidad tiene costo. Migrado desde `BACKLOG-INVESTIGACION` §Enriquecimientos R25/R30, donde convivía con dos candidatos de contenido que se quedan allá.

### M-16 — Verificar `Derivados a revisar` contra el disco y la tabla SSOT

El bloque `[SDD-Check]` declara `Derivados a revisar` y `Cobertura` en prosa que escribe el autor de la entrega sobre sí mismo. Nada verifica que los derivados nombrados existan, ni que un cambio en un SSOT haya nombrado a los suyos.

Origen: sdd-first [R39] SPEC-024, que cerró el hueco equivalente del lado del código —un requisito «verde» sobre un test que prueba otra cosa— exigiendo que el ID del FR aparezca como token completo dentro del archivo de test, con el cuidado explícito de no usar substring (`FR-1` dentro de `FR-10`). Ver `../software/analisis/ANALISIS-SDD-FIRST.md` C2.

Reserva antes de aprobarla: en un repo documental el vínculo requisito→verificador no tiene análogo tan limpio como FR→test, así que el alcance realista es el par SSOT→derivado registrado en `../SPECS_REGISTRY.md`, no la adecuación de la revisión.

**Hay implementación de referencia, y es de la mitad descendente (agregado 2026-08-30).** [R40] corre desde el 2026-08-25 un check `propagacion` que hace exactamente el alcance que esta reserva declara realista: con contexto de commit, si el commit toca un documento del que otras specs derivan, emite **WARN** nombrando los derivados que quedaron fuera. Sus tres decisiones de diseño valen más que el código:

1. **WARN y nunca ERROR.** Tocar un SSOT es trabajo normal; bloquear el commit por eso enseña `--no-verify`, que es peor que no tener el check.
2. **Silencio si el derivado está en el mismo commit** — si ya se tocó, ya se propagó.
3. **Silencio si el cambio no altera ninguna palabra**, comparando las dos versiones normalizadas a secuencia de palabras (sin tildes, puntuación, mayúsculas ni espaciado). El punto fino: un filtro por **magnitud del diff** habría silenciado justo el cambio que más importa propagar. Su tabla de validación lo prueba con dos casos de diff idéntico y resultado opuesto — quitar una coma da silencio; cambiar un `30` por un `45` da WARN con los cuatro derivados.

Y declara su propio límite en el campo `Verificador:` del principio: es un **recordatorio**, no una verificación. Nombra derivados; no puede saber si alguien los revisó, y ningún script puede.

Consecuencia para este ítem, y cambió el 2026-08-30: **M-16 está bloqueada por un resultado adverso propio**, medido en M-36. El insumo que el check necesita no existe en ninguna de las dos formas que hacen falta — el grafo declarado subrepresenta la dependencia real por un factor de 17, y el grafo real es tan denso que un recordatorio construido sobre él dispararía en casi cada commit. Portar el mecanismo del caso no está esperando trabajo: está esperando una idea distinta. M-36 es previo y puede concluir que este ítem se descarta. Lo que sigue abierto, y es lo que M-16 pide de más, es la mitad **ascendente**: cruzar esos nombres contra el campo `Derivados a revisar` del bloque `[SDD-Check]`, que hoy no se verifica contra nada. [R40] tampoco la implementó, y dejó escrito por qué: no quiso afinar un verificador recién nacido sin datos de uso.

### M-17 — Portar el modelo de skills multi-asistente desde una fuente única

Contraparte concreta de M-03, que declara la incoherencia (investigamos SDD multi-asistente y el tooling es Claude-only) pero no el mecanismo. sdd-first sirve siete skills a cuatro asistentes desde una fuente única: playbook agnóstico como SSOT del contenido, `SKILL.md` fuente como wrapper, y adaptadores generados y committeados con cabecera «NO EDITAR A MANO». Sin symlinks a propósito: se degradan en Windows sin Developer Mode. Detalle en `../fuentes-externas/sdd-first/docs/SKILLS-MULTITOOL.md`; lectura en `../software/analisis/ANALISIS-SDD-FIRST.md` C5.

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

### M-32 — Las decisiones evaluadas y descartadas no tienen dónde vivir

Este documento define `Descartada` como estado posible en §Criterio de separación, y ningún ítem lo usa. Tampoco hay lugar donde escribir **por qué** se descartó algo: una alternativa que se evaluó y se dejó afuera desaparece del registro, y vuelve a discutirse desde cero la próxima vez que a alguien se le ocurra.

sdd-first [R39] resolvió esto con un §Índice de descartes: una tabla de dos columnas —qué se descartó, dónde está escrito el motivo— cuyo encabezado declara que existe «para no re-litigarlas» y que el razonamiento **no se reproduce ahí**. Es una aplicación literal del Principio I: el índice apunta, el motivo vive en el ítem que lo produjo.

El repositorio ya tiene descartes reales sin registrar. Dos que se pueden nombrar hoy sin investigar nada: la opción «bajar el MUST a SHOULD» de M-26, si la decisión se resuelve por la otra vía; y la salida «lista de exenciones» para specs que un check nuevo pone en rojo, que M-13 y M-28 descartaron migrando en la misma iteración.

Costo: una sección de este documento. Reserva: un índice de descartes que nadie actualiza es peor que no tenerlo, porque afirma completitud. Conviene que la entrada se cree en la misma entrega que produce el descarte, no en un barrido retroactivo.


### M-34 — Un check que clasifica no tiene tabla de regresión que lo pruebe

Varios checks de `../tools/check_docs.py` no verifican una propiedad: **clasifican**. `excluded-field` decide si una celda es una anotación de campo o prosa legítima; `sdd-check-fields` decide si un texto es una definición o una instancia; `ssot-collision` decide si dos specs hablan del mismo tema; `metodo-historial` decide si un archivo es método. Todos tienen frontera difusa y todos la ajustaron al menos una vez (M-23, M-27, y M-21 sigue abierto).

Un clasificador mal calibrado no se manifiesta como un error: se manifiesta como **trabajo legítimo bloqueado**, y el remedio que la gente encuentra sola es desactivar el gate. Es el mismo razonamiento por el que el `propagacion` de [R40] emite WARN y no ERROR.

En [R40] el hueco se cerró con un check `gate-reglas`: el gate lleva su tabla de regresión al lado de sus propias reglas, expuesta como `--autotest`, y el backstop la corre en cada pasada. El invariante es que las reglas sigan clasificando como declaran, verificado por el mismo script que las usa.

Acá el hueco es doble y conviene no confundirlo: no hay tabla de casos **ni** hay quien la corra. `../tools/check_docs.py` no tiene tests de ningún tipo; su única verificación es correr sobre el árbol real, que sólo contiene los casos que hoy existen. Cada ajuste de frontera se validó a mano y esa validación no quedó ejecutable en ningún lado.

Reserva antes de aprobarla: sumar una suite de tests es una dependencia nueva y un cambio de naturaleza — hoy `tools/` está declarado «no es pieza documental autorada» y vive sin infraestructura. El alcance mínimo que lo evita es el de [R40]: casos declarados como datos dentro del propio script, corridos por un check más, sin framework.

### M-39 — Qué MUST del protocolo se sostienen sólo por disciplina no está escrito en ningún lado

`../CONSTITUTION.md` §Límite honesto contesta esta pregunta para los siete principios: cuáles tienen verificador, cuál es parcial y cuál sustantivo, y qué mitad de cada invariante queda humana. Para las reglas de proceso no la contesta nadie.

Superficie medida el 2026-08-30: **11 MUST en `../AGENTS.md` y 5 en `../CONVENCIONES.md`**. Cuántos de esos 16 tienen algo mecánico detrás no está escrito, y por lo tanto tampoco está escrito cuáles dependen enteramente de que alguien se acuerde.

Precedente de que el barrido produce algo: la Fase 37 de [R40] tomó un MUST que su convención declaraba y que sostenía sólo la disciplina —completar la descripción de cada entrada versionada de su changelog— y lo convirtió en check. No lo encontró buscando qué automatizar: lo encontró habiendo hecho el inventario.

**El ítem es el barrido, no la automatización.** Producir la tabla MUST → verificador (o `ninguno`), y recién sobre esa tabla decidir uno por uno. La mitad del valor está en el inventario mismo, por la misma razón que el §Límite honesto vale aunque no cambie nada: saber cuál regla no tiene red es lo que permite mirarla.

Dos reservas:

- **Dónde vive el resultado no es obvio.** Si va a `../CONSTITUTION.md`, mezcla invariantes con reglas de proceso, que es justo la separación que ese documento mantiene. Si va a `../AGENTS.md`, engorda la capa residente con algo que no es disparador. Un documento nuevo necesita spec y sube el conteo. Conviene decidirlo antes de barrer, no después.
- **Es el más caro de los ítems abiertos de higiene**, porque cada MUST hay que evaluarlo contra lo que `../tools/check_docs.py` efectivamente emite — y M-31 acaba de mostrar que lo que emite no siempre es lo que su nombre dice. Este ítem MUST hacerse después de M-31, o su tabla nace mintiendo.

### M-41 — Un diff dirigido que lee sólo el CHANGELOG no ve un documento agregado sin línea de changelog

Este repositorio re-consulta cuatro clones vendored y cada re-consulta produce un diff dirigido contra el análisis correspondiente. El procedimiento no está escrito en ningún lado: se improvisa cada vez, y el `[SDD-Check]` de la entrega declara después qué se leyó.

El del 2026-07-10 declaró el suyo con honestidad —«diff basado en CHANGELOG + spec-driven.md»— y esa declaración es exactamente el registro de su punto ciego. `docs/concepts/spec-persistence.md` estaba en el árbol de Spec Kit desde el 2026-06-09, un mes antes de ese corte, y no aparece en el análisis: **un documento agregado sin línea de changelog es invisible a un diff que lee el changelog**. Lo que se perdió no era menor — es la sección que califica la tesis central de la fuente (`../software/analisis/ANALISIS-SPEC-KIT.md` C6) y la que da vocabulario upstream al eje que nuestra comparativa ya usaba (C7).

Es una instancia de la clase 4 de `../fuentes-externas/sdd-first/docs/PATRONES.md` («la carpeta que existe y ningún paso mira») aplicada a un procedimiento humano en vez de a un pipeline: el directorio estaba, el paso no lo visitaba, y el resultado salió en verde durante dos meses.

Qué hace falta: un procedimiento mínimo de re-consulta, escrito una vez y aplicado a las cuatro fuentes. Tres pasos que ya se ejecutaron a mano en el diff del 2026-09-05 y sirven de borrador:

1. `git diff --stat <ancla>..HEAD` sobre el árbol completo, no sobre los archivos que uno espera que cambien — es lo que hace visible un directorio nuevo.
2. Verificar la no-invalidación de la tesis central con `git diff <ancla>..HEAD -- <doc de filosofía>` y reportar si salió vacío, en vez de afirmarlo por lectura comparada.
3. Declarar en el `[SDD-Check]` qué se leyó **y qué no**, que es lo único que la entrega del 2026-07-10 ya hacía bien.

Prioridad media: el costo de no tenerlo ya se pagó una vez y se detectó solo porque la re-consulta siguiente miró el árbol. Con cuatro fuentes vivas, va a volver a pasar.

### M-42 — El marcador `[NEEDS CLARIFICATION]` registra la pregunta y no lo que se asumió ni lo que cuesta si está mal

`../AGENTS.md` §Disambiguación permite marcar incertidumbre puntual con `[NEEDS CLARIFICATION: <pregunta>]` cuando no bloquea el resto del trabajo. El marcador es grep-able, el check `clarificacion` verifica que ningún documento `Activo` conserve uno abierto, y hasta ahí funciona.

Lo que no registra es qué hizo el asistente mientras tanto. Un marcador que no bloquea significa, por definición, que el trabajo siguió — y siguió sobre **alguna** lectura de la ambigüedad. Esa lectura hoy no queda escrita en ningún lado: quien resuelve el marcador más tarde ve la pregunta, no la respuesta provisional que el texto ya está asumiendo, y no tiene forma de saber cuánto del documento se cae si la respuesta es la otra.

Superpowers v6.3.0 [R37] resuelve la mitad simétrica del problema con una forma de tres campos: `Ruling: <qué se decidió> — <por qué> — <cuánto cuesta si está mal>` (`../software/analisis/ANALISIS-SUPERPOWERS.md` C7). El tercer campo es el que falta acá: convierte una duda anotada en una duda **priorizable**.

Propuesta concreta, mínima: extender el marcador a `[NEEDS CLARIFICATION: <pregunta> | asumido: <lectura provisional> | costo: <qué se rehace si está mal>]`, con los dos campos nuevos opcionales — un marcador que sí bloquea no necesita declarar asunción porque no la hay.

**Qué NO propone este ítem, y conviene que quede escrito**: no relaja la obligación de preguntar. El Principio VII manda preguntar ante ambigüedad y detener ante contradicción, y eso no se toca; el marcador cubre el caso que el propio principio ya excluye —incertidumbre puntual que no bloquea—. Superpowers va bastante más lejos (decide y sigue sin humano para todo conflicto no catastrófico), y **esa parte no se propone**: es constitucional, responde a un riesgo distinto — proteger una corrida autónoma larga, no evitar que el asistente interprete en silencio — y su única evidencia es un caso autoreportado.

Costo de implementarlo: una línea en `../AGENTS.md` y ninguna en el backstop. Verificado el 2026-09-05: `CLARIFICACION` de `../tools/check_docs.py` captura `([^\]]*)` —todo hasta el corchete de cierre— así que los dos campos nuevos entran en el payload sin tocar el patrón, y `es_placeholder()` los distingue de un marcador de relleno por la misma vía que hoy.

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

**Segunda instancia, el mismo día que se registró el ítem.** El 2026-08-30 M-02 bajó de `alta` a `media` y M-36 subió de `media` a `alta`. Las dos filas se movieron; los dos cuerpos no, y el documento quedó afirmando un orden que no tenía. Se detectó comparando tabla contra cuerpo con un script, no leyendo — o sea que a ojo no se ve. Se corrigió moviendo dos bloques, que es exactamente el costo que este ítem propone eliminar.

Corolario para cuando se implemente: mientras la convención siga siendo la actual, la coherencia entre tabla y cuerpo **MUST** poder verificarse mecánicamente. Es comparable a los dos órdenes con el mismo parser que ya lee las filas, y sin eso la deriva vuelve en la próxima recalibración.

### M-37 — El nivel «Extendida» y el campo `refresh` están declarados y no los usa ninguna spec

La tabla de profundidad de `../SPECS_REGISTRY.md` define tres niveles de spec, y el nivel `Extendida` se distingue por llevar el campo `refresh`. Distribución real medida el 2026-08-30 sobre las 46 entradas: **36 `Estandar`, 10 `Minima`, 0 `Extendida`**. El campo `refresh` aparece una sola vez en todo el repositorio — en la fila de la tabla que lo define.

Y hay dos documentos que cumplen el criterio que la propia tabla declara para `Extendida` («SSOTs criticos con multiples derivados»): `../software/analisis/ANALISIS-SPEC-KIT.md` y `../experimentos/b07-formato-hibrido/EXPERIMENTO-B7-formato-hibrido.md`, cada uno con dos derivados registrados. Ninguno lo usa.

Es una instancia del patrón 4 de `../fuentes-externas/sdd-first/docs/PATRONES.md` («la carpeta que existe y ningún paso mira»): una clave de primera clase que ningún consumidor visita. No falla — calla, y el silencio se lee como salud.

Dos salidas, y no hay una obviamente mejor:

1. **Aplicarlo** a los dos documentos que califican, y con eso averiguar si `refresh` sirve para algo. Riesgo: se aplica por completar la tabla y no porque alguien necesite el dato, que es cómo nacen los campos que después nadie mantiene — el mismo destino de las 195 casillas de M-35.
2. **Retirarlo**, dejando dos niveles. Es la más barata y la que menos promete. Si más adelante hace falta un campo de refresco, se agrega con un consumidor.

Lo que no se sostiene es dejarlo declarado sin usuarios: el registro afirma una taxonomía de tres niveles y opera con dos.

### M-38 — Seis encabezados del registro escriben un directorio que no existe

Seis entradas de `../SPECS_REGISTRY.md` titulan su bloque `### docs-y-investigación/...`, con tilde. El directorio en disco es `docs-y-investigacion/`, sin tilde. Nada lo detecta porque `parse_registry()` toma la ruta del campo `path` —que está bien escrito en las seis— y el encabezado queda como decoración.

No rompe nada hoy. Lo que hace es peor a largo plazo: quien lea el registro y copie el encabezado escribe una ruta inválida, y el próximo consumidor que decida parsear los `### ` en vez del campo `path` hereda seis fallas silenciosas.

**Uno de los seis lo escribí yo el 2026-08-30**, dando de alta la spec del análisis de caso, copiando la convención local sin verificar que el directorio existiera. Vale registrarlo porque es la evidencia del patrón 1 de `../fuentes-externas/sdd-first/docs/PATRONES.md` en su forma más literal: el archivo número siete nace roto igual que el primero, y lo que sostiene el fix no es corregir los seis sino un check que falle nombrando al séptimo.

Qué hace falta: corregir los seis encabezados, y agregar al backstop la verificación de que el encabezado de cada bloque coincida con alguno de sus `path` declarados. El check es de tres líneas y ya tiene los dos insumos parseados.

Prioridad baja, no nula: es higiene, pero la guarda es tan barata que postergarla cuesta más en discusión que en implementación.

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
