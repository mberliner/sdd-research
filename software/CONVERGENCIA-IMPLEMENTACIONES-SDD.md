# Convergencia entre implementaciones de SDD

Fecha: 2026-08-02. Última incorporación: 2026-08-02 (OpenSpec).
Casos leídos: GitHub Spec Kit v0.8.13 / v0.12.11 [R10], Superpowers v6.2.0 [R37], OpenSpec v1.7.0 [R38], y el proyecto testigo `evaluador-flujo-intent` (artefactos reales al 2026-08-02, HEAD `6b0d0d7`, 70 commits, constitución v0.6.0).
Alcance: Línea B (software).

SSOT de qué elementos del método SDD son invariantes entre implementaciones independientes y cuáles no. La caracterización individual de cada caso vive en `ANALISIS-SPEC-KIT.md`, `ANALISIS-SUPERPOWERS.md` y `ANALISIS-OPENSPEC.md`; acá se lee a través de ellos.

---

## Por qué existe este documento

`ANALISIS-SPEC-KIT.md` venía afirmando que la convergencia entre Spec Kit y nuestro protocolo era alta y que eso reforzaba la hipótesis B6. Esa afirmación tenía dos problemas que este documento corrige.

El primero es de conteo. Los puntos eran dos, y el tercer actor que solía sumarse —el testigo— **deriva de este repositorio**, con sesgo de confirmación declarado en B-06. La incorporación de Superpowers agrega el primer punto que no nació ni de nuestro método ni del de Spec Kit.

El segundo es de archivo. El tema "qué es invariante entre implementaciones" estaba afirmado dentro de un documento cuyo alcance declarado es un solo framework. Su dueño natural es este documento.

**Encuadre que este documento NO hereda.** `COMPARATIVA-SPECKIT-VS-TESTIGO.md` caracteriza a Spec Kit como "el estándar de referencia" en una comparación pareada. Esa jerarquía es propia de aquella comparación y acá no se asume: los casos se leen todos con el mismo instrumento y ninguno es la vara de los otros.

---

## El instrumento y su procedencia

**Instrumento v1** — las ocho filas del mapeo de `ANALISIS-SPEC-KIT.md`, fijadas el **2026-05-24**, más de un año antes de que Superpowers y OpenSpec se incorporaran al análisis. Esto importa: con libertad para elegir qué comparar, la convergencia se fabrica. El instrumento es anterior a tres de los cuatro casos y no se le agregó ni se le redefinió ninguna fila después de leerlos.

Las divergencias se reportan con el mismo detalle que las convergencias. Un relevamiento que solo cuenta coincidencias no mide convergencia: la busca.

**Linajes, no implementaciones.** Para efectos de independencia hay **cuatro linajes**, no cinco fuentes: Spec Kit; Superpowers; OpenSpec; y la línea de este repositorio junto con el testigo, que no son independientes entre sí. Toda afirmación de invariancia de abajo se cuenta sobre linajes.

### Procedencia declarada de cada caso

| Caso | Procedencia | Cuenta como linaje |
|------|-------------|--------------------|
| Spec Kit [R10] | Origen de `[NEEDS CLARIFICATION]` y del coverage mapping; no deriva de ningún otro caso del corpus | Sí |
| Superpowers [R37] | No cita, forkea ni deriva de los demás; ausentes los marcadores de difusión conocidos | Sí |
| OpenSpec [R38] | Primer commit 2025-08-05, dieciséis días **anterior** al primer commit del repositorio de Spec Kit (2025-08-21); menciona a Spec Kit y a Kiro solo para diferenciarse comercialmente; ausentes los tres marcadores de difusión conocidos. Detalle y límites en `ANALISIS-OPENSPEC.md` | Sí, respecto de Spec Kit |
| Testigo + este repo | El testigo deriva de este repositorio, con sesgo de confirmación declarado en B-06 | Sí, como un solo linaje |
| sdd-first [R39] | Mismo autor; generaliza el tooling del testigo y arrastra vocabulario nacido acá (`[SDD-Check]`, el par `hibrido`/`casero` de B-07, la forma de principio de `../CONSTITUTION.md`) más la difusión desde Spec Kit ya declarada (`analyze`, `clarify`) | **No** como linaje — pero **sí** se lee dentro de la columna del linaje desde 2026-09-05; ver «Qué artefacto representa a nuestro linaje». Detalle en `ANALISIS-SDD-FIRST.md` |

### Qué artefacto representa a nuestro linaje (2026-09-05)

