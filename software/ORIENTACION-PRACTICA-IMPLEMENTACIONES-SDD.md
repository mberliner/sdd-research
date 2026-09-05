# Orientación práctica de las implementaciones SDD adoptables

Fecha: 2026-09-05. Línea B (software).

Pregunta que origina el documento: *si quisiera usar una de estas herramientas, ¿para qué sirve cada una, qué me pasa si mi proyecto es grande o chico, y qué consecuencias tiene configurarla de un modo u otro?*

> **Advertencia que condiciona todo lo que sigue.** **Ninguna de las cuatro fuentes reporta medición alguna** — ni interna ni externa — sobre su idoneidad para ningún escenario. Este documento dice para qué está **declaradamente** orientada cada una y qué se **deriva de sus mecanismos verificables**. No dice cuál funciona mejor, ni en proyectos grandes ni en chicos, porque nadie lo midió. Cada afirmación de abajo declara cuál de las dos cosas es: `[declarado]` o `[derivado]`. Un `[derivado]` es una consecuencia estructural de un mecanismo que se puede leer en el clon, no un resultado.

---

## 1. Población: por qué no es la misma que la de convergencia

`CONVERGENCIA-IMPLEMENTACIONES-SDD.md` lee **linajes** y pregunta de dónde vino cada método. Acá la pregunta es otra —¿lo podés instalar y usar?— y por eso la población no coincide: tres casos entran acá sin sumar linaje allá.

| Caso | En convergencia | Acá | Motivo |
|---|---|---|---|
| Spec Kit [R10] | Sí | **Sí** | — |
| OpenSpec [R38] | Sí | **Sí** | — |
| Superpowers [R37] | Sí | **Sí** | — |
| sdd-first [R39] | **No** suma linaje | **Sí** | Es un kit instalable. Su procedencia no importa para decidir si sirve; importa que exista y se pueda usar |
| Kiro [R44] | **No** toma columna | **Sí** | Producto cerrado y disponible. Que sea cerrado es una **dimensión** (D13), no un impedimento |
| Tessl [R46] | **No** toma columna | **Sí** | Producto cerrado, con el *Framework* en beta cerrada. Que no esté disponible hoy es una **dimensión** (D14), no un impedimento — y excluirlo dejaba afuera al único caso que regenera |

**Corrección del criterio (2026-09-05).** La primera versión de este documento decía que la población era «lo adoptable» y dejaba a Tessl afuera por estar en beta cerrada. Estaba mal por dos motivos. El primero es de coherencia: Kiro también es producto cerrado y entraba, así que «cerrado» parecía hacer el trabajo de excluir cuando el criterio declarado era otro. El segundo es de propósito: un criterio que deja afuera al único caso del corpus que **regenera código desde la spec** está mal elegido para un documento que existe para ayudar a decidir. Saber que una herramienta existe, qué hace distinto y que todavía no se consigue **es** información para decidir.

Población, entonces: **lo que alguien podría evaluar o adoptar**. Ni la apertura del código ni la disponibilidad admiten o excluyen: se documentan, en D13 y D14.

**Reserva sobre sdd-first, que MUST leerse antes de su ficha.** Es del mismo autor que este repositorio [R39]. Todo juicio favorable sobre él en un documento escrito acá es autocorrelación por construcción, y por eso su ficha se limita a hechos verificables del clon —conteos, fechas, mecanismos— sin ninguna valoración comparativa. Su factor de bus está escrito en la ficha y en la tabla.

---

## 2. Las quince dimensiones y su procedencia

Fijadas el **2026-09-05**. Su origen es la pregunta del usuario que encargó el documento —orientación de uso, comportamiento por tamaño, consecuencias de las variantes, características particulares, más madurez, actividad, licencia y soporte—, formulada **antes** de que se diseñara el instrumento. D13 y D14 se sumaron el mismo día, también a pedido, al detectar que la apertura del código estaba operando como filtro en vez de como dimensión. **D15 se sumó el 2026-09-05**, también a pedido y con el encargo formulado así: información de usuarios de primera mano, objeciones fundadas y verificaciones de buen comportamiento.

**Límite honesto, y es distinto del de convergencia.** Este instrumento **no es anterior a la lectura de los casos**: los cuatro clones se releyeron los días previos. En `CONVERGENCIA` eso sería descalificante, porque con libertad para elegir qué comparar la convergencia se fabrica. Acá el riesgo es otro y menor —elegir dimensiones donde una herramienta luzca—, y la mitigación es la procedencia: las quince salen de lo que preguntó quien va a decidir, no de lo que los casos ofrecen. Quien no acepte esa mitigación debe leer la tabla como descriptiva y no como criterio de selección.

| # | Dimensión | Qué responde |
|---|---|---|
| D1 | Orientación declarada | Para qué dice servir la fuente |
| D2 | Objeto gobernado | Qué gobierna: código, documentación, o el trabajo del agente |
| D3 | Unidad de trabajo y comportamiento por tamaño | Qué pasa cuando el trabajo crece, y cuando es trivial |
| D4 | Variantes y sus consecuencias | Qué opciones ofrece y qué cuesta cada una |
| D5 | Configuración y personalización | Cuánto se puede cambiar y a qué costo |
| D6 | Exigencias del entorno | Qué hace falta tener instalado |
| D7 | Costo de entrada y de salida | Qué deja puesto y cómo se saca |
| D8 | Modo de falla característico | Qué se rompe primero cuando se usa mal |
| D9 | Madurez | Edad, volumen, versión |
| D10 | Actividad | Movimiento y gente, últimos 90 días |
| D11 | Licencia | Qué permite |
| D12 | Soporte y respaldo | Quién está detrás y qué se puede esperar |
| D13 | Apertura del código | Si se puede leer, auditar y forkear — y qué queda en tu repositorio si dejás de usarlo |
| D14 | Disponibilidad | Si se consigue hoy: general, beta abierta, o beta cerrada |
| D15 | Uso y reputación en redes | Cuánta atención acumuló, y qué reportan de primera mano quienes la usaron: objeciones fundadas y verificaciones de buen comportamiento |

**D13 y D14 se agregaron el 2026-09-05**, al corregir el criterio de población. Antes estaban implícitas y operando como filtro, que es la peor forma de tener una dimensión: decidía admisiones sin figurar en ningún lado. La regla ahora es explícita — **describen, no admiten**.

**D15 se agregó el mismo día**, y es la dimensión de peor clase de evidencia del documento: no `[declarado]` ni `[derivado]`, sino una tercera categoría, `[reportado]` — lo que dijeron terceros identificables sobre su propia experiencia. Su tratamiento está en la sección 4 quinquies, y la advertencia que la gobierna es una sola: **un reporte de práctica no es una medición, y contar reportes tampoco lo vuelve una**.

---

## 3. Tabla resumen

Los números de D9 a D11 salen de los clones vendored con `git`, no de la documentación de cada fuente. Corte: 2026-09-05; ventana de 90 días desde 2026-06-07.

