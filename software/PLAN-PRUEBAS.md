# Plan de Pruebas Reales (Software)

## Diseno general
Metodo: pilotos por servicio/modulo con baseline previo y posterior.

## Proyecto testigo
Sujeto experimental oficial de Linea B: `evaluador-flujo-intent` (ex `agent-test-suite`, renombrado 2026-06-21; `../../../test_circuito_intents/evaluador-flujo-intent/`). Es un proyecto Python real (src/tests/pytest/ruff + **git/CI/pre-commit**) que adopto nuestra misma variante SDD (SPECS_REGISTRY, specs `SPEC-NNN-slug`, bloque `[SDD-Check]`, specs vivas, `historial/sdd.md`). Su registry declara explicitamente derivar el patron de este proyecto. Funciona como linea base de "nuestra SDD sobre software"; los experimentos definidos aqui se ejecutan sobre el y sus resultados se guardan en `../experimentos/`.

**Premisa del testigo (2026-06-21): SDD universal primero, adaptadores por ambiente despues.** El protocolo es SSOT unico en `AGENTS.md` (lo leen opencode/Cursor/Codex/Aider/Gemini por convencion; Claude via `@AGENTS.md`); el cuerpo de `/analyze` y `/clarify` vive neutro en `docs/playbooks/` con wrappers finos por asistente (`.claude/skills/`, `.opencode/command/`); el gate `tools/sdd_gate.py` es multi-transporte (argv/env/stdin). El detalle del enforcement y su lectura sobre la decision A/B esta en `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` §9.1, no se duplica aqui.

## Experimento B-01: Contract-first vs code-first
- Hipotesis cubierta: B2 (contract-first), ver `LINEAS-INVESTIGACION.md`.
- Grupo A: implementar endpoint sin contrato previo.
- Grupo B: implementar con contrato OpenAPI previo.
- Metrica primaria: incidencias de integracion en QA/produccion.

## Experimento B-02: BDD en historias criticas
- Hipotesis cubierta: B3 (behavior-first / BDD), ver `LINEAS-INVESTIGACION.md`.
- Alcance: flujo de negocio sensible.
- Metrica primaria: defectos de aceptacion.
- Metrica secundaria: tiempo de clarificacion con negocio.

## Experimento B-03: IA con y sin guardrails
- Hipotesis cubierta: B4 (IA en ciclo de desarrollo), ver `LINEAS-INVESTIGACION.md`.
- Grupo A: asistencia IA sin checklist de validacion.
- Grupo B: asistencia IA con checklist (seguridad, tests, compatibilidad).
- Metrica primaria: change failure rate.

## Experimento B-06: Circuito de aprendizaje en el testigo (observacional)
- Tipo: retrospectivo sobre el proyecto testigo; no interviene el codigo.
- Hipotesis: ver B6 en `LINEAS-INVESTIGACION.md` (specs vivas como circuito de aprendizaje vs. cascada encubierta, `../comun/SDD-ADAPTATIVO-VS-CASCADA.md`).
- Fuente de datos: `specs/`, `specs/SPECS_REGISTRY.md` e `historial/sdd.md` del testigo.
- Metrica primaria: proporcion de specs revisadas tras ejecucion/verificacion vs. specs creadas y congeladas.
- Diseno completo: `../experimentos/EXPERIMENTO-B6-circuito-testigo.md`.

