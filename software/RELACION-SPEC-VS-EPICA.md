# Relación entre "spec" y los artefactos ágiles (épica / historia de usuario)

Fecha: 2026-06-03. Revisado y reestructurado el 2026-09-05.
Línea B (software): el vocabulario ágil y las implementaciónes SDD son nativos de software.

Pregunta que origina el documento: *¿una "spec" es análoga a una "épica"?*

Respuesta corta: **no, y el motivo es anterior a cualquier implementación.** Los dos artefactos no tienen el mismo estatuto —uno está definido por una norma, el otro no tiene definición autoritativa— y no operan sobre el mismo eje. Además, el término "spec" tiene **dos sentidos** en este proyecto que responden la pregunta de forma diferente; confundirlos es la causa habitual del malentendido.

---

## 1. El estatuto de los dos artefactos no es el mismo

Antes de comparar jerarquías conviene preguntar qué autoridad define cada término. La respuesta es asimétrica, y esa asimetría explica por qué la pregunta se responde mal tan seguido.

### La especificación de requisitos tiene definición normativa

`ISO/IEC/IEEE 29148:2018` es el estándar de ingeniería de requisitos y declara en su alcance que **«defines the construct of a good requirement, provides attributes and characteristics of requirements»** [R03]. Hay, entonces, un cuerpo normativo que dice qué es una especificación de requisitos y qué la hace buena, con características exigibles y verificables. Se la puede evaluar contra un criterio externo al equipo que la escribió.

### La épica no aparece en la fuente autoritativa del marco al que se le atribuye

La **Scrum Guide** —edición 2020, de Schwaber y Sutherland— **no contiene las palabras «epic» ni «user story»**, en ninguna forma [R41]. Su unidad de trabajo es el *Product Backlog item*, y ni siquiera la define formalmente: la caracteriza por comportamiento («Product Backlog items that can be Done by the Scrum Team within one Sprint are deemed ready for selection») y por el refinamiento, que es «breaking down and further defining Product Backlog items into smaller more precise items».

Esto no es una omisión menor ni un tecnicismo. El marco que la mayoría de los equipos nombra cuando dice «épica» no usa la palabra.

### Lo que la épica sí tiene: una etiqueta de práctica, datada y en disputa

La definición disponible es de glosario profesional, no de norma: **«An epic is a large user story that cannot be delivered as defined within a single iteration or is large enough that it can be split into smaller user stories»**, con el origen atribuido a Mike Cohn en 2004, en *User Stories Applied* [R42].

Y esa definición no se sostuvo estable. Thoughtworks documentó su deriva: **«In a case of Semantic Diffusion, the original definition of "epic" has weakened over the years»** [R43]. Hoy conviven dos usos incompatibles —marcador de una historia demasiado grande que hay que partir, y mecanismo de agrupación para reportar— y el artículo lo dice sin rodeos: «It goes without saying that this is confusing, so teams pick the definition that suits them». Señala además que la herramienta moldea la práctica: «software tools such as Jira are influencing team processes».

Dicho de otro modo: buena parte de lo que un equipo entiende por «épica» viene del tablero que usa, no de un cuerpo doctrinario.

### Y la historia de usuario fue diseñada, explícitamente, para **no** ser una especificación

Este es el punto que cierra el encuadre, y es el más olvidado. El modelo de las tres C —*Card, Conversation, Confirmation*— lo propuso Ron Jeffries en 2001 **«to distinguish "social" user stories from "documentary" requirements practices such as use cases»**, y la tarjeta es «a physical token giving tangible and durable form to what would otherwise only be an abstraction» [R42].

La historia no es una especificación corta: es un **recordatorio de una conversación pendiente**, concebido en oposición a la práctica documental. Preguntar si una spec es análoga a una épica —que es un agregado de historias— es preguntar si un artefacto cuya razón de ser es documentar equivale a uno cuya razón de ser es reemplazar la documentación por conversación.

