# Historial SDD

Registro de fases y mejoras completadas al sistema SDD del proyecto.

Archivo vivo: el trimestre en curso. Las entradas de trimestres cerrados están, intactas, en los tomos `historial/sdd-*.md` (regla de rotación en la spec de este documento, `SPECS_REGISTRY.md`).

---

## M-26: «qué decisión habilita» pasa a SHOULD (2026-10-07) — COMPLETADA

**Acción**: M-26 resuelta con la segunda salida del ítem, bajar el MUST a SHOULD, elegida por el usuario en la tanda del 2026-10-07. La otra salida, un campo nuevo en el bloque `[SDD-Check]`, queda descartada: sumaba una línea a cada entrega para una pregunta que casi siempre se contesta con una obviedad.

### Qué cambió
- **`AGENTS.md` §Criterios de calidad mínima**: «cada cambio indica qué decisión habilita» pasa de MUST a SHOULD. El texto dice que es criterio de juicio y que el bloque no tiene campo para eso a propósito.
- **`agenda/MEJORAS-METODO.md`**: M-26 pasa a `Hecha` y su planteo migra acá abajo.

### Validación
`tools/check_docs.py` en verde (0 ERROR, 0 WARN). Ningún otro documento cita la regla como MUST. `comun/SDD-ADAPTATIVO-VS-CASCADA.md` nombra «decisión habilitada» como criterio de éxito, y eso sigue siendo cierto con SHOULD.

### Límite
El costo que el ítem le asignaba a esta salida sigue en pie: la regla pierde fuerza justo en los cambios que no habilitan nada y que nadie nota. Se acepta ese costo; no hay verificador.

### Deuda abierta
- ninguna

### Planteo migrado del backlog (2026-10-07)

#### M-26 — «Qué decisión habilita» es un MUST sin casillero donde satisfacerse

`../AGENTS.md` §Criterios de calidad mínima exige que cada cambio indique qué decisión habilita. A diferencia de `Derivados a revisar` o `Deuda arrastrada`, no tiene campo en el bloque `[SDD-Check]`: no hay lugar donde escribirlo ni dónde verificar que se escribió.

Detectado el 2026-08-22 en la revisión de `../AGENTS.md`. No es contradicción —nada lo prohíbe—, es un MUST que en la práctica se cumple o no según se acuerde el asistente.

Dos salidas, y la elección no es obvia:

1. **Campo nuevo** en el bloque. Le da lugar mecánico y lo vuelve verificable por presencia. Costo: una línea más en **cada** entrega, para una exigencia que muchas veces se responde con una obviedad («habilita seguir escribiendo el documento»), y el bloque ya tiene siete campos.
2. **Bajar el MUST a SHOULD**, reconociendo que es un criterio de juicio y no una casilla. Costo: pierde fuerza justo en los cambios donde importa, que son los que no habilitan nada y nadie nota.

Ninguna es claramente mejor. Conviene decidirla junto con cualquier otra revisión del bloque `[SDD-Check]`, no sola.

---

## M-31, paso 3: la regla de que el verde signifique que el check miró, y cuatro checks que no la cumplían (2026-10-07) — COMPLETADA

**Acción**: paso 3 de M-31, aprobado por el usuario el 2026-10-07 en la tanda con M-26, M-32 y M-33. Con esto M-31 queda cerrada. Se auditaron todas las derivaciones y reconocedores de `tools/check_docs.py` y se escribió la regla que el ítem pedía, para que el próximo check no nazca con el mismo hueco. La auditoría encontró cuatro checks que no la cumplían y se corrigieron en la misma entrega.

### Qué cambió
- **`tools/check_docs.py`, docstring del módulo**: la regla, con dos obligaciones. Un insumo derivado de otro documento MUST fallar con ERROR si la derivación no produce nada. El docstring de cada check MUST nombrar el alcance que cubre de verdad. Las enumeraciones copiadas a mano quedan fuera de la regla y declaran su límite al lado.
- **Cuatro checks que salían en verde sin haber mirado**:
  - `sdd-check-fields`: si no derivaba los campos del bloque `[SDD-Check]` de `AGENTS.md`, volvía sin decir nada. Ahora da ERROR.
  - `historial-rotacion`: si ninguna entrada del historial tenía fecha legible, no veía trimestres y callaba. Ahora da ERROR.
  - `deuda-punteros`: reconoce la sección por su título literal; una entrada nueva sin `### Deuda abierta` pasaba sin que mirara nada. Ahora da ERROR.
  - `referencias`: exigía ids de exactamente dos dígitos. Desde el id 100 no habría visto ni la entrada del catálogo ni la cita. Ahora admite dos o más.
- **Límites declarados, sin cambio de conducta**: el docstring de `emoji` dice qué emoticones no ve. El comentario de `EXEMPT_PATTERNS` dice que es una copia de §Docs excluidos y en qué dirección diverge en silencio.
- **Tabla de regresión**: tres casos nuevos (`referencias-tres-digitos`, `sdd-check-fields-sin-bloque`, `deuda-punteros-sin-seccion`). La guarda de `historial-rotacion` queda sin caso y figura en la lista de los que no tienen: vaciar el historial de fechas dispara medio backstop.
- **`agenda/MEJORAS-METODO.md`**: M-31 pasa a `Hecha` y su planteo migra acá abajo.

### Auditoría
| Insumo o reconocedor | Antes | Ahora |
|---|---|---|
| `parse_registry()` | vacío deja a cada documento sin cobertura: ruidoso por construcción | igual |
| `parse_ssot_table()` | guarda desde el paso 1 | igual |
| `registry_spec_fields()`, `emitted_check_ids()` | guarda propia | igual |
| campos del `[SDD-Check]` | no-op silencioso | ERROR |
| trimestres del historial | no-op silencioso | ERROR |
| título `### Deuda abierta` | no-op silencioso | ERROR |
| ids `[Rxx]` | ciego desde el id 100 | dos o más dígitos |
| hermanos de `CONVENCIONES.md` | falla cerrado | igual |
| URLs de GitHub, catálogo `[Rxx]`, principios, backlog de método | vacío dispara un hallazgo por cita o por ítem: ruidoso | igual |
| `METODO_FILES`, `EXEMPT_PATTERNS` | copias a mano | límite declarado |

### Validación
`tools/check_docs.py` en verde (0 ERROR, 0 WARN). `--autotest`: 38 casos, 0 fallas. En una copia del árbol con las cuatro correcciones anuladas, los tres casos nuevos fallan.

### Límite
La regla obliga a quien escribe un check; nada la verifica. Su único verificador es la tabla de regresión, y sólo cuando el check suma un caso que vacía su insumo.

### Deuda abierta
- ninguna

### Planteo migrado del backlog (2026-10-07)

#### M-31 — Un check reporta salud sobre lo que no mira: dos formas verificadas

`../tools/check_docs.py` deriva parte de sus insumos leyendo otros documentos: los campos reservados salen de una viñeta de `../SPECS_REGISTRY.md` §Reglas globales, los ids de check salen de la propia fuente del script, y la tabla SSOT sale de una sección del registro localizada por su título. Derivar en vez de enumerar es deliberado y correcto —una lista a mano vuelve a divergir—, pero le agrega al check una dependencia que puede romperse sin que nadie la nombre.

Dos de esas tres derivaciones ya tienen guarda: `emitted_check_ids()` falla si extrae menos de diez ids, y `check_excluded_fields` falla explícitamente con «este check quedaria vacio sin avisar» si no logra derivar los campos reservados. O sea: el patrón ya está en el repositorio, aplicado dos veces, y no está declarado en ningún lado.

**La tercera derivación no tiene guarda, y se verificó el 2026-08-30.** Renombrando el título `## Tabla SSOT` del registro, `parse_ssot_table()` devuelve una lista vacía y los checks `ssot-table` y `ssot-collision` recorren cero filas. El backstop sale **0 ERROR** y ninguno de los dos ids aparece en la salida: no hay diferencia observable entre «la tabla está sana» y «nadie la miró».

Origen del encuadre: [R40] tiene un check `normativos` cuyo único trabajo es verificar que el módulo donde vive una regla de la que depende otro check siga siendo importable. Su motivo, escrito en el docstring, es exactamente éste: sin ese aviso, un import roto apagaría el check dependiente entero y el backstop seguiría en verde informando sobre una cobertura que ya no tiene.

Qué hace falta, en dos pasos:

