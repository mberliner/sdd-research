# Analisis: GitHub Spec Kit y su relacion con nuestra investigacion SDD (Linea B)

Fecha: 2026-05-24.
Fuente: GitHub Spec Kit v0.8.13 (consultada 2026-05-21) [R10].
Alcance: Linea B (software). La transferencia de conceptos a Linea A (docs/investigacion) queda diferida — ver `../../agenda/BACKLOG-INVESTIGACION.md`.

---

## Contexto

Spec Kit ya estaba catalogado como framework de referencia en `../../comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md` [R10], pero solo a nivel de mencion. Este documento analiza el repositorio real para extraer su metodologia operativa, mapearla contra nuestro protocolo SDD (`../../AGENTS.md`, `../../SPECS_REGISTRY.md`) y derivar conclusiones accionables para Linea B.

Spec Kit es un toolkit open-source de GitHub que materializa SDD mediante una CLI (`specify`) y un conjunto de comandos slash para 30+ agentes de IA. Es **Linea-B-nativo**: todas sus plantillas (`spec`, `plan`, `tasks`, `constitution`, `checklist`) son centradas en software (data-model, contracts, API endpoints, tech stack). No ofrece soporte nativo para documentos de analisis o conocimiento.

---

## Tesis central: "Power Inversion"

El documento de filosofia (`spec-kit:spec-driven.md`) plantea que SDD invierte la jerarquia tradicional: la spec deja de ser andamiaje desechable y se convierte en el **artefacto primario** que genera el codigo; el codigo pasa a ser "la ultima milla" regenerable.

- Mantener software = evolucionar specs.
- Depurar = corregir la spec o el plan que genero codigo incorrecto.
- Pivotar = regenerar desde la spec, no reescribir a mano.

Esta tesis es mas radical que nuestra posicion actual. Nuestro proyecto trata la spec como **mejor representacion actual del conocimiento** (ver `../../comun/SDD-ADAPTATIVO-VS-CASCADA.md`), no necesariamente como generador automatico del entregable. La diferencia se discute en Conclusiones.

---

## Flujo de trabajo de Spec Kit

Seis comandos nucleo y varios opcionales, ejecutados como slash commands del agente:

| Orden | Comando | Funcion | Artefacto |
|-------|---------|---------|-----------|
| 1 | `/speckit.constitution` | Principios de gobernanza del proyecto, no-negociables | `memory/constitution.md` |
| 2 | `/speckit.specify` | Define el *que/por que*: user stories priorizadas (P1/P2/P3), criterios de aceptacion Given/When/Then | `spec.md` |
| 3 | `/speckit.clarify` (opcional) | Reduce ambiguedad con hasta 5 preguntas dirigidas, antes de planificar | edita `spec.md` |
| 4 | `/speckit.plan` | Traduce a arquitectura/stack. Incluye **Constitution Check** como gate | `plan.md`, `research.md`, `data-model.md`, `contracts/` |
| 5 | `/speckit.tasks` | Deriva tareas ejecutables; marca `[P]` las paralelizables | `tasks.md` |
| 6 | `/speckit.analyze` (opcional) | Analisis read-only de consistencia cruzada spec/plan/tasks/constitution | reporte (no escribe) |
| 7 | `/speckit.implement` | Ejecuta las tareas y construye | codigo |
| 8 | `/speckit.converge` (opcional) | Evalua el codebase actual contra spec/plan/tasks y **anade como tareas nuevas** el trabajo aun no construido, para que `implement` lo complete | edita `tasks.md` |

> Nota de versión: la tabla refleja el snapshot v0.8.13. `/speckit.converge` se añadió en upstream v0.11.2 (2026-06; documentado en v0.11.10) — relevante para SDD sobre *codebases existentes* (Línea B legacy): cierra la brecha entre lo especificado y lo ya construido reponiéndola como tareas, en lugar de asumir greenfield. Ver `historial/sdd.md`, entrada 2026-07-10.

Rasgos de diseno relevantes:

- **Lenguaje normativo**: las plantillas usan `MUST` en requisitos funcionales (FR-001, FR-002...) — alineado con RFC 2119 [R04].
- **Marcadores de incertidumbre**: `[NEEDS CLARIFICATION: ...]` explicita lo no resuelto dentro de la spec, en vez de que el agente asuma.
- **User stories independientes**: cada historia es un slice testeable de forma aislada (MVP incremental).
- **Criterios de exito medibles** (SC-001...): tecnologicamente agnosticos y cuantificables.
- **Constitution como autoridad**: en `/speckit.analyze`, todo conflicto con un principio MUST de la constitution es CRITICAL y obliga a ajustar spec/plan/tasks, no a diluir el principio.
- **Extensibilidad**: *presets* (sobreescriben plantillas/terminologia sin tocar el tooling) y *extensions* (anaden comandos/fases). Es el mecanismo por el que podria adaptarse a otros dominios.

---

## La constitution: uso general y variacion por dominio

`memory/constitution.md` es el documento de gobernanza que produce `/speckit.constitution`: una lista de principios no-negociables que el agente lee en cada comando posterior (especialmente como gate en `/speckit.plan` y `/speckit.analyze`, ver C4). Se ejecuta una sola vez, al inicio del proyecto, antes de `/speckit.specify`.

**Contenido tipico** [R28] [R32]:
- preferencias/restricciones tecnologicas (librerias aprobadas, dependencias prohibidas, versiones de lenguaje)
- requisitos de seguridad (autenticacion, validacion de inputs, manejo de secretos)
- principios arquitectonicos (simplicidad, anti-abstraccion, integration-first, library-first, test-first)
- estandares de documentacion y de equipo

**No es generica: la evidencia muestra que se especializa por dominio**, no por una plantilla unica:
- *Cloud/Azure*: seguridad con Managed Identity/Key Vault, costos, observabilidad (Application Insights/OpenTelemetry), IaC con Bicep [R31].
- *Sitios estaticos*: minimas dependencias, sin servicios externos, contenido en Markdown [R32].
- *Sistemas con autenticacion*: reglas concretas tipo "todo endpoint requiere auth, secretos nunca commiteados, >80% cobertura, bcrypt para passwords" — la misma feature ("sistema de auth") produce resultados distintos con vs. sin esa constitution [R32].

Esto refuerza la lectura de C4 (mas abajo): el valor no esta en *tener* una constitution generica, sino en que sea **especifica al dominio y verificable como gate**. Para Linea B esto sugiere que, si se adopta o porta el concepto, la constitution del proyecto testigo deberia redactarse a medida del stack y los riesgos reales de ese proyecto — no copiarse de un ejemplo externo.

---

## Mapeo: Spec Kit vs. nuestro protocolo SDD

