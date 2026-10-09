# Análisis: Tessl como método, y el único caso que regenera

Fecha: 2026-09-05.
Fuente: Tessl, blog y documentación oficiales consultados el 2026-09-05 [R46]; la regeneración y su no-determinismo, verificados en [R20].
Alcance: Línea B (software).

> **Clase de evidencia.** Igual que Kiro [R44], Tessl **no tiene código que clonar y no puede tenerlo**. Y va un paso más allá: su *Framework* está en **beta cerrada**, así que ni siquiera es instalable libremente. Todo rasgo se cita de documentación oficial o de un tercero identificado. Nada se leyó en código, nada se corrió.

---

## Por qué se incorpora ahora

Completa la deuda que `CONVERGENCIA-IMPLEMENTACIONES-SDD.md` arrastra desde el 2026-08-02: «Kiro y Tessl, nombrados en [R20], siguen sin pasar por el filtro de procedencia y sin alta en ningún backlog». Kiro se leyó el 2026-09-05; con esto la deuda queda saldada entera.

---

## Procedencia

| Hito | Fecha | Verificable en |
|---|---|---|
| Anuncio de productos | **2025-09-16** | Blog oficial [R46] |
| Nota de lanzamiento | **2025-09-23** | Blog oficial [R46] |

Por fecha de **producto público** es el más reciente de los cinco casos externos: posterior a Kiro (2025-07-14), OpenSpec (2025-08-05) y Spec Kit (2025-08-21). La empresa y su discurso son anteriores al producto, pero la anterioridad de un discurso no se puede fechar con la precisión que el filtro exige, así que no se usa.

**Consecuencia para el filtro**: las fechas no descartan que Tessl haya conocido a los otros tres al construir sus productos. Y a diferencia de Kiro, acá no hay una anterioridad que proteger. Como con los demás, establecer difusión exigiría marcadores, no cronología, y ese trabajo no está hecho.

**No toma columna** en la tabla de veredictos de convergencia, por la misma razón que Kiro: clase de evidencia. Las ocho filas se contestaron leyendo archivos.

---

## El método

**El problema que declara.** Los agentes son potentes y poco fiables: empiezan a codificar antes de tiempo, alucinan APIs, mezclan versiones y rompen lo que ya andaba. La respuesta es poner la spec —no el prompt, no el código— como lo que persiste. Textual [R46]: «These instructions live in the codebase as **long-term memory**, guiding agents as the app evolves and pairing with tests to enforce guardrails so existing functionality isn't broken».

**Anatomía de la spec** [R46] (`docs.tessl.io`, extensión `.spec.md`), tres partes:

1. **Descripción** del componente que la spec representa.
2. **Capacidades en lenguaje natural, cada una con su test enlazado.** Es el rasgo estructural distintivo: la unidad de la spec no es un requisito, es un par capacidad-verificador.
3. **API pública**, con las interfaces que el componente expone al resto del código.

**Dos directivas que cambian el modo de operación** [R46]:

| Directiva | Qué hace | Dirección |
|---|---|---|
| `@generate` | El código se genera **desde** la spec | spec → código |
| `@describe` | La spec **documenta** código existente en vez de generarlo | código → spec |

Esa pareja es un mecanismo de adopción en brownfield que ninguno de los otros cuatro tiene en esta forma: la misma herramienta sirve para levantar specs de lo que ya existe y para generar lo que todavía no.

**El Spec Registry** [R46], en beta abierta: «more than 10,000 pre-built specs» de librerías open source, orientadas a que el agente use bien una API y no invente versiones. Los equipos pueden además publicar sus propias *usage specs* internas como paquetes instalables.

Es un rasgo sin equivalente en el corpus, y conviene nombrarlo con precisión: los otros cuatro distribuyen **método** (comandos, skills, plantillas, adaptadores); Tessl distribuye **specs como paquete**. Es la spec tratada como dependencia, con registro y versión.

---

## Lo que lo separa de los otros cuatro: regenera

Los otros cuatro casos del corpus **no regeneran nada**. Spec Kit enuncia la «Power Inversion» —la spec como artefacto primario y el código como su derivado— pero su documentación de referencia declara que no impone ningún modelo de persistencia (`ANALISIS-SPEC-KIT.md`, C6). Superpowers no regenera y así está caracterizado. OpenSpec fusiona deltas en la spec vigente, que es propagación, no generación. Kiro sincroniza en las dos direcciones, sin regenerar.