1. **Guarda en `parse_ssot_table()`** — error si no encontró la sección o si devolvió cero filas. Es el hueco verificado y es barato.
2. **Auditar el resto de las derivaciones** y declarar la regla: todo insumo derivado de otro documento MUST fallar ruidosamente cuando la derivación no produce nada, en vez de degradar a no-op. Sin la regla escrita, la guarda número cuatro nace sin ella igual que nació ésta.

Es una instancia del patrón 1 de `sdd-first:docs/PATRONES.md` («el mecanismo correcto que los casos nuevos no adoptan»): lo que sostiene el fix no es haber puesto dos guardas, es un barrido que falle nombrando a la que falta.

##### Segunda forma, verificada el mismo día: el alcance más angosto que el nombre

`check_backtick_paths` se llama «las rutas escritas en backticks existen» y su docstring dice lo mismo. Lo que hace es más chico: `BACKTICK_PATH` es `^[\w./-]+\.md$`, o sea que **sólo verifica rutas Markdown**. Toda ruta a un `.py`, un `.sh`, un `.yaml` o un archivo sin extensión conocida se ignora en silencio.

Medido: **105 rutas no-`.md` citadas en backticks y resolubles contra este repositorio, de las cuales 42 no existen** (15 pares documento→ruta distintos).

La lectura honesta de ese 42 es más interesante que el número. La mayoría **no son errores**: son herramientas del proyecto testigo —`tools/sdd_gate.py`, `tools/check_traceability.py`, `tools/pipeline_local.sh`, `tools/check_constitution.py`— citadas sin ningún prefijo que diga que son de otro repositorio, así que se leen como si fueran nuestras. Eso no es un link roto sino una **ambigüedad de procedencia**, y es un defecto distinto que hoy no tiene ni nombre ni convención. El caso que sí es error liso: `../historial/sdd.md` cita `./tools/check_docs.py`, que resuelve a `historial/tools/check_docs.py`.

Se descubrió intentando verificar que `../tools/sdd_gate.py`, citado dos veces en M-02, existiera. No existe, y el backstop está en verde.

##### Por qué las dos formas son el mismo ítem

Una derivación que no produce nada y un reconocedor más angosto que su nombre producen el mismo efecto observable: el check corre, sale limpio, y la limpieza no significa lo que su nombre promete. En los dos casos el consumidor —una persona leyendo `0 ERROR`— no tiene forma de distinguir «está sano» de «no lo miró».

Qué hace falta, actualizado a tres pasos:

1. **Guarda en `parse_ssot_table()`** — error si no encontró la sección o devolvió cero filas.
2. **Decidir el alcance real de `check_backtick_paths`** y hacer que el nombre y el docstring lo digan. Dos salidas: ampliarlo a toda ruta resoluble —lo que exige antes una convención para citar herramientas de otro repositorio, o los 42 entran como falsos positivos—, o dejarlo en `.md` y renombrarlo para que no prometa de más. La segunda es honesta y cuesta una línea; la primera cierra el hueco pero arrastra un problema de convención que no está resuelto.
3. **Auditar el resto de las derivaciones y de los reconocedores**, y declarar la regla: todo insumo derivado MUST fallar ruidosamente cuando no produce nada, y todo check MUST nombrar el alcance que efectivamente cubre. Sin la regla escrita, el próximo nace igual.

**Pasos 1 y 2 hechos (2026-10-07).** Aprobados por el usuario junto con otras cuatro mejoras baratas. El paso 2 tomó la salida honesta: el check quedó en `.md` y pasó a llamarse `rutas-md`. Detalle en la entrada «M-31, pasos 1 y 2» de `../historial/sdd.md`. Queda abierto el paso 3.

**Cuatro decisiones de diseño ajenas, verificadas (2026-09-05).** OpenSpec [R38] v1.11.0 corrigió un caso de esta misma clase —`openspec validate` aprobaba un `## Purpose` que seguía siendo el placeholder que `archive` escribe, porque el placeholder supera el piso de brevedad— y las cuatro decisiones con que lo cerró son transferibles a este ítem sin traer código: la detección es **angosta a propósito** (reconoce el placeholder por la misma definición que lo escribe, y fuera de eso sólo un `TBD`/`TODO` que abra el texto); es **WARN y no ERROR**, para que un repositorio con placeholders ya en disco siga validando y sólo `--strict` falle; el texto **entre backticks no cuenta**, porque un documento que cita el marcador no lo está usando; y un hallazgo de placeholder **no se reporta además como «demasiado breve»**, para que un caso produzca un mensaje y no dos. Detalle en `../software/analisis/ANALISIS-OPENSPEC.md` §Nota menor.

---

## `agent-loop-lab` entra a la lista de repositorios hermanos (2026-10-07) — COMPLETADA

**Acción**: alta de un repositorio hermano en `CONVENCIONES.md` §Citas a fuentes externas, por el mecanismo que esa línea prevé («Sumar uno es editar esta línea»). Lo pide el ítem #24 de `agenda/BACKLOG-INVESTIGACION.md`, que cita un archivo de `agent-loop-lab` —proyecto del mismo autor, construido con Kiro— y sin el alta `ruta-externa` lo rechaza.

### Qué cambió
- **`CONVENCIONES.md`**: la lista de hermanos admitidos suma `agent-loop-lab`. Ninguna otra regla cambia.

### Validación
`tools/check_docs.py` en verde (0 ERROR, 0 WARN) con la cita del ítem #24 presente. Antes del alta, el mismo check daba `ruta-externa` sobre esa cita.

### Deuda abierta
- ninguna

---

## M-37: el registro retira el nivel «Extendida» y el campo `refresh` (2026-10-07) — COMPLETADA

**Acción**: M-37 resuelta con la segunda salida del ítem, retirar el nivel, aprobada por el usuario en la tanda del 2026-10-07. Es la más barata y la que menos promete. Aplicarlo a los dos documentos que calificaban habría completado una tabla que nadie consulta, que es como nacieron las 195 casillas de M-35.

### Qué cambió
- **`SPECS_REGISTRY.md` §Profundidad de spec**:
  - La tabla queda en dos niveles: se va la fila `Extendida`, con su campo `refresh` y sus requisitos con `[ ]`.
  - `Estandar` pasa a aplicarse a «SSOTs y derivados», porque los SSOT críticos que antes iban a `Extendida` caen ahí.
  - Una línea deja escrito que un nivel con campo de refresco se agrega cuando haya quien lo consuma.
- **`agenda/MEJORAS-METODO.md`**: M-37 pasa a `Hecha` y su planteo migra acá abajo.

### Validación
`tools/check_docs.py` en verde (0 ERROR, 0 WARN). Antes de retirarlo se comprobó que nada lo leía:
- `refresh` no aparece en el backstop, ni en `SPEC_FIELD_LINE`, ni entre los ocho campos reservados de §Reglas globales.
- Las otras menciones a `Extendida` o `refresh` son registro fechado (`historial/ROADMAP-MEJORAS-SDD.md` y una entrada de este historial) o citas textuales de Kiro [R44].

### Límite
`docs-y-investigacion/NECESIDADES-Y-METRICAS.md` §Riesgos y mitigacion dice «specs minimas por defecto, extendidas solo en docs de alto impacto». Se dejó como está: usa «extendidas» como adjetivo y no nombra el nivel, y la mitigación que describe sigue valiendo con dos niveles.

### Planteo migrado del backlog (2026-10-07)

#### M-37 — El nivel «Extendida» y el campo `refresh` están declarados y no los usa ninguna spec

La tabla de profundidad de `../SPECS_REGISTRY.md` define tres niveles de spec, y el nivel `Extendida` se distingue por llevar el campo `refresh`. Distribución real medida el 2026-08-30 sobre las 46 entradas: **36 `Estandar`, 10 `Minima`, 0 `Extendida`**. El campo `refresh` aparece una sola vez en todo el repositorio — en la fila de la tabla que lo define.

Y hay dos documentos que cumplen el criterio que la propia tabla declara para `Extendida` («SSOTs criticos con multiples derivados»): `../software/analisis/ANALISIS-SPEC-KIT.md` y `../experimentos/b07-formato-hibrido/EXPERIMENTO-B7-formato-hibrido.md`, cada uno con dos derivados registrados. Ninguno lo usa.

Es una instancia del patrón 4 de `sdd-first:docs/PATRONES.md` («la carpeta que existe y ningún paso mira»): una clave de primera clase que ningún consumidor visita. No falla — calla, y el silencio se lee como salud.

Dos salidas, y no hay una obviamente mejor:

1. **Aplicarlo** a los dos documentos que califican, y con eso averiguar si `refresh` sirve para algo. Riesgo: se aplica por completar la tabla y no porque alguien necesite el dato, que es cómo nacen los campos que después nadie mantiene — el mismo destino de las 195 casillas de M-35.
2. **Retirarlo**, dejando dos niveles. Es la más barata y la que menos promete. Si más adelante hace falta un campo de refresco, se agrega con un consumidor.

Lo que no se sostiene es dejarlo declarado sin usuarios: el registro afirma una taxonomía de tres niveles y opera con dos.

### Deuda abierta
- ninguna

---

## M-43: `AGENTS.md` declara cross-asistente sólo lo comprobado (2026-10-07) — COMPLETADA

**Acción**: M-43 resuelta con la tercera salida del ítem, acotar la declaración por escrito, aprobada por el usuario en la tanda del 2026-10-07. El ítem preguntaba qué hace el repositorio con su propia declaración mientras nadie la verifique, y esta salida responde eso. Verificarla (salida 1) es la pregunta 1 de alta prioridad de `agenda/BACKLOG-INVESTIGACION.md`, que sigue abierta. Instrumentarla con adaptadores (salida 2) no tiene dato que la justifique.

### Qué cambió
- **`AGENTS.md`, encabezado**: antes afirmaba que opencode, Cursor, Codex, Aider y Gemini CLI «lo leen directo». Ahora distingue tres niveles de evidencia:
  - Claude Code, por el import de `CLAUDE.md`, es el asistente con el que se trabaja el repositorio.
  - `agy` es el único comprobado que lee el `AGENTS.md` de la raíz y lo obedece, según el hallazgo 5 de A-04.
  - Para el resto rige la convención de cada herramienta, no un uso verificado acá.

  El encabezado también declara que nadie midió que el mismo protocolo produzca la misma conducta en asistentes distintos.
- **`agenda/MEJORAS-METODO.md`**: M-43 pasa a `Hecha` y su planteo migra acá abajo.

### Validación
`tools/check_docs.py` en verde (0 ERROR, 0 WARN). Se buscó en los documentos vivos cualquier otra afirmación de neutralidad entre asistentes:
- `CLAUDE.md` y la spec de `AGENTS.md` en el registro dicen «estándar cross-asistente». Se refieren a la convención del nombre de archivo, que es cierta, y quedan como están.
- La de `software/COMPARATIVA-SPECKIT-VS-TESTIGO.md` habla del proyecto testigo, no de este repositorio.

### Límite
El hallazgo 5 de A-04 comprobó que `agy` obedece un `AGENTS.md` de prueba con dos instrucciones de forma, no este protocolo entero. Sigue sin verificar la afirmación de Superpowers [R37] de que Claude Code lee `AGENTS.md` sólo cuando no hay `CLAUDE.md`. Acá no cambia nada, porque `CLAUDE.md` existe y lo importa.

### Planteo migrado del backlog (2026-10-07)

#### M-43 — El protocolo se declara cross-asistente y nadie verificó que lo sea

`../AGENTS.md` abre declarando que es el SSOT del protocolo, que los asistentes que buscan `AGENTS.md` por convención lo leen directo y que Claude Code lo recibe por import. La afirmación operativa detrás de esa arquitectura es que **el mismo documento produce el mismo comportamiento en asistentes distintos**, y nadie la verificó: todo el trabajo de este repositorio se hizo con uno o dos.

[R56] mide ese supuesto en el dominio vecino —specs, no protocolos— y en el caso extremo lo encuentra falso: una especificación producida por un agente y consumida directamente por otro degrada fuerte y de forma dependiente del agente. Su límite está declarado en la referencia y es serio: el estudio es traducción de dialecto SQL, no prosa normativa, así que **no prueba nada sobre protocolos**. Lo que aporta es que el supuesto de neutralidad es falsable y que, donde se lo midió, falló.

Y aporta algo más útil que la advertencia: el mecanismo que propone —mantener una especificación estructurada común y entregar **vistas adaptadas por agente**— es la arquitectura que este repositorio ya tiene a medias, con `AGENTS.md` como fuente y `CLAUDE.md` como adaptador de una línea.

Tres salidas, y hoy no hay dato para elegir entre las dos primeras:

1. **Verificarlo**: una sonda barata —mismo pedido, mismo protocolo, dos asistentes, comparar qué partes del protocolo se ejercen— que es trabajo de investigación y no de método.
2. **Instrumentarlo**: adaptadores por asistente más allá del import de una línea, que es la dirección que sugiere [R56] y cuesta mantenimiento.
3. **Acotar la declaración por escrito** a los asistentes con los que efectivamente se ejerció. Es la barata y la honesta mientras no haya sonda, y no cierra ninguna de las otras dos.

**Señalado sin verificar (2026-09-30).** Superpowers [R37] afirma que Claude Code lee `AGENTS.md` sólo cuando no existe `CLAUDE.md`. Si es así, en Claude Code este repositorio funciona por el import de `CLAUDE.md` y no por la convención, y la arquitectura de fuente más adaptador ya es la única vía, no un refuerzo. Llega por una fuente y no se probó.

**Contraparte de investigación**: el ítem 1 de prioridad alta de `BACKLOG-INVESTIGACION.md` («medir variabilidad entre asistentes IA») es la misma pregunta del lado del conocimiento. Acá se decide qué hace el repositorio con su propia declaración mientras esa pregunta siga abierta.

### Deuda abierta
- ninguna

---

## M-42: el marcador `[NEEDS CLARIFICATION]` registra lo asumido y lo que cuesta si está mal (2026-10-07) — COMPLETADA

**Acción**: M-42 ejecutada tal como la proponía el ítem. Es la tercera de la tanda aprobada por el usuario el 2026-10-07. Un marcador que no bloquea significa que el trabajo siguió sobre alguna lectura de la duda, y esa lectura ahora puede quedar escrita al lado de la pregunta.

### Qué cambió
- **`AGENTS.md` §Disambiguación**: cuando el trabajo siguió sobre una lectura provisional, el marcador SHOULD llevar `asumido:` y `costo:`. Los dos campos son opcionales, como pedía el ítem: un marcador que bloquea no tiene asunción que declarar. No se relaja la obligación de preguntar del Principio VII. La parte de Superpowers [R37] que decide y sigue sin humano no se adopta.
- **`agenda/MEJORAS-METODO.md`**: M-42 pasa a `Hecha` y su planteo migra acá abajo.

### Validación
`tools/check_docs.py` en verde (0 ERROR, 0 WARN), sin tocar el backstop. Se comprobó lo que el ítem ya había verificado el 2026-09-05: `CLARIFICACION` captura todo hasta el corchete de cierre, y `es_placeholder()` trata la forma de tres campos citada con metavariables como relleno, porque empieza con `<` y termina con `>`. El marcador nuevo no aparece en ningún otro documento que defina su forma.

### Límite
El campo `costo:` ordena las dudas por lo que cuestan pero no las mide. Si con él se pregunta menos o mejor es la pregunta #23 de `agenda/BACKLOG-INVESTIGACION.md`, y ahora los marcadores escritos con esta forma le aportan datos.

### Planteo migrado del backlog (2026-10-07)

#### M-42 — El marcador `[NEEDS CLARIFICATION]` registra la pregunta y no lo que se asumió ni lo que cuesta si está mal

`../AGENTS.md` §Disambiguación permite marcar incertidumbre puntual con `[NEEDS CLARIFICATION: <pregunta>]` cuando no bloquea el resto del trabajo. El marcador es grep-able, el check `clarificacion` verifica que ningún documento `Activo` conserve uno abierto, y hasta ahí funciona.

Lo que no registra es qué hizo el asistente mientras tanto. Un marcador que no bloquea significa, por definición, que el trabajo siguió — y siguió sobre **alguna** lectura de la ambigüedad. Esa lectura hoy no queda escrita en ningún lado: quien resuelve el marcador más tarde ve la pregunta, no la respuesta provisional que el texto ya está asumiendo, y no tiene forma de saber cuánto del documento se cae si la respuesta es la otra.

Superpowers v6.3.0 [R37] resuelve la mitad simétrica del problema con una forma de tres campos: `Ruling: <qué se decidió> — <por qué> — <cuánto cuesta si está mal>` (`../software/analisis/ANALISIS-SUPERPOWERS.md` C7). El tercer campo es el que falta acá: convierte una duda anotada en una duda **priorizable**.

Propuesta concreta, mínima: extender el marcador a `[NEEDS CLARIFICATION: <pregunta> | asumido: <lectura provisional> | costo: <qué se rehace si está mal>]`, con los dos campos nuevos opcionales — un marcador que sí bloquea no necesita declarar asunción porque no la hay.