| Concepto | Spec Kit | Nuestro proyecto |
|----------|----------|------------------|
| Fuente de autoridad no-negociable | `memory/constitution.md` + Constitution Check gate | `../../CONSTITUTION.md` (desde 2026-07-31) > `../../SPECS_REGISTRY.md` > `../../AGENTS.md` |
| Lenguaje normativo | `MUST` en FR/plantillas [R04] | `MUST`/`SHOULD`/`MAY` al inicio de sentencia (`../../AGENTS.md`) [R04] |
| Manejo de ambiguedad | `[NEEDS CLARIFICATION]` + `/speckit.clarify` (<=5 preguntas) | "MUST preguntar al usuario si la spec tiene ambiguedad" (`../../AGENTS.md`, seccion Disambiguacion) |
| Validacion de consistencia | `/speckit.analyze`: duplicacion, ambiguedad, gaps de cobertura, conflictos | Bloque `[SDD-Check]` por entrega + checks post-generacion (`../../AGENTS.md`) |
| Trazabilidad requisito->tarea | Coverage mapping FR/SC -> task IDs | Regla de propagacion SSOT -> derivados (`../../SPECS_REGISTRY.md`) |
| Circuito de aprendizaje | "Bidirectional Feedback": metricas/incidentes -> spec | Circuitos de aprendizaje y disparadores por tiempo/evento/anomalia (`../../comun/SDD-ADAPTATIVO-VS-CASCADA.md`) |
| Registro de specs | Carpeta `specs/[###-feature]/` por feature | `SPECS_REGISTRY.md` central por documento |
| Personalizacion | presets / extensions | niveles de profundidad de spec y `ssot_level` (`../../SPECS_REGISTRY.md`) |

Hay coincidencias notables entre las dos columnas, pero **este documento no es el lugar donde se juzga la convergencia**: leer un mapeo pareado como evidencia de invariancia sobreestima lo que un solo par puede mostrar. El veredicto sobre qué elementos son invariantes entre implementaciones independientes, contado por linajes y con las divergencias al mismo peso, vive en `CONVERGENCIA-IMPLEMENTACIONES-SDD.md` (SSOT del tema desde 2026-08-02).

> **Corrección 2026-08-02.** Hasta esta fecha el párrafo afirmaba que la convergencia era alta y que eso reforzaba la hipótesis **B6**. Ambas partes quedaron acotadas al leer un tercer caso independiente [R37]: el manejo de ambigüedad por marcador resultó **difusión desde un solo origen**, no convergencia independiente, y la inferencia hacia B6 no se sostiene —B6 afirma un mecanismo causal, y el acuerdo entre frameworks es evidencia de consenso, no de eficacia. Detalle en `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`.

---

## Conclusiones para Linea B

### C1. `/speckit.analyze` valida empiricamente nuestro `[SDD-Check]`

> **Estado del hueco de cobertura (2026-07-31).** B-07 (b) intento medir si el formato hibrido produce
> menos requisitos sin verificador: `H1` resulto **NO CONCLUYENTE**, luego **el hueco C1 sigue abierto** —
> pero ya no por falta de datos. El motivo medido es que la **direccion de `H1` depende de la convencion de
> conteo** y que el **piso de ruido del instrumento es de 5 a 8 veces la brecha** buscada. Consecuencia
> para C1: el *coverage mapping* se conserva por su valor de metodo y MUST NOT presentarse como practica
> con superioridad de cobertura medida. Ver `../../experimentos/b07-formato-hibrido/RESULTADO-EXPERIMENTO-B7.md` §Resultado del
> criterio (b).

Spec Kit independientemente disenó un comando de consistencia cruzada read-only cuyas pasadas de deteccion (duplicacion, ambiguedad, subespecificacion, conflicto con constitution, gaps de cobertura, inconsistencia) son casi un superconjunto de nuestros checks post-generacion. Esto sugiere que nuestro `[SDD-Check]` esta en el camino correcto, pero es mas debil en **coverage mapping** (mapear cada requisito a su tarea/derivado). Mejora candidata: anadir a `[SDD-Check]` una linea de cobertura "requisitos sin derivado/tarea asociada".

### C2. Marcadores `[NEEDS CLARIFICATION]` son adoptables ya

Nuestro protocolo dice "MUST preguntar al usuario", pero no tiene un marcador estandar para incertidumbre *dentro* del documento. El patron `[NEEDS CLARIFICATION: ...]` de Spec Kit es liviano, grep-able y compatible con nuestro contexto sin CI. Candidato a incorporarse a las convenciones de `../../AGENTS.md`.

### C3. La "Power Inversion" es una posicion mas fuerte que la nuestra — y es una tension a investigar

> **Precision del 2026-09-05.** Esta conclusion quedo doblemente acotada. Primero por C6: el manifiesto de Spec Kit afirma la inversion y su documentacion de referencia declara que **no impone** ningun modelo de persistencia. Y despues desde afuera: existe un caso del corpus que **si** regenera codigo desde la spec —Tessl [R46], `tessl build`, con el archivo generado marcado `// GENERATED FROM SPEC - DO NOT EDIT`, ubicado por [R20] como el unico que «is even exploring the spec-as-source level of SDD»— y no es Spec Kit. Al citar «la posicion mas fuerte» MUST nombrarse a quien se le atribuye: **la fuente que la enuncia y la que la ejerce no son la misma** (`ANALISIS-TESSL.md`, C1).
>
> **Nota del 2026-10-09.** «Si regenera» vale hasta el **2025-11-14**: ese dia Tessl pauso su *Framework* y lo saco de la CLI, y ya estaba pausado cuando se escribio la precision de arriba (`ANALISIS-TESSL.md` §Actualización: cuándo cambió el producto). Desde entonces **ningun caso del corpus ejerce la posicion fuerte**: Spec Kit la enuncia y nadie la practica. La precision sigue valiendo en su forma —nombrar a quien se le atribuye la posicion—, y ahora la respuesta honesta a «quien la ejerce» es «nadie, desde esa fecha».

Spec Kit asume specs **ejecutables que generan codigo**. Nuestro proyecto, hoy, trata la spec como representacion del conocimiento, no como generador automatico. Esta no es una deficiencia: es una decision deliberada para contexto sin CI (`../../comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md`). Pero plantea una pregunta de investigacion: hasta que punto conviene mover el entregable hacia "regenerable desde spec" vs. "editado a mano con spec como guia". Conecta con el backlog "umbral de control manual a automatizado".

### C4. Constitution Check confirma el valor de un gate de autoridad explicito

