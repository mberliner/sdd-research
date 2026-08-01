# Plan de Pruebas Reales (Docs e Investigacion)

## Diseno general
Metodo: experimentos cortos A/B sobre tareas reales de analisis documental.

Unidad de analisis: entrega de documento o seccion.

## Experimento A-01
Objetivo: medir impacto de spec minima.

- Grupo A: trabajo sin spec explicita.
- Grupo B: trabajo con spec explicita (proposito, incluye/excluye, validacion).
- Metrica primaria: defectos de alcance por entrega.
- Metrica secundaria: tiempo total por entrega.

Criterio de exito:
- Reducir >= 30% defectos de alcance sin subir > 15% el tiempo.

## Experimento A-02
Objetivo: medir impacto de protocolo de salida estandar del asistente.

Bloque obligatorio: el `[SDD-Check]` definido en `../AGENTS.md`, que es su SSOT. El experimento mide su efecto; no redefine sus campos.

Metrica primaria:
- Variabilidad entre asistentes en la misma tarea.

## Experimento A-03
Objetivo: medir trazabilidad de evidencia.

- Tarea: analisis comparativo con afirmaciones criticas.
- Metrica: % afirmaciones criticas con fuente primaria.

## Cadencia
- Sprint de prueba: 2 semanas.
- Revision de resultados: semanal.
- Decision de adopcion: al completar 3 experimentos.

## Plantillas
- [template de experimento](../templates/EXPERIMENTO.md)
- [template de resultado](../templates/RESULTADO-EXPERIMENTO.md)