| | **Spec Kit** [R10] | **OpenSpec** [R38] | **Superpowers** [R37] | **sdd-first** [R39] | **Kiro** [R44] | **Tessl** [R46] |
|---|---|---|---|---|---|---|
| **D1** Orientación | Feature nueva, ciclo completo spec→plan→tasks→código | Cambio sobre un sistema que ya existe, por capacidad | Metodología de trabajo del agente, no de specs | Sembrar gobernanza SDD dentro de otro proyecto | El salto de prototipo a producción, dentro de un IDE | Que la spec sea la fuente y el código su derivado |
| **D2** Objeto | Código | Código | El trabajo del agente | Código, o sólo gobernanza (modo `none`) | Código | Código, **generado desde la spec** |
| **D3** Unidad / tamaño | Carpeta por feature. Escalera **explícita de 4 opciones** cuando no entra en un ciclo | Capacidad durable + *change* como unidad de trabajo | Clasifica cada pedido en **spike / bounded / architectural** | Spec numerada con historias y FR por historia | Tres artefactos por spec, con `Feature Spec` / `Quick Spec` / `Quick Plan` | `.spec.md` por componente: descripción, capacidades **con test enlazado**, API pública |
| **D4** Variantes | **Tres modelos de persistencia, con su riesgo declarado por la fuente** | *Schemas* forkeables; *stores* multi-repo (beta) | Tres caminos de ceremonia; harness elegible | Adaptador de lenguaje, o modo `none` | *Requirements-First* / *Design-First*; `Quick Spec` **sin compuertas** | `@generate` (spec→código) o `@describe` (código→spec) |
| **D5** Configuración | 41 integraciones; **165 extensiones y 34 presets de comunidad** contra 4 y 2 oficiales | `openspec/config.yaml` + schemas forkeables | Plugins + adaptadores por harness | `.sdd/config.yaml`, todo generado desde ahí | `.kiro/steering/` + hooks por evento | *Spec Registry*: **+10.000 specs** de uso, y las propias publicables |
| **D6** Entorno | Python ≥3.11 + CLI | Node ≥20.19 + CLI | El harness; sin CLI propio | Python 3.11 + git | El IDE de Kiro | El agente que ya uses + el Framework |
| **D7** Entrada / salida | `specify init`; desinstalar y cambiar integración están documentados | `openspec init`; `openspec update` regenera | Plugin del harness; se quita como plugin | Se siembra **y el kit se descarta**; `sdd_update.py` propaga después | No hay instalación de método: lo trae el IDE | Se integra al agente existente |
| **D8** Modo de falla | La cadena de suministro de extensiones | No invocar el CLI: sin comando no hay método | La skill no se dispara | El verificador que reporta OK sin verificar | Usar `Quick Spec` por defecto: método sin compuertas | Regenerar y obtener algo distinto — no-determinismo observado [R20] |
| **D9** Madurez | 2025-08-21; 1927 commits; **188 releases**; v1.0.5.dev0 | 2025-08-05; 828 commits; 48 releases; v1.12.0 | 2025-10-09; 681 commits; 34 releases; v6.3.0 | **2026-08-01**; 143 commits; **0 releases** | Anuncio **2025-07-14**, el más antiguo. Resto **no medible** | Productos **2025-09-16/23**. Resto **no medible** |
| **D10** Actividad 90d | 838 commits, **97 autores** | 226 commits, 54 autores | 240 commits, 17 autores | 143 commits, **1 autor** | **No medible** — sin repositorio de producto | **No medible** — sin repositorio de producto |
| **D11** Licencia | MIT | MIT | MIT | Apache 2.0 | Propietaria | Propietaria |
| **D12** Soporte | GitHub; 297 autores históricos | Fission AI (comercial); 111 autores | Prime Radiant (comercial); 47 autores | **Individual; factor de bus 1** | Amazon Web Services; tracker público de issues | Tessl (startup); blog y docs |
| **D13** Apertura | **Abierto** | **Abierto** | **Abierto** | **Abierto** | **Cerrado** — artefactos en tu repo (`.kiro/specs/`, `.kiro/steering/`) | **Cerrado** — artefactos en tu repo (`.spec.md`) |
| **D14** Disponibilidad | General | General | General | Público, sin release versionada | General | *Registry* beta abierta; **Framework beta cerrada** |
| **D15** Uso y reputación `[reportado]` | 133 601 estrellas. Objecion recurrente: sobredimensiona lo chico | 67 384 estrellas. Objecion recurrente: deriva de las specs al sincronizar | **282 058 estrellas**, la mayor. Reputación **partida**: entusiasmo y rechazo explícito, ambos de primera mano | **0 estrellas, 0 forks**. Sin ningún reporte de terceros | Estrellas **no comparables** (repositorio sólo de issues); **1614 issues abiertas**; incidente de cupos y precios reconocido por AWS | **No medible** — sin repositorio; sin reportes de uso, porque casi nadie pudo usarlo |

---

## 4. Ficha por caso

### Spec Kit [R10] — el ciclo completo para una feature nueva

**Orientación** `[declarado]`: un ciclo por feature, de la spec al código, con comandos que el asistente ejecuta en orden. `/speckit.converge` cubre el caso de un codebase ya existente, pero el diseño base asume que empezás algo.

**Cuando el trabajo crece** `[declarado]`: es el único de los cuatro con una **escalera escrita**, ordenada de más barata a más cara (`../fuentes-externas/spec-kit/docs/concepts/complex-features.md`): limitar cuántas tareas corre cada invocación; delegar en subagentes; combinar las dos; y sólo si nada de eso alcanza, descomponer en un *roadmap* de sub-specs (`spec-of-specs.md`). La fuente advierte que la descomposición «adds the most overhead of any strategy».

**Variantes, con su costo dicho por la fuente** `[declarado]` — esto es lo más útil de este caso y no tiene equivalente en los otros tres (`../fuentes-externas/spec-kit/docs/concepts/spec-persistence.md`):

| Modelo | Regla | Riesgo, en palabras de la fuente |
|---|---|---|
| Flow-back | Se edita cualquier artefacto y después se reconcilia | «The main risk is silent divergence» |
| Flow-forward | Los artefactos completados son inmutables; un requisito nuevo abre carpeta nueva | «The main tradeoff is duplication» |
| Living spec | Se edita `spec.md` y lo derivado se regenera | «Losing useful implementation rationale» |

La fuente subraya que **no impone ninguno**: «None is the default, and none is required by Spec Kit». Elegir es tarea del equipo, y no elegir es elegir flow-back por omisión `[derivado]`.

**Configuración y su costo** `[derivado]`: el catálogo oficial tiene 4 extensiones y 2 presets; el de comunidad, **165 y 34**. La personalización real pasa por código de terceros, y por eso la propia fuente incorporó un modelo de confianza declarado para los catálogos. Es potencia y es superficie de ataque en la misma pieza.

**Modo de falla** `[derivado]`: con 169 extensiones disponibles y 165 de ellas ajenas, el punto débil se desplaza del método a la cadena de suministro.

**Madurez y soporte**: el más maduro de los cuatro por cualquier medida — 1927 commits, 188 releases, 297 autores, 97 activos en 90 días. Respaldo de GitHub. MIT.

**Rasgo sin equivalente**: haber escrito las consecuencias de sus propias variantes en vez de dejarlas al lector.

---

### OpenSpec [R38] — el sistema que ya existe, gobernado por capacidad

