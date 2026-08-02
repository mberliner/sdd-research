# Análisis: OpenSpec y su relación con nuestra investigación SDD (Línea B)

Fecha: 2026-08-02.
Fuente: OpenSpec v1.7.0, commit `45cca5d` (consultada 2026-08-02) [R38]. Clon local vendored en `../fuentes-externas/OpenSpec/`.
Alcance: Línea B (software).

---

## Contexto

OpenSpec es un sistema de SDD distribuido como CLI de npm (`@fission-ai/openspec`, MIT, respaldo de Fission AI). El agente no lee la metodología de un documento: la pide a la herramienta. Se instala en el proyecto, genera adaptadores para más de 30 asistentes (`../fuentes-externas/OpenSpec/docs/supported-tools.md`) y expone doce skills sobre un CLI que resuelve rutas, valida estructura y sirve las instrucciones de cada artefacto.

Este documento la caracteriza y la mapea contra nuestro protocolo (`../AGENTS.md`, `../SPECS_REGISTRY.md`) con el mismo instrumento de ocho filas que `ANALISIS-SPEC-KIT.md` y `ANALISIS-SUPERPOWERS.md`. La lectura cruzada de los cuatro casos **no** vive acá: su SSOT es `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`.

---

## Procedencia: por qué cuenta como linaje

`CONVERGENCIA-IMPLEMENTACIONES-SDD.md` exige que todo caso nuevo declare su procedencia antes de contarse. Este es el resultado de aplicar ese filtro, y es la sección que decide si el resto del documento tiene valor para el relevamiento.

**Independiente de Spec Kit, por fecha.** El primer commit de OpenSpec es del **2025-08-05** y ya se llama "initialize openspec project structure"; el primer commit del repositorio de Spec Kit es del **2025-08-21**, dieciséis días posterior (ambos verificables en los clones vendored). La anatomía `openspec/specs/` + `openspec/changes/` existía antes de que el repositorio del que podría haberla copiado tuviera historia pública. No hay derivación posible en esa dirección.

**Menciona a Spec Kit y a Kiro, pero para diferenciarse.** Su README los usa como contraste comercial —"heavyweight", "locked into their IDE"— y cita el catálogo de extensiones de Spec Kit como analogía de un mecanismo propio. Eso es posicionamiento de competidor, no herencia de método.

**Los marcadores de difusión conocidos están ausentes.** No hay `[NEEDS CLARIFICATION]`, no hay constitución ni gate de principios, no hay coverage mapping requisito a verificador (verificado por búsqueda sobre el clon completo). Las tres prácticas que este proyecto ya identificó como difusión desde Spec Kit no aparecen.

**Reserva declarada.** La notación `WHEN/THEN` de sus escenarios desciende de Gherkin [R07], ancestro común anterior a los cuatro casos: es herencia compartida, no derivación entre ellos. Lo que queda sin resolver es su relación con Kiro, anunciado el 2025-07-14 y ausente del corpus: tres semanas de anterioridad y un formato de requisitos emparentado no alcanzan para afirmar independencia total. La independencia que este documento sostiene es **respecto de Spec Kit**, que es el linaje relevante para el relevamiento; frente a Kiro queda como límite abierto.

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

- **Disuelve el problema que `M-04` intenta administrar.** `M-04` (`../agenda/MEJORAS-METODO.md`) trata el costo de contexto de los documentos de método, y Superpowers aportó la advertencia de que compactarlos tiene costo conductual medido [R37]. La entrega bajo demanda cambia el planteo: no se compacta el documento, se fragmenta la entrega. Nuestro `AGENTS.md` se inyecta entero en cada sesión aunque el noventa por ciento no aplique al cambio en curso.
- **Cambia dónde puede fallar el cumplimiento.** Con documento leído, el modo de falla es que el agente no lo aplique; con instrucción servida, es que no corra el comando. Es un modo de falla distinto, y —esto importa— **observable desde afuera**: la ausencia de una llamada al CLI se detecta sin juzgar prosa. Es exactamente el tipo de señal independiente del artefacto que la prioridad alta #6 de `../agenda/BACKLOG-INVESTIGACION.md` declara faltante.

