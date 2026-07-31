# Necesidades y Metricas (Docs e Investigacion)

## Necesidades operativas
- Reglas claras de alcance por documento.
- Citas verificables en afirmaciones criticas.
- Control de vigencia de fuentes (fecha de consulta/publicacion).
- Protocolo de salida estandar para asistentes IA.

## Metricas nucleo
1. Cobertura de specs
Definicion: `% de documentos activos con spec definida`.

2. Adherencia a spec
Definicion: `% de entregas que cumplen incluye/excluye y validaciones`.

3. Trazabilidad
Definicion: `% de afirmaciones criticas con fuente primaria`.

4. Consistencia interdocumental
Definicion: `cantidad de contradicciones detectadas por ciclo de revision`.

5. Costo de mantenimiento
Definicion: `horas por mes dedicadas a mantener sistema SDD`.

## Umbrales iniciales sugeridos
- Cobertura specs: >= 80% docs criticos.
- Afirmaciones criticas con fuente: >= 95%.
- Contradicciones criticas: 0 por release documental.

## Riesgos y mitigacion
- Riesgo: burocracia documental.
  Mitigacion: specs minimas por defecto, extendidas solo en docs de alto impacto.

- Riesgo: dependencia de memoria del asistente.
  Mitigacion: bloque obligatorio de salida con checks explicitos.