Tessl sí. Verificado en [R20], no en la documentación de la fuente:

- «Running `tessl build` for this spec **generates the corresponding JavaScript code file**».
- Los archivos generados llevan el marcador `// GENERATED FROM SPEC - DO NOT EDIT`.
- Y su ubicación en la taxonomía, textual: «**Tessl is the only one of these three tools that explicitly aspires to a spec-anchored approach, and is even exploring the spec-as-source level of SDD**».

En la taxonomía de [R20] —la misma que [R10] cita en `spec-persistence.md`— eso lo pone en el único caso del corpus que se acerca a **spec-as-source**: «the spec is the main source file over time, and only the spec is edited by the human».

### Y un tercero identificado reporta no-determinismo

El mismo autor de [R20] corrió la regeneración y observó, textual: «even at this low abstraction level I have seen the **non-determinism** in action though, when I generated code multiple times from the same spec».

**Qué estatuto tiene esto y qué no.** Es la observación de un practicante identificado, en su propio texto, sin diseño experimental, sin repeticiones declaradas y sin criterio de medida. **No es una medición** y MUST NOT usarse como tal. Lo que sí es: la única evidencia empírica de terceros que este corpus tiene sobre el comportamiento de una regeneración spec → código.

---

## Conclusiones para Línea B

### C1. La posición fuerte del corpus deja de ser retórica y pasa a tener un mecanismo

`ANALISIS-SPEC-KIT.md` C3 sostiene que la «Power Inversion» es «una posición más fuerte que la nuestra», y su actualización del 2026-09-05 (C6) la matizó: el manifiesto de Spec Kit afirma la inversión y su referencia declara que el toolkit no impone ninguna persistencia. Tessl cierra ese hueco desde afuera: **la posición fuerte existe, y no es la de Spec Kit — es la de Tessl**, que efectivamente genera código desde la spec y lo marca como no editable.

Eso no valida la posición; la vuelve observable. **Lectura**, y una precisión para C3: al citar «la posición más fuerte» conviene nombrar a quién se le atribuye, porque la fuente que la enuncia y la que la ejerce no son la misma.

### C2. La spec como dependencia instalable es un eje que el instrumento no mira

Un registro de más de 10.000 specs de uso, versionadas y publicables por terceros, no encaja en la fila 8 de convergencia («personalización»), que trata de cómo se extiende el método. Acá lo que se distribuye es **contenido de spec**, no método. **Dimensión a registrar fuera del instrumento** en `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, sin veredicto: un solo caso la ejerce.

### C3. Hay una observación externa sobre regeneración, y su destino es el backlog — no B-07

B-07 midió regenerabilidad y está **cerrado**. Este documento MUST NOT reinterpretarlo, y no lo hace: no toca su hipótesis, su resultado ni su criterio de éxito (Principio V).

Lo que corresponde es otra cosa: existe ahora una observación de terceros sobre el no-determinismo de una regeneración spec → código, en una herramienta que regenera de verdad, y este repositorio no tiene ningún ítem que la recoja. **Candidata a alta en `../../agenda/BACKLOG-INVESTIGACION.md`**, formulada como pregunta nueva y con el recaudo de que la observación disponible no es una medición. No se da de alta acá: plantearla bien es trabajo propio, y darla de alta a medias es peor que no darla.

### C4. Lo que NO se puede hacer con esta fuente

- **Leerla con el instrumento v1.** Misma razón que Kiro, agravada: el Framework está en beta cerrada.
- **Contarla como evidencia de efectividad.** No reporta ninguna medición propia.
- **Tratar el marcador `// GENERATED FROM SPEC - DO NOT EDIT` como práctica verificada.** Sale de [R20], de una corrida de un practicante, no de leer la herramienta.

---