**Orientación** `[derivado]`: el par `openspec/specs/` (capacidades durables, del tipo `cli-init`) más `openspec/changes/` (unidades de trabajo con `Why` / `What Changes` / `Capabilities`) está armado para un producto que ya existe y se modifica. Un *change* declara qué capacidades crea y cuáles modifica; al archivar, el delta se fusiona en la spec vigente.

**Cuando el trabajo crece** `[derivado]`: no tiene mecanismo de escala por tamaño de tarea. Lo que sí tiene es escala **por repositorio**: los *stores* (beta) sacan `openspec/` a un repositorio propio compartido por varios repos de código, con ramas y pull requests como cualquier repositorio (`../fuentes-externas/OpenSpec/docs-lab/multi-repo/stores.md`). Es el único de los cuatro que aborda el caso de una feature que cruza frontend y backend en repos distintos.

**Variantes** `[declarado]`: *schemas* forkeables que redefinen el conjunto de artefactos y sus dependencias; `--strict` para endurecer la validación; `init --language` para el idioma de los artefactos.

**Entrega del método** `[derivado]`: es el único que **no** entrega el método como documento a leer, sino en fragmentos servidos por el CLI. Cambia el modo de falla: no es «no aplicó lo que leyó» sino «no invocó el comando», que es observable sin juzgar prosa (`ANALISIS-OPENSPEC.md`, C2). La contracara es una dependencia dura del CLI.

**Modo de falla** `[derivado]`: si el asistente no invoca el CLI, no hay método. Nada avisa.

**Madurez y soporte**: 828 commits, 48 releases, 111 autores, 54 activos en 90 días. Fission AI, respaldo comercial. MIT. Soporta 62 herramientas, la superficie más ancha del corpus.

**Rasgo sin equivalente**: la separación del repositorio de specs respecto del repositorio del artefacto.

---

### Superpowers [R37] — no gobierna specs, gobierna cómo trabaja el agente

**Orientación** `[derivado]`: es el caso que menos se parece a los otros tres. Su «spec» es un documento de diseño fechado (`Goal` / `Design` / `Tests` / `Non-Goals`) y nada se regenera desde ella. Lo que empaqueta son 14 skills de método: TDD, depuración sistemática, revisión por subagentes, cierre de rama. **Si lo que buscás es un registro de specs, este no es.**

**Cuando el trabajo crece o es chico** `[declarado]`: es el más explícito de los cuatro en escalar la ceremonia, y en las dos direcciones. Clasifica cada pedido en **spike** (pregunta de factibilidad, no escribe nada), **bounded** (diseño corto en chat) o **architectural** (spec y plan completos). Con cuatro guardas: la clasificación se anuncia en voz alta para que el humano la anule; ante la duda se toma el camino pesado; la complejidad descubierta a mitad sube de camino y nada baja; y **la compuerta de aprobación no escala** — «What scales with simplicity is the artifact, never the approval».

**Variante de ejecución** `[declarado]`: desde v6.3.0, un conflicto no catastrófico no frena — se resuelve contra la spec, se registra como `Ruling: <qué> — <por qué> — <cuánto cuesta si está mal>` y el trabajo sigue. Sólo lo destructivo o irreversible espera a un humano. La fuente motiva el cambio con un caso: una sesión bloqueada casi nueve horas por una pregunta que el controlador podía haber decidido. **Autoreportado, un caso, sin medición**.

**Modo de falla** `[derivado]`: todo depende de que la skill se dispare. Y sus propios evals mostraron que el contenido de la prosa es load-bearing — borrar una sección argumentativa de la skill de TDD degradó la conducta test-first de 8/10 a 5/10 bajo presión.

**Madurez y soporte**: 681 commits, 34 releases, 47 autores, 17 activos en 90 días — la comunidad más chica de los tres externos. Prime Radiant, respaldo comercial. MIT. 14 harnesses.

**Rasgo sin equivalente**: evaluar la documentación por la conducta que produce, con subagentes frescos y escenarios de presión.

---

### sdd-first [R39] — el andamiaje que se siembra y se descarta

> **Leer primero la reserva de la sección 1.** Mismo autor que este repositorio. Esta ficha son hechos del clon, sin valoración comparativa.

**Orientación** `[declarado]`: no es una herramienta de ciclo sino un **instalador de gobernanza**. Se clona una vez, se siembra dentro de otro proyecto con `core/sdd_init.py`, y el kit se descarta. Lo que queda en el destino es constitución, registro de specs, gate que bloquea editar código sin spec vigente declarada, pipeline determinista y skills servidas a cuatro asistentes desde una fuente única.

**Objeto gobernado** `[declarado]`: código, o —en modo `none`— sólo gobernanza y specs, sin adaptador de lenguaje. Es el único de los cuatro que contempla explícitamente un repositorio sin código de producto, aunque ese modo no está probado sobre un corpus documental grande (`ANALISIS-SDD-FIRST.md`, C6).

**Cuando el trabajo crece** `[derivado]`: sin mecanismo de escala por tamaño. La unidad es la spec numerada con historias de usuario priorizadas y requisitos numerados por historia (`FR-US1-004`).

**Costo de salida** `[declarado]`: el kit no queda instalado; queda el andamiaje. Actualizar el método después se hace con `core/sdd_update.py`, que muestra el plan sin escribir salvo `--apply`, nunca pisa una plantilla editada y deja la versión nueva como `.kit-new` para fusionar a mano.

**Modo de falla** `[derivado]`: sus ocho correcciones de agosto son todas de la misma familia — un verificador que reportaba OK sin verificar nada, o una guarda abierta por un camino que nadie probó (`ANALISIS-SDD-FIRST.md`, §Los ocho arreglos y C8). El gate es fail-closed por diseño, y el trabajo del kit consiste en encontrar dónde no lo era.

**Madurez, actividad y soporte — el punto decisivo**: primer commit **2026-08-01**, un mes de vida; 143 commits; **cero releases**; **un solo autor**. Licencia Apache 2.0, la única del corpus que no es MIT. No hay comunidad, ni respaldo comercial, ni versionado publicado. **Factor de bus 1.** Adoptarlo es adoptar el trabajo de una persona sin release estable.

**Rasgo sin equivalente**: propagar el método a instalaciones derivadas a través de una frontera de repositorios, con detección de conflictos.

### 4 bis. Kiro [R44] — el IDE con el método adentro, y el único que no se puede auditar

> **Clase de evidencia.** Kiro es **producto cerrado** (D13): su repositorio público declara que no aloja el código del producto. Todo lo de abajo se cita de documentación oficial. Y **D9, D10 y D11 no se pueden calcular con `git`** como en los cuatro abiertos: no hay clon, no hay conteo de commits, ni de autores, ni de releases. Que sea cerrado no lo excluye de este documento — es la dimensión D13, y su consecuencia práctica está al final de la ficha.

**Orientación** `[declarado]`: el salto de prototipo a producción, formulado así — «prompt, prompt, prompt, and you have a working application. It's fun and feels like magic. But getting it to production requires more». Las specs sirven «anytime you need to think through a feature in-depth, refactor work that needs upfront planning, or when you want to understand the behavior of systems».

