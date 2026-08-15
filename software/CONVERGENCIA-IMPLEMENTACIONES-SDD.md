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
| sdd-first [R39] | Mismo autor; generaliza el tooling del testigo y arrastra vocabulario nacido acá (`[SDD-Check]`, el par `hibrido`/`casero` de B-07, la forma de principio de `../CONSTITUTION.md`) más la difusión desde Spec Kit ya declarada (`analyze`, `clarify`) | **No** — cae dentro del linaje «Testigo + este repo». Detalle en `ANALISIS-SDD-FIRST.md` |

**El filtro ejercido sobre un caso que no pasa (2026-08-15).** sdd-first es el primer caso al que la regla 1 se le aplica y lo rechaza. Se lo registra acá, y no en silencio, porque el corolario de esa regla —la mayoría de los métodos SDD nuevos no van a sumar linaje— solo es verificable si los rechazos quedan escritos junto a las aceptaciones. El conteo sigue siendo de cuatro linajes y ningún veredicto por fila cambia.

**Límite del filtro.** La independencia de OpenSpec está establecida frente a Spec Kit por fechas verificables, no frente a Kiro, anunciado el 2025-07-14 y ausente del corpus. La notación `WHEN/THEN` compartida desciende de Gherkin [R07], ancestro común anterior a los cuatro, y por eso no cuenta como derivación entre casos. Mientras Kiro no se lea, la cuarta columna se sostiene sobre una independencia parcialmente verificada, y toda afirmación de invariancia que dependa **solo** de sumar OpenSpec MUST leerse con esa reserva.

---

## Veredicto por fila

| # | Concepto | Spec Kit | Superpowers | OpenSpec | Testigo / este repo | Veredicto |
|---|----------|----------|-------------|----------|---------------------|-----------|
| 1 | Fuente de autoridad no-negociable | `constitution.md` + Constitution Check como gate | Precedencia declarada (usuario > skills > default); autoridad en el humano, sin artefacto | `openspec/config.yaml` (`context` + `rules`), servido por el CLI; orden de resolución declarado; sin constitución ni gate de principios | `CONSTITUTION.md` v0.6.0 + `check_constitution.py`; acá `CONSTITUTION.md` v0.1.0 | **Parcial** |
| 2 | Lenguaje normativo | `MUST` en FR y plantillas [R04] | `MUST`, `HARD-GATE`, "Iron Law"; sin citar RFC 2119 | `SHALL` en requisitos [R03], `MUST` en skills; sin citar RFC 2119 | `MUST` en 12 de 17 specs del testigo; `MUST`/`SHOULD`/`MAY` acá [R04] | **Converge** |
| 3 | Manejo de ambigüedad | `[NEEDS CLARIFICATION]` + `/speckit.clarify` | Conversacional: una pregunta por mensaje, gate de aprobación; sin marcador | Preguntar solo si el contexto es críticamente confuso; instruye preferir la decisión razonable para no frenar. Sin marcador | `[NEEDS CLARIFICATION]` en 7 specs del testigo + playbook `clarify`; adoptado acá | **Diverge** |
| 4 | Validación de consistencia | `/speckit.analyze`, read-only cross-artefacto | `verification-before-completion` + revisión por subagente contra la spec | `openspec validate [--strict]` (determinista) + `/opsx:verify` por juicio contra el código, con severidades | `check_traceability.py` (determinista) + `[SDD-Check]`; acá `check_docs.py` | **Converge** |
| 5 | Trazabilidad requisito a verificador | Coverage mapping FR/SC a tareas | Ledger de tareas y revisión por tarea; sin coverage mapping | Requisito a código y escenario a test, por búsqueda heurística en el momento; sin mapeo mantenido | Coverage mapping FR a test, verificado por script en specs `active` | **Parcial** |
| 6 | Circuito de aprendizaje | Declarado ("bidirectional feedback"), no instrumentado | Instrumentado sobre los **documentos de método**, con medición conductual | Instrumentado sobre el **contrato** y automatizado: archivar fusiona el delta en la spec vigente | Instrumentado sobre las **specs**: `Deuda arrastrada` (49 ocurrencias en el historial del testigo), Principio III acá | **Diverge en el objeto** |
| 7 | Registro de specs | Carpeta por feature `specs/[###-feature]/` | Archivos fechados, sin registro ni estado | Central por capacidad, consultable por CLI; estado implícito en la ubicación, sin campo `estado` ni nivel SSOT | Registro central por capacidad, con `estado` y `ssot_level` | **Diverge** |
| 8 | Personalización | Presets y extensions | Plugins independientes + adaptadores por harness | *Schemas* forkeables que redefinen artefactos y dependencias + adaptadores para 30+ asistentes | `ssot_level`, niveles de profundidad, generación de adaptadores | **Converge** |

