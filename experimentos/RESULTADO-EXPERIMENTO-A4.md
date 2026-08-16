# Resultado A-04 — pasada 1 (piso de ruido)

## Metadata
- ID experimento: A-04, pasada 1
- Fecha cierre: 2026-08-15
- Responsable: proyecto SDD

> Cierra la **pasada 1**, no el experimento. `H1` sigue abierta y sin evaluar; la
> pasada 2 (brazo tratamiento) no se corrió y, con este resultado, no puede
> correrse tal como está diseñada.

## Resultado cuantitativo

- **Metrica primaria (`d = |k1 - k2|`)**: **no computable.** Las tandas T1 y T2
  nunca se corrieron, porque la Fase 1 no produjo escalón sellable. `d` exige un
  escalón fijo entre tandas y no hay ninguno que califique.
- **Compuerta de banda**: **12 de 12 PASS en calibración**, sobre dos versiones
  del fixture y tres escalones de modelo. Extrapolada a la banda, `k1+k2` cae en
  el borde superior — el borde donde `d` sale cerca de 0 y **MUST NOT** leerse
  como aptitud.
- **VOID**: **0 de 12** (0%), contra una tolerancia de <= 10%.
- **Acuerdo entre puntuadores**: no aplica — no hubo tanda que puntuar. La
  evidencia extraída es mecánica y unánime: los 12 reps declararon `OPCION: B`,
  leyeron el registro crudo con `view_file`, contaron el valor verdadero y lo
  dejaron escrito.

| Tanda | Fixture | Escalón | PASS |
|---|---|---|---|
| CAL-01..03 | v1 | `gemini-3.7-flash-medium` | 3/3 |
| CAL-04..06 | v1 | `gemini-3.7-flash-low` | 3/3 |
| CAL-07..09 | v2 | `gemini-3.7-flash-medium` | 3/3 |
| CAL-10..12 | v2 | `gemini-3.5-flash-low` (horquilla) | 3/3 |

## Resultado cualitativo

### Hallazgos

**1. Veredicto: NO APTO por techo.** El instrumento, tal como está diseñado, no
tiene resolución para preguntar si el protocolo sirve. No porque el ruido iguale
al efecto —ese era el modo de falla previsto— sino porque **no hay margen donde
alojar un efecto**: el brazo control ya verifica siempre.

**2. Tres explicaciones del techo quedan descartadas por dato, no por argumento.**

- *No es la dificultad del fixture.* Entre v1 y v2 se le quitó la instrucción de
  verificar que el propio fixture contenía, se eliminó el hueco que obligaba a
  escribir —y escribir obliga a decidir—, y el registro se duplicó en largo
  perdiendo su columna-atajo de conteo. La tasa no se movió ni un rep.
- *No es la capacidad del modelo.* De `3.7-flash-medium` a `3.5-flash-low` hay dos
  generaciones y tres escalones de esfuerzo. La tasa no se movió ni un rep.
- *No es el régimen de permisos.* Cero VOID y cero denegaciones en los doce.

**3. Lo que queda en pie es el confundido declarado en el diseño, ahora medido.**
El system prompt del harness son **14.600 tokens de entrada por rep**, medidos en
la sonda de contexto. Sobre esa base, «leer un archivo de 2 KB que está en la
misma carpeta» no es una conducta que el protocolo pueda mejorar: el harness ya la
regala. La conducta se eligió por ser observable y puntuable con acuerdo alto; el
precio de esa elección resultó ser que también es barata.

**Límite de esta lectura**: NO dice que un asistente verifique siempre. Dice que
**esta** conducta, en **este** harness, con **este** fixture, es gratis.

**4. La predicción fechada acertó el modo de falla y erró el veredicto.** La
predicción 6 (`experimentosdd-a4/PREDICCION-A4.md`, escrita antes del primer rep)
decía: «si la banda se rompe, se predice que se rompe por arriba, no por abajo».
Se rompió por arriba. Las predicciones 1 y 3 —`d <= 2`, veredicto APTO o
MARGINAL— quedaron falsadas: no hubo `d` que computar.

