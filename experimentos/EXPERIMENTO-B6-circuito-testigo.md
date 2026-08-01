# Experimento B-06: Circuito de aprendizaje en el proyecto testigo

## Metadata
- ID: B-06
- Linea: software
- Fecha inicio: 2026-05-24
- Responsable: proyecto SDD (analisis)
- Sujeto: `agent-test-suite` (`../../../test_circuito_intents/agent_test_suite/`) — proyecto testigo oficial (ver `../software/PLAN-PRUEBAS.md`)

> **Nota (2026-06-01):** al corte de este experimento, `../comun/SDD-ADAPTATIVO-VS-CASCADA.md` fijaba la ventana de inactividad en **30 dias absolutos**. Este experimento motivo su reformulacion a un criterio **relativo** (2-3 iteraciones o ciclos de cierre); ver Fase 3 en `../historial/sdd.md`. Las menciones a "30 dias" mas abajo reflejan el umbral vigente en su momento, no el actual.

## Hipotesis

H (B6, ver `../software/LINEAS-INVESTIGACION.md`): en un proyecto que practica specs vivas, las specs se actualizan tras la ejecucion/verificacion (circuito de aprendizaje activo), en lugar de quedar congeladas en su version inicial (cascada encubierta, `../comun/SDD-ADAPTATIVO-VS-CASCADA.md`).

Prediccion: la mayoria de las specs `active` muestran al menos una revision posterior a su creacion disparada por un hallazgo de ejecucion/test, y la "deuda arrastrada" registrada en iteraciones previas se resuelve o se hace explicita en iteraciones siguientes (no se abandona silenciosamente).

## Diseno
- Tipo: observacional / retrospectivo. NO interviene el codigo ni el flujo del testigo.
- Grupo control: no aplica (estudio de caso unico sobre artefactos existentes).
- Grupo tratamiento: no aplica.
- Muestra: el conjunto de specs del testigo a la fecha de corte (`SPEC-000-naming`, `SPEC-000-bootstrap`, `SPEC-001`..`SPEC-003` active; `SPEC-004`..`SPEC-007` draft) y todas las entradas de `historial/sdd.md`.
- Duracion: corte unico 2026-05-24; repetible como serie si el testigo sigue activo.

## Metricas
- Primaria: proporcion de specs `active` con al menos una revision post-creacion atribuible a ejecucion/verificacion (ej. `SPEC-002` "revisada 2026-05-23 tras verificacion e2e").
- Secundarias:
  - Antiguedad de specs `draft` sin movimiento (señal de cascada si supera el umbral de 30 dias de `../comun/SDD-ADAPTATIVO-VS-CASCADA.md`).
  - Tasa de resolucion de "deuda arrastrada": items de deuda de una iteracion que se cierran o se reexplicitan en la siguiente vs. los que desaparecen sin traza.
  - Divergencia spec<->codigo: specs cuyo alcance declarado no coincide con el codigo/tests presentes (muestreo manual).
  - Presencia y completitud del bloque `[SDD-Check]` por iteracion.

## Criterio de exito

El circuito de aprendizaje se considera ACTIVO (hipotesis sostenida) si, al corte:
- Metrica primaria >= 50% de specs `active` con revision post-ejecucion, Y
- Ninguna spec `draft` supera 30 dias sin movimiento sin justificacion registrada, Y
- La deuda arrastrada tiene tasa de resolucion/reexplicitacion observable (no abandono silencioso).

Se considera SEÑAL DE CASCADA ENCUBIERTA si la primaria < 50% o aparecen drafts estancados sin justificacion.

## Riesgos
- Muestra pequena (pocas specs): el resultado es indicativo, no concluyente. Mitigacion: declararlo como estudio de caso, no como evidencia generalizable.
- Sesgo del observador: el testigo derivo su SDD de este proyecto, por lo que confirma parcialmente nuestro propio diseno. Mitigacion: separar hallazgos descriptivos (que paso) de interpretativos (por que).
- Atribucion de causa: "revisada tras verificacion" puede no implicar que el test causo la revision. Mitigacion: citar la entrada de `historial/sdd.md` que documente el disparador.

## Plan de captura de datos
1. Inventariar specs del testigo y su estado/iteracion desde `specs/SPECS_REGISTRY.md`.
2. Por cada spec `active`, registrar si hay marca de revision post-creacion y su disparador (campo `Iter`/`revisada` + entrada de historial).
3. Extraer de `historial/sdd.md` las secciones "Deuda arrastrada" y rastrear su destino en iteraciones posteriores.
4. Datar las specs `draft` (ultima modificacion) y compararlas contra el umbral de 30 dias.
5. Muestreo de divergencia spec<->codigo en 1-2 specs (lectura de alcance vs. `src/`).
6. Consolidar en `RESULTADO-EXPERIMENTO-B6.md` usando `../templates/RESULTADO-EXPERIMENTO.md`.

## Referencias
- Hipotesis B6: `../software/LINEAS-INVESTIGACION.md`
- Anti-patron y umbral 30 dias: `../comun/SDD-ADAPTATIVO-VS-CASCADA.md`
- Plan experimental Linea B: `../software/PLAN-PRUEBAS.md`
- DORA / feedback loops en entrega: [R09] (`../REFERENCIAS.md`)
