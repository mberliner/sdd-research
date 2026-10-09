# Análisis: Kiro como método, y su lugar en el corpus

Fecha: 2026-09-05.
Fuente: Kiro (AWS), documentación y blog oficiales consultados el 2026-09-05 [R44]; un dato de ruta atribuido a [R45].
Alcance: Línea B (software).

> **Clase de evidencia, y hay que leerla antes que cualquier otra cosa.** Kiro es **producto cerrado**. Su repositorio público declara textualmente «The Kiro product source code is not hosted here» y aloja sólo issues y discusiones. **No hay código que clonar y no puede haberlo.** Todo lo que sigue se cita de documentación oficial: es lo que la fuente *dice* que hace, no lo que se leyó que hace. Los otros cuatro casos del corpus se caracterizaron leyendo archivos en un clon; este no. La diferencia no es de grado — cambia qué tipo de afirmación se puede sostener, y por eso este documento no emite ningún veredicto comparativo.

---

## Por qué se incorpora ahora

Kiro es una deuda declarada. `CONVERGENCIA-IMPLEMENTACIONES-SDD.md` dice desde el 2026-08-02 que la independencia de OpenSpec «está establecida frente a Spec Kit por fechas verificables, no frente a Kiro, anunciado el 2025-07-14 y ausente del corpus», y arrastra en su deuda que «Kiro y Tessl, nombrados en [R20], siguen sin pasar por el filtro de procedencia». `ANALISIS-OPENSPEC.md` declara el mismo hueco.

Se incorpora **como método**, que es lo único que la clase de evidencia permite.

---

## Procedencia: es el caso más antiguo del corpus

| Caso | Fecha pública más temprana | Verificable en |
|---|---|---|
| **Kiro** | **2025-07-14** (anuncio) | Post «Introducing Kiro» [R44] |
| OpenSpec | 2025-08-05 (primer commit) | Clon del repositorio |
| Spec Kit | 2025-08-21 (primer commit) | Clon del repositorio |
| Superpowers | 2025-10-09 (primer commit) | Clon del repositorio |
| sdd-first | 2026-08-01 (primer commit) | Clon del repositorio |

Kiro precede a OpenSpec por 22 días y a Spec Kit por 38.

**Qué deciden las fechas.** Descartan una sola dirección: Kiro **no** puede derivar de ningún otro caso del corpus, porque todos son posteriores. Esa dirección queda cerrada.

**Qué NO deciden, y es lo que importa.** No establecen que los otros deriven de Kiro. Anterioridad no es derivación. Y acá hay un elemento que corta en sentido contrario: la tríada **requisitos → diseño → tareas** es anterior a los cinco por décadas —es la secuencia de manual de ingeniería de software—, así que coincidir en ella no es marcador de difusión entre estos casos, del mismo modo que `WHEN/THEN` desciende de Gherkin [R07] y no de ninguno de ellos.

