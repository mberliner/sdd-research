# Análisis: Tessl como método, y el único caso que regenera

Fecha: 2026-09-05.
Fuente: Tessl, blog y documentación oficiales consultados el 2026-09-05 [R46]; la regeneración y su no-determinismo, verificados en [R20].
Alcance: Línea B (software).

> **Clase de evidencia.** Igual que Kiro [R44], Tessl **no tiene clon vendored y no puede tenerlo**. Y va un paso más allá: su *Framework* está en **beta cerrada**, así que ni siquiera es instalable libremente. Todo rasgo se cita de documentación oficial o de un tercero identificado. Nada se leyó en código, nada se corrió.

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
