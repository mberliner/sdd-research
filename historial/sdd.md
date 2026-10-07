# Historial SDD

Registro de fases y mejoras completadas al sistema SDD del proyecto.

Archivo vivo: el trimestre en curso. Las entradas de trimestres cerrados están, intactas, en los tomos `historial/sdd-*.md` (regla de rotación en la spec de este documento, `SPECS_REGISTRY.md`).

---

## M-30, pieza 2: el historial rota por trimestre, y el tercer trimestre de 2026 pasa a su tomo (2026-10-07) — COMPLETADA

**Acción**: regla de rotación escrita en el registro y aplicada por primera vez. Las 68 entradas anteriores al 2026-10-01 se trasladan sin cambios a `historial/sdd-2026-T1-T3.md`. El archivo vivo pasa de 2452 a 268 líneas y conserva las 9 entradas del cuarto trimestre. Motivo, en palabras del usuario: «que haya propuestas no realizadas no es un problema; que tengamos un contexto alto sin necesidad sí lo es».

### Qué cambió
- **`SPECS_REGISTRY.md`**, spec de `historial/sdd.md`:
  - rotación trimestral al asentar la primera entrada de un trimestre nuevo, sin umbral por tamaño, declarado como elección;
  - «mover no es reescribir»;
  - una cita a `historial/sdd.md` designa el archivo vivo y los tomos, así que las citas existentes —algunas en experimentos sellados— no se tocan.
- **Spec nueva de `historial/sdd-2026-T1-T3.md`**, registro histórico cerrado. Junta tres trimestres porque los dos primeros tenían una y tres entradas.
- **`historial/sdd.md`**: una línea fija remite a los tomos por patrón, no por lista. El índice mantenido a mano es la variante que falló en [R40] (planteo de M-30).
- **`00-INDEX.md`**: la fila de `historial/` nombra el archivo vivo y los tomos.

### Validación
El traslado se hizo por script y se verificó que el cuerpo del archivo vivo, concatenado con el del tomo, es idéntico byte a byte al cuerpo original. Las fechas de los encabezados ya estaban en orden descendente, y el corte cae en la primera entrada anterior al 2026-10-01. `tools/check_docs.py` en verde (0 ERROR, 0 WARN): los punteros de los ítems `Hecha` que ahora viven en el tomo resuelven gracias a la pieza 1.

### Deuda abierta
- Pieza 3, el check `historial-rotacion`: M-30.

---

## M-30, pieza 1: `backlog-metodo` resuelve los punteros también contra los tomos cerrados del historial (2026-10-07) — COMPLETADA

**Acción**: primera de tres piezas de M-30, aprobada por el usuario el 2026-10-07 con rotación trimestral y un check que avise cuándo rotar. Va primero porque la rotación mueve las entradas a las que apuntan los 22 ítems `Hecha` de `agenda/MEJORAS-METODO.md`. Si el check no supiera buscar en los tomos, el commit de la rotación nacería con 22 WARN falsos.

### Qué cambió
- **`tools/check_docs.py`**: constante `HISTORIAL_TOMOS` (`historial/sdd-*.md`, por patrón, no por lista) y función `historial_completo()`, que devuelve el archivo vivo más los tomos. `backlog-metodo` busca ahí los punteros. Mientras no exista ningún tomo, la conducta es idéntica a la anterior.
- **Caso `backlog-metodo-tomo`** en `AUTOTEST_CASOS`: un puntero que sólo existe en un tomo deja un único WARN, el de estado, en vez de dos.
- **`agenda/MEJORAS-METODO.md`**: M-30 pasa a `Aprobada`, con las dos premisas del planteo que no se sostenían.

### Validación
`tools/check_docs.py` en verde (0 ERROR, 0 WARN). `--autotest`: 31 casos, 0 fallas. Para probar al probador, se dejó `historial_completo()` devolviendo sólo el archivo vivo: el caso nuevo falló con el WARN de más que se esperaba, y se restauró.

### Deuda abierta
- Piezas 2 (regla en el registro y rotación) y 3 (check `historial-rotacion`): M-30.

---

## M-34 — El backstop tiene tabla de regresión, y la corre al tocar sus propios checks (2026-10-06) — COMPLETADA

