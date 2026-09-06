# Análisis: OpenSpec y su relación con nuestra investigación SDD (Línea B)

Fecha: 2026-08-02.
Fuente: OpenSpec v1.7.0, commit `45cca5d` (consultada 2026-08-02) [R38]. Clon local vendored en `../../fuentes-externas/OpenSpec/`.
Alcance: Línea B (software).

---

## Contexto

OpenSpec es un sistema de SDD distribuido como CLI de npm (`@fission-ai/openspec`, MIT, respaldo de Fission AI). El agente no lee la metodología de un documento: la pide a la herramienta. Se instala en el proyecto, genera adaptadores para más de 30 asistentes (`../../fuentes-externas/OpenSpec/docs/supported-tools.md`) y expone doce skills sobre un CLI que resuelve rutas, valida estructura y sirve las instrucciones de cada artefacto.

Este documento la caracteriza y la mapea contra nuestro protocolo (`../../AGENTS.md`, `../../SPECS_REGISTRY.md`) con el mismo instrumento de ocho filas que `ANALISIS-SPEC-KIT.md` y `ANALISIS-SUPERPOWERS.md`. La lectura cruzada de los cuatro casos **no** vive acá: su SSOT es `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`.

---

## Procedencia: por qué cuenta como linaje

`CONVERGENCIA-IMPLEMENTACIONES-SDD.md` exige que todo caso nuevo declare su procedencia antes de contarse. Este es el resultado de aplicar ese filtro, y es la sección que decide si el resto del documento tiene valor para el relevamiento.

**Independiente de Spec Kit, por fecha.** El primer commit de OpenSpec es del **2025-08-05** y ya se llama "initialize openspec project structure"; el primer commit del repositorio de Spec Kit es del **2025-08-21**, dieciséis días posterior (ambos verificables en los clones vendored). La anatomía `openspec/specs/` + `openspec/changes/` existía antes de que el repositorio del que podría haberla copiado tuviera historia pública. No hay derivación posible en esa dirección.

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

83 cambios archivados, cada uno con propuesta, diseño, tareas y delta de specs, más 725 commits desde 2025-08-05 y specs vigentes que muestran su estado final. Es el segundo corpus dogfooded disponible en `fuentes-externas/` y el primero de un linaje que no toca al nuestro, lo cual lo vuelve el candidato más limpio para la línea observacional del backlog (prioridad alta #6). **No dado de alta**: el diseño de ese estudio requiere decidir antes qué se mide, y ese trabajo no está hecho.

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