El Constitution Check como gate previo a Phase 0 (y re-chequeado tras el diseno) es el equivalente operativo de nuestra cadena de precedencia, que desde 2026-07-31 encabeza `../../CONSTITUTION.md` y sigue con `../../SPECS_REGISTRY.md` y `../../AGENTS.md`. Spec Kit lo hace *ejecutable* en el flujo del agente; nosotros lo aplicamos por protocolo. Validar si formalizar nuestra precedencia como un paso explicito reduce violaciones.

### C5. Lo que NO conviene adoptar tal cual

- La estructura `specs/[###-feature]/` por feature con branch git automatico asume proyecto de software con git y CI implicito. Nuestro contexto (sin CI, registro central) no se beneficia de fragmentar specs por feature.
- La dependencia de la CLI `specify` y de 30+ integraciones de agentes anade superficie operativa que no necesitamos para un proyecto de investigacion documental.
- El acoplamiento spec->codigo->tests automatico es prematuro mientras no haya experimentos que midan su costo/beneficio en equipos pequenos (backlog: "fatiga operacional por checklists").

---

## Transferencia a Linea A (diferida)

Spec Kit no tiene funcion nativa para documentos de analisis/conocimiento. Los unicos conceptos transferibles a Linea A son `/speckit.checklist` ("unit tests for English": valida completitud y claridad de requisitos en prosa) y el modelo de presets/extensions como via de adaptacion. Esta transferencia se desarrollara solo si Linea B avanza y aporta claridad — registrada como item de backlog en `../../agenda/BACKLOG-INVESTIGACION.md`.

---

[SDD-Check]
- Spec leida: SI (spec propuesta y registrada en SPECS_REGISTRY.md para este doc)
- Incluye/Excluye verificado: SI (foco Linea B; Linea A explicitamente diferida)
- Validaciones aplicadas: refs internas verificadas; cifras/afirmaciones externas con [R04][R09][R10]; sin emoticones; fechas YYYY-MM-DD; no duplica SSOT (referencia PROYECTOS-LIDERES, SDD-ADAPTATIVO, CLAUDE, SPECS_REGISTRY)
- SSOT afectado: ninguno (doc operativo). Enriquece entrada en ../comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md (SSOT) por separado
- Derivados a revisar: ninguno
- Riesgos/reservas: analisis basado en snapshot v0.8.13; conclusiones C1-C2 son candidatas a mejora, no cambios aprobados de protocolo

---

## Actualizacion: C4 validado empiricamente en el testigo (2026-05-26)

El proyecto testigo `agent-test-suite` (hoy `evaluador-flujo-intent`; ver `PLAN-PRUEBAS.md`) implemento el patron que C4 dejaba como pregunta abierta: formalizo un documento de principios no-negociables (`CONSTITUTION.md`) y un Constitution Check ejecutable (`tools/check_constitution.py`) como primer paso de su pipeline local. Es la primera evidencia operativa de "formalizar la precedencia como un paso explicito" en el contexto SDD del proyecto.

Diferencias con el Constitution Check de Spec Kit [R10], relevantes para Linea B:

- **Gate de integridad, no de contenido.** El check del testigo no evalua si el codigo respeta los principios (eso lo siguen haciendo el linter de naming, `lint-imports` y los tests); verifica que la constitucion sea coherente: cada principio referencia un SSOT que existe y su enforcement automatico esta cableado en el pipeline. Es una version liviana de la *consistency propagation* de `/speckit.constitution` (paso 4 del skill), no del gate de Phase 0.
- **Invariante en la constitucion, detalle en el SSOT.** Cada principio declara la afirmacion estable y referencia el documento donde vive la regla completa (nomenclatura -> spec de naming; capas -> ADR de arquitectura). Evita duplicacion divergente y resuelve la ambiguedad de "donde esta el contenido canonico" — un riesgo que el modelo de constitution-by-reference introduce si no se separa invariante de detalle.
- **Constitucion vs. arranque del agente.** El testigo mantuvo su archivo de protocolo del asistente como punto de arranque (referencia la constitucion, no la contiene), de modo que la constitucion sobreviva a un cambio de asistente IA. Refuerza C4: el gate de autoridad es del proyecto, no del agente.

Implicacion para nuestro propio marco: formalizar la precedencia `SPECS_REGISTRY.md` como un paso ejecutable (no solo protocolo en `AGENTS.md`) tiene ahora un precedente operativo de bajo costo. Sigue siendo mejora candidata, no cambio aprobado; su evaluacion formal como experimento propio queda fuera de este analisis (candidato de backlog, hermano de B-07 pero sobre gobernanza, no formato).

**Adoptado en este repositorio (2026-07-31, cambio aprobado):** el patron *invariante en la constitucion, detalle en el SSOT* se porto aca — `../../CONSTITUTION.md` v0.1.0 encabeza la precedencia, con siete principios que declaran invariante + `Enforcement` + `Detalle`. Es la parte **declarativa** del patron; la parte **ejecutable** (gate y check deterministas, equivalentes a `tools/check_constitution.py`) sigue sin portarse, y por eso la constitucion declara su enforcement como humano y a pedido. La pregunta de C4 —si formalizar la precedencia reduce violaciones— queda igual de abierta: adoptar el artefacto no la responde.

**Respaldo upstream (v0.11.6+):** Spec Kit hizo explicito en su filosofia que los articulos IV, V y VI de su constitucion de ejemplo son *project-defined governance* — slots que cada proyecto rellena, no principios prescritos por el framework [R10] (`spec-driven.md`, "Articles IV, V & VI: Project-Defined Governance"; commit `3cfc81f`). Es una aclaracion de docs, no de comportamiento (la plantilla `constitution-template.md` ya era 100% placeholders en v0.8.13), y **converge con la posicion del testigo**: la estructura la fija el framework, el contenido no-negociable lo posee el proyecto. Corrobora C4 y el enfoque "gate de autoridad del proyecto, no del agente". Ademas, `/speckit.analyze` evalua la constitucion *concreta*, de modo que los articulos project-defined participan de los compliance checks igual que los prescritos — el mismo mecanismo de *consistency propagation* que el gate de integridad del testigo aplica en version liviana.

