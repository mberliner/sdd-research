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

Deslinde con A-04: A-02 mide variabilidad **entre asistentes**; A-04 mide **efecto
sobre conducta** con un solo modelo.

## Experimento A-04
Objetivo: medir si el protocolo del asistente cambia la **conducta** del agente.

Diseño, hipótesis y criterio: `../experimentos/EXPERIMENTO-A4-protocolo-conducta.md`.
Protocolo de medición: `../experimentos/PRUEBA-PISO-RUIDO-A4.md`.

Alcance de la pasada 1 (ejecutada 2026-08-15): **sólo el piso de ruido del
instrumento**. El brazo tratamiento no se corre. Es lo que exige el backlog alta
#7 desde B-07: correr el brazo control dos veces antes de reportar ninguna brecha.

Deslinde con A-02: A-02 mide variabilidad **entre asistentes** del `[SDD-Check]`;
A-04 mide **efecto sobre conducta** con un solo modelo. Sin este deslinde los dos
experimentos se declararían dueños del mismo tema.

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