**Acción**: M-34 ejecutada con el alcance mínimo que el propio ítem pedía: casos declarados como datos dentro de `tools/check_docs.py`, corridos por el mismo script, sin framework (el patrón `--autotest` de [R40]). La aprobó el usuario como primera mejora de la segunda tanda de la revisión de la forma de trabajo. El disparador concreto fue esta misma sesión: tres checks nuevos validados copiando, inyectando y restaurando a mano, y ninguna de esas pruebas había quedado escrita.

### Qué cambió
- **`tools/check_docs.py`**: tabla `AUTOTEST_CASOS` con 30 casos. Cada uno copia el árbol a un directorio temporal con su propio git y el gate cableado, aplica mutaciones (agregar, escribir, reemplazar, comando git, stage), corre el script real sobre la copia y exige **exactamente** los hallazgos esperados. Si aparece uno de más, es un falso positivo y el caso falla. Incluye casos de borde que no deben disparar: un link dentro de código, una mención del marcador, un bloque `[SDD-Check]` como instancia, citas válidas a repositorio, `00-INDEX.md` staged y deuda con puntero. Un `replace` cuyo texto ya no existe falla como «caso desactualizado», para que la tabla no se pudra en silencio.
- **Modo `--autotest`**, y check `autotest` en modo `--staged` sólo cuando el commit toca `tools/`: tarda unos 16 s con los casos en paralelo.
- **`AGENTS.md`**: el modo commit nombra el tercer check, y un check nuevo MUST sumar su caso.
- **`agenda/MEJORAS-METODO.md`**: M-34 pasa a `Hecha` y su planteo migra acá abajo.

### Validación
`--autotest`: 30 casos, 0 fallas. Como un autotest que nunca falla es justo la trampa de M-31, se probó al probador con tres roturas inyectadas y restauradas: `check_links` convertido en no-op (falla el caso `links`), una expectativa falsa (falla `links-en-codigo`) y un ancla borrada (falla `constitucion` como caso desactualizado). El primer intento de la segunda rotura dio verde porque el reemplazo no había encontrado su texto por un escape de comillas, y la rotura nunca se había aplicado. Se rehízo verificando que el texto se encontrara. `tools/check_docs.py` normal y con `--staged` en verde.

El gate encontró además un falso positivo de `deuda-punteros` en esta misma entrada: el check sólo aceptaba rutas `.md`, y la deuda de abajo apunta a `tools/check_docs.py`. Ahora acepta rutas con cualquier extensión, y la tabla suma ese caso.

### Planteo migrado del backlog (2026-10-06)

#### M-34 — Un check que clasifica no tiene tabla de regresión que lo pruebe

Varios checks de `../tools/check_docs.py` no verifican una propiedad: **clasifican**. `excluded-field` decide si una celda es una anotación de campo o prosa legítima; `sdd-check-fields` decide si un texto es una definición o una instancia; `ssot-collision` decide si dos specs hablan del mismo tema; `metodo-historial` decide si un archivo es método. Todos tienen frontera difusa y todos la ajustaron al menos una vez (M-23, M-27, y M-21 sigue abierto).

Un clasificador mal calibrado no se manifiesta como un error: se manifiesta como **trabajo legítimo bloqueado**, y el remedio que la gente encuentra sola es desactivar el gate. Es el mismo razonamiento por el que el `propagacion` de [R40] emite WARN y no ERROR.

En [R40] el hueco se cerró con un check `gate-reglas`: el gate lleva su tabla de regresión al lado de sus propias reglas, expuesta como `--autotest`, y el backstop la corre en cada pasada. El invariante es que las reglas sigan clasificando como declaran, verificado por el mismo script que las usa.

Acá el hueco es doble y conviene no confundirlo: no hay tabla de casos **ni** hay quien la corra. `../tools/check_docs.py` no tiene tests de ningún tipo; su única verificación es correr sobre el árbol real, que sólo contiene los casos que hoy existen. Cada ajuste de frontera se validó a mano y esa validación no quedó ejecutable en ningún lado.

Reserva antes de aprobarla: sumar una suite de tests es una dependencia nueva y un cambio de naturaleza — hoy `tools/` está declarado «no es pieza documental autorada» y vive sin infraestructura. El alcance mínimo que lo evita es el de [R40]: casos declarados como datos dentro del propio script, corridos por un check más, sin framework.