> **Reserva de fuente.** El artículo original de Jeffries (2001-08-30) no se pudo alcanzar el 2026-09-05; la atribución de las tres C se cita por el glosario de Agile Alliance [R42], no por la fuente primaria. La cita textual de arriba es del glosario.

### Consecuencia

| | Especificación de requisitos | Épica |
|---|---|---|
| ¿Definición normativa? | Sí — `ISO/IEC/IEEE 29148:2018` [R03] | No |
| ¿Presente en la fuente autoritativa del marco? | Sí | **No** — ausente de la Scrum Guide [R41] |
| Origen del término | Cuerpo normativo de ingeniería de requisitos | Etiqueta de práctica, Cohn 2004 [R42] |
| Estabilidad del significado | Fijado por norma revisable | Difusión semántica documentada; dos usos en conflicto [R43] |
| Criterio de calidad | Externo y verificable [R03] | Convención del equipo o de la herramienta [R43] |

**Comparar los dos es comparar objetos de distinto orden.** No es que la analogía sea imprecisa: es que uno de los dos términos no tiene un referente único contra el cual medirla.

---

## 2. Los dos ejes

Aun descontando la asimetría de estatuto, los artefactos responden preguntas distintas:

- **Eje de alcance del trabajo** — *qué hay que hacer y en qué orden*. Es el eje de la épica, de la historia y de la tarea. Su unidad se consume: cuando el trabajo está hecho, el artefacto dejó de tener función.
- **Eje de contrato del artefacto** — *qué es correcto, completo y consistente*. Es el eje de la especificación. Su unidad sobrevive al trabajo, porque sirve para juzgar el resultado y para el cambio siguiente.

Un artefacto puede ocupar los dos ejes a la vez —y varias implementaciónes SDD lo hacen—, pero eso es una decisión de diseño de cada una, no una propiedad del concepto. La pregunta original supone que hay un solo eje, y ahí está el error.

---

## 3. Los dos sentidos de "spec" en este proyecto

| Sentido | Qué es | Eje | Relación con la épica |
|---------|--------|-----|-----------------------|
| **Spec de una implementación SDD** (p. ej. Spec Kit [R10]) | Artefacto de *alcance funcional* que agrupa historias de usuario, criterios de aceptación y restricciones | alcance + contrato | **Supra-épica**: la contiene, no la equivale — con la salvedad de la sección 4 |
| **Spec de este repo** (`../SPECS_REGISTRY.md`) | *Contrato de gobernanza* de un documento concreto: `incluye`/`excluye`/`validacion`/`ssot_level` | contrato | **Ortogonal**: no es una unidad de alcance de trabajo |

La pregunta "spec ≈ épica" sólo tiene sentido para el primer significado. Para el segundo, la spec no compite con la épica en absoluto: gobierna la calidad de un artefacto, no organiza el trabajo a hacer.

La "épica" se acerca más a un **SSOT** de este repositorio (fuente grande y autoritativa de la que cuelgan derivados, igual que una épica cuelga historias) que a una *spec* local. La spec local es más bien el *Definition of Ready/Done* de cada documento.

---

## 4. Cómo resuelve el eje de alcance cada implementación

> **Qué es esta sección y qué no.** Las cuatro implementaciónes entran acá como **evidencia** de que el eje de alcance no está resuelto de una sola manera. **No es una comparación entre frameworks**: eso vive en `CONVERGENCIA-IMPLEMENTACIONES-SDD.md` para el veredicto de convergencia, y el análisis comparativo propiamente dicho queda diferido a un trabajo posterior.