La columna «Testigo / este repo» nunca fue un artefacto sino un linaje, y el linaje produjo un tercero: **sdd-first es la consecuencia de esta investigación llevada a código**, no una fuente ajena. Dos hechos obligan a revisar a quién se lee en esa columna:

- **El testigo quedó dormido.** Su último commit es del **2026-08-02** (`04d921d`, 71 commits, 18 specs). El primer commit de sdd-first es del **2026-08-01**. El trabajo del linaje migró, y leer sólo al testigo describe una posición que el linaje ya no está ejerciendo.
- **sdd-first es el único artefacto del linaje con el método ejecutado por código de punta a punta**, y es público y vendorizado, mientras que el testigo es privado.

Entra, entonces, a la columna. Con tres reglas, porque incorporarlo sin ellas fabrica convergencia:

1. **No cambia el conteo.** Siguen siendo **cuatro linajes**. sdd-first no agrega un punto de comparación: refina la descripción de uno que ya estaba.
2. **Cada celda declara de qué artefacto del linaje sale** —testigo, este repositorio, o sdd-first—. Sin eso, quien escribe puede elegir en cada fila el artefacto que más se parece a los otros casos, y eso no es leer: es seleccionar.
3. **Lo que sdd-first declara adoptado de otro caso del corpus MUST NOT sostener un veredicto de convergencia.** Sus playbooks dicen textualmente «Adaptado de `/speckit.analyze`» y «Adaptado de `/speckit.clarify`» (`../fuentes-externas/sdd-first/docs/playbooks/analyze.md` y `clarify.md`, línea 4). Eso es difusión desde Spec Kit, y en las filas 3 y 4 cuenta como tal, igual que ya contaba el marcador heredado por el testigo.

El testigo **no se retira**: es el artefacto que se leyó cuando el instrumento se fijó, y borrarlo reescribiría la base de las lecturas anteriores. Se lo mantiene con su fecha de última actividad declarada.

**El filtro ejercido sobre un caso que no pasa (2026-08-15).** sdd-first es el primer caso al que la regla 1 se le aplica y lo rechaza. Se lo registra acá, y no en silencio, porque el corolario de esa regla —la mayoría de los métodos SDD nuevos no van a sumar linaje— solo es verificable si los rechazos quedan escritos junto a las aceptaciones. El conteo sigue siendo de cuatro linajes y ningún veredicto por fila cambia.

**Límite del filtro.** La independencia de OpenSpec está establecida frente a Spec Kit por fechas verificables, no frente a Kiro, anunciado el 2025-07-14 y ausente del corpus. La notación `WHEN/THEN` compartida desciende de Gherkin [R07], ancestro común anterior a los cuatro, y por eso no cuenta como derivación entre casos. Mientras Kiro no se lea, la cuarta columna se sostiene sobre una independencia parcialmente verificada, y toda afirmación de invariancia que dependa **solo** de sumar OpenSpec MUST leerse con esa reserva.

---

## Veredicto por fila