**Qué NO propone este ítem, y conviene que quede escrito**: no relaja la obligación de preguntar. El Principio VII manda preguntar ante ambigüedad y detener ante contradicción, y eso no se toca; el marcador cubre el caso que el propio principio ya excluye —incertidumbre puntual que no bloquea—. Superpowers va bastante más lejos (decide y sigue sin humano para todo conflicto no catastrófico), y **esa parte no se propone**: es constitucional, responde a un riesgo distinto — proteger una corrida autónoma larga, no evitar que el asistente interprete en silencio — y su única evidencia es un caso autoreportado.

Costo de implementarlo: una línea en `../AGENTS.md` y ninguna en el backstop. Verificado el 2026-09-05: `CLARIFICACION` de `../tools/check_docs.py` captura `([^\]]*)` —todo hasta el corchete de cierre— así que los dos campos nuevos entran en el payload sin tocar el patrón, y `es_placeholder()` los distingue de un marcador de relleno por la misma vía que hoy.

### Deuda abierta
- ninguna

---

## M-31, pasos 1 y 2: la tabla SSOT vacía falla, y el check de rutas dice que sólo mira `.md` (2026-10-07) — COMPLETADA

**Acción**: dos de los tres pasos de M-31, aprobados por el usuario en la misma tanda que M-38. Los dos cierran casos en que el backstop sale en verde sin haber mirado lo que su nombre promete. El paso 3, auditar el resto de las derivaciones y escribir la regla, sigue abierto en el ítem.

### Qué cambió
- **`tools/check_docs.py`, paso 1**: `check_ssot_table` emite ERROR si la tabla SSOT no se encontró o no dio filas. Antes, `ssot-table` y `ssot-collision` recorrían cero filas y el backstop salía en verde. La tabla se parsea una vez y la usan los dos checks.
- **`tools/check_docs.py`, paso 2**: de las dos salidas del ítem se tomó la honesta, que no exige convención nueva. El check sigue mirando sólo rutas `.md`, y ahora lo dice: el id pasa de `rutas` a `rutas-md`, la función de `check_backtick_paths` a `check_backtick_md_paths`, y el docstring declara el alcance y por qué no se amplía.
- **Casos de la tabla de regresión**: `ssot-table-vacia`, nuevo, y `rutas`, que pasa a `rutas-md`.
- **`AGENTS.md`**: la enumeración de lo que cubre el backstop dice «rutas `.md` escritas en backticks».
- **`docs-y-investigacion/ANALISIS-CASO-CAMPO-1.md`**: el nombre de la función se actualiza donde el análisis la cita.
- **`agenda/MEJORAS-METODO.md`**: M-31 pasa a `Aprobada` con los pasos 1 y 2 hechos.

### Validación
`tools/check_docs.py` en verde (0 ERROR, 0 WARN). `--autotest`: 35 casos, 0 fallas. Con la guarda anulada, el caso `ssot-table-vacia` falla.

### Límite
El ítem citaba como «error liso» un `./tools/check_docs.py` del historial. Al revisarlo resultó ser el comando que se corrió, no una cita, y está en el tomo cerrado `historial/sdd-2026-T1-T3.md`, que no se edita. Las 42 rutas no-`.md` a herramientas del proyecto testigo siguen sin que nada las mire. El hueco ahora está declarado en el docstring en lugar de quedar oculto bajo el nombre del check.

### Deuda abierta
- Paso 3 (auditar las derivaciones y los reconocedores, y escribir la regla): M-31.

---

## M-38: el título de cada bloque del registro nombra uno de sus `path` (2026-10-07) — COMPLETADA

**Acción**: M-38 ejecutada, primera de la tanda de cinco mejoras baratas que aprobó el usuario el 2026-10-07. Se corrigieron los siete títulos y, sobre todo, se agregó el check que el propio ítem pedía: corregirlos sin guarda deja que el octavo nazca igual.

### Qué cambió
- **`SPECS_REGISTRY.md`**: los siete títulos `### docs-y-investigación/...` pasan a `docs-y-investigacion/`, el directorio real. El campo `path` de cada bloque ya estaba bien.
- **`tools/check_docs.py`**: check `registro-encabezado` (ERROR). Cada ruta `.md` que nombra el título de un bloque tiene que ser uno de sus `path`. Los bloques de dos documentos (`A y B`) se miran ruta por ruta. Es ERROR porque no tiene falsos positivos: la ruta está declarada o no lo está.
- **Caso `registro-encabezado`** en la tabla de regresión: el título de un bloque gana una ruta que no declara. El caso deja el texto original como prefijo del título mutado; si lo borrara, `autotest-anclas` lo marcaría dentro de la propia copia, que fue lo que pasó en el primer intento.
- **`agenda/MEJORAS-METODO.md`**: M-38 pasa a `Hecha` y su planteo migra acá abajo.

### Validación
`tools/check_docs.py` en verde (0 ERROR, 0 WARN). Antes de corregir los títulos, el check nuevo dio exactamente los siete ERROR del recuento del ítem. `--autotest`: 34 casos, 0 fallas. Con el check convertido en no-op, el caso nuevo falla.

### Planteo migrado del backlog (2026-10-07)

#### M-38 — Seis encabezados del registro escriben un directorio que no existe

Seis entradas de `../SPECS_REGISTRY.md` titulan su bloque `### docs-y-investigación/...`, con tilde. El directorio en disco es `docs-y-investigacion/`, sin tilde. Nada lo detecta porque `parse_registry()` toma la ruta del campo `path` —que está bien escrito en las seis— y el encabezado queda como decoración.

No rompe nada hoy. Lo que hace es peor a largo plazo: quien lea el registro y copie el encabezado escribe una ruta inválida, y el próximo consumidor que decida parsear los `### ` en vez del campo `path` hereda seis fallas silenciosas.

**Uno de los seis lo escribí yo el 2026-08-30**, dando de alta la spec del análisis de caso, copiando la convención local sin verificar que el directorio existiera. Vale registrarlo porque es la evidencia del patrón 1 de `sdd-first:docs/PATRONES.md` en su forma más literal: el archivo número siete nace roto igual que el primero, y lo que sostiene el fix no es corregir los seis sino un check que falle nombrando al séptimo.

Qué hace falta: corregir los seis encabezados, y agregar al backstop la verificación de que el encabezado de cada bloque coincida con alguno de sus `path` declarados. El check es de tres líneas y ya tiene los dos insumos parseados.

Prioridad baja, no nula: es higiene, pero la guarda es tan barata que postergarla cuesta más en discusión que en implementación.

**Recuento (2026-10-06).** Ya son siete: a los seis se sumó el de `ANALISIS-EDICION-COLABORATIVA-IA.md`. El patrón se reprodujo mientras el ítem estaba abierto, que es lo que el párrafo anterior predecía.

### Deuda abierta
- ninguna

---

## M-49: el backstop verifica en cada pasada que las anclas de su tabla de regresión sigan existiendo (2026-10-07) — COMPLETADA

**Acción**: M-49 ejecutada con la tercera de las salidas evaluadas, elegida por el usuario. Las dos del planteo de abajo quedaron descartadas. Correr la tabla completa en cada commit que toca un documento usado por un caso cuesta unos veinte segundos en commits frecuentes: `SPECS_REGISTRY.md` se tocó en 38 commits desde agosto. Anclar todos los casos en estructura es disciplina, no verificación. Lo que se rompía en silencio era un texto ausente, y ver un texto ausente no exige correr la tabla: alcanza con buscarlo.

### Qué cambió
- **`tools/check_docs.py`**: check `autotest-anclas` (ERROR), que corre siempre y tarda milisegundos.
  - Por cada `replace` de `AUTOTEST_CASOS`, el texto que reemplaza tiene que existir en su documento.
  - Se saltea el `replace` sobre un archivo que una operación anterior del mismo caso ya modificó.
  - Es ERROR porque no tiene falsos positivos: o el texto está o no está. Quien cambia el texto actualiza el caso, y al tocar `tools/` el gate corre la tabla completa.
- **Caso `autotest-anclas`** en la tabla: la copia gana un caso con un ancla inexistente.
- **`agenda/MEJORAS-METODO.md`**: M-49 pasa a `Hecha` y su planteo migra acá abajo.

### Validación
`tools/check_docs.py` en verde (0 ERROR, 0 WARN). `--autotest`: 33 casos, 0 fallas. Dos roturas inyectadas, restauradas después:
- **El ancla vieja del historial**, `del proyecto.` antes del separador, que es la falla real de `fe965b1`: el check da 4 ERROR en una pasada normal, sin `--staged` ni tabla.
- **El check convertido en no-op**: el caso nuevo falla.