Límite que MUST acompañar cualquier uso de esto: OpenSpec **no reporta ninguna medición**, ni interna ni externa, de que su forma de entrega funcione mejor. La ventaja es argumental. A diferencia de [R37], que al menos aporta evals autoreportados, acá no hay ni eso: se porta una idea de diseño, no un resultado.

---

## Mapeo: OpenSpec vs. nuestro protocolo SDD

Se usa el instrumento v1, las mismas ocho filas fijadas el 2026-05-24, sin agregar ni redefinir ninguna para alojar a esta fuente.

| Concepto | OpenSpec | Nuestro proyecto |
|----------|----------|------------------|
| Fuente de autoridad no-negociable | `openspec/config.yaml` (`context` + `rules` por artefacto), servido por el CLI en el momento de escribir. Orden de resolución declarado: flag > metadata del cambio > config del proyecto > default. **Sin constitución ni gate de principios** | `../CONSTITUTION.md` > `../SPECS_REGISTRY.md` > `../AGENTS.md`, leídos por el asistente al inicio de sesión |
| Lenguaje normativo | `SHALL` en requisitos (registro ISO/IEC/IEEE 29148 [R03]), `MUST` y `IMPORTANT` en skills; sin referencia a RFC 2119 | `MUST`/`SHOULD`/`MAY` al inicio de sentencia (`../AGENTS.md`) [R04] |
| Manejo de ambigüedad | Preguntar solo si el contexto es críticamente confuso; la guía explícita es "prefer making reasonable decisions to keep momentum". **Sin marcador de incertidumbre** | `[NEEDS CLARIFICATION: ...]` grep-able + MUST preguntar en lugar de interpretar (Principio VII) |
| Validación de consistencia | Dos capas: `openspec validate [--strict]`, determinista sobre estructura de specs y deltas; y `/opsx:verify`, por juicio, en completitud / corrección / coherencia contra el código, con severidades CRITICAL / WARNING / SUGGESTION | Backstop determinista `../tools/check_docs.py` (ERROR/WARN) + bloque `[SDD-Check]` por entrega |
| Trazabilidad requisito a verificador | Verifica requisito a código y escenario a test **por búsqueda heurística en el momento**, no por un mapeo mantenido; escenario sin cobertura emite WARNING | Campo `Cobertura` del `[SDD-Check]` + regla de propagación (`../SPECS_REGISTRY.md`) |
| Circuito de aprendizaje | Sobre el contrato, y **automatizado**: archivar fusiona el delta aprobado en la spec vigente. Nada equivalente sobre sus documentos de método | Sobre las specs: propagación bidireccional (Principio III) y `Deuda arrastrada`, ambas manuales |
| Registro de specs | `openspec/specs/<capacidad>/spec.md`, central por capacidad, consultable por CLI (`list`, `show`, `status`); estado implícito en la ubicación (vigente / en cambio / archivado), sin campo `estado` ni nivel SSOT | `../SPECS_REGISTRY.md` central por documento, con `estado` y `ssot_level` explícitos |
| Personalización | *Schemas* forkeables (`schema init/fork/validate`) que redefinen artefactos y dependencias, más adaptadores generados para más de 30 asistentes | Niveles de profundidad de spec y `ssot_level` |

Lectura del mapeo: convergencia fuerte en lenguaje normativo y en validación de consistencia previa al cierre; convergencia parcial en autoridad, trazabilidad, registro y personalización; divergencia neta en manejo de ambigüedad, donde OpenSpec adopta la postura opuesta a nuestro Principio VII. El veredicto de invariancia leído sobre los cuatro casos vive en `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, no acá.

---

## Conclusiones para Línea B

### C1. La ambigüedad es donde el consenso se rompe

Este proyecto trata "preguntar en vez de interpretar" como principio constitucional (VII). OpenSpec instruye lo contrario de forma explícita: preferir la decisión razonable para mantener el impulso. No es una omisión, es una elección de producto, y viene de un sistema que se dirige a usuarios que quieren velocidad. Vale como recordatorio de que nuestro Principio VII es una **postura defendible, no una obviedad del campo**, y de que su costo —fricción, interrupciones— es real y otros lo pagan al revés. **Lectura**, no cambio propuesto: nada acá sugiere mover el principio.

### C2. La entrega de la instrucción es una dimensión que nuestro instrumento no mide

Las ocho filas describen **qué** dice el método, nunca **cómo llega** al agente. Los cuatro casos difieren en eso y el instrumento no lo ve. Por la regla 2 de `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, la observación se registra fuera de la tabla y sin veredicto: **no** se agrega una novena fila para alojar al caso que la motivó. Si más adelante demuestra importar, abre instrumento v2 y obliga a re-correr los cuatro casos.

