# Relación entre "spec" y los artefactos ágiles (épica / historia de usuario)

Fecha: 2026-06-03.
Deriva de: `ANALISIS-SPEC-KIT.md` (SSOT del análisis de Spec Kit).
Alcance: Línea B (software). El vocabulario ágil (épicas, historias) y Spec Kit son nativos de software; la transferencia del razonamiento a Línea A queda fuera (ver `../agenda/BACKLOG-INVESTIGACION.md`).

Pregunta que origina el documento: *¿una "spec" es análoga a una "épica"?*

Respuesta corta: **no son análogas; operan en ejes distintos.** Y el término "spec" tiene **dos sentidos** en este proyecto que responden la pregunta de forma diferente. Confundirlos es la causa habitual del malentendido.

---

## Los dos sentidos de "spec" en este proyecto

| Sentido | Qué es | Eje | Relación con la épica |
|---------|--------|-----|-----------------------|
| **Spec-Kit** [R10] | Artefacto de *alcance funcional* que agrupa varias historias de usuario, criterios de aceptación y restricciones | "qué construir" | **Supra-épica**: la contiene, no la equivale |
| **Spec de este repo** (`../SPECS_REGISTRY.md`) | *Contrato de gobernanza* de un documento concreto: `incluye`/`excluye`/`validacion`/`ssot_level` | "qué es correcto y consistente" | **Ortogonal**: no es una unidad de alcance de trabajo |

La pregunta "spec ≈ épica" solo tiene sentido para el primer significado. Para el segundo, la spec no compite con la épica en absoluto: gobierna la calidad de un artefacto, no organiza el trabajo a hacer.

---

## Jerarquía de artefactos: Spec Kit vs. ágil

En ágil, la unidad mínima es la historia de usuario y la épica es "una historia grande" que se descompone [R21]. En Spec Kit la jerarquía se invierte en granularidad: la spec está *por encima* y **contiene** las historias [R10].

```text
Ágil:       Épica  ─────────►  Historia de usuario  ─────────►  Tarea
                               (criterios de aceptación)

Spec Kit:   Spec  ──/plan──►  Plan  ──/tasks──►  Tasks  ──/implement──►  Código
            (contiene varias historias P1/P2/P3 + criterios Given/When/Then)
```

Evidencia [R10]: en Spec Kit "las historias de usuario se vuelven endpoints de API, los conceptos de dominio se vuelven modelos de datos, los escenarios de aceptación se vuelven tests". Las historias **viven dentro** de la spec y generan los artefactos aguas abajo; no son artefactos hermanos. Ver el flujo completo en `ANALISIS-SPEC-KIT.md` (tabla de comandos), no se reproduce aquí.

Por tanto, en el plano de *alcance*, el mapeo más fiel es:

```text
Épica (ágil)              ≈   parte del cuerpo de una Spec (Spec Kit), o un SSOT (este repo)
Historia de usuario       ≈   requisito FR-xxx dentro de la spec / documento derivado
Criterios de aceptación   ≈   bloque `validacion` con `[ ]` (este repo)
```

La "épica" se acerca más a un **SSOT** (fuente grande y autoritativa de la que cuelgan derivados, igual que una épica cuelga historias) que a una *spec* de este repo. La spec de este repo es más bien el *Definition of Ready/Done* de cada documento.

---

## Dónde sí se parecen (spec-Kit y épica)

Ambas son **contenedores con criterio de aceptación** que se descomponen y trazan:

| Dimensión | Épica (ágil) | Spec (Spec Kit) [R10] |
|-----------|--------------|------------------------|
| Agrupa alcance | sí (funcionalidad) | sí (historias + restricciones) |
| Criterio de "hecho" | Definition of Done | criterios de éxito SC-xxx medibles |
| Se descompone | en historias -> tareas | en plan -> tasks |
| Trazabilidad | épica -> historia -> commit | spec -> plan -> task (coverage mapping) |

---

## La diferencia de fondo que conviene no perder

SDD nace en parte como **reacción** al modo en que ágil trató a las especificaciones: las relegó a historias ligeras y backlogs, dejando la "verdad" en el código y la documentación como rastro posterior [R20][R21]. SDD invierte esa jerarquía (la "Power Inversion", ver `ANALISIS-SPEC-KIT.md`): la spec pasa a ser el artefacto durable y el entregable su derivado verificable.

Consecuencia para la analogía:

- En **ágil**, la spec/historia es *efímera* — se descarta tras el sprint.
- En **SDD**, la spec es el *activo durable* — mantener el software es evolucionar la spec [R10].

Por eso forzar "spec ≈ épica" induce a error: en SDD la spec no es el *trabajo a hacer* (rol de la épica), sino el *contrato que sobrevive al trabajo*.

---

## Estado de la discusión externa

Existe discusión autoritativa y reciente (2025-2026), con consenso en lo esencial y tensión en la interpretación:

- **Convergencia**: una spec de Spec Kit comprende múltiples historias de usuario junto a specs funcionales, supuestos y resultados; trata las historias como componentes de un marco mayor, no como su equivalente [R10][R21].
- **SDD como síntesis waterfall/ágil**: enfatiza especificación detallada (como waterfall) pero iterativa y viva (como ágil), con la spec en el centro [R20][R21].
- **Tensión crítica**: parte de la comunidad lee Spec Kit como un retorno encubierto a cascada ("documentary bureaucracy") [R22]. Esta crítica conecta con nuestro propio anti-patrón "cascada encubierta" (ver `../comun/SDD-ADAPTATIVO-VS-CASCADA.md`): la diferencia no está en cuánta spec se escribe, sino en si la spec permanece viva o se congela.

No se ha hallado una fuente que defienda la equivalencia estricta "spec = épica"; la posición dominante es la de **contención/inversión de jerarquía**, coherente con lo documentado arriba.

---

## Fuentes

- [R10] GitHub Spec Kit — jerarquía spec/plan/tasks y "las historias viven dentro de la spec".
- [R20] Martin Fowler — SDD como síntesis y crítica al trato ágil de las specs.
- [R21] Thoughtworks — la spec agrupa múltiples historias; ágil relegó las specs a historias ligeras.
- [R22] Scott Logic — lectura crítica de Spec Kit como posible cascada reinventada.

---

[SDD-Check]
- Spec leida: SI (spec propuesta, aprobada y registrada en `../SPECS_REGISTRY.md` para este doc)
- Incluye/Excluye verificado: SI (foco en la relación spec/épica; no re-analiza el flujo interno de Spec Kit ni duplica el mapeo del SSOT; Línea A diferida)
- Validaciones aplicadas: afirmaciones externas ancladas en [R10][R20][R21][R22]; refs internas verificadas (ANALISIS-SPEC-KIT, SDD-ADAPTATIVO-VS-CASCADA, SPECS_REGISTRY, BACKLOG-INVESTIGACION); sin emoticones; fechas YYYY-MM-DD; ortografía del español con tildes (convención fijada en SPECS_REGISTRY.md); no duplica SSOT (referencia, no copia)
- SSOT afectado: ninguno (derivado de `software/ANALISIS-SPEC-KIT.md`)
- Derivados a revisar: ninguno
- Cobertura: completa — cada afirmación de la comparación mapea a una fuente [Rxx] o a un SSOT interno referenciado
- Deuda arrastrada: ninguna; la transferencia del razonamiento a Línea A queda como item de backlog preexistente, no abierto por esta entrega
- Riesgos/reservas: análisis basado en snapshot Spec Kit v0.8.13 [R10] y en discusión externa de 2025-2026 que aún evoluciona