| # | Concepto | Spec Kit | Superpowers | OpenSpec | Testigo / este repo | Veredicto |
|---|----------|----------|-------------|----------|---------------------|-----------|
| 1 | Fuente de autoridad no-negociable | `constitution.md` + Constitution Check como gate | Precedencia declarada (usuario > skills > default); desde v6.3.0 la **spec es autoridad vinculante** para resolver conflictos del plan («the spec is the binding authority, the plan is its argument»), pero sigue sin constitución ni gate de principios | `openspec/config.yaml` (`context` + `rules`), servido por el CLI; orden de resolución declarado; sin constitución ni gate de principios | *testigo*: `CONSTITUTION.md` v0.6.0 + `check_constitution.py`; *acá*: `CONSTITUTION.md` v0.1.0; *sdd-first*: constitución **generada** desde `.sdd/config.yaml` y check que verifica que cada enforcement declarado exista | **Parcial** |
| 2 | Lenguaje normativo | `MUST` en FR y plantillas [R04] | `MUST`, `HARD-GATE`, "Iron Law"; sin citar RFC 2119 | `SHALL` en requisitos [R03], `MUST` en skills; sin citar RFC 2119 | `MUST` en 12 de 17 specs del testigo; `MUST`/`SHOULD`/`MAY` acá [R04] | **Converge** |
| 3 | Manejo de ambigüedad | `[NEEDS CLARIFICATION]` + `/speckit.clarify` | Conversacional para el diseño, pero desde v6.3.0 **decide y registra** en ejecución: «Rulings, not stalls», con la forma `Ruling: <qué> — <por qué> — <cuánto cuesta si está mal>`; sólo lo destructivo frena. Sin marcador | Preguntar solo si el contexto es críticamente confuso; instruye preferir la decisión razonable para no frenar. Sin marcador | *testigo*: `[NEEDS CLARIFICATION]` en 7 specs + playbook `clarify`; *acá*: adoptado, y Principio VII manda preguntar y detener. **Difusión desde Spec Kit, no acuerdo** | **Diverge — en dos posiciones, no en cuatro** |
| 4 | Validación de consistencia | `/speckit.analyze`, read-only cross-artefacto | `verification-before-completion` + revisión por subagente contra la spec | `openspec validate [--strict]` (determinista) + `/opsx:verify` por juicio contra el código, con severidades | `check_traceability.py` (determinista) + `[SDD-Check]`; acá `check_docs.py` | **Converge** |
| 5 | Trazabilidad requisito a verificador | Coverage mapping FR/SC a tareas | Ledger de tareas y revisión por tarea; sin coverage mapping | Requisito a código y escenario a test, por búsqueda heurística en el momento; sin mapeo mantenido | Coverage mapping FR a test, verificado por script en specs `active` | **Parcial** |
| 6 | Circuito de aprendizaje | Declarado ("bidirectional feedback"), no instrumentado; `spec-persistence.md` nombra tres modelos de mutación y declara que **no impone ninguno** | Instrumentado sobre los **documentos de método**, con medición conductual | Instrumentado sobre el **contrato** y automatizado: archivar fusiona el delta en la spec vigente | Sobre el **contrato**: `Deuda arrastrada` (49 ocurrencias en el historial del testigo), Principio III acá. Y desde 2026-08-16 también sobre el **método**: `docs/PATRONES.md` de sdd-first destila clases de defecto de sus post-mortems | **Diverge en el objeto** |
| 7 | Registro de specs | Carpeta por feature `specs/[###-feature]/` | Archivos fechados, sin registro ni estado | Central por capacidad, consultable por CLI; estado implícito en la ubicación, sin campo `estado` ni nivel SSOT. Desde v1.12.0, *stores* en beta: el registro **puede vivir en un repositorio propio** compartido por varios repos de código | *testigo* y *acá*: registro central por capacidad/documento, con `estado` y `ssot_level`; *sdd-first*: registro propio más `SPEC-000` | **Diverge** |
| 8 | Personalización | Presets y extensions, y desde el 1.0 (2026-08-21) un **ecosistema**: bundler, catálogos de comunidad con modelo de confianza declarado, workflows y events | Plugins independientes + adaptadores por harness (14 harnesses) | *Schemas* forkeables que redefinen artefactos y dependencias + adaptadores para 62 herramientas | *acá*: `ssot_level` y niveles de profundidad; *sdd-first*: `.sdd/config.yaml` con adaptador de lenguaje y modo `none`, más generación de adaptadores por asistente | **Converge** |

### Qué cambió al incorporar el cuarto caso

El instrumento no se tocó; dos veredictos sí, y conviene que el cambio quede firmado en vez de aparecer reescrito en silencio.

- **Fila 3 pasó de «converge el principio, diverge el instrumento» a Diverge.** La lectura anterior sostenía que los tres casos compartían el principio "no asumir, preguntar" y solo diferían en cómo. OpenSpec no comparte el principio: instruye explícitamente preferir la decisión razonable para no frenar. Con dos linajes independientes de cuatro apartándose —uno del instrumento, otro del principio— lo que queda no es convergencia.
- **Fila 8 pasó de Parcial a Converge.** Con tres casos, la adaptación por capa externa era un parecido vago entre mecanismos dispares. El cuarto la ejerce en la forma más fuerte del corpus —*schemas* forkeables que redefinen el conjunto de artefactos y sus dependencias— y muestra que los cuatro no solo prevén extensión, sino que la ubican en el mismo lugar: fuera del núcleo, sin bifurcarlo.

### Qué cambió al re-consultar los cuatro casos (2026-09-05)

Las cuatro fuentes se re-consultaron en versiones nuevas (`../REFERENCIAS.md`, estado de cada clon). **El instrumento sigue en v1 y no se le agregó ni redefinió ninguna fila.** Cambiaron celdas, cambió la forma de una divergencia y se falsificó un invariante débil. Firmado, como el cambio anterior.

