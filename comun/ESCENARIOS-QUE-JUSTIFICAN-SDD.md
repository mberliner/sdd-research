# Escenarios que Justifican SDD

SSOT del catálogo de problemas y escenarios que hacen necesario Spec-Driven Development hoy. Cataloga los *modos de fallo* (cualitativo); las cifras de respaldo viven en `ESTADISTICAS-TENDENCIAS-EVOLUCION.md` y la dinámica de deriva en `SDD-ADAPTATIVO-VS-CASCADA.md` (se referencian, no se duplican).

## Tesis

La IA hizo barata la *generación* y cara la *verificación, la coherencia y la trazabilidad*. SDD es necesario porque la spec gobierna exactamente esos tres ejes que la generación masiva por IA dejó al descubierto. La brecha principal hoy está en gobernanza y validación, no en acceso a herramientas (ver `ESTADISTICAS-TENDENCIAS-EVOLUCION.md`).

## Causas raíz (transversales a línea A y B)

1. **Adopción masiva de IA sin gobernanza.** El uso de IA en desarrollo y trabajo de conocimiento ya es masivo, pero la capacidad de control no creció al mismo ritmo. El cuello de botella dejó de ser generar; pasó a ser validar y mantener coherencia (cifras de adopción: `ESTADISTICAS-TENDENCIAS-EVOLUCION.md` [R11][R15]).

2. **Velocidad sin guardrails degrada estabilidad.** Acelerar la generación sin contratos ni pruebas puede reducir la estabilidad de entrega; la spec actúa como guardrail aguas arriba [R09].

3. **Alucinación y deriva de intención.** Los LLMs son excelentes completando patrones pero pésimos leyendo la mente: producen código o texto plausible con decenas de supuestos no declarados, muchos erróneos. Un pedido como "agregar login" está subespecificado y el modelo elige defaults que rara vez coinciden con lo que el equipo quería (*intent drift*) [R21][R30]. La spec hace explícito el problema, el criterio de éxito y las restricciones antes de generar.

4. **Incidentes IA en aumento.** El crecimiento de incidentes reportados refuerza la necesidad de trazabilidad y control [R16].

## Escenarios — Línea B (software)

- **Vibe coding como antipatrón.** Acelera el prototipado pero, al escalar a producción, deja código one-off, inmantenible y defectuoso ("development hell"). Es el dolor que originó SDD en 2025 [R21][R28].
- **Código vulnerable por defecto.** Las tasas de vulnerabilidad del código generado por LLMs son materialmente altas (ver cifras en `ESTADISTICAS-TENDENCIAS-EVOLUCION.md` [R28][R29]); la spec con criterios de seguridad y los contratos/pruebas deterministas son el contrapeso.
- **Límite de la ventana de contexto.** Cargar el codebase entero satura el contexto del LLM. La organización jerárquica de specs selecciona solo lo relevante por tarea y previene *specification drift* por sincronización [R28].
- **Coordinación multi-agente.** Varios agentes especializados (requisitos, arquitectura, desarrollo, QA) necesitan una fuente de verdad compartida para no pisarse. La spec es ese contrato común que permite tratarlos como pair-programmers literales, no como buscadores [R28][R30].
- **Brecha spec↔implementación y costo de rework.** Cuando la spec genera (o regenera) el código, la divergencia entre intención e implementación se reduce a transformación, no a reescritura desde cero [R30].
- **Regresiones introducidas por IA.** Exigen specs + pruebas + contratos, "no solo prompts" (ver `ESTADISTICAS-TENDENCIAS-EVOLUCION.md`, implicaciones para software).

## Escenarios — Línea A (docs e investigación)

- **Afirmaciones sin fuente verificable.** SDD obliga a citar `[Rxx]` en afirmaciones críticas (umbral en `../docs-y-investigacion/NECESIDADES-Y-METRICAS.md`).
- **Contradicciones entre documentos.** La separación SSOT/derivados evita duplicar y contradecir; meta de 0 contradicciones por release documental (`../docs-y-investigacion/NECESIDADES-Y-METRICAS.md`).
- **Deriva narrativa al crecer el uso de IA.** Sube el riesgo de error factual; la prioridad pasa de producir más texto a mejorar verificabilidad y coherencia (`ESTADISTICAS-TENDENCIAS-EVOLUCION.md`).
- **Alcance difuso por documento.** La spec con `Incluye/Excluye` delimita qué entra y qué no antes de escribir.

## Escenarios — Transversales (A y B)

- **Pérdida de conocimiento institucional / onboarding.** Cuando un autor o ingeniero senior se va, las decisiones de diseño desaparecen si no están en la spec. La spec preserva el *rationale* y acelera la incorporación de nuevos integrantes (humanos o agentes) [R28].
- **Interpretation drift entre personas y sesiones IA.** Distintos integrantes con distintas herramientas IA divergen sin una spec común que los ancle [R28].
- **Auditoría, compliance y trazabilidad.** Cada cambio trazable a un requisito; reglas capturadas como restricciones con enforcement; audit trail para seguridad y regulación [R28].
- **Portabilidad entre herramientas.** La spec es el activo portable entre asistentes (Copilot, Claude Code, Gemini, Cursor); reduce el lock-in de herramienta [R10].

## Cascada encubierta (modo de fallo propio del proyecto)

El riesgo no es solo no tener spec, sino tener una spec que no se actualiza con los resultados. Los derivados divergen del SSOT y la deuda se abandona en silencio. El tratamiento (señales de alarma, feedback loops, mecanismo `Deuda arrastrada`) es SSOT de `SDD-ADAPTATIVO-VS-CASCADA.md` — aquí solo se nombra como escenario que justifica el ciclo de revisión de SDD.

## Señal de mercado (por qué *ahora*)

Las cifras concretas (concentración de código IA en startups, potencial de automatización guiada por specs, first-pass success de adopters tempranos) viven en `ESTADISTICAS-TENDENCIAS-EVOLUCION.md`, sección "Calidad del código generado por IA y señal de adopción SDD" [R28]. Síntesis: sin método, la generación masiva por IA no escala a producción mantenible.

## Mapa escenario → eje que gobierna la spec

| Escenario | Eje SDD que lo mitiga |
|---|---|
| Alucinación / intent drift | Intención y criterio de éxito explícitos |
| Código vulnerable | Restricciones de seguridad en la spec + contratos/pruebas |
| Límite de contexto | Specs jerárquicas, selección por tarea |
| Multi-agente | Fuente de verdad compartida |
| Pérdida de conocimiento | Rationale persistido y versionado |
| Auditoría/compliance | Trazabilidad requisito→entregable |
| Afirmaciones sin fuente | Citas `[Rxx]` obligatorias |
| Contradicciones interdoc | SSOT/derivados, no duplicación |
| Cascada encubierta | Ciclo de revisión y `Deuda arrastrada` |