**Objeto gobernado** `[derivado]`: código, dentro de un IDE. Es el único de los cinco donde el método **no se instala sobre tu herramienta**: la herramienta lo trae. No hay paso de scaffolding porque no hay nada que sembrar.

**Unidad y comportamiento por tamaño** `[declarado]`: tres artefactos por spec —`requirements.md`, `design.md`, `tasks.md`— en `.kiro/specs/<feature>/` (esta ruta, atribuida a [R45]; la documentación oficial consultada no la expone). Y una escala de ceremonia con tres escalones: `Feature Spec` con compuertas de aprobación entre fases, `Quick Spec` que las **saltea** y `Quick Plan`.

**Variantes y sus consecuencias**:

| Variante | Qué cambia | Consecuencia |
|---|---|---|
| *Requirements-First* | requisitos → diseño → tareas | El orden de manual |
| *Design-First* | diseño → requisitos → tareas | Para cuando la forma técnica precede al enunciado |
| **Quick Spec** | Genera los tres artefactos **sin compuertas** | `[derivado]` Escala el artefacto **y** la aprobación a la vez. Superpowers hace lo contrario a propósito: «what scales with simplicity is the artifact, never the approval». Elegir Quick Spec es elegir que nadie mire antes de que se escriba código |

**Requisitos en EARS** `[declarado]`: `WHEN <condición> THE SYSTEM SHALL <comportamiento>`, con `IF-THEN` reservado a condiciones de error. Es el único de los cinco que adopta una sintaxis de requisitos con nombre propio y reglas de patrón, en vez de acuñar la suya.

**Persistencia** `[declarado]`: «Kiro's specs stay synced with your evolving codebase. Developers can author code and ask Kiro to update specs». Es el único que declara el camino **código → spec** como soportado por la herramienta. En los modelos de [R10] eso es *flow-back*, y hereda su riesgo declarado: «silent divergence».

**Configuración** `[declarado]`: convenciones de proyecto en `.kiro/steering/`, compartidas entre todas las superficies; y *hooks* de agente, «event-driven automations that execute when you save or create files». El enforcement es por evento, no por compuerta de fase.

**Modo de falla** `[derivado]`: si el equipo usa `Quick Spec` por defecto, el método queda sin compuertas y el artefacto se genera sin que nadie lo apruebe — que es el escenario que el resto del producto existe para evitar.

**Costo de entrada y de salida** `[derivado]`: la entrada es baja, porque no hay que instalar ni configurar un método sobre tu editor. La salida cuesta el **motor**, no los **documentos**: `.kiro/specs/` y `.kiro/steering/` son markdown que vive en tu repositorio y se lo puede llevar cualquiera, pero el flujo de fases, las compuertas y los hooks son el producto y no se van con vos.

> Esta afirmación corrige una anterior de este mismo documento, que decía que la salida era «la más cara de las cinco» porque «el método está atado al producto». Era demasiado gruesa: confundía perder la herramienta con perder el trabajo. Ver §4 quater.

**Madurez, actividad, apertura y soporte**: anuncio del **2025-07-14**, lo que lo vuelve **el más antiguo del corpus**; respaldo de Amazon Web Services, el más grande de los seis; documentación oficial extensa, tracker público de issues y material formativo propio en AWS Skill Builder. Disponibilidad general (D14). Y **cerrado** (D13): sin licencia abierta, sin historial auditable, sin conteo de contribuyentes, y sin posibilidad de forkearlo si el producto cambia de rumbo o de precio.

**Rasgo sin equivalente**: que el método no se instala — lo trae la herramienta. Su contracara: el método tampoco se puede llevar a otro lado, aunque los documentos sí.

### 4 ter. Tessl [R46] — el único que regenera, y el que menos se puede conseguir

> **Clase de evidencia, la más débil del documento.** Producto **cerrado** (D13) y con el *Framework* en **beta cerrada** (D14): no hay clon, no hay repositorio de producto, y hoy no se puede instalar. Además, el rasgo por el que este caso importa —la regeneración— está verificado en **[R20]**, un tercero identificado, y no en la documentación de la fuente. Entra igual: excluirlo dejaba afuera al único caso que hace lo que los demás sólo enuncian.

**Orientación** `[declarado]`: que la spec sea lo que persiste y el código su derivado. El problema declarado son agentes que codifican antes de tiempo, alucinan APIs, mezclan versiones y rompen lo que ya andaba. Textual: «These instructions live in the codebase as **long-term memory**, guiding agents as the app evolves and pairing with tests to enforce guardrails so existing functionality isn't broken».

**Unidad de trabajo** `[declarado]`: el archivo `.spec.md` por componente, con tres partes — descripción, **capacidades en lenguaje natural con un test enlazado cada una**, y la API pública. La unidad no es un requisito suelto: es el par capacidad-verificador. Ningún otro caso ata la unidad de la spec a su test en la estructura misma del archivo.

**Variantes, y son las de más consecuencia del documento** `[declarado]`:

| Directiva | Dirección | Consecuencia |
|---|---|---|
| `@generate` | spec → código | El código se genera desde la spec. `[R20]` reporta que los archivos resultantes llevan `// GENERATED FROM SPEC - DO NOT EDIT` |
| `@describe` | código → spec | La spec documenta lo que ya existe, sin generarlo |

Esa pareja es un camino de adopción en brownfield que ningún otro caso tiene en esta forma: la misma herramienta levanta specs de lo que ya está y genera lo que todavía no. Elegir entre las dos directivas es elegir quién manda sobre cada componente.

**Configuración** `[declarado]`: el *Spec Registry*, en beta abierta y gratuito, con «more than 10,000 pre-built specs» de librerías open source y la posibilidad de publicar las propias como paquete instalable. Los otros cinco distribuyen **método**; éste distribuye **contenido de spec**. Es la spec tratada como dependencia, con registro y versión.

**Modo de falla** `[derivado]`, y está documentado por un tercero: regenerar y obtener algo distinto. El autor de [R20] generó código varias veces desde la misma spec y reporta «the **non-determinism** in action». **No es una medición** —observación de un practicante, sin diseño ni repeticiones declaradas— pero es la única evidencia empírica de terceros que este corpus tiene sobre una regeneración spec → código.

**Costo de entrada y de salida** `[derivado]`: la entrada exige acceso a una beta cerrada, que es el costo más alto de los seis y no es de dinero sino de disponibilidad. La salida, como en Kiro, cuesta el motor y no los documentos: los `.spec.md` viven en tu repositorio. Con una diferencia que sí es grave — si el código está marcado `DO NOT EDIT` y la herramienta que lo genera deja de estar, lo que queda es código generado que nadie mantuvo nunca a mano.

**Madurez, actividad y soporte**: productos lanzados el **2025-09-16** y el **2025-09-23**; el más reciente de los casos externos. Sin repositorio de producto, así que D9 y D10 **no son medibles** del modo en que lo son para los cuatro abiertos. Respaldo de una startup, con blog y documentación propios.

**Rasgo sin equivalente**: es el único que regenera. [R20] lo ubica como «the only one of these three tools that explicitly aspires to a spec-anchored approach, and is even **exploring the spec-as-source level of SDD**».

---

### 4 quater. Lo que la apertura decide en la práctica