[SDD-Check]
- Spec leida: SI, y **registrada antes de escribir** (`../../SPECS_REGISTRY.md` -> `software/analisis/ANALISIS-TESSL.md`)
- Incluye/Excluye verificado: SI — no se emite veredicto de convergencia (la propagacion va al SSOT, señalada abajo), no se toca la orientacion practica, no se re-analiza ninguna otra implementacion, y **no se reformula B-07 en ningun punto**
- Validaciones aplicadas: la clase de evidencia encabeza el documento y se repite en C4; cada rasgo declara si sale de [R46] o de [R20], y los tres hechos que sostienen la seccion de regeneracion —`tessl build`, el marcador de archivo generado y la ubicacion en la taxonomia— se atribuyen a [R20] y **no** a la fuente, porque no estan en la documentacion consultada; la observacion de no-determinismo lleva su estatuto escrito en un parrafo propio, con lo que es y lo que no; las fechas de lanzamiento se verificaron en el blog de la fuente; la fuente no reporta medicion y eso queda dicho dos veces; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: ninguno por este documento (`ssot_level: operativo`). `../../REFERENCIAS.md` recibio el alta de [R46] y la anotacion de [R20], que pasa a ser fuente de carga para la taxonomia y para la observacion de regeneracion
- Derivados a revisar: **`software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md` requiere propagacion** — fila de procedencia, cierre de la deuda «Kiro y Tessl», y la dimension de C2 registrada fuera del instrumento. **`software/analisis/ANALISIS-SPEC-KIT.md` C3 queda señalado** por la precision de C1. `software/ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md`: Tessl entra a la poblacion con una salvedad mas dura que la de Kiro, porque el Framework esta en **beta cerrada** y por lo tanto no es adoptable hoy
- Cobertura: **incompleta y declarada** — C1, C2 y C3 tienen destino; la propagacion a los tres documentos señalados **queda sin ejecutar** en esta entrega, y el item de backlog de C3 **no se da de alta**
- Deuda arrastrada: **la pregunta de investigacion de C3 queda sin item**; ninguna afirmacion sobre Tessl es verificable en codigo y no lo sera mientras el Framework siga en beta cerrada; la regeneracion, que es el rasgo por el que este caso importa, se conoce **por un tercero** y no por la fuente. Sigue abierto: M-40, M-41, M-42, el ecosistema del 1.0 de Spec Kit sin caracterizar, e instrumento v2 sin decidir
- Riesgos/reservas: es el caso peor verificado del corpus —producto en beta cerrada, sin clon, y su rasgo distintivo conocido por un tercero—; es una empresa comercial con financiamiento y un producto que vender, y su documentacion cumple tambien esa funcion; y la tentacion de leer a Tessl como confirmacion de la tesis de regenerabilidad de este proyecto es exactamente el error que C3 evita, porque B-07 ya midio y esta cerrado

---

## Actualización: la documentación pública ya no describe el producto analizado (2026-10-09)

Re-consulta de [R46] del 2026-10-09: el índice completo de la documentación (`docs.tessl.io/llms.txt`) y las páginas que indexa, leídas en su versión markdown y no en un resumen. La clase de evidencia no cambia: todo es lo que la fuente declara. Lo que cambia es **qué** declara, y lo de arriba sigue siendo correcto para su fecha.

### Qué dejó de documentarse

- **El flujo de specs.** Ninguna de las entradas del índice menciona specs, `.spec.md`, `@generate`, `@describe` ni `tessl build`. La fuente se presenta como «an open platform for managing agentic development across your organization», con registro y gestor de *skills* y *plugins* como primer componente.
- **Las specs de uso de librerías**, que sostenían C2. La guía de migración de *tiles* a *plugins* retira dos campos: `docs` y `describes`. Del segundo dice que «declared that a tile described a specific versioned package (e.g. a Go library)… as Docs have not been carried forward, neither has Describes» (`docs.tessl.io/use/tile-to-plugin-migration.md`) [R46].

**Qué se puede afirmar y qué no.** Se puede afirmar que la documentación pública ya no describe el *Framework* de specs, y que el mecanismo con el que el registro distribuía contenido de spec no pasó al formato actual. **No** se puede afirmar que el *Framework* se haya discontinuado: estaba en beta cerrada, y su ausencia de la documentación pública es compatible con varias explicaciones que desde afuera no se distinguen. C1 no cambia de estatuto: la regeneración se conocía por [R20] y se sigue conociendo sólo por [R20]. **C2 pierde su mecanismo en el formato vigente**; queda como descripción del producto al 2026-09-05.

### Lo que documenta hoy para las reglas transversales

Todo con [R46], de la página que se nombra:

