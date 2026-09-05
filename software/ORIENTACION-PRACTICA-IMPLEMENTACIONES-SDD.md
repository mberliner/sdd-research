# Orientación práctica de las implementaciones SDD adoptables

Fecha: 2026-09-05. Línea B (software).

Pregunta que origina el documento: *si quisiera usar una de estas herramientas, ¿para qué sirve cada una, qué me pasa si mi proyecto es grande o chico, y qué consecuencias tiene configurarla de un modo u otro?*

> **Advertencia que condiciona todo lo que sigue.** **Ninguna de las cuatro fuentes reporta medición alguna** — ni interna ni externa — sobre su idoneidad para ningún escenario. Este documento dice para qué está **declaradamente** orientada cada una y qué se **deriva de sus mecanismos verificables**. No dice cuál funciona mejor, ni en proyectos grandes ni en chicos, porque nadie lo midió. Cada afirmación de abajo declara cuál de las dos cosas es: `[declarado]` o `[derivado]`. Un `[derivado]` es una consecuencia estructural de un mecanismo que se puede leer en el clon, no un resultado.

---

## 1. Población: por qué no es la misma que la de convergencia

`CONVERGENCIA-IMPLEMENTACIONES-SDD.md` lee cuatro **linajes** y pregunta de dónde vino cada método. Acá la pregunta es otra —¿lo podés instalar y usar?— y la población se invierte en dos casos:

| Caso | En convergencia | Acá | Motivo |
|---|---|---|---|
| Spec Kit [R10] | Sí | **Sí** | — |
| OpenSpec [R38] | Sí | **Sí** | — |
| Superpowers [R37] | Sí | **Sí** | — |
| Proyecto testigo | Sí, cuarto linaje | **No** | No es adoptable por terceros: es un proyecto testigo privado |
| sdd-first [R39] | **No** suma linaje | **Sí** | Es un kit instalable. Su procedencia no importa para decidir si sirve; importa que exista y se pueda usar |
| Kiro [R44] | **No** toma columna | **Sí, con asterisco** | Es adoptable —se instala y se usa— pero es producto cerrado, y eso cambia qué se puede afirmar. Ficha aparte en §4 bis |

**Reserva sobre sdd-first, que MUST leerse antes de su ficha.** Es del mismo autor que este repositorio [R39]. Todo juicio favorable sobre él en un documento escrito acá es autocorrelación por construcción, y por eso su ficha se limita a hechos verificables del clon —conteos, fechas, mecanismos— sin ninguna valoración comparativa. Su factor de bus está escrito en la ficha y en la tabla.

---

## 2. Las doce dimensiones y su procedencia

Fijadas el **2026-09-05**. Su origen es la pregunta del usuario que encargó el documento —orientación de uso, comportamiento por tamaño, consecuencias de las variantes, características particulares, más madurez, actividad, licencia y soporte—, formulada **antes** de que se diseñara el instrumento.

**Límite honesto, y es distinto del de convergencia.** Este instrumento **no es anterior a la lectura de los casos**: los cuatro clones se releyeron los días previos. En `CONVERGENCIA` eso sería descalificante, porque con libertad para elegir qué comparar la convergencia se fabrica. Acá el riesgo es otro y menor —elegir dimensiones donde una herramienta luzca—, y la mitigación es la procedencia: las doce salen de lo que preguntó quien va a decidir, no de lo que los casos ofrecen. Quien no acepte esa mitigación debe leer la tabla como descriptiva y no como criterio de selección.

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

---

## 3. Tabla resumen

Los números de D9 a D11 salen de los clones vendored con `git`, no de la documentación de cada fuente. Corte: 2026-09-05; ventana de 90 días desde 2026-06-07.

