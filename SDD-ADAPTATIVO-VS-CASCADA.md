# SDD Adaptativo: Circuitos de Aprendizaje y el Riesgo de Cascada Encubierta

## Premisa

SDD no es un proceso de una sola pasada. Una spec creada al inicio de un proyecto no puede capturar todo el conocimiento relevante, porque parte de ese conocimiento emerge durante la ejecucion.

Cuando SDD se aplica sin mecanismos de retroalimentacion, degenera en lo que este documento llama "cascada encubierta": se mantiene la apariencia de metodo estructurado, pero el conocimiento queda congelado en la spec inicial y los ciclos de aprendizaje no existen.

## Anti-patron: Cascada Encubierta

### Definicion

Cascada encubierta ocurre cuando:
- La spec se define al inicio con toda la informacion disponible.
- No hay ciclos formales para revisarla ni actualizarla durante el proyecto.
- Los aprendizajes del proyecto no se propagan de vuelta hacia la spec.
- Los derivados (documentos, tests, codigo) evolucionan, pero la spec permanece estatica.

### Señales de alarma

- Specs activas que no se han modificado durante una "ventana de inactividad" sin justificacion (ver definicion abajo).
- Documentos derivados que divergen de su SSOT sin que se haya actualizado la spec.
- Preguntas del equipo sobre "lo que dice la spec" en lugar de "lo que aprendimos".
- Decisiones tomadas fuera del registro (sin ADR, sin actualizacion de spec).
- Resistencia a modificar la spec porque "ya fue aprobada".

### Ventana de inactividad (umbral relativo a la velocidad)

La señal de congelamiento MUST medirse en **iteraciones del proyecto, no en tiempo de calendario fijo**. Un umbral absoluto (p.ej. 30 dias) solo discrimina en proyectos de cadencia mensual; en proyectos que iteran en horas o dias nunca se gatilla aunque haya congelamiento real.

- Criterio recomendado: una spec activa sin tocar durante **2-3 iteraciones o ciclos de cierre** del proyecto es candidata a revision.
- Equivalencias de referencia: cadencia mensual ≈ 30 dias; cadencia semanal ≈ 1 semana; cadencia por iteracion rapida ≈ N iteraciones.

Hallazgo de respaldo: experimento B-06 (`experimentos/RESULTADO-EXPERIMENTO-B6.md`) mostro que un proyecto testigo que itera en horas vuelve inutil el umbral absoluto de 30 dias.

### Por que ocurre

La cascada encubierta surge de confundir estabilidad de la spec (deseable) con inmutabilidad (anti-patron). Una spec debe ser la mejor representacion actual del conocimiento del proyecto, no un contrato cerrado.

## Circuitos de Aprendizaje en SDD

### Principio

Un circuito de aprendizaje es un ciclo explicito: ejecutar -> observar -> actualizar spec -> ejecutar. SDD solo es sostenible si incluye mecanismos regulares de retroalimentacion que permitan que las specs reflejen lo que el proyecto aprende [R03].

### Tipos de disparo

| Tipo | Cuando ocurre | Accion sobre specs |
|------|--------------|-------------------|
| Por tiempo | Cadencia fija (semanal, quincenal, mensual) | Revision de specs activas |
| Por evento | Experimento cerrado, decision tomada, cambio de contexto | Actualizacion del SSOT afectado |
| Por anomalia | Derivado diverge de SSOT; hallazgo contradice la spec | Reconciliacion forzada |

### Cadencia sugerida (punto de partida)

- Revision rapida de specs activas: cada 2 semanas en proyectos activos.
- Revision completa de SSOTs: al cerrar un experimento o mensual si no hay cierres.
- Revision de derivados: cada vez que se modifica el SSOT del que dependen.

La cadencia correcta es una variable del proyecto, no un estandar fijo. SHOULD ajustarse segun velocidad de cambio y costo de divergencia detectada.

### Mecanismos en este proyecto

- El ciclo hipotesis -> experimento -> resultado -> revision de `LINEAS-INVESTIGACION.md` es el circuito de aprendizaje primario.
- El bloque `[SDD-Check]` al final de cada entrega es un micro-circuito de retroalimentacion por sesion.
- El campo `estado: Borrador/Activo/Deprecado` en specs explicita el ciclo de vida del conocimiento.
- El historial en `historial/sdd.md` registra la evolucion del sistema como evidencia de que los circuitos funcionan.
- El campo **`Deuda arrastrada`** del bloque `[SDD-Check]` (ver `AGENTS.md`) lista lo diferido en cada entrega y MUST re-explicitarse en las siguientes hasta resolverse. Es el mecanismo anti-cascada mas directo: convierte el pendiente en un artefacto obligatorio y grep-able en lugar de depender de que alguien lo recuerde. Distingue deuda de producto (se resuelve rapido) de deuda de tooling/entorno (persiste, señal de alarma leve). Derivado del experimento B-06 (`experimentos/RESULTADO-EXPERIMENTO-B6.md`, hallazgo 2 y propuesta 1), que lo identifico como "el instrumento que mas claramente previene la cascada encubierta" en el proyecto testigo.

## SDD vs Cascada: Comparativa