[SDD-Check] — actualizacion 2026-05-26
- Spec leida: SI (spec registrada en SPECS_REGISTRY.md para este doc; sin cambio de incluye/excluye)
- Incluye/Excluye verificado: SI (la actualizacion cae en "conclusiones accionables para Linea B"; Linea A sigue diferida)
- Validaciones aplicadas: refs internas verificadas; afirmacion externa anclada en [R10]; sin emoticones; fechas YYYY-MM-DD; no duplica SSOT (referencia al testigo, no copia su contenido)
- SSOT afectado: ninguno (doc operativo)
- Derivados a revisar: ninguno — la adopcion de constitucion en el testigo no toca las specs del experimento B-07 (formato), su baseline ni sus brazos
- Cobertura: completa — la actualizacion de C4 mapea a la implementacion del testigo (`CONSTITUTION.md` + `tools/check_constitution.py` + paso en pipeline)
- Deuda arrastrada: evaluar si la formalizacion de la precedencia merece experimento propio (candidato de backlog sobre gobernanza); EXPERIMENTO-B7 NO se modifica (fuera de su alcance de formato)
- Riesgos/reservas: evidencia de 1 proyecto testigo derivado de este (sesgo de confirmacion, declarado en B-06); analisis base sobre snapshot Spec Kit v0.8.13

---

## Actualizacion: revision contra Spec Kit v0.12.11 (2026-07-10)

Clon vendored actualizado v0.8.13 → v0.12.11.dev0. Diff dirigido: ninguna conclusion (Power Inversion, C1-C5) invalidada. Dos incorporaciones:

- **`/speckit.converge`** (nuevo, v0.11.2): añadido a la tabla de comandos como opcional. Relevante a Linea B legacy (cierra brecha spec↔codebase existente reponiendola como tareas).
- **Articulos IV-VI project-defined** (v0.11.6): nota de respaldo upstream añadida a la seccion C4/testigo — corrobora el enfoque "gate de autoridad del proyecto".

Detalle del diff completo en `historial/sdd.md` (entrada 2026-07-10).

[SDD-Check] — actualizacion 2026-07-10
- Spec leida: SI (spec de este doc en SPECS_REGISTRY.md; sin cambio de incluye/excluye)
- Incluye/Excluye verificado: SI (cae en "conclusiones accionables para Linea B"; Linea A sigue diferida)
- Validaciones aplicadas: afirmaciones externas ancladas en [R10] con commit/version verificados en fuente vendored; refs internas verificadas; fechas YYYY-MM-DD; no duplica SSOT
- SSOT afectado: ninguno (doc operativo; REFERENCIAS.md e historial/sdd.md actualizados por separado)
- Derivados a revisar: DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md y COMPARATIVA-SPECKIT-VS-TESTIGO.md — verificar si el set de comandos o el modelo de constitucion citados requieren alinear con v0.12.11
- Cobertura: completa para las dos incorporaciones (a: converge en tabla; b: nota de respaldo en C4)
- Deuda arrastrada: R33/R34/R30/R25 sin verificar en fuente completa (independiente de este doc)
- Riesgos/reservas: diff basado en CHANGELOG + spec-driven.md; snapshot conceptual sigue anclado a v0.8.13, actualizaciones marcadas con su version de origen

---

## Actualizacion: revision contra Spec Kit v1.0.5.dev0 (2026-09-05)

Clon vendored movido v0.12.11.dev0 `983a87f` (2026-07-10) → v1.0.5.dev0 `4a7341a` (2026-09-04), 560 commits, con el **1.0.0 liberado el 2026-08-21**. Ninguna conclusion (Power Inversion, C1-C5) queda invalidada, y por una razon verificable y no por lectura: **`spec-driven.md` es byte a byte identico** al del corte anterior (`git diff 983a87f..HEAD -- spec-driven.md` sale vacio). La tesis central y los nueve articulos son los mismos textos que este documento analizo. El set de comandos tampoco se movio: los diez de la tabla siguen ahi, `converge` incluido.

Lo que cambio esta en otro lado, y son tres cosas de peso muy distinto.

### El corpus conceptual crecio en un directorio que el diff anterior no miraba

`docs/concepts/` reune hoy cuatro documentos. `sdd.md` es `spec-driven.md` con otro titulo. Los otros tres son material conceptual nuevo: `spec-persistence.md` (2026-06-09), `spec-of-specs.md` y `complex-features.md` (ambos 2026-07-22).

**`spec-persistence.md` ya estaba en el arbol el 2026-07-10 y el diff de esa fecha no lo vio.** Su propio `[SDD-Check]` declara el metodo que lo explica: «diff basado en CHANGELOG + spec-driven.md». Un documento agregado sin linea de changelog es invisible a ese procedimiento, y este lo era. Es la misma clase de defecto que `sdd-first:docs/PATRONES.md` llama «la carpeta que existe y ningun paso mira»: no falla, calla. Consecuencia de metodo dada de alta en `../../agenda/MEJORAS-METODO.md` M-41.

### C6. Spec Kit adopta la taxonomia de [R30] y declara que **no fuerza** ninguno de sus tres niveles

`docs/concepts/spec-persistence.md` cita el articulo de Fowler que este proyecto usa como [R30] y reproduce sus tres niveles —spec-first, spec-anchored, spec-as-source—; es decir, la fuente y el analista comparten instrumento, no solo practica. Y sobre esa taxonomia la fuente toma posicion explicita: «Spec Kit intentionally leaves teams in control of what happens to `spec.md`, `plan.md`, and `tasks.md` after requirements change [...] **None is the default, and none is required by Spec Kit**».

Eso califica a C3. C3 lee la Power Inversion como «una posicion mas fuerte que la nuestra» —specs ejecutables que generan codigo— y construye sobre esa lectura una pregunta de investigacion. La lectura sigue siendo correcta **para `spec-driven.md`**, que no cambio. Lo que hay ahora es una **tension adentro de la fuente**: su documento de filosofia afirma la inversion, y su documentacion de referencia declara que el modelo de persistencia es convencion de equipo y que el toolkit no impone ninguno. C3 no se retira; se le agrega que la posicion fuerte es la del manifiesto y no la del producto, y que citarla sin esa distincion sobre-atribuye.

### C7. El eje de mutacion es ortogonal al temporal, y nuestra comparacion ya operaba en el sin nombrarlo

El mismo documento agrega una segunda pregunta, que declara separada de la de [R30]: que pasa con el conjunto de artefactos cuando cambian los requisitos. Tres modelos: **flow-back** (se edita cualquier artefacto y despues se reconcilia; riesgo, divergencia silenciosa), **flow-forward** (los artefactos completados son inmutables y un requisito nuevo abre una carpeta nueva; costo, duplicacion), y **living spec** (se edita `spec.md` y lo derivado se regenera; riesgo, perder el razonamiento que vivia en lo derivado).

`COMPARATIVA-SPECKIT-VS-TESTIGO.md` compara «carpeta por feature» contra «registro central» y concluye que optimizan ejes distintos —el trabajo contra el sistema—. Ese es exactamente el eje de mutacion, y ahora tiene vocabulario upstream: la carpeta por feature es flow-forward, el registro central esta del lado de living spec. La comparacion no se invalida; gana un nombre que no tuvo que inventar. **Es convergencia de instrumento y MUST NOT contarse como convergencia de linaje**: `CONVERGENCIA-IMPLEMENTACIONES-SDD.md` sigue siendo su SSOT y su conteo no se toca.