| | **Spec Kit** [R10] | **OpenSpec** [R38] | **Superpowers** [R37] | **sdd-first** [R39] |
|---|---|---|---|---|
| **D1** Orientación | Feature nueva, ciclo completo spec→plan→tasks→código | Cambio sobre un sistema que ya existe, por capacidad | Metodología de trabajo del agente, no de specs | Sembrar gobernanza SDD dentro de otro proyecto |
| **D2** Objeto | Código | Código | El trabajo del agente | Código, o sólo gobernanza (modo `none`) |
| **D3** Unidad / tamaño | Carpeta por feature. Escalera **explícita de 4 opciones** cuando no entra en un ciclo | Capacidad durable + *change* como unidad de trabajo | Clasifica cada pedido en **spike / bounded / architectural** | Spec numerada con historias y FR por historia |
| **D4** Variantes | **Tres modelos de persistencia, con su riesgo declarado por la fuente** | *Schemas* forkeables; *stores* multi-repo (beta) | Tres caminos de ceremonia; harness elegible | Adaptador de lenguaje, o modo `none` |
| **D5** Configuración | 41 integraciones; **165 extensiones y 34 presets de comunidad** contra 4 y 2 oficiales | `openspec/config.yaml` + schemas forkeables | Plugins + adaptadores por harness | `.sdd/config.yaml`, todo generado desde ahí |
| **D6** Entorno | Python ≥3.11 + CLI | Node ≥20.19 + CLI | El harness; sin CLI propio | Python 3.11 + git |
| **D7** Entrada / salida | `specify init`; desinstalar y cambiar integración están documentados | `openspec init`; `openspec update` regenera | Plugin del harness; se quita como plugin | Se siembra **y el kit se descarta**; `sdd_update.py` propaga después |
| **D8** Modo de falla | La cadena de suministro de extensiones | No invocar el CLI: sin comando no hay método | La skill no se dispara | El verificador que reporta OK sin verificar |
| **D9** Madurez | 2025-08-21; 1927 commits; **188 releases**; v1.0.5.dev0 | 2025-08-05; 828 commits; 48 releases; v1.12.0 | 2025-10-09; 681 commits; 34 releases; v6.3.0 | **2026-08-01**; 143 commits; **0 releases** |
| **D10** Actividad 90d | 838 commits, **97 autores** | 226 commits, 54 autores | 240 commits, 17 autores | 143 commits, **1 autor** |
| **D11** Licencia | MIT | MIT | MIT | Apache 2.0 |
| **D12** Soporte | GitHub; 297 autores históricos | Fission AI (comercial); 111 autores | Prime Radiant (comercial); 47 autores | **Individual; factor de bus 1** |

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

> **Asterisco de población.** Kiro es **producto cerrado**: su repositorio público declara que no aloja el código del producto. Todo lo de abajo se cita de documentación oficial. Y **D9, D10 y D11 no se pueden calcular con `git`** como en los otros cuatro: no hay clon, no hay conteo de commits, ni de autores, ni de releases. Esa asimetría es en sí un dato práctico, y está al final de la ficha.

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

**Costo de entrada y de salida** `[derivado]`: la entrada es baja, porque no hay que instalar ni configurar un método sobre tu editor. La salida es la más cara de las cinco: **el método está atado al producto**. Los otros cuatro dejan archivos que sobreviven a la herramienta; acá el flujo, las compuertas y los hooks son la herramienta.

**Madurez, actividad, licencia y soporte** — y acá está la asimetría: anuncio del **2025-07-14**, lo que lo vuelve **el más antiguo del corpus**; respaldo de Amazon Web Services, el más grande de los cinco; documentación oficial extensa, tracker público de issues y material formativo propio en AWS Skill Builder. Pero **cerrado**: sin licencia abierta, sin historial auditable, sin conteo de contribuyentes, y sin posibilidad de forkearlo si el producto cambia de rumbo o de precio. Los otros cuatro son MIT o Apache 2.0 y se pueden leer entero.

**Rasgo sin equivalente**: que el método no se instala. Y su contracara exacta: que tampoco se puede llevar a otro lado.

---

## 5. Orientación por escenario

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
| Quiero el método sin instalar ni configurar nada | Viene dentro del IDE, sin scaffolding | Kiro, **cerrado** |
| Necesito poder auditar, forkear o llevarme el método | Código abierto y archivos que sobreviven a la herramienta | Los cuatro **menos** Kiro |
| Requisitos con una sintaxis formal y con nombre | EARS (`WHEN ... THE SYSTEM SHALL ...`) | Kiro |

Dos advertencias sobre esta tabla `[derivado]`:

- **Las filas no son excluyentes.** Superpowers gobierna el trabajo del agente y los otros tres gobiernan artefactos: combinarlo con cualquiera de ellos no es contradictorio, y la propia Spec Kit publica una extensión puente hacia él.
- **La columna «caso» no dice «el mejor».** Dice cuál tiene un mecanismo escrito para esa situación. Que exista el mecanismo no dice que funcione.
- **Kiro está peor verificado que los otros cuatro**, y no por casualidad: es el único cerrado. Sus filas salen de lo que declara su documentación; las de los demás, de leer archivos. Al comparar, esa asimetría corre en contra de Kiro en confianza y a favor en comodidad, y ninguna de las dos cosas se midió.

---

## 6. Lo que este documento no puede decir