### Que evitar de cascada

| Anti-patron cascada | Por que es danino en SDD |
|---------------------|--------------------------|
| Big Design Up Front — toda la spec antes de empezar | Congela conocimiento incierto; la spec pierde vigencia antes de usarse |
| Fases secuenciales sin retorno | Impide corregir errores de spec hasta que el costo es alto |
| Aprobacion formal que cierra el ciclo | Genera resistencia a actualizar la spec cuando cambia el contexto |
| Documentacion como artefacto de entrega, no de trabajo | Specs que se escriben para cumplir y luego se ignoran |
| Separacion rigida entre quien especifica y quien ejecuta | Elimina el feedback de quien detecta los problemas reales |
| Exito medido por cobertura documental, no por decision habilitada | Incentiva burocracia en lugar de utilidad |

### Que es indiferente hoy

| Practica asociada a cascada | Por que es indiferente en SDD |
|-----------------------------|-------------------------------|
| Escribir specs antes de implementar | SDD tambien lo hace; el problema no es el orden sino la rigidez |
| Usar documentacion formal | El problema no es la formalidad sino la falta de ciclo de revision |
| Tener fases distinguibles | Las fases son utiles; el problema es la unidireccionalidad |
| Involucrar stakeholders al inicio | Tambien deseable en SDD; el problema es solo involucrarlos al inicio |
| Definir criterios de exito por adelantado | SDD lo conserva y lo requiere |

### Que retiene SDD de procesos estructurados

- Explicitar el alcance antes de actuar (campos `incluye`/`excluye`).
- Trazabilidad de decisiones y sus razones (ADR, registro de historial).
- Definicion de criterios de exito antes de ejecutar, no post-hoc.
- Separacion entre SSOT y derivados para reducir contradicciones.

### Aclaracion: invertir la jerarquia no es anticipar el conocimiento

Un SDD **generativo** —donde la spec es el artefacto primario que genera el codigo y el codigo es "ultima milla" regenerable (la "Power Inversion"; ver `software/ANALISIS-SPEC-KIT.md` [R10])— se confunde a veces con Big Design Up Front. No lo es. La inversion afecta la **jerarquia** (la spec manda sobre el codigo), no el **momento** en que se adquiere el conocimiento.

- Un SDD generativo sigue siendo iterativo: incorpora feedback bidireccional (la realidad de produccion -> evolucion de la spec), descompone el alcance en slices incrementales y usa marcadores de incertidumbre (`[NEEDS CLARIFICATION]`) en vez de suposiciones [R03][R10].
- Lo que exige no es conocer **todo el producto** por adelantado, sino que el conocimiento **disponible para cada slice** este explicito y desambiguado en la spec antes de generar ese slice. Es "spec completa por slice", no "spec completa del producto".
- Por lo tanto, la regenerabilidad (codigo desde spec) es **ortogonal** al eje adaptativo/cascada: un SDD generativo cae en cascada encubierta exactamente igual que cualquier otro si sus specs se congelan y no se reconcilian con lo aprendido. El anti-patron es de **uso** (ausencia de circuito de aprendizaje), no de la inversion de jerarquia en si.

Corolario practico: al evaluar un enfoque SDD, separar dos preguntas que suelen mezclarse — "¿la spec genera el codigo?" (jerarquia/regenerabilidad) y "¿la spec se actualiza con lo aprendido?" (adaptativo vs. cascada). Solo la segunda determina el riesgo de cascada encubierta.

## Implicaciones por linea

### Linea A (docs e investigacion)

El riesgo de cascada es alto cuando el marco teorico se define al inicio y no se actualiza con los resultados de los experimentos. El circuito de aprendizaje primario es: hipotesis en `LINEAS-INVESTIGACION.md` -> experimento en `experimentos/` -> resultado -> revision de la hipotesis y sus specs derivadas.

### Linea B (software)

El riesgo de cascada es alto en specs de API o contratos que se congelan tras la primera aprobacion. El circuito de aprendizaje primario es el feedback de tests ligados a specs: cada falla de test es una señal de que la spec o la implementacion deben actualizarse. Los ADR registran el aprendizaje de decisiones tecnicas [R09].

## Señales de salud del circuito de aprendizaje

- Al menos un SSOT activo fue modificado en las ultimas 2 semanas en un proyecto en curso.
- Los experimentos cerrados derivaron en actualizaciones de `LINEAS-INVESTIGACION.md`.
- El campo `excluye` de alguna spec fue refinado desde su creacion (indica que el alcance fue puesto a prueba).
- Hay entradas en `historial/sdd.md` con frecuencia consistente con la cadencia declarada.
- Las specs que superan la ventana de inactividad sin cambio tienen justificacion explícita (proyecto pausado, conocimiento estable confirmado).
- La `Deuda arrastrada` de cada entrega se re-explicita hasta resolverse, no se abandona en silencio entre iteraciones (B-06 verifico esta señal en el testigo: deuda re-declarada en las 4 iteraciones del corte).

## Referencias

- Requisitos como proceso iterativo, no como artefacto estatico: [R03].
- Ciclos de feedback y aprendizaje en entrega de software: [R09].