**Lo que sí cambia.** Hasta hoy `CONVERGENCIA` sostenía la independencia de OpenSpec frente a Spec Kit con fechas, y declaraba que frente a Kiro no estaba establecida. Ahora se sabe que Kiro es anterior a los dos: **la defensa por fecha no está disponible en esa dirección**, para ninguno de ellos. Eso no convierte la convergencia en difusión; retira un argumento y deja la pregunta abierta con más precisión que antes. La propagación de esto al SSOT se hace en `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, no acá.

---

## La tesis del método

El post fundacional plantea el problema como el salto de prototipo a producción, no como calidad de la generación:

> «prompt, prompt, prompt, and you have a working application. It's fun and feels like magic. But getting it to production requires more.» [R44]

Y sitúa las specs como el instrumento de ese salto: son «artifacts that prove useful anytime you need to think through a feature in-depth, refactor work that needs upfront planning, or when you want to understand the behavior of systems» [R44].

La tercera cláusula es la interesante: *entender el comportamiento de sistemas*. Coloca a la spec también del lado de la lectura de lo existente, no sólo de la construcción de lo nuevo.

---

## Anatomía declarada

**Tres artefactos por spec** [R44]: `requirements.md` (historias de usuario con criterios de aceptación), `design.md` (arquitectura técnica, diagramas de flujo de datos, interfaces, esquemas, endpoints) y `tasks.md` (plan de implementación en tareas discretas y rastreables). La documentación define la spec como «structured artifacts that formalize the development process for features and bug fixes».

**Ruta de los artefactos**: `.kiro/specs/<feature>/` — **atribuido a [R45]**, no a la documentación oficial, que no expone la ruta en las páginas consultadas.

**Requisitos en notación EARS** [R44]. Es el rasgo más distintivo del método: los criterios de aceptación siguen `WHEN <condición> THE SYSTEM SHALL <comportamiento>`, con `IF-THEN` reservado a condiciones de error y `WHEN` a las nominales. EARS es un estándar externo y nombrado de sintaxis de requisitos: Kiro no inventa un formato, adopta uno.

**Contexto de proyecto en `.kiro/steering/`** [R44]: archivos que capturan convenciones del codebase, compartidos entre todas las superficies del producto.

**Hooks de agente** [R44]: «event-driven automations that execute when you save or create files». Es enforcement por evento, no por compuerta de fase.

---

## Las variantes, y la escala de ceremonia

Kiro no ofrece un solo flujo, y las diferencias tienen consecuencia directa:

| Variante | Compuertas | Consecuencia |
|---|---|---|
| **Feature Spec**, *Requirements-First* | Sí, entre fases | Requisitos → diseño → tareas. El orden de manual |
| **Feature Spec**, *Design-First* | Sí, entre fases | Diseño → requisitos → tareas. Para cuando la forma técnica precede al enunciado |
| **Quick Spec** | **No** | «auto-generate[s] all three artifacts without approval gates» |
| **Quick Plan** | — | Variante liviana |

Esto convierte a Kiro en el **cuarto caso del corpus con escala de ceremonia explícita**, junto a Superpowers (spike / bounded / architectural), Spec Kit (la escalera de cuatro opciones de `complex-features.md`) y nuestro propio linaje (tres niveles de profundidad de spec, que `../../agenda/MEJORAS-METODO.md` M-37 midió sin usar). Con una diferencia de diseño que vale registrar: en Superpowers **la ceremonia escala y la compuerta de aprobación no**; en Kiro, `Quick Spec` **escala las dos** — menos artefacto y además sin compuertas.

Es la observación con más consecuencia de este análisis. La dimensión «la ceremonia escala con el tamaño del trabajo», registrada en `CONVERGENCIA` el 2026-09-05 como candidata a instrumento v2, pasa de tres casos a cuatro, y ahora tiene además **una divergencia interna de diseño** —si la compuerta escala junto con el artefacto— que es exactamente lo que vuelve informativa a una dimensión.

---

## Persistencia de la spec

La posición declarada es explícita y bidireccional:

> «Kiro's specs stay synced with your evolving codebase. Developers can author code and ask Kiro to update specs or manually update specs to refresh tasks.» [R44]

Situada en las taxonomías que este repositorio ya usa:

- En la de [R20]: **spec-anchored**, no *spec-as-source*. La spec sobrevive a la implementación y sirve para el cambio siguiente, pero el código no se regenera desde ella. La asignación sale de la declaración de la fuente, citada arriba. **Divergencia con el tercero, declarada el 2026-09-20:** [R20] reserva *anchored* a Tessl entre los tres casos que analiza, así que ubica a Kiro por debajo. Es lectura fundada de su autor, no medición, y no desplaza la declaración propia: quedan escritas las dos (regla en `../ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md` §5).
- En los modelos de persistencia de [R10] (`spec-persistence.md`): **flow-back**, porque las ediciones pueden empezar en cualquier artefacto y después se reconcilian. Y con eso hereda el riesgo que esa fuente le atribuye al modelo, «silent divergence».

Notable: Kiro es el único caso del corpus que declara la sincronización desde el código hacia la spec como camino previsto y soportado por la herramienta, en vez de como deriva a evitar.

---

## Conclusiones para Línea B

### C1. La escala de ceremonia pasa a cuatro casos, y gana una divergencia de diseño

Cuatro de los cinco casos escalan la ceremonia, con cuatro mecanismos distintos. Y no coinciden en lo que escala: Superpowers mantiene la compuerta fija por diseño explícito, Kiro la retira en su variante rápida. **Lectura** que refuerza la candidatura a instrumento v2 registrada en `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, y que le agrega el eje sobre el que la dimensión discriminaría.