### Qué cambió al incorporar el cuarto caso

El instrumento no se tocó; dos veredictos sí, y conviene que el cambio quede firmado en vez de aparecer reescrito en silencio.

- **Fila 3 pasó de «converge el principio, diverge el instrumento» a Diverge.** La lectura anterior sostenía que los tres casos compartían el principio "no asumir, preguntar" y solo diferían en cómo. OpenSpec no comparte el principio: instruye explícitamente preferir la decisión razonable para no frenar. Con dos linajes independientes de cuatro apartándose —uno del instrumento, otro del principio— lo que queda no es convergencia.
- **Fila 8 pasó de Parcial a Converge.** Con tres casos, la adaptación por capa externa era un parecido vago entre mecanismos dispares. El cuarto la ejerce en la forma más fuerte del corpus —*schemas* forkeables que redefinen el conjunto de artefactos y sus dependencias— y muestra que los cuatro no solo prevén extensión, sino que la ubican en el mismo lugar: fuera del núcleo, sin bifurcarlo.

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
- **El registro de specs diverge de plano** (fila 7): cuatro soluciones incompatibles —carpeta por feature, archivos fechados, central por capacidad con estado implícito, central por documento con `estado` y `ssot_level`— para el mismo problema. El invariante que queda es débil: las specs son archivos versionados que viven junto al artefacto que gobiernan. Lo que el cuarto caso sí agrega es un dato menor: **dos de cuatro mantienen inventario central consultable**, así que la carpeta-por-feature no es la solución dominante.

---

## Dimensiones observadas fuera del instrumento v1

Registradas por la regla 2 de la sección «Cómo se incorpora un caso nuevo»: se anotan, no se puntúan, y no abren fila.

- **Cómo llega el método al agente** (observada al incorporar OpenSpec, 2026-08-02). Las ocho filas describen qué dice el método y ninguna describe su vía de entrega. Tres casos y este repositorio usan documentos que el agente lee y sostiene en contexto; OpenSpec sirve fragmentos bajo demanda desde un CLI (`ANALISIS-OPENSPEC.md`, C2). La diferencia cambia el modo de falla del cumplimiento —no aplicar lo leído, contra no invocar el comando— y el segundo es observable sin juzgar prosa. **Sin veredicto**: con un solo caso del lado servido no hay nada que comparar, y fabricar una fila ahora garantizaría que ese caso destaque en ella. Si un quinto caso independiente la ejerce, es la primera candidata a instrumento v2.

### La divergencia más informativa: el objeto del circuito de aprendizaje

`COMPARATIVA-SPECKIT-VS-TESTIGO.md` cerró su síntesis sobre dos ejes ortogonales, regenerabilidad y adaptatividad. Superpowers no entra limpio en ese marco: es débil en regenerabilidad —no regenera nada— y su circuito de adaptatividad **no corre sobre las specs del proyecto sino sobre sus propios documentos de método**, medido por conducta de agentes en sesiones frescas.

Eso sugiere un tercer eje que los dos existentes no capturan: **sobre qué objeto corre el feedback**. Un SDD puede instrumentar el aprendizaje sobre el contrato (las specs se revisan tras la ejecución), sobre el método (el protocolo se revisa según cómo se comporta quien lo lee), o sobre ninguno. Los cuatro linajes se reparten así: el testigo y este repositorio, el contrato; OpenSpec, el contrato también, pero automatizado —archivar fusiona el delta aprobado en la spec vigente, sin que nadie tenga que acordarse—; Superpowers, el método; Spec Kit declara el circuito y no lo instrumenta en ninguno de los dos.

El cuarto caso aporta dos cosas al eje. La primera es que la casilla "contrato" deja de ser exclusiva de nuestro linaje, lo que la vuelve un punto de convergencia real y no una particularidad nuestra. La segunda es más incómoda: **somos los únicos de esa casilla que lo hacemos a mano**. La regla de propagación del Principio III y el campo `Deuda arrastrada` dependen de que una persona los ejecute; OpenSpec llegó a la misma regla y la puso en un comando. Que la parte mecánica sea automatizable está demostrado por un tercero.

Este documento propone el eje, no lo cierra: se apoya en cuatro casos y la asignación de casillas sale de leer artefactos, no de medir.

---

## Qué se puede y qué no se puede inferir de esto

**Se puede inferir consenso de diseño.** Cuatro linajes independientes que llegan a lenguaje normativo, a un gate de consistencia previo al cierre y a la extensión por capa externa, con mecanismos distintos, indican que esos elementos resuelven un problema real y recurrente del trabajo asistido por IA. El cuarto caso sube el conteo de tres a cuatro, con la reserva de procedencia declarada arriba, y ninguno de los tres invariantes se apoya solo en él.