- **Ningún veredicto se dio vuelta.** Los ocho se sostienen. Lo que cambió es qué dice cada caso adentro de su celda.
- **La fila 3 dejó de ser una divergencia de cuatro respuestas y pasó a ser un empate de dos contra dos.** Superpowers v6.3.0 incorporó «Rulings, not stalls»: ante un conflicto no catastrófico decide contra la spec, registra el fallo y sigue. Es la posición que OpenSpec ya sostenía. Del otro lado quedan el marcador y la pregunta: Spec Kit y nosotros.

  Y acá hay algo incómodo que conviene decir en vez de dejarlo implícito: **de esos dos, uno adoptó la práctica del otro.** El marcador tiene un solo origen independiente, así que la posición «marcar y preguntar» está sostenida por **un linaje independiente**, y la posición «decidir y registrar» por **dos**. Sobre este eje, la posición de este repositorio es la minoritaria entre linajes independientes, y su única compañía es la fuente de la que la copió. No es un argumento para cambiar el Principio VII —la decisión es constitucional y los diseños responden a riesgos distintos (`../software/ANALISIS-SUPERPOWERS.md` C7)—, pero sí un dato que el documento debía registrar y no tenía.

- **El invariante débil de la fila 7 queda falsificado por el caso que lo sostenía.** Este documento afirmaba que lo que sobrevivía a cuatro registros incompatibles era que «las specs son archivos versionados que viven junto al artefacto que gobiernan». Los *stores* de OpenSpec v1.12.0 (beta) sacan el registro a un repositorio propio compartido por varios repos de código: las specs siguen versionadas, y ya no viven junto al artefacto. El invariante se reduce a **«las specs son archivos versionados»**, que es casi nada. Se corrige abajo.
- **La fila 6 gana un dato sobre nuestro propio linaje.** `docs/PATRONES.md` de sdd-first destila clases de defecto a partir de post-mortems: eso es circuito de aprendizaje corriendo sobre el **método**, que es la casilla de Superpowers. Nuestro linaje pasa a ocupar las dos casillas del tercer eje, no una.
- **Las filas 1, 4 y 8 se refuerzan sin moverse.** Superpowers suma un artefacto de autoridad para conflictos de plan; OpenSpec suma severidades y detección de placeholder a su validación; Spec Kit convierte la personalización en un ecosistema con modelo de confianza declarado.

---

## Qué resulta invariante y qué no

### Invariante sobre los cuatro linajes

- **Lenguaje normativo explícito** (fila 2). Los cuatro lo adoptan; dos citan RFC 2119 [R04] y uno usa el registro de ISO/IEC/IEEE 29148 [R03], así que lo invariante es la práctica, no la norma que la respalda.
- **Un mecanismo de consistencia antes de cerrar** (fila 4). Los cuatro tienen uno y los cuatro lo ubican en el mismo punto del ciclo —antes de declarar terminado—, con mecanismos que no se parecen: análisis read-only cross-artefacto, gate conductual con evidencia fresca, validación determinista más verificación por juicio contra el código, y verificación determinista de estructura y cobertura. Es la convergencia más fuerte del relevamiento, precisamente por eso. Dos de los cuatro llegaron además a la **misma arquitectura de dos capas** —una determinista sobre estructura, otra por juicio sobre contenido— sin contacto entre sí.
- **Precedencia explícita de instrucciones** (fila 1, forma débil). Los cuatro declaran un orden de autoridad, incluido el que menos artefacto tiene. Lo que **no** es invariante es quién la encarna: dos la ponen en un artefacto del proyecto, uno en el humano de la sesión, uno en un archivo de configuración que sirve una herramienta.
- **Extensión sin tocar el núcleo** (fila 8). Los cuatro la prevén y los cuatro la ubican fuera del núcleo.

### No invariante, y un caso de difusión mal leída