## Experimento B-07: Formato de spec híbrido (Spec Kit) vs. baseline casera
- Tipo: estudio de caso comparativo intervencional sobre el proyecto testigo.
- Hipótesis: ver B7 en `LINEAS-INVESTIGACION.md` (anatomía Spec Kit mejora cobertura, ambigüedad temprana y regenerabilidad vs. formato casero).
- Corpus observacional (métricas secundarias): control casero SPEC-001/002/003 vs tratamiento híbrido SPEC-004/005/006/008. **Corrección 2026-07-29:** el control **no está congelado** al corte B-06 — las tres specs se editaron después (`SPEC-002` y `SPEC-003` hasta el 2026-06-08) y referencian specs posteriores. Se mide el corte tal cual, declarando que la contaminación **favorece al control**. Ver `../experimentos/PRUEBA-OBSERVACIONAL-B7.md` §Reglas criticas 7.
- Métrica primaria: regenerabilidad desde spec (reconstruir el código desde la spec sola con mínimos errores), medida sobre un **diseño 2×2 por traducción** (SPEC-001 casero vs SPEC-013 híbrida + celdas cruzadas) — no sobre el corpus observacional; ver runbook.
- Diseño completo: `../experimentos/EXPERIMENTO-B7-formato-hibrido.md`.
- Protocolo de ejecución de la métrica primaria (runbook 2×2): `../experimentos/PRUEBA-REGENERABILIDAD-B7.md`.
- **Estado: CERRADO (2026-07-28).** Resultado en `../experimentos/RESULTADO-EXPERIMENTO-B7.md`. La **prueba de regenerabilidad** se ejecutó completa (4 celdas, métricas R1–R5); el **corpus observacional** de las métricas secundarias (H1/H2/H3, costo de redacción, specs vivas) **no se midió** y queda pendiente.
- **Resultado en una línea:** en la única feature que discriminó (F013) el formato **casero** superó al híbrido en R1, R2 y R5; F001 empató en las cinco métricas. **H4 (regenerabilidad, componente primaria de B7) no queda sostenida, pero tampoco refutada**: en F013 el eje formato está confundido con el eje spec auténtica/traducida, y una sola ronda de reparación borra la diferencia (las 4 celdas llegan a 100%).
- **Decisión:** Ajustar — no se adopta ni se descarta el formato híbrido; se ajusta el aparato de evaluación.
- **Ajuste del aparato (2026-07-29):** alta de la métrica **`R6` (verificación funcional manual)** en el SSOT del experimento — `R1` se automatizó con `pytest`, luego midió sólo el subconjunto pytest-verificable del espacio de requisitos. `R6` **no se midió en B-07** y aplica desde la próxima corrida. El espacio que cubriría se relevó de forma **exploratoria y no ciega**: de los 13 requisitos de `SPEC-013` fuera del denominador, 9 resultaron mecanizables y están satisfechos en **ambas** celdas de F013 (empate ⇒ no aporta dirección); quedan 4, todos de UI, sin ningún dato. **No altera el veredicto ni la decisión.**
- **CERRADO INTEGRALMENTE (2026-07-31) — corpus observacional medido.** 28 sesiones de extractor, 14 pares, corte `3f1ed33`, 7 enmiendas aditivas post-sello. **(b)**: `H1` **NO CONCLUYENTE** por tres de las cuatro vías pre-registradas (divergencia entre variantes de unidad, inversión bajo *leave-one-out* en la primaria y en los dos extractores, piso de ruido de 5 a 8 veces la brecha); `H3` **no consistente con la hipótesis** en colisión, capas cruzadas y fan-out, robusto al `LOO`, con instrumento sin validación —su compuerta se anuló por HARKing— y modo de fallo común `src/dashboard/app.py` no descartado. Tier B no puntuó. **Decisión: AJUSTAR**, con (a) pesando más que (b) por controlado vs. observacional. Hallazgo transferible: **medir el piso de ruido del instrumento antes de reportar una brecha**.
- **Instrumento verificado bajo una segunda familia de modelos (2026-08-01) — posterior al cierre, no lo modifica.** El acuerdo inter-extractor del corpus se había medido con dos modelos de la misma familia, así que no distinguía claridad de la regla de idiosincrasia compartida. El corpus se replicó bajo otro harness y otra familia, con pre-registro sellado antes de correr y los mismos bytes de entrada: 13 de las 14 celdas. **Bajo la regla que fija la unidad por identificador declarado las dos familias producen inventarios de idéntico tamaño celda por celda; bajo la regla que deja el corte al modelo divergen**, lo que respalda desde otra familia el hallazgo de que la convención de conteo manda. `n`=1 por celda; MUST NOT atribuirse al harness ni al modelo por separado ni compararse celda contra celda entre harness; no sostiene por sí sola la cláusula de reproducibilidad de (b). Detalle: `../experimentos/RESULTADO-EXPERIMENTO-B7.md` §Adenda 2026-08-01.
- **Criterio de éxito REFORMULADO (2026-07-29) — cierra la deuda del cierre de B-07.** En `../experimentos/EXPERIMENTO-B7-formato-hibrido.md` §Criterio de exito, ahora son **dos criterios independientes** más una regla de cierre: **(a)** prueba de regenerabilidad contra `R1`–`R6`, unidad de inferencia **intra-feature**, tres condiciones (`R1` mayor + `R2` menor + **≥1 secundaria independiente** en el mismo sentido y ninguna en contra, admisibles `R4`/`R5`/`R6`), empate ⇒ no concluyente, veredicto global sólo con ≥2 features discriminantes, y **guarda de confusión** con techo *"no atribuible al formato"*; **(b)** corpus observacional contra **`H1`+`H3`** (sólo Tier A), comparación de **medianas con solapamiento declarado** más sensibilidad *leave-one-out* —relajada el 2026-07-29 desde el no-solapamiento original, que con `n`=3 vs 4 daba *no concluyente* por construcción; el costo evidencial se declara—, techo de conclusión **descriptivo**; **regla de cierre**: B-07 cierra con **dos veredictos**, nunca fundidos, y la decisión declara el peso relativo. Ambos pasan la comprobación de satisfacibilidad de `../templates/EXPERIMENTO.md`. Aplicado a lo ya ejecutado **no cambia el veredicto** (H4 no sostenida, F001 no concluyente, techo "no atribuible"): lo que cambia es que el criterio pasa de **no evaluable** a **evaluable**.
- **H2 degradada a descriptiva (2026-07-29):** su ratio upfront/reactivo no es computable (`[NEEDS CLARIFICATION]` no existe en la anatomía casero — `N/A`, no `0`) y su variable de salida está confundida con el tratamiento (una práctica documental altera la visibilidad de su propio resultado). MUST NOT integrar criterio de éxito; se conserva la lectura cualitativa. **Las secundarias del corpus observacional quedan en H1, H3 y costo de redacción**, y siguen sin medirse. **Runbook ejecutable listo (2026-07-29): `../experimentos/PRUEBA-OBSERVACIONAL-B7.md`**, con §Definicion operacional, Fase 0 sellada y corte fijado en `3f1ed33` (el ciclo de vida del corpus es pre-git). Pendiente: ejecutarlo. Anti-patrón generalizado en `../agenda/BACKLOG-INVESTIGACION.md` §Prioridad alta 6.
- **Corpus observacional EN EJECUCIÓN (estado al 2026-07-30).** Fase 0 **sellada** (corte `3f1ed33`, 9 artefactos), Fase 1 **completa**, Fase 2 calibración **pasada** (acuerdo 0.951 casero / 1.000 híbrido, umbral 0.20) e inventario **3 de 7 specs**. Datos y bitácora en el repo externo `experimentosdd-b7/obs/`. **Tres enmiendas** post-sello, aditivas, con el set sellado intacto: (1) disparador de unidad por declaración propia; (2) el brazo control **no** estaba congelado al 2026-05-24 y se mide igual, sin filtrar, porque la contaminación lo favorece; (3) **selector de regla externo**, que hace ejecutable la variante de sensibilidad. Restan **22 sesiones** de extractor (8 primarias + 14 neutrales).
- **Criterio (b) reforzado (2026-07-30): la variante de sensibilidad de `H1` entra al criterio, con regla de decisión.** Estaba obligatoria desde el sello pero sólo en el runbook y **sin veredicto declarado ante divergencia**. Ahora en el SSOT: coincidencia de dirección descarta la preocupación por granularidad **sólo si ambas variantes son estables al *leave-one-out***; **divergencia ⇒ `H1` NO CONCLUYENTE** (si la dirección depende de la unidad elegida es propiedad de la convención, no del corpus); y **piso de ruido del instrumento** — la re-medición del casero con la misma regla cuantifica el ruido de sesión de extractor y, si iguala la brecha entre brazos, `H1` es NO CONCLUYENTE. Decidido **sin ninguna proporción calculada**. Baja la probabilidad de veredicto y ese costo se declara. Detalle normativo en `../experimentos/EXPERIMENTO-B7-formato-hibrido.md` §Criterio de exito (b).