| Caso | ¿La spec es contenedor de alcance? | Cómo trata la épica | ¿Linaje independiente? |
|---|---|---|---|
| **Spec Kit** [R10] | Sí: agrupa historias P1/P2/P3 con criterios Given/When/Then | Contención — **salvo** que la feature sea demasiado grande | Sí |
| **OpenSpec** [R38] | Partido en dos: `openspec/specs/` son capacidades durables (`cli-init`, `command-generation`), `openspec/changes/` son unidades de trabajo con `Why` / `What Changes` / `Capabilities` | Los dos ejes existen y están **separados estructuralmente** | Sí, por fecha |
| **Superpowers** [R37] | **No**: la spec es `Goal` / `Design` / `Tests` / `Non-Goals`, sin historias ni agrupación de alcance | No hay contenedor de alcance | Sí |
| **sdd-first** [R39] | Sí, el más explícito: `## User Story 1 (Priority P1)`, requisitos numerados por historia (`FR-US1-004`), escenarios de aceptación por historia | Contención | **No** — mismo autor que este repositorio |

Cuatro precisiónes, y las cuatro importan:

**La contención tiene un solo caso independiente.** sdd-first es del mismo autor que este repositorio y `REFERENCIAS.md` [R39] prohíbe contarlo como linaje: su acuerdo con este método es autocorrelación por construcción. Su spec es la instancia más nítida de contención del corpus, y aun así **no cuenta como evidencia**. Queda en la tabla para que la exclusión sea visible, no para sumar.

**Y ese caso independiente tiene, él mismo, las dos direcciones.** Spec Kit contiene historias dentro de la spec, pero cuando la feature no entra en un ciclo, `../fuentes-externas/spec-kit/docs/concepts/spec-of-specs.md` escribe **la épica por encima**: un *roadmap* descompone lo que el documento llama «the epic» en sub-specs, cada una con su propio ciclo. Es la jerarquía contraria, y no depende del framework sino del **tamaño**. La misma fuente ordena esa opción como la más cara de cuatro (`../fuentes-externas/spec-kit/docs/concepts/complex-features.md`), a usar sólo cuando las livianas no alcanzan.

**Hay un caso que separa los dos ejes en el disco.** OpenSpec no elige entre alcance y contrato: pone cada uno en su directorio, y un *change* nombra explícitamente qué capacidades crea o modifica. Es la tesis de la sección 2 hecha estructura, desde un linaje que el repositorio ya certificó independiente por fecha.

**Y hay un caso que no tiene el eje.** Superpowers no ofrece ningún contenedor de alcance: su spec es un documento de diseño fechado. Si «spec ≈ épica» fuera una propiedad del concepto SDD, este caso no debería existir.

---

## 5. Dónde sí se parecen

Cuando una implementación **elige** que su spec ocupe los dos ejes, el parecido con la épica es real y vale nombrarlo:

| Dimensión | Épica (ágil) [R42] | Spec que agrupa alcance (p. ej. Spec Kit) [R10] |
|-----------|--------------------|--------------------------------------------------|
| Agrupa alcance | sí (funcionalidad) | sí (historias + restricciones) |
| Criterio de "hecho" | Definition of Done | criterios de éxito SC-xxx medibles |
| Se descompone | en historias -> tareas | en plan -> tasks |
| Trazabilidad | épica -> historia -> commit | spec -> plan -> task (coverage mapping) |

Evidencia del lado SDD [R10]: en Spec Kit "las historias de usuario se vuelven endpoints de API, los conceptos de dominio se vuelven modelos de datos, los escenarios de aceptación se vuelven tests". Las historias **viven dentro** de la spec y generan los artefactos aguas abajo; no son artefactos hermanos. El flujo completo está en `ANALISIS-SPEC-KIT.md`, no se reproduce aquí.

En el plano de *alcance*, el mapeo más fiel es:

```text
Épica (ágil)              ≈   parte del cuerpo de una spec que agrupa alcance, o un SSOT (este repo)
Historia de usuario       ≈   requisito FR-xxx dentro de la spec / documento derivado
Criterios de aceptación   ≈   bloque `validacion` con `[ ]` (este repo)
```

Y el contraste de jerarquías, que sólo vale para las implementaciónes que sí contienen:

```text
Ágil:       Épica  ─────────►  Historia de usuario  ─────────►  Tarea
                               (criterios de aceptación)

Spec Kit:   Spec  ──/plan──►  Plan  ──/tasks──►  Tasks  ──/implement──►  Código
            (contiene varias historias P1/P2/P3 + criterios Given/When/Then)
```