- **El marcador de ambigüedad no es convergencia: es difusión.** `[NEEDS CLARIFICATION]` aparece en tres de las cinco fuentes, pero tiene **un solo origen independiente**: lo inventó Spec Kit, este repositorio lo adoptó deliberadamente (`ANALISIS-SPEC-KIT.md`, C2) y el testigo lo heredó de acá. Los dos linajes verdaderamente independientes que quedan —Superpowers y OpenSpec— **no lo tienen**. El cuarto caso además desarma la versión débil del argumento: no solo no usa el instrumento, tampoco sostiene el principio. Contar esas tres apariciones como convergencia independiente habría sido un error de conteo.
- **El coverage mapping tiene el mismo problema** (fila 5). Nuestro campo `Cobertura` fue adoptado explícitamente de Spec Kit (C1). De los dos linajes independientes restantes, uno no lo implementa y el otro reconstruye el vínculo por búsqueda en el momento de verificar, sin mantener mapeo alguno.
- **El registro de specs diverge de plano** (fila 7): cuatro soluciones incompatibles —carpeta por feature, archivos fechados, central por capacidad con estado implícito, central por documento con `estado` y `ssot_level`— para el mismo problema. El invariante que queda es **más débil todavía desde 2026-09-05**: las specs son archivos versionados, y nada más. La formulación anterior —«que viven junto al artefacto que gobiernan»— la falsificaron los *stores* de OpenSpec, que sacan el registro a un repositorio propio compartido por varios repos de código. Queda como advertencia de método: un invariante sostenido por los cuatro casos puede caer cuando uno de ellos publica una variante. Lo que el cuarto caso sí agrega es un dato menor: **dos de cuatro mantienen inventario central consultable**, así que la carpeta-por-feature no es la solución dominante.

---

## Dimensiones observadas fuera del instrumento v1

Registradas por la regla 2 de la sección «Cómo se incorpora un caso nuevo»: se anotan, no se puntúan, y no abren fila.

- **Cómo llega el método al agente** (observada al incorporar OpenSpec, 2026-08-02). Las ocho filas describen qué dice el método y ninguna describe su vía de entrega. Tres casos y este repositorio usan documentos que el agente lee y sostiene en contexto; OpenSpec sirve fragmentos bajo demanda desde un CLI (`ANALISIS-OPENSPEC.md`, C2). La diferencia cambia el modo de falla del cumplimiento —no aplicar lo leído, contra no invocar el comando— y el segundo es observable sin juzgar prosa. **Sin veredicto**: con un solo caso del lado servido no hay nada que comparar, y fabricar una fila ahora garantizaría que ese caso destaque en ella. Si un quinto caso independiente la ejerce, es la primera candidata a instrumento v2.

- **Dónde vive el método respecto del artefacto que gobierna** (observada al re-consultar OpenSpec, 2026-09-05). Los cuatro casos alojaban el método adentro del repositorio del artefacto. Los *stores* de OpenSpec (beta) lo sacan a un repositorio propio compartido por varios repos de código. Es la dimensión que falsificó el invariante débil de la fila 7. **Sin veredicto**: un solo caso la ejerce, y en beta. Este repositorio tiene el problema en la forma inversa —un repositorio de método cuyas piezas se ejecutan afuera— y sin mecanismo (`ANALISIS-OPENSPEC.md`, C6).

- **La ceremonia escala con el tamaño del trabajo** (observada al re-consultar Superpowers y Spec Kit, 2026-09-05). Ninguna de las ocho filas pregunta si el método produce el mismo artefacto para una tarea chica que para una grande, y **tres de los cuatro casos ya tienen respuesta**:
  - *Superpowers* clasifica cada pedido en spike / bounded / architectural y sólo el último escribe spec y plan; la clasificación se anuncia en voz alta para que el humano la anule, el trinquete es de una sola vía, y la compuerta de aprobación **no** escala.
  - *Spec Kit* tiene una escalera de cuatro opciones para features que no entran en un ciclo (`complex-features.md`), ordenada de más barata a más cara, que termina en el *spec of specs*.
  - *Nuestro linaje* declara tres niveles de profundidad de spec en `../SPECS_REGISTRY.md` y **no usa el más alto en ninguna de sus entradas** (`../agenda/MEJORAS-METODO.md` M-37): la escala existe declarada y no opera.
  - *OpenSpec* no expone un mecanismo de escala en lo leído.

  **Sin veredicto**, por la regla 2. Pero es hoy la **candidata más fuerte a instrumento v2**, por encima de «cómo llega el método al agente»: tres casos la ejercen contra uno, y los tres llegaron a mecanismos distintos, que es la forma que tiene una dimensión de ser informativa. Decidirlo es trabajo aparte y caro: abre v2 y obliga a re-correr los cuatro casos (regla 3).

### La divergencia más informativa: el objeto del circuito de aprendizaje

`COMPARATIVA-SPECKIT-VS-TESTIGO.md` cerró su síntesis sobre dos ejes ortogonales, regenerabilidad y adaptatividad. Superpowers no entra limpio en ese marco: es débil en regenerabilidad —no regenera nada— y su circuito de adaptatividad **no corre sobre las specs del proyecto sino sobre sus propios documentos de método**, medido por conducta de agentes en sesiones frescas.