### C2. EARS es un estándar externo nombrado, y eso separa a Kiro del resto

Los otros cuatro casos usan lenguaje normativo sin citar de dónde sale, o citándolo de pasada: Spec Kit usa `MUST` con RFC 2119 [R04], OpenSpec usa `SHALL` en el registro de ISO/IEC/IEEE 29148 [R03] sin citarla, Superpowers acuña el suyo, nuestro linaje usa `MUST` con [R04]. Kiro adopta **EARS**, que es una sintaxis de requisitos con nombre propio y reglas de patrón. Refuerza la fila 2 de convergencia —lenguaje normativo explícito— y agrega un dato: **de cinco casos, tres apoyan su lenguaje en una fuente externa nombrada**. **Lectura.**

### C3. La procedencia del corpus tiene un caso anterior a todos, y eso obliga a reformular una reserva

No a retirar una conclusión: a reformular una reserva. Ver §Procedencia. **Cambio** a propagar al SSOT de convergencia.

### C4. Lo que NO se puede hacer con esta fuente

- **Leerla con el instrumento v1 al mismo nivel que las otras cuatro.** Las ocho filas se contestaron leyendo archivos; acá se contestarían leyendo marketing y documentación de producto. Una columna «Kiro» en esa tabla parecería del mismo tipo que las demás y no lo sería.
- **Contarla como evidencia de efectividad.** No reporta ninguna medición. El material formativo oficial de AWS es didáctico y tampoco mide.
- **Verificar la anatomía.** Que los artefactos sean tres y las compuertas existan es lo que la documentación declara; nadie de este proyecto corrió el producto.

---

## Fuentes secundarias evaluadas y no usadas

Se evaluaron tres fuentes secundarias propuestas al encargar el análisis. **Ninguna sostiene una afirmación de este documento**, y se registran para que la decisión quede escrita:

- `pingax.com/kiro-spec-driven-development/` — existe; autor Vignesh Prajapati, 2026-06-28. Coincide con la fuente oficial en EARS y en `.kiro/steering/`. Cita «kiro.dev, AWS Summit NYC 2026» sin enlaces. **No usada**: todo lo que aporta ya está en fuente oficial.
- `tutorialsdojo.com/amazon-kiro-ai-ide-spec-driven-development/` — la página existe pero no se pudo recuperar su cuerpo. **No usada**: no se leyó.
- `devtoollab.com/blog/spec-driven-development-ai-agents` — existe; comparación de Spec Kit y Kiro, sin citas oficiales. Una de sus afirmaciones verificables (Spec Kit 1.0 el 2026-08-21) **coincide** con lo verificado en el clon de [R10]. **No usada**: fuente sin autoridad declarada, y nada de lo que aporta hace falta.

También existe material formativo oficial de AWS —un curso en AWS Skill Builder y contenido en `builder.aws.com`— que es didáctico, no normativo, y no se usó.

---