- **Rules.** «An always-on convention the agent follows without being asked. A plain Markdown file in `rules/`, no frontmatter» (`creating-skills-and-plugins/create-a-plugin.md`). Se distribuyen dentro de un plugin y Tessl las instala «into each agent's native format». La misma guía de migración registra que `steering` se aceptaba como alias de `rules`.
- **Rules del propio repositorio.** Un plugin puede vivir en el repositorio y referenciarse desde `tessl.json` con una fuente `file:`; quien clona y corre `tessl install` recibe esas reglas (`distribute/repository-plugins.md`). El ejemplo de monorepo pone las de frontend en una carpeta que comenta como «UI standards».
- **Verifiers.** «A verifier is an LLM-as-judge check that compares committed files with an invariant stored as JSON». La fuente los presenta como pareja de las reglas: «a rule teaches the expected pattern, and a verifier catches changes that do not follow it». La severidad se fija en `tessl.json`, y en CI «`warn` findings remain advisory and `error` findings exit non-zero, so they can block a pull request» (`codifying-and-enforcing-your-skill-standards/verifiers-overview.md`).
- **Políticas.** De organización, workspace y proyecto, sobre la calidad y la seguridad de las skills: «lower levels only tighten, never relax, and when levels disagree the strictest one wins» (`tutorials/codifying-and-enforcing-skill-standards.md`).

### C5. El caso que ataba la spec a su test ahora documenta otra pareja: regla y juez

Lo que distinguía a Tessl en el corpus era la **correspondencia**: cada capacidad del `.spec.md` llevaba su test enlazado. Lo que documenta hoy es una pareja distinta: una regla que el agente recibe siempre y un verificador que juzga el resultado commiteado. Tiene dos diferencias que importan. El juez es un modelo, no un test, así que el veredicto no es determinista. Y lo que se compara es el código contra un invariante que el equipo escribió, no contra una spec de la que el código derive. **Lectura**, sin consecuencia sobre lo que este documento dijo al 2026-09-05. La comparación con los otros casos no se hace acá: vive en `../ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md`.

---