Cuatro de los seis casos son abiertos (MIT o Apache 2.0) y dos son cerrados. Es tentador leer eso como una línea que separa lo confiable de lo que no, y es más útil separar tres cosas distintas que la apertura decide por separado:

| Qué está en juego | Abiertos | Cerrados |
|---|---|---|
| **Auditar el método** | Se lee el código que lo implementa | Sólo lo que la documentación declara |
| **Medir madurez y actividad** | `git`: commits, autores, releases | **No medible** de forma comparable |
| **Forkear o continuar** si el proyecto cambia de rumbo | Se puede | No |
| **Conservar tus artefactos** | Sí | **También sí** — `.kiro/specs/`, `.kiro/steering/`, `.spec.md` son markdown en tu repositorio |

La última fila es la que suele leerse mal, y este documento la leyó mal en su primera versión. **Un producto cerrado no te encierra los documentos: te encierra el motor.** Con Kiro conservás las specs y perdés el flujo de fases, las compuertas y los hooks. Con Tessl conservás los `.spec.md` y perdés `tessl build` — y ahí sí hay un agravante propio, porque el código generado lleva marca de no editarse a mano.

Lo que la apertura **no** decide: cuál funciona mejor. Ninguno de los seis lo midió.

---

### 4 quinquies. Uso y reputación: qué reportan quienes las usaron (D15)

**Clase de evidencia, y hay que leerla antes que cualquier cita de abajo.** Esta sección no mide nada. Reúne dos cosas distintas y las mantiene separadas:

1. **Atención acumulada** — estrellas, forks, watchers e issues abiertas, tomadas de la API de GitHub el 2026-09-05 [R49]. Una estrella es barata, no decrece cuando alguien abandona la herramienta, y no distingue uso de curiosidad. Mide **cuánta gente miró**, no cuánta usa ni cuánta quedó conforme.
2. **Reportes de práctica de primera mano** — comentarios firmados en hilos públicos [R47] y objeciones en los trackers de los propios proyectos [R48], más el registro de prensa del único incidente operativo documentado del corpus [R50].

Los tres canales tienen sesgos conocidos y **opuestos**, y por eso se citan juntos: quien comenta en un hilo es quien tuvo una experiencia lo bastante buena o lo bastante mala como para escribirla; un tracker recoge quejas y no satisfacción; la prensa cubre incidentes y no funcionamiento normal. Ninguna cita de abajo dice qué proporción de usuarios piensa qué, porque ninguna de estas fuentes puede decirlo. Lo que sí aportan, y es lo que se pidió: **objeciones fundadas** —reproducibles, atribuidas y respondibles— y **verificaciones de buen comportamiento** de gente que corrió la herramienta.

Todo lo de esta sección se marca `[reportado]`, una tercera categoría junto a `[declarado]` y `[derivado]`.

**Spec Kit** [R10] — 133 601 estrellas, 12 025 forks, 313 issues abiertas [R49]. La objeción más votada de su propio tracker se titula «SpecKit creates the illusion of work, generating a bunch of text», y es concreta: «Files are created ignoring the project structure, because the focus is not on the project, but on thousands of lines of instructions» [R48]. La respuesta más votada no la refuta, la reencuadra —«The balance has shifted from ~80% coding to 50% planning, 20% coding, 30% validation»— y un tercer participante concede el límite: «for smaller changes, speckit is overkill» [R48]. En hilos públicos, dos reportes de fracaso con detalle: «When it finished, there was still a huge gap. Most tests were failing, and the build was not successful» (yoaviram, sobre dos proyectos) y «it generated steps that were the equivalent of Tony Stark building a robot from scratch in a cave» (ctxc), ambos por sobredimensionamiento [R47]. Del otro lado, reportes de buen comportamiento en brownfield: «I still find tools like spec kit give reliably good results in brownfield codebases» [R47]. **El patrón de la objeción es estable y coincide con lo que la propia fuente admite en su escalera de complejidad**: el costo fijo del ciclo no baja cuando el trabajo es chico.

**OpenSpec** [R38] — 67 384 estrellas, 4636 forks [R49]; su presentación en Hacker News no generó discusión (2 puntos, sin comentarios) [R47], así que lo que hay son reportes sueltos y posteriores. Uno positivo y condicionado: «it's really good if you invest enough in the specs» (jochem9, tras meses de uso), que añade el problema práctico —«when a spec changes, AI needs to find the relevant code to change it»— [R47]. Y uno negativo, del mismo hilo, que ataca justo el mecanismo central del caso: «I enjoy the OpenSpec format but I think maintaining the main specs is not worth it… When you do the sync process, it just keeps drifting and drifting until you have duplication and contradictions across specs» (alasano, que dice haber dejado de mantener las specs durables y archivar directo) [R47]. **Es la objeción más específica que este documento recogió**, porque no impugna la ceremonia en general sino la fusión del delta en la spec vigente, que es el rasgo que distingue a OpenSpec.

**Superpowers** [R37] — 282 058 estrellas y 25 261 forks, la mayor atención acumulada del corpus [R49], y también la **reputación más partida**. A favor, con el mecanismo nombrado: «it does a great job with TDD that stops the model from jumping to conclusions» (prplfsh); «it simply is as much a part of my workflow as any, say, using git» (devnonymous) [R47]. En contra, y con un costo cuantificado por quien lo sufrió: «It started a workflow that spawned like a 100 sub agents… It burnt through all my max plan» (yard2010); «Aside from consuming a stupid amount of tokens, it did materially worse across all my personal benchmarks» (artisin); y una objeción de fondo, «It's just not necessary with the modern models and fills up the context windows with garbage» (arcticfox) [R47]. La objeción de artisin es la única del corpus que invoca comparación contra una línea base propia —y aun así son *benchmarks* personales sin publicar, no una medición reproducible. **Consumo de contexto y de tokens es el eje de casi todo el rechazo**, y es coherente con el mecanismo del caso: el método se paga en prosa que entra al contexto.

**sdd-first** [R39] — **0 estrellas, 0 forks, 0 issues, 0 watchers** [R49], y ningún reporte de terceros en ningún canal consultado. No hay reputación que informar: no porque sea mala, sino porque **nadie de afuera lo usó**. Combinado con su factor de bus 1, esta dimensión es la que más pesa en su contra para alguien que evalúe adoptarlo, y por eso se deja escrita sin atenuantes.

**Kiro** [R44] — sus 4259 estrellas **no son comparables** con las de los cuatro abiertos: ese repositorio no aloja el producto, sólo issues. Lo comparable es lo otro: **1614 issues abiertas** [R49]. Es el único caso del corpus con un **incidente operativo documentado y con respuesta del proveedor**: en julio de 2025 AWS impuso lista de espera y cupos diarios en la preview por exceso de demanda —«we've introduced some temporary measures – including a waitlist for new users and daily usage limits for existing users»— y en agosto reconoció un error de facturación —«some tasks are inaccurately consuming multiple requests. That's causing people to burn through their limits much faster than expected»—, con reseteo de límites a los afectados [R50]. La objeción de producto más citada de su tracker es de precio y de diseño de la unidad cobrada: «Vibe requests are useless because the Vibe agent constantly nags me to switch to Spec requests, claiming my chats are "too complex"» [R48]. En práctica, los dos signos: en contra, «generated massive task lists (12+ tasks with 4+ sub-tasks each)», con borrado impredecible de código, «a sledgehammer to crack a nut» (hatmanstack); a favor, y con un uso acotado que vale la pena registrar porque contradice la orientación declarada del producto, «I use Kiro IDE (≠ Kiro CLI) primarily as a spec generator… it's quite opinionated, but very effective» (wenc) [R47]. **La verificación de buen comportamiento que aparece es la de un uso parcial**: la herramienta como generadora de specs, no como IDE de ciclo completo.