[SDD-Check]
- Spec leida: SI, y **registrada antes de escribir** (`../../SPECS_REGISTRY.md` -> `software/analisis/ANALISIS-KIRO.md`)
- Incluye/Excluye verificado: SI — no se emite veredicto de convergencia (la propagacion va al SSOT, en entrega aparte), no se toca la orientacion practica de uso, no se re-analiza ninguna otra implementacion
- Validaciones aplicadas: la clase de evidencia esta declarada en el encabezado, antes de cualquier rasgo, y se repite en C4; cada rasgo declara si sale de fuente oficial [R44] o de [R45], y el unico dato que no esta en fuente oficial —la ruta `.kiro/specs/<feature>/`— esta atribuido explicitamente a [R45]; las cuatro citas textuales se verificaron en la pagina que las contiene el 2026-09-05; la procedencia declara **las dos** cosas, que las fechas cierran una direccion y que no abren la contraria, con el contraejemplo de la triada requisitos-diseño-tareas como ancestro comun anterior a los cinco; la fuente no reporta medicion y eso queda dicho dos veces; las tres fuentes secundarias evaluadas quedan registradas con su estado y con el motivo de no usarlas; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: ninguno por este documento (`ssot_level: operativo`). `../../REFERENCIAS.md` recibio el alta de [R44] y [R45] en la misma entrega
- Derivados a revisar: **`software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md` requiere propagacion** — C3 reformula su reserva sobre la independencia de OpenSpec, y C1 suma un cuarto caso a la dimension candidata a instrumento v2. `software/analisis/ANALISIS-OPENSPEC.md` declara el mismo hueco de Kiro y queda señalado. `software/ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md`: Kiro es adoptable y su poblacion deberia incluirlo, con la salvedad de que sus dimensiones de madurez y actividad **no** se pueden calcular con `git` como las otras cuatro
- Cobertura: **incompleta y declarada** — C1, C2 y C3 tienen destino; la propagacion a los tres documentos señalados **queda sin ejecutar** en esta entrega
- Deuda arrastrada: **Tessl sigue sin pasar por el filtro de procedencia**, y era la otra mitad de la deuda que este documento paga a medias; ninguna afirmacion sobre Kiro es verificable en codigo y eso no se puede remediar mientras el producto sea cerrado. Sigue abierto: M-40 sin decidir, M-41 sin escribir, M-42 en Propuesta, el ecosistema del 1.0 de Spec Kit sin caracterizar, e instrumento v2 sin decidir
- Riesgos/reservas: es el unico caso del corpus caracterizado **sin leer una sola linea de su implementacion**, y por lo tanto el mas expuesto a describir lo que la fuente promete en vez de lo que hace; es producto comercial de una empresa grande, con documentacion que cumple tambien una funcion de venta; y la incorporacion llega despues de que el instrumento v1 se fijara y de que los otros cuatro casos se leyeran, lo que MUST tenerse presente si alguna vez se lo lee con ese instrumento

---

## Actualización: steering y hooks, leídos en sus páginas propias (2026-10-09)

La anatomía de arriba despacha el contexto de proyecto y los hooks en una línea cada uno, tomados de la página de specs. Esta actualización lee las dos páginas que los documentan —`kiro.dev/docs/steering/` y `kiro.dev/docs/hooks/`, consultadas el 2026-10-09 [R44]—, porque son el mecanismo con el que Kiro hace llegar reglas transversales a todo el trabajo: estilos, arquitectura, convenciones. Sigue valiendo la clase de evidencia del encabezado: todo lo de abajo es lo que la documentación declara.

### El steering es el canal de las reglas transversales, y se carga por modo

La página lo define como conocimiento persistente: «Steering gives Kiro persistent knowledge about your project through markdown files. Instead of explaining your conventions in every chat, steering files ensure Kiro consistently follows your established patterns, libraries, and standards» [R44].

**Dos alcances, con precedencia declarada.** Archivos de workspace en `.kiro/steering/` y globales en `~/.kiro/steering/`. Si chocan, «Kiro will prioritize the workspace steering instructions» [R44]. Los globales pueden distribuirse a un equipo entero: «Team steering files can be pushed to user's PCs via MDM solutions or Group Policies» [R44].

**Cuatro modos de inclusión**, declarados en el *front matter* de cada archivo [R44]:

| Modo | Cuándo entra al contexto | Uso que la fuente le asigna |
|---|---|---|
| `always` (por defecto) | «loaded into every Kiro interaction automatically» | «core standards that should influence all code generation and suggestions», con el stack, las convenciones y «fundamental architectural principles» como ejemplos |
| `fileMatch` | Sólo al trabajar con archivos que coinciden con `fileMatchPattern` | Guía especializada que no hace falta siempre |
| `manual` | Cuando se la nombra en el chat | Contexto puntual, sin cargar cada interacción |
| `auto` | Cuando el pedido coincide con la descripción del archivo | Guía pesada que sólo conviene cargar si es relevante |

Los tres archivos base que la herramienta genera —producto, tecnología y estructura— «are included in every interaction by default» [R44].

**Otros tres rasgos con consecuencia práctica** [R44]:
- Lee `AGENTS.md`, de la raíz, de la ubicación global y de subdirectorios, pero esos archivos «do not support inclusion modes and are always included».
- El steering puede referenciar archivos vivos del workspace con `#[[file:<ruta>]]`; si la referencia no resuelve, «Kiro leaves a visible unresolved-reference marker» en vez de descartar el documento en silencio.
- Con agentes personalizados el steering **no** se carga solo: hay que declararlo en los recursos del agente.