---

## 6. La diferencia de fondo que conviene no perder

SDD nace en parte como **reacción** al modo en que ágil trató a las especificaciones: las relegó a historias ligeras y backlogs, dejando la "verdad" en el código y la documentación como rastro posterior [R20][R21]. Visto desde la sección 1, esa reacción es contra algo que ágil hizo **a propósito**: la historia se diseñó para no ser documentación [R42]. SDD no corrige un descuido; discute una decisión.

Consecuencia para la analogía:

- En **ágil**, la historia es *efímera* — es el recordatorio de una conversación, y se descarta cuando la conversación ocurrió [R42].
- En **SDD**, la spec es el *activo durable* — mantener el software es evolucionar la spec [R10].

Por eso forzar "spec ≈ épica" induce a error: en SDD la spec no es el *trabajo a hacer* (rol de la épica), sino el *contrato que sobrevive al trabajo*.

---

## 7. Estado de la discusión externa

- **Sobre la contención**: una spec de Spec Kit comprende múltiples historias de usuario junto a specs funcionales, supuestos y resultados; trata las historias como componentes de un marco mayor, no como su equivalente [R10][R21].
- **SDD como síntesis waterfall/ágil**: enfatiza especificación detallada (como waterfall) pero iterativa y viva (como ágil), con la spec en el centro [R20][R21].
- **Tensión crítica**: parte de la comunidad lee Spec Kit como un retorno encubierto a cascada ("documentary bureaucracy") [R22]. Conecta con nuestro anti-patrón "cascada encubierta" (`../comun/SDD-ADAPTATIVO-VS-CASCADA.md`): la diferencia no está en cuánta spec se escribe, sino en si la spec permanece viva o se congela.
- **Sobre el término «épica» en sí**: la discusión no es sólo entre ágil y SDD. Dentro de ágil el término está en disputa desde antes de que SDD existiera [R43], y la fuente autoritativa del marco no lo usa [R41].

No se ha hallado ninguna fuente que defienda la equivalencia estricta "spec = épica". Lo que **no** puede afirmarse —y una versión anterior de este documento lo afirmaba— es que exista una posición dominante de contención: sobre el corpus disponible hay tres respuestas distintas al eje de alcance (sección 4), y el único caso independiente que contiene documenta también la jerarquía inversa.

---

## 8. Qué cambió respecto de la versión del 2026-06-03

El documento original respondía bien la pregunta y lo hacía sobre una sola implementación, que era todo lo que el corpus tenía en junio. Lo que se retiró y lo que se agregó, para que la revisión sea auditable:

| Afirmación de la versión 2026-06-03 | Estado hoy |
|---|---|
| «la posición dominante es la de **contención/inversión de jerarquía**» | **Retirada.** Sobre cuatro casos hay tres respuestas distintas, y la contención tiene un solo caso independiente (sección 4) |
| «En ágil, la unidad mínima es la historia de usuario y la épica es "una historia grande" que se descompone», atribuido a [R21] | **Conservada, reanclada.** La definición ahora sale de [R42], fuente autoritativa de vocabulario ágil, en vez de una fuente secundaria |
| «En Spec Kit la jerarquía se invierte en granularidad: la spec está *por encima* y contiene las historias» | **Conservada, condicionada.** Vale hasta que la feature no entra en un ciclo; a partir de ahí la propia fuente pone la épica arriba (sección 4) |
| Los dos sentidos de "spec", la tabla de parecidos y la diferencia de fondo | **Conservados**, con el encuadre de estatuto (sección 1) delante, que antes no existía |
| Encuadre general fundado en fuentes normativas | **Nuevo.** La versión anterior no tenía sección 1: el lado ágil se apoyaba en [R21] y el lado spec en ninguna norma |

Nada de lo anterior estaba mal en su fecha: estaba fundado en un corpus de un caso y en fuentes secundarias para el vocabulario ágil. Lo que cambió es el corpus y el nivel de las fuentes, no el criterio.