### Deuda abierta
- Checks sin caso en la tabla: la lista vive en el comentario de `AUTOTEST_CASOS` (`tools/check_docs.py`), donde también se declara que un check nuevo MUST sumar el suyo.
- M-31 y M-38, los siguientes de la misma revisión.

---

## Triaje de la deuda de septiembre y octubre con la regla nueva (2026-10-06) — COMPLETADA

**Acción**: aplicación de la regla de la entrada anterior a los pendientes de las entradas del 2026-09-01 en adelante. El usuario revisó y aprobó la tabla de destinos antes de aplicarla.

### Resultado
Juntando los repetidos quedaron 35 pendientes distintos. Así se distribuyeron:
- **Resueltos sin acción (13)**: M-40 y las tres deudas cerradas el mismo día; re-anclajes y propagaciones del 2026-09-05 y del 2026-09-30; la orientación práctica creada; el no-determinismo de Tessl (#20); los clones vivos (no hay clones desde el 2026-10-05); las líneas 337 y 398 de la orientación práctica (corregidas el 2026-09-30); las versiones de los brazos de B-09, que su §Sello ya obliga a fijar.
- **Límites, dejan de contar como deuda (8)**: entre ellos, la dirección Kiro → Spec Kit/OpenSpec, cuya búsqueda de marcadores (2026-09-06) dio negativa.
- **Método**: M-47 y M-48 nuevos, nota fechada en M-43, M-21 ya anotado (commit `c0de612`).
- **Investigación**: #23 nuevo y nota fechada en #19 (commit `c64ba7f`).
- **Ediciones de documentos**: un bloque `[SDD-Check]` de consolidación en seis documentos, que lista lo abierto, lo cerrado y lo derivado a otro lugar, sin la cadena «la de la entrega anterior sigue entera» (commit siguiente a `c64ba7f`).

### Qué cambió respecto de la tabla aprobada
Tres reclasificaciones hechas al aplicarla, las tres porque ya había una decisión escrita:
- **La dirección Kiro → Spec Kit/OpenSpec** no abre ítem: la búsqueda ya se hizo y da límite, no pregunta.
- **Las dos preguntas de OpenSpec (C6, C7)** no abren ítem: su entrada del 2026-09-05 decidió no darlas de alta a medias. Quedan en el bloque de su documento como edición pendiente: formularlas.
- **Las versiones de B-09** no son deuda: §Sello ya lo exige.

Apareció además un caso que el triaje no vio porque estaba en un bloque viejo: en `software/analisis/ANALISIS-SPEC-KIT.md`, «si la formalización de la precedencia merece experimento propio», que nunca llegó a ningún backlog. Quedó en el bloque de su documento.

### Validación
`tools/check_docs.py` en verde (0 ERROR, 0 WARN), normal y con `--staged`, en cada uno de los cuatro commits. Cada «resuelto» se contrastó con la entrega que lo resolvió.

### Deuda abierta
- Las 46 entradas anteriores al 2026-09-01 conservan su deuda en prosa y no se triaron: es registro datado (`historial/sdd.md`), y lo vigente de ellas ya debería estar en sus documentos.
- M-21, M-47 y M-48, abiertos en el backlog de método.

---

## La deuda vive donde se resuelve, y el historial sólo apunta (2026-10-06) — COMPLETADA

**Acción**: cambio de método aprobado por el usuario, opción C de la revisión de la forma de trabajo de hoy. El historial juntaba 178 pendientes en 55 secciones «Deuda abierta» y nada registraba qué pasaba con cada uno. Releídos los de septiembre y octubre, había de todo: deuda real, deuda ya resuelta y límites sin remedio, mezclados y descritos en prosa que cambiaba de una entrada a otra.

### Qué cambió
- **`AGENTS.md`, campo `Deuda arrastrada`**: lo diferido vive en un solo lugar y se cita por ID o ruta. Método va a `agenda/MEJORAS-METODO.md`; una pregunta, a `agenda/BACKLOG-INVESTIGACION.md`; una edición pendiente de un documento, al `[SDD-Check]` de ese documento; el diseño de un experimento, a su `EXPERIMENTO-*.md`. Re-explicitar pasa a ser que el ID siga abierto donde vive. Un límite sin remedio no es deuda. Así se generaliza a toda entrega la regla que `SPECS_REGISTRY.md` ya aplicaba al cerrar experimentos: la deuda no queda atada al cierre siguiente.
- **El cuarto destino** (el bloque del propio documento) lo agregó el usuario al ver el triaje: unas diez deudas eran ediciones pendientes de documentos puntuales, que no son preguntas de investigación ni cambios de método.
- **`tools/check_docs.py`**: check nuevo `deuda-punteros` (ERROR, sólo con `--staged`). Cada viñeta de «Deuda abierta» de una entrada nueva tiene que citar un `M-NN`, un `#N`, un ID de experimento, una ruta, o decir «ninguna». Las entradas anteriores no se tocan.

### Validación
`tools/check_docs.py` en verde, normal y con `--staged`. Se inyectó una entrada con cuatro viñetas —sin puntero, con `M-21`, «ninguna» y con una ruta— y sólo dio ERROR la primera. La sección de abajo es el primer caso real del check.

### Deuda abierta
- Triaje de los pendientes de sep-oct según esta regla: en revisión del usuario. Hasta entonces, las deudas de las entradas anteriores siguen descritas en ellas (`historial/sdd.md`).
- M-21, agravado desde M-40.

---

## M-35 — Las validaciones del registro dejan de ser casillas (2026-10-06) — COMPLETADA

**Acción**: M-35 ejecutada con la salida 3, elegida por el usuario. La salida 2 —que `Validaciones aplicadas` del `[SDD-Check]` nombre las validaciones de la spec y un check lo compruebe— se descarta: la mayoría de los bloques se entregan en el chat y no quedan en el repositorio, así que el check vería sólo los 18 documentos que llevan el bloque adentro.

### Qué cambió
- **`SPECS_REGISTRY.md`**: las 246 casillas `[ ]` de `validacion` (eran 195 cuando se midió M-35, el 2026-08-30), ninguna marcada nunca, pasan a ser viñetas sin casilla. §Profundidad de spec suma una línea que dice qué es el campo: criterios de revisión permanentes, no tareas.
- **`tools/check_docs.py`**: `spec-fields` da ERROR si una viñeta de `validacion` vuelve a tener casilla. Sin esa guarda, la próxima spec copiada de una vieja la reintroduce.
- **`agenda/MEJORAS-METODO.md`**: M-35 pasa a `Hecha` y su planteo migra acá abajo.

### Qué quedó como estaba, a propósito
- La lista de post-generación de `AGENTS.md` sigue con `[ ]`: ésa sí es una lista por entrega.
- El nivel «Extendida» de §Profundidad de spec sigue diciendo «requisitos con `[ ]`». Ninguna spec lo usa, y qué hacer con ese nivel es M-37.

### Validación
`tools/check_docs.py` en verde (0 ERROR, 0 WARN). La guarda se probó inyectando una casilla en la spec de `CONSTITUTION.md` y dio ERROR. `ssot-collision`, que lee esas viñetas como texto, sigue sin avisos.

### Planteo migrado del backlog (2026-10-06)

#### M-35 — Las 195 casillas de `validacion` del registro nunca se marcaron y nada las mira

Cada entrada de `../SPECS_REGISTRY.md` declara una lista de validación en formato `- [ ]`. Medido el 2026-08-30: **195 casillas en las 46 entradas, ninguna marcada, y ninguna entrada sin el campo**. Es la promesa más repetida del registro y la única que no tiene ningún respaldo.

Ningún check las lee. `parse_registry()` guarda `validacion_items`, y su único consumidor es `ssot-collision`, que las usa como texto para comparar temas entre specs — no para verificar que se hayan corrido. El campo existe para el humano que escribe la entrega y depende enteramente de que se acuerde.

**El problema no es sólo que no se verifique: es que la forma miente.** Una casilla `- [ ]` afirma un estado —«pendiente»— y sugiere que en algún momento pasa a `- [x]`. Eso nunca ocurrió ni se espera que ocurra, porque las casillas no describen el estado de *un* documento sino el criterio permanente con que se lo revisa cada vez. La notación importada de una checklist de tarea se aplicó a algo que no es una tarea.

Tres salidas, y la primera es la tentadora y la peor:

1. **Mecanizar las casillas.** No aplica a la mayoría. «La procedencia concluye explícitamente que la fuente NO suma linaje» o «las descripciones no parafrasean el `proposito` registrado» son juicio editorial; automatizarlas produciría o falsos positivos o un check que aprueba cualquier cosa. Es además la salida que `../CONSTITUTION.md` §Límite honesto advierte contra: un verificador que no juzga adecuación no puede sostener un criterio de adecuación.
2. **Cablear el campo al bloque de salida.** Que `Validaciones aplicadas` del `[SDD-Check]` MUST nombrar las validaciones de la spec del documento tocado, y que un check verifique esa correspondencia **por presencia**: los nombres declarados aparecen, o falta trabajo. No juzga si la validación se hizo bien —nada puede—, pero convierte «me acordé» en «está escrito y se puede contrastar».
3. **Retirar la forma de casilla** y dejar la lista como criterios de revisión, sin `[ ]`. No pierde nada real y deja de afirmar un estado falso.

Las salidas 2 y 3 son compatibles y probablemente sean la respuesta juntas: la 3 corrige la notación, la 2 le da al campo el único enforcement honesto disponible.

Reservas antes de aprobarla:

- **La salida 2 tiene costo por entrega y hay que dimensionarlo.** Varias specs tienen diez u once validaciones; copiarlas todas al bloque de cada entrega lo vuelve ilegible. El alcance realista es nombrar las que la entrega ejercitó y declarar las que no aplicaron, no transcribir la lista.
- **La salida 3 toca las 46 entradas de un saque.** Es una edición mecánica y de bajo riesgo, pero conviene hacerla en su propio commit y no mezclada con cambios de contenido del registro.
- **Hay una cuarta salida que no propongo pero conviene nombrar para descartarla explícitamente:** dejar todo como está y anotar en el registro que las casillas son decorativas. Es peor que las tres, porque documenta la inconsistencia en vez de resolverla, y `../CONSTITUTION.md` ya declara sus límites en un lugar donde se leen.

Decisión pendiente del usuario: cuál de las salidas, o la 2 y la 3 juntas. El ítem no la anticipa.

### Deuda abierta
- Siguen las de las dos entradas anteriores: M-21 agravado por `REFERENCIAS.md`, `backlog-metodo` no detecta un estado falso pero coherente, deuda del historial sin vista consolidada (en curso: va a los backlogs, decisión del usuario de hoy), rutas absolutas en prosa sin check, `EMOJI_SELLADOS` fuera del registro.

---

## La spec de la constitución deja de ubicar las convenciones en el registro (2026-10-06) — COMPLETADA

**Acción**: reconciliación de spec contra documento, aprobada por el usuario. Cierra la deuda que había quedado señalada en la entrada anterior.

### Qué cambió
- En `SPECS_REGISTRY.md`, la spec de `CONSTITUTION.md` decía en `excluye` que las convenciones de forma «viven en este registro». Desde la 0.2.3 viven en `CONVENCIONES.md`, que es lo que ya dice el preámbulo de la constitución. Ahora la spec apunta ahí y también nombra el léxico.

### Validación
`tools/check_docs.py` en verde (0 ERROR, 0 WARN). Ningún check podía verlo: `excluye` es prosa, y la divergencia duró desde el 2026-08-23 hasta que una lectura humana la encontró.

### Deuda abierta
- Las demás deudas de la entrada anterior siguen como estaban.

---

## M-40 y M-08 cerradas: el Principio VI suma convenciones y referencias, y el backlog de método se verifica contra sí mismo (2026-10-06) — COMPLETADA

**Acción**: enmienda constitucional PATCH (0.2.4 → 0.2.5), check nuevo y mantenimiento del backlog de método, aprobados por el usuario el mismo día tras una revisión de la forma de trabajo. El disparador fue el commit `3b9af33`, que cambió `CONVENCIONES.md` sin entrada de historial y pasó el gate: M-40 descrito el 2026-09-05 y ocurrido en la práctica.

### Decisiones del usuario
- **Qué es método**: `CONVENCIONES.md` y `REFERENCIAS.md` entran; `00-INDEX.md` queda afuera porque es navegación. La recomendación era sólo `CONVENCIONES.md`; el usuario sumó el catálogo de referencias.
- **Versión**: PATCH. El léxico vivía en `SPECS_REGISTRY.md` y `AGENTS.md`, que ya eran método, hasta que la 0.2.3 lo mudó sin actualizar la enumeración: se repara una omisión. Para `REFERENCIAS.md` el argumento no vale igual, porque nunca fue método; queda dicho y la versión queda como la decidió el usuario.
- **M-08**: se confirma como excepción permanente para documentos sellados la que ya aplicaba `EMOJI_SELLADOS` desde la entrada anterior.
- **Check**: de coherencia, no de antigüedad, para no agregar columnas a la tabla de estado.

### Qué cambió
- **`CONSTITUTION.md` 0.2.5**: el Principio VI enumera también «convenciones de léxico y forma» y «catálogo de referencias». El `Verificador:` del Principio II suma `ruta-externa`, que la entrada anterior había diferido a la próxima enmienda.
- **`tools/check_docs.py`**: `METODO_FILES` suma `CONVENCIONES.md` y `REFERENCIAS.md`, y el comentario explica por qué `00-INDEX.md` no está. Check nuevo `backlog-metodo` (WARN): todo ítem `Hecha` tiene fila en «Items cerrados», su puntero es una entrada real del historial y no conserva sección de detalle; todo ítem abierto tiene la suya; nada figura en «Items cerrados» sin estar `Hecha`.
- **Las otras copias de la enumeración** —`AGENTS.md` §Al cerrar una iteración paso 3, dos líneas de `SPECS_REGISTRY.md` y el encabezado de `agenda/MEJORAS-METODO.md`— dejan de repetirla y remiten al Principio VI. `AGENTS.md` pasa a nombrar tres checks de señal.
- **`agenda/MEJORAS-METODO.md`**: M-08 y M-40 pasan a `Hecha`, con sus planteos migrados acá abajo. El puntero de M-44 se corrigió, porque llevaba tildes y la entrada del historial no, y buscándolo literal no aparecía (lo encontró el check en su primera corrida). Los cerrados quedaron ordenados por ID, como dice el documento; M-44 y M-46 estaban arriba. M-21 y M-38 suman una nota fechada cada uno.

### Validación
`tools/check_docs.py` en verde (0 ERROR, 0 WARN). Cada rama de `backlog-metodo` se probó inyectando el caso y restaurando: ítem `Hecha` sin fila de cerrados y con detalle, ítem abierto sin detalle, puntero inexistente y fila de cerrados de un ítem no `Hecha`. Las cuatro avisaron. En la primera corrida aparecieron 19 falsos positivos por un error de parseo de `**Hecha**`, que se corrigió antes de la prueba. `metodo-historial` con `CONVENCIONES.md` staged se verifica con el commit de esta misma entrega.

### Planteos migrados del backlog (2026-10-06)

#### M-40 — La enumeración de «qué es método» del Principio VI deja afuera a `CONVENCIONES.md`, y el verificador la copia fiel

El Principio VI de `../CONSTITUTION.md` enumera qué cuenta como método: «protocolo del asistente, registro de specs, templates, esta constitución». Su verificador `metodo-historial` deriva de ahí su lista, y el comentario de `../tools/check_docs.py` lo dice sin rodeos: «La enumeracion sale literal del Principio VI [...] mas `tools/`, porque un check ES metodo».

`../CONVENCIONES.md` no está en esa enumeración. Y es el SSOT del léxico normativo (qué significa MUST, SHOULD, MAY en este repositorio), de la forma de los documentos, de los nombres de archivo y del formato de los mensajes de commit. `../AGENTS.md` le delega esas cuatro cosas por remisión explícita.

**Sonda corrida el 2026-09-05.** Se agregó una línea a `../CONVENCIONES.md`, se la dejó staged y se corrió `./tools/check_docs.py --staged`, que es el modo que invoca el gate de commit: **0 ERROR**, sin pedir entrada de historial. Un commit que redefine qué significa MUST en este repositorio pasa sin dejar rastro en `../historial/sdd.md`.

Lo que hace a este ítem distinto de M-31 —con el que comparte familia— es dónde está el defecto. En M-31 el check miraba mal. Acá **el check mira exactamente lo que le dijeron**: la lista es fiel, la fuente está incompleta. Arreglar `METODO_FILES` sin tocar el Principio VI deja la constitución diciendo una cosa y el verificador otra, que es justo la divergencia que la fidelidad de la lista evitaba.

Es una instancia de la clase 2 de `sdd-first:docs/PATRONES.md` («la lista duplicada que nada ata») en su variante menos visible: las dos enumeraciones **no** divergieron —una deriva de la otra— y el defecto viajó entero desde el original.

Qué hace falta, en este orden:

1. **Decidir si `CONVENCIONES.md` es método.** Es la pregunta real y es del usuario, no del backstop. Si lo es, el Principio VI se enmienda con su procedimiento completo (es cambio de constitución, no de check).
2. **Barrer el resto de la enumeración** con el mismo criterio antes de enmendar, para no pagar dos enmiendas: `../REFERENCIAS.md` y `../00-INDEX.md` son los otros dos candidatos, y ninguno de los dos es obvio. `agenda/` e `historial/` ya están razonados y quedan afuera.
3. **Recién entonces** actualizar `METODO_FILES`, que sigue siendo la copia fiel.

Prioridad alta y no media: mientras esté abierto, la única garantía mecánica del Principio VI tiene un agujero del tamaño del SSOT del léxico, y el repositorio no lo sabe.

#### M-08 — Emoticones en `PREREG-B7.md`

El documento viola la regla global «sin emoticones» pero está **pre-registrado y sellado**. Editarlo post-sello tiene implicancias metodológicas (Principio V). Decisión pendiente del usuario: corregir con enmienda fechada, o declarar excepción permanente para documentos sellados.

### Deuda abierta
- `backlog-metodo` mira la coherencia del estado, no si es verdadero: un ítem resuelto de hecho que sigue en `Propuesta` —como M-08 hasta hoy— pasa igual.
- M-21 se agrava: cada alta de `[Rxx]` pide ahora entrada de historial. Se cuenta antes de ajustar el check.
- La spec de `CONSTITUTION.md` en el registro sigue diciendo, en `excluye`, que las convenciones de forma «viven en este registro». Es una divergencia previa (desde la 0.2.3), señalada para que el usuario decida.
- Las 64 secciones «Deuda abierta» del historial siguen sin vista consolidada (mejora 2 de la misma revisión, no elegida en esta tanda).
- Siguen abiertas dos deudas de la entrada anterior: rutas absolutas en prosa sin check, y `EMOJI_SELLADOS` fuera del registro.

---

## `ruta-externa` mira la prosa y valida el repositorio citado; los sellados dejan de dar WARN de emoticones (2026-10-06) — COMPLETADA

**Acción**: cierre de tres deudas que dejó la entrada anterior, más una que venía de antes. La lista de repositorios hermanos y la regla de registro fechado entraron en `CONVENCIONES.md` en el commit previo, para que éste pasara el backstop solo.

### Qué cambió
- **`ruta-externa` en prosa**: además de backticks y links, marca las dos formas de ruta local que se delatan solas en texto corrido —`../` que sale de la raíz y la carpeta local de fuentes—.
- **`ruta-externa` valida `<repo>`**: una cita `<repo>:<ruta>` o `<repo>@<commit>:<ruta>` tiene que nombrar un repositorio de una URL de GitHub de `REFERENCIAS.md` o de la línea de hermanos de `CONVENCIONES.md`. Las dos listas se derivan de su fuente; el check no guarda copia. Si la línea de hermanos desaparece, falla cerrado. Para no confundir `path:line` o `campo:valor` con una cita, la ruta tiene que llevar barra o extensión.
- **`emoji` exceptúa documentos sellados**: `PREREG-B7.md` traía emoticones de antes del sello, y corregirlos sería reescribir un sellado (Principio V). La excepción es una lista a mano (`EMOJI_SELLADOS`), y por eso se vigila: una entrada cuyo archivo no existe, o que ya no tiene emoticones, da ERROR como excepción vencida.

### Validación
`tools/check_docs.py` en verde, ahora **sin WARN**. Cada rama se probó inyectando el caso y restaurando: ruta en prosa con `../` y con la carpeta local, prefijo mal escrito (`sdd-frist`), excepción vencida en `EMOJI_SELLADOS`, y línea de hermanos borrada. Las cuatro dieron ERROR; `path:line` y un hermano válido no.

### Deuda abierta
- En prosa, una ruta absoluta (`C:\...`, `/home/...`) o una relativa que no empiece con `../` no la ve el check.
- `EMOJI_SELLADOS` y el estado «sellado» no salen del registro: el registro no tiene un valor de `estado` para eso, y agregarlo sería cambiar su vocabulario.
- `ruta-externa` no figura en ningún `Verificador:` de `CONSTITUTION.md`; se difiere a la próxima enmienda.

---

## Las fuentes externas se citan por repositorio, no por copia local (2026-10-05) — COMPLETADA

**Acción**: cambio de método pedido por el usuario. Las fuentes externas no viven en este repositorio, y una cita que apunta a una copia en disco sólo la resuelve quien la escribió. En este clon, además, `fuentes-externas/` ya no tenía clones sino accesos directos de Windows, que tampoco resuelve nadie más (diagnóstico que B-09 ya había hecho el 2026-09-09 para su unidad de tratamiento).

### Qué cambió
- **`CONVENCIONES.md` §Citas a fuentes externas** (nueva): repositorio de código como `[Rxx]` + `<repo>:<ruta>`; el commit no se repite en la cita y se resuelve por el encabezado de la sección o del documento, después por lo que `REFERENCIAS.md` asigne a ese material, y por último por el último corte registrado; `<repo>@<commit>:<ruta>` cuando haga falta fijar otro. Papers y documentos, sólo `[Rxx]`. Fuente reservada, `[Rxx]` sin ruta.
- **`SPECS_REGISTRY.md`**: §Docs excluidos deja de declarar el material externo como clonado adentro; las validaciones que pedían «el clon vendored» pasan a pedir el repositorio de la fuente en el commit anclado.
- **`REFERENCIAS.md`**: sin rutas locales. Los papers declaran la versión leída de arXiv; [R39] cambia su reserva de vendorizado por una de anclaje y suma el corte `0e09037`. Se quitó el puntero de [R35] a un resumen que sólo existía en disco y nunca se versionó.
- **Unas 80 citas reescritas en 22 documentos**, fuera de `historial/` y `experimentos/`: rutas a los cuatro repositorios, a papers, al extracto de [R40], al testigo, al repositorio hermano `investigaIA` y al de datos de A-04. Las menciones en prosa a «clon vendored» en texto vigente pasan a describir la clase de evidencia sin suponer una copia interna.
- **`tools/check_docs.py`**: check nuevo `ruta-externa` (ERROR), que marca cualquier cita en backticks o link a la carpeta local de fuentes o a un `../` que sale de la raíz. Mira toda extensión y también directorios; `rutas` sólo mira `.md`. `AGENTS.md` lo suma a la enumeración de lo que cubre el backstop.

### Qué quedó como estaba, a propósito
- **`historial/` y `experimentos/`**: registro fechado, exento del check. Sus rutas describen lo que se hizo con la forma de su momento.
- **Bloques `[SDD-Check]` de entregas anteriores**: conservan su prosa («clon vendored»), por la misma razón. Sólo se reescribieron las rutas que tenían, porque el check no distingue bloques.
- **`software/DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md`, recomendación de vía híbrida**: propone mantener un clon como fuente de cosecha. Eso es una decisión sobre dónde leer, no una forma de citar, y no se toca.

### Validación
`tools/check_docs.py` en verde (0 ERROR; el WARN de emoticones de `PREREG-B7.md` es previo). El check se probó inyectando una ruta a la carpeta local y un link a un repositorio hermano: marcó las dos. Al estrenarse encontró cinco citas que el relevamiento manual no había visto —tres al repositorio de datos de A-04 y una ruta interna mal formada en `REFERENCIAS.md`, que `rutas` daba por ajena porque salía de la raíz—.

### Deuda abierta
- Una ruta escrita en prosa, sin backticks ni link, no la ve el check.
- `<repo>` no se valida contra `REFERENCIAS.md`: un prefijo mal escrito pasa.
- El historial y los experimentos conservan 13 líneas con rutas a la carpeta local, por diseño.

---

