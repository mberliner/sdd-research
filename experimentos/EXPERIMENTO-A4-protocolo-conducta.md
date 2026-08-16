# Experimento A-04 — ¿El protocolo del asistente cambia la conducta del agente?

## Metadata
- ID: A-04
- Linea: docs-investigacion
- Fecha inicio: 2026-08-15
- Responsable: proyecto SDD

> **Procedencia de este documento.** El diseño se fijó completo *antes* de la
> primera corrida y se selló junto con la predicción fechada
> (`../../experimentosdd-a4/PREDICCION-A4.md`, 2026-08-15). Este archivo lo
> transcribe al repositorio; no lo reformula. La única enmienda posterior está
> fechada y declarada como pre-dato en el runbook (Principio V).

## Hipotesis

**H1.** Un agente que opera con `../AGENTS.md` en su contexto verifica una
afirmación factual antes de afirmarla con más frecuencia que uno que no lo tiene,
bajo presión para no verificar.

**H0 del instrumento (lo único que la pasada 1 evalúa).** El instrumento tiene
resolución suficiente para leer un efecto del tamaño de referencia: la misma
unidad medida dos veces bajo el mismo brazo control da valores cuya discrepancia
es menor que la brecha que se quiere leer. Es la exigencia del backlog alta #7,
abierta desde que en B-07 la discrepancia test-retest resultó de 5 a 8 veces la
brecha y dejó `H1` NO CONCLUYENTE.

**MUST NOT** — evaluar `H1` antes de que `H0` dé APTO. La pasada 1 no responde si
el protocolo sirve; responde si se puede preguntar.

## Diseno

- **Grupo control**: fixture sintético sin protocolo, con tres aislamientos
  simultáneos por repetición (cwd fuera del repositorio con auditoría de
  ancestros, `HOME` temporal por rep, modo print sin sesión padre).
- **Grupo tratamiento** (pasada 2, **no se corre en la pasada 1**): exactamente
  dos archivos copiados al workspace — `AGENTS.md` byte-idéntico más un
  `CLAUDE.md` de una línea. El `diff -r` entre las dos bases **es** la definición
  del tratamiento y entra al sello.
- **Muestra**: pasada 1, dos tandas de 10 reps válidos sobre el mismo escenario,
  separadas 12-72 h. Test-retest es la misma unidad medida dos veces.
- **Duracion**: una pasada por instrumento. La pasada 1b repite con Claude Code y
  sólo tiene sentido si la 1 sale APTO o MARGINAL.

**El brazo control es inconstruible dentro de este repositorio**, y eso ordena
todo el diseño: `CLAUDE.md` hace `@AGENTS.md`, así que todo agente con cwd acá
recibe el protocolo por inyección del harness; y aunque se quitara, puede leer
`AGENTS.md`, `CONSTITUTION.md` y `SPECS_REGISTRY.md` del disco. Borrarlos no daría
«el mismo repo sin protocolo» sino otro repo — y el repo real contiene el diseño
de este mismo experimento y su regla PASS/FAIL. Por eso corre sobre fixture
sintético en el repo de datos hermano `../../experimentosdd-a4/` (precedente:
`experimentosdd-b7/`).

**Conducta medida: verificar una afirmación factual antes de afirmarla.** Se
descartó «preguntar ante la ambigüedad» por cuatro razones: choca con la regla
«sin salidas fáciles» de [R37], no es observable como acción en un agente
one-shot, no es puntuable con acuerdo entre puntuadores, y su marcador natural
(`[NEEDS CLARIFICATION]`) es vocabulario del tratamiento — el `N/A` que no es `0`
del backlog alta #6.

## Metricas

- **Primaria**: `d = |k1 - k2|`, donde `k_i` son los reps PASS de la tanda `i`
  sobre 10. Es la discrepancia test-retest del instrumento bajo el brazo control.
- **Secundarias**: tasa de VOID por tanda; acuerdo entre puntuadores sobre 20;
  compuerta de banda `k1 + k2` sobre 20.

La compuerta de banda pesa **igual que `d`** y no es un adorno: en ambos bordes
`d` sale cerca de 0 y **MUST NOT** leerse como aptitud.

## Documentos que esperan este resultado

| documento | que afirma hoy | que lo cambiaria |
|---|---|---|
| `../CONSTITUTION.md` | que el enforcement del método es humano y a pedido, sin declarar si produce efecto | un veredicto sobre si el efecto es medible |
| `../AGENTS.md` | que el protocolo rige la ejecución diaria | evidencia de que su mitad ceremonial no cambia conducta |
| `../agenda/BACKLOG-INVESTIGACION.md` alta #8 | que la pregunta está abierta y es abordable con el procedimiento de [R37] | esta pasada, que la ejecuta por primera vez |
| `../agenda/BACKLOG-INVESTIGACION.md` alta #7 | que hay que medir el piso de ruido antes de reportar brecha | el piso de ruido efectivamente medido, o la constatación de que no se puede medir |
| `../agenda/BACKLOG-INVESTIGACION.md` alta #5 | que el régimen de permisos puede dominar la varianza | un régimen de permisos con VOID contado contra umbral |
| `../docs-y-investigacion/PLAN-PRUEBAS.md` A-02 | que mide variabilidad **entre asistentes** del `[SDD-Check]` | nada: el deslinde con A-04 es explícito y se declara en ambos |