**Tessl** [R46] — **no medible y sin reportes**: no hay repositorio público de producto [R49], y el *Framework* sigue en beta cerrada, así que casi nadie pudo usarlo y no hay práctica que reportar. Lo único de primera mano que este corpus tiene sobre él es lo de [R20], ya citado en su ficha, y es de un practicante, no una medición. Su ausencia de reputación **no es un dato en su contra**: es la consecuencia directa de D14.

**Qué decide D15 y qué no.** Decide una cosa sola: si alguien más ya se chocó con esto y lo contó. Sirve para anticipar el modo de falla que vas a encontrar —y en los cuatro casos con reportes, la objeción recurrente coincide con el modo de falla `[derivado]` que este documento ya había leído en el mecanismo, lo cual es una **convergencia entre dos clases de evidencia independientes** y es el hallazgo más interesante de esta sección. **No** decide cuál funciona mejor: 282 058 estrellas con rechazo explícito de practicantes y 0 estrellas sin ningún reporte no son extremos de una misma escala de calidad. Son extremos de una escala de **exposición**.

---

## 5. Paradigma por caso: qué es la spec en cada uno

Fijado el **2026-09-05**, a pedido del usuario, y con una restricción de método: **esta sección no introduce ninguna fuente ni ningún dato nuevo**. Cada paradigma se deriva de dimensiones ya enunciadas arriba —sobre todo D1, D2, D3, D4, D7 y D8— y se puede rastrear hasta la ficha del caso. Si algo no está en las quince dimensiones, no está acá.

Las quince dimensiones convergen en un eje discriminante único, y es el que ordena la tabla: **qué es la spec, y dónde vive la autoridad**.

| | Qué es la spec | Dónde vive la autoridad | Dónde vive el enforcement | Qué se paga |
|---|---|---|---|---|
| **Spec Kit** | Una **etapa** del ciclo | En el ciclo, no en el artefacto: terminada la feature, la spec deja de mandar salvo que el equipo elija un modelo de persistencia | Comandos en orden, ejecutados por el asistente | El costo fijo del ciclo, que no baja cuando el trabajo es chico |
| **OpenSpec** | El **estado vigente** del sistema | En la capacidad durable; el trabajo es un delta contra ella | El CLI, que sirve el método por fragmentos y bajo demanda | La fusión del delta al archivar |
| **Superpowers** | Efímera — un documento de diseño fechado, del que no se regenera nada | **Fuera de la spec**: en la conducta del agente | El disparo de la skill, más una compuerta de aprobación que a propósito no escala | Contexto y tokens |
| **sdd-first** | Un **permiso** para tocar el código | En el gate: sin spec vigente declarada, no hay edición | Código fail-closed, instalado en el repositorio de destino | Que el verificador reporte OK sin verificar |
| **Kiro** | Un artefacto **del entorno**, sincronizable en las dos direcciones | En el producto: el flujo de fases es el IDE | Compuertas de fase —salteables con `Quick Spec`— más hooks por evento | Dependencia de proveedor: precio, cupos, y ningún fork posible |
| **Tessl** | El **archivo fuente**; el código es salida, marcada `DO NOT EDIT` | En la spec, sin discusión: es el único caso donde el código es derivado | El par capacidad-test, dentro del propio `.spec.md` | No-determinismo al regenerar |

De ahí salen seis paradigmas nombrables:

**Spec Kit — proceso ceremonial parametrizable.** Da el ciclo completo y delega en el equipo el régimen de persistencia, con los tres modelos y sus riesgos escritos. Su apuesta es que el orden de las fases es lo que produce el resultado; su consecuencia, que el mismo orden se cobra igual en lo grande y en lo chico, que es exactamente la objeción recurrente de sus usuarios (§4 quinquies).

**OpenSpec — control de cambios sobre un estado declarado.** Es la contabilidad aplicada a las capacidades: hay un vigente y hay asientos contra él. La spec no acompaña al trabajo, lo precede y lo sobrevive. Su punto débil está en la misma operación que lo define —fusionar el delta en el vigente—, y ahí es donde apuntan sus objeciones.

**Superpowers — disciplina de oficio.** No gobierna el artefacto: gobierna al operario. Es el único de los seis donde la spec es prescindible y el método no lo es. Por eso su modo de falla no es documental sino conductual, y su costo se paga en contexto.

**sdd-first — cumplimiento verificado por código.** La gobernanza no se lee, se ejecuta: se siembra en el repositorio, bloquea, y el kit se descarta. La spec cambia de estatuto —de guía a condición de admisibilidad—, y por eso el punto crítico se desplaza al verificador: un método así vale exactamente lo que valga su comprobación.

**Kiro — método encarnado en el producto.** No se instala porque no es del equipo: es una propiedad del entorno. Eso resuelve el costo de entrada y crea el único riesgo del corpus que no es técnico sino de proveedor, con el incidente de cupos y precios de 2025 como evidencia fechada ([R50], §4 quinquies).

**Tessl — compilación desde la especificación.** La spec como código fuente y como dependencia versionada de un registro. Es el único que trata al código como salida y el único que distribuye contenido de spec en vez de proceso. Su riesgo es el del compilador que no es determinista.

**Tres advertencias sobre esta sección** `[derivado]`:

- **Un paradigma no es un juicio de calidad.** Son respuestas distintas a preguntas distintas, no puestos de un orden. Nada de lo anterior dice cuál conviene, y este documento no tiene con qué decirlo (§7).
- **La lista no es una partición.** Superpowers gobierna el trabajo del agente y los otros cinco gobiernan artefactos: es **ortogonal** a ellos, no una alternativa. Combinarlo con cualquiera de los otros es coherente con ambos paradigmas.
- **Esto no es un veredicto de convergencia.** Acá cada caso se caracteriza por separado, con el instrumento de este documento. Si dos paradigmas se parecen, esta sección **no** afirma que converjan, que uno derive del otro ni que compartan linaje: eso se decide con otro instrumento y otra población, en `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`.

---

## 6. Orientación por escenario

Derivada de mecanismos declarados, **no de medición**. Si dos opciones parecen igual de buenas para un caso, este documento no tiene con qué desempatarlas.

