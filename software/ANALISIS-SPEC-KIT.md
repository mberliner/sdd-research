# Analisis: GitHub Spec Kit y su relacion con nuestra investigacion SDD (Linea B)

Fecha: 2026-05-24.
Fuente: GitHub Spec Kit v0.8.13 (consultada 2026-05-21) [R10]. Clon local vendored en `../fuentes-externas/spec-kit/`.
Alcance: Linea B (software). La transferencia de conceptos a Linea A (docs/investigacion) queda diferida — ver `../06-BACKLOG-INVESTIGACION-FUTURA.md`.

---

## Contexto

Spec Kit ya estaba catalogado como framework de referencia en `../PROYECTOS-LIDERES-Y-FRAMEWORKS.md` [R10], pero solo a nivel de mencion. Este documento analiza el repositorio real para extraer su metodologia operativa, mapearla contra nuestro protocolo SDD (`../AGENTS.md`, `../SPECS_REGISTRY.md`) y derivar conclusiones accionables para Linea B.

Spec Kit es un toolkit open-source de GitHub que materializa SDD mediante una CLI (`specify`) y un conjunto de comandos slash para 30+ agentes de IA. Es **Linea-B-nativo**: todas sus plantillas (`spec`, `plan`, `tasks`, `constitution`, `checklist`) son centradas en software (data-model, contracts, API endpoints, tech stack). No ofrece soporte nativo para documentos de analisis o conocimiento.

---

## Tesis central: "Power Inversion"

El documento de filosofia (`../fuentes-externas/spec-kit/spec-driven.md`) plantea que SDD invierte la jerarquia tradicional: la spec deja de ser andamiaje desechable y se convierte en el **artefacto primario** que genera el codigo; el codigo pasa a ser "la ultima milla" regenerable.

- Mantener software = evolucionar specs.
- Depurar = corregir la spec o el plan que genero codigo incorrecto.
- Pivotar = regenerar desde la spec, no reescribir a mano.

Esta tesis es mas radical que nuestra posicion actual. Nuestro proyecto trata la spec como **mejor representacion actual del conocimiento** (ver `../SDD-ADAPTATIVO-VS-CASCADA.md`), no necesariamente como generador automatico del entregable. La diferencia se discute en Conclusiones.

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
| Fuente de autoridad no-negociable | `memory/constitution.md` + Constitution Check gate | `../CONSTITUTION.md` (desde 2026-07-31) > `../SPECS_REGISTRY.md` > `../AGENTS.md` |
| Lenguaje normativo | `MUST` en FR/plantillas [R04] | `MUST`/`SHOULD`/`MAY` al inicio de sentencia (`../AGENTS.md`) [R04] |
| Manejo de ambiguedad | `[NEEDS CLARIFICATION]` + `/speckit.clarify` (<=5 preguntas) | "MUST preguntar al usuario si la spec tiene ambiguedad" (`../AGENTS.md`, seccion Disambiguacion) |
| Validacion de consistencia | `/speckit.analyze`: duplicacion, ambiguedad, gaps de cobertura, conflictos | Bloque `[SDD-Check]` por entrega + checks post-generacion (`../AGENTS.md`) |
| Trazabilidad requisito->tarea | Coverage mapping FR/SC -> task IDs | Regla de propagacion SSOT -> derivados (`../SPECS_REGISTRY.md`) |
| Circuito de aprendizaje | "Bidirectional Feedback": metricas/incidentes -> spec | Circuitos de aprendizaje y disparadores por tiempo/evento/anomalia (`../SDD-ADAPTATIVO-VS-CASCADA.md`) |
| Registro de specs | Carpeta `specs/[###-feature]/` por feature | `SPECS_REGISTRY.md` central por documento |
| Personalizacion | presets / extensions | niveles de profundidad de spec y `ssot_level` (`../SPECS_REGISTRY.md`) |

La convergencia es alta: ambos llegan independientemente a lenguaje normativo, gate de autoridad, manejo explicito de ambiguedad y validacion de consistencia como proceso continuo (no gate unico). Esto refuerza nuestra hipotesis **B6** (specs como circuito de aprendizaje, ver `LINEAS-INVESTIGACION.md`).

---

## Conclusiones para Linea B

### C1. `/speckit.analyze` valida empiricamente nuestro `[SDD-Check]`