El primer intento de la primera rotura no se aplicó, porque el `sed` no encontró el texto. Se rehízo con un script que afirma haber encontrado el texto antes de reemplazarlo: la misma trampa que registró M-34.

### Límite
El check verifica que el ancla exista, no que el caso siga probando lo que declara. Está declarado en su docstring.

### Planteo migrado del backlog (2026-10-07)

#### M-49 — La tabla de regresión sólo corre cuando el commit toca `tools/`

`check_autotest` corre `AUTOTEST_CASOS` sólo en commits que tocan `../tools/`, porque tarda unos veinte segundos. Pero varios casos mutan documentos reales con `replace` y dependen de su texto. Un commit que cambia ese texto sin tocar `tools/` deja casos desactualizados y nadie se entera hasta el próximo commit de tooling. Pasó el 2026-10-07: la pieza 2 de M-30 cambió el encabezado de `../historial/sdd.md` y tres casos de `deuda-punteros` quedaron apuntando a un texto que ya no existía. La pieza 3 los arregló anclando en el separador en vez de en el encabezado. Eso arregla esos tres, no la clase.

Dos salidas posibles, sin decidir: correr también la tabla cuando el commit toca un archivo que algún caso muta con `replace`, que se puede derivar de la propia tabla; o anclar todos los casos en estructura y no en prosa, que es disciplina y no verificación.

### Deuda abierta
- ninguna

---

## M-30, pieza 3: `historial-rotacion` avisa cuándo rotar, y M-30 queda cerrada (2026-10-07) — COMPLETADA

**Acción**: tercera y última pieza de M-30. Un check avisa cuándo toca rotar, para que la regla de la pieza 2 no dependa de que alguien se acuerde. Es la forma en que falló el índice manual de [R40], citado en el planteo de abajo.

### Qué cambió
- **`tools/check_docs.py`**: check `historial-rotacion`, que emite WARN si las entradas del archivo vivo abarcan más de un trimestre.
  - No depende del reloj, porque compara las entradas entre sí.
  - Es WARN y no ERROR porque la entrada que lo dispara es legítima. Bloquearla obligaría a rotar dentro de un commit que trata de otra cosa.
  - Caso `historial-rotacion` en `AUTOTEST_CASOS`.
- **Tres casos de `deuda-punteros` reanclados.** Su ancla era el texto del encabezado del historial, que la pieza 2 cambió, y quedaron desactualizados sin que el gate lo viera: el autotest sólo corre cuando el commit toca `tools/`. Ahora anclan en el primer separador y toman el mes de la entrada más reciente, para no abrir un trimestre en casos que no lo miran. La clase del problema queda como M-49.
- **`AGENTS.md`**: la lista de checks que emiten WARN suma `historial-rotacion`.
- **`agenda/MEJORAS-METODO.md`**: M-30 pasa a `Hecha` y su planteo migra acá abajo; alta de M-49.

### Validación
`tools/check_docs.py` en verde (0 ERROR, 0 WARN). `--autotest`: 32 casos, 0 fallas. Se probó al probador de dos formas, y en las dos se restauró después:
- Con el check convertido en no-op, el caso nuevo falla.
- Contra el `historial/sdd.md` de `7f3107f`, anterior a la rotación, el check emite `el archivo vivo abarca 4 trimestres (2026-T4, 2026-T3, 2026-T2, 2026-T1)`.

### Planteo migrado del backlog (2026-10-07)

#### M-30 — `historial/sdd.md` crece sin techo y no tiene regla de rotación

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

**Aprobada el 2026-10-07, con dos correcciones al planteo.** El usuario eligió rotación **trimestral**, no semestral, y un check que avise cuando toca rotar. El semestre no sirve: al 2026-10-07 el segundo semestre ya concentraba 72 de las 76 entradas (2295 de 2427 líneas), así que cerrar el primero movía 4. Las dos premisas de arriba que no se sostienen: el consumidor 2 lee el historial **del testigo**, no este (`../experimentos/b06-circuito-testigo/RESULTADO-EXPERIMENTO-B6.md`, §Evidencia adjunta); y «nada en `../tools/check_docs.py`» dejó de ser cierto con M-40, porque `backlog-metodo` resuelve los punteros de los ítems `Hecha` contra el historial.

### Deuda abierta
- La tabla de regresión no corre cuando un commit cambia texto que sus casos usan: M-49.

---

## M-30, pieza 2: el historial rota por trimestre, y el tercer trimestre de 2026 pasa a su tomo (2026-10-07) — COMPLETADA

**Acción**: regla de rotación escrita en el registro y aplicada por primera vez. Las 68 entradas anteriores al 2026-10-01 se trasladan sin cambios a `historial/sdd-2026-T1-T3.md`. El archivo vivo pasa de 2452 a 268 líneas y conserva las 9 entradas del cuarto trimestre. Motivo, en palabras del usuario: «que haya propuestas no realizadas no es un problema; que tengamos un contexto alto sin necesidad sí lo es».

### Qué cambió
- **`SPECS_REGISTRY.md`**, spec de `historial/sdd.md`:
  - rotación trimestral al asentar la primera entrada de un trimestre nuevo, sin umbral por tamaño, declarado como elección;
  - «mover no es reescribir»;
  - una cita a `historial/sdd.md` designa el archivo vivo y los tomos, así que las citas existentes —algunas en experimentos sellados— no se tocan.
- **Spec nueva de `historial/sdd-2026-T1-T3.md`**, registro histórico cerrado. Junta tres trimestres porque los dos primeros tenían una y tres entradas.
- **`historial/sdd.md`**: una línea fija remite a los tomos por patrón, no por lista. El índice mantenido a mano es la variante que falló en [R40] (planteo de M-30).
- **`00-INDEX.md`**: la fila de `historial/` nombra el archivo vivo y los tomos.

### Validación
El traslado se hizo por script y se verificó que el cuerpo del archivo vivo, concatenado con el del tomo, es idéntico byte a byte al cuerpo original. Las fechas de los encabezados ya estaban en orden descendente, y el corte cae en la primera entrada anterior al 2026-10-01. `tools/check_docs.py` en verde (0 ERROR, 0 WARN): los punteros de los ítems `Hecha` que ahora viven en el tomo resuelven gracias a la pieza 1.

### Deuda abierta
- Pieza 3, el check `historial-rotacion`: M-30.

---

## M-30, pieza 1: `backlog-metodo` resuelve los punteros también contra los tomos cerrados del historial (2026-10-07) — COMPLETADA

**Acción**: primera de tres piezas de M-30, aprobada por el usuario el 2026-10-07 con rotación trimestral y un check que avise cuándo rotar. Va primero porque la rotación mueve las entradas a las que apuntan los 22 ítems `Hecha` de `agenda/MEJORAS-METODO.md`. Si el check no supiera buscar en los tomos, el commit de la rotación nacería con 22 WARN falsos.

### Qué cambió
- **`tools/check_docs.py`**: constante `HISTORIAL_TOMOS` (`historial/sdd-*.md`, por patrón, no por lista) y función `historial_completo()`, que devuelve el archivo vivo más los tomos. `backlog-metodo` busca ahí los punteros. Mientras no exista ningún tomo, la conducta es idéntica a la anterior.
- **Caso `backlog-metodo-tomo`** en `AUTOTEST_CASOS`: un puntero que sólo existe en un tomo deja un único WARN, el de estado, en vez de dos.
- **`agenda/MEJORAS-METODO.md`**: M-30 pasa a `Aprobada`, con las dos premisas del planteo que no se sostenían.

### Validación
`tools/check_docs.py` en verde (0 ERROR, 0 WARN). `--autotest`: 31 casos, 0 fallas. Para probar al probador, se dejó `historial_completo()` devolviendo sólo el archivo vivo: el caso nuevo falló con el WARN de más que se esperaba, y se restauró.

### Deuda abierta
- Piezas 2 (regla en el registro y rotación) y 3 (check `historial-rotacion`): M-30.

---

## M-34 — El backstop tiene tabla de regresión, y la corre al tocar sus propios checks (2026-10-06) — COMPLETADA

**Acción**: M-34 ejecutada con el alcance mínimo que el propio ítem pedía: casos declarados como datos dentro de `tools/check_docs.py`, corridos por el mismo script, sin framework (el patrón `--autotest` de [R40]). La aprobó el usuario como primera mejora de la segunda tanda de la revisión de la forma de trabajo. El disparador concreto fue esta misma sesión: tres checks nuevos validados copiando, inyectando y restaurando a mano, y ninguna de esas pruebas había quedado escrita.