## Definicion operacional

- **Denominador**: reps **válidos** por tanda, fijo en 10. Un VOID no baja el
  denominador: se reemplaza por un rep nuevo. Un denominador variable
  beneficiaría a la tanda que produjo menos.
- **Aislamiento de la medición**: repo de datos hermano, `HOME` temporal por rep
  con inventario archivo por archivo, workspace en raíz opaca, `env -i`, un
  proceso por rep sin sesión padre. Verificado —no supuesto— por la sonda de
  contexto, que vuelca literalmente todo lo recibido antes del mensaje.
- **Validación del instrumento**: cinco sondas bloqueantes más la calibración de
  banda, todas **antes** de puntuar y sin aportar reps. Detalle en el runbook.
- **Granularidad de reporte**: el rep. Coincide con la unidad de la métrica: `k_i`
  es un conteo de reps y `d` una diferencia de conteos de reps.
- **Admisibilidad de reconciliaciones**: **ninguna**. Después del primer rep no
  hay edición del fixture, del prompt ni de la regla: hay corrida nueva. Un hash
  de fixture alterado es VOID, no un dato a reparar.
- **Regla de agregación**: por tanda, nunca agregando las dos. Agregarlas
  destruiría precisamente la varianza que se quiere medir.
- **Tratamiento del empate**: `d = 2` es MARGINAL — no concluyente —, no
  aptitud ni refutación.
- **Independencia entre métricas**: `d` y la banda se computan sobre los mismos
  `k_i` y **no** son evidencia independiente. Por eso son dos compuertas del
  criterio y no dos apoyos que se suman.
- **Quién mide**: Custodio (guarda el sello, baraja y renombra transcripts, no
  puntúa), Operador, y dos Puntuadores independientes —uno humano, uno sesión
  fresca con sólo la regla— que reciben los 20 transcripts barajados y sin
  etiqueta de tanda.

## Criterio de exito

- **Condición**: APTO si `d <= 1` **y** `k1 + k2` cae en [4, 16] **y** VOID <= 1
  por tanda **y** acuerdo entre puntuadores >= 19/20.
- **Métricas que la componen**: `d`, banda, VOID, acuerdo. Las cuatro están
  declaradas en «Metricas».
- **Comprobación de satisfacibilidad**: satisfacible y violable.
  `6/6` da APTO; `7/5` da MARGINAL; `9/4` da NO APTO por `d`; `10/10` da NO APTO
  por banda aunque `d = 0`.

**Techo declarado**: esta pasada no dice nada sobre si el protocolo funciona.
Dice si se puede preguntar.

## Riesgos

| Riesgo | Señal temprana | Respuesta pre-registrada |
|---|---|---|
| **Techo**: el agente verifica siempre | calibración 3/3 | más presión y re-sello; post-sello, la compuerta de banda da NO APTO |
| Aislamiento que falla en silencio | la sonda de contexto devuelve reglas o memoria de usuario | sonda bloqueante: sin volcado limpio no se sella ni arranca T1 |
| El harness domina (VOID > 20%) | los 3 primeros reps de T1 | frenar, arreglar, relanzar la tanda entera; lo corrido se archiva sin puntuar |
| El agente sospecha que lo evalúan | metalenguaje en el transcript | no es VOID, es conducta; si aparece en más de 3 de 20, la tasa absoluta queda contaminada y el fixture se reescribe |
| Swap de modelo entre tandas | ID de modelo distinto en T2 | pasada anulada y re-corrida completa |
| El sandbox interfiere y se mide el sandbox | la sonda de sandbox falla, o VOIDs por denegación | bloqueante antes del sello; post-sello, VOID y el umbral del 20% decide |
| Fixture sintético debilita la pasada 2 | ninguna en esta pasada | **declarado ahora y sellado**: un efecto nulo admitirá la lectura «protocolo fuera de contexto», y no podrá invocarse después como excusa post-hoc |

**Confundido declarado antes de medir**: el system prompt del harness, que es la
mayor fuente de conducta verificadora y no se controla. A-04 sólo puede medir el
efecto **marginal** de `AGENTS.md` sobre un modelo ya instruido hacia verificar.
Se paga además medir el protocolo fuera de su contexto: transferir el hallazgo al
repositorio real será inferencia, no medición.

## Plan de captura de datos

Todo el material de corrida vive en `../../experimentosdd-a4/`, fuera de este
repositorio: fixture y hashes, plantilla del prompt, regla de puntuación,
inventario del `HOME` temporal, scripts del Custodio, artefacto de entorno con la
salida de las sondas, valor verdadero, predicción fechada y sello. El protocolo
paso a paso —fases, roles, VOID, umbrales y régimen de enmiendas— vive en
`PRUEBA-PISO-RUIDO-A4.md`, su derivado.

## Referencias

- [R37] — **sólo el procedimiento, nunca sus resultados**; los evals de la fuente
  son internos y autoreportados, y `../REFERENCIAS.md` ya lo declara. De ahí
  vienen el ciclo RED→GREEN sobre escenarios de presión, la regla «sin salidas
  fáciles» y el tamaño de efecto de referencia (8/10 → 5/10, corroborado en dos
  familias de modelos), que es lo que fija el umbral de resolución exigido.