| Situación | Qué mecanismo la atiende | Caso |
|---|---|---|
| Feature nueva, greenfield, ciclo completo | Comandos en orden, carpeta por feature | Spec Kit |
| Sistema existente, cambios por capacidad | `specs/` durable + `changes/` como delta | OpenSpec |
| Una feature que cruza dos repositorios | *Stores* multi-repo (beta) | OpenSpec |
| El equipo no sabe qué hacer con las specs viejas | Los tres modelos de persistencia, con su riesgo escrito | Spec Kit |
| Tareas de tamaño muy dispar, y la ceremonia molesta | Clasificación en tres caminos, con trinquete de una vía | Superpowers |
| El problema es cómo trabaja el agente, no las specs | 14 skills de método | Superpowers |
| Quiero gobernanza SDD dentro de un proyecto que ya tengo | Siembra y descarte, con actualización posterior | sdd-first |
| Repositorio sin código de producto | Modo `none` | sdd-first, **sin probar a escala** |
| Necesito estabilidad y comunidad | 188 releases, 297 autores, respaldo institucional | Spec Kit |
| Necesito la superficie de asistentes más ancha | 62 herramientas soportadas | OpenSpec |
| Quiero el método sin instalar ni configurar nada | Viene dentro del IDE, sin scaffolding | Kiro |
| Necesito auditar el método, medir su actividad o forkearlo | Código abierto | Spec Kit, OpenSpec, Superpowers, sdd-first |
| Requisitos con una sintaxis formal y con nombre | EARS (`WHEN ... THE SYSTEM SHALL ...`) | Kiro |
| Quiero que el código se genere desde la spec, no junto a ella | `@generate` y `tessl build` | Tessl, **beta cerrada** |
| Tengo código y quiero levantar specs de lo que ya existe | `@describe` (Tessl); `/speckit.converge` (Spec Kit); `changes` sobre capacidades (OpenSpec) | Tres opciones, con mecanismos distintos |
| Que el agente no alucine APIs de librerías | Registro de specs de uso, +10.000 | Tessl |
| Quiero saber con qué me voy a chocar antes de adoptar | Reportes de práctica de terceros identificables (D15) | Spec Kit, OpenSpec, Superpowers, Kiro. **sdd-first y Tessl no tienen ninguno** |

Cuatro advertencias sobre esta tabla `[derivado]`:

- **Las filas no son excluyentes.** Superpowers gobierna el trabajo del agente y los otros tres gobiernan artefactos: combinarlo con cualquiera de ellos no es contradictorio, y la propia Spec Kit publica una extensión puente hacia él.
- **La columna «caso» no dice «el mejor».** Dice cuál tiene un mecanismo escrito para esa situación. Que exista el mecanismo no dice que funcione.
- **D15 no ordena por calidad.** Un caso sin reportes no es limpio: es desconocido. Y el caso con más atención acumulada es también el que reúne el rechazo más explícito.
- **Los dos casos cerrados están peor verificados que los cuatro abiertos**, y no por casualidad. Sus filas salen de lo que declara su documentación —y en Tessl, el rasgo principal, de un tercero—; las de los demás, de leer archivos. Esa asimetría es consecuencia de D13 y hay que tenerla presente al comparar: no dice que sean peores, dice que se sabe menos de ellos.

---

## 7. Lo que este documento no puede decir