### Correccion sobre `--require-spec`

El relevamiento previo a este diff marco `--require-spec` (#4367) como candidato a respaldar `M-02`. El diff lo desmiente: `scripts/python/check_prerequisites.py` lo documenta como «Require spec.md to exist (for analysis phase)» y lo unico que hace es fallar si el archivo no esta antes de la fase de analisis. Es una precondicion de fase, no un gate de autoria: no mira quien edita, ni que se edita, ni si la spec tiene contenido. **No respalda M-02**, cuyo criterio de contenido sigue viniendo de sdd-first (C3 de `ANALISIS-SDD-FIRST.md`).

### Lo que el 1.0 agrega y este analisis NO caracteriza

Entre v0.12 y v1.0.4 la superficie que mas crecio no es el flujo SDD sino la plataforma alrededor: extensiones, presets, bundler, catalogos de comunidad con modelo de confianza declarado, workflows y events. El CHANGELOG del tramo es mayoritariamente eso. **No esta caracterizado acá**, y la razon es de alcance: la spec de este documento incluye el flujo y el mapeo, no el ecosistema de distribucion. Donde si pesa es en `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md`, que comparo adoptar contra portar sobre un snapshot donde nada de eso existia — queda señalado, sin modificar.

### Revision de derivados (regla de propagacion)

- **`COMPARATIVA-SPECKIT-VS-TESTIGO.md`** — revisado. No hay contradiccion: el set de comandos y el modelo de constitucion que cita siguen vigentes. Lo que gana es el vocabulario de C7, y eso es una edicion propia, no una correccion.
- **`RELACION-FR-VS-SC-Y-COBERTURA.md`** — revisado. El delta no toca la cardinalidad FR↔SC ni el modelo de cobertura. Sin impacto.
- **`RELACION-SPEC-VS-EPICA.md`** (no es derivado registrado, pero el hallazgo lo alcanza) — su §Estado de la discusion externa afirma que «la posicion dominante es la de contencion/inversion de jerarquia», con la spec conteniendo historias, y que no se hallo fuente que sostenga la equivalencia estricta. `docs/concepts/spec-of-specs.md` no la sostiene tampoco, pero **escribe la epica por encima de la spec**: un roadmap descompone una feature grande —que el documento llama «the epic»— en sub-specs, cada una con su propio ciclo. Es la direccion contraria a la contencion, condicionada al tamaño. La fuente ademas ordena esa opcion como **la mas cara de cuatro** en `complex-features.md`, a usar solo cuando las otras tres no alcanzan. **Requirió actualizar ese documento**, y se hizo el 2026-09-05 en una entrega propia: su spec se enmendó para poner el encuadre general por delante y la evidencia de implementaciónes después, y la afirmación de «posición dominante» se retiró. Ver `RELACION-SPEC-VS-EPICA.md` §8.

[SDD-Check] — actualizacion 2026-09-05
- Spec leida: SI (spec de este doc en `../../SPECS_REGISTRY.md`; sin cambio de incluye/excluye)
- Incluye/Excluye verificado: SI — C6 y C7 caen en «conclusiónes accionables para Linea B»; el ecosistema de extensiones del 1.0 queda declarado como fuera de alcance en vez de caracterizado a medias; el veredicto de convergencia no se toca (vive en `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`); Linea A sigue diferida
- Validaciones aplicadas: la no-invalidacion de la tesis central se verifico con `git diff 983a87f..HEAD -- spec-driven.md` (vacio) y no por lectura comparada; cada documento citado declara su ruta en el clon vendored y su fecha de alta; la cita de `spec-persistence.md` es textual; el candidato `--require-spec` se verifico en el script y se reporta la correccion en vez de dejarla caer; refs internas verificadas con `../../tools/check_docs.py`; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: este documento (`ssot_level: SSOT`)
- Derivados a revisar: **revisados los dos registrados** — `COMPARATIVA-SPECKIT-VS-TESTIGO.md` (sin contradiccion; gana vocabulario de C7) y `RELACION-FR-VS-SC-Y-COBERTURA.md` (sin impacto). Fuera del registro de derivados: `RELACION-SPEC-VS-EPICA.md` **actualizado el 2026-09-05**, con enmienda de spec, y `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` queda señalado por el ecosistema del 1.0
- Cobertura: **incompleta y declarada** — C6, C7, la correccion de `--require-spec` y la consecuencia de metodo (M-41) tienen destino; el ecosistema de extensiones/presets del 1.0 queda sin caracterizar por alcance; la actualizacion de `RELACION-SPEC-VS-EPICA.md` queda sin ejecutar
- Deuda arrastrada: R33/R34/R30/R25 sin verificar en fuente completa (independiente de este doc); se agrega una: **el ecosistema del 1.0 sin caracterizar** (la de `RELACION-SPEC-VS-EPICA.md` se salda el 2026-09-05 en entrega propia) con su efecto sobre `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` sin evaluar
- Riesgos/reservas: el diff leyo CHANGELOG, `git diff` sobre los documentos conceptuales y los scripts citados, sin correr el CLI ni un ciclo completo; el snapshot conceptual del cuerpo del documento sigue anclado a v0.8.13 y cada actualizacion queda marcada con su version de origen; C6 describe una tension entre dos documentos de la misma fuente y no una posicion declarada por ella — la fuente no dice en ningun lado que su manifiesto y su referencia difieran

---

## Actualización: revisión contra Spec Kit v1.0.14.dev0 (2026-09-30)

Clon vendored movido v1.0.5.dev0 `4a7341a` (2026-09-04) → v1.0.14.dev0 `d2ddd910` (2026-09-30), 172 commits; la última versión liberada del tramo es la 1.0.13 (2026-09-29). Nadie hizo `git pull` a propósito: el movimiento se detectó porque un informe externo sobre la combinación Spec Kit + Superpowers, ajeno al repositorio, citaba el clon en `987c9b8b`, que ya había quedado siete commits atrás. El informe no se usa como fuente.

Procedimiento, el borrador de M-41 completo: `git diff --stat 4a7341a..HEAD` sobre el árbol entero (591 archivos) antes de abrir nada, y `git diff 4a7341a..HEAD -- spec-driven.md`, que **sale vacío**. La tesis central y los nueve artículos siguen siendo el texto analizado, y C1-C7 quedan en pie. El grueso del tramo vuelve a ser plataforma —`src/specify_cli/` (bundles, extensiones, integraciones, presets, workflows) y sus tests—, que sigue fuera de alcance. Fuera del código de la CLI cambian las diez plantillas de comando, con ajustes chicos, y aparecen cinco guías y dos referencias nuevas en `docs/`. Una de esas guías es la que importa.

### C8. La fuente se usa a sí misma para una feature, y no conserva sus specs

`docs/guides/agentic-sdlc.md` (alta el 2026-09-28) es un caso de estudio de cómo se desarrolla Spec Kit, y es la primera vez que la fuente describe su propia práctica en vez de la del usuario. Lo que dice, textual:

- **El SDD completo se usó en una feature.** «The bundler feature used Spec Kit's SDD process to produce its specification, plan, and tasks» (junio de 2026), y la guía lo presenta como «evidence of SDD dogfooding for that feature». Los cambios acotados van por issue y PR: «For a bounded change, that may be enough; it does not have to become an SDD `spec.md`».
- **Las specs no se versionan.** «Generated `specs/` artifacts are normally gitignored; the linked commit preserves a historical snapshot». El `.gitignore` del repositorio ya excluía `specs/` en `4a7341a`: lo nuevo no es la práctica, es que la fuente la declare.
- **La adopción no se midió.** La guía cierra con «the timeline shows adoption rather than measured time savings».

Esto extiende C6 sin cambiarle el signo. C6 encontró que el manifiesto afirma la Power Inversion y que la referencia (`spec-persistence.md`) deja la persistencia a criterio de cada equipo. Ahora la tercera pieza —lo que el proyecto hace consigo mismo— cae del lado de la referencia: en su propio repositorio, la spec es entrada del ciclo de una feature grande y después no se conserva. En la taxonomía de [R20] esa práctica es *spec-first*, que es exactamente el nivel que el manifiesto dice superar. **La reserva que MUST acompañar esta lectura**: la guía describe la práctica de un proyecto open-source con un modelo de confianza particular y aclara que «Spec Kit's production mix is not a prescribed recipe»; no es una recomendación al usuario, y no dice que el nivel *anchored* no funcione, sólo que este proyecto no lo usa para sí.

Señalado sin tocar, porque la lectura cruzada no vive acá: OpenSpec se desarrolla con su propio corpus de specs vigentes y cambios archivados (`ANALISIS-OPENSPEC.md`). Los dos casos quedan en posiciones opuestas sobre la misma pregunta, y eso es materia de `../CONVERGENCIA-IMPLEMENTACIONES-SDD.md`.

### Ajustes de plantilla que no llegan a conclusión

Todos leídos en `git diff 4a7341a..HEAD -- templates/commands/`:

- **`converge`** deja de fiarse de las casillas: «completion claims are not evidence». Verifica el comportamiento actual contra spec, plan, tareas y constitución, y busca tanto lo incumplido como la implementación que «contradicts, exceeds, or falls outside the stated intent». Ataca el mismo defecto que domina los arreglos de sdd-first leídos en `ANALISIS-SDD-FIRST.md` C8 —un verificador que da por hecho lo que no verificó—, esta vez del lado de la fuente.
- **`tasks`** manda citar textual en la tarea toda restricción de `data-model.md` (largo máximo, nulabilidad, enums, reglas de validación), para que no quede a criterio de quien implementa.
- **`clarify`** achica lo que se puede diferir a planificación: sólo lo que es de método de implementación, comparación de stack o desglose de tareas.
- **`constitution`** declara que el *Sync Impact Report* es material temporal para revisar la enmienda, «not governance content», y que se borra antes de commitear la constitución enmendada. Nuestro procedimiento de enmienda hace lo contrario: la trazabilidad vive en `../../historial/sdd.md` y se conserva.

### Lo que no es del delta y este documento no decía

- **Los tests son opcionales**: «Tests are OPTIONAL: Only generate test tasks if explicitly requested in the feature specification or if user requests TDD approach» (`spec-kit:templates/commands/tasks.md`). Ya estaba en `4a7341a`. Este documento sólo registraba *test-first* como principio de la constitución de ejemplo, y las dos cosas no son lo mismo: la constitución lo propone y la plantilla de tareas no lo aplica salvo que se pida.
- **La extensión `bug`** (assess, fix, test) también estaba en `4a7341a`, y es parte del ecosistema que sigue sin caracterizarse. La guía nueva agrega un dato sobre ella: los workflows de bugs del propio repositorio «do not consume Spec Kit's bundled `bug` extension».

### Lo que el delta agrega y este análisis NO caracteriza

`docs/guides/contract-driven-development.md` (2026-09-17), que se engancha al flujo desde `docs/concepts/sdd.md`; los *bundles* `assess` y `bugfix` con sus workflows; y el resto de la plataforma. Siguen fuera por alcance, con su efecto sobre `../DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` sin evaluar.

### Revisión de derivados (regla de propagación)

- **`../COMPARATIVA-SPECKIT-VS-TESTIGO.md`** — revisado. Sin contradicción: C8 es consistente con la lectura de la carpeta por feature como efímera frente al registro central, y no cambia ningún dato del documento.
- **`../RELACION-FR-VS-SC-Y-COBERTURA.md`** — revisado. Sin impacto: el delta no toca la relación FR↔SC ni el modelo de cobertura.

[SDD-Check] — actualizacion 2026-09-30
- Spec leida: SI (spec de este doc en `../../SPECS_REGISTRY.md`; sin cambio de incluye/excluye)
- Incluye/Excluye verificado: SI — C8 y los ajustes de plantilla caen en «síntesis del flujo» y «conclusiónes accionables para Linea B»; el ecosistema sigue fuera por alcance; la lectura cruzada con OpenSpec queda señalada para su SSOT, no hecha acá
- Validaciones aplicadas: borrador de M-41 completo (`git diff --stat` sobre el árbol entero y `git diff -- spec-driven.md`, vacío); cada cita es textual y declara su archivo; lo que ya estaba en `4a7341a` se verificó con `git show` y se separó del delta; el informe externo que disparó la revisión no se cita
- SSOT afectado: este documento (`ssot_level: SSOT`)
- Derivados a revisar: **revisados los dos registrados** — `../COMPARATIVA-SPECKIT-VS-TESTIGO.md` (sin contradicción) y `../RELACION-FR-VS-SC-Y-COBERTURA.md` (sin impacto). Señalados sin modificar: `../CONVERGENCIA-IMPLEMENTACIONES-SDD.md` (C8 contra el dogfooding de OpenSpec; el contraste entre tests opcionales y TDD obligatorio, que no tiene fila) y `../ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md` §5 (el nivel de Spec Kit en la taxonomía, a la luz de C8)
- Cobertura: **incompleta y declarada** — C8, los ajustes de plantilla y los dos hechos previos tienen destino; la guía de contratos, los bundles y el resto de la plataforma quedan sin caracterizar por alcance
- Deuda arrastrada: R33/R34/R30/R25 sin verificar en fuente completa (independiente de este doc); el ecosistema sin caracterizar, ahora con una guía conceptual más, y su efecto sobre `../DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` sin evaluar
- Riesgos/reservas: lectura de plantillas, guías y `.gitignore`, sin correr el CLI; C8 se apoya en lo que el proyecto declara de sí mismo, y un caso de estudio escrito por la fuente puede seleccionar lo que muestra; el clon es un directorio vivo y volvió a moverse mientras se escribía otra fuente

---

## Lectura externa: [R35] sobre Spec Kit (2026-10-06)

[R35] es una revisión multivocal que evalúa Spec Kit como la instancia más completa de su modelo de gobernanza, y lo hace con la reserva por delante: sin validación académica independiente. Es la única evaluación externa del corpus con datos de campo, y los datos son de un **piloto ilustrativo**, no de un experimento: cuatro meses, tres equipos de una misma organización, catorce ingenieros de nivel medio y senior, comparación antes/después sin grupo de control.

Su hallazgo cualitativo central, textual: «Spec Kit did not eliminate the PRP. It shifted its locus». El esfuerzo de verificación pasó de inspeccionar tarde código generado y opaco a invertir antes en specs y constituciones.

**Lectura.** Es la forma que toma en la práctica la tensión de C3: si la spec pasa a ser el artefacto primario, lo que se ahorra en revisar código se paga en escribir y revisar specs. [R35] lo observa sin medirlo, así que no confirma ni refuta C3; muestra dónde mirar. La cifra de costo de autoría que el mismo trabajo da vive en `../../comun/ESTADISTICAS-TENDENCIAS-EVOLUCION.md`, con su reserva.

[SDD-Check] — lectura externa 2026-10-06
- Spec leida: SI (spec de este doc en `../../SPECS_REGISTRY.md`; sin cambio de incluye/excluye: es lectura para «conclusiónes accionables para Linea B»)
- Incluye/Excluye verificado: SI — no se reproduce el modelo de gobernanza de [R35], solo lo que dice de Spec Kit
- Validaciones aplicadas: cita textual y datos del piloto verificados en el LaTeX de [R35] (§Illustrative Pilot Study)
- SSOT afectado: este documento (`ssot_level: SSOT`)
- Derivados a revisar: `../COMPARATIVA-SPECKIT-VS-TESTIGO.md` y `../RELACION-FR-VS-SC-Y-COBERTURA.md` — sin impacto: la lectura no toca la comparación pareada ni la relación FR↔SC
- Cobertura: completa para lo que [R35] afirma de Spec Kit
- Deuda arrastrada: la del documento sigue intacta
- Riesgos/reservas: el piloto es ilustrativo y de una sola organización; el hallazgo es cualitativo

---

[SDD-Check] — consolidación de deuda 2026-10-06
- Spec leida: SI (sin cambio de `incluye`/`excluye`: no se toca el cuerpo)
- Incluye/Excluye verificado: SI — sólo se consolida la deuda de los bloques anteriores, que quedan como registro datado y no se reescriben
- Validaciones aplicadas: cada pendiente de los bloques anteriores se clasificó con la regla de `../../AGENTS.md` (`Deuda arrastrada`): resuelto, límite sin remedio, o con destino; lo resuelto se verificó contra la entrega que lo resolvió
- SSOT afectado: ninguno
- Derivados a revisar: ninguno
- Cobertura: completa para la deuda de los bloques anteriores
- Deuda arrastrada: abierta en este documento — **el ecosistema del 1.0 sin caracterizar**, y su efecto sobre `../DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` sin evaluar; si la formalización de la precedencia merece experimento propio, candidato señalado el día de su bloque y nunca dado de alta. Con destino fuera: [R33], [R34], [R30] y [R25] sin verificar en fuente completa, deuda de `../../REFERENCIAS.md` y no de este documento
- Riesgos/reservas: la consolidación lee los bloques anteriores, no re-verifica sus afirmaciones

---

## Actualización: cómo llegan al flujo las reglas transversales (2026-10-09)

Lectura dirigida, **sin mover el corte**: todo lo de abajo se verificó en `d2ddd910`, el commit que ya ancla [R10], con `git show` sobre cada archivo citado. La pregunta es cómo hace Spec Kit para que una regla que vale para todas las features —un estilo de interfaz, una restricción de arquitectura, una convención— llegue a cada spec y cada plan.

Responderla obliga a entrar en una parte del ecosistema que las actualizaciones del 2026-09-05 y del 2026-09-30 dejaron fuera por alcance. La spec de este documento se enmendó antes de escribir para incluir **sólo esa parte** —resolución de la constitución, composición de presets, hooks y presets de gobernanza—; el bundler, los workflows y las integraciones siguen fuera.

### La constitución se lee en cada ejecución, y la propagación pasó a ser opcional

El comando del núcleo lo declara en su guarda de alcance: «Dependent templates and commands read the constitution at runtime and are not modified here» (`spec-kit:templates/commands/constitution.md`). Hasta el 2026-07-28 el mismo comando propagaba la constitución a las plantillas; ese día dejó de hacerlo (#3790), y dos días después la propagación volvió como preset **opcional**, `constitution-sync` (#3873).

El README de ese preset explica por qué se sacó: «Propagation was removed deliberately — it duplicates the constitution as the source of truth and can fight the composition stack». Y precisa qué pasa sin él: `plan`, `tasks` y `analyze` «still read the live constitution every run» (`spec-kit:presets/constitution-sync/README.md`). Con el preset instalado, la constitución generada se re-materializa cuando cambia la pila de presets, pero sólo si nadie la editó a mano.

**Lectura.** El motivo que da la fuente es el de nuestro Principio I: una copia de la regla en otro archivo es una segunda fuente de verdad que termina divergiendo. Y responde algo que C4 dejaba abierto desde el comienzo: el gate de autoridad no se apoya en una copia de la constitución dentro de la plantilla, sino en el archivo vivo leído en cada comando.

### C9. Las reglas transversales tienen dos canales, y para una organización la fuente recomienda los presets

**Primer canal: la constitución**, con su gate en la plantilla de plan y su severidad CRITICAL en `analyze` (§Mapeo, C4).

**Segundo canal: los presets.** Son pilas de overrides de plantillas, comandos y scripts, ordenadas por prioridad; entre presets gana el número más bajo. Por defecto un archivo reemplaza entero al de abajo, pero plantillas y comandos también pueden componerse: «**prepend** places preset content before lower-priority content, **append** places it after lower-priority content, and **wrap** replaces `{CORE_TEMPLATE}` with lower-priority content» (`spec-kit:docs/reference/presets.md`). La misma página les asigna el propósito que importa acá: «enforce organizational standards». Y el README de `constitution-sync` dice cuál de los dos canales recomienda la fuente para gobernar muchos repositorios: una política que un equipo central «owns, versions, and audits… in one place», en un preset versionado, en vez de copias congeladas por repositorio.

**Los hooks de las extensiones** se atan a eventos del ciclo —`after_specify`, `after_plan`, `after_tasks`, `after_implement`, `before_analyze`— y son opcionales por defecto: `optional: boolean # Default: true` (`spec-kit:extensions/EXTENSION-API-REFERENCE.md`).

**El catálogo de comunidad ya trae reglas transversales empaquetadas.** De los 40 presets de comunidad en `d2ddd910`, varios son de gobernanza por tema: `a11y-governance` («WCAG 2.2 AA, accessible status output…»), `architecture-governance` («STRIDE/CAPEC threat modeling, arc42/S-ADR guidance, Zero Trust…»), `isaqb-architecture-governance`, `security-governance`, `test-first-governance` y `db-standards` (`spec-kit:presets/catalog.community.json`). **Ninguno de los 40 está marcado como verificado**, y la fuente advierte que «Catalog discovery does not audit or endorse community code» (`spec-kit:docs/guides/agentic-sdlc.md`). De estos presets se leyó sólo la descripción del catálogo, no su contenido.

**Lectura**: para la pregunta de cómo imponer estilos o arquitectura a todas las specs, Spec Kit responde con el mismo mecanismo con el que se personaliza todo lo demás, no con un registro de reglas propio. La regla vive en el texto de una plantilla compuesta, y nada verifica que el artefacto la cumpla, salvo que esté escrita como principio de la constitución.

### La constitución del propio proyecto usa ese canal para su guía de UX

`.specify/memory/constitution.md` es la constitución con la que se desarrolla Spec Kit. Tiene cinco principios, y el III, «CLI & User-Experience Consistency», es una guía de UX escrita como principio: vocabulario de verbos compartido («New verbs MUST NOT be invented when an existing one fits»), convenciones de salida, JSON limpio en `--json`, y acciones destructivas que muestran el cambio antes de confirmar. Su §Governance los vuelve vinculantes: «Principles I–V are binding gates», con la Constitution Check del plan, CRITICAL en `analyze` y «Unjustified violations block merge» (`spec-kit:.specify/memory/constitution.md`).

**Nota menor, de la familia del Principio I.** La misma constitución exige que toda enmienda «MUST propagate to dependent templates and command guidance in the same change». Se escribió el 2026-06-19 (#3070), antes de que el núcleo dejara de propagar, y no se tocó después. La regla del propio proyecto quedó describiendo un modelo que la herramienta abandonó: lo que el README de `constitution-sync` llama duplicación y deriva, dentro de la fuente.

### Lo que sigue sin caracterizar

El bundler, los workflows, las integraciones y el contenido de los presets de gobernanza, del que sólo se leyó la descripción. Y el efecto de todo el ecosistema sobre `../DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md`, que sigue sin evaluarse.

### Revisión de derivados (regla de propagación)

- **`../COMPARATIVA-SPECKIT-VS-TESTIGO.md`** — revisado. Sin contradicción: describe la Constitution Check como gate de contenido y los presets como mecanismo de adaptación, y las dos cosas siguen valiendo.
- **`../RELACION-FR-VS-SC-Y-COBERTURA.md`** — revisado. Sin impacto.

[SDD-Check] — actualizacion 2026-10-09
- Spec leida: SI, y **enmendada antes de escribir**: `incluye` suma la parte del ecosistema que gobierna como llegan al flujo las reglas transversales, y deja escrito que el resto de la plataforma sigue fuera
- Incluye/Excluye verificado: SI — la constitucion, los presets, los hooks y los presets de gobernanza caen en el `incluye` enmendado; C9 en «conclusiónes accionables para Linea B»; la comparacion con los otros casos va a `../ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md` §6, en la misma entrega, y no se hace aca
- Validaciones aplicadas: sin mover el corte — cada archivo citado se verifico con `git show d2ddd910:<ruta>`; las fechas de #3070, #3790 y #3873 salen de `git log` en ese commit; el conteo de presets de comunidad y su estado de verificacion salen de leer el catalogo en ese commit; de los presets de gobernanza se declara que solo se leyo su descripcion; las citas son textuales y declaran su archivo; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: este documento (`ssot_level: SSOT`) y `../../SPECS_REGISTRY.md` (enmienda de su spec)
- Derivados a revisar: **revisados los dos registrados** — `../COMPARATIVA-SPECKIT-VS-TESTIGO.md` (sin contradiccion) y `../RELACION-FR-VS-SC-Y-COBERTURA.md` (sin impacto). `../ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md` §6 suma las reglas transversales como escenario en la misma entrega. Señalado sin modificar: `../DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md`
- Cobertura: **incompleta y declarada** — la parte del ecosistema que toca reglas transversales queda caracterizada; bundler, workflows, integraciones y el contenido de los presets de gobernanza siguen sin leer
- Deuda arrastrada: el ecosistema del 1.0 queda **caracterizado en parte**: lo que sigue abierto es el resto de la plataforma y su efecto sobre `../DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md`. La formalizacion de la precedencia como experimento sigue como estaba
- Riesgos/reservas: lectura de plantillas, documentacion, catalogo y constitucion, sin correr el CLI ni instalar un preset; la recomendacion de presets versionados es de la fuente sobre si misma, no un resultado; el clon sigue moviendose (56 commits despues de `d2ddd910` el 2026-10-09) y este bloque no los lee

---

[SDD-Check] — nota sobre Tessl en C3 2026-10-09
- Spec leida: SI (sin cambio de `incluye`/`excluye`)
- Incluye/Excluye verificado: SI — nota fechada dentro de C3, sin reescribir la precision del 2026-09-05; la caracterizacion del cambio de Tessl vive en `ANALISIS-TESSL.md`
- Validaciones aplicadas: fecha del cambio tomada de [R46]; la nota no reformula C3, solo actualiza quien ejerce la posicion fuerte
- SSOT afectado: este documento (`ssot_level: SSOT`)
- Derivados a revisar: `../COMPARATIVA-SPECKIT-VS-TESTIGO.md` y `../RELACION-FR-VS-SC-Y-COBERTURA.md` — sin impacto: ninguno menciona a Tessl
- Cobertura: completa para la mencion de Tessl
- Deuda arrastrada: la del bloque anterior de este mismo dia
- Riesgos/reservas: ninguno nuevo