**No se puede inferir eficacia, y este proyecto tiene evidencia propia de que la distinción no es teórica.** Que varios equipos coincidan en una práctica muestra acuerdo, no que la práctica funcione — el mismo criterio que aplicamos a fuentes secundarias como [R28] y [R30]. El cuarto caso lo ilustra por el lado más crudo: OpenSpec **no reporta ninguna medición propia**, así que suma un voto de diseño y cero evidencia. Y hay un caso medido en casa: B-07 puso a prueba justamente el elemento donde la anatomía de Spec Kit debía ganar —la regenerabilidad— y cerró **sin ventaja del formato híbrido** (`../experimentos/RESULTADO-EXPERIMENTO-B7.md`). La convergencia de diseño y el desempeño medido están desacoplados.

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

[SDD-Check]
- Spec leida: SI (spec registrada en `../SPECS_REGISTRY.md` para este doc; alta en la tabla SSOT)
- Incluye/Excluye verificado: SI - no reproduce la caracterizacion individual de ningun caso (referencia a `ANALISIS-SPEC-KIT.md`, `ANALISIS-SUPERPOWERS.md` y `ANALISIS-OPENSPEC.md`), no reproduce la comparacion pareada de cinco dimensiones, y no toma decisiones de adopcion
- Validaciones aplicadas: instrumento declarado con su version y fecha de origen (v1, 2026-05-24), anterior a tres de los cuatro casos; ninguna fila agregada ni redefinida al incorporar el cuarto caso, y la dimension que no cubre queda registrada sin veredicto; los dos veredictos que cambiaron estan firmados y motivados en «Que cambio al incorporar el cuarto caso», no reescritos en silencio; cada caso declara su procedencia antes de contarse, con los limites del filtro explicitos; divergencias reportadas con el mismo detalle que las convergencias; caracterizacion del testigo derivada de sus artefactos reales al HEAD `6b0d0d7` (17 specs, 12 con `MUST`, 7 con `[NEEDS CLARIFICATION]`, 49 ocurrencias de `Deuda arrastrada`, `check_traceability.py`), no copiada de la comparativa; encuadre «estandar de referencia» declarado como no heredado; refs internas verificadas; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: este documento (incorporacion del cuarto caso, 2026-08-02); `software/ANALISIS-SPEC-KIT.md` no vuelve a sostener la afirmacion de convergencia y la referencia
- Derivados a revisar: `software/ANALISIS-SPEC-KIT.md` (afirmacion de convergencia e inferencia hacia B6, ya corregidas; el cuarto caso no las reabre); `software/COMPARATIVA-SPECKIT-VS-TESTIGO.md` (su marco de dos ejes ya tenia puntero por el tercer caso; el cuarto refuerza el mismo señalamiento y no obliga a reescribir su sintesis); `agenda/MEJORAS-METODO.md` M-04 (la entrega bajo demanda replantea el problema de contexto que M-04 administra) y M-03 (la dependencia dura de CLI de OpenSpec es el contraejemplo de la portabilidad que M-03 defiende) — señalados, sin modificar
- Cobertura: completa - las ocho filas tienen veredicto sobre los cuatro casos, cada afirmacion de invariancia declara sobre cuantos linajes se cuenta y ninguna se apoya solo en el caso nuevo, y el procedimiento de incorporacion se ejercito en sus tres reglas: filtro de procedencia aplicado con evidencia de fechas, dimension nueva registrada fuera de la tabla, instrumento no ampliado
- Deuda arrastrada: la independencia de OpenSpec esta verificada frente a Spec Kit pero no frente a Kiro, que sigue sin leerse; Kiro y Tessl, nombrados en [R20], siguen sin pasar por el filtro de procedencia y sin alta en ningun backlog; la dimension «como llega el metodo al agente» queda registrada sin veredicto y sin decision sobre instrumento v2; el corpus observacional de OpenSpec (83 cambios archivados) no esta dado de alta; el tercer eje queda propuesto y sin cerrar, apoyado en lectura de artefactos, no en medicion; `software/LINEAS-INVESTIGACION.md` B6 conserva su enunciado original, que este documento acota pero no reescribe; la inconsistencia de `deriva_de` detectada en el registro es `M-13`, ajena a este doc
- Riesgos/reservas: tres de los cuatro casos se caracterizan desde snapshots vendored, no desde correr los sistemas; el cuarto es un repositorio propio, con el sesgo de confirmacion de B-06 ya declarado; el conteo por linajes reduce a cuatro puntos lo que a primera vista parecian cinco, y uno de esos cuatro tiene independencia solo parcialmente verificada; dos de las cuatro fuentes externas tienen interes comercial y una de ellas no reporta ninguna medicion propia