**Lo que la página no dice.** No dice que el steering gobierne específicamente la generación de los tres artefactos de la spec: dice que entra en «every interaction». Leerlo como regla de redacción de specs es inferencia, no declaración.

### Los hooks pueden bloquear, y cambiaron de formato

«Hooks run shell commands or agent prompts automatically when specific events happen in your session» [R44]. Cada hook es un archivo JSON en `.kiro/hooks/` con un evento disparador, un *matcher* opcional y una acción: un comando de shell o un prompt que se inyecta en la conversación. Entre los usos que la página enumera está el de compuerta: «Gate dangerous operations - block tool execution unless preconditions are met (PreToolUse)» [R44].

Esto corrige en parte la línea de §Anatomía, que caracterizaba los hooks sólo por guardar o crear archivos: el evento previo al uso de una herramienta los vuelve capaces de **impedir** una acción, no sólo de reaccionar a ella.

**El formato se movió**, y la página lo declara: en IDE 1.0, «Hooks moved from the previous format to standalone JSON files with PascalCase trigger names», y la CLI 3.0 tiene su propia migración desde el formato embebido en agentes de la 2.x [R44]. Ejemplos de terceros escritos antes de ese cambio —archivos `.kiro.hook` con bloques `when`/`then` y eventos en minúscula— describen el formato anterior y no deben leerse como el vigente.

### C5. Una regla transversal no tiene por qué cargarse siempre

Los cuatro modos de inclusión permiten que una regla del proyecto entre al contexto **sólo cuando aplica** —por el archivo que se está tocando o por coincidencia con lo que se pide— en vez de cargarse en cada interacción. La fuente lo justifica por el costo: `fileMatch` «keeps context relevant and reduces noise» [R44]. Una guía de estilo de interfaz, por ejemplo, puede atarse a los archivos de componentes y no viajar con cada pedido de backend. **Lectura**, con la reserva de siempre: nadie de este proyecto corrió el producto, y la documentación no dice cuánto contexto ahorra ni si la activación por descripción acierta. La comparación con los otros casos no se hace acá: vive en `../ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md` §6.

---

[SDD-Check] — actualizacion 2026-10-09
- Spec leida: SI (spec registrada en `../../SPECS_REGISTRY.md`; sin enmienda: la actualizacion cae en «sintesis del metodo declarado… contexto de proyecto y automatizaciones» y en «conclusiones accionables para Linea B»)
- Incluye/Excluye verificado: SI — no se emite veredicto de convergencia ni orientacion practica (la comparacion entre casos va a `../ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md` §6, en la misma entrega); no se re-analiza ninguna otra implementacion, y C5 remite la comparacion a su lugar en vez de hacerla
- Validaciones aplicadas: cada cita textual se verifico en la pagina oficial descargada el 2026-10-09 (`kiro.dev/docs/steering/`, `kiro.dev/docs/hooks/`), no en un resumen; la clase de evidencia del encabezado sigue rigiendo y se repite en la apertura de la seccion; lo que la pagina no dice —que el steering gobierne la redaccion de specs— queda escrito como inferencia; la correccion a la linea de §Anatomia sobre hooks se escribe como correccion, sin reescribir esa linea; los ejemplos de terceros en formato `.kiro.hook` no sostienen ninguna afirmacion y se declaran formato anterior con la frase oficial que lo dice; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: ninguno por este documento. `../../REFERENCIAS.md` suma a [R44] las dos paginas consultadas
- Derivados a revisar: `../ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md` — §6 suma las reglas transversales como escenario, en la misma entrega; su ficha de Kiro («Configuracion») queda correcta y menos detallada que esta seccion, sin contradiccion
- Cobertura: completa para steering y hooks tal como la documentacion los declara
- Deuda arrastrada: ninguna nueva; las de los bloques anteriores siguen donde viven
- Riesgos/reservas: todo es declaracion de producto cerrado; la documentacion cambia sin version publicada, asi que las citas valen para la fecha de consulta y no hay commit que las ancle