### C3. La propagación automatizada es un espejo de nuestro Principio III

Nuestra regla de propagación —los resultados suben al SSOT antes de bajar a sus derivados— es idéntica en intención a `archive`: el delta aprobado se fusiona en la spec vigente y el cambio pasa a histórico. La diferencia es de mecanismo, no de idea: allá lo ejecuta un comando, acá lo ejecuta una persona que se acuerda. Es el segundo linaje independiente que llega a la misma regla, lo cual la refuerza como invariante; y es evidencia de que la parte mecánica es automatizable. **Candidata**, no cambio aprobado: un repositorio documental sin CI (`../CONSTITUTION.md`) no tiene dónde correr esa automatización hoy, y `../tools/check_docs.py` verifica forma, no propagación.

### C4. Corpus observacional con procedencia limpia

83 cambios archivados, cada uno con propuesta, diseño, tareas y delta de specs, más 725 commits desde 2025-08-05 y specs vigentes que muestran su estado final. Es el segundo corpus dogfooded disponible en `fuentes-externas/` y el primero de un linaje que no toca al nuestro, lo cual lo vuelve el candidato más limpio para la línea observacional del backlog (prioridad alta #6). **No dado de alta**: el diseño de ese estudio requiere decidir antes qué se mide, y ese trabajo no está hecho.

### C5. Lo que NO conviene adoptar tal cual

- La postura frente a la ambigüedad (C1): contradice el Principio VII de frente.
- El estado implícito por ubicación en vez de campo `estado`: funciona con un CLI que resuelve rutas, y este repositorio no tiene ninguno.
- La dependencia dura de una herramienta: el método completo de OpenSpec es inejecutable sin el CLI instalado. El nuestro se sostiene en documentos que cualquier asistente lee, y `M-03` apunta justamente a preservar esa portabilidad.

---

[SDD-Check]
- Spec leida: SI (spec registrada en `../SPECS_REGISTRY.md` para este doc)
- Incluye/Excluye verificado: SI - la lectura cruzada de los cuatro casos queda excluida y remitida a `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`; no se re-analiza el flujo de Spec Kit ni el de Superpowers; no se toman decisiones de adopcion
- Validaciones aplicadas: version anclada en `../REFERENCIAS.md` [R38]; procedencia declarada antes de la lectura, con la fecha de primer commit verificada en ambos clones vendored; cada rasgo citado declara su archivo de origen o el comando que lo expone; la fuente se presenta sin evidencia de efectividad porque no reporta ninguna; mapeo corrido sobre el instrumento v1 sin agregar filas; la dimension no cubierta se registra fuera de la tabla (C2) por la regla 2 del SSOT de convergencia; refs internas verificadas; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: ninguno (doc operativo)
- Derivados a revisar: ninguno; `CONVERGENCIA-IMPLEMENTACIONES-SDD.md` consume este documento como insumo, no deriva de el
- Cobertura: completa - las cinco conclusiones mapean a filas del mapeo o a secciones de caracterizacion, y cada una declara si es lectura, candidata o cambio aprobado (ninguna lo es)
- Deuda arrastrada: la relacion de OpenSpec con Kiro queda sin resolver y Kiro sigue sin estar en el corpus ni dado de alta en ningun backlog; el corpus observacional de C4 no esta dado de alta; la dimension de C2 queda registrada sin veredicto, a la espera de decidir si abre instrumento v2
- Riesgos/reservas: analisis sobre snapshot v1.7.0 commit `45cca5d`, leyendo skills, docs y config, sin correr el CLI ni un ciclo completo en un proyecto real; fuente autoreportada, con interes comercial y sin ninguna medicion propia; sus comparaciones contra Spec Kit y Kiro son material de posicionamiento y no se usan como insumo del mapeo