Eso sugiere un tercer eje que los dos existentes no capturan: **sobre qué objeto corre el feedback**. Un SDD puede instrumentar el aprendizaje sobre el contrato (las specs se revisan tras la ejecución), sobre el método (el protocolo se revisa según cómo se comporta quien lo lee), o sobre ninguno. Los cuatro linajes se reparten así: el testigo y este repositorio, el contrato; OpenSpec, el contrato también, pero automatizado —archivar fusiona el delta aprobado en la spec vigente, sin que nadie tenga que acordarse—; Superpowers, el método; Spec Kit declara el circuito y no lo instrumenta en ninguno de los dos.

El cuarto caso aporta dos cosas al eje. La primera es que la casilla "contrato" deja de ser exclusiva de nuestro linaje, lo que la vuelve un punto de convergencia real y no una particularidad nuestra. La segunda es más incómoda: **somos los únicos de esa casilla que lo hacemos a mano**. La regla de propagación del Principio III y el campo `Deuda arrastrada` dependen de que una persona los ejecute; OpenSpec llegó a la misma regla y la puso en un comando. Que la parte mecánica sea automatizable está demostrado por un tercero.

**Corrección del 2026-09-05: el reparto en casillas exclusivas no se sostiene.** `docs/PATRONES.md` de sdd-first destila clases de defecto recurrentes a partir de post-mortems, y eso es aprendizaje sobre el **método**, no sobre el contrato. Nuestro linaje ocupa entonces las dos casillas, no una. El eje sigue siendo útil —distingue objetos de feedback que no son el mismo— pero deja de ser una partición: un linaje puede correr los dos circuitos, y el nuestro los corre. Lo que queda como dato es que el circuito sobre el método nació en el artefacto más nuevo del linaje y **no está en el protocolo de este repositorio**, donde nadie destila (`ANALISIS-SDD-FIRST.md`, C7).

Este documento propone el eje, no lo cierra: se apoya en cuatro casos y la asignación de casillas sale de leer artefactos, no de medir.

---

## Qué se puede y qué no se puede inferir de esto

**Se puede inferir consenso de diseño.** Cuatro linajes independientes que llegan a lenguaje normativo, a un gate de consistencia previo al cierre y a la extensión por capa externa, con mecanismos distintos, indican que esos elementos resuelven un problema real y recurrente del trabajo asistido por IA. El cuarto caso sube el conteo de tres a cuatro, con la reserva de procedencia declarada arriba, y ninguno de los tres invariantes se apoya solo en él.

**No se puede inferir eficacia, y este proyecto tiene evidencia propia de que la distinción no es teórica.** Que varios equipos coincidan en una práctica muestra acuerdo, no que la práctica funcione — el mismo criterio que aplicamos a fuentes secundarias como [R28] y [R30]. El cuarto caso lo ilustra por el lado más crudo: OpenSpec **no reporta ninguna medición propia**, así que suma un voto de diseño y cero evidencia. Y hay un caso medido en casa: B-07 puso a prueba justamente el elemento donde la anatomía de Spec Kit debía ganar —la regenerabilidad— y cerró **sin ventaja del formato híbrido** (`../experimentos/b07-formato-hibrido/RESULTADO-EXPERIMENTO-B7.md`). La convergencia de diseño y el desempeño medido están desacoplados.

**Consecuencia para B6.** La afirmación previa —que la convergencia refuerza la hipótesis B6— MUST leerse en forma más chica. B6 hipotetiza que los tests ligados a specs *detectan divergencia entre contrato y realidad antes de producción*: eso es una afirmación causal sobre un mecanismo, y ninguna cantidad de coincidencia entre frameworks la sostiene. Lo que la convergencia sí respalda es algo más modesto y aun así útil: que el problema que B6 aborda es reconocido de forma independiente por quienes construyen estas herramientas.

---

## Cómo se incorpora un caso nuevo

Este documento está hecho para crecer, y el modo de hacerlo crecer es donde se pierde la honestidad si no está escrito. Tres reglas.

### 1. Primero la procedencia, después la lectura

MUST — todo caso nuevo declara su procedencia antes de contarse. La pregunta no es qué tiene, sino **si lo inventó o lo heredó**: ¿cita, forkea o deriva de alguno de los casos ya presentes?

Un método que adopta la anatomía de otro **no agrega un linaje, agrega una copia**, y sumarlo como punto de convergencia repite el error que este documento corrigió en la fila 3. Puede tener interés por otros motivos —madurez, adopción, ergonomía— y entonces su lugar es `../comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md` o un análisis individual propio, no una columna acá.