### Qué cambió
- **`tools/check_docs.py`**: tabla `AUTOTEST_CASOS` con 30 casos. Cada uno copia el árbol a un directorio temporal con su propio git y el gate cableado, aplica mutaciones (agregar, escribir, reemplazar, comando git, stage), corre el script real sobre la copia y exige **exactamente** los hallazgos esperados. Si aparece uno de más, es un falso positivo y el caso falla. Incluye casos de borde que no deben disparar: un link dentro de código, una mención del marcador, un bloque `[SDD-Check]` como instancia, citas válidas a repositorio, `00-INDEX.md` staged y deuda con puntero. Un `replace` cuyo texto ya no existe falla como «caso desactualizado», para que la tabla no se pudra en silencio.
- **Modo `--autotest`**, y check `autotest` en modo `--staged` sólo cuando el commit toca `tools/`: tarda unos 16 s con los casos en paralelo.
- **`AGENTS.md`**: el modo commit nombra el tercer check, y un check nuevo MUST sumar su caso.
- **`agenda/MEJORAS-METODO.md`**: M-34 pasa a `Hecha` y su planteo migra acá abajo.

### Validación
`--autotest`: 30 casos, 0 fallas. Como un autotest que nunca falla es justo la trampa de M-31, se probó al probador con tres roturas inyectadas y restauradas: `check_links` convertido en no-op (falla el caso `links`), una expectativa falsa (falla `links-en-codigo`) y un ancla borrada (falla `constitucion` como caso desactualizado). El primer intento de la segunda rotura dio verde porque el reemplazo no había encontrado su texto por un escape de comillas, y la rotura nunca se había aplicado. Se rehízo verificando que el texto se encontrara. `tools/check_docs.py` normal y con `--staged` en verde.

El gate encontró además un falso positivo de `deuda-punteros` en esta misma entrada: el check sólo aceptaba rutas `.md`, y la deuda de abajo apunta a `tools/check_docs.py`. Ahora acepta rutas con cualquier extensión, y la tabla suma ese caso.

### Planteo migrado del backlog (2026-10-06)

#### M-34 — Un check que clasifica no tiene tabla de regresión que lo pruebe

Varios checks de `../tools/check_docs.py` no verifican una propiedad: **clasifican**. `excluded-field` decide si una celda es una anotación de campo o prosa legítima; `sdd-check-fields` decide si un texto es una definición o una instancia; `ssot-collision` decide si dos specs hablan del mismo tema; `metodo-historial` decide si un archivo es método. Todos tienen frontera difusa y todos la ajustaron al menos una vez (M-23, M-27, y M-21 sigue abierto).

Un clasificador mal calibrado no se manifiesta como un error: se manifiesta como **trabajo legítimo bloqueado**, y el remedio que la gente encuentra sola es desactivar el gate. Es el mismo razonamiento por el que el `propagacion` de [R40] emite WARN y no ERROR.

En [R40] el hueco se cerró con un check `gate-reglas`: el gate lleva su tabla de regresión al lado de sus propias reglas, expuesta como `--autotest`, y el backstop la corre en cada pasada. El invariante es que las reglas sigan clasificando como declaran, verificado por el mismo script que las usa.

Acá el hueco es doble y conviene no confundirlo: no hay tabla de casos **ni** hay quien la corra. `../tools/check_docs.py` no tiene tests de ningún tipo; su única verificación es correr sobre el árbol real, que sólo contiene los casos que hoy existen. Cada ajuste de frontera se validó a mano y esa validación no quedó ejecutable en ningún lado.

Reserva antes de aprobarla: sumar una suite de tests es una dependencia nueva y un cambio de naturaleza — hoy `tools/` está declarado «no es pieza documental autorada» y vive sin infraestructura. El alcance mínimo que lo evita es el de [R40]: casos declarados como datos dentro del propio script, corridos por un check más, sin framework.

### Deuda abierta
- Checks sin caso en la tabla: la lista vive en el comentario de `AUTOTEST_CASOS` (`tools/check_docs.py`), donde también se declara que un check nuevo MUST sumar el suyo.
- M-31 y M-38, los siguientes de la misma revisión.

---

## Triaje de la deuda de septiembre y octubre con la regla nueva (2026-10-06) — COMPLETADA

**Acción**: aplicación de la regla de la entrada anterior a los pendientes de las entradas del 2026-09-01 en adelante. El usuario revisó y aprobó la tabla de destinos antes de aplicarla.

