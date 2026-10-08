# Resultado del Experimento A-05: carga ceremonial persistida del método, en dos corpus

## Metadata
- ID experimento: A-05
- Fecha cierre: 2026-10-07
- Responsable: proyecto SDD

Diseño sellado en `c32a617` (`EXPERIMENTO-A5-carga-ceremonial.md`). El instrumento se corrió desde ese commit, extraído con `git show`, con Python 3.13.3. La autoprueba dio VERDE antes de medir.

## Resultado cuantitativo
- Metrica primaria:

| corpus | commits de método con texto nuevo | ceremonia (car.) | cambio (car.) | razón agregada | IC95 |
|---|---|---|---|---|---|
| este repositorio (`a5bc3e1`) | 102 | 242.929 | 1.177.386 | **0,171** | [0,114, 0,249] |
| [R40] (`3ae88cf`) | 28 | 31.153 | 246.989 | **0,112** | no se calculó por separado |

  Diferencia entre corpus (este menos [R40]): 0,059, con IC95 **[−0,063, +0,161]**.

  - **H1 REFUTADA.** El extremo superior del IC95 (0,249) queda por debajo de 1/3. La ceremonia que persiste en git es alrededor de un sexto de lo que escriben las entregas de método, no un tercio.
  - **H2 NO CONCLUYENTE.** El intervalo de la diferencia no cabe entero en ±0,10, y tampoco queda entero afuera. Los dos corpus superan el mínimo de 15 commits, así que no es un problema de n mínimo: es un intervalo ancho.

- Metricas secundarias, descriptivas y sin veredicto:
  - **Mediana por commit:** 0,246 acá y 0,184 en [R40]. Las dos quedan por debajo de 1/3, así que la refutación de H1 no depende de que la agregada esté dominada por commits grandes. El commit más grande de este repositorio tiene 321.308 caracteres, cuatro veces el siguiente.
  - **Commits de método que no tocan el historial:** 21 de 102 acá, 12 de 29 en [R40].
  - **Texto movido** y excluido de la razón: 283.830 caracteres acá y 16.678 en [R40]. Acá lo movido supera a toda la ceremonia, porque el planteo que migra del backlog al historial (M-29) y la rotación a tomos (M-30) son movimiento y no escritura.
  - **Los cuatro commits que cita #14:**

| ítem | commit | razón medida | cifra de partida de #14 |
|---|---|---|---|
| M-15 | `1d94947` | 0,232 | 65 % |
| M-18 | `608815c` | 0,280 | 70 % |
| M-20 | ningún mensaje de commit lo nombra | — | 53 % |
| M-19 | ningún mensaje de commit lo nombra | — | 69 % |

  Sin el `[SDD-Check]` y sin la prosa de justificación de otros documentos, los dos casos medibles caen de 65-70 % a 23-28 %. La diferencia es lo que la cifra de partida contaba y git no guarda.

## Resultado cualitativo
- Hallazgos:
  1. **La parte de la ceremonia que queda en git es chica.** Escribir el historial cuesta alrededor de un sexto del texto de una entrega de método, y la entrega típica no pasa de un cuarto. Si la ceremonia pesa, el peso está en lo que no se persiste: el bloque `[SDD-Check]` de la conversación, el orden de lectura, la prosa de justificación. Este experimento no lo mide.
  2. **El contraste entre dominios no separa nada todavía.** La estimación puntual es menor en [R40] (11 % contra 17 %), pero el intervalo admite desde un [R40] seis puntos por encima hasta dieciséis por debajo. Con 28 commits del lado de [R40], el intervalo de la diferencia queda demasiado ancho para la banda de ±0,10.
  3. **Una parte de las entregas de método no deja historial en el mismo commit**: 21 % acá y 41 % en [R40]. No es necesariamente un incumplimiento, porque una entrega partida en commits chicos asienta el historial en uno solo. Pero confirma que contar entregas por entradas de historial subestima la población, que es la advertencia de #15.