---

## Fuentes

- [R03] ISO/IEC/IEEE 29148:2018 — la especificación de requisitos tiene definición normativa.
- [R10] GitHub Spec Kit — jerarquía spec/plan/tasks, "las historias viven dentro de la spec", y el *roadmap* de `spec-of-specs.md` que invierte esa jerarquía por tamaño.
- [R20] Martin Fowler — SDD como síntesis y crítica al trato ágil de las specs.
- [R21] Thoughtworks — la spec agrupa múltiples historias; ágil relegó las specs a historias ligeras.
- [R22] Scott Logic — lectura crítica de Spec Kit como posible cascada reinventada.
- [R37] obra/superpowers — implementación sin contenedor de alcance.
- [R38] Fission-AI/OpenSpec — los dos ejes separados en dos directorios.
- [R39] mberliner/sdd-first — contención explícita por historia; **mismo autor, no cuenta como evidencia independiente**.
- [R41] Scrum Guide (2020) — no contiene «epic» ni «user story».
- [R42] Agile Alliance, glosario — definición y origen de «epic»; las tres C de Jeffries (2001).
- [R43] Matt Riley / Thoughtworks (2020) — difusión semántica del término «épica».

---

[SDD-Check] — reestructuracion 2026-09-05
- Spec leida: SI, y **enmendada antes de escribir** (`../SPECS_REGISTRY.md` -> `software/RELACION-SPEC-VS-EPICA.md`): el `proposito` pasa a declarar el encuadre general primero y la evidencia de implementaciónes despues; `incluye` suma el estatuto de los artefactos, el eje de alcance en las cuatro implementaciónes y la seccion datada de cambios; `excluye` incorpora explicitamente la comparacion entre frameworks; `validacion` suma cinco casillas nuevas
- Incluye/Excluye verificado: SI — las cuatro implementaciónes entran como evidencia y la seccion 4 lo declara en su encabezado; no se re-analiza el flujo interno de ninguna; el veredicto de convergencia se remite a su SSOT; la transferencia a Linea A sigue excluida
- Validaciones aplicadas: el encuadre general (seccion 1) precede a toda evidencia de implementacion y se funda en norma [R03] y en fuentes autoritativas de vocabulario [R41][R42], no en secundarias; los cuatro rasgos de la seccion 4 se leyeron en los clones vendored y no de los analisis previos (Superpowers verificado con `grep -ci "user story\|epic"` sobre su spec mas reciente: 0 ocurrencias; la ausencia en la Scrum Guide, verificada en fuente el 2026-09-05); la reserva de [R39] esta escrita dos veces, en la tabla y en la precision que la sigue; la imposibilidad de alcanzar la fuente primaria de Jeffries esta declarada donde se cita; ninguna afirmacion retirada se borro, todas figuran en la seccion 8; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: `../SPECS_REGISTRY.md` (enmienda de spec) y `../REFERENCIAS.md` (alta de [R41], [R42] y [R43]; correccion de [R03], que apuntaba a la edicion 2011 y ahora apunta a la 2018 vigente)
- Derivados a revisar: ninguno registrado para este documento. Señalado sin modificar: `software/ANALISIS-SPEC-KIT.md` §Actualizacion 2026-09-05 dejo esta actualizacion como deuda y **queda saldada acá**
- Cobertura: completa para el alcance enmendado — cada seccion de `incluye` tiene su seccion en el cuerpo, y cada casilla de `validacion` tiene su verificacion declarada arriba
- Deuda arrastrada: la **fuente primaria de Jeffries no se pudo verificar** y la atribucion descansa en [R42]; la definicion de epica de Cohn 2004 se cita por atribucion de [R42], no por el libro; el texto completo de [R03] es de pago y se cita por su alcance declarado. Sigue abierto de la sesion: M-40 sin decidir, M-41 sin escribir, M-42 en Propuesta, el ecosistema del 1.0 de Spec Kit sin caracterizar
- Riesgos/reservas: la seccion 4 describe cuatro implementaciónes sobre una sola dimension y **MUST NOT leerse como comparacion entre frameworks**, que es trabajo diferido; el corpus son cuatro casos de los cuales uno no cuenta, asi que «tres respuestas distintas» describe lo disponible y no una distribucion; ninguna de las cuatro fuentes reporta medicion alguna sobre esta dimension

