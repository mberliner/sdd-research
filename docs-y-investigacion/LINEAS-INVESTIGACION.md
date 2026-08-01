# Lineas de Investigacion (Docs e Investigacion)

## A1. Calidad de specs documentales
Hipotesis: specs breves y explicitas (proposito, alcance, validacion) reducen ambiguedad en salidas de asistentes IA.

Preguntas:
- Que campos minimos generan mayor adherencia?
- Que nivel de detalle empeora velocidad sin mejorar calidad?

## A2. Trazabilidad de evidencia
Hipotesis: obligar mapeo "afirmacion -> fuente" reduce errores factuales en analisis.

Preguntas:
- Cuanto baja la tasa de afirmaciones sin fuente primaria?
- Que formato de cita es mas mantenible en Markdown?

## A3. Gobernanza de SSOT
Hipotesis: separar SSOT/derivado/operativo reduce contradicciones entre documentos vivos.

Preguntas:
- Que reglas de propagacion son suficientes sin automatizacion pesada?
- Cada cuanto conviene revisar derivados?

## A4. Coordinacion multi-asistente
Hipotesis: protocolo comun de salida minimiza variabilidad entre distintos asistentes IA.

Preguntas:
- Que campos de salida son obligatorios?
- Que errores son mas frecuentes por asistente?

## A5. Economia de mantenimiento documental
Hipotesis: un modelo SDD liviano baja el costo de actualizacion periodica.

Preguntas:
- Cuanto tiempo consume mantener specs + historial?
- Que parte agrega valor y que parte es burocracia?

## A6. Circuitos de aprendizaje y specs adaptativas

Hipotesis: incorporar cadencias de revision de specs reduce la tasa de divergencia entre documentos activos y el conocimiento real del proyecto, evitando la cascada encubierta.

Preguntas:
- Que cadencia minima es suficiente para detectar divergencia antes de que sea costosa de corregir?
- Cuales son las señales observables de que una spec se ha congelado sin justificacion?
- Que porcentaje de actualizaciones de spec provienen de experimentos vs de cambio de contexto externo?

Base: circuitos de aprendizaje SDD y anti-patron cascada encubierta — ver `../comun/SDD-ADAPTATIVO-VS-CASCADA.md`.

## Evidencia externa relevante
- Modelos de riesgo y gobernanza IA para documentacion responsable [R01], [R02], [R05].
- Estandares de calidad de requisitos y lenguaje normativo [R03], [R04].
