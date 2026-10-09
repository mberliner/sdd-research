# Análisis: OpenSpec y su relación con nuestra investigación SDD (Línea B)

Fecha: 2026-08-02.
Fuente: OpenSpec v1.7.0, commit `45cca5d` (consultada 2026-08-02) [R38].
Alcance: Línea B (software).

---

## Contexto

OpenSpec es un sistema de SDD distribuido como CLI de npm (`@fission-ai/openspec`, MIT, respaldo de Fission AI). El agente no lee la metodología de un documento: la pide a la herramienta. Se instala en el proyecto, genera adaptadores para más de 30 asistentes (`OpenSpec:docs/supported-tools.md`) y expone doce skills sobre un CLI que resuelve rutas, valida estructura y sirve las instrucciones de cada artefacto.

Este documento la caracteriza y la mapea contra nuestro protocolo (`../../AGENTS.md`, `../../SPECS_REGISTRY.md`) con el mismo instrumento de ocho filas que `ANALISIS-SPEC-KIT.md` y `ANALISIS-SUPERPOWERS.md`. La lectura cruzada de los cuatro casos **no** vive acá: su SSOT es `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`.

---

## Procedencia: por qué cuenta como linaje

`CONVERGENCIA-IMPLEMENTACIONES-SDD.md` exige que todo caso nuevo declare su procedencia antes de contarse. Este es el resultado de aplicar ese filtro, y es la sección que decide si el resto del documento tiene valor para el relevamiento.

**Independiente de Spec Kit, por fecha.** El primer commit de OpenSpec es del **2025-08-05** y ya se llama "initialize openspec project structure"; el primer commit del repositorio de Spec Kit es del **2025-08-21**, dieciséis días posterior (ambos verificables en el historial de cada repositorio). La anatomía `openspec/specs/` + `openspec/changes/` existía antes de que el repositorio del que podría haberla copiado tuviera historia pública. No hay derivación posible en esa dirección.

**Menciona a Spec Kit y a Kiro, pero para diferenciarse.** Su README los usa como contraste comercial —"heavyweight", "locked into their IDE"— y cita el catálogo de extensiones de Spec Kit como analogía de un mecanismo propio. Eso es posicionamiento de competidor, no herencia de método.

**Los marcadores de difusión conocidos están ausentes.** No hay `[NEEDS CLARIFICATION]`, no hay constitución ni gate de principios, no hay coverage mapping requisito a verificador (verificado por búsqueda sobre el clon completo). Las tres prácticas que este proyecto ya identificó como difusión desde Spec Kit no aparecen.

**Reserva declarada.** La notación `WHEN/THEN` de sus escenarios desciende de Gherkin [R07], ancestro común anterior a los cuatro casos: es herencia compartida, no derivación entre ellos. Lo que queda sin resolver es su relación con Kiro, anunciado el 2025-07-14: tres semanas de anterioridad y un formato de requisitos emparentado no alcanzan para afirmar independencia total. **Kiro dejó de estar ausente del corpus el 2026-09-05** (`ANALISIS-KIRO.md`, [R44]) y la lectura no resolvió esta reserva: la confirmó y la extendió a Spec Kit, que es 38 días posterior a Kiro. Establecer o descartar esa derivación exige marcadores de difusión, no cronología, y ese trabajo sigue sin hacerse. La independencia que este documento sostiene es **respecto de Spec Kit**, que es el linaje relevante para el relevamiento; frente a Kiro queda como límite abierto.

---

## Flujo de trabajo

| Orden | Comando | Función | Artefacto |
|-------|---------|---------|-----------|
| 0 | `/opsx:explore` | Explorar sin compromiso: lee el código, propone caminos, no escribe nada | ninguno |
| 1 | `/opsx:propose` | Generar en un paso todos los artefactos que el schema declare | `proposal.md`, `specs/<capacidad>/spec.md` (delta), `design.md`, `tasks.md` |
| 2 | `/opsx:apply` | Implementar recorriendo el checklist de tareas | código + tareas marcadas |
| 3 | `/opsx:verify` | Verificar implementación contra los artefactos en tres dimensiones | reporte con CRITICAL / WARNING / SUGGESTION |
| 4 | `/opsx:archive` | Fusionar el delta aprobado en la spec vigente y archivar el cambio | `openspec/specs/` actualizado, cambio en `changes/archive/` |

Rasgos de diseño relevantes:

- **Spec vigente y delta propuesto son artefactos distintos.** `openspec/specs/` es la verdad actual; `openspec/changes/<nombre>/specs/` son deltas con encabezados `## ADDED / MODIFIED / REMOVED Requirements`. Archivar es la operación que los fusiona.
- **La instrucción se sirve, no se lee.** Para cada artefacto el agente corre `openspec instructions <id> --json` y recibe `context`, `rules`, `template`, `dependencies` y la ruta de salida resuelta. La skill le prohíbe explícitamente copiar `context` y `rules` al archivo: son restricciones para quien escribe, no contenido.
- **Las reglas del proyecto viven en `openspec/config.yaml`**, en dos campos: `context` (stack, lenguaje de producto, restricciones transversales) y `rules` desglosado por artefacto (`specs:`, `tasks:`, `design:`).
- **El grafo de artefactos es de dependencias, no de fases.** `openspec status --json` devuelve las aristas `requires`; la skill advierte que las dependencias son habilitadores y no compuertas. Es un rechazo explícito de las fases rígidas.
- **Brownfield declarado como posicionamiento.** "built for brownfield not just greenfield" es una de las cinco líneas de su filosofía; su argumento contra Spec Kit y Kiro es que ambos brillan en 0→1 y se degradan en 1→n.
- **Dogfooding con corpus.** El repositorio se desarrolla con OpenSpec: 36 specs vigentes y 83 cambios archivados con propuesta, diseño, tareas y deltas.

---

## El rasgo que más aporta: la instrucción entregada por herramienta

Es el aporte distintivo de esta fuente y no tiene equivalente en Spec Kit, en Superpowers ni acá. Los otros tres casos —y este repositorio— resuelven "cómo llega el método al agente" del mismo modo: un documento que el agente lee y debe sostener en contexto. OpenSpec lo resuelve al revés: el método vive en un schema versionado y el CLI entrega **solo el fragmento del momento**, resuelto contra el estado real del cambio.

Dos consecuencias que tocan deudas abiertas de este repositorio:

- **Disuelve el problema que `M-04` intenta administrar.** `M-04` (`../../agenda/MEJORAS-METODO.md`) trata el costo de contexto de los documentos de método, y Superpowers aportó la advertencia de que compactarlos tiene costo conductual medido [R37]. La entrega bajo demanda cambia el planteo: no se compacta el documento, se fragmenta la entrega. Nuestro `AGENTS.md` se inyecta entero en cada sesión aunque el noventa por ciento no aplique al cambio en curso.
- **Cambia dónde puede fallar el cumplimiento.** Con documento leído, el modo de falla es que el agente no lo aplique; con instrucción servida, es que no corra el comando. Es un modo de falla distinto, y —esto importa— **observable desde afuera**: la ausencia de una llamada al CLI se detecta sin juzgar prosa. Es exactamente el tipo de señal independiente del artefacto que la prioridad alta #6 de `../../agenda/BACKLOG-INVESTIGACION.md` declara faltante.

Límite que MUST acompañar cualquier uso de esto: OpenSpec **no reporta ninguna medición**, ni interna ni externa, de que su forma de entrega funcione mejor. La ventaja es argumental. A diferencia de [R37], que al menos aporta evals autoreportados, acá no hay ni eso: se porta una idea de diseño, no un resultado.

---

## Mapeo: OpenSpec vs. nuestro protocolo SDD

Se usa el instrumento v1, las mismas ocho filas fijadas el 2026-05-24, sin agregar ni redefinir ninguna para alojar a esta fuente.

| Concepto | OpenSpec | Nuestro proyecto |
|----------|----------|------------------|
| Fuente de autoridad no-negociable | `openspec/config.yaml` (`context` + `rules` por artefacto), servido por el CLI en el momento de escribir. Orden de resolución declarado: flag > metadata del cambio > config del proyecto > default. **Sin constitución ni gate de principios** | `../../CONSTITUTION.md` > `../../SPECS_REGISTRY.md` > `../../AGENTS.md`, leídos por el asistente al inicio de sesión |
| Lenguaje normativo | `SHALL` en requisitos (registro ISO/IEC/IEEE 29148 [R03]), `MUST` y `IMPORTANT` en skills; sin referencia a RFC 2119 | `MUST`/`SHOULD`/`MAY` al inicio de sentencia (`../../AGENTS.md`) [R04] |
| Manejo de ambigüedad | Preguntar solo si el contexto es críticamente confuso; la guía explícita es "prefer making reasonable decisions to keep momentum". **Sin marcador de incertidumbre** | `[NEEDS CLARIFICATION: ...]` grep-able + MUST preguntar en lugar de interpretar (Principio VII) |
| Validación de consistencia | Dos capas: `openspec validate [--strict]`, determinista sobre estructura de specs y deltas; y `/opsx:verify`, por juicio, en completitud / corrección / coherencia contra el código, con severidades CRITICAL / WARNING / SUGGESTION | Backstop determinista `../../tools/check_docs.py` (ERROR/WARN) + bloque `[SDD-Check]` por entrega |
| Trazabilidad requisito a verificador | Verifica requisito a código y escenario a test **por búsqueda heurística en el momento**, no por un mapeo mantenido; escenario sin cobertura emite WARNING | Campo `Cobertura` del `[SDD-Check]` + regla de propagación (`../../SPECS_REGISTRY.md`) |
| Circuito de aprendizaje | Sobre el contrato, y **automatizado**: archivar fusiona el delta aprobado en la spec vigente. Nada equivalente sobre sus documentos de método | Sobre las specs: propagación bidireccional (Principio III) y `Deuda arrastrada`, ambas manuales |
| Registro de specs | `openspec/specs/<capacidad>/spec.md`, central por capacidad, consultable por CLI (`list`, `show`, `status`); estado implícito en la ubicación (vigente / en cambio / archivado), sin campo `estado` ni nivel SSOT | `../../SPECS_REGISTRY.md` central por documento, con `estado` y `ssot_level` explícitos |
| Personalización | *Schemas* forkeables (`schema init/fork/validate`) que redefinen artefactos y dependencias, más adaptadores generados para más de 30 asistentes | Niveles de profundidad de spec y `ssot_level` |