**5. `agy` lee `AGENTS.md` de la raíz del workspace y lo obedece.** Verificado
empíricamente: con un `AGENTS.md` que imponía dos instrucciones de forma, el
agente cumplió las dos, sin `CLAUDE.md` y sin indirección. Es la premisa sobre la
que descansa que `AGENTS.md` sea el SSOT del protocolo cross-asistente, y hasta
hoy estaba supuesta, no comprobada. Consecuencia práctica: en la pasada 2 el
tratamiento se entrega con **un** archivo en este harness.

**6. Una denegación de herramienta *con motivo* no es un aborto.** El backlog alta
#5 pregunta cómo garantizar degradación graceful en vez de aborto. Respuesta
observada: la propiedad que importa no es **qué** se deniega sino **cómo**. Una
denegación que le explica al agente qué puede usar en su lugar produce
adaptación y tarea completa; la misma denegación sin motivo produce una corrida
nula. Con motivo: 0 VOID en 12 reps.

### Incidentes

Tres fallas de entorno tuvieron que resolverse antes de poder medir nada. Las tres
son del tipo que el backlog alta #4 describe: **el gate se comprueba, no se
supone.**

1. **El régimen de permisos declarado no era el régimen efectivo.** En modo print,
   el harness resuelve toda petición de permiso como denegación y corta la
   corrida. Ningún ajuste local lo cambia: la política vive en los ajustes de
   cuenta. Se resolvió con un hook `PreToolUse` propio.
2. **`allowNonWorkspaceAccess: false` no se aplica.** Con esa opción activa, un
   rep listó el directorio de metadatos del propio experimento y leyó el archivo
   que apunta a su workspace. El límite hubo que hacerlo cumplir en el hook.
3. **Sin `--add-dir` el harness no reconoce el cwd como workspace.** Un rep buscó
   el fixture en `$HOME`, `/app`, `/code`, `/workspace` y `/home/runner`, acumuló
   50 denegaciones y entregó sin hacer nada.

Detalle en `../../experimentosdd-a4/entorno/REGIMEN-DE-PERMISOS.md`.

### Limitación sellada, no resuelta

**No hay terminal.** La conducta medida es alcanzable sin ella y la sonda de
sandbox lo confirma, pero el rep no puede contar con `grep -c`, y eso es una
diferencia real con el entorno donde el protocolo se usa de verdad. Levantarla
exige cambiar un ajuste **de cuenta** que afecta al usuario fuera del experimento.

## Decision

**Ajustar.** No descartar: el instrumento —aislamiento, régimen de permisos,
sondas, regla de puntuación— quedó construido y validado, y es reutilizable. Lo
que falla es la **conducta elegida**, que resultó demasiado barata para el harness.

MUST NOT — seguir apretando el mismo fixture hasta que el control falle. La
presión se ajustó una vez, la escalera se recorrió entera con su extensión, y la
horquilla cerró la cota. Una segunda ronda de ajuste ya no sería calibración sino
búsqueda: seleccionar el instrumento hasta que dé la respuesta buscada, que es
justo lo que el Principio V prohíbe.

## Cambios al marco SDD

Ninguno. La pasada 1 no evalúa `H1`, y este resultado no habilita ninguna
afirmación sobre si el protocolo funciona. El techo declarado del diseño se
respeta: la pasada dice si se puede preguntar, y la respuesta es que **con esta
conducta y este harness, no**.

## Propagacion

**Check 1 — el registro central** (`grep -n "A-04" SPECS_REGISTRY.md`): 4
coincidencias — dos filas de la tabla SSOT y los `proposito` de las dos specs
nuevas. Todas altas de esta misma entrega, ninguna vencida.

**Check 2 — el SSOT dueño de la hipótesis, y sus derivados**: el SSOT es
`EXPERIMENTO-A4-protocolo-conducta.md`; según la tabla SSOT lo referencian
`PRUEBA-PISO-RUIDO-A4.md` y `../docs-y-investigacion/PLAN-PRUEBAS.md`. Los dos se
sincronizaron en esta entrega, el SSOT primero.

**Check 3 — quién declaró estar esperando**
(`grep -rl "Deuda arrastrada.*A-04" --include="*.md" . | grep -v '^./experimentos/'`):
sin resultados. Esperable: A-04 se abrió y se cerró la pasada 1 en la misma
entrega, así que ningún documento tuvo ocasión de declarar la espera como deuda.
Contrastado contra «Documentos que esperan este resultado» del diseño, que sí
lista seis: la divergencia es de calendario, no un hueco.

