# Marco Comparativo SDD: Dos Lineas de Investigacion

## Tesis
SDD es un enfoque, no un unico estandar. Su aplicacion cambia segun el tipo de proyecto.

Para el catálogo de problemas y escenarios que justifican adoptar SDD (común a ambas líneas), ver `ESCENARIOS-QUE-JUSTIFICAN-SDD.md`.

## Linea A: Docs e investigacion
Objetivo principal: calidad de decision basada en evidencia.

Necesidades tipicas:
- Delimitacion explicita de alcance (incluye/excluye).
- Trazabilidad fuente -> afirmacion -> conclusion.
- Consistencia terminologica (SSOT).
- Control de contradicciones entre documentos.
- Cadencia de actualizacion y vigencia de evidencia.

Riesgos tipicos:
- Alucinacion o extrapolacion no sustentada.
- Deriva de narrativa (documentos se contradicen).
- Sobrecarga documental sin criterio de decision.

Metricas sugeridas:
- Tasa de hallazgos sin fuente primaria.
- Tasa de contradicciones detectadas por revision.
- Tiempo de localizacion de evidencia para auditoria.
- Cobertura de documentos con spec activa.

Artefactos SDD mas utiles:
- Spec por documento.
- Registro de decisiones.
- Matriz de fuentes.
- Checklist de validacion semantica.

## Linea B: Software
Objetivo principal: comportamiento correcto y evolucion segura del sistema.

Necesidades tipicas:
- Requisitos verificables y testeables.
- Contratos de integracion estables (API/eventos).
- Trazabilidad requisito -> test -> cambio de codigo.
- Manejo explicito de breaking changes.
- Seguridad y confiabilidad desde diseño.

Riesgos tipicos:
- Specs ambiguas que no se traducen en tests.
- Desalineacion entre contrato y implementacion.
- Aceleracion IA sin validacion de calidad.

Metricas sugeridas:
- Defectos en produccion por requisito ambiguo.
- Porcentaje de cambios con prueba ligada a spec.
- Change failure rate y MTTR (DORA).
- Tiempo de ciclo desde spec aceptada a deploy.

Artefactos SDD mas utiles:
- Especificaciones de API/contratos.
- Criterios de aceptacion ejecutables (BDD/ATDD).
- ADR para decisiones tecnicas.
- Paquetes de tests por requisito.

## Implicacion para este proyecto
Se investigan ambas lineas en paralelo, pero con backlog y metrica separada.

No se fuerza un solo stack de herramientas para las dos lineas.

## Referencias base
- [R01], [R02], [R03], [R04], [R06], [R07], [R08], [R09], [R10], [R11], [R12]
