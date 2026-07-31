# Necesidades y Metricas (Software)

## Necesidades operativas
- Specs que se puedan verificar con tests.
- Contratos versionados para APIs y eventos.
- Criterios explicitos de breaking change.
- Trazabilidad requisito -> commit -> test -> release.

## Metricas tecnicas
1. Defect escape rate
Definicion: defectos funcionales detectados en produccion / total defectos.

2. Change failure rate
Definicion: porcentaje de cambios que causan incidente o rollback.

3. MTTR
Definicion: tiempo medio de recuperacion.

4. Lead time for changes
Definicion: tiempo desde cambio aprobado hasta produccion.

5. Cobertura de requisitos con tests
Definicion: `% requisitos activos con al menos una prueba asociada`.

## Relacion con DORA
Estas metricas se alinean con indicadores de performance de entrega [R09].

## Riesgos y mitigacion
- Riesgo: specs bonitas pero no ejecutables.
  Mitigacion: exigir criterio de aceptacion verificable por requisito.

- Riesgo: sobredependencia en IA para coding.
  Mitigacion: gates de revision y pruebas basadas en riesgo.