## Experimento B-08: Retro-spec en modulo legacy (esbozo)
- Estado: borrador (no pre-registrado; pendiente de afinar antes de ejecutar).
- Tipo: estudio comparativo intervencional sobre un modulo legacy del proyecto testigo (codigo sin red de pruebas de regresion, sentido Feathers [R23]).
- Hipotesis (candidata): una retro-spec minima + characterization tests reduce el costo/error del proximo cambio en un modulo legacy frente a tocarlo sin spec. No mapea a B1-B7; base conceptual en `SDD-EN-LEGACY-Y-BROWNFIELD.md`.
- Diseno:
  - Control: aplicar un cambio (bug fix o feature pequena) sobre el modulo legacy sin retro-spec previa.
  - Tratamiento: antes del mismo tipo de cambio, escribir retro-spec minima (Incluye/Excluye + comportamiento observado vs. deseado) y characterization tests que anclen el comportamiento actual [R23].
  - Muestra: 2-3 modulos comparables del testigo, o cambios sucesivos sobre el mismo modulo con orden contrabalanceado.
- Metricas:
  - Primaria: defectos introducidos por el cambio (regresiones detectadas post-cambio).
  - Secundarias: tiempo de comprension hasta el primer cambio correcto; cobertura de comportamiento capturada antes de tocar.