### Resultado
Juntando los repetidos quedaron 35 pendientes distintos. Así se distribuyeron:
- **Resueltos sin acción (13)**: M-40 y las tres deudas cerradas el mismo día; re-anclajes y propagaciones del 2026-09-05 y del 2026-09-30; la orientación práctica creada; el no-determinismo de Tessl (#20); los clones vivos (no hay clones desde el 2026-10-05); las líneas 337 y 398 de la orientación práctica (corregidas el 2026-09-30); las versiones de los brazos de B-09, que su §Sello ya obliga a fijar.
- **Límites, dejan de contar como deuda (8)**: entre ellos, la dirección Kiro → Spec Kit/OpenSpec, cuya búsqueda de marcadores (2026-09-06) dio negativa.
- **Método**: M-47 y M-48 nuevos, nota fechada en M-43, M-21 ya anotado (commit `c0de612`).
- **Investigación**: #23 nuevo y nota fechada en #19 (commit `c64ba7f`).
- **Ediciones de documentos**: un bloque `[SDD-Check]` de consolidación en seis documentos, que lista lo abierto, lo cerrado y lo derivado a otro lugar, sin la cadena «la de la entrega anterior sigue entera» (commit siguiente a `c64ba7f`).

### Qué cambió respecto de la tabla aprobada
Tres reclasificaciones hechas al aplicarla, las tres porque ya había una decisión escrita:
- **La dirección Kiro → Spec Kit/OpenSpec** no abre ítem: la búsqueda ya se hizo y da límite, no pregunta.
- **Las dos preguntas de OpenSpec (C6, C7)** no abren ítem: su entrada del 2026-09-05 decidió no darlas de alta a medias. Quedan en el bloque de su documento como edición pendiente: formularlas.
- **Las versiones de B-09** no son deuda: §Sello ya lo exige.

Apareció además un caso que el triaje no vio porque estaba en un bloque viejo: en `software/analisis/ANALISIS-SPEC-KIT.md`, «si la formalización de la precedencia merece experimento propio», que nunca llegó a ningún backlog. Quedó en el bloque de su documento.

### Validación
`tools/check_docs.py` en verde (0 ERROR, 0 WARN), normal y con `--staged`, en cada uno de los cuatro commits. Cada «resuelto» se contrastó con la entrega que lo resolvió.

### Deuda abierta
- Las 46 entradas anteriores al 2026-09-01 conservan su deuda en prosa y no se triaron: es registro datado (`historial/sdd.md`), y lo vigente de ellas ya debería estar en sus documentos.
- M-21, M-47 y M-48, abiertos en el backlog de método.

---

## La deuda vive donde se resuelve, y el historial sólo apunta (2026-10-06) — COMPLETADA

**Acción**: cambio de método aprobado por el usuario, opción C de la revisión de la forma de trabajo de hoy. El historial juntaba 178 pendientes en 55 secciones «Deuda abierta» y nada registraba qué pasaba con cada uno. Releídos los de septiembre y octubre, había de todo: deuda real, deuda ya resuelta y límites sin remedio, mezclados y descritos en prosa que cambiaba de una entrada a otra.

### Qué cambió
- **`AGENTS.md`, campo `Deuda arrastrada`**: lo diferido vive en un solo lugar y se cita por ID o ruta. Método va a `agenda/MEJORAS-METODO.md`; una pregunta, a `agenda/BACKLOG-INVESTIGACION.md`; una edición pendiente de un documento, al `[SDD-Check]` de ese documento; el diseño de un experimento, a su `EXPERIMENTO-*.md`. Re-explicitar pasa a ser que el ID siga abierto donde vive. Un límite sin remedio no es deuda. Así se generaliza a toda entrega la regla que `SPECS_REGISTRY.md` ya aplicaba al cerrar experimentos: la deuda no queda atada al cierre siguiente.
- **El cuarto destino** (el bloque del propio documento) lo agregó el usuario al ver el triaje: unas diez deudas eran ediciones pendientes de documentos puntuales, que no son preguntas de investigación ni cambios de método.
- **`tools/check_docs.py`**: check nuevo `deuda-punteros` (ERROR, sólo con `--staged`). Cada viñeta de «Deuda abierta» de una entrada nueva tiene que citar un `M-NN`, un `#N`, un ID de experimento, una ruta, o decir «ninguna». Las entradas anteriores no se tocan.

### Validación
`tools/check_docs.py` en verde, normal y con `--staged`. Se inyectó una entrada con cuatro viñetas —sin puntero, con `M-21`, «ninguna» y con una ruta— y sólo dio ERROR la primera. La sección de abajo es el primer caso real del check.

### Deuda abierta
- Triaje de los pendientes de sep-oct según esta regla: en revisión del usuario. Hasta entonces, las deudas de las entradas anteriores siguen descritas en ellas (`historial/sdd.md`).
- M-21, agravado desde M-40.

---

## M-35 — Las validaciones del registro dejan de ser casillas (2026-10-06) — COMPLETADA

**Acción**: M-35 ejecutada con la salida 3, elegida por el usuario. La salida 2 —que `Validaciones aplicadas` del `[SDD-Check]` nombre las validaciones de la spec y un check lo compruebe— se descarta: la mayoría de los bloques se entregan en el chat y no quedan en el repositorio, así que el check vería sólo los 18 documentos que llevan el bloque adentro.

### Qué cambió
- **`SPECS_REGISTRY.md`**: las 246 casillas `[ ]` de `validacion` (eran 195 cuando se midió M-35, el 2026-08-30), ninguna marcada nunca, pasan a ser viñetas sin casilla. §Profundidad de spec suma una línea que dice qué es el campo: criterios de revisión permanentes, no tareas.
- **`tools/check_docs.py`**: `spec-fields` da ERROR si una viñeta de `validacion` vuelve a tener casilla. Sin esa guarda, la próxima spec copiada de una vieja la reintroduce.
- **`agenda/MEJORAS-METODO.md`**: M-35 pasa a `Hecha` y su planteo migra acá abajo.

### Qué quedó como estaba, a propósito
- La lista de post-generación de `AGENTS.md` sigue con `[ ]`: ésa sí es una lista por entrega.
- El nivel «Extendida» de §Profundidad de spec sigue diciendo «requisitos con `[ ]`». Ninguna spec lo usa, y qué hacer con ese nivel es M-37.

### Validación
`tools/check_docs.py` en verde (0 ERROR, 0 WARN). La guarda se probó inyectando una casilla en la spec de `CONSTITUTION.md` y dio ERROR. `ssot-collision`, que lee esas viñetas como texto, sigue sin avisos.

### Planteo migrado del backlog (2026-10-06)

#### M-35 — Las 195 casillas de `validacion` del registro nunca se marcaron y nada las mira

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

### Deuda abierta
- Siguen las de las dos entradas anteriores: M-21 agravado por `REFERENCIAS.md`, `backlog-metodo` no detecta un estado falso pero coherente, deuda del historial sin vista consolidada (en curso: va a los backlogs, decisión del usuario de hoy), rutas absolutas en prosa sin check, `EMOJI_SELLADOS` fuera del registro.

---

## La spec de la constitución deja de ubicar las convenciones en el registro (2026-10-06) — COMPLETADA

**Acción**: reconciliación de spec contra documento, aprobada por el usuario. Cierra la deuda que había quedado señalada en la entrada anterior.

### Qué cambió
- En `SPECS_REGISTRY.md`, la spec de `CONSTITUTION.md` decía en `excluye` que las convenciones de forma «viven en este registro». Desde la 0.2.3 viven en `CONVENCIONES.md`, que es lo que ya dice el preámbulo de la constitución. Ahora la spec apunta ahí y también nombra el léxico.

### Validación
`tools/check_docs.py` en verde (0 ERROR, 0 WARN). Ningún check podía verlo: `excluye` es prosa, y la divergencia duró desde el 2026-08-23 hasta que una lectura humana la encontró.

### Deuda abierta
- Las demás deudas de la entrada anterior siguen como estaban.

---

## M-40 y M-08 cerradas: el Principio VI suma convenciones y referencias, y el backlog de método se verifica contra sí mismo (2026-10-06) — COMPLETADA

**Acción**: enmienda constitucional PATCH (0.2.4 → 0.2.5), check nuevo y mantenimiento del backlog de método, aprobados por el usuario el mismo día tras una revisión de la forma de trabajo. El disparador fue el commit `3b9af33`, que cambió `CONVENCIONES.md` sin entrada de historial y pasó el gate: M-40 descrito el 2026-09-05 y ocurrido en la práctica.

### Decisiones del usuario
- **Qué es método**: `CONVENCIONES.md` y `REFERENCIAS.md` entran; `00-INDEX.md` queda afuera porque es navegación. La recomendación era sólo `CONVENCIONES.md`; el usuario sumó el catálogo de referencias.
- **Versión**: PATCH. El léxico vivía en `SPECS_REGISTRY.md` y `AGENTS.md`, que ya eran método, hasta que la 0.2.3 lo mudó sin actualizar la enumeración: se repara una omisión. Para `REFERENCIAS.md` el argumento no vale igual, porque nunca fue método; queda dicho y la versión queda como la decidió el usuario.
- **M-08**: se confirma como excepción permanente para documentos sellados la que ya aplicaba `EMOJI_SELLADOS` desde la entrada anterior.
- **Check**: de coherencia, no de antigüedad, para no agregar columnas a la tabla de estado.

### Qué cambió
- **`CONSTITUTION.md` 0.2.5**: el Principio VI enumera también «convenciones de léxico y forma» y «catálogo de referencias». El `Verificador:` del Principio II suma `ruta-externa`, que la entrada anterior había diferido a la próxima enmienda.
- **`tools/check_docs.py`**: `METODO_FILES` suma `CONVENCIONES.md` y `REFERENCIAS.md`, y el comentario explica por qué `00-INDEX.md` no está. Check nuevo `backlog-metodo` (WARN): todo ítem `Hecha` tiene fila en «Items cerrados», su puntero es una entrada real del historial y no conserva sección de detalle; todo ítem abierto tiene la suya; nada figura en «Items cerrados» sin estar `Hecha`.
- **Las otras copias de la enumeración** —`AGENTS.md` §Al cerrar una iteración paso 3, dos líneas de `SPECS_REGISTRY.md` y el encabezado de `agenda/MEJORAS-METODO.md`— dejan de repetirla y remiten al Principio VI. `AGENTS.md` pasa a nombrar tres checks de señal.
- **`agenda/MEJORAS-METODO.md`**: M-08 y M-40 pasan a `Hecha`, con sus planteos migrados acá abajo. El puntero de M-44 se corrigió, porque llevaba tildes y la entrada del historial no, y buscándolo literal no aparecía (lo encontró el check en su primera corrida). Los cerrados quedaron ordenados por ID, como dice el documento; M-44 y M-46 estaban arriba. M-21 y M-38 suman una nota fechada cada uno.

### Validación
`tools/check_docs.py` en verde (0 ERROR, 0 WARN). Cada rama de `backlog-metodo` se probó inyectando el caso y restaurando: ítem `Hecha` sin fila de cerrados y con detalle, ítem abierto sin detalle, puntero inexistente y fila de cerrados de un ítem no `Hecha`. Las cuatro avisaron. En la primera corrida aparecieron 19 falsos positivos por un error de parseo de `**Hecha**`, que se corrigió antes de la prueba. `metodo-historial` con `CONVENCIONES.md` staged se verifica con el commit de esta misma entrega.

### Planteos migrados del backlog (2026-10-06)

#### M-40 — La enumeración de «qué es método» del Principio VI deja afuera a `CONVENCIONES.md`, y el verificador la copia fiel

El Principio VI de `../CONSTITUTION.md` enumera qué cuenta como método: «protocolo del asistente, registro de specs, templates, esta constitución». Su verificador `metodo-historial` deriva de ahí su lista, y el comentario de `../tools/check_docs.py` lo dice sin rodeos: «La enumeracion sale literal del Principio VI [...] mas `tools/`, porque un check ES metodo».

`../CONVENCIONES.md` no está en esa enumeración. Y es el SSOT del léxico normativo (qué significa MUST, SHOULD, MAY en este repositorio), de la forma de los documentos, de los nombres de archivo y del formato de los mensajes de commit. `../AGENTS.md` le delega esas cuatro cosas por remisión explícita.

**Sonda corrida el 2026-09-05.** Se agregó una línea a `../CONVENCIONES.md`, se la dejó staged y se corrió `./tools/check_docs.py --staged`, que es el modo que invoca el gate de commit: **0 ERROR**, sin pedir entrada de historial. Un commit que redefine qué significa MUST en este repositorio pasa sin dejar rastro en `../historial/sdd.md`.

Lo que hace a este ítem distinto de M-31 —con el que comparte familia— es dónde está el defecto. En M-31 el check miraba mal. Acá **el check mira exactamente lo que le dijeron**: la lista es fiel, la fuente está incompleta. Arreglar `METODO_FILES` sin tocar el Principio VI deja la constitución diciendo una cosa y el verificador otra, que es justo la divergencia que la fidelidad de la lista evitaba.

Es una instancia de la clase 2 de `sdd-first:docs/PATRONES.md` («la lista duplicada que nada ata») en su variante menos visible: las dos enumeraciones **no** divergieron —una deriva de la otra— y el defecto viajó entero desde el original.

Qué hace falta, en este orden:

1. **Decidir si `CONVENCIONES.md` es método.** Es la pregunta real y es del usuario, no del backstop. Si lo es, el Principio VI se enmienda con su procedimiento completo (es cambio de constitución, no de check).
2. **Barrer el resto de la enumeración** con el mismo criterio antes de enmendar, para no pagar dos enmiendas: `../REFERENCIAS.md` y `../00-INDEX.md` son los otros dos candidatos, y ninguno de los dos es obvio. `agenda/` e `historial/` ya están razonados y quedan afuera.
3. **Recién entonces** actualizar `METODO_FILES`, que sigue siendo la copia fiel.

Prioridad alta y no media: mientras esté abierto, la única garantía mecánica del Principio VI tiene un agujero del tamaño del SSOT del léxico, y el repositorio no lo sabe.

#### M-08 — Emoticones en `PREREG-B7.md`

El documento viola la regla global «sin emoticones» pero está **pre-registrado y sellado**. Editarlo post-sello tiene implicancias metodológicas (Principio V). Decisión pendiente del usuario: corregir con enmienda fechada, o declarar excepción permanente para documentos sellados.

### Deuda abierta
- `backlog-metodo` mira la coherencia del estado, no si es verdadero: un ítem resuelto de hecho que sigue en `Propuesta` —como M-08 hasta hoy— pasa igual.
- M-21 se agrava: cada alta de `[Rxx]` pide ahora entrada de historial. Se cuenta antes de ajustar el check.
- La spec de `CONSTITUTION.md` en el registro sigue diciendo, en `excluye`, que las convenciones de forma «viven en este registro». Es una divergencia previa (desde la 0.2.3), señalada para que el usuario decida.
- Las 64 secciones «Deuda abierta» del historial siguen sin vista consolidada (mejora 2 de la misma revisión, no elegida en esta tanda).
- Siguen abiertas dos deudas de la entrada anterior: rutas absolutas en prosa sin check, y `EMOJI_SELLADOS` fuera del registro.

---

## `ruta-externa` mira la prosa y valida el repositorio citado; los sellados dejan de dar WARN de emoticones (2026-10-06) — COMPLETADA

**Acción**: cierre de tres deudas que dejó la entrada anterior, más una que venía de antes. La lista de repositorios hermanos y la regla de registro fechado entraron en `CONVENCIONES.md` en el commit previo, para que éste pasara el backstop solo.

### Qué cambió
- **`ruta-externa` en prosa**: además de backticks y links, marca las dos formas de ruta local que se delatan solas en texto corrido —`../` que sale de la raíz y la carpeta local de fuentes—.
- **`ruta-externa` valida `<repo>`**: una cita `<repo>:<ruta>` o `<repo>@<commit>:<ruta>` tiene que nombrar un repositorio de una URL de GitHub de `REFERENCIAS.md` o de la línea de hermanos de `CONVENCIONES.md`. Las dos listas se derivan de su fuente; el check no guarda copia. Si la línea de hermanos desaparece, falla cerrado. Para no confundir `path:line` o `campo:valor` con una cita, la ruta tiene que llevar barra o extensión.
- **`emoji` exceptúa documentos sellados**: `PREREG-B7.md` traía emoticones de antes del sello, y corregirlos sería reescribir un sellado (Principio V). La excepción es una lista a mano (`EMOJI_SELLADOS`), y por eso se vigila: una entrada cuyo archivo no existe, o que ya no tiene emoticones, da ERROR como excepción vencida.

### Validación
`tools/check_docs.py` en verde, ahora **sin WARN**. Cada rama se probó inyectando el caso y restaurando: ruta en prosa con `../` y con la carpeta local, prefijo mal escrito (`sdd-frist`), excepción vencida en `EMOJI_SELLADOS`, y línea de hermanos borrada. Las cuatro dieron ERROR; `path:line` y un hermano válido no.

### Deuda abierta
- En prosa, una ruta absoluta (`C:\...`, `/home/...`) o una relativa que no empiece con `../` no la ve el check.
- `EMOJI_SELLADOS` y el estado «sellado» no salen del registro: el registro no tiene un valor de `estado` para eso, y agregarlo sería cambiar su vocabulario.
- `ruta-externa` no figura en ningún `Verificador:` de `CONSTITUTION.md`; se difiere a la próxima enmienda.

---

## Las fuentes externas se citan por repositorio, no por copia local (2026-10-05) — COMPLETADA

**Acción**: cambio de método pedido por el usuario. Las fuentes externas no viven en este repositorio, y una cita que apunta a una copia en disco sólo la resuelve quien la escribió. En este clon, además, `fuentes-externas/` ya no tenía clones sino accesos directos de Windows, que tampoco resuelve nadie más (diagnóstico que B-09 ya había hecho el 2026-09-09 para su unidad de tratamiento).

### Qué cambió
- **`CONVENCIONES.md` §Citas a fuentes externas** (nueva): repositorio de código como `[Rxx]` + `<repo>:<ruta>`; el commit no se repite en la cita y se resuelve por el encabezado de la sección o del documento, después por lo que `REFERENCIAS.md` asigne a ese material, y por último por el último corte registrado; `<repo>@<commit>:<ruta>` cuando haga falta fijar otro. Papers y documentos, sólo `[Rxx]`. Fuente reservada, `[Rxx]` sin ruta.
- **`SPECS_REGISTRY.md`**: §Docs excluidos deja de declarar el material externo como clonado adentro; las validaciones que pedían «el clon vendored» pasan a pedir el repositorio de la fuente en el commit anclado.
- **`REFERENCIAS.md`**: sin rutas locales. Los papers declaran la versión leída de arXiv; [R39] cambia su reserva de vendorizado por una de anclaje y suma el corte `0e09037`. Se quitó el puntero de [R35] a un resumen que sólo existía en disco y nunca se versionó.
- **Unas 80 citas reescritas en 22 documentos**, fuera de `historial/` y `experimentos/`: rutas a los cuatro repositorios, a papers, al extracto de [R40], al testigo, al repositorio hermano `investigaIA` y al de datos de A-04. Las menciones en prosa a «clon vendored» en texto vigente pasan a describir la clase de evidencia sin suponer una copia interna.
- **`tools/check_docs.py`**: check nuevo `ruta-externa` (ERROR), que marca cualquier cita en backticks o link a la carpeta local de fuentes o a un `../` que sale de la raíz. Mira toda extensión y también directorios; `rutas` sólo mira `.md`. `AGENTS.md` lo suma a la enumeración de lo que cubre el backstop.

### Qué quedó como estaba, a propósito
- **`historial/` y `experimentos/`**: registro fechado, exento del check. Sus rutas describen lo que se hizo con la forma de su momento.
- **Bloques `[SDD-Check]` de entregas anteriores**: conservan su prosa («clon vendored»), por la misma razón. Sólo se reescribieron las rutas que tenían, porque el check no distingue bloques.
- **`software/DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md`, recomendación de vía híbrida**: propone mantener un clon como fuente de cosecha. Eso es una decisión sobre dónde leer, no una forma de citar, y no se toca.

### Validación
`tools/check_docs.py` en verde (0 ERROR; el WARN de emoticones de `PREREG-B7.md` es previo). El check se probó inyectando una ruta a la carpeta local y un link a un repositorio hermano: marcó las dos. Al estrenarse encontró cinco citas que el relevamiento manual no había visto —tres al repositorio de datos de A-04 y una ruta interna mal formada en `REFERENCIAS.md`, que `rutas` daba por ajena porque salía de la raíz—.

### Deuda abierta
- Una ruta escrita en prosa, sin backticks ni link, no la ve el check.
- `<repo>` no se valida contra `REFERENCIAS.md`: un prefijo mal escrito pasa.
- El historial y los experimentos conservan 13 líneas con rutas a la carpeta local, por diseño.

---

