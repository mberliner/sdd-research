# Marco Comparativo SDD: Dos Lineas de Investigacion

## Tesis
SDD es un enfoque, no un unico estandar. Su aplicacion cambia segun el tipo de proyecto.

Este documento aisla **en que se diferencian** la linea A (docs e investigacion) y la linea B (software). Lo que es propio de cada lado vive en el SSOT de esa linea y aca se referencia, no se copia:

- Necesidades operativas, metricas, umbrales y riesgos por linea: `docs-y-investigacion/NECESIDADES-Y-METRICAS.md` (A) y `software/NECESIDADES-Y-METRICAS.md` (B).
- Modos de fallo y escenarios que justifican adoptar SDD, ya separados por linea: `ESCENARIOS-QUE-JUSTIFICAN-SDD.md`.
- Frameworks y herramientas concretas recomendadas por linea: `PROYECTOS-LIDERES-Y-FRAMEWORKS.md`.

## Eje diferencial

| Eje | Linea A — docs e investigacion | Linea B — software |
|---|---|---|
| Objetivo principal | calidad de decision basada en evidencia | comportamiento correcto y evolucion segura del sistema |
| Artefactos SDD mas utiles | spec por documento, registro de decisiones, matriz de fuentes, checklist de validacion semantica | especificaciones de API/contratos, criterios de aceptacion ejecutables (BDD/ATDD), ADR, paquetes de tests por requisito |
| Familia de metricas | verificabilidad y coherencia del cuerpo documental | correccion del comportamiento y estabilidad de la entrega (DORA) |
| SSOT del detalle | `docs-y-investigacion/NECESIDADES-Y-METRICAS.md` | `software/NECESIDADES-Y-METRICAS.md` |

La fila "familia de metricas" nombra el **tipo** de metrica que cada linea necesita, no las metricas: la lista concreta y sus umbrales son SSOT de cada linea.

## Implicacion para este proyecto
Se investigan ambas lineas en paralelo, pero con backlog y metrica separada.

No se fuerza un solo stack de herramientas para las dos lineas.

## Referencias base
- [R01], [R02], [R03], [R04], [R06], [R07], [R08], [R09], [R10], [R11], [R12]
