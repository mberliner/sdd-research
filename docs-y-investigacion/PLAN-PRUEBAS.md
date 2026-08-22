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

Deslinde con A-04: para A-02 el asistente es el **objeto de estudio** y la
variabilidad entre asistentes es la métrica; para A-04 el asistente es el
**instrumento**, y si cruza más de uno es para caracterizarlo, nunca para
compararlos.

## Experimento A-04
Objetivo: medir si el protocolo del asistente cambia la **conducta** del agente.

Diseño, hipótesis y criterio: `../experimentos/a04-conducta-agente/EXPERIMENTO-A4-protocolo-conducta.md`.
Protocolo de medición: `../experimentos/a04-conducta-agente/PRUEBA-PISO-RUIDO-A4.md`.

Alcance de la pasada 1 (ejecutada 2026-08-15): **sólo el piso de ruido del
instrumento**. El brazo tratamiento no se corre. Es lo que exige el backlog alta
#7 desde B-07: correr el brazo control dos veces antes de reportar ninguna brecha.

Alcance de la pasada 1b (habilitada 2026-08-16, ejecutada y cerrada 2026-08-22):
el **mismo** instrumento en un segundo harness, con el mismo alcance de piso de
ruido. La habilita la enmienda 3 del diseño, que invirtió su condición de disparo
tras el cierre NO APTO por techo de la pasada 1. Tampoco corrió el brazo
tratamiento. Cerró **NO APTO por banda, rota por arriba** (`k1 = 10`, `k2 = 9`
sobre 10): el techo replicó. Las dos compuertas quedan una al lado de la otra —en
ninguno de los dos harnesses hubo un escalón que cayera en banda a resolución de
tanda—, que es la única lectura que la regla sellada admite. `H1` sigue sin
evaluar.

Deslinde con A-02: A-02 mide variabilidad **entre asistentes** del `[SDD-Check]`,
que son su objeto de estudio; en A-04 el asistente es el instrumento y sus tandas
selladas usan un escalón único. La 1b cruza dos harnesses, pero para preguntar si
el instrumento tiene resolución en cada uno —una compuerta categórica por
harness—, no para comparar sus tasas: la regla que lo prohíbe y su única lectura
admisible están selladas en `../experimentos/a04-conducta-agente/PRUEBA-PISO-RUIDO-A4.md`. Sin este
deslinde los dos experimentos se declararían dueños del mismo tema.

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