Lectura del mapeo: convergencia fuerte en lenguaje normativo y en validación de consistencia previa al cierre; convergencia parcial en autoridad, trazabilidad, registro y personalización; divergencia neta en manejo de ambigüedad, donde OpenSpec adopta la postura opuesta a nuestro Principio VII. El veredicto de invariancia leído sobre los cuatro casos vive en `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, no acá.

---

## Conclusiones para Línea B

### C1. La ambigüedad es donde el consenso se rompe

Este proyecto trata "preguntar en vez de interpretar" como principio constitucional (VII). OpenSpec instruye lo contrario de forma explícita: preferir la decisión razonable para mantener el impulso. No es una omisión, es una elección de producto, y viene de un sistema que se dirige a usuarios que quieren velocidad. Vale como recordatorio de que nuestro Principio VII es una **postura defendible, no una obviedad del campo**, y de que su costo —fricción, interrupciones— es real y otros lo pagan al revés. **Lectura**, no cambio propuesto: nada acá sugiere mover el principio.

### C2. La entrega de la instrucción es una dimensión que nuestro instrumento no mide

Las ocho filas describen **qué** dice el método, nunca **cómo llega** al agente. Los cuatro casos difieren en eso y el instrumento no lo ve. Por la regla 2 de `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, la observación se registra fuera de la tabla y sin veredicto: **no** se agrega una novena fila para alojar al caso que la motivó. Si más adelante demuestra importar, abre instrumento v2 y obliga a re-correr los cuatro casos.

### C3. La propagación automatizada es un espejo de nuestro Principio III

Nuestra regla de propagación —los resultados suben al SSOT antes de bajar a sus derivados— es idéntica en intención a `archive`: el delta aprobado se fusiona en la spec vigente y el cambio pasa a histórico. La diferencia es de mecanismo, no de idea: allá lo ejecuta un comando, acá lo ejecuta una persona que se acuerda. Es el segundo linaje independiente que llega a la misma regla, lo cual la refuerza como invariante; y es evidencia de que la parte mecánica es automatizable. **Candidata**, no cambio aprobado: un repositorio documental sin CI (`../../CONSTITUTION.md`) no tiene dónde correr esa automatización hoy, y `../../tools/check_docs.py` verifica forma, no propagación.

### C4. Corpus observacional con procedencia limpia