---

## Bloques de entrega anteriores

Registro datado y **no editable hacia atrás**: cada bloque vale para su fecha y para el cuerpo que el documento tenía entonces. El primero cierra la entrega original del 2026-06-03; el segundo, la reconciliación de encabezado del 2026-08-23. Ninguno de los dos describe el documento actual — eso lo hace el bloque de arriba.

[SDD-Check]
- Spec leida: SI (spec propuesta, aprobada y registrada en `../SPECS_REGISTRY.md` para este doc)
- Incluye/Excluye verificado: SI (foco en la relación spec/épica; no re-analiza el flujo interno de Spec Kit ni duplica el mapeo del SSOT; Línea A diferida)
- Validaciones aplicadas: afirmaciones externas ancladas en [R10][R20][R21][R22]; refs internas verificadas (ANALISIS-SPEC-KIT, SDD-ADAPTATIVO-VS-CASCADA, SPECS_REGISTRY, BACKLOG-INVESTIGACION); sin emoticones; fechas YYYY-MM-DD; ortografía del español con tildes (convención fijada en SPECS_REGISTRY.md); no duplica SSOT (referencia, no copia)
- SSOT afectado: ninguno (derivado de `software/ANALISIS-SPEC-KIT.md`)
- Derivados a revisar: ninguno
- Cobertura: completa — cada afirmación de la comparación mapea a una fuente [Rxx] o a un SSOT interno referenciado
- Deuda arrastrada: ninguna; la transferencia del razonamiento a Línea A queda como item de backlog preexistente, no abierto por esta entrega
- Riesgos/reservas: análisis basado en snapshot Spec Kit v0.8.13 [R10] y en discusión externa de 2025-2026 que aún evoluciona

---

[SDD-Check]
- Spec leida: SI (`../SPECS_REGISTRY.md` → `software/RELACION-SPEC-VS-EPICA.md`)
- Incluye/Excluye verificado: SI — la entrega es de reconciliación: el encabezado declaraba «Deriva de: `ANALISIS-SPEC-KIT.md`» y el registro no le declara `deriva_de` desde el 2026-08-03, cuando M-13 se lo quitó por ser relación forzada. El documento es original, no derivado; la línea era el último resto del error de modelado, que M-13 corrigió en el registro sin bajar al documento
- Validaciones aplicadas: cruce del encabezado contra la entrada del registro; verificación de que ningún otro documento sostenga la derivación (`software/00-INDEX.md` y `RELACION-FR-VS-SC-Y-COBERTURA.md` lo citan sin llamarlo derivado); `tools/check_docs.py` en verde
- SSOT afectado: `../SPECS_REGISTRY.md` — la exclusión «transferencia del razonamiento a Línea A», que vivía sólo en el encabezado de este documento, se trajo al campo `excluye` de su spec, que es donde el alcance vive
- Derivados a revisar: ninguno — este documento no tiene derivados registrados
- Cobertura: completa sobre el encabezado; el cuerpo del documento no se tocó
- Deuda arrastrada: otros dos documentos reproducen campos del registro en su encabezado —`docs-y-investigacion/GUIA-INICIO-PROYECTO-INVESTIGACION.md` (tabla con `ssot_level` y `owner`) y `software/SDD-EN-LEGACY-Y-BROWNFIELD.md` («Estado: Borrador»)— y siguen sin remediar: es M-28 en `../agenda/MEJORAS-METODO.md`
- Riesgos/reservas: el bloque anterior de este documento sigue diciendo «SSOT afectado: ninguno (derivado de `software/ANALISIS-SPEC-KIT.md`)» y NO se corrige: es registro datado y la corrección se anota hacia adelante, no hacia atrás
