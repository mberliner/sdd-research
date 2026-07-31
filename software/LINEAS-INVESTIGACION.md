# Lineas de Investigacion (Software)

## B1. Requisitos verificables
Hipotesis: requisitos escritos con criterios de aceptacion testeables reducen defectos de interpretacion.

Base: ingenieria de requisitos y lenguaje normativo [R03], [R04].

## B2. Contract-first
Hipotesis: definir contratos antes de implementar reduce roturas de integracion.

Base: OpenAPI y contract testing [R06], [R08].

## B3. Behavior-first
Hipotesis: escenarios ejecutables (BDD/ATDD) mejoran alineacion negocio-tecnico.

Base: Cucumber/Gherkin [R07].

## B4. IA en ciclo de desarrollo
Hipotesis: IA acelera pero puede degradar estabilidad si no hay guardrails de validacion.

Base: evidencia DORA 2025 y benchmarking reciente [R09], [R16].

## B6. Specs ejecutables como circuito de aprendizaje

Hipotesis: los tests ligados a specs detectan divergencia entre contrato y realidad antes de que llegue a produccion, creando un feedback loop automatico que evita la cascada encubierta.

Preguntas:
- Con que frecuencia los tests revelan que la spec original era incorrecta o incompleta?
- Que mecanismo de actualizacion de spec tras falla de test es menos costoso en equipos pequeños?
- Que diferencia hay en tasa de regresion entre proyectos que actualizan la spec vs los que solo actualizan el codigo?

Base: circuitos de aprendizaje SDD — ver `SDD-ADAPTATIVO-VS-CASCADA.md`. Evidencia de feedback loops en entrega: [R09].

## B5. Gobernanza de cambios
Hipotesis: ADR + politica de versionado + reglas de compatibilidad disminuyen incidentes por cambios mayores.

Base: practicas de arquitectura y contratos [R06], [R08].

## B7. Formato de spec hibrido (anatomia Spec Kit)

Hipotesis: adoptar la anatomia de spec de GitHub Spec Kit (User Story priorizada + FR/SC + Given/When/Then + coverage mapping) sobre un flujo casero mejora la cobertura requisito->derivado, surface ambiguedad antes de codear y aumenta la regenerabilidad del codigo desde la spec, sin un sobrecosto de redaccion que anule la mejora.

Preguntas:
- ~~Cuanto mejora la regenerabilidad (reconstruir el codigo desde la spec sola con minimos errores) vs. specs casero?~~ **RESPONDIDA (2026-07-28) — la mejora no aparecio.** Ver `Estado` abajo.
- El coverage mapping elimina los "requisitos sin derivado" (hueco C1 de `ANALISIS-SPEC-KIT.md`)? **ABIERTA.**
- `[NEEDS CLARIFICATION]` + Given/When/Then reducen revisiones reactivas de spec durante implementacion? **NO RESPONDIBLE TAL COMO ESTA PLANTEADA (2026-07-29).** H2 fue **degradada a descriptiva**: el ratio upfront/reactivo no es computable (`[NEEDS CLARIFICATION]` no existe en la anatomia casero — es `N/A`, no `0`) y su variable de salida esta confundida con el tratamiento (una practica documental altera la visibilidad de su propio resultado; sin git en la ventana del corpus no hay fuente independiente). Queda la lectura **cualitativa**: *que* tuvo que agregar cada brazo despues. Ver `../experimentos/EXPERIMENTO-B7-formato-hibrido.md` §Hipotesis H2 y el anti-patron en `../06-BACKLOG-INVESTIGACION-FUTURA.md` §Prioridad alta 6.

Estado (2026-07-28): la **componente de regenerabilidad** se midio y cerro en **"ajustar / no concluyente"** — en la unica feature que discrimino (F013) el formato **casero** supero al hibrido en R1, R2 y R5, y F001 empato en las cinco metricas; H4 no queda sostenida **ni refutada** (formato confundido con procedencia autentica/traducida, y una sola ronda de reparacion lleva las 4 celdas a 100%). Las otras dos preguntas dependen del **corpus observacional**, que **no se midio**. Resultado: `../experimentos/RESULTADO-EXPERIMENTO-B7.md`; estado del experimento: `PLAN-PRUEBAS.md` §B-07.

Actualizacion (2026-07-29): el **Criterio de exito de B7 fue reformulado** en el SSOT del experimento y ya es **evaluable** — se parte en **(a)** prueba de regenerabilidad (contra `R1`–`R6`, unidad intra-feature, **guarda de confusion** con techo "no atribuible al formato") y **(b)** corpus observacional (contra **H1** y **H3** solamente; comparacion de **medianas con solapamiento declarado** mas sensibilidad *leave-one-out*; techo de conclusion **descriptivo**), con regla de cierre a **dos veredictos**. La unidad de medida quedo definida el 2026-07-29: **cada formato aporta su propia anatomia de requisitos** (casero por aserciones normativas atomicas del cuerpo, hibrido por sus `FR-`/`SC-`), porque el estudio mide los formatos **como se practicaron**; el *Coverage mapping* MUST NOT usarse como instrumento de `H1` porque **es el tratamiento**. Runbook ejecutable: `../experimentos/PRUEBA-OBSERVACIONAL-B7.md`. Aplicado a lo ya ejecutado **no cambia el veredicto** de arriba. Se dio de alta la metrica **`R6`** (verificacion funcional manual) y **H2 quedo degradada a descriptiva**. En consecuencia, cerrar B7 requiere unicamente **medir `H1` y `H3`** sobre el corpus observacional.

Actualizacion (2026-07-30): el corpus observacional esta **en ejecucion** — Fase 0 sellada, Fase 1 completa, inventario de 3 de 7 specs, con tres enmiendas aditivas post-sello y **22 sesiones de extractor restantes** (ver `PLAN-PRUEBAS.md` §B-07 para el estado). El criterio (b) se reforzo: la **variante de sensibilidad de `H1` con unidad neutral** paso del runbook al SSOT del experimento y ahora trae **regla de decision** — coincidencia de direccion descarta la preocupacion por granularidad solo si ambas variantes son estables al *leave-one-out*; **divergencia entre variantes deja `H1` NO CONCLUYENTE**; y se pre-registro un **piso de ruido del instrumento** que tambien puede dejarlo NO CONCLUYENTE. Todo decidido sin ninguna proporcion calculada. Consecuencia para la agenda: la pregunta de cobertura sigue **ABIERTA**, y ahora con probabilidad de veredicto declaradamente menor — es posible que B7 cierre con `H1` sin direccion y eso **no** seria un resultado nulo por falta de datos sino por dependencia del resultado respecto de la convencion de medicion, que es en si un hallazgo sobre medir SDD.

Base: GitHub Spec Kit [R10], lenguaje normativo [R04], "Power Inversion" (C3 de `ANALISIS-SPEC-KIT.md`). Experimento: `../experimentos/EXPERIMENTO-B7-formato-hibrido.md`.