- **Cuál funciona mejor.** Ninguna fuente reporta medición. Cuatro herramientas con mecanismos distintos para el mismo problema, y cero datos de desempeño comparado.
- **Si la orientación declarada se cumple.** Todo `[declarado]` es lo que la fuente dice de sí misma; dos de las cuatro tienen interés comercial y una es del mismo autor que este repositorio.
- **Cómo se comportan en un proyecto real.** Ninguna se corrió: las cuatro se leyeron de clones vendored.
- **Cuál paradigma es el correcto.** La sección 5 dice qué es la spec en cada caso y dónde vive la autoridad. No dice cuál de esas seis respuestas es la buena, ni si conviene que la spec sea una etapa, un estado vigente, un permiso o un archivo fuente. Eso depende del proyecto, y además nadie lo midió.
- **Si la reputación refleja calidad.** D15 recoge atención acumulada y reportes autoseleccionados de terceros. Ninguna de las tres fuentes que la alimentan —métricas de GitHub, hilos públicos, trackers— tiene población definida ni control, y las tres tienen sesgos distintos y opuestos. Sirve para anticipar objeciones, nunca para ordenar por mérito.
- **Si convergen o divergen entre sí como método.** Eso vive en `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, se lee con otro instrumento y con otra población.
- **Qué le conviene a este repositorio.** Vive en `../agenda/MEJORAS-METODO.md` y en `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md`.
- **Si un caso cerrado es mejor o peor que uno abierto.** D13 dice qué se puede auditar, medir, forkear y conservar. No dice qué funciona. Y los dos cerrados no están peor evaluados: están **menos** evaluados, que es distinto.

---

## Fuentes

- [R10] GitHub Spec Kit — ciclo por feature, escalera de complejidad, modelos de persistencia, ecosistema de extensiones.
- [R37] obra/superpowers — skills de método, router de tres caminos, «rulings, not stalls».
- [R38] Fission-AI/OpenSpec — capacidades y cambios, entrega por CLI, *stores* multi-repo.
- [R39] mberliner/sdd-first — siembra y descarte, modo `none`, propagación a derivados. **Mismo autor que este repositorio.**
- [R44] Kiro (Amazon Web Services) — IDE con el método adentro, EARS, `Quick Spec` sin compuertas. Producto cerrado.
- [R46] Tessl — `.spec.md` con test por capacidad, `@generate` / `@describe`, *Spec Registry*. Producto cerrado, *Framework* en beta cerrada.
- [R20] Martin Fowler — la taxonomía de tres niveles y la única observación de primera mano sobre regeneración desde spec.
- [R47] Hilos públicos de práctica en Hacker News — reportes de primera mano, con handle, sobre las cuatro implementaciones que alguien pudo usar. **Autoseleccionados; no son medición.**
- [R48] Discusiones y trackers de los propios proyectos — la objeción más votada de Spec Kit y la de precio de Kiro.
- [R49] API de GitHub, 2026-09-05 — estrellas, forks, watchers e issues abiertas. **Atención acumulada, no uso.**
- [R50] The Register e InfoWorld — cupos por demanda e incidente de facturación de Kiro, con la respuesta de AWS.

---

[SDD-Check]
- Spec leida: SI, y **registrada antes de escribir** el 2026-09-05, mas fila en la Tabla SSOT; **enmendada el mismo dia** al corregir el criterio de poblacion: `proposito` pasa de «adoptable» a «que alguien pueda evaluar o adoptar», `incluye` sube de doce a catorce dimensiones y suma la distincion entre perder la herramienta y perder los artefactos, y `validacion` suma tres casillas, entre ellas que la apertura y la disponibilidad **nunca** se usen para admitir o excluir. **Enmendada por segunda vez el 2026-09-05** al agregar D15 (uso y reputacion en redes) a pedido del usuario: `proposito` suma la reputacion reportada por terceros, `incluye` sube de catorce a quince dimensiones y suma un bullet propio para D15 con sus tres canales y sus sesgos, y `validacion` suma tres casillas sobre clase de evidencia, procedencia de las metricas y lectura de la ausencia de reportes. **Enmendada por tercera vez el 2026-09-05** al agregar la seccion de paradigmas, tambien a pedido: `proposito` suma el paradigma derivado, `incluye` suma un bullet propio con su frontera contra `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, `excluye` explicita que la seccion **no es** lectura cruzada, y `validacion` suma dos casillas —derivacion sin fuente nueva, y la lista declarada como no-particion—
- Incluye/Excluye verificado: SI — D15 y la seccion de paradigmas se agregaron a la spec **antes** de escribirse en el documento, y el usuario eligio explicitamente este documento como destino de los paradigmas frente a `CONVERGENCIA-IMPLEMENTACIONES-SDD.md` y frente a un documento nuevo; no se emite veredicto de convergencia (remitido a su SSOT), no se reproduce la caracterizacion individual completa de ningun caso, no se toma ninguna decision de adopcion para este repositorio
- Validaciones aplicadas: **D13 (apertura) y D14 (disponibilidad) son dimensiones y no filtros**, y la seccion 1 registra por escrito que la version anterior las usaba como filtro y por que estaba mal; los dos casos cerrados declaran que artefactos quedan en el repositorio del usuario, para no confundir perder la herramienta con perder el trabajo; en los casos sin clon, D9 y D10 se declaran **no medibles** en vez de completarse con datos no comparables; una afirmacion propia de la version anterior —que la salida de Kiro era «la mas cara de las cinco»— se corrige en su lugar y con nota, en vez de reescribirse en silencio; las quince dimensiones estan fechadas y su procedencia declarada, **incluida la advertencia de que NO son anteriores a la lectura de los casos** y por que eso pesa distinto que en convergencia; cada afirmacion lleva `[declarado]` o `[derivado]` y ninguna se presenta como medida; los datos de D9, D10 y D11 salen de `git` sobre los clones vendored con la ventana declarada (90 dias desde 2026-06-07), no de la documentacion de las fuentes; la reserva de procedencia de [R39] esta escrita dos veces —en la poblacion y encabezando su ficha— y su factor de bus 1 figura en la tabla y en la ficha; las tres citas de consecuencias de Spec Kit son textuales; **D15 introduce una tercera marca, `[reportado]`, distinta de `[declarado]` y `[derivado]`**, y su seccion abre declarando que no mide nada, que sus tres canales tienen sesgos conocidos y opuestos, y que ninguna cita dice que proporcion de usuarios piensa que; las metricas de atencion salen de la API de GitHub con fecha y comando declarados ([R49]) y se declaran atencion y no uso; cada cita de practica lleva el handle de quien la escribio y su [Rxx]; la ausencia total de reportes sobre sdd-first se escribe sin atenuantes y la de Tessl se explica por D14; **la seccion 5 no introduce ninguna fuente ni dato nuevo** —cada paradigma se deriva de D1, D2, D3, D4, D7 y D8, ya enunciadas— y cierra con tres advertencias: no es juicio de calidad, no es una particion porque Superpowers es ortogonal a los otros cinco, y no es veredicto de convergencia; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: este documento (alta el 2026-09-05; incorporacion de Kiro y de Tessl, y alta de D15, el mismo dia), `../SPECS_REGISTRY.md` (spec nueva mas fila en la Tabla SSOT, enmendada dos veces) y `../REFERENCIAS.md` (altas [R47] a [R50])
- Derivados a revisar: `CONVERGENCIA-IMPLEMENTACIONES-SDD.md` — **no modificado**, pero la seccion 5 corre paralela a su materia y declara su frontera; si alguna vez esa frontera se borra, se borra alli y no aca. Ninguno mas registrado todavia. Señalados sin modificar: `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md`, cuya comparacion adoptar-contra-portar se hizo sobre un snapshot donde el ecosistema del 1.0 no existia, y `../comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md`, que posee la estadistica de adopcion que este documento no toca
- Cobertura: completa — las quince dimensiones tienen fila en la tabla resumen, las catorce primeras desarrollo en las seis fichas y D15 seccion propia (4 quinquies) con los seis casos, la seccion 4 quater desarrolla que decide la apertura en la practica, la seccion 5 deriva un paradigma por caso sin introducir fuente nueva, y la seccion 7 enumera explicitamente lo que queda fuera del alcance de lo afirmable
- Deuda arrastrada: **D15 no tiene ni una sola fuente con poblacion definida**: son metricas de atencion y reportes autoseleccionados, y no hay forma de subir esa clase de evidencia sin un instrumento propio, que no existe; los reportes recogidos son los que aparecieron en la busqueda del 2026-09-05, sin criterio de exhaustividad declarado, asi que **el conjunto no es reproducible tal cual**; sobre Tessl, el blog oficial consultado ese dia no anuncia disponibilidad general del *Framework* ni la desmiente, de modo que su D14 queda como estaba; **los dos casos cerrados tienen D9 y D10 no medibles**, y eso no tiene remedio mientras no publiquen repositorio; el rasgo principal de Tessl —la regeneracion— se conoce **por [R20]** y no por la fuente; el *Framework* de Tessl sigue en beta cerrada, asi que su ficha describe algo que hoy no se puede probar. **Kiro entra con una asimetria de evidencia que no tiene remedio** —producto cerrado, sin clon, sin conteos de `git`— y sus tres dimensiones de madurez, actividad y licencia se responden en prosa y no con datos comparables; **el ecosistema del 1.0 de Spec Kit sigue sin caracterizar en `ANALISIS-SPEC-KIT.md`**, y acá entra solo por su efecto practico (165 extensiones de comunidad, modelo de confianza), no como caracterizacion; ninguna fuente se corrio, asi que D6, D7 y D8 son lectura de mecanismo y no experiencia de uso. Sigue abierto: M-40 sin decidir, M-41 sin escribir, M-42 en Propuesta, y la decision sobre instrumento v2 de convergencia
- Riesgos/reservas: **la seccion 5 es la que mas cerca pasa de un SSOT ajeno**: caracterizar seis casos con un mismo eje se parece a leerlos cruzados, y lo que la separa de `CONVERGENCIA-IMPLEMENTACIONES-SDD.md` es una restriccion declarada —no afirmar convergencia, derivacion ni linaje— que ningun verificador comprueba; **D15 es la dimension mas facil de leer mal de todo el documento** —un numero grande de estrellas invita a leerse como calidad, y la seccion lo niega tres veces, en su apertura, en su cierre y en la seccion 7—; la seleccion de citas la hizo quien escribe, sobre lo que devolvio la busqueda, y aunque se incluyeron reportes de los dos signos para cada caso con reportes, no hay garantia de balance; el hallazgo de que la objecion recurrente coincide con el modo de falla `[derivado]` es **interesante y debil a la vez**, porque quien leyo los mecanismos y quien selecciono las citas es la misma persona y la coincidencia puede ser de sesgo de confirmacion; la poblacion tiene ahora seis casos con **tres clases de evidencia distintas** —cuatro clones leidos, uno de documentacion de producto cerrado, y uno de documentacion mas un tercero—, y las fichas de los dos cerrados lo declaran arriba de todo, para que nadie compare sus filas como si fueran del mismo tipo; el instrumento no es anterior a la lectura de los casos y eso esta declarado en la seccion 2 con su mitigacion, que es discutible; dos de las cuatro fuentes tienen interes comercial y una es del mismo autor que este repositorio; los conteos de actividad miden movimiento, no calidad ni idoneidad, y un proyecto con 97 autores en 90 dias no es por eso mejor que uno con 17; la seccion 6 es la mas facil de leer como recomendacion y es la que menos evidencia tiene, por lo que declara dos veces que no ordena por calidad
