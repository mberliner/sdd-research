# Relación FR ↔ SC y naturaleza de la cobertura (no son 1 a 1)

Fecha: 2026-06-16.
Deriva de: `ANALISIS-SPEC-KIT.md` (SSOT del análisis de Spec Kit) y de la anatomía de spec híbrida documentada en el testigo (`SPEC-FORMAT.md`).
Alcance: Línea B (software). El FR/SC y el coverage mapping son nativos de la anatomía de spec de software [R10]; la transferencia a Línea A queda fuera (ver `../06-BACKLOG-INVESTIGACION-FUTURA.md`).

Pregunta que origina el documento: *¿los `FR-xxx` y los `SC-xxx` van 1 a 1? Si necesitan un test para verificarse, ¿hay un test por requisito?*

Respuesta corta: **no, ninguna de las dos cardinalidades es 1 a 1.** FR y SC operan en ejes distintos (contrato construido vs. valor observable), y la cobertura es una relación **muchos-a-muchos** entre requisitos y artefactos de verificación — donde "artefacto" no siempre es un test ejecutable.

---

## FR y SC responden preguntas distintas

| | **FR** (Functional Requirement) | **SC** (Success Criteria) |
|---|---|---|
| Responde a | *qué construye* el sistema (comportamiento / contrato) | *cómo se sabe que el corte vertical entrega valor* (resultado observable) |
| Granularidad | fina, por pieza de comportamiento | gruesa, por objetivo de la User Story |
| Estilo | "el sistema hace X" (presente, `MUST`/`SHOULD`/`MAY`) [R04] | binario, medible, agnóstico de tecnología |
| Cantidad típica en una spec | muchos | pocos |

Por construcción son distintos en número: una User Story suele desplegar varios FR (un comportamiento cada uno) pero pocos SC (uno por objetivo demostrable). Si en una spec aparecen tantos SC como FR, normalmente es señal de que los SC se redactaron como espejo del contrato y no como criterios de aceptación del usuario.

---

## La relación FR ↔ SC es N:M

Un SC se apoya en varios FR, y un FR puede no tener SC propio.

Ejemplo del testigo (`evaluador-flujo-intent`, SPEC-008-suite-metrics: 8 FR, 3 SC):

- **Un SC ⇐ varios FR**: `SC-001` ("la matriz coincide con el cálculo manual") se sostiene en `FR-001` (funciones puras) **y** `FR-002` (ejes de la matriz) a la vez.
- **SC transversal**: `SC-003` ("se computa sobre un run persistido sin invocar al agente") valida una propiedad del conjunto, no un FR individual.
- **FR sin SC**: `FR-009` (resiliencia ante una corrida corrupta) es comportamiento interno; no asciende a criterio de éxito del usuario y no tiene SC asociado.

Regla práctica: el conjunto de SC debe cubrir el *valor* de la User Story; no existe obligación de que cada FR genere un SC ni viceversa.

---

## Cobertura ≠ "un test por requisito"

El malentendido habitual es leer el *coverage mapping* como una tabla 1 FR → 1 test. No lo es. La regla real (anatomía híbrida) es: **cada FR y cada SC MUST tener al menos una entrada en el coverage mapping** — pero la entrada puede agrupar requisitos, y el verificador no siempre es un test ejecutable.

Tres patrones que rompen el 1 a 1, observados en el coverage mapping real de SPEC-008:

1. **Un verificador cubre varios FR** (N FR → 1 entrada).
   `FR-001, FR-002, FR-005 → domain/metrics.py + tests con runs de fixture`. Tres requisitos los cierra el mismo conjunto de tests.
2. **Un FR se verifica sin test ejecutable** (1 FR → revisión humana o visual).
   `FR-003 → revisión cruzada contra PRODUCT.md §Métricas`; `FR-004 → verificación funcional visual confirmada por el usuario`. Consistencia documental y UI no siempre se atrapan con `pytest`.
3. **Un FR exige varios artefactos** (1 FR → N piezas).
   `FR-008 → función pura + flag de CLI + repositorio en adapters + cuatro tests + verificación funcional CLI`.

---

## Cuándo un requisito sí obliga a un test

La distinción operativa es por la naturaleza del requisito, no por su etiqueta FR/SC:

| Tipo de requisito | Verificación esperada |
|---|---|
| Comportamiento ejecutable (cómputo, contrato de función, branch de error) | MUST — test unitario o de integración (puede compartirse entre FR) |
| Consistencia con un SSOT documental | revisión cruzada (no test) |
| Comportamiento de UI | verificación funcional en la app real; es el último SC en marcarse y requisito de cierre |
| Propiedad transversal (p. ej. "sin volver a invocar al agente") | un test que ejercite el conjunto, no un FR puntual |

Esto se alinea con el protocolo SDD del testigo ("todo cambio que toque comportamiento requiere test correspondiente") y con el gate determinista `check_traceability.py`, cuya función es exigir **fila en el coverage mapping** para cada `FR`/`SC`, no un test 1:1 — de hecho atrapó `FR-012` de SPEC-007 implementado pero sin fila en su tabla (ver `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md`, evidencia del gate).

---

## Relación con los otros artefactos

Este documento aclara la cardinalidad **dentro** de una spec (FR/SC/cobertura). La cardinalidad **entre** artefactos de alcance (spec / épica / historia) vive en `RELACION-SPEC-VS-EPICA.md`. Conexión: lo que allí se mapea como "historia de usuario ≈ FR-xxx" no implica simetría con los SC — un FR es una pieza del contrato, un SC es el criterio de aceptación de la historia completa.

---

## Fuentes

- [R04] RFC 2119 — palabras clave normativas `MUST`/`SHOULD`/`MAY` en requisitos.
- [R10] GitHub Spec Kit — anatomía de spec (User Story + FR/SC + Given/When/Then + coverage mapping) y `/speckit.analyze` (gaps de cobertura).

---

[SDD-Check]
- Spec leida: SI (spec propuesta y registrada en `../SPECS_REGISTRY.md` para este doc, derivada de `ANALISIS-SPEC-KIT.md`)
- Incluye/Excluye verificado: SI (foco en cardinalidad FR↔SC y naturaleza de la cobertura; no re-analiza el flujo de Spec Kit ni duplica el mapeo spec/épica de `RELACION-SPEC-VS-EPICA.md`; Línea A diferida)
- Validaciones aplicadas: afirmaciones externas ancladas en [R04][R10]; refs internas verificadas (ANALISIS-SPEC-KIT, RELACION-SPEC-VS-EPICA, DECISION-ADOPTAR-VS-PORTAR-SPECKIT); ejemplos tomados del testigo (SPEC-008/SPEC-007) sin copiar su contenido; sin emoticones; fechas YYYY-MM-DD; ortografía del español con tildes
- SSOT afectado: ninguno (derivado de `software/ANALISIS-SPEC-KIT.md`)
- Derivados a revisar: ninguno
- Cobertura: completa — cada afirmación mapea a una fuente [Rxx] o a un ejemplo verificable del testigo
- Deuda arrastrada: ninguna
- Riesgos/reservas: ejemplos basados en el estado del testigo a 2026-06-16; la anatomía híbrida puede evolucionar