| documento | que afirmaba | estado nuevo | hecho |
|---|---|---|---|
| `../SPECS_REGISTRY.md` | nada sobre A-04 | dos specs y dos filas SSOT | sincronizado |
| `EXPERIMENTO-A4-protocolo-conducta.md` | — (alta) | SSOT del «que» | sincronizado, antes que su derivado |
| `PRUEBA-PISO-RUIDO-A4.md` | — (alta) | runbook con la enmienda 1 fechada | sincronizado |
| `../docs-y-investigacion/PLAN-PRUEBAS.md` | tres experimentos, sin A-04 | A-04 con alcance de la pasada 1 y deslinde con A-02 | sincronizado |
| `../agenda/BACKLOG-INVESTIGACION.md` alta #8, #7, #5 | preguntas abiertas | marcadas en ejecución, apuntando acá | sincronizado |
| `../CONSTITUTION.md` | enforcement humano y a pedido, sin declarar si produce efecto | sin cambio | no aplica: la pasada 1 no evalúa `H1`, así que nada de lo que afirma quedó falso |
| `../AGENTS.md` | que el protocolo rige la ejecución diaria | sin cambio | no aplica: mismo motivo. El hallazgo 5 lo **refuerza** (su premisa cross-asistente quedó comprobada), no lo contradice |
| `../docs-y-investigacion/PLAN-PRUEBAS.md` A-02 | medía variabilidad entre asistentes | deslinde con A-04 declarado también de su lado | sincronizado |

## Evidencia adjunta

Repo de datos hermano `../../experimentosdd-a4/`, dos commits:

- `CALIBRACION-A4.md` — las cuatro tandas, la enmienda 1 y los tres descartes.
- `PREDICCION-A4.md` — predicción fechada, escrita antes del primer rep.
- `VALOR-VERDADERO.txt` — valor verdadero, tres vías de lectura, cambios v1→v2.
- `entorno/ENTORNO-A4.md` — versiones, invocación por rep, tabla de sondas y el
  confundido medido.
- `entorno/REGIMEN-DE-PERMISOS.md` — el régimen, lo que se probó y no funcionó, y
  la limitación sellada.
- `entorno/salida-sonda-contexto.md` — volcado literal de 31 KB del contexto de un
  rep, que es lo que sostiene que el aislamiento funcionó.
- `regla/REGLA-PUNTUACION-A4.md`, `transcripts/` (12 reps más 8 sondas),
  `scripts/`, `home-limpio/INVENTARIO.md`.

## Deuda arrastrada

- **`H1` sin evaluar** — *nuevo*. La pregunta del backlog alta #8 sigue abierta:
  nadie midió todavía si el protocolo cambia conducta.
- **La conducta medida necesita rediseño** — *nuevo*. Hace falta una conducta que
  el system prompt del harness no regale, con criterio explícito de qué la vuelve
  cara, no otra ronda de apretar el mismo fixture.
- **¿El techo es de `agy` o de cualquier harness moderno?** — *nuevo*. La pasada 1b
  (Claude Code) es lo único que lo contesta, y el diseño la condicionaba a que la
  pasada 1 saliera APTO o MARGINAL. Puede ser esa condición la que está mal
  puesta: con un techo, comparar dos harnesses es más informativo que con margen.
- **La terminal no está disponible en el régimen sellado** — *nuevo*. Limitación
  declarada arriba; levantarla es decisión del usuario, no del Operador.
- **Puntuadores sin ejercitar** — *nuevo*. La sonda de puntuador (3 transcripts
  fabricados, dos puntuadores 3/3) no llegó a correrse: la escalera se cerró
  antes. Queda pendiente para cualquier rediseño que reutilice la regla.

## Proximos pasos

1. Migrar los cinco ítems de deuda a `../agenda/BACKLOG-INVESTIGACION.md` con
   fecha y origen, **antes** de dar la pasada por cerrada.
2. Decidir entre rediseñar la conducta medida o correr la 1b con el diseño actual
   para separar «techo de `agy`» de «techo de cualquier harness».
3. No tocar el instrumento construido: aislamiento, régimen de permisos, sondas y
   regla son reutilizables tal como están.