[SDD-Check] — actualizacion 2026-10-09
- Spec leida: SI, y **enmendada antes de escribir**: `incluye` admite el estado de la documentacion publica en cada re-consulta fechada, con la advertencia de que una ausencia no prueba discontinuidad
- Incluye/Excluye verificado: SI — no se emite orientacion practica ni veredicto de convergencia; no se re-analiza ninguna otra implementacion; B-07 no se toca
- Validaciones aplicadas: el indice `llms.txt` se descargo entero (108 lineas) y se busco en el literalmente, sin resumen automatico; cada cita es textual de la pagina markdown que se nombra; la ausencia del *Framework* se declara como ausencia en la documentacion y **no** como discontinuidad; lo que el documento dijo al 2026-09-05 no se reescribe, y C2 se declara sin mecanismo en el formato vigente en vez de borrarse; la clase de evidencia se repite en la apertura; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: ninguno por este documento (`ssot_level: operativo`). `../../REFERENCIAS.md` suma a [R46] la re-consulta
- Derivados a revisar: `../ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md` — D16 de Tessl se escribe desde esta seccion, en la misma entrega; su ficha sigue describiendo el producto del 2026-09-05 en D4, D5 y D14, y eso queda como deuda alli. Señalado sin modificar: `../CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, que registro la dimension de C2 fuera del instrumento
- Cobertura: completa para lo que la documentacion publica dice hoy de reglas, verificadores y politicas
- Deuda arrastrada: la de este documento sigue donde estaba; se suma que el estado del *Framework* de specs es desconocido y no se puede averiguar desde la documentacion publica
- Riesgos/reservas: la documentacion no tiene version que la ancle, asi que todo vale para la fecha de consulta; la fuente describe una plataforma comercial y su documentacion cumple tambien una funcion de venta; nada se corrio

---

## Actualización: cuándo cambió el producto, y una corrección a este documento (2026-10-09)

La sección anterior registró que la documentación ya no describe el producto, sin fecharlo. Fecharlo exigió leer el changelog de la CLI —publicado dentro del corpus completo de la documentación, `docs.tessl.io/llms-full.txt`— y cruzarlo con las fechas de publicación del paquete `@tessl/cli` en npm [R46].

### Cronología

| Fecha | Hecho | Fuente |
|---|---|---|
| 2025-09-16 y 2025-09-23 | Lanzamiento: *Spec Registry* en beta abierta, *Framework* en beta cerrada | Blog |
| 2025-10-17 | CLI 0.28.0, la última que incluye el *Framework* | npm; changelog |
| **2025-11-14** | CLI 0.50.3: «pausing work on the Tessl Framework to concentrate on our registry functionality and agent integration»; «The Framework functionality is no longer included. If you need the full framework features, v0.28.0 remains available (though development is paused)» | npm; changelog |
| 2025-12-05 | Se crea el plugin de SDD del registro, `tessl-labs/spec-driven-development` | Su repositorio |
| 2026-01-29 | «Announcing skills on Tessl: the package manager for agent skills» | Blog |
| 2026-05-29 | CLI 0.81.0: «Tiles are now Plugins» | npm; changelog |

**La fecha del cambio es el 2025-11-14.** Lo que vino después —skills, plugins, verificadores— es la plataforma nueva creciendo; el corte con el producto que analizó este documento está en esa versión de la CLI.

### Corrección: el estado que este documento dio al *Framework* ya era falso en su fecha

Este análisis se escribió el 2026-09-05 y dice, en su encabezado y en C4, que el *Framework* «está en beta cerrada». A esa fecha llevaba casi diez meses pausado y fuera de la CLI. El dato salía del blog de septiembre de 2025 y no se contrastó con el estado del producto al momento de escribir. **Se corrige acá, sin reescribir arriba**: lo de arriba describe el producto que la fuente anunció, no el que existía al consultarlo. La consecuencia de método es la que el repositorio ya conoce para los clones —anclar la versión antes de leer—, y acá se manifiesta en una fuente sin clon: una fecha de anuncio no es una fecha de vigencia.

La regeneración que sostiene C1 sigue verificada por [R20], que la observó en 2025, con el *Framework* activo. Lo que cambia es su alcance: describe un producto pausado, no el actual.

### El flujo de specs sobrevive como plugin

El registro publica `tessl-labs/spec-driven-development` (versión 2.0.1 al consultarlo), con código abierto bajo MIT en `spec-driven-development-tile` [R46], leído en el commit `b8fdff70` (2026-03-30). Es **método entregado como plugin**, no motor:

- Una regla siempre activa, «Never begin implementation without an approved spec», con excepciones declaradas para cambios triviales y para urgencias, que exigen spec retroactiva (`spec-driven-development-tile:rules/spec-before-code.md`).
- Specs en `specs/`, con extensión `.spec.md`, *front matter* con `targets` —los archivos que la spec describe— y enlaces `[@test]` a los tests que verifican cada requisito (`spec-driven-development-tile:docs/spec-format.md`). Es el formato de la anatomía original, sin `@generate` ni `@describe`.
- Un script que comprueba que los enlaces `[@test]` y los `targets` apunten a archivos que existen (`spec-driven-development-tile:scripts/check-spec-links.sh`), y skills para escribir specs, verificarlas contra el código y revisar el trabajo.
- Nueve escenarios de evaluación, uno de ellos para que un cambio trivial **no** dispare el flujo completo.

**Lectura.** El par capacidad-test que distinguía a Tessl se conserva como formato, pero cambia lo que lo sostiene: antes, un motor que generaba código desde la spec; ahora, una regla que el agente sigue y un script que comprueba que los enlaces existan, no que el test pase ni que el código cumpla la spec. C5 queda así: la pareja documentada es regla y juez para las reglas del proyecto, y regla y verificador de enlaces para las specs.

---

[SDD-Check] — cronologia 2026-10-09
- Spec leida: SI (spec enmendada en la entrega anterior del mismo dia; la cronologia y el plugin caen en «el estado de la documentacion publica en cada re-consulta fechada… y los mecanismos que la fuente documenta en su lugar»)
- Incluye/Excluye verificado: SI — no se emite orientacion practica; no se toca B-07; la correccion se escribe como correccion y no reescribe el cuerpo del 2026-09-05
- Validaciones aplicadas: cada fecha de la cronologia sale de la publicacion en npm (`registry.npmjs.org/@tessl/cli`, campo `time`), del post del blog o de la API de GitHub, y cada cita del changelog es textual; el plugin se leyo en su repositorio en un commit fijado; dos fuentes de terceros que señalaban la pausa —un perfil de ai.engineer y la reseña de un producto competidor— no se citan, porque la fuente oficial lo dice; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: ninguno por este documento. `../../REFERENCIAS.md` suma a [R46] la cronologia y la correccion
- Derivados a revisar: `../ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md` — la ficha de Tessl se rehace con el producto actual en la misma entrega. Señalado sin modificar: `../CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, cuya mencion de Tessl describe el producto anunciado
- Cobertura: completa para la fecha del cambio y para el flujo de specs que sobrevive
- Deuda arrastrada: ninguna nueva en este documento
- Riesgos/reservas: el changelog no fecha sus entradas y las fechas salen de npm, que registra la publicacion del paquete y no el anuncio; «pausa» es la palabra de la fuente, y no se sabe si el *Framework* volvera