Spec Kit independientemente disenó un comando de consistencia cruzada read-only cuyas pasadas de deteccion (duplicacion, ambiguedad, subespecificacion, conflicto con constitution, gaps de cobertura, inconsistencia) son casi un superconjunto de nuestros checks post-generacion. Esto sugiere que nuestro `[SDD-Check]` esta en el camino correcto, pero es mas debil en **coverage mapping** (mapear cada requisito a su tarea/derivado). Mejora candidata: anadir a `[SDD-Check]` una linea de cobertura "requisitos sin derivado/tarea asociada".

### C2. Marcadores `[NEEDS CLARIFICATION]` son adoptables ya

Nuestro protocolo dice "MUST preguntar al usuario", pero no tiene un marcador estandar para incertidumbre *dentro* del documento. El patron `[NEEDS CLARIFICATION: ...]` de Spec Kit es liviano, grep-able y compatible con nuestro contexto sin CI. Candidato a incorporarse a las convenciones de `../AGENTS.md`.

### C3. La "Power Inversion" es una posicion mas fuerte que la nuestra — y es una tension a investigar

Spec Kit asume specs **ejecutables que generan codigo**. Nuestro proyecto, hoy, trata la spec como representacion del conocimiento, no como generador automatico. Esta no es una deficiencia: es una decision deliberada para contexto sin CI (`../IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md`). Pero plantea una pregunta de investigacion: hasta que punto conviene mover el entregable hacia "regenerable desde spec" vs. "editado a mano con spec como guia". Conecta con el backlog "umbral de control manual a automatizado".

### C4. Constitution Check confirma el valor de un gate de autoridad explicito

El Constitution Check como gate previo a Phase 0 (y re-chequeado tras el diseno) es el equivalente operativo de nuestra precedencia `SPECS_REGISTRY.md`. Spec Kit lo hace *ejecutable* en el flujo del agente; nosotros lo aplicamos por protocolo. Validar si formalizar nuestra precedencia como un paso explicito reduce violaciones.

### C5. Lo que NO conviene adoptar tal cual

- La estructura `specs/[###-feature]/` por feature con branch git automatico asume proyecto de software con git y CI implicito. Nuestro contexto (sin CI, registro central) no se beneficia de fragmentar specs por feature.
- La dependencia de la CLI `specify` y de 30+ integraciones de agentes anade superficie operativa que no necesitamos para un proyecto de investigacion documental.
- El acoplamiento spec->codigo->tests automatico es prematuro mientras no haya experimentos que midan su costo/beneficio en equipos pequenos (backlog: "fatiga operacional por checklists").

---

## Transferencia a Linea A (diferida)

Spec Kit no tiene funcion nativa para documentos de analisis/conocimiento. Los unicos conceptos transferibles a Linea A son `/speckit.checklist` ("unit tests for English": valida completitud y claridad de requisitos en prosa) y el modelo de presets/extensions como via de adaptacion. Esta transferencia se desarrollara solo si Linea B avanza y aporta claridad — registrada como item de backlog en `../06-BACKLOG-INVESTIGACION-FUTURA.md`.

---

[SDD-Check]
- Spec leida: SI (spec propuesta y registrada en SPECS_REGISTRY.md para este doc)
- Incluye/Excluye verificado: SI (foco Linea B; Linea A explicitamente diferida)
- Validaciones aplicadas: refs internas verificadas; cifras/afirmaciones externas con [R04][R09][R10]; sin emoticones; fechas YYYY-MM-DD; no duplica SSOT (referencia PROYECTOS-LIDERES, SDD-ADAPTATIVO, CLAUDE, SPECS_REGISTRY)
- SSOT afectado: ninguno (doc operativo). Enriquece entrada en PROYECTOS-LIDERES-Y-FRAMEWORKS.md (SSOT) por separado
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

**Adoptado en este repositorio (2026-07-31, cambio aprobado):** el patron *invariante en la constitucion, detalle en el SSOT* se porto aca — `../CONSTITUTION.md` v0.1.0 encabeza la precedencia, con siete principios que declaran invariante + `Enforcement` + `Detalle`. Es la parte **declarativa** del patron; la parte **ejecutable** (gate y check deterministas, equivalentes a `tools/check_constitution.py`) sigue sin portarse, y por eso la constitucion declara su enforcement como humano y a pedido. La pregunta de C4 —si formalizar la precedencia reduce violaciones— queda igual de abierta: adoptar el artefacto no la responde.

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