- **Cuál funciona mejor.** Ninguna fuente reporta medición. Cuatro herramientas con mecanismos distintos para el mismo problema, y cero datos de desempeño comparado.
- **Si la orientación declarada se cumple.** Todo `[declarado]` es lo que la fuente dice de sí misma; dos de las cuatro tienen interés comercial y una es del mismo autor que este repositorio.
- **Cómo se comportan en un proyecto real.** Ninguna se corrió: las cuatro se leyeron de clones vendored.
- **Si convergen o divergen entre sí como método.** Eso vive en `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, se lee con otro instrumento y con otra población.
- **Qué le conviene a este repositorio.** Vive en `../agenda/MEJORAS-METODO.md` y en `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md`.

---

## Fuentes

- [R10] GitHub Spec Kit — ciclo por feature, escalera de complejidad, modelos de persistencia, ecosistema de extensiones.
- [R37] obra/superpowers — skills de método, router de tres caminos, «rulings, not stalls».
- [R38] Fission-AI/OpenSpec — capacidades y cambios, entrega por CLI, *stores* multi-repo.
- [R39] mberliner/sdd-first — siembra y descarte, modo `none`, propagación a derivados. **Mismo autor que este repositorio.**

---

[SDD-Check]
- Spec leida: SI, y **registrada antes de escribir** (`../SPECS_REGISTRY.md` -> `software/ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md`, mas fila en la Tabla SSOT)
- Incluye/Excluye verificado: SI — no se emite veredicto de convergencia (remitido a su SSOT), no se reproduce la caracterizacion individual completa de ningun caso, no se toma ninguna decision de adopcion para este repositorio, y el testigo queda fuera por no ser adoptable
- Validaciones aplicadas: las doce dimensiones estan fechadas y su procedencia declarada, **incluida la advertencia de que NO son anteriores a la lectura de los casos** y por que eso pesa distinto que en convergencia; cada afirmacion lleva `[declarado]` o `[derivado]` y ninguna se presenta como medida; los datos de D9, D10 y D11 salen de `git` sobre los clones vendored con la ventana declarada (90 dias desde 2026-06-07), no de la documentacion de las fuentes; la reserva de procedencia de [R39] esta escrita dos veces —en la poblacion y encabezando su ficha— y su factor de bus 1 figura en la tabla y en la ficha; las tres citas de consecuencias de Spec Kit son textuales; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: este documento (alta el 2026-09-05; incorporacion de Kiro el mismo dia) y `../SPECS_REGISTRY.md` (spec nueva mas fila en la Tabla SSOT)
- Derivados a revisar: ninguno registrado todavia. Señalados sin modificar: `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md`, cuya comparacion adoptar-contra-portar se hizo sobre un snapshot donde el ecosistema del 1.0 no existia, y `../comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md`, que posee la estadistica de adopcion que este documento no toca
- Cobertura: completa — las doce dimensiones tienen fila en la tabla resumen y desarrollo en las cuatro fichas, y la seccion 6 enumera explicitamente lo que queda fuera del alcance de lo afirmable
- Deuda arrastrada: **Kiro entra con una asimetria de evidencia que no tiene remedio** —producto cerrado, sin clon, sin conteos de `git`— y sus tres dimensiones de madurez, actividad y licencia se responden en prosa y no con datos comparables; **el ecosistema del 1.0 de Spec Kit sigue sin caracterizar en `ANALISIS-SPEC-KIT.md`**, y acá entra solo por su efecto practico (165 extensiones de comunidad, modelo de confianza), no como caracterizacion; ninguna fuente se corrio, asi que D6, D7 y D8 son lectura de mecanismo y no experiencia de uso. Sigue abierto: M-40 sin decidir, M-41 sin escribir, M-42 en Propuesta, y la decision sobre instrumento v2 de convergencia
- Riesgos/reservas: la poblacion tiene ahora cinco casos con **dos clases de evidencia distintas** —cuatro leidos en clones y uno leido en documentacion de producto—, y la ficha de Kiro lo declara arriba de todo para que nadie compare sus filas como si fueran del mismo tipo; el instrumento no es anterior a la lectura de los casos y eso esta declarado en la seccion 2 con su mitigacion, que es discutible; dos de las cuatro fuentes tienen interes comercial y una es del mismo autor que este repositorio; los conteos de actividad miden movimiento, no calidad ni idoneidad, y un proyecto con 97 autores en 90 dias no es por eso mejor que uno con 17; la seccion 5 es la mas facil de leer como recomendacion y es la que menos evidencia tiene, por lo que declara dos veces que no ordena por calidad