83 cambios archivados, cada uno con propuesta, diseño, tareas y delta de specs, más 725 commits desde 2025-08-05 y specs vigentes que muestran su estado final. Es el segundo corpus dogfooded del corpus de fuentes y el primero de un linaje que no toca al nuestro, lo cual lo vuelve el candidato más limpio para la línea observacional del backlog (prioridad alta #6). **No dado de alta**: el diseño de ese estudio requiere decidir antes qué se mide, y ese trabajo no está hecho.

### C5. Lo que NO conviene adoptar tal cual

- La postura frente a la ambigüedad (C1): contradice el Principio VII de frente.
- El estado implícito por ubicación en vez de campo `estado`: funciona con un CLI que resuelve rutas, y este repositorio no tiene ninguno.
- La dependencia dura de una herramienta: el método completo de OpenSpec es inejecutable sin el CLI instalado. El nuestro se sostiene en documentos que cualquier asistente lee, y `M-03` apunta justamente a preservar esa portabilidad.

---

[SDD-Check]
- Spec leida: SI (spec registrada en `../../SPECS_REGISTRY.md` para este doc)
- Incluye/Excluye verificado: SI - la lectura cruzada de los cuatro casos queda excluida y remitida a `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`; no se re-analiza el flujo de Spec Kit ni el de Superpowers; no se toman decisiones de adopcion
- Validaciones aplicadas: version anclada en `../../REFERENCIAS.md` [R38]; procedencia declarada antes de la lectura, con la fecha de primer commit verificada en ambos clones vendored; cada rasgo citado declara su archivo de origen o el comando que lo expone; la fuente se presenta sin evidencia de efectividad porque no reporta ninguna; mapeo corrido sobre el instrumento v1 sin agregar filas; la dimension no cubierta se registra fuera de la tabla (C2) por la regla 2 del SSOT de convergencia; refs internas verificadas; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: ninguno (doc operativo)
- Derivados a revisar: ninguno; `CONVERGENCIA-IMPLEMENTACIONES-SDD.md` consume este documento como insumo, no deriva de el
- Cobertura: completa - las cinco conclusiones mapean a filas del mapeo o a secciones de caracterizacion, y cada una declara si es lectura, candidata o cambio aprobado (ninguna lo es)
- Deuda arrastrada: la relacion de OpenSpec con Kiro queda sin resolver y Kiro sigue sin estar en el corpus ni dado de alta en ningun backlog; el corpus observacional de C4 no esta dado de alta; la dimension de C2 queda registrada sin veredicto, a la espera de decidir si abre instrumento v2
- Riesgos/reservas: analisis sobre snapshot v1.7.0 commit `45cca5d`, leyendo skills, docs y config, sin correr el CLI ni un ciclo completo en un proyecto real; fuente autoreportada, con interes comercial y sin ninguna medicion propia; sus comparaciones contra Spec Kit y Kiro son material de posicionamiento y no se usan como insumo del mapeo

---

## Actualizacion: revision contra OpenSpec v1.12.0 (2026-09-05)

Clon vendored movido v1.7.0 `45cca5d` (2026-07-30) → v1.12.0 `e062b95` (2026-09-03), 103 commits y cinco versiones menores. Diff sobre el arbol completo, siguiendo el borrador de M-41.

**Lo analizado no se movio, y en un punto se verifico contra una sospecha previa.** La anatomia `openspec/` es la misma —`git ls-tree 45cca5d openspec/` y el mismo comando sobre `HEAD` devuelven las mismas seis entradas, `initiatives/`, `explorations/` y `work/` incluidas—, asi que la lectura preliminar que las tomo por estructura nueva era falsa y no llego a escribirse. Las 12 skills siguen siendo 12. El argumento de procedencia por fecha, que es lo que sostiene a esta fuente como linaje, no depende de nada que haya cambiado. C1-C5 intactas.

El delta se reparte en tres cosas.

### C6. La primera implementacion del corpus que separa el repositorio de specs del repositorio del artefacto

`docs-lab/multi-repo/stores.md` documenta una capacidad **en beta**: un *store* saca la carpeta `openspec/` del repositorio de codigo y la pone en un repositorio propio, que varios repositorios de codigo comparten. Tras una configuracion por maquina, `status`, `new change` y `archive` operan sobre el store desde cualquier directorio, y el store se comparte por git como cualquier repositorio — las specs reciben ramas y pull requests igual que el codigo. La fuente declara dos motivos de uso: una feature que toca frontend y backend alojados por separado, y un plan que necesita una sola casa en vez de dos mitades.

Es un rasgo nuevo para el corpus: los otros tres casos y este repositorio alojan el metodo **adentro** del artefacto que gobierna. Y toca un problema que este repositorio tiene declarado y sin resolver, no una curiosidad ajena — `../../historial/sdd.md` arrastra desde el 2026-08-23 que «la pieza 3 sigue fuera de este repositorio» para A-04; sdd-first resuelve la frontera con propagacion asistida (`core/sdd_update.py`, `software/analisis/ANALISIS-SDD-FIRST.md` §Actualizacion de instalaciones derivadas); y [R40] es un fork del backstop de acá viviendo en otro repositorio. Tres formas distintas del mismo problema, ninguna con mecanismo.

Dos advertencias, porque la analogia es parcial y conviene no forzarla:

- **La direccion no es la misma.** Un store centraliza specs de varios repositorios de codigo. Acá el caso es al reves: un repositorio de metodo cuyas piezas se ejecutan afuera. El mecanismo puede servir; la forma no se copia.
- **Es beta y autodeclarada.** La fuente no reporta ninguna medicion —de este rasgo ni de ningun otro— y la reserva de [R38] sigue valiendo entera.

**Lectura**, no candidata. Lo que si habilita es una pregunta que el corpus todavia no tiene planteada, y cuyo lugar es `../../agenda/BACKLOG-INVESTIGACION.md`: si la frontera entre el repositorio de specs y el del artefacto es una decision de diseño con consecuencias medibles, o una comodidad de alojamiento. Se señala; no se da de alta acá, porque plantear bien esa pregunta es trabajo propio.

### C7. La fuente reescribe su documentacion a mano y prohibe explicitamente arrastrar texto

`docs-lab/` es un arbol de documentacion nuevo —mas de 40 archivos, el sitio ya construye desde ahi y el `docs/` viejo dejo de usarse— y su README declara la regla de trabajo: «Every page in docs-lab is written by hand, from scratch. The old `docs/` tree is source material for facts, never text to carry over.» Tiene ademas una skill propia para escribirla (`.agents/skills/write-openspec-docs/`, con `writing.md` de estilo y `full-process.md`).

Es una posicion explicita de un proyecto spec-driven sobre su **propia** documentacion, y es la contraria a la regeneracion: los hechos se reutilizan, el texto no. Vale registrarla porque el eje que atraviesa —cuando conviene regenerar un documento y cuando reescribirlo— es el de B-07 en este repositorio, y hasta ahora ninguna de las cuatro fuentes habia declarado postura sobre su propia prosa.

**No se desarrolla acá.** La transferencia a Linea A no esta en el `incluye` de este documento, y la skill de escritura es material de Linea A, no de Linea B. Queda señalado para el backlog, con la misma reserva de siempre: es una politica declarada, sin ninguna medicion detras.

### Nota menor, de la misma familia que M-31

En v1.11.0 la fuente corrigio que `openspec validate` **aprobaba** un `## Purpose` que seguia siendo el placeholder que `archive` escribe: el placeholder supera el piso de 50 caracteres, asi que el unico chequeo pensado para atrapar un Purpose que nadie escribio quedaba satisfecho por el texto exacto que dice que nadie lo escribio. Una spec con `Does stuff.` fallaba en `--strict` y una spec sin nada pasaba.

Es la misma clase que `../../agenda/MEJORAS-METODO.md` M-31 registra acá, y el detalle de su solucion es lo aprovechable: la deteccion es **angosta a proposito** —reconoce el placeholder por la misma definicion que lo escribe, y fuera de eso solo un `TBD`/`TODO` que abra el Purpose—, es WARN y no ERROR para que un proyecto con placeholders en disco siga validando, y el texto entre backticks no cuenta porque un documento que cita el placeholder no lo esta usando. Las cuatro decisiones son transferibles a M-31 sin traer una linea de codigo.

### Y una recurrencia del punto ciego de M-41

`docs-lab/` no aparece en el CHANGELOG: es infraestructura de documentacion, no una entrada de release. Un diff que hubiera leido solo el changelog no lo habria visto, igual que el del 2026-07-10 no vio `spec-persistence.md` en Spec Kit. **Segunda instancia del mismo modo de falla en la misma sesion**, en una fuente distinta, y esta vez evitada porque el procedimiento borrador de M-41 empieza por el arbol completo. Vale como evidencia de que M-41 no describe un descuido puntual.

[SDD-Check] — actualizacion 2026-09-05
- Spec leida: SI (spec de este doc en `../../SPECS_REGISTRY.md`; sin cambio de incluye/excluye)
- Incluye/Excluye verificado: SI — C6 y C7 caen en «conclusiónes accionables para Linea B» y ambas se marcan como lectura; la transferencia a Linea A que C7 haria posible **no se desarrolla**, por no estar en el `incluye`; no se toca la lectura cruzada de los cuatro casos ni se re-analiza ninguna otra fuente
- Validaciones aplicadas: diff corrido sobre el arbol completo antes de mirar ningun archivo esperado (borrador de M-41); la invariancia de la anatomia `openspec/` se verifico con `git ls-tree` en los dos commits y no por lectura, lo que descarto por escrito una sospecha previa; cada rasgo citado declara su archivo de origen en el clon vendored y las dos citas de politica son textuales; la fuente no reporta medicion alguna y eso queda dicho en C6 y en C7; sus comparaciones con otros frameworks no se usaron; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: ninguno (doc `operativo`)
- Derivados a revisar: ninguno registrado. Señalados sin modificar: `../../agenda/MEJORAS-METODO.md` M-31 (las cuatro decisiones de diseño de la deteccion angosta) y `../../agenda/BACKLOG-INVESTIGACION.md` (dos preguntas señaladas y **no** dadas de alta: la frontera entre repositorio de specs y repositorio del artefacto, y la postura sobre reescribir en vez de regenerar documentacion propia)
- Cobertura: **incompleta y declarada** — C6, C7 y la nota de M-31 tienen destino; las dos preguntas de investigacion quedan señaladas sin item, porque plantearlas bien es trabajo propio y darlas de alta a medias es peor que no darlas
- Deuda arrastrada: la del documento original sigue casi intacta (**Kiro ya leido el 2026-09-05, pero la reserva de procedencia que lo nombra sigue abierta y ahora alcanza tambien a Spec Kit**; corpus observacional de C4 sin dar de alta). Se agregan las dos preguntas de arriba, sin item. Sigue abierto de las entradas previas: M-40 sin decidir, M-41 sin escribir, M-42 en Propuesta, `RELACION-SPEC-VS-EPICA.md` sin actualizar, el ecosistema del 1.0 de Spec Kit sin caracterizar, el hueco de `PATRONES.md` del lado del canal de error, y cuanto cuesta frenar sin medir
- Riesgos/reservas: la lectura sale de documentos, skills y changelog del clon, sin correr el CLI ni un store; `stores` es una capacidad **beta** y lo que se describe es lo que la fuente declara, no lo que se verifico funcionando; la analogia de C6 con el problema de este repositorio es parcial y corre en direccion contraria, y eso esta escrito en la propia conclusion

---

## Actualización: revisión contra OpenSpec v1.13.2 (2026-09-30)

Clon vendored movido v1.12.0 `e062b95` (2026-09-03) → `c879d13d` (2026-09-29), 123 commits, con v1.13.0, v1.13.1 y v1.13.2 publicadas y 25 *changesets* todavía sin liberar en `.changeset/`. Diff sobre el árbol completo antes de abrir nada (borrador de M-41): 362 archivos. **La anatomía no se mueve**: `git ls-tree HEAD openspec/` devuelve las mismas seis entradas, las 12 skills siguen siendo las mismas 12 y ninguna se agrega ni se borra. El tramo es, en su enorme mayoría, corrección de bugs y soporte de herramientas nuevas. Esta vez el CHANGELOG sí refleja lo que importa, porque no hay árbol de documentación nuevo: `docs-lab/` sólo tiene modificaciones.

Motivo de la revisión: dejar las cuatro fuentes del corpus en el mismo corte. Spec Kit y Superpowers se re-anclaron el mismo día, y sin OpenSpec la tabla de convergencia mezclaría cortes.

### C8. Dos pasajes defendibles de la misma instrucción producían dos conductas distintas, y la fuente lo arregló en el texto

El caso está en v1.13.1 (#1832, que cierra #1828). La skill `openspec-explore` decía dos veces que, antes de la primera acción que escribe, el agente debía hacer una pregunta de sí o no y esperar la respuesta en otro mensaje. Pero la rama de captura le indicaba pasar «seamlessly» a `openspec new change` sin ningún paso de confirmación. La fuente lo describe así: «Both readings were defensible from the text, so the same "capture this as a change" request either wrote `.openspec.yaml` plus several artifacts immediately or stopped and asked, depending on which passage the agent weighed» (`CHANGELOG.md`, 1.13.1).

La corrección no agregó un control: resolvió la contradicción en el texto. Un pedido explícito de captura cuenta como la confirmación, y sólo para lo que el pedido nombra. Si la propuesta de capturar sale del agente, o el trabajo excede lo pedido, sigue preguntando, y «answers to design or clarifying questions are still never consent to write».

Por qué importa acá: es el primer caso del corpus donde una fuente documenta que **dos pasajes de su propio método que no coincidían hicieron que la conducta del agente dependiera de cuál leyó con más peso**. Es el modo de falla que el Principio I previene del lado de los documentos —una regla dicha dos veces termina dicha de dos maneras—, visto acá del lado de la conducta. **Lectura**, con la reserva de siempre para esta fuente: es un caso, autoreportado y sin medición. Queda señalado para A-04, que mide conducta del agente frente al protocolo, sin proponer nada.

Un matiz para la fila 3 de convergencia, que sale del mismo cambio y de #1940 (v1.13.2): OpenSpec sigue decidiendo ante la ambigüedad —«If context is critically unclear, ask the user - but prefer making reasonable decisions to keep momentum» (`skills/openspec-ff-change/SKILL.md`)—, pero separa esa decisión del **permiso para escribir**, que exige confirmación explícita en `explore`, y de la aprobación del desglose de tareas, que `onboard` pide antes de guardarlo. Resuelve la ambigüedad del contenido sin preguntar, pero no escribe sin consentimiento.

### Tests por grupo de tareas

v1.13.2 (#1955) agrega a la instrucción de tareas que cada grupo entregue los tests y la documentación que su propio trabajo requiere, en vez de dejarlos para un grupo final: «Each task group MUST land the tests and documentation its own work calls for» (`schemas/spec-driven/schema.yaml`). Un grupo cuyo trabajo no los requiere, como el andamiaje, no los lleva. Lo que ya estaba en `e062b95` sigue igual: cada tarea MUST decir cómo se verifica, y el test es una de cuatro formas admitidas. La obligación del test se vuelve más fuerte, pero sigue condicionada a lo que el trabajo requiera.

### Nota menor, otra vez de la familia de M-31

Un *changeset* todavía no liberado (`.changeset/warn-unknown-change-metadata-keys.md`, 2026-09-29) corrige que las claves desconocidas de `.openspec.yaml` se descartaban sin aviso: `status` seguía exigiendo el artefacto de diseño y `validate --strict` salía con 0. Es un verificador en verde sobre una configuración que no había leído, la misma clase que la nota del 2026-09-05. Ahora las nombra y `--strict` falla.

### Una cifra que este análisis heredó sin verificar su fuente

La fila 8 de convergencia y [R38] dicen «62 herramientas» a partir de `docs/supported-tools.md`. Ese árbol quedó abandonado a favor de `docs-lab/` (C7), y `docs-lab/reference/supported-tools.md` es otra tabla, con otro recorte (48 líneas de tabla en `HEAD`, 38 en `e062b95`). El número no se corrige acá porque no se reconcilió qué cuenta cada tabla; queda declarado que el 62 sale del árbol que la fuente ya no mantiene.

[SDD-Check] — actualizacion 2026-09-30
- Spec leida: SI (spec de este doc en `../../SPECS_REGISTRY.md`; sin cambio de incluye/excluye)
- Incluye/Excluye verificado: SI — C8, la nota de tests y la nota menor caen en «conclusiónes accionables para Linea B»; el matiz de la fila 3 se señala para `../CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, que es donde se juzga
- Validaciones aplicadas: diff sobre el árbol completo antes de abrir nada (borrador de M-41); anatomía verificada con `git ls-tree` y conteo de skills sobre el árbol; citas textuales con archivo, o entrada de CHANGELOG y número de PR; lo que ya estaba en `e062b95` se separó con `git show` de lo nuevo
- SSOT afectado: ninguno (doc `operativo`)
- Derivados a revisar: ninguno registrado. Señalados sin modificar: `../CONVERGENCIA-IMPLEMENTACIONES-SDD.md` (matiz de la fila 3, celda de OpenSpec en la dimensión de tests, cifra de la fila 8) y `../../agenda/BACKLOG-INVESTIGACION.md` (C8 como caso para A-04)
- Cobertura: **incompleta y declarada** — el soporte de herramientas nuevas y las correcciones de CLI sin efecto sobre el método no se caracterizan; la cifra de herramientas queda sin reconciliar
- Deuda arrastrada: la de la entrega anterior (corpus observacional de C4 sin dar de alta; las dos preguntas señaladas sin ítem); se agrega la cifra de herramientas sin reconciliar
- Riesgos/reservas: lectura de skills, schema y changelog sin correr el CLI; C8 descansa en la descripción que la propia fuente hace del defecto, sin reproducirlo; 25 *changesets* describen cambios en `main` que ninguna versión publicada trae todavía

---

[SDD-Check] — consolidación de deuda 2026-10-06
- Spec leida: SI (sin cambio de `incluye`/`excluye`: no se toca el cuerpo)
- Incluye/Excluye verificado: SI — sólo se consolida la deuda de los bloques anteriores, que quedan como registro datado y no se reescriben
- Validaciones aplicadas: cada pendiente de los bloques anteriores se clasificó con la regla de `../../AGENTS.md` (`Deuda arrastrada`): resuelto, límite sin remedio, o con destino; lo resuelto se verificó contra la entrega que lo resolvió
- SSOT afectado: ninguno
- Derivados a revisar: ninguno
- Cobertura: completa para la deuda de los bloques anteriores
- Deuda arrastrada: abierta en este documento — **las dos preguntas sin formular** (C6: si separar el repositorio de specs del del artefacto tiene consecuencias medibles; C7: reescribir en vez de regenerar la documentación propia) y la transferencia a Línea A que C7 habilita; se formulan acá antes de darlas de alta, porque darlas de alta a medias es peor que no darlas. **La cifra de herramientas soportadas, sin reconciliar**; la fila 8 de `../CONVERGENCIA-IMPLEMENTACIONES-SDD.md` la toma de acá. Con destino fuera: el corpus observacional de C4 es el ítem #21 de `../../agenda/BACKLOG-INVESTIGACION.md`; M-41 y M-42 siguen en `../../agenda/MEJORAS-METODO.md`; el ecosistema del 1.0 de Spec Kit, en `ANALISIS-SPEC-KIT.md`; cuánto cuesta frenar es el ítem #23. Cerradas: M-40 hecha, `../RELACION-SPEC-VS-EPICA.md` actualizado el 2026-09-05. Pasa a límite: la reserva de procedencia frente a Kiro (búsqueda de marcadores negativa, 2026-09-06)
- Riesgos/reservas: la consolidación lee los bloques anteriores, no re-verifica sus afirmaciones

---

## Actualización: las reglas transversales del proyecto, en el corte vigente (2026-10-09)

Lectura dirigida, **sin mover el corte**: todo lo de abajo se verificó en `c879d13d`, el commit que ya ancla [R38], con `git show` sobre cada archivo citado. El motivo es una pregunta que este análisis no se había hecho: cómo llega al agente una regla que vale para todos los cambios —un estilo, una restricción de arquitectura, una convención—. La respuesta ya estaba en §Flujo de trabajo («las reglas del proyecto viven en `openspec/config.yaml`»); lo que se agrega es por qué la fuente eligió ese mecanismo y cómo se comporta.

### C9. La fuente abandonó el documento de contexto pasivo, y dijo por qué

Antes de `config.yaml`, el contexto del proyecto vivía en `openspec/project.md`, un markdown libre. La guía de migración explica el cambio así: «The old `project.md` was passive—agents might read it, might not, might forget what they read. We found reliability was inconsistent», y lo contrapone a que el `context` nuevo «is **actively injected into every OpenSpec planning request**» (`OpenSpec:docs/migration-guide.md`). El pasaje está en la fuente desde el 2026-01-25 (#574), antes del primer corte de este análisis; no se había leído.

Es la justificación que la propia fuente da del rasgo que este documento destaca en §El rasgo que más aporta y en C2: la instrucción **servida** en vez de leída. Ahí era una lectura de este análisis; acá es la razón declarada por quien lo diseñó. **Lectura**, y con la reserva que esta fuente exige siempre: «we found» no viene acompañado de ninguna medición, así que es una observación del equipo, no un dato. Toca de cerca el problema de este repositorio, que entrega su protocolo como documentos a leer (`../../AGENTS.md`, `../../CONSTITUTION.md`), y queda señalado para A-04 sin proponer nada.

### Cómo se comporta `config.yaml`

Leído en `OpenSpec:src/core/project-config.ts` y `OpenSpec:src/core/artifact-graph/instruction-loader.ts`:

- **`context`** va a las instrucciones de todos los artefactos; **`rules`** se indexa por ID de artefacto y sólo entra en el que coincide. Los dos se entregan como campos aparte, marcados en el código como «constraints for AI, not to be included in output»: son restricciones para quien escribe, no texto para copiar al artefacto.
- **Los IDs de `rules` no se limitan a los del esquema por defecto**: sirven para artefactos de esquemas propios. Una clave que no coincide con ningún artefacto de ningún esquema disponible produce un aviso, no un error.
- **Nada falla.** Un `context` de más de 50KB se ignora con aviso; un campo inválido se descarta con aviso y el resto de la configuración sigue valiendo («Returns partial config if some fields are invalid»).
- **`operations`** agrega una guía consultiva sólo para `apply` y `archive`, separada de las reglas por artefacto.

El propio `openspec/config.yaml` de la fuente sirve de ejemplo de uso: en `context` pone el stack, el lenguaje de producto en que se escriben las specs y los requisitos multiplataforma; en `rules`, reglas concretas por artefacto —escenarios de rutas de Windows en `specs`, verificación en CI de Windows en `tasks`, búsquedas explícitas en vez de patrones en `design`—.

**Lo que esto no hace**, y vale escribirlo: ningún mecanismo comprueba que el artefacto producido cumpla las reglas. La configuración se entrega, no se verifica. Un aviso por una clave inválida es la misma familia que las notas de M-31 de las actualizaciones anteriores, en versión más suave: no hay verificador en verde, porque no hay verificador.

---

[SDD-Check] — actualizacion 2026-10-09
- Spec leida: SI (spec de este doc en `../../SPECS_REGISTRY.md`; sin cambio de incluye/excluye)
- Incluye/Excluye verificado: SI — el comportamiento de `config.yaml` cae en «síntesis del flujo de trabajo» y C9 en «conclusiónes accionables para Linea B»; la comparacion con los otros casos va a `../ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md` §6, en la misma entrega, y no se hace aca
- Validaciones aplicadas: sin mover el corte — cada archivo citado se verifico con `git show c879d13d:<ruta>`, y el commit de origen del pasaje de `project.md` se fecho con `git log -S`; las citas textuales son del codigo y de la guia de migracion en ese commit; «we found» se declara sin medicion; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: ninguno (doc `operativo`)
- Derivados a revisar: `../ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md` — §6 suma las reglas transversales como escenario, en la misma entrega. Señalado sin modificar: `../../agenda/BACKLOG-INVESTIGACION.md`, C9 como caso para A-04, igual que C8
- Cobertura: completa para el mecanismo de reglas transversales; el resto del clon no se releyo
- Deuda arrastrada: ninguna nueva; la del bloque de consolidacion sigue donde vive
- Riesgos/reservas: lectura de codigo y documentacion sin correr el CLI; C9 descansa en lo que la fuente dice de su propia experiencia, sin dato que la respalde