- Incidentes: ninguno. Ningún commit quedó sin leer.

## Decision
- **Ajustar.** No hay cambio de método que este resultado justifique. Lo que se ajusta es la agenda:
  - #14 deja de tener abierta la mitad de costo en lo que persiste.
  - La pregunta abierta pasa a ser el costo y el beneficio de lo que no persiste.
  - #18 queda abierta con su primer dato.

## Cambios al marco SDD

Ninguno. El resultado no mueve ninguna regla (Principio VI). Una consecuencia queda registrada para quien proponga cambios: si se busca alivianar el protocolo, compactar el historial tiene poco margen. Lo que habría que medir antes de tocar es el `[SDD-Check]` de la conversación.

## Propagacion

1. **Registro central**: `grep -n "A-05" SPECS_REGISTRY.md` no devuelve nada. Ninguna cláusula depende del estado de A-05.
2. **SSOT dueño de la hipótesis**: `docs-y-investigacion/PLAN-PRUEBAS.md`, entrada A-05. Sus derivados en la tabla SSOT son `00-INDEX.md` global y de línea, y lo que hay en `experimentos/`. Ninguno de los dos índices lista experimentos por nombre (M-44): el global los cubre con el patrón `experimentos/<id>-<nombre>/`.
3. **Quién declaró esperar**: `grep -rl "Deuda arrastrada.*A-05" --include="*.md" . | grep -v '^./experimentos/'` no devuelve nada. Se contrasta contra «Documentos que esperan este resultado» del diseño.

| documento | que afirmaba | estado nuevo | hecho |
|---|---|---|---|
| `../../docs-y-investigacion/PLAN-PRUEBAS.md` (SSOT, A-05) | A-05 en diseño | resultado: H1 refutada, H2 no concluyente | sincronizado, antes que el backlog |
| `../../agenda/BACKLOG-INVESTIGACION.md` #14 | cifra de partida de 53-70 % a recalcular; costo y beneficio abiertos | costo de lo persistido medido (17 %); los dos casos recalculables dan 23-28 %; queda abierto lo no persistido y el beneficio | sincronizado |
| `../../agenda/BACKLOG-INVESTIGACION.md` #18 | el contraste entre dos corpus es la vía | primer dato: diferencia no concluyente, IC95 [−0,06, +0,16] | sincronizado |
| `../../agenda/MEJORAS-METODO.md` M-04 | compactar tiene costo desconocido | no aplica: M-04 compacta documentos por tamaño, no el historial. El diseño la listó por la contraparte que nombra #14, y ese vínculo resultó ser de otra cosa | sin cambio, justificado |
| `../../docs-y-investigacion/ANALISIS-CASO-CAMPO-1.md` §El corpus que agrega | el segundo corpus habilita el contraste de #14 | sigue siendo cierto: el contraste se pudo correr y su resultado no contradice nada de lo que el análisis afirma | sin cambio, justificado |

## Evidencia adjunta

Las salidas del instrumento no se versionan, porque el corpus de [R40] es reservado. Se reproducen corriendo `medir_carga.py` desde `c32a617` con los comandos de §Plan de captura de datos del diseño: el instrumento es determinista y la semilla está sellada. El IC95 de [R40] por separado no está en la tabla porque el diseño sólo lo pedía para H1, que es sobre este repositorio.

## Deuda arrastrada
- nuevo: costo y beneficio de la ceremonia que **no** persiste (`[SDD-Check]` de la conversación, orden de lectura) — migrado a #14 de `../../agenda/BACKLOG-INVESTIGACION.md`.
- nuevo: H2 sin veredicto por intervalo ancho; se retoma si el corpus de [R40] crece — migrado a #18.

## Proximos pasos
- La mitad de beneficio de #14 necesita transcripciones de sesión, y hoy sólo hay desde el 2026-09-08. Antes de diseñarla, hay que decidir si un corpus de un mes alcanza.