El corolario incomoda y por eso conviene tenerlo escrito: **la mayoría de los métodos SDD nuevos no van a sumar linaje**, porque el campo converge por difusión desde pocos orígenes. Un documento de convergencia que crece sin filtro mide popularidad, no invariancia.

### 2. Las dimensiones fuera del instrumento se registran, no se puntúan

Si un caso nuevo hace algo que ninguna de las ocho filas contempla, MUST NOT agregarse una fila para alojarlo: una fila fabricada a medida del caso que la motiva garantiza que ese caso destaque en ella. La observación se registra fuera de la tabla, visible y sin veredicto, hasta que se decida si merece instrumento nuevo.

### 3. Ampliar el instrumento abre versión, y obliga a re-correr todo

MUST — si una dimensión registrada demuestra importar, se fija un **instrumento v2** fechado y se re-corren **todos** los casos contra él, declarando la versión en cada lectura. MUST NOT ampliarse la v1 en caliente: leer unos casos con ocho filas y otros con nueve produce una tabla que no compara nada.

Es el mismo régimen que el proyecto aplica a los experimentos sellados —enmienda fechada y motivada, nunca edición silenciosa (Principio V)—, trasladado a un instrumento de análisis. La diferencia con un experimento es que acá el costo de re-correr es leer documentos, no producir datos: es caro en atención, barato en todo lo demás.

---

[SDD-Check] — re-consulta de los cuatro casos 2026-09-05
- Spec leida: SI (spec registrada en `../SPECS_REGISTRY.md`; sin cambio de `incluye`/`excluye`: la re-lectura de casos y el registro de dimensiones fuera del instrumento ya estaban previstos)
- Incluye/Excluye verificado: SI — no se reproduce la caracterizacion individual de ningun caso (cada celda remite a su `ANALISIS-*.md`), no se toman decisiones de adopcion, y la orientacion practica de cada framework **no entra acá**: es documento aparte, pendiente
- Validaciones aplicadas: **el instrumento sigue en v1 y no se le agrego ni redefinio ninguna fila**, pese a que dos dimensiones nuevas quedaron registradas fuera de la tabla (regla 2); los cambios de celda estan firmados y motivados en «Que cambio al re-consultar los cuatro casos», no reescritos en silencio; la incorporacion de sdd-first a la columna del linaje **no altera el conteo de cuatro linajes** y viene con tres reglas que impiden seleccionar el artefacto mas favorable por fila; lo que sdd-first declara adoptado de Spec Kit se marca como difusion y no sostiene ningun veredicto, con la cita verificada en fuente (`docs/playbooks/analyze.md` y `clarify.md`, linea 4); la fecha de ultima actividad del testigo se verifico en su repositorio (`04d921d`, 2026-08-02); divergencias reportadas con el mismo detalle que las convergencias, incluida la que deja a este repositorio en la posicion minoritaria; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: este documento
- Derivados a revisar: `software/COMPARATIVA-SPECKIT-VS-TESTIGO.md` — su marco de dos ejes ya tenia puntero por el tercer eje, y ahora ese tercer eje deja de ser una particion; señalado, sin modificar. `agenda/MEJORAS-METODO.md` M-37 (la dimension «la ceremonia escala» le da contexto a la tabla de profundidad que no opera) y M-42 (la fila 3 le agrega que la posicion de este repositorio es minoritaria entre linajes independientes) — señalados, sin modificar
- Cobertura: completa para la re-consulta — las ocho filas se releyeron contra las cuatro versiones nuevas, cada cambio de celda esta declarado, las dos dimensiones nuevas quedan registradas sin veredicto y el invariante falsificado se corrigio donde estaba escrito. Queda **sin cubrir por decision**: si «la ceremonia escala» merece instrumento v2, que es trabajo aparte
- Deuda arrastrada: la de la entrega anterior sigue entera (Kiro sin leer, Tessl sin filtro de procedencia, corpus observacional de OpenSpec sin dar de alta, `LINEAS-INVESTIGACION.md` B6 sin reescribir, M-13). Se agregan tres: **«la ceremonia escala con el tamaño del trabajo» es hoy la candidata mas fuerte a instrumento v2 y no esta decidida**; **«donde vive el metodo respecto del artefacto» queda sin veredicto con un solo caso y en beta**; y **el testigo esta dormido desde el 2026-08-02**, asi que su celda describe una posicion congelada y eso MUST releerse si vuelve a moverse
- Riesgos/reservas: los cuatro casos se caracterizan desde clones vendored, sin correr ninguno; ninguna fuente reporta medicion sobre ninguna de las ocho filas; la independencia de OpenSpec sigue verificada solo frente a Spec Kit; y la incorporacion de sdd-first mejora la descripcion de nuestro linaje al costo de leer un artefacto **posterior** a las lecturas de los otros tres, lo que MUST tenerse presente: es el unico caso del corpus que pudo escribirse sabiendo lo que hacian los demas