- Criterio de exito: el grupo tratamiento reduce defectos introducidos sin aumentar >10% el tiempo total del cambio (alineado con el criterio de adopcion general).
- Riesgo principal: fosilizar bugs si la retro-spec no distingue observado de deseado; mitigacion = marcar cada afirmacion (MUST del doc tematico) y usar `[NEEDS CLARIFICATION]`.
- Diseno completo: pendiente en `../experimentos/` usando `../templates/EXPERIMENTO.md`.
- Base conceptual: `SDD-EN-LEGACY-Y-BROWNFIELD.md`.

## Duracion recomendada
- 6 a 8 semanas por ciclo experimental.

## Criterio de adopcion
Adoptar practica cuando mejora al menos 2 metricas clave sin deteriorar mas de 10% la velocidad de entrega.

## Cobertura de hipotesis (B1-B7)

La numeracion de experimentos (`B-0N`) es independiente de la de hipotesis (`BN` en `LINEAS-INVESTIGACION.md`): salvo B-06/B-07, que coinciden a proposito, el resto no mapea 1:1.

| Hipotesis | Experimento | Estado |
|-----------|-------------|--------|
| B1 (requisitos verificables) | — | sin experimento aun |
| B2 (contract-first) | B-01 | definido |
| B3 (behavior-first) | B-02 | definido |
| B4 (IA en ciclo) | B-03 | definido |
| B5 (gobernanza de cambios) | — | sin experimento aun |
| B6 (specs como circuito de aprendizaje) | B-06 | cerrado (`../experimentos/RESULTADO-EXPERIMENTO-B6.md`) |
| B7 (formato hibrido Spec Kit) | B-07 | **cerrado integralmente 2026-07-31** (`../experimentos/RESULTADO-EXPERIMENTO-B7.md`) — dos veredictos: (a) H4 **no sostenida, sin ser refutada**; (b) `H1` **NO CONCLUYENTE**, `H3` **no consistente** con la hipotesis. Decision: **AJUSTAR** |

B1 y B5 quedan sin experimento por ahora (no es un hueco de numeracion, sino agenda pendiente); priorizarlos es decision de backlog.

B-08 (retro-spec en legacy) es un experimento tematico que no cubre ninguna hipotesis B1-B7; su base es `SDD-EN-LEGACY-Y-BROWNFIELD.md`. Por eso no aparece en la tabla de cobertura.

## Plantillas
- [template de experimento](../templates/EXPERIMENTO.md)
- [template de resultado](../templates/RESULTADO-EXPERIMENTO.md)
