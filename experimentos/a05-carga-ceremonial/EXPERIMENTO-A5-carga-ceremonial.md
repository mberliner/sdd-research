# Experimento A-05: carga ceremonial persistida del método, en dos corpus

## Metadata
- ID: A-05
- Linea: docs-investigacion
- Fecha inicio: 2026-10-07
- Responsable: proyecto SDD

Origen: preguntas #14 y #18 de `../../agenda/BACKLOG-INVESTIGACION.md`. Esta pasada contesta la mitad de **costo** de #14 y el contraste entre dominios de #18. La mitad de **beneficio** de #14 queda fuera (ver §Riesgos).

## Hipotesis

Escritas el 2026-10-07, antes de correr el instrumento sobre ninguno de los dos corpus. Lo único visto de los corpus antes de escribirlas es la cantidad de commits, la fecha del primero y del último, y las constantes de método de cada backstop.

- **H1 (costo, #14).** En este repositorio, la ceremonia persistida es al menos un tercio de lo que escriben las entregas de método: razón agregada ≥ 1/3. El umbral sale de la decisión que habilita. Por encima de un tercio, compactar la ceremonia (M-04) tiene margen suficiente para que valga diseñar cómo hacerlo sin perder conducta. Por debajo, no hay mucho que ganar.
- **H2 (dominio, #18).** La razón agregada de este repositorio y la de [R40] difieren en no más de 10 puntos. Si se sostiene, la carga es del método y no del objeto de trabajo. Si difieren en más, depende del dominio.

## Diseno
- Grupo control: no hay brazo control. Es un estudio observacional sobre dos corpus ya cerrados. El contraste de H2 es entre corpus, no entre tratamiento y control.
- Grupo tratamiento: no aplica.
- Muestra:
  - Este repositorio: los commits de método ancestros de `a5bc3e1`, inclusive.
  - [R40]: los commits de método ancestros de `3ae88cf`, inclusive.
  - En los dos: sin merges y sin el commit raíz, que es una importación inicial y no una entrega.
- Duracion: una corrida por corpus.

## Sello

| componente | qué queda sellado (valor o identificador) | escalón | mecanismo | qué hace el verificador si diverge |
|---|---|---|---|---|
| tratamiento | no aplica: no hay tratamiento | — | — | — |
| instrumento | `medir_carga.py` en el commit que sella este diseño | 1 | se corre extrayéndolo de ese commit con `git show <commit>:<ruta>`, no del árbol de trabajo | — |
| entorno de ejecución | Python 3.8+ de la stdlib, sin dependencias. El intérprete efectivo se registra al correr | 3 | el instrumento usa sólo aritmética entera y `random` con semilla, así que no se espera variación entre versiones | — |
| fixture / workspace | los dos corpus, identificados por commit (`a5bc3e1` y `3ae88cf`) | 1 | el instrumento recibe el commit y recorre `git rev-list` desde ahí: un commit posterior no puede entrar | — |
| semilla y remuestreos | `20261007`, 10000 remuestreos | 1 | constantes del instrumento sellado | — |

## Metricas
- Primaria: **razón agregada** por corpus, que es la ceremonia sobre la suma de ceremonia y cambio en todos los commits de método. Se reporta con su intervalo de confianza del 95 % por remuestreo de commits.
- Secundarias, descriptivas y sin veredicto:
  - Mediana por commit de la misma razón, como robustez frente a commits grandes.
  - Cantidad de commits de método que no tocan el historial.
  - Caracteres movidos, es decir, excluidos por ser movimiento.
  - En este repositorio, la razón de los cuatro commits que #14 cita (M-15, M-18, M-20, M-19), para compararla con la cifra de partida de 53-70 %. Se identifican como los commits de método cuyo mensaje nombra el ID; si un ID no aparece en ningún mensaje, se reporta así y no se busca por otra vía.

## Documentos que esperan este resultado

| documento | que afirma hoy | que lo cambiaria |
|---|---|---|
| `../../agenda/BACKLOG-INVESTIGACION.md` #14 | una cifra de partida de 53-70 % que MUST recalcularse antes de citarse | la razón medida, y que excluya el `[SDD-Check]` |
| `../../agenda/BACKLOG-INVESTIGACION.md` #18 | que el contraste entre dos corpus es la única vía para separar método de dominio | el veredicto de H2 |
| `../../agenda/MEJORAS-METODO.md` M-04 | que compactar tiene un costo desconocido | H1 acota cuánto hay para compactar |
| `../../docs-y-investigacion/ANALISIS-CASO-CAMPO-1.md` §El corpus que agrega | que el contraste entre corpus es viable | el veredicto de H2 y su n |

## Definicion operacional

- **Qué es un commit de método.** Un commit que toca un archivo de método o del historial, según la definición de cada repositorio en el commit sellado: `METODO_FILES` y `METODO_DIRS` de su backstop, más su historial. La definición vigente se aplica a toda la historia, aunque haya cambiado con el tiempo. Las dos definiciones no son iguales: [R40] cuenta `agenda/` como método y este repositorio no. Es un confundido declarado: la población de cada corpus es la que su propio gate trata como método.
- **Ceremonia.** Caracteres no blancos de las líneas agregadas al historial de método: `historial/sdd.md` y sus tomos acá, `historial/sdd.md` en [R40].
- **Cambio.** Caracteres no blancos de las líneas agregadas a cualquier otro archivo del commit.
- **Movimiento.** Una línea agregada cuyo texto, recortado y de 20 caracteres o más, coincide con una línea quitada en el mismo commit. No es ni ceremonia ni cambio. Cubre el planteo que migra del backlog al historial (M-29) y la rotación a tomos (M-30). El mínimo de 20 caracteres evita que `---` o `- ninguna` se cuenten como movimiento.
- **Denominador.** La suma de ceremonia y cambio de los commits de método con texto nuevo. Es fijo una vez sellado el commit del corpus. Los commits sin texto nuevo, como los de sólo movimiento o sólo borrado, se cuentan aparte y no entran a la razón.
- **Aislamiento de la medición.** El instrumento sólo lee la historia de git y no ejecuta nada del corpus. De [R40] sale únicamente el resumen agregado: el modo de detalle se niega a correr sobre ese perfil.
- **Validación del instrumento.** `medir_carga.py --selftest` construye un repositorio sintético con cuatro commits de razón conocida (0,25; sólo movimiento; contenido fuera de la población; 1,0) y exige exactamente esos valores. MUST dar VERDE antes de medir. Dio VERDE el 2026-10-07.
- **Granularidad de reporte.** La métrica es por corpus y se reporta por corpus. El remuestreo es por commit, que es la unidad que la historia registra.
- **Admisibilidad de reconciliaciones.** Ninguna. Si un commit no se puede leer, se reporta cuántos y la corrida sigue con los demás. Ninguna clasificación se corrige a mano.
- **Regla de agregación.** Nunca se agregan los dos corpus. H2 compara dos razones, cada una calculada dentro de su corpus.
- **Tratamiento del empate.** Un intervalo que cruza el umbral es NO CONCLUYENTE, no una refutación.
- **Independencia entre métricas.** La mediana por commit sale de los mismos datos que la primaria. Es robustez y no evidencia adicional.
- **Quién mide.** El script. No hay puntuación humana ni lectura de prosa.

## Criterio de exito

- Condición:
  - **H1 CONFIRMADA** si el extremo inferior del IC95 de la razón de este repositorio es ≥ 1/3. **REFUTADA** si el extremo superior es < 1/3. En cualquier otro caso, NO CONCLUYENTE.
  - **H2 CONFIRMADA (equivalencia)** si el IC95 de la diferencia entre las dos razones queda entero dentro de [−0,10, +0,10]. **REFUTADA** si queda entero fuera de ese intervalo. En cualquier otro caso, NO CONCLUYENTE. El IC95 de la diferencia sale de remuestrear cada corpus por separado con la misma semilla.
  - **Tamaño mínimo.** Un corpus con menos de 15 commits de método con texto nuevo no emite veredicto en ninguna hipótesis que lo use.
- Métricas que la componen: la razón agregada de cada corpus y su IC95, todas en «Metricas».
- Comprobación de satisfacibilidad: las tres salidas de cada hipótesis son alcanzables. La razón puede tomar cualquier valor en [0, 1] y el IC se angosta con el n. Con 39 commits en [R40], el mínimo de 15 es alcanzable, pero no está garantizado: lo decide la cantidad que resulten ser de método.

## Riesgos

- **Mide sólo la ceremonia que persiste.** El bloque `[SDD-Check]` se entrega en la conversación y no queda en git: cero menciones en los mensajes de commit de este repositorio. Tampoco quedan el orden de lectura previo ni la prosa de justificación dentro de otros documentos, que se cuenta como cambio. Por eso la razón es una **cota inferior** de la carga ceremonial, y no es comparable con la cifra de 53-70 % de #14, que incluía el bloque.
- **No mide beneficio.** Saber si el `[SDD-Check]` cambió alguna entrega exige leer las sesiones. Las transcripciones locales sólo cubren desde el 2026-09-08 (12 sesiones) y su lectura es puntuación humana sobre prosa, con el riesgo del anti-patrón #6. Queda para otra pasada.
- **Commits chicos.** Una entrega partida en varios commits puede dejar el historial en uno y el cambio en otro. Eso mueve la razón por commit, no la agregada. Por eso la primaria es la agregada.
- **Mismo autor en los dos corpus.** Sumarlos agrava la autocorrelación en lugar de resolverla. Todo resultado es sobre **este** método ejercido por **este** autor en dos dominios, y MUST escribirse así en el resultado (#18).
- **Restricción de fuente de [R40].** Sólo cifras agregadas: ni nombres de archivo, ni contenido, ni nombre de la organización.

## Plan de captura de datos

1. Sellar este diseño en un commit `C`.
2. `git show C:experimentos/a05-carga-ceremonial/medir_carga.py > <tmp>/medir_carga.py`, y correr `--selftest` desde esa copia.
3. Correr sobre este repositorio con `--head a5bc3e1 --perfil propio --detalle`, para H1 y el detalle. Después correr el contraste: este repositorio como primero y [R40] como segundo (`--repo2 … --head2 3ae88cf --perfil2 r40`), sin `--detalle`. Esa corrida da el IC95 de la diferencia para H2.
4. Registrar el intérprete, las dos salidas JSON y el commit `C` en `RESULTADO-EXPERIMENTO-A5.md`. Las de [R40] se registran sólo agregadas.

## Referencias
- [R40] (corpus de contraste).
- `../../agenda/BACKLOG-INVESTIGACION.md` #6, #14, #15 y #18.