---

## Bloque de entrega anterior

Registro datado: cierra la incorporacion del cuarto caso (2026-08-02) y vale para el cuerpo que el documento tenia entonces.

[SDD-Check]
- Spec leida: SI (spec registrada en `../SPECS_REGISTRY.md` para este doc; alta en la tabla SSOT)
- Incluye/Excluye verificado: SI - no reproduce la caracterizacion individual de ningun caso (referencia a `ANALISIS-SPEC-KIT.md`, `ANALISIS-SUPERPOWERS.md` y `ANALISIS-OPENSPEC.md`), no reproduce la comparacion pareada de cinco dimensiones, y no toma decisiones de adopcion
- Validaciones aplicadas: instrumento declarado con su version y fecha de origen (v1, 2026-05-24), anterior a tres de los cuatro casos; ninguna fila agregada ni redefinida al incorporar el cuarto caso, y la dimension que no cubre queda registrada sin veredicto; los dos veredictos que cambiaron estan firmados y motivados en «Que cambio al incorporar el cuarto caso», no reescritos en silencio; cada caso declara su procedencia antes de contarse, con los limites del filtro explicitos; divergencias reportadas con el mismo detalle que las convergencias; caracterizacion del testigo derivada de sus artefactos reales al HEAD `6b0d0d7` (17 specs, 12 con `MUST`, 7 con `[NEEDS CLARIFICATION]`, 49 ocurrencias de `Deuda arrastrada`, `check_traceability.py`), no copiada de la comparativa; encuadre «estandar de referencia» declarado como no heredado; refs internas verificadas; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: este documento (incorporacion del cuarto caso, 2026-08-02); `software/ANALISIS-SPEC-KIT.md` no vuelve a sostener la afirmacion de convergencia y la referencia
- Derivados a revisar: `software/ANALISIS-SPEC-KIT.md` (afirmacion de convergencia e inferencia hacia B6, ya corregidas; el cuarto caso no las reabre); `software/COMPARATIVA-SPECKIT-VS-TESTIGO.md` (su marco de dos ejes ya tenia puntero por el tercer caso; el cuarto refuerza el mismo señalamiento y no obliga a reescribir su sintesis); `agenda/MEJORAS-METODO.md` M-04 (la entrega bajo demanda replantea el problema de contexto que M-04 administra) y M-03 (la dependencia dura de CLI de OpenSpec es el contraejemplo de la portabilidad que M-03 defiende) — señalados, sin modificar
- Cobertura: completa - las ocho filas tienen veredicto sobre los cuatro casos, cada afirmacion de invariancia declara sobre cuantos linajes se cuenta y ninguna se apoya solo en el caso nuevo, y el procedimiento de incorporacion se ejercito en sus tres reglas: filtro de procedencia aplicado con evidencia de fechas, dimension nueva registrada fuera de la tabla, instrumento no ampliado
- Deuda arrastrada: la independencia de OpenSpec esta verificada frente a Spec Kit pero no frente a Kiro, que sigue sin leerse; Kiro y Tessl, nombrados en [R20], siguen sin pasar por el filtro de procedencia y sin alta en ningun backlog; la dimension «como llega el metodo al agente» queda registrada sin veredicto y sin decision sobre instrumento v2; el corpus observacional de OpenSpec (83 cambios archivados) no esta dado de alta; el tercer eje queda propuesto y sin cerrar, apoyado en lectura de artefactos, no en medicion; `software/LINEAS-INVESTIGACION.md` B6 conserva su enunciado original, que este documento acota pero no reescribe; la inconsistencia de `deriva_de` detectada en el registro es `M-13`, ajena a este doc
- Riesgos/reservas: tres de los cuatro casos se caracterizan desde snapshots vendored, no desde correr los sistemas; el cuarto es un repositorio propio, con el sesgo de confirmacion de B-06 ya declarado; el conteo por linajes reduce a cuatro puntos lo que a primera vista parecian cinco, y uno de esos cuatro tiene independencia solo parcialmente verificada; dos de las cuatro fuentes externas tienen interes comercial y una de ellas no reporta ninguna medicion propia
