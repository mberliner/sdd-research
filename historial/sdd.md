# Historial SDD

Registro de fases y mejoras completadas al sistema SDD del proyecto.

---

## M-46 — Una columna comparativa que no responde la misma pregunta en todas las filas (2026-09-07) — COMPLETADA

**Accion**: se corrige el instrumento de la seccion 5 de `software/ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md` y se enmienda su spec. Entra al historial porque enmienda `SPECS_REGISTRY.md` (archivo de metodo), Principio VI. El contenido del documento cambia como consecuencia, no como hallazgo nuevo: no se leyo ninguna fuente que no estuviera ya en el documento.

### Que se pidio
El usuario pidio repasar las tres primeras columnas de la tabla de paradigmas —«que es la spec», «donde vive la autoridad», «donde vive el enforcement»— porque «algunas lucen debiles», y preguntar si los paradigmas son demasiado abiertos: un «proceso ceremonial» puede aplicarse a casi todo.

### Que se verifico antes de decidir
Las dos sospechas se confirmaron leyendo la tabla contra si misma, sin fuente nueva:

- **La columna 1 mezclaba cuatro predicados.** Contestaba *cuando* en Spec Kit («una etapa»), *de que habla* en OpenSpec («el estado vigente»), *para que sirve* en sdd-first («un permiso») y *de quien es* en Kiro («un artefacto del entorno»). Un encabezado con cuatro predicados describe, pero no discrimina.
- **«Autoridad» se usaba en tres sentidos incompatibles**: quien gana ante discrepancia, quien define el metodo (Kiro: «el flujo de fases es el IDE», que es propiedad de la herramienta y no autoridad sobre el proyecto) y quien autoriza avanzar. Ademas repetia: en `sdd-first`, «en el gate» y «codigo fail-closed» eran la misma frase en dos columnas.
- **La columna 3 mezclaba enforcement del metodo con enforcement de la spec sobre el codigo**, y al mezclarlos escondia que hay tres niveles y no seis mecanismos equivalentes.
- **Cinco de los seis nombres de paradigma sobreviven si se les quita la palabra «spec»** y siguen nombrando algo real: RUP, ITIL, TDD, policy-as-code, un IDE opinado. Solo «compilacion desde la especificacion» no sobrevive.

### Que se decidio y por que no la opcion contraria
Se fija **un predicado por columna** y se define «autoridad» en un solo sentido —quien gana ante discrepancia entre spec y codigo—, que es el unico de los tres que es propio de SDD y no de cualquier metodologia. Se agrega una **escala de vinculacion** de tres niveles (N0 nada mecanico; N1 la forma del proceso; N2 la correspondencia) y la **prueba del nombre**.

La opcion contraria era dejar la tabla y solo desambiguar en una nota. Se descarto porque el defecto no era de redaccion: una columna que en cada fila responde otra pregunta no se arregla explicando que lo hace. La otra opcion descartada era no construir la escala, para no rozar `software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md`. Se descarto porque el patron —cinco de seis casos sin comprobar la correspondencia— es exactamente lo que el usuario pidio buscar, y ocultarlo por prudencia de frontera habria sido peor que declararlo con la reserva escrita, que es lo que se hizo.

**La spec prohibia presentar los paradigmas «como puesto en un orden», y la escala es un orden.** Por eso la enmienda es previa al documento: se distinguio orden **de calidad** —que sigue prohibido— de orden **de grado de vinculacion**, que es descriptivo y verificable en el mecanismo.

### Que cambio
- `SPECS_REGISTRY.md`, spec de `software/ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md`: `incluye` reformula el bullet de paradigmas (predicado uniforme obligatorio, cuatro predicados renombrados) y suma dos bullets —escala de vinculacion y prueba del nombre—; `validacion` suma tres casillas y afina la que hablaba de «puesto en un orden».
- `software/ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md` §5: tabla reescrita con las cuatro columnas uniformes, nota de correccion fechada que registra que afirmaba la version anterior, escala de vinculacion, prueba del nombre, y cuarta advertencia. §7 suma una linea sobre lo que la escala no puede decir.
- `agenda/MEJORAS-METODO.md`: alta de M-46 en la tabla de estado y en la de items cerrados.

### Como se valido
`tools/check_docs.py`: 0 ERROR. El unico WARN es preexistente y ajeno (emoji en `experimentos/b07-formato-hibrido/PREREG-B7.md`, M-08).

Verificacion manual, porque el backstop no la cubre: que las cuatro columnas respondan la misma pregunta en las seis filas, y que ninguna celda de la columna 2 repita lo que dice la 1 o la 3.

### Deuda abierta
**Nada verifica la uniformidad de predicado de una columna.** Es la casilla nueva de `validacion`, y como las 196 anteriores no la mira nadie. A diferencia de otras, esta probablemente **no** sea automatizable: decidir si dos celdas contestan la misma pregunta es juicio, no sintaxis. Se declara asi en vez de proponerla como candidato de M-31 o M-35.

**El defecto es de clase, no de este documento.** La tabla corregida era la mas cuidada del repositorio y el defecto sobrevivio a tres enmiendas de spec en un dia. Ninguna otra tabla comparativa del corpus fue auditada con este criterio, y hay varias: `comun/MARCO-COMPARATIVO-DOS-LINEAS.md` y `software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md` al menos. **No se auditaron acá** —seria alcance ajeno a lo pedido— y queda como pendiente sin item propio.

---

## M-44 — Los indices de linea no listan experimentos, y eso nunca se escribio (2026-09-06) — COMPLETADA

**Accion**: se asienta por escrito una regla que ya se cumplia. Entra al historial porque enmienda una spec de `SPECS_REGISTRY.md` (archivo de metodo), Principio VI.

### Que se pidio
Explicar y despues resolver una deuda que la apertura de B-09 arrastro tres entregas seguidas: si un experimento entra al indice de su linea. Al abrir B-09 hubo que decidirlo de hecho —quedo afuera— sin ninguna norma donde apoyarse.

### Que se verifico antes de decidir
Barrido de los tres indices, y el resultado desarmo la premisa con la que se habia planteado la deuda. No es un caso ambiguo con dos caminos razonables:

- `software/00-INDEX.md` no lista B-06 ni B-07, cerrados desde julio.
- `docs-y-investigacion/00-INDEX.md` no lista A-04. Ni una mencion.
- `00-INDEX.md` global **si** lista el directorio: la fila `experimentos/<id>-<nombre>/`, glosada «disenos, runbooks y resultados, una carpeta por experimento».

O sea que la practica es uniforme en tres experimentos, dos lineas y varios meses, y la navegacion ya esta resuelta en dos saltos que no duplican nada: el indice global apunta al directorio y el `PLAN-PRUEBAS.md` de cada linea apunta a cada experimento **con su estado**. Lo unico que faltaba era escribirlo.

### Que se decidio y por que no la opcion contraria
Los indices de linea **no listan experimentos, abiertos ni cerrados**. Listarlos agregaria un tercer lugar donde el estado de un experimento puede quedar viejo, que es exactamente el defecto que M-14 cerro para los documentos: `software/00-INDEX.md` habia quedado con `Estado: Borrador` cuando el registro ya declaraba `Activo`. El caso de B-09 lo vuelve concreto: esta en BORRADOR PRE-SELLO, y listarlo invita a anotar ese estado al lado del link — el campo que M-14 prohibio.

### Que cambio
- `SPECS_REGISTRY.md`, spec de `docs-y-investigacion/00-INDEX.md` y `software/00-INDEX.md`: bullet nuevo en `excluye` con la regla y su motivo, mas una casilla nueva de `validacion` («ningun link apunta a un documento de `experimentos/`»).
- `agenda/MEJORAS-METODO.md`: alta de M-44 en la tabla de estado y en la tabla de items cerrados.
- Ningun indice se edito: los tres ya cumplian.

### Como se valido
`tools/check_docs.py`: 0 ERROR. El unico WARN es preexistente y ajeno (emoji en `experimentos/b07-formato-hibrido/PREREG-B7.md`, M-08).

Verificacion manual, porque el backstop no la cubre: se releyeron los tres indices y ninguno enlaza a `experimentos/`.

### Deuda abierta
**La casilla nueva de `validacion` no la mira nadie.** Es una de las 195 casillas que M-35 ya declaro nunca marcadas y sin verificador — este cambio suma la 196.ª en vez de resolver el problema de fondo, y eso se declara en vez de disimularse. El check seria barato (ningun link de un indice de linea resuelve dentro de `experimentos/`) y entra naturalmente por M-31 o por M-35, no por aca.

**El alcance es de los indices de linea, no del global.** El `00-INDEX.md` global sigue listando el directorio de experimentos y debe seguir haciendolo: es lo que sostiene el primero de los dos saltos. Si alguna vez se toca esa fila, esta regla se queda sin la mitad de su fundamento.

---

## Alta del analisis CHI 2026 sobre edicion colaborativa con IA (2026-09-06) — COMPLETADA

**Accion**: alta de spec y documento nuevo en Linea A. Entra al historial porque toca `SPECS_REGISTRY.md` (archivo de metodo), no porque el metodo haya cambiado.

### Que se pidio
Un resumen para Linea A de una fuente externa (arXiv 2509.11826v2, ACM CHI 2026, ya citada puntualmente como [R53] en `comun/PRESENTACION-SDD-DOCS.md`), analogo a los `ANALISIS-*.md` que Linea B ya tiene en `software/analisis/`, en un directorio propio a definir.

### Que se decidio antes de escribir
No habia spec para el documento nuevo; se propuso una minima (proposito, incluye/excluye, validacion) siguiendo el precedente de `docs-y-investigacion/ANALISIS-CASO-CAMPO-1.md` — que fija el patron de Linea A: el analisis vive directo en `docs-y-investigacion/`, sin subdirectorio `analisis/` (eso es convencion de Linea B). El usuario aprobo con un ajuste: el analisis queda independiente, sin referenciar `comun/PRESENTACION-SDD-DOCS.md`.

### Que cambio
- `docs-y-investigacion/ANALISIS-EDICION-COLABORATIVA-IA.md`: documento nuevo. Caracteriza el estudio (RQs, prototipo, metodologia N=30/14 equipos/technology probe de una semana), sus cinco hallazgos centrales y dos decisiones de diseño con razon explicita, y separa lo transferible como hipotesis para Linea A de lo que no lo es.
- `SPECS_REGISTRY.md`: spec nueva para el documento.
- `docs-y-investigacion/00-INDEX.md`: entrada nueva en §Analisis de casos.

### Como se valido
`tools/check_docs.py`: 0 ERROR, el unico WARN es preexistente y ajeno (emoji en `experimentos/b07-formato-hibrido/PREREG-B7.md`).

### Deuda abierta
Ninguna. El documento no da de alta items de agenda: la hipotesis de disenar un experimento con mas de un autor humano, que la seccion de transferibilidad sugiere, queda anotada ahi mismo como candidata futura, no como item abierto de `agenda/BACKLOG-INVESTIGACION.md`.

---

## Los seis ANALISIS-* de linea B se mudan a software/analisis/ (2026-09-06) — COMPLETADA

**Accion**: reorganizacion pura de rutas, sin cambio de contenido. Los seis documentos `ANALISIS-SPEC-KIT.md`, `ANALISIS-SUPERPOWERS.md`, `ANALISIS-OPENSPEC.md`, `ANALISIS-SDD-FIRST.md`, `ANALISIS-TESSL.md` y `ANALISIS-KIRO.md` pasan de `software/` a `software/analisis/`. Entra al historial porque toca `SPECS_REGISTRY.md` (archivo de metodo), no porque el metodo haya cambiado.

### Que se pidio
Evaluar si separar en subdirectorios los directorios con muchos archivos ayudaba a la administracion y revision, tomando `software/` (16 documentos) como caso. Antes de mover nada se pidio el mapa completo de referencias a tocar, para decidir con el costo a la vista.

### Que cambio
- Movidos los seis archivos a `software/analisis/` (`git mv`).
- Los seis `path:` correspondientes en `SPECS_REGISTRY.md`.
- Las 106 ocurrencias de `software/ANALISIS-*.md` como ruta absoluta-desde-raiz en el resto del repo (`AGENTS.md`, `REFERENCIAS.md`, `comun/*.md`, `agenda/*.md`, `experimentos/b07-formato-hibrido/*.md`, `software/*.md`, `historial/sdd.md` incluidas las entradas retroactivas que citaban la ruta vieja).
- Los 94 backticks `../` internos de los seis archivos movidos, que pasan a `../../` por bajar un nivel (apuntaban a `AGENTS.md`, `SPECS_REGISTRY.md`, `CONSTITUTION.md`, `CONVENCIONES.md`, `REFERENCIAS.md`, `agenda/`, `comun/`, `experimentos/`, `fuentes-externas/`, `tools/`, `historial/`).
- Un caso especial en `ANALISIS-OPENSPEC.md`: una referencia con `../` a `ANALISIS-SDD-FIRST.md` que ya era redundante antes del cambio (equivalente a la ruta absoluta-desde-raiz), corregida a `software/analisis/ANALISIS-SDD-FIRST.md`.
- Los 4 links relativos de `software/00-INDEX.md` a los cuatro analisis que ya listaba.

### Como se valido
`tools/check_docs.py`: 0 ERROR, el unico WARN es preexistente y ajeno (emoji en `experimentos/b07-formato-hibrido/PREREG-B7.md`). Confirma que ningun link ni ruta en backticks quedo roto.

### Deuda abierta
Ninguna nueva. `software/00-INDEX.md` ya no listaba `ANALISIS-TESSL.md` ni `ANALISIS-KIRO.md` antes de este cambio; ese hueco preexistente no se toco, por estar fuera de alcance de una reorganizacion de rutas.

---

## Un paradigma por caso, derivado del instrumento y no de fuentes nuevas (2026-09-05) — COMPLETADA

**Accion**: seccion 5 nueva en `software/ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md`, con enmienda de spec previa (tercera del documento en el dia). Las secciones de escenarios y de limites se renumeraron a 6 y 7.

### Que se pidio
Si se podia definir un paradigma claro de cada implementacion **a partir de las dimensiones ya establecidas**. La restriccion vino en la pregunta: a partir de estas dimensiones, no de material nuevo.

### La decision de alcance, que se consulto antes de escribir
Caracterizar seis casos con un mismo eje se parece peligrosamente a lectura cruzada, y esa es materia de `software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, su SSOT. Se ofrecieron tres destinos —este documento, aquel, o uno nuevo— y el usuario eligio este, por el motivo que lo justifica: **la derivacion sale integra del instrumento de quince dimensiones, que es de este documento**. La frontera quedo escrita en tres lugares: en `incluye` y `excluye` de la spec, y como tercera advertencia de la propia seccion.

### Que dice
Las quince dimensiones convergen en un eje discriminante unico —**que es la spec, y donde vive la autoridad**— del que salen seis paradigmas: proceso ceremonial parametrizable (Spec Kit), control de cambios sobre un estado declarado (OpenSpec), disciplina de oficio (Superpowers), cumplimiento verificado por codigo (sdd-first), metodo encarnado en el producto (Kiro) y compilacion desde la especificacion (Tessl). Cada uno se rastrea a D1, D2, D3, D4, D7 y D8.

Lo que hace util a la seccion, y no es un adorno: **el modo de falla de cada caso cae exactamente sobre la operacion que define su paradigma**. El costo fijo del ciclo en el que apuesta al orden de las fases; la fusion del delta en el que lleva un estado vigente; el contexto en el que gobierna la conducta; el verificador en el que ejecuta el cumplimiento; el proveedor en el que no es tuyo; el no-determinismo en el que compila. Eso no se busco: aparecio al ordenar.

### Que NO dice
No ordena por calidad, y **no es una particion**: Superpowers gobierna el trabajo del agente y los otros cinco gobiernan artefactos, asi que es ortogonal y se combina. La seccion 7 suma un limite nuevo: cual de los seis paradigmas es el correcto es indecidible con lo que hay.

### Como se valido
`tools/check_docs.py` en verde (0 ERROR; unico WARN preexistente y ajeno). Ninguna referencia nueva: la seccion cita [R50] y §4 quinquies, ya presentes.

### Deuda abierta
La frontera con `CONVERGENCIA-IMPLEMENTACIONES-SDD.md` es una **restriccion declarada que ningun verificador comprueba**. Si alguna vez la seccion 5 empieza a afirmar derivacion o linaje entre casos, nada la va a frenar salvo la lectura humana. Queda anotado para la eventual revision del instrumento v2 de convergencia.

---

## D15: uso y reputacion en redes entra a la orientacion practica (2026-09-05) — COMPLETADA

**Accion**: alta de una dimension a pedido del usuario en `software/ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md`, con enmienda de spec previa y cuatro referencias nuevas. El documento pasa de **catorce a quince dimensiones**. En la misma jornada, y antes de esto, salio del documento toda mencion al proyecto testigo, que la spec ya excluia.

### Que se pidio
Informacion de usuarios de **primera mano**: objeciones fundadas y verificaciones de buen comportamiento. No popularidad.

### Que cambio
- **Enmienda de spec** (segunda del documento): `proposito` suma la reputacion reportada por terceros; `incluye` sube a quince dimensiones y suma un bullet propio para D15 con sus tres canales y sus sesgos; `validacion` suma tres casillas —marca `[reportado]` obligatoria, procedencia fechada de las metricas de atencion, y que la ausencia de reportes se lea como ausencia de exposicion y no de defectos—.
- **D15 Uso y reputacion en redes**, con fila en la tabla resumen y **seccion propia (§4 quinquies)** para los seis casos, en vez de repartirse por ficha: la advertencia de clase de evidencia tenia que quedar en un solo lugar y antes de la primera cita.
- **Tercera marca de procedencia, `[reportado]`.** El documento tenia dos, `[declarado]` y `[derivado]`. Lo que dice un tercero sobre su propia experiencia no es ninguna de las dos.
- **Altas en `REFERENCIAS.md`**: [R47] hilos publicos de practica, [R48] discusiones y trackers de los propios proyectos, [R49] metricas de la API de GitHub con fecha y comando, [R50] prensa tecnica del incidente de cupos y precios de Kiro. Las cuatro entradas declaran su sesgo y prohiben expresamente su uso como medicion.
- **Fila nueva en la tabla de escenarios** y **bullet nuevo en la seccion 6** (lo que el documento no puede decir).

### Lo que la dimension mostro
La objecion recurrente de cada caso **coincide con el modo de falla que el documento ya habia derivado de su mecanismo**: el costo fijo del ciclo en Spec Kit, la deriva al fusionar el delta en OpenSpec, el consumo de contexto en Superpowers. Es convergencia entre dos clases de evidencia independientes, y quedo escrita como interesante **y debil a la vez**: quien leyo los mecanismos y quien selecciono las citas es la misma persona.

Dos casos quedan **sin ningun reporte**, por motivos opuestos: sdd-first porque nadie de afuera lo uso (0 estrellas, 0 forks, factor de bus 1), y Tessl porque casi nadie pudo usarlo (beta cerrada, D14). Ninguna de las dos ausencias se presenta como dato favorable.

### Como se valido
`tools/check_docs.py` en verde (0 ERROR; el unico WARN es preexistente y ajeno). Metricas de atencion tomadas el 2026-09-05 con `curl` contra la API de GitHub, con los numeros escritos en [R49]. Cada cita de practica lleva handle y referencia.

### Deuda abierta
**Ninguna fuente de D15 tiene poblacion definida**, y no hay forma de mejorar esa clase de evidencia sin un instrumento propio, que no existe. El conjunto de reportes recogidos es el que devolvio la busqueda de ese dia, sin criterio de exhaustividad: **no es reproducible tal cual**. Si la dimension se vuelve a mirar, MUST declararse el criterio de busqueda antes de buscar.

---

## Abierto o cerrado deja de ser filtro y pasa a ser dimension; Tessl entra a la orientacion practica (2026-09-05) — COMPLETADA

**Accion**: correccion de un error de diseño propio en `software/ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md`, señalado por el usuario, con enmienda de spec. El documento se entrego ayer con doce dimensiones y cuatro casos; queda con **catorce dimensiones y seis casos**.

### El error
El criterio de poblacion declarado era la **adoptabilidad**, y bajo el se admitio a Kiro y se excluyo a Tessl por tener su Framework en beta cerrada. Dos cosas estaban mal:

1. **Incoherencia visible.** Kiro tambien es producto cerrado y entraba. Leidas juntas, las dos filas hacian parecer que «cerrado» era lo que excluia, cuando el criterio declarado era otro. Un lector razonable concluia que el documento discrimina por apertura sin decirlo.
2. **El criterio estaba mal elegido para el proposito.** El documento existe para ayudar a decidir, y dejaba afuera al **unico caso del corpus que regenera codigo desde la spec**. La entrega de ayer registro eso como «incomodidad»; era, en realidad, la señal de que el criterio no servia. Saber que una herramienta existe, que hace distinto y que todavia no se consigue **es** informacion para decidir.

La observacion del usuario fue precisa: abierto o cerrado es una caracteristica mas a documentar, no una puerta.

### Que cambio
- **Enmienda de spec**: `proposito` pasa de «adoptable» a «que alguien pueda evaluar o adoptar»; `incluye` sube de doce a catorce dimensiones y suma la distincion entre perder la herramienta y perder los artefactos; `excluye` reformula por que el testigo sigue afuera —no es un producto, que es un motivo distinto—; `validacion` suma tres casillas, entre ellas que **la apertura y la disponibilidad nunca se usen para admitir o excluir**.
- **D13 Apertura del codigo** y **D14 Disponibilidad**, nuevas. La seccion 2 declara por que se agregan: estaban implicitas y operando como filtro, que es la peor forma de tener una dimension — decidia admisiones sin figurar en ningun lado.
- **Tessl entra** con ficha propia (§4 ter), encabezada por la clase de evidencia mas debil del documento: producto cerrado, Framework en beta cerrada, y su rasgo principal verificado por [R20] y no por la fuente.
- **§4 quater, nueva**: que decide la apertura en la practica, separada en cuatro cosas que se deciden por separado —auditar el metodo, medir madurez y actividad, forkear, y conservar los artefactos—.
- **Tabla resumen** ampliada a seis columnas y catorce filas. En los dos casos cerrados, D9 y D10 se declaran **no medibles** en vez de completarse con datos no comparables.

### Una afirmacion propia corregida en su lugar
La ficha de Kiro decia que su salida era «la mas cara de las cinco» porque «el metodo esta atado al producto». Era demasiado gruesa y confundia dos cosas: **un producto cerrado no te encierra los documentos, te encierra el motor.** `.kiro/specs/` y `.kiro/steering/` son markdown en el repositorio del usuario; lo que no se va con vos es el flujo de fases, las compuertas y los hooks. Lo mismo en Tessl con los `.spec.md`, con un agravante propio: el codigo generado lleva marca `DO NOT EDIT`, asi que si la herramienta deja de estar, lo que queda es codigo generado que nadie mantuvo nunca a mano. La correccion quedo escrita **en el lugar de la afirmacion anterior y con nota**, no reescrita en silencio.

Tambien se corrigio una fila de la tabla de escenarios que decia «necesito poder auditar, forkear o llevarme el metodo: los cuatro **menos** Kiro». Mezclaba tres cosas distintas y la ultima era falsa.

### Validacion
`tools/check_docs.py` en verde (0 ERROR) despues de cada edicion.

### Deuda abierta
- **D9 y D10 no son medibles en los dos casos cerrados**, y no lo seran mientras no publiquen repositorio. Queda declarado en la tabla en vez de completado.
- El *Framework* de Tessl sigue en beta cerrada: su ficha describe algo que hoy no se puede probar.
- Su rasgo principal se conoce por [R20], no por la fuente.
- Sigue abierto: M-40, M-41, M-42, el ecosistema del 1.0 de Spec Kit sin caracterizar, instrumento v2 sin decidir, y la pregunta que abre el no-determinismo observado, sin item.

---

## Alta de ANALISIS-TESSL: el unico caso que regenera, y la deuda de procedencia queda saldada (2026-09-05) — COMPLETADA

**Accion**: alta de `software/analisis/ANALISIS-TESSL.md` con spec registrada antes de escribirlo, alta de [R46], anotacion de [R20], y propagacion a tres documentos. Cierra la deuda abierta el 2026-08-02: «Kiro y Tessl siguen sin pasar por el filtro de procedencia».

### La fuente que sostiene el hallazgo no era la propuesta
El pedido traia dos URLs del blog de Tessl y una caracterizacion con directivas `@generate`/`@describe`/`@use` y tres recursos plans/specs/tests. **Ninguna de las dos URLs sostiene eso**: la nota de lanzamiento no enumera esos tres recursos, y el anuncio de productos describe specs que **guian** al agente, no que generen codigo. Lo que resolvio la cuestion fue **[R20] Fowler, que ya estaba en `REFERENCIAS.md` desde el 2026-06-03** y cuyo titulo nombra a Tessl, mas `docs.tessl.io`. La verificacion cambio la atribucion, no la conclusion: el encuadre del pedido era correcto y su fuente no.

### Lo que Tessl es, y por que importa mas que su tamaño
**Es el unico caso del corpus que regenera codigo desde la spec.** Verificado en [R20], textual: «Running `tessl build` for this spec generates the corresponding JavaScript code file», con los archivos generados marcados `// GENERATED FROM SPEC - DO NOT EDIT`. Y su ubicacion, tambien textual: «Tessl is the only one of these three tools that explicitly aspires to a spec-anchored approach, and is even **exploring the spec-as-source level of SDD**».

Los cuatro casos de la tabla de convergencia son *spec-anchored*: ninguno regenera. Spec Kit **enuncia** la Power Inversion y su referencia declara que no impone ninguna persistencia; Superpowers no regenera; OpenSpec fusiona deltas; Kiro sincroniza en dos direcciones. **La posicion fuerte del corpus existe y no es la de Spec Kit: es la de Tessl.** De ahi la precision agregada a C3 de `ANALISIS-SPEC-KIT.md`: al citar «la posicion mas fuerte» MUST nombrarse a quien se le atribuye, porque **la fuente que la enuncia y la que la ejerce no son la misma**.

**Un rasgo sin equivalente**: el *Spec Registry* distribuye **contenido de spec** —mas de 10.000 specs de uso de librerias, versionadas, y las propias publicables como paquete—, mientras los otros cinco distribuyen **metodo**. Es la spec tratada como dependencia. Registrada como dimension fuera del instrumento v1, sin veredicto: un solo caso y en beta.

**Y una observacion de terceros sobre regeneracion**: el autor de [R20] corrio la generacion varias veces desde la misma spec y reporta «the non-determinism in action». Es observacion de un practicante identificado, sin diseño ni repeticiones declaradas: **no es una medicion** y el documento lo dice en un parrafo propio.

### Lo que NO se hizo, y es deliberado
**B-07 esta cerrado y no se toco.** La tentacion de leer a Tessl como confirmacion —o como refutacion— de la tesis de regenerabilidad de este proyecto es exactamente lo que el Principio V prohibe, y la spec del documento lo pone en `excluye`. Lo que corresponde es un item de backlog con una pregunta **nueva**, y **no se dio de alta**: plantearla bien es trabajo propio.

### Que cambio
- `REFERENCIAS.md`: alta de **[R46]** con su clase de evidencia (Framework en beta cerrada, sin clon posible). **[R20] pasa a ser fuente de carga**: lleva ahora la taxonomia de tres niveles textual, la ubicacion de Tessl y la observacion de no-determinismo, con su estatuto declarado.
- `SPECS_REGISTRY.md`: spec de `software/analisis/ANALISIS-TESSL.md`, con una casilla de validacion que dice explicitamente que el documento **no reformula B-07**.
- `software/analisis/ANALISIS-TESSL.md`: alta.
- `software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md`: fila de procedencia; dimension «la spec como dependencia instalable» registrada fuera del instrumento; y un parrafo nuevo en §Que se puede inferir que dice que **un caso del corpus si regenera y no es ninguno de los cuatro de la tabla**. Instrumento sigue en v1.
- `software/analisis/ANALISIS-SPEC-KIT.md`: precision en C3.
- `software/ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md`: Tessl **queda fuera** por beta cerrada, con el motivo escrito y la incomodidad declarada — el documento excluye, por un criterio correcto, al caso mas distinto de todos.

### Validacion
`tools/check_docs.py` en verde (0 ERROR) despues de cada edicion. Las citas de [R20] y [R46] se verificaron en la pagina que las contiene el 2026-09-05.

### Deuda abierta
- **La pregunta que abre el no-determinismo observado sigue sin item** en ningun backlog.
- **Tessl fuera de la orientacion practica** mientras el Framework siga en beta cerrada; revisar si abre.
- Su rasgo distintivo se conoce **por un tercero**, no por la fuente, y eso no tiene remedio con el producto cerrado.
- La direccion Kiro -> Spec Kit / OpenSpec sigue abierta y exige marcadores de difusion.
- Sigue abierto: M-40, M-41, M-42, el ecosistema del 1.0 de Spec Kit sin caracterizar, instrumento v2 sin decidir.

---

## Kiro se propaga a los tres documentos que lo esperaban, y debilita un argumento propio (2026-09-05) — COMPLETADA

**Accion**: propagacion de `software/analisis/ANALISIS-KIRO.md` a los tres derivados que la entrega anterior dejo señalados. Cierra la deuda que ella misma abrio.

### Lo que Kiro le hace al argumento de convergencia
`CONVERGENCIA-IMPLEMENTACIONES-SDD.md` sostenia la independencia de OpenSpec «frente a Spec Kit por fechas verificables» y declaraba la reserva «mientras Kiro no se lea». Kiro se leyo, y el resultado **no es la confirmacion que la reserva esperaba**: Kiro se anuncio 22 dias antes del primer commit de OpenSpec y 38 antes del de Spec Kit. Es el caso mas antiguo del corpus.

Eso cierra una direccion —Kiro no puede derivar de ninguno— y no abre la contraria. Pero **retira la defensa por fecha en la direccion Kiro -> Spec Kit / OpenSpec, para los dos**. La reserva quedo reformulada: ya no dice «mientras Kiro no se lea» sino que establecer o descartar esa derivacion exige marcadores de difusion y no cronologia, y que ese trabajo no esta hecho. Ahora alcanza a **dos columnas** y no a una.

Se dejo escrito el corte en sentido contrario, para que la reformulacion no se lea como una acusacion: la triada requisitos-diseño-tareas es anterior a los cinco por decadas, igual que `WHEN/THEN` desciende de Gherkin [R07]. Coincidir en un ancestro comun muy anterior no es difusion entre casos.

**Kiro no toma columna en la tabla de veredictos**, y el motivo es de clase de evidencia y no de linaje: las ocho filas se contestaron leyendo archivos y con Kiro eso es imposible. Una columna suya pareceria del mismo tipo que las otras cuatro y no lo seria.

### La candidata a instrumento v2 gana lo que le faltaba
«La ceremonia escala con el tamaño del trabajo» pasa de tres casos a **cuatro contra uno**. Y con Kiro aparece el eje sobre el que discriminaria, que es lo que la volvia solo una coincidencia: **no coinciden en que escala**. Superpowers mantiene la compuerta fija por diseño explicito —«what scales with simplicity is the artifact, never the approval»— y Kiro la retira en `Quick Spec`, que genera los tres artefactos sin compuertas de aprobacion. Una dimension donde todos hacen lo mismo no informa; esta separa a dos casos en una decision de diseño nombrable.

### Que cambio
- `software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md`: fila de procedencia para Kiro con su exclusion motivada; §Limite del filtro reformulado entero; la dimension candidata a v2 ampliada con el cuarto caso y con su eje de discriminacion; bloque `[SDD-Check]` propio.
- `software/analisis/ANALISIS-OPENSPEC.md`: su reserva ya estaba bien formulada —«tres semanas de anterioridad y un formato de requisitos emparentado no alcanzan para afirmar independencia total»— y solo se actualizo que Kiro dejo de estar ausente, con el resultado: la lectura **no la resolvio, la extendio** a Spec Kit.
- `software/ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md`: Kiro entra a la poblacion «con asterisco» y recibe ficha propia (§4 bis), encabezada por la asimetria de evidencia. Tres filas nuevas en la tabla de escenarios, incluida la que corre en su contra —«necesito poder auditar, forkear o llevarme el metodo: los cuatro **menos** Kiro»—, y una advertencia nueva que dice que Kiro esta peor verificado que los demas y por que.

### El dato practico que aparecio al escribir la ficha
Kiro es el unico caso donde **el metodo no se instala: la herramienta lo trae**. Entrada barata, sin scaffolding. Y su contracara exacta, que ningun otro tiene: **la salida es la mas cara de las cinco**, porque el flujo, las compuertas y los hooks *son* la herramienta. Los otros cuatro dejan archivos que sobreviven al producto; ademas son MIT o Apache 2.0 y se pueden leer enteros.

### Validacion
`tools/check_docs.py` en verde (0 ERROR) despues de cada edicion.

### Deuda abierta
- **La direccion Kiro -> Spec Kit / OpenSpec queda abierta** y exige marcadores de difusion, no fechas. Es el trabajo que la reformulacion deja planteado y no hace.
- **Tessl sigue sin filtro de procedencia.**
- **La asimetria de evidencia de Kiro no tiene remedio** mientras el producto sea cerrado: sus dimensiones de madurez, actividad y licencia se responden en prosa, no con datos comparables a los de los otros cuatro.
- **Instrumento v2 sin decidir**, ahora con una candidata bastante mas fuerte que ayer.
- Sigue abierto: M-40, M-41, M-42, el ecosistema del 1.0 de Spec Kit sin caracterizar.

---

## Alta de ANALISIS-KIRO: el caso mas antiguo del corpus entra como metodo, sin clon posible (2026-09-05) — COMPLETADA

**Accion**: alta de `software/analisis/ANALISIS-KIRO.md` con spec registrada antes de escribirlo, mas [R44] y [R45] en `REFERENCIAS.md`. Paga a medias una deuda declarada desde el 2026-08-02: «Kiro y Tessl siguen sin pasar por el filtro de procedencia». Tessl sigue pendiente.

### La clase de evidencia es distinta, y eso condiciona todo
Kiro es **producto cerrado**: su repositorio publico declara «The Kiro product source code is not hosted here» y aloja solo issues. **No hay clon vendored y no puede haberlo.** Los otros cuatro casos se caracterizaron leyendo archivos; este se caracteriza leyendo documentacion de producto. Por eso el documento no emite ningun veredicto comparativo y la advertencia encabeza el texto en vez de ir en las reservas.

### Lo que devolvio la lectura
**Es el caso mas antiguo del corpus.** Anuncio del **2025-07-14**, verificado en su propio blog: 22 dias antes del primer commit de OpenSpec y 38 antes del de Spec Kit.

Eso decide una sola cosa —Kiro no puede derivar de ningun otro caso— y **no** decide la contraria: anterioridad no es derivacion. Y hay un corte en sentido opuesto que el documento deja escrito: la triada requisitos-diseño-tareas es anterior a los cinco por decadas, asi que coincidir en ella no es marcador de difusion, igual que `WHEN/THEN` desciende de Gherkin [R07]. Lo que si cambia es que **la defensa por fecha ya no esta disponible**: `CONVERGENCIA` sostenia la independencia de OpenSpec frente a Spec Kit con fechas y declaraba que frente a Kiro no estaba establecida; ahora se sabe que Kiro precede a los dos. No convierte convergencia en difusion; retira un argumento.

**La escala de ceremonia pasa a cuatro casos, y gana el eje que la vuelve informativa.** Kiro tiene `Feature Spec` con compuertas en dos ordenamientos, `Quick Spec` que las **saltea** —«auto-generate[s] all three artifacts without approval gates»— y `Quick Plan`. Con Superpowers, Spec Kit y nuestro linaje son cuatro de cinco. Y no coinciden en **que** escala: Superpowers mantiene la compuerta fija por diseño explicito («what scales with simplicity is the artifact, never the approval») y Kiro la retira. Esa divergencia interna es exactamente lo que le faltaba a la candidata a instrumento v2 registrada ayer.

**EARS.** Kiro adopta una sintaxis de requisitos con nombre propio y reglas de patron (`WHEN ... THE SYSTEM SHALL ...`, con `IF-THEN` para condiciones de error). Refuerza la fila 2 y agrega el dato de que **tres de cinco** casos apoyan su lenguaje normativo en una fuente externa nombrada.

**Persistencia.** «Kiro's specs stay synced with your evolving codebase. Developers can author code and ask Kiro to update specs». Es *spec-anchored* en [R30] y **flow-back** en los modelos de [R10], con el riesgo que esa fuente le atribuye: «silent divergence». Es el unico caso del corpus que declara la sincronizacion **desde el codigo hacia la spec** como camino previsto por la herramienta.

### Sobre las fuentes propuestas
Se verificaron las siete. Las oficiales (blog, docs y tracker de `kiro.dev` / GitHub) sostienen todo el documento. `sddobservatory.com` existe, es comunitario con metodologia y licencia declaradas, y se usa **para un solo dato** que la documentacion oficial no expone: la ruta `.kiro/specs/<feature>/`, atribuida a [R45] y no a [R44]. Las tres secundarias restantes quedan registradas en el documento **como evaluadas y no usadas**, con el motivo. En `aws.amazon.com` no hay guia tecnica: lo que existe es un curso en AWS Skill Builder y contenido en `builder.aws.com`, material didactico que tampoco mide.

### Que cambio
- `REFERENCIAS.md`: alta de **[R44]** (Kiro oficial, con la clase de evidencia y la prohibicion de usarlo como efectividad) y **[R45]** (SDD Observatory, con su uso acotado a un dato).
- `SPECS_REGISTRY.md`: spec de `software/analisis/ANALISIS-KIRO.md`, con cinco casillas de validacion, entre ellas que la procedencia declare que las fechas cierran una direccion y no abren la contraria.
- `software/analisis/ANALISIS-KIRO.md`: alta.

### Validacion
`tools/check_docs.py` en verde (0 ERROR). Las cuatro citas textuales se verificaron en la pagina que las contiene el 2026-09-05.

### Deuda abierta
- **La propagacion queda sin ejecutar**, y es lo que sigue: `CONVERGENCIA-IMPLEMENTACIONES-SDD.md` (reserva de procedencia reformulada, y cuarto caso en la dimension candidata a v2), `ANALISIS-OPENSPEC.md` (declara el mismo hueco de Kiro) y `ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md` (Kiro es adoptable, pero madurez y actividad **no** se pueden calcular con `git` como en los otros cuatro).
- **Tessl sigue sin filtro de procedencia**: la deuda se paga a medias.
- Ninguna afirmacion sobre Kiro es verificable en codigo, y eso no tiene remedio mientras el producto sea cerrado.
- Sigue abierto: M-40, M-41, M-42, el ecosistema del 1.0 de Spec Kit sin caracterizar, e instrumento v2 sin decidir.

---

## Alta de ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD: para que sirve cada herramienta, con doce dimensiones y sin una sola medicion (2026-09-05) — COMPLETADA

**Accion**: documento nuevo, con spec registrada antes de escribirlo y fila propia en la Tabla SSOT. Responde la pregunta que quedo diferida el 2026-09-05 al reestructurar `software/RELACION-SPEC-VS-EPICA.md`: la comparacion entre frameworks, ahora en clave de uso y no de convergencia.

### Por que documento nuevo y no una fila mas en convergencia
`software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md` debe su credibilidad a que su instrumento v1 es **anterior** a tres de los cuatro casos: «con libertad para elegir que comparar, la convergencia se fabrica». Las dimensiones que esta pregunta necesita solo pueden formularse despues de leer los cuatro, asi que alojarlas ahi destruiria justo esa propiedad, y su regla 2 lo prohibe. La regla 1 ya decia adonde va un caso con interes por «madurez, adopcion, ergonomia»: a otro lado.

### La poblacion se invierte
Convergencia pregunta de donde vino el metodo; acá, si lo podes instalar. Sale el **testigo** (no es adoptable por terceros) y entra **sdd-first** (es un kit instalable, aunque no sume linaje). Es el mismo caso mirado con dos criterios distintos, y las dos lecturas conviven sin contradecirse.

### El limite, escrito donde se lee
**Ninguna de las cuatro fuentes reporta medicion alguna** sobre su idoneidad. El documento lo declara en el encabezado y despues marca **cada** afirmacion como `[declarado]` —lo que la fuente dice de si misma— o `[derivado]` —consecuencia estructural de un mecanismo leible en el clon—. Sin esa marca el documento seria un recomendador sin evidencia, que es lo que convergencia prohibe en su seccion «Que se puede y que no se puede inferir».

Y una honestidad que el instrumento de convergencia no necesita: **estas doce dimensiones NO son anteriores a la lectura de los casos**. La mitigacion declarada es su procedencia —salen de la pregunta de quien va a decidir, formulada antes de diseñar el instrumento—, y el documento dice que quien no la acepte lea la tabla como descriptiva y no como criterio de seleccion.

### Lo que devolvieron los datos duros
D9 a D11 salen de `git` sobre los clones, no de la documentacion de cada fuente. El contraste mas fuerte no estaba en los mecanismos sino acá:

| | Spec Kit | OpenSpec | Superpowers | sdd-first |
|---|---|---|---|---|
| Primer commit | 2025-08-21 | 2025-08-05 | 2025-10-09 | **2026-08-01** |
| Releases | 188 | 48 | 34 | **0** |
| Autores 90d | 97 | 54 | 17 | **1** |
| Licencia | MIT | MIT | MIT | Apache 2.0 |

**sdd-first tiene factor de bus 1, un mes de vida y cero releases**, y eso queda escrito en la tabla y en su ficha sin suavizar, pese a ser del mismo autor que este repositorio. Su ficha ademas se limita a hechos del clon, sin ninguna valoracion comparativa, porque cualquier juicio favorable emitido acá seria autocorrelacion.

Dato util del otro extremo: el catalogo de extensiones de Spec Kit tiene **165 de comunidad contra 4 oficiales**, y 34 presets contra 2. Su personalizacion real pasa por codigo de terceros, y por eso su modo de falla caracteristico se desplazo del metodo a la cadena de suministro — lo que explica que la propia fuente incorporara un modelo de confianza declarado para los catalogos.

### Que cambio
- `SPECS_REGISTRY.md`: spec nueva con doce dimensiones en `incluye`, la comparacion de convergencia y la decision de adopcion en `excluye`, y seis casillas de `validacion` —entre ellas que cada dato de madurez salga del clon con el comando que lo produce, y que la reserva de [R39] quede escrita—. Mas fila en la Tabla SSOT.
- `software/ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md`: alta. Poblacion y su inversion, las doce dimensiones con su procedencia y su limite, tabla resumen, ficha por caso, orientacion por escenario, y una seccion final que enumera lo que el documento **no puede** decir.

### Validacion
`tools/check_docs.py` en verde (0 ERROR), y bloqueando correctamente mientras la spec existia sin el archivo. Los conteos se reprodujeron con `git rev-list`, `git log` y lectura de los catalogos JSON.

### Deuda abierta
- **La seccion 5 (orientacion por escenario) es la mas facil de leer como recomendacion y la que menos evidencia tiene.** Declara dos veces que no ordena por calidad; si aparece un uso indebido, el remedio es podarla, no matizarla mas.
- Ninguna fuente se corrio: D6, D7 y D8 son lectura de mecanismo, no experiencia de uso.
- El ecosistema del 1.0 de Spec Kit sigue **sin caracterizar** en su analisis; acá entra solo por su efecto practico.
- Sigue abierto: M-40 sin decidir, M-41 sin escribir, M-42 en Propuesta, y la decision sobre instrumento v2 de convergencia, cuya candidata mas fuerte —«la ceremonia escala con el tamaño del trabajo»— quedo registrada ayer.

---

## Convergencia se re-corre contra las cuatro versiones nuevas; sdd-first entra a la columna del linaje (2026-09-05) — COMPLETADA

**Accion**: propagacion al SSOT de convergencia de los cuatro diffs dirigidos de esta sesion, que se habia salteado. Mas la revision de que artefacto representa a nuestro linaje, a pedido del usuario.

### La omision
Los cuatro diffs se entregaron sin propagar a `software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, que es SSOT y que lee justo lo que esos diffs tocaron. Es la regla de propagacion del Principio III y no se aplico; lo detecto el usuario, no el proceso. Vale registrarlo asi: el bloque `[SDD-Check]` de cada uno de los cuatro declaro «Derivados a revisar» mirando hacia abajo, y ninguno miro hacia el SSOT que los agrega.

### Que artefacto representa a nuestro linaje
El usuario planteo que sdd-first es la consecuencia de esta investigacion y que el testigo quizas ya no deba representar al linaje. Dos hechos verificados lo respaldan: el testigo esta **dormido desde el 2026-08-02** (`04d921d`, 71 commits, 18 specs) y el primer commit de sdd-first es del **2026-08-01** — el trabajo migro. Y sdd-first es el unico artefacto del linaje con el metodo ejecutado por codigo de punta a punta, ademas de publico y vendorizado.

Entra a la columna, con tres reglas que impiden que su entrada fabrique convergencia: no cambia el conteo de cuatro linajes; **cada celda declara de que artefacto del linaje sale**, para que nadie elija por fila el que mas se parece a los otros casos; y lo que sdd-first declara adoptado de otro caso del corpus MUST NOT sostener un veredicto. Esto ultimo esta verificado en fuente: sus playbooks dicen «Adaptado de `/speckit.analyze`» y «Adaptado de `/speckit.clarify`». El testigo **no se retira**: es el artefacto que se leyo cuando el instrumento se fijo.

### Que devolvio la re-lectura
**El instrumento sigue en v1** y no se le agrego ni redefinio ninguna fila, pese a que dos dimensiones nuevas quedaron registradas fuera de la tabla. Ningun veredicto se dio vuelta. Cambio otra cosa:

- **La fila 3 dejo de ser cuatro respuestas y paso a ser dos contra dos.** Superpowers v6.3.0 adopto «decidir y registrar», que es la posicion de OpenSpec. Y el dato incomodo que el documento no tenia: de los dos que quedan del lado «marcar y preguntar», **uno adopto la practica del otro**, asi que esa posicion la sostiene **un** linaje independiente y la contraria **dos**. Sobre este eje la posicion de este repositorio es la minoritaria, y su unica compañia es la fuente de la que la copio.
- **Se falsifico un invariante.** El documento afirmaba que lo que sobrevivia a cuatro registros incompatibles era que «las specs son archivos versionados que viven junto al artefacto que gobiernan». Los *stores* de OpenSpec sacan el registro a un repositorio propio: queda reducido a «las specs son archivos versionados». Corregido donde estaba escrito, con la leccion de metodo al lado.
- **El tercer eje deja de ser una particion.** `docs/PATRONES.md` de sdd-first corre aprendizaje sobre el **metodo**, que era la casilla de Superpowers, asi que nuestro linaje ocupa las dos.
- **Dos dimensiones nuevas registradas sin veredicto**: «donde vive el metodo respecto del artefacto» (un caso, en beta) y **«la ceremonia escala con el tamaño del trabajo»**, que hoy es la **candidata mas fuerte a instrumento v2** — tres de cuatro casos la ejercen con mecanismos distintos, contra uno solo de la candidata anterior.

### Validacion
`tools/check_docs.py` en verde (0 ERROR). Fechas de actividad del testigo y citas de procedencia de sdd-first verificadas en sus repositorios, no en documentos previos.

### Deuda abierta
- **«La ceremonia escala» sin decidir**: abrir instrumento v2 obliga a re-correr los cuatro casos (regla 3) y es trabajo aparte.
- **El testigo dormido**: su celda describe una posicion congelada y MUST releerse si vuelve a moverse.
- **La orientacion practica de cada framework sigue sin documento**: es el trabajo que sigue, con poblacion distinta a la de convergencia (entra sdd-first por adoptable, sale el testigo por no serlo) y con madurez, actividad, licencia y soporte como dimensiones, a pedido del usuario.
- Sigue abierto: M-40 sin decidir, M-41 sin escribir, M-42 en Propuesta, el ecosistema del 1.0 de Spec Kit sin caracterizar.

---

## RELACION-SPEC-VS-EPICA se funda primero en norma y despues en implementaciónes; la spec se enmienda para permitirlo (2026-09-05) — COMPLETADA

**Accion**: reestructuracion del documento y enmienda de su spec, a pedido del usuario, con cuatro criterios que el pedido fijo: fidelidad al estado de hoy sin perder la historia; el concepto general primero y las implementaciónes despues; libertad para cambiar estructura o alcance si mejora la calidad; y la comparacion entre frameworks explicitamente diferida a otro analisis.

### El problema
El documento era general en el titulo, en la tesis y en el veredicto de cierre, y su base empirica era **una sola implementacion** mas tres comentarios sobre esa misma implementacion ([R20], [R21], [R22]). Escrito el 2026-06-03, cuando eso era todo lo que el corpus tenia. Los otros tres casos se analizaron el 2026-08-02 y el 2026-08-15 y nunca entraron.

Peor que estrecho: el lado **agil** estaba tan poco fundado como el lado SDD. La definicion de epica se atribuia a [R21], una consultora, no a una fuente de vocabulario.

### Lo que devolvio ir a las fuentes
La asimetria es mas fuerte de lo que el documento suponia, y es verificable:

- `ISO/IEC/IEEE 29148:2018` declara en su alcance que «defines the construct of a good requirement» [R03]: la especificacion de requisitos tiene definicion normativa.
- La **Scrum Guide (2020) no contiene las palabras «epic» ni «user story»**, en ninguna forma [R41]. Verificado en fuente. Su unidad es el *Product Backlog item*, ni siquiera definido formalmente.
- La unica definicion disponible de epica es de glosario profesional, con origen datado en Cohn 2004 [R42], y su significado derivo: «In a case of Semantic Diffusion, the original definition of "epic" has weakened over the years», con dos usos hoy incompatibles y la herramienta moldeando la practica [R43].
- Y el remate: las tres C de Jeffries (2001) nacieron «to distinguish "social" user stories from "documentary" requirements practices such as use cases» [R42]. **La historia de usuario se diseño para no ser una especificacion.** La pregunta original compara un artefacto cuya razon de ser es documentar con uno cuya razon de ser es reemplazar la documentacion por conversacion.

Sobre esa base, las cuatro implementaciónes entran como **evidencia** y muestran tres respuestas distintas al eje de alcance: contencion (Spec Kit; sdd-first, que no cuenta), separacion estructural en dos directorios (OpenSpec), y ausencia de contenedor (Superpowers, verificado con `grep`: cero ocurrencias de historia o epica en su spec). Y el unico caso independiente que contiene documenta tambien la jerarquia inversa cuando la feature no entra en un ciclo.

**Una afirmacion retirada**: «la posicion dominante es la de contencion/inversion de jerarquia». Sobre cuatro casos —uno de los cuales no cuenta por procedencia— no se sostiene.

### Que cambio
- `SPECS_REGISTRY.md` (**enmienda de spec, antes de escribir el documento**): `proposito` pasa a exigir el encuadre general primero; `incluye` suma el estatuto de los artefactos, el eje de alcance en las cuatro implementaciónes y la seccion datada de cambios; `excluye` incorpora **la comparacion entre frameworks**, diferida por decision del usuario; `validacion` suma cinco casillas, entre ellas que ninguna implementacion del mismo autor cuente como evidencia y que toda afirmacion retirada quede registrada.
- `REFERENCIAS.md`: alta de **[R41]** (Scrum Guide, citada por ausencia), **[R42]** (glosario de Agile Alliance: epica y tres C) y **[R43]** (Thoughtworks sobre la difusion semantica). Correccion de **[R03]**, que apuntaba a la edicion **2011** y ahora apunta a la **2018** vigente, con su alcance textual.
- `software/RELACION-SPEC-VS-EPICA.md`: reescrito en ocho secciones. La 1 es nueva y es el encuadre normativo; la 4 son las implementaciónes como evidencia, con su encabezado declarando que no es comparacion; la 8 registra que se retiro y que se conservo, para que la revision sea auditable. Los dos bloques `[SDD-Check]` previos se conservan bajo un encabezado que aclara que son registro datado.
- `software/analisis/ANALISIS-SPEC-KIT.md`: la deuda «RELACION-SPEC-VS-EPICA sin actualizar», abierta esta misma sesion, queda **saldada** en los tres lugares donde estaba escrita.

### Validacion
`tools/check_docs.py` en verde (0 ERROR). Cada afirmacion externa nueva se verifico en fuente el 2026-09-05, salvo las dos que se declaran sin verificar donde se citan.

### Deuda abierta
- **La fuente primaria de Jeffries no se pudo alcanzar** (conexion rechazada); la atribucion de las tres C descansa en [R42] y eso esta escrito donde se cita. Lo mismo con la definicion de Cohn 2004, citada por atribucion, y con el texto completo de [R03], que es de pago.
- **La comparacion entre frameworks queda diferida** por decision del usuario: sigue sin documento y sin item.
- Sigue abierto: M-40 sin decidir, M-41 sin escribir, M-42 en Propuesta, el ecosistema del 1.0 de Spec Kit sin caracterizar, el hueco de `PATRONES.md` del lado del canal de error, y cuanto cuesta frenar sin medir.

---

## Diff dirigido de OpenSpec [R38]: el repositorio de specs se separa del artefacto, y el punto ciego de M-41 reaparece (2026-09-05) — COMPLETADA

**Accion**: fase B del re-anclaje, ultima de cuatro. Diff dirigido de OpenSpec entre `45cca5d` (v1.7.0, 2026-07-30) y `e062b95` (v1.12.0, 2026-09-03) contra `software/analisis/ANALISIS-OPENSPEC.md`. Con esto quedan cerradas las cuatro re-consultas.

### Que se encontro
Lo analizado no se movio, y en un punto se verifico contra una sospecha propia: `git ls-tree` en los dos commits devuelve la misma anatomia `openspec/`, asi que la lectura preliminar del relevamiento —que tomaba `initiatives/`, `explorations/` y `work/` por estructura nueva— era falsa y quedo descartada antes de escribirse. Las 12 skills siguen siendo 12 y el argumento de procedencia por fecha no depende de nada que haya cambiado. C1-C5 intactas.

**C6 — la primera implementacion del corpus que separa el repositorio de specs del repositorio del artefacto.** `docs-lab/multi-repo/stores.md` documenta los *stores* (beta): la carpeta `openspec/` se muda a un repositorio propio que varios repositorios de codigo comparten, se sincroniza por git como cualquier repositorio, y las specs reciben ramas y pull requests igual que el codigo. Los otros tres casos y este repositorio alojan el metodo adentro del artefacto que gobierna.

Toca un problema que acá esta declarado y sin resolver, en tres formas distintas: la pieza 3 de A-04 fuera de este repositorio (deuda desde el 2026-08-23), la propagacion asistida de sdd-first a traves de una frontera de repositorios, y [R40] como fork del backstop viviendo afuera. Queda como **lectura** y no candidata, con dos advertencias escritas en la conclusion: la direccion es la contraria —un store centraliza specs de varios repos de codigo, acá el caso es un repositorio de metodo cuyas piezas corren afuera— y la capacidad es beta y autodeclarada.

**C7 — la fuente reescribe su documentacion a mano y prohibe arrastrar texto.** `docs-lab/` es un arbol nuevo desde el que ya construye el sitio, con la regla escrita: «written by hand, from scratch. The old `docs/` tree is source material for facts, never text to carry over», y una skill propia para escribirlo. Es una postura explicita de un proyecto spec-driven sobre su propia prosa, y es la contraria a la regeneracion — el eje de B-07. **No se desarrolla**: la transferencia a Linea A no esta en el `incluye` de ese documento.

**Una nota menor con cuatro decisiones aprovechables.** En v1.11.0 la fuente corrigio que `validate` aprobaba un `## Purpose` que seguia siendo su propio placeholder, porque el placeholder supera el piso de brevedad. Misma clase que M-31 acá, y su solucion trae cuatro decisiones de diseño transferibles sin una linea de codigo: deteccion angosta a proposito, WARN y no ERROR, el texto entre backticks no cuenta, y un caso produce un mensaje y no dos. Anotadas en M-31.

**Y una recurrencia.** `docs-lab/` no figura en el CHANGELOG —es infraestructura de documentacion, no entrada de release—, asi que un diff que leyera solo el changelog no lo habria visto, igual que el del 2026-07-10 no vio `spec-persistence.md`. **Segunda instancia del modo de falla de M-41 en la misma sesion y en otra fuente**, esta vez evitada porque el procedimiento borrador empieza por el arbol completo. M-41 deja de describir un descuido puntual.

### Que cambio
- `software/analisis/ANALISIS-OPENSPEC.md`: §Actualizacion 2026-09-05 con **C6**, **C7**, la nota de M-31, la recurrencia de M-41 y bloque `[SDD-Check]` propio con `Cobertura` declarada **incompleta**.
- `agenda/MEJORAS-METODO.md`: M-31 recibe las cuatro decisiones de diseño ajenas.
- `REFERENCIAS.md`: [R38] pasa de «diff pendiente» a re-consulta cerrada.

### Validacion
`tools/check_docs.py` en verde (0 ERROR). La invariancia de la anatomia se verifico con `git ls-tree`, no por lectura; las dos citas de politica son textuales.

### Deuda abierta
- **Dos preguntas de investigacion señaladas y NO dadas de alta**: si la frontera entre el repositorio de specs y el del artefacto es una decision de diseño con consecuencias medibles o una comodidad de alojamiento (C6), y la postura de reescribir en vez de regenerar documentacion propia (C7, eje de B-07). Plantearlas bien es trabajo propio y darlas de alta a medias es peor que no darlas.
- **La transferencia a Linea A que C7 habilita queda sin desarrollar**, por alcance de la spec de ese documento.
- Cierra la fase B, y con ella el arrastre «faltan N re-consultas». Sigue abierto todo lo demas: M-40 sin decidir, M-41 sin escribir, M-42 en Propuesta, `software/RELACION-SPEC-VS-EPICA.md` sin actualizar, el ecosistema del 1.0 de Spec Kit sin caracterizar, el hueco de `PATRONES.md` del lado del canal de error, y cuanto cuesta frenar sin medir.

---

## Diff dirigido de Superpowers [R37]: la ceremonia escala, la compuerta no, y la precedencia se usa para no frenar (2026-09-05) — COMPLETADA

**Accion**: fase B del re-anclaje, tercera de cuatro. Diff dirigido de Superpowers entre `44c9b2d` (v6.2.0, 2026-08-02) y `b36e082` (v6.3.0, 2026-08-12) contra `software/analisis/ANALISIS-SUPERPOWERS.md`. Primer diff que aplica el borrador de procedimiento de M-41: `git diff --stat` sobre el arbol completo antes de mirar ningun archivo esperado.

### Que se encontro
Un unico commit de release, 40 archivos, +2888 lineas. Las 14 skills siguen siendo 14 y la tesis central —no hay Power Inversion— no se mueve. El peso esta en dos skills, y cada una devuelve algo que este repositorio no tiene.

**C6 — la ceremonia escala con la tarea; la compuerta de aprobacion no.** `brainstorming` clasifica el pedido en spike / bounded / architectural, y solo el ultimo escribe spec y plan. Las cuatro guardas que rodean la clasificacion son lo portable: se anuncia en voz alta **antes** de la primera pregunta para que el humano la anule; el trinquete es de una sola via (ante la duda, el camino mas pesado; la complejidad descubierta sube, nada baja); los tres caminos terminan igual en aprobacion humana explicita; y el atajo tiene nombre de anti-patron —«reaching for a label to skip work IS the doubt»—.

Acá `SPECS_REGISTRY.md` §Profundidad de spec declara tres niveles y M-37 midio que el mas alto no lo usa ninguna de las 46 entradas: la escala existe declarada y no opera. Superpowers muestra las tres piezas que le faltan —quien elige, cuando lo anuncia, que impide elegir hacia abajo— pero clasifica **trabajo** y nuestra tabla clasifica **documentos**. Queda como lectura para M-37, no como candidata, y la distincion esta escrita en la conclusion para que nadie porte la forma sin el mecanismo.

**C7 — la precedencia se usa para no frenar, en direccion contraria a nuestro Principio VII.** «Rulings, not stalls. A running plan does not wait on a human.» Un conflicto se resuelve contra la spec —«the spec is the binding authority, the plan is its argument»—, se registra como `Ruling: <que se decidio> — <por que> — <cuanto cuesta si esta mal>` y el trabajo sigue; solo lo destructivo frena. La fuente declara el costo que lo motivo: una sesion bloqueada casi nueve horas por una pregunta que el controlador podia haber decidido. Autoreportado, un caso, sin medicion agregada — no se usa como efectividad.

Acá el Principio VII manda lo contrario, y **no se propone cambiarlo**: es constitucional, y los dos diseños responden a riesgos distintos. Lo portable sin tocar nada es la forma de tres campos: nuestro `[NEEDS CLARIFICATION]` registra la pregunta y no lo que el texto ya esta asumiendo mientras el marcador sigue abierto, ni lo que se rehace si la asuncion es la otra. Alta de **M-42**.

Refuerzo de C1 sin cambiarla: los planes llevan un puntero `Spec:` y la skill lee la spec al armar el trabajo, asi que la fuente es **mas** spec-anchored que en v6.2.0 y sigue sin regenerar nada.

### Que cambio
- `software/analisis/ANALISIS-SUPERPOWERS.md`: §Actualizacion 2026-09-05 con **C6** y **C7**, la nota de refuerzo a C1/C4, y bloque `[SDD-Check]` propio.
- `agenda/MEJORAS-METODO.md`: alta de **M-42**, con lo que propone y —escrito aparte— lo que NO propone. Verificado que el patron `CLARIFICACION` del backstop captura todo el interior del corchete, asi que los dos campos nuevos no cuestan una linea de codigo.
- `REFERENCIAS.md`: [R37] pasa de «diff pendiente» a re-consulta cerrada.

### Validacion
`tools/check_docs.py` en verde (0 ERROR). Todas las citas de la fuente son textuales y declaran su archivo; el caso de las nueve horas lleva su reserva al lado.

### Deuda abierta
- **Cuanto cuesta frenar no esta medido acá.** Sin ese dato, C7 describe dos diseños y no puede compararlos. Es el hueco mas concreto que deja esta entrada.
- Sigue abierto: M-40 sin decidir, M-41 sin escribir, M-42 en Propuesta, `software/RELACION-SPEC-VS-EPICA.md` sin actualizar, el ecosistema del 1.0 de Spec Kit sin caracterizar, y el hueco de `PATRONES.md` del lado del canal de error.
- Falta la ultima fase B: OpenSpec.

---

## Diff dirigido de Spec Kit [R10]: la tesis no se movio, y el material que la califica llevaba dos meses invisible (2026-09-05) — COMPLETADA

**Accion**: fase B del re-anclaje, segunda de cuatro. Diff dirigido de Spec Kit entre `983a87f` (v0.12.11.dev0, 2026-07-10) y `4a7341a` (v1.0.5.dev0, 2026-09-04) contra `software/analisis/ANALISIS-SPEC-KIT.md`, que es SSOT. 560 commits, con el 1.0.0 liberado el 2026-08-21.

### Que se encontro
**Nada de lo analizado se movio, y esta vez se verifico en vez de afirmarse**: `git diff 983a87f..HEAD -- spec-driven.md` sale vacio. La Power Inversion y los nueve articulos son el mismo texto. Los diez comandos siguen ahi. C1-C5 intactas.

Lo que cambio esta en `docs/concepts/`, un directorio de cuatro documentos que el diff anterior no miro. Tres son conceptuales y nuevos para nosotros, y uno de ellos —`spec-persistence.md`— **estaba en el arbol desde el 2026-06-09, un mes antes del corte anterior**. El `[SDD-Check]` de aquella entrega declara por que no lo vio: «diff basado en CHANGELOG + spec-driven.md». Un documento agregado sin linea de changelog es invisible a ese procedimiento.

Lo que estuvo perdido dos meses no era decorativo:

1. **La fuente adopta nuestro instrumento.** `spec-persistence.md` cita el articulo de Fowler que usamos como [R30] y reproduce sus tres niveles. Compartimos taxonomia, no solo practica.
2. **Y declara que no fuerza ninguno**: «None is the default, and none is required by Spec Kit». Eso califica a C3, que lee la Power Inversion como una posicion mas fuerte que la nuestra. La lectura sigue siendo correcta para el manifiesto —que no cambio— pero ahora hay una **tension adentro de la fuente**: filosofia que afirma la inversion, referencia que declara el modelo de persistencia como convencion de equipo. C3 no se retira; se le agrega que citar la posicion fuerte sin esa distincion sobre-atribuye. Nueva conclusion **C6**.
3. **Un eje que ya usabamos sin nombre.** La fuente separa la pregunta temporal de [R30] de una segunda, de mutacion: flow-back, flow-forward, living spec. `COMPARATIVA-SPECKIT-VS-TESTIGO.md` compara «carpeta por feature» contra «registro central» — que es ese eje exacto. Nueva conclusion **C7**, con la advertencia de que es convergencia de instrumento y MUST NOT contarse como linaje.

**Una correccion.** El relevamiento previo marco `--require-spec` como respaldo upstream de M-02. El diff lo desmiente: es una precondicion de fase para `analyze` («Require spec.md to exist»), no mira quien edita ni si la spec tiene contenido. No respalda M-02.

**Lo que no se caracterizo, dicho**: entre v0.12 y v1.0.4 la superficie que mas crecio es la plataforma —extensiones, presets, bundler, catalogos de comunidad con modelo de confianza—. Queda fuera por alcance de la spec, y con su efecto sobre `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` sin evaluar.

### Que cambio
- `software/analisis/ANALISIS-SPEC-KIT.md`: §Actualizacion 2026-09-05 con **C6** y **C7**, la correccion de `--require-spec`, lo que el 1.0 agrega y no se caracteriza, y la revision explicita de los dos derivados registrados. Bloque `[SDD-Check]` propio, con `Cobertura` declarada **incompleta**.
- `agenda/MEJORAS-METODO.md`: alta de **M-41** — el procedimiento de re-consulta de fuentes no esta escrito, y el que se improviso el 2026-07-10 tenia un punto ciego que costo dos meses. Trae tres pasos de borrador, ya ejecutados a mano en este diff.
- `REFERENCIAS.md`: [R10] pasa de «diff pendiente» a re-consulta cerrada, con lo que vale y lo que no.

### Revision de derivados (regla de propagacion)
Los dos registrados, revisados: `COMPARATIVA-SPECKIT-VS-TESTIGO.md` sin contradiccion (gana vocabulario de C7, edicion propia); `RELACION-FR-VS-SC-Y-COBERTURA.md` sin impacto.

Fuera del registro de derivados, un hallazgo que alcanza a otro documento: `docs/concepts/spec-of-specs.md` escribe **la epica por encima de la spec** —un roadmap descompone «the epic» en sub-specs—, que es la direccion contraria a la contencion que `software/RELACION-SPEC-VS-EPICA.md` reporta como posicion dominante. No se toco: tiene spec propia y no deriva de este.

### Validacion
`tools/check_docs.py` en verde (0 ERROR). La no-invalidacion se verifico con `git diff`, no por lectura; la cita de `spec-persistence.md` es textual; `--require-spec` se leyo en el script.

### Deuda abierta
- **`software/RELACION-SPEC-VS-EPICA.md` sin actualizar** por el material de `spec-of-specs.md`. Es el pendiente mas concreto que deja esta entrada.
- **El ecosistema del 1.0 sin caracterizar**, y su efecto sobre `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` sin evaluar.
- M-41 en Propuesta: mientras no se escriba, las dos re-consultas que faltan siguen improvisando el procedimiento.
- Sigue abierto lo de la entrada anterior: M-40 sin decidir, y el hueco de `PATRONES.md` del lado del canal de error.
- Faltan las dos fases B restantes: superpowers y OpenSpec.

---

## Diff dirigido de sdd-first [R39]: la taxonomia ajena absorbe defectos que no la formaron, y devuelve un agujero propio (2026-09-05) — COMPLETADA

**Accion**: fase B del re-anclaje, primera de cuatro. Diff dirigido de los 8 commits de sdd-first entre `f032dce` (2026-08-17) y `4a0851e` (2026-09-03) contra `software/analisis/ANALISIS-SDD-FIRST.md`. Ninguna conclusion previa (C1-C7) queda invalidada.

### Que se encontro
Los ocho commits son `fix:` contra specs propias, sin entrada de historial alla porque el kit reserva ese registro para cambios de metodo. Lo que los vuelve material no es lo que arreglan sino que **seis de los ocho son la misma cosa**: un verificador que reportaba OK sin verificar nada, o una guarda abierta por un camino que nadie probo. El check de constitucion no reconocia sus propios enforcements como rutas y salia exit 0; el doctor daba el gate por cableado con un comentario que decia lo contrario; el gate no leia `notebook_path` y permitia la edicion en silencio; la rama fail-closed del hook era fail-open en Windows.

**El hallazgo no es ese, es el de arriba.** `docs/PATRONES.md` se escribio el 2026-08-16 y no se toco desde entonces; los defectos son del 2026-08-26 en adelante. La taxonomia es anterior y absorbe seis de los ocho sin necesitar una clase nueva. Es la primera vez que una pieza de metodo de este corpus se enfrenta a casos que no la formaron.

Lo que eso vale esta escrito con el mismo cuidado en C8: **no es un test predictivo** —nadie predijo nada, la clasificacion es post-hoc, de un solo clasificador con incentivo a que encaje, n=8, sin criterio escrito de antemano— pero **si es fuera de muestra**, y hasta acá `PATRONES.md` era una buena idea sin ninguna muestra.

Y el hueco importa tanto como la cobertura: los dos que no encajan estan del lado del canal de error (un `[FALLO]` que colapsa «archivo ilegible» con «violacion real»). Las ocho clases estan enunciadas del lado del verde. **Ninguna cubre un rojo que no significa nada**, y C7 propone portar esa taxonomia acá: quien la porte MUST NOT hacerlo como si estuviera completa.

### Una instancia propia, verificada
La clase mas instanciada del delta (3 de 6) es «la lista duplicada que nada ata», y describe algo que este repositorio tiene. `METODO_FILES` de `tools/check_docs.py` enumera a mano que archivo es metodo, derivandolo **literalmente** de la enumeracion del Principio VI. La lista es fiel; la fuente esta incompleta: `CONVENCIONES.md` no figura, y es el SSOT del lexico normativo, la forma de los documentos, los nombres y el formato de commit.

**Sonda**: se agrego una linea a `CONVENCIONES.md`, se la dejo staged y se corrio `./tools/check_docs.py --staged` —el modo que invoca el gate—. Resultado **0 ERROR**, sin pedir entrada de historial. Un commit que redefine que significa MUST en este repositorio pasa sin dejar rastro. Revertido sin commitear.

Es distinto de M-31: alla el check miraba mal, acá mira exactamente lo que le dijeron. Por eso el arreglo no empieza en el check.

### Que cambio
- `software/analisis/ANALISIS-SDD-FIRST.md`: §Los ocho arreglos que siguieron (tabla de los seis, con hash y el caso concreto que salia verde en cada uno) y **C8** nueva; encabezado con el tercer anclaje; bloque `[SDD-Check]` actualizado en cinco campos.
- `agenda/MEJORAS-METODO.md`: alta de **M-40** (prioridad alta), con la sonda, la distincion respecto de M-31 y el orden de trabajo — decidir si `CONVENCIONES.md` es metodo, barrer el resto de la enumeracion antes de enmendar, y recien despues tocar `METODO_FILES`.
- `REFERENCIAS.md`: [R39] gana el tercer anclaje y su reserva de vendorizado pasa a nombrar los tres commits con lo que cada uno sostiene.

### Validacion
`tools/check_docs.py` en verde (0 ERROR). Cada arreglo citado declara su hash; ninguna cifra de efectividad se toma de la fuente, que no reporta ninguna.

### Deuda abierta
- **M-40 sin decidir**, y mientras tanto la unica garantia mecanica del Principio VI tiene un agujero del tamaño del SSOT del lexico. La decision es del usuario: es enmienda de constitucion, no ajuste de check.
- **El hueco de `PATRONES.md` del lado del canal de error** queda declarado y sin resolver; lo hereda quien porte la taxonomia (C7).
- Faltan las tres fases B restantes: spec-kit, superpowers, OpenSpec.

---

## Los cuatro clones vendored se re-anclan al estado del disco (2026-09-05) — COMPLETADA

**Accion**: `git pull` deliberado de los cuatro clones de `fuentes-externas/` y re-anclaje de `REFERENCIAS.md` al estado real del disco. **No** es re-analisis: ningun documento de `software/` se toco.

### Por que
Las cuatro entradas afirmaban un commit de clon que ya no estaba en disco. `[R10]` era el caso mas visible: declaraba el clon en v0.12.11.dev0 `983a87f` cuando estaba en `4a7341a`. Una afirmacion falsa sobre el estado del vendorizado no invalida los analisis —que estan anclados a su snapshot conceptual— pero rompe la reproducibilidad de toda cita que alguien quiera verificar volviendo al clon.

### Que se movio, de donde a donde

| Fuente | Anclaje anterior | Estado hoy | Tramo |
|---|---|---|---|
| [R10] spec-kit | v0.12.11.dev0 `983a87f` (2026-07-10) | v1.0.5.dev0 `4a7341a` (2026-09-04) | 560 commits; cruzo su 1.0.0 el 2026-08-21 |
| [R37] superpowers | v6.2.0 `44c9b2d` (2026-08-02) | v6.3.0 `b36e082` (2026-08-12) | 1 commit de release |
| [R38] OpenSpec | v1.7.0 `45cca5d` (2026-07-30) | v1.12.0 `e062b95` (2026-09-03) | 103 commits, 5 versiones menores |
| [R39] sdd-first | `f032dce` (2026-08-17) | `4a0851e` (2026-09-03) | 8 commits, todos `fix:` contra specs propias |

Los cuatro clones estan en `main` con arbol limpio.

### Que cambio en `REFERENCIAS.md`
- Cada una de las cuatro entradas gana una linea **Estado del clon vendored** separada de **Version analizada**, con el par origen → destino y su fecha. La separacion es el punto: el analisis vale para el snapshot, el disco esta en otro lado, y ahora las dos cosas se leen por separado en vez de confundirse en una sola frase.
- Cada linea nueva declara que el diff dirigido esta **pendiente**, para que el re-anclaje no se lea como re-analisis.
- `[R10]`: corregido un pendiente que ya no lo era — la linea decia «pendiente incorporar `/speckit.converge` y articulos IV-VI *project-defined*» y ambos estan incorporados a `software/analisis/ANALISIS-SPEC-KIT.md` desde el 2026-07-10.
- `[R37]`: los harnesses pasaron de 11 a 14 (Devin CLI, Hermes Agent, Grok Build CLI); las 14 skills no cambiaron.
- `[R38]`: `docs/supported-tools.md` paso de mas de 30 a 62 filas; la anatomia de `openspec/` y las 12 skills no cambiaron. Se verifico con `git ls-tree` contra `45cca5d` que `initiatives/`, `explorations/` y `work/` **ya existian** en el commit analizado: una lectura preliminar los tomo por estructura nueva y quedo descartada antes de escribirse.
- `[R39]`: la reserva de vendorizado decia «anclarse al commit declarado arriba» y arriba ahora hay dos; pasa a nombrar cual sirve para que (`ebfbd67` la version analizada, `f032dce` el delta del 2026-08-30) y a prohibir explicitamente citar contra el estado del clon.

### Validacion
`tools/check_docs.py` en verde (0 ERROR). Cada commit, version y conteo se leyo del clon en disco, no del documento previo.

### Deuda abierta
- **El diff dirigido de las cuatro fuentes queda sin correr** (fase B, un commit por fuente). Orden acordado: sdd-first, spec-kit, superpowers, OpenSpec.
- Los cuatro clones son directorios vivos y pueden volver a moverse sin aviso; la unica entrada que declaraba esa reserva era `[R39]` y sigue siendo la unica que la necesita por ser del mismo autor, pero el modo de falla es comun a los cuatro.

---

## Dos aplicaciones del metodo devuelven mecanismos ya ejercidos y dos resultados negativos (2026-08-30) — COMPLETADA

**Accion**: relevamiento de dos repositorios que aplican este metodo —el kit de [R39], re-consultado, y una aplicacion de campo documental dada de alta como [R40]— y volcado de lo transferible al backlog de metodo, al backlog de investigacion y a un analisis de caso nuevo.

### Que se encontro
Lo relevante no fue confirmacion sino tres cosas que este repositorio no tenia:

1. **Mecanismos propuestos aca que alla ya corrieron.** M-16 (recordatorio de propagacion) esta implementado en [R40] desde el 2026-08-25, con tres decisiones de diseño escritas y una tabla de validacion que discrimina dos diffs identicos con resultado opuesto. M-17 tiene una segunda implementacion, esta vez en un repositorio documental sin codigo de producto, que era la reserva que lo frenaba.
2. **Dos resultados negativos.** La variante «indice de entradas» que M-30 podria haber elegido ya se probo y fallo alla: llego a estar trece iteraciones atrasada y apuntando a un archivo borrado. Y el saldo de T-1 en [R39] invalida una estrategia de barrido que el item #15 del backlog de investigacion podria haber intentado.
3. **Un hueco propio, verificado.** Encuadrado por el check `normativos` de [R40], se probo que renombrar el titulo `## Tabla SSOT` del registro deja `ssot-table` y `ssot-collision` recorriendo cero filas, con el backstop saliendo **0 ERROR** y sin nombrar ninguno de los dos ids. El patron de guarda ya estaba aplicado dos veces en `tools/check_docs.py` y no estaba declarado en ningun lado.

Una lectura preliminar erronea quedo corregida y escrita: el campo `Verificador:` que declara que mitad del invariante ve el check no es un refinamiento ajeno a importar — ya es practica de `CONSTITUTION.md` y el caso la heredo.

### Que cambio
- `REFERENCIAS.md`: alta de [R40] como **fuente reservada** con su restriccion de uso escrita; [R39] gana el anclaje del segundo commit para el delta del 2026-08-16/17.
- `agenda/MEJORAS-METODO.md`: alta de M-31 a M-34; M-16, M-17 y M-30 anotados con la evidencia de campo y con lo que de cada uno queda abierto.
- `agenda/BACKLOG-INVESTIGACION.md`: alta de los items 17, 18 y 19; correccion del inventario de corpus de Linea A del item #15, que declaraba un solo corpus cuando hay dos.
- `software/analisis/ANALISIS-SDD-FIRST.md`: §Lo que el kit destilo despues y conclusion C7, ambas ancladas al segundo commit.
- `SPECS_REGISTRY.md` + `docs-y-investigacion/ANALISIS-CASO-CAMPO-1.md` + `docs-y-investigacion/00-INDEX.md`: alta del analisis del caso, con spec que incorpora cuatro checks de validacion sin precedente en el registro — los que sostienen la anonimizacion.

### Como se valido
`./tools/check_docs.py` en 0 ERROR y 1 WARN (M-08, preexistente) despues de cada pieza, y el gate al commit en cada uno. El hueco del punto 3 se verifico ejecutando el backstop sobre el registro con el titulo renombrado y restaurandolo.

La anonimizacion se verifico por barrido: el extracto saneado sale con cero ocurrencias de nombre comercial, de nombres de documento del caso y de nombres de area, sobre siete archivos. El analisis va mas lejos que el extracto y no usa ni siquiera los nombres saneados: nombra por rol.

### Por que esto es entrada de metodo y no hallazgo de investigacion
Mueve el backlog de metodo, el registro de specs y el catalogo de referencias. Las preguntas que el relevamiento abrio **no** se contestaron aca: quedaron como items 17, 18 y 19 del backlog de investigacion, que se cierran con evidencia y no con una edicion.

### Deuda abierta
- **La viabilidad contractual de difundir aprendizajes derivados de [R40], aun anonimizados, no esta verificada.** Es previa a cualquier uso fuera de este repositorio y no la resuelve ningun check.
- **El extracto saneado no entra a git** (`fuentes-externas/` esta ignorado), asi que la verificabilidad de las citas del analisis depende de una copia local. Es el mismo regimen que los otros clones vendorizados, y la misma limitacion.
- **M-31 a M-34 quedan en `Propuesta`**, sin aprobacion. El hueco verificado de M-31 sigue abierto en el codigo.
- **La mitad ascendente de M-16** —cruzar los derivados nombrados contra el campo `Derivados a revisar`— no tiene implementacion en ningun repositorio.
- Sin novedad: M-02 `Aprobada` sin ejecutar; M-30 `Propuesta`; M-24(2) sin aprobar; M-26 y M-08 sin decidir; la sonda de Fase 0 sobre el snapshot sigue sin correr y la pieza 3 de M-22/M-25 sigue fuera de este repositorio.

## El entorno se sella por snapshot del ejecutable, no por ajuste de actualizacion (2026-08-23) — COMPLETADA

**Accion**: correccion dentro de la enmienda 4 del runbook de A-04 y de §Sello del template, antes de commitear la version anterior. El mecanismo del componente «entorno» pasa de desactivar la auto-actualizacion a **copiar el ejecutable a una ruta privada al abrir la tanda**.

### Que se encontro
La version anterior de esta entrega iba a apoyarse en la variable de entorno que suprime el actualizador del harness, verificada presente en el bundle instalado. **El usuario detuvo la escritura con la objecion correcta**: esa variable suprime el actualizador *de ese proceso*, no de la instalacion. El ejecutable es compartido, asi que cualquier otra sesion del harness abierta en la maquina corre su propio actualizador y mueve el binario que los reps van a lanzar. La tanda quedaba igual de expuesta y ademas con la falsa confianza de creerse protegida — un escalon 2 disfrazado de 1, que es exactamente lo que M-22 advierte cuando dice que un mecanismo de eliminacion es a su vez algo sellado.

Verificado que el arreglo es viable, no supuesto: se copio el ejecutable a una ruta privada y arranca reportando su version (2.1.241). Con eso el desvio pasa a ser imposible en vez de improbable, que es lo que separa el escalon 1 del 2, y sigue respetando la restriccion de origen —no se elige una version de antemano, se congela la que haya al correr—. Es la misma construccion que M-25 aplica al tratamiento: entregar desde un punto fijo en vez de apuntar a algo que se mueve.

### Que cambio
- `experimentos/a04-conducta-agente/PRUEBA-PISO-RUIDO-A4.md`: la fila del entorno sella el **snapshot** y no la version suelta; se explica por que el ajuste no alcanza; la supresion de auto-actualizacion se conserva pero baja de rango, solo para que el snapshot no se actualice a si mismo; el snapshot se hashea y su version se relee **de el** en cada rep; Fase 3 lanza el snapshot por ruta absoluta; y la nota de pieza faltante exige que el lanzador apunte al snapshot y no al `PATH`.
- `templates/EXPERIMENTO.md` §Sello: la regla general para herramienta de terceros gana el parrafo del escalon 1 por copia privada, con la advertencia de que un ajuste de proceso deja el componente en escalon 2 creyendose en 1.

### Como se valido
`./tools/check_docs.py` y `--staged` en 0 ERROR, 1 WARN (M-08). El mecanismo se probo a mano hasta donde alcanza: la copia arranca y reporta su version.

**Lo que no esta validado, escrito donde se lee**: que el harness se comporte igual desde el snapshot en una corrida completa de agente. Solo se probo el flag de version. Credenciales, rutas de configuracion y actualizador interno pueden depender de la ruta de instalacion. El runbook lo declara como sonda obligatoria de Fase 0 y fija el degradado: si falla, la fila vuelve a escalon 2 y se registra.

### Por que esto es entrada de metodo y no hallazgo de investigacion
Corrige el protocolo de un experimento y una plantilla de metodo. No mueve ningun dato.

### Deuda abierta
- **La sonda de Fase 0 sobre el snapshot esta sin correr**, y hasta entonces el escalon 1 del entorno es una construccion propuesta, no comprobada.
- **El equivalente en `agy` esta sin determinar.** Si ese harness no admite snapshot, su fila queda en escalon 2 y la asimetria entre harnesses MUST reportarse junto al resultado.
- **Pieza 3 sigue fuera de este repositorio**, y ahora con un requisito mas: el lanzador de `experimentosdd-a4/` MUST apuntar al snapshot. Mientras apunte al `PATH`, la fila del entorno describe un control que el aparato no ejecuta.
- Sin novedad: «Cinco sondas» vs seis filas, preexistente y no corregido; M-02 `Aprobada` sin ejecutar; M-30 `Propuesta`; M-24(2) sin aprobar; M-26 y M-08 sin decidir.

## El runbook de A-04 resuelve su sello por escalones (2026-08-23) — COMPLETADA

**Accion**: pieza 2 de M-22 y M-25. `experimentos/a04-conducta-agente/PRUEBA-PISO-RUIDO-A4.md` suma §Sello como **enmienda 4**, pre-dato respecto de la pasada 2 y sin alterar las pasadas 1 y 1b, cerradas. El template gana ademas la regla general que salio de ejercitarlo.

### Que se encontro
Ejercitar la seccion sobre un experimento real era el punto de la pieza 2, y produjo dos correcciones que la pieza 1 no podia dar sola.

**El entorno no admite sello anticipado.** La version de la CLI del harness puede cambiar varias veces en un mismo dia, asi que una version elegida al escribir el diseno llega desactualizada —o no instalable— al momento de correr. El sello del entorno tiene que tomarse **al abrir cada tanda**, con la version que efectivamente haya. Es una restriccion del usuario, no una deduccion del corpus, y refina lo que M-22 preveia: alli el escalon 1 para el entorno figuraba como «pinneo» entre los mecanismos disponibles, y resulta que para esta clase de herramienta no lo es.

**La primera version de la tabla se etiqueto mal a si misma.** Se anoto el entorno como escalon 1 intra-tanda cuando el mecanismo escrito —registrar al abrir y releer por rep— solo **detecta**, no impide. Corregido a escalon 2 intra-tanda mas 3 entre tandas. Llegar al escalon 1 exigiria suprimir la auto-actualizacion mientras la tanda corre, y este runbook no determina si el harness lo permite: queda como pregunta de Fase 0 de la pasada 2, con su resultado registrado pase lo que pase.

**El precedente decidio la forma.** La 1b se manejo como enmiendas al mismo runbook y no como documento nuevo, asi que la pieza 2 entra igual, con el regimen de enmiendas que el propio documento fija: fechada, motivada y clasificada pre/post dato.

### Que cambio
- `experimentos/a04-conducta-agente/PRUEBA-PISO-RUIDO-A4.md`: seccion §Sello nueva, antes de §Fases, con la tabla de cinco componentes —tratamiento, entorno, fixture y workspace, modelo, regimen de permisos—, cada uno con su escalon, su mecanismo y que pasa si diverge. El tratamiento queda sellado **por commit** y se entrega extrayendolo de el. Fase 2 declara que el sello de diseno no fija la version del harness y si el commit del tratamiento; Fase 3 suma el registro de version al abrir la tanda, la relectura por rep y la comprobacion de correspondencia del tratamiento.
- `templates/EXPERIMENTO.md`: §Sello suma la regla general para herramienta de terceros —sello del dia de la corrida, no del diseno—, con el escalon que eso deja y la advertencia de que el escalon 1 MAY no ser posible y MUST NOT suponerse.
- `SPECS_REGISTRY.md`: el `incluye` del runbook nombra el sello por escalones.
- `agenda/MEJORAS-METODO.md`: M-22 y M-25 con piezas 1 y 2 hechas.

### Como se valido
`./tools/check_docs.py` y `--staged` en 0 ERROR, 1 WARN (M-08). La seccion se lleno entera para un experimento real, que era la prueba que la pieza 1 no tenia: las cinco filas se pudieron responder, y las dos que no tienen verificador quedaron declaradas como tales en vez de vacias.

### Por que esto es entrada de metodo y no hallazgo de investigacion
Cambia el protocolo de un experimento y una plantilla de metodo. No mueve ningun dato: las pasadas 1 y 1b conservan sello, datos y veredictos.

### Deuda abierta
- **Pieza 3, fuera de este repositorio.** Los verificadores del tratamiento y del entorno viven en `experimentosdd-a4/scripts/`. Hasta que existan, las dos filas declaran escalon 2 **sin tener quien lo ejecute**, y el runbook lo dice asi: es limite vigente, no control activo. M-22 y M-25 quedan `Aprobada` y no pueden cerrarse desde aca.
- **Si el harness permite suprimir la auto-actualizacion durante una tanda esta sin averiguar.** Determina si el entorno llega a escalon 1 intra-tanda o se queda en 2.
- **T1 y T2 pueden correr bajo versiones distintas y eso no se elimina**, se declara. Es un confundido conocido de cualquier pasada con tandas separadas 12-72 h.
- **§Fases dice «Cinco sondas» y la tabla lista seis.** Error preexistente, detectado al escribir esta entrega y **no corregido**: tocarlo seria una edicion post-dato a pasadas cerradas sin beneficio para ninguna corrida futura. Se deja contado.
- Sin novedad: M-02 sigue `Aprobada` y sin ejecutar; M-30 `Propuesta`; M-24(2) sin aprobar; M-26 y M-08 sin decidir.

## El sello del experimento pasa a resolverse por escalones (2026-08-23) — COMPLETADA

**Accion**: pieza 1 de M-22 y M-25, entregada junta porque cae en un solo artefacto. `templates/EXPERIMENTO.md` suma la seccion obligatoria «Sello». Los dos items quedan **`Aprobada`**, no `Hecha`: su cierre depende de piezas que este repositorio no contiene.

### Que se encontro
Los dos items apuntaban al mismo lugar. M-22 fija la jerarquia general —eliminar como variable, verificar en corrida, o declarar sin verificador— y M-25 la aplica al tratamiento, declarando a M-22 como su SSOT y sin reproducirla. Se evaluo unificarlos y **no conviene**: fusionarlos obligaria a duplicar la jerarquia o a perder el modo de falla propio del tratamiento, y borraria cual de las dos observaciones sostiene cual regla —M-22 nacio del entorno auto-actualizandose entre tandas, M-25 del tratamiento editado por el trabajo normal del repositorio—. Lo que si se unifica es la entrega: la pieza documental de ambos es una sola seccion.

Al mapear las piezas aparecio el limite que decide el estado de los items: **el verificador en corrida vive en otro repositorio**. Los scripts de preparacion de A-04 (`preparar_rep.sh`, `preparar_rep_cc.sh`) estan en `experimentosdd-a4`, hermano de este arbol y fuera del alcance de este protocolo. Ninguno de los dos items puede declararse `Hecha` desde aca.

### Que cambio
- `templates/EXPERIMENTO.md`: seccion «Sello», entre «Diseno» y «Metricas». Trae los tres escalones en orden y por que el orden importa; una tabla por componente —que queda sellado, escalon, mecanismo, que hace el verificador si diverge—; el criterio de que entra en la tabla, que es lo que el documento declare sellado y nada mas; la regla de M-25 para tratamiento versionado, por commit y extraido de ese commit, con el residuo de vigencia externa declarado como cosa distinta de la atribucion; que la prevencion no vuelve prescindible el verificador sino que lo deja como heartbeat; y que el verificador MUST detener y explicitar, MUST NOT elegir.
- `SPECS_REGISTRY.md`: la spec de los templates suma el check de validacion de la seccion nueva.
- `agenda/MEJORAS-METODO.md`: M-22 y M-25 pasan a `Aprobada` con la pieza 1 hecha, y cada una enumera las dos que le faltan y donde viven.

Las tres reservas que M-22 pedia resolver antes de darla por disenada quedaron resueltas dentro de la seccion, no en prosa aparte: que componentes entran, que hace el verificador cuando dispara, y el retorno decreciente del escalon 1.

### Como se valido
`./tools/check_docs.py` y `--staged` en 0 ERROR, 1 WARN (M-08). La seccion se escribio con rutas relativas a la raiz, que es la convencion que el template ya usaba, para que siga resolviendo cuando se copia dentro de `experimentos/`.

Lo que **no** esta validado: que la seccion se pueda llenar sin ambiguedad para un experimento real. Eso lo prueba la pieza 2 sobre el runbook de A-04, y hasta entonces la seccion es una forma propuesta que nadie ejercito.

### Por que esto es entrada de metodo y no hallazgo de investigacion
Cambia una plantilla de metodo y la spec que la gobierna. No mueve ningun dato de A-04 ni de ningun otro experimento.

### Deuda abierta
- **Pieza 2, en este repositorio**: `experimentos/a04-conducta-agente/PRUEBA-PISO-RUIDO-A4.md` sella componentes sin resolver los escalones. Es ademas la prueba de que la seccion es llenable.
- **Pieza 3, fuera de este repositorio**: el verificador de entorno y de correspondencia con el commit sellado, en `experimentosdd-a4/scripts/`. Mientras no exista, la regla del template es una exigencia sin verificador — el escalon 3 aplicado a la propia mejora.
- **El template es obligatorio para experimentos nuevos, y los vigentes no se migran solos.** A-04 y B-07 ya estan escritos sin la seccion; solo A-04 tiene pasada futura, asi que la pieza 2 lo cubre y B-07 queda como esta, cerrado.
- Sin novedad: M-02 sigue `Aprobada` y sin ejecutar; M-30 `Propuesta`; M-24(2) sin aprobar; M-26 y M-08 sin decidir.

## Alta de M-30 y cierre de las dos deudas sin item que dejo M-29 (2026-08-23) — COMPLETADA

**Accion**: la deuda de rotacion del historial se da de alta como **M-30** (`Propuesta`); la deuda sobre la ventana de `precedencia` se cierra escribiendo el limite donde se lee; la deuda sobre los cerrados sin descripcion se cierra por verificacion: estaba sobredimensionada.

### Que se encontro
Las tres deudas que M-29 dejo contadas y sin item no eran de la misma clase, y tratarlas igual las habria dejado arrastrandose otra entrega mas.

**La rotacion es una mejora de metodo y necesitaba item.** Es lo unico de las tres que exige trabajo futuro: cambia la forma del registro cronologico y toca el registro de specs y el indice.

**La ventana de `precedencia` es un limite, no un defecto.** El check mira -4/+12 lineas alrededor de cada mencion; al reordenar el backlog, la mencion de `SPECS_REGISTRY.md` de una seccion entro en la ventana de otra que hablaba de otro tema. La consecuencia general es que su veredicto depende de la disposicion del documento y no solo de su contenido: mover secciones puede crear o borrar hallazgos sin que cambie una afirmacion. Un limite de esa clase no se cierra ajustando el check —afinar un verificador sobre un caso unico es lo que M-21 ya decidio no hacer sin datos— sino escribiendolo donde alguien lo vaya a leer.

**La tercera estaba sobredimensionada.** M-29 anoto que el backlog «ya no dice de que trataba un item cerrado». Verificado contra el documento: los 18 cerrados conservan titulo y prioridad en la tabla de estado, y §Items cerrados ya lo dice explicitamente. Lo que se perdio es el desarrollo, no la identificacion. La deuda se cierra sin cambio de artefacto.

### Que cambio
- `agenda/MEJORAS-METODO.md`: alta de **M-30**, prioridad media, `Propuesta`. Propone rotar por periodo —no podar, que esta prohibido— con el precedente de `historial/ROADMAP-MEJORAS-SDD.md` ya aplicado, la medicion que lo motiva, los dos consumidores que pagan el crecimiento y tres reservas. La primera reserva declara que cualquier umbral por tamano seria hoy eleccion de diseno y no medicion, y MUST presentarse como tal.
- `tools/check_docs.py`: el docstring de `check_precedence` suma el limite de la ventana, con el caso que lo hizo visible y el motivo de no ajustar el check.

### Como se valido
`./tools/check_docs.py` y `--staged` en 0 ERROR, 1 WARN (M-08). Para la tercera deuda, conteo cruzado sobre el documento: 18 ids `Hecha` en la tabla de estado y 18 filas en la tabla de punteros, los mismos en las dos.

### Por que esto es entrada de metodo y no hallazgo de investigacion
Da de alta una mejora al metodo y modifica el docstring de un verificador. No mueve ningun dato.

### Deuda abierta
- **M-30 queda `Propuesta` y sin ejecutar, a proposito.** Al corte el archivo se sigue leyendo; lo que se compra hoy es que la rotacion dispare por regla escrita y no por decision en caliente. El item declara ademas que rotar parte el grep en dos, que es su costo real.
- **M-02 sigue `Aprobada` y sin ejecutar** desde la Fase 9. Un item aprobado que nadie toca en un mes es una decision revertida de hecho y sin registrar: o se ejecuta, o se le cambia el estado.
- Sin novedad: M-22 y M-25 en `Propuesta`, ambas precondicion de cualquier pasada 2 de A-04; M-24(2) sin aprobar; M-26 y M-08 sin decidir.

## El contenido de los items cerrados migra al historial; el backlog queda con el puntero solo (2026-08-23) — COMPLETADA

**Accion**: segunda pasada de M-29, por correccion del usuario. La primera dejaba en el backlog el planteo previo al cierre de cada item `Hecha`; ahora un item cerrado no conserva contenido propio. El planteo no se borra: migra a la entrada de historial que cerro el item.

### Que se encontro
La primera pasada corto la narracion de cierre pero conservo el planteo, con el argumento de que ese texto no estaba duplicado y que el Principio V pide no reescribirlo desde el resultado. El argumento sobrevive, pero la conclusion era la equivocada: el planteo se preserva igual si **se muda** en vez de quedarse, y quedandose seguia cobrandole al lector del backlog el costo que M-29 existe para eliminar. La primera pasada bajo el documento de 388 a 355 lineas; esta lo baja a 199.

### Que cambio
- `historial/sdd.md`: cada una de las 15 entradas que cierran un item de metodo suma al final un bloque `### Planteo de la mejora, migrado de agenda/MEJORAS-METODO.md (2026-08-23)`, con el texto tal como estaba en el backlog y un subtitulo `####` por item. **No se toco una sola linea de lo ya asentado**: el bloque se añade, se fecha y declara su origen, que es la unica forma de traer material a un registro que MUST NOT reescribirse hacia atras. Las rutas migradas pierden el prefijo `../`, que en este directorio apuntaria fuera del repositorio.
- `agenda/MEJORAS-METODO.md`: 355 → 199 lineas. §Items cerrados deja de tener una seccion por item y pasa a ser una tabla de dos columnas —ID y entrada de historial que lo cerro—, que es lo que el campo `validacion` de la spec pedia desde el alta del documento. El titulo y la prioridad de cada cerrado siguen en la tabla de estado, sin duplicarse.
- `SPECS_REGISTRY.md`: el `incluye`, el `excluye` y el check de validacion de ese documento pasan de «solo su planteo previo al cierre» a «solo el puntero», y el `excluye` describe la migracion como bloque añadido y fechado.

### Como se valido
`./tools/check_docs.py` y `--staged` en 0 ERROR, 1 WARN (M-08). Los 18 items cerrados tienen fila en la tabla de punteros y bloque migrado; los 27 separadores `---` entre entradas siguen siendo 27, con el bloque migrado por dentro de su entrada y no despues.

### Por que esto es entrada de metodo y no hallazgo de investigacion
Cambia la forma del backlog de metodo y la spec que lo gobierna, y mueve material entre dos documentos de metodo. No mueve ningun dato de investigacion.

### Deuda abierta
- **El backlog ya no dice de que trataba un item cerrado**, mas alla del titulo de la tabla de estado. Es el costo aceptado de la regla nueva: para saber mas hay que ir al historial. Si aparece friccion real —alguien releyendo cerrados seguido— el caso se cuenta antes de aflojar la regla, igual que M-21.
- **La entrada anterior de este mismo dia describe la regla que esta corrige.** Se deja como esta: registra lo que se decidio cuando se decidio.
- Sin novedad: la ventana de `precedencia` sigue siendo sensible a la disposicion del documento; `historial/sdd.md` crece sin techo y la salida es rotar por periodo, sin item todavia; M-22 y M-25 en `Propuesta`; M-24(2) sin aprobar; M-26 y M-08 sin decidir.

## El backlog de metodo se poda a puntero y se reordena por estado (2026-08-23) — COMPLETADA

**Accion**: M-29 dada de alta y ejecutada. `agenda/MEJORAS-METODO.md` deja de narrar la ejecucion de lo ya cerrado y pasa a referenciar la entrada de historial que la contiene; los items quedan agrupados por estado. La regla del corte se escribe en la spec, no en el item.

### Que se encontro
El 57% del documento —222 de 388 lineas— eran secciones de items `Hecha` narrando ejecucion, validacion y limites. Esa narracion ya vivia aca, y la spec del documento la excluye desde su alta: `excluye` decia «el registro cronologico de lo ya aplicado — vive en `historial/sdd.md`» y `validacion` pedia que «los items `Hecha` referencian la fase de `historial/sdd.md` que los cerro». No era una mejora pendiente sino deriva doc-vs-spec, y ninguno de los checks la ve: reproducir prosa fuera de su SSOT sigue sin verificador (limite ya declarado en el Principio I).

El costo lo paga el uso normal del documento —leerlo para decidir que falta hacer—, porque no hay forma de saber que esta abierto sin barrerlo entero.

### Que cambio
- `agenda/MEJORAS-METODO.md`: 388 → 355 lineas. Cada item `Hecha` conserva su planteo previo al cierre y remite el resto a la entrada que lo cerro; se verifico entrada por entrada que el material cortado estuviera efectivamente aca antes de cortarlo. Los items pasan a `###` bajo dos agrupadores `##` —«Items abiertos», por prioridad, y «Items cerrados», por ID— y la tabla de estado se ordena igual. Alta de **M-29**.
- `SPECS_REGISTRY.md`: la spec de ese documento suma al `incluye` «de un item `Hecha`, solo su planteo previo al cierre», al `excluye` la ejecucion, la validacion y los limites resultantes, y un check de validacion nuevo. La regla vive ahi y no en M-29, que solo explica por que el corte cae donde cae.

Un limite vigente no se copia al backlog: se nombra donde vive. M-15 remite al campo `Verificador:` de `CONSTITUTION.md` en vez de reproducir el conteo de principios cubiertos, que cambia cada vez que se cierra una mejora; M-18, M-19, M-23, M-24 y M-28 remiten al docstring del check o al propio hook.

### Como se valido
`./tools/check_docs.py` y `--staged` en 0 ERROR, 1 WARN (M-08, el vivo a proposito).

La primera corrida dio 1 ERROR, y es el hallazgo del dia: `precedencia` marco `agenda/MEJORAS-METODO.md:181`. Falso positivo **producido por el reordenamiento**. El check mira una ventana de -4/+12 lineas alrededor de cada mencion de «precedencia» y exige que nombre la constitucion si nombra el registro; al mover M-05 junto a M-01, la mencion de `SPECS_REGISTRY.md` de una seccion entro en la ventana de la otra, que hablaba de otro tema. Se resolvio nombrando la constitucion en la frase de M-01, que ademas es lo que el check verifica.

### Por que esto es entrada de metodo y no hallazgo de investigacion
Cambia la forma del backlog de metodo y la spec que lo gobierna. No mueve ningun dato. `agenda/` no dispara `metodo-historial` a proposito —proponer una mejora no es adoptarla— pero esta entrega no propone: reorganiza el documento y enmienda su spec, y el cambio de `SPECS_REGISTRY.md` disparo el check igual.

### Deuda abierta
- **La ventana de `precedencia` depende de la disposicion del documento, no solo de su contenido.** Mover secciones puede crear o borrar hallazgos sin que cambie una sola afirmacion. Es la misma clase de limite que el resto del script —heuristica declarada como tal en su propio docstring— y no se ajusto: aflojar un verificador para acomodar un reordenamiento es la deriva que M-21 ya decidio no cometer. Queda contado, sin item.
- **`historial/sdd.md` crece sin techo.** 34 entradas y ~890 lineas, 20 de ellas de agosto. No es el problema que M-29 corrige —este archivo es append-only y se lee por la punta o por grep, no entero— pero tiene limite real, y la salida para un log es rotar por periodo, no podar. Sin item propio todavia; hay precedente de rotacion en `historial/ROADMAP-MEJORAS-SDD.md`.
- **La poda rindio menos de lo proyectado**: se estimaron ~150 lineas y salieron 33 netas, porque la regla conserva todo el planteo previo y varios items cerrados lo tienen largo. Lo que si bajo a la mitad es el costo del uso normal: decidir que falta hacer pasa de leer 388 lineas a leer las 174 primeras.
- Sin cambios: M-22 y M-25 en `Propuesta`; M-24(2) sin aprobar; M-26 y M-08 sin decidir.

### Planteo de la mejora, migrado de `agenda/MEJORAS-METODO.md` (2026-08-23)

Texto tal como estaba escrito en el backlog **antes** de este cierre: diagnostico, forma propuesta y reservas. Se trae aca por M-29, que deja en el backlog solo el puntero. No modifica nada de lo asentado arriba.

#### M-29 — El backlog de método cargaba la narración de lo ya cerrado

El 57% de este documento —222 de 388 líneas— narraba la ejecución de items ya cerrados: qué se hizo, cómo se validó, qué deformaciones deliberadas se probaron. Esa narración ya vivía en `historial/sdd.md`, y la spec de este documento la excluye desde su alta (`SPECS_REGISTRY.md`: «el registro cronológico de lo ya aplicado — vive en `historial/sdd.md`», y `validacion`: «los items `Hecha` referencian la fase de `historial/sdd.md` que los cerró»). No era una mejora pendiente: era deriva doc-vs-spec.

El costo lo paga quien lee para decidir qué falta hacer, que es el uso normal del documento: no hay forma de saber qué está abierto sin barrerlo entero.

**Hecha el 2026-08-23.** Dos cambios: cada item `Hecha` conserva su planteo previo al cierre y remite el resto a la entrada de historial que lo cerró; y los items quedan agrupados por estado —abiertos primero— en vez de por orden de alta.

**El corte quedó escrito en la spec**, no acá: `SPECS_REGISTRY.md` lo declara en el `incluye` y el `excluye` de este documento, y suma el check de validación correspondiente. Dejarlo enunciado sólo en este item habría reincidido en lo mismo que el item corrige.

Lo que sí pertenece acá es **por qué** el corte cae donde cae. Se conserva el texto anterior al cierre porque no está duplicado en ningún lado y porque el Principio V es la razón de no reescribirlo desde el resultado: M-23 es el caso que lo justifica —el diseño enunciado se ejecutó más angosto, y esa diferencia sólo se ve si el enunciado original sigue ahí—. Se corta la narración posterior porque sí está duplicada, y un límite vigente se referencia en vez de copiarse, que es el Principio I aplicado al propio backlog.

Reserva registrada y no resuelta: `historial/sdd.md` crece sin techo por diseño (34 entradas, ~890 líneas, 20 de ellas de agosto). No es el mismo problema —es append-only y se lee por la punta o por grep, no entero— pero tiene un límite real, y la salida para un log no es podar sino rotar por período. Sin item propio todavía.

## Propagacion de M-28 a los documentos que describen el backstop (2026-08-23) — COMPLETADA

**Acción**: cerrar M-28 del lado documental. Ninguna regla ni verificador cambia; se alinea lo que tres documentos afirmaban sobre lo que el backstop cubre.

### Qué se encontró
Al revisar si M-28 quedaba cerrada aparecieron tres desalineaciones, todas del mismo tipo: texto que describía el estado anterior al cambio.

### Qué cambió
- `AGENTS.md` §Al cerrar una iteración: la enumeración de lo que el backstop cubre suma el disparador que faltaba —que ningún documento anote en su encabezado un campo que el registro reserva—, nombrando su SSOT en vez de repetir la regla.
- `00-INDEX.md`: la línea que remitía al registro enumeraba cuatro campos cuando la regla ya nombra ocho. Se quitó la enumeración y quedó el puntero: enumerar de nuevo habría reintroducido la duplicación que la regla prohíbe.
- `tools/check_docs.py`: el docstring del módulo suma `M-27` y `M-28` a los ids que implementa.

`CONSTITUTION.md` no requiere cambio: el `Verificador:` del Principio I ya nombra `excluded-field`, y su nota sobre lo que ningún check cubre —la regla reproducida en prosa— sigue siendo cierta.

### Cómo se validó
`./tools/check_docs.py` y `--staged` en 0 ERROR, 1 WARN (M-08). El error de `metodo-historial` que exigió esta entrada es el Principio VI funcionando: la propagación tocaba método y no se podía commitear sin asentarla.

### Por qué esto es entrada de método y no hallazgo de investigación
Toca el protocolo del asistente y el índice de navegación. No mueve ningún dato.

### Deuda abierta
- Sin novedad respecto de la entrada anterior: la paráfrasis sigue sin verificador y la clave a mitad de renglón no se detecta.

## `excluded-field` verifica la regla del registro, no el `excluye` de cada spec (2026-08-23) — COMPLETADA

**Acción**: M-28 cerrada. El check cambia de fuente de autoridad, gana dos formas de detección y encuentra seis anotaciones en cinco documentos, corregidas en la misma entrega.

### Qué se encontró
La regla escrita el mismo día cubría los ocho campos, pero el verificador seguía cableado al `excluye` de cada spec, y esa exclusión estaba escrita sólo para los dos índices de línea: cuarenta y ocho documentos quedaban fuera de toda verificación. Con la autoridad puesta en la regla global, el check encontró seis anotaciones vivas.

Aparecieron además dos anotaciones que el check **no** ve y se corrigieron a mano: un «Estado: Activo» a mitad de renglón —la detección por clave exige que la clave abra la línea— y una línea `Alcance:` que declaraba una exclusión ausente del `excluye` registrado.

### Qué cambió
- `tools/check_docs.py`: `registry_spec_fields()` deriva los ocho campos de la viñeta del registro, y el check falla si la derivación devuelve menos de cuatro — una regla reescrita no puede vaciarlo en silencio. Tres formas: encabezado por clave, título de columna por clave, anotación por valor. Las dos primeras corren sólo en el encabezado; la tercera, en todo el documento.
- `SPECS_REGISTRY.md`: las exclusiones per-spec de los dos índices de línea se resumen a una línea que remite a la regla global; la exclusión «transferencia a Línea A» de `software/RELACION-FR-VS-SC-Y-COBERTURA.md` pasa a su `excluye`.
- Cinco documentos limpiados: `docs-y-investigacion/GUIA-INICIO-PROYECTO-INVESTIGACION.md` (columnas `Owner` y `ssot_level`), `software/COMPARATIVA-SPECKIT-VS-TESTIGO.md`, `software/DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` y `software/RELACION-FR-VS-SC-Y-COBERTURA.md` (línea «Deriva de:»), `software/SDD-EN-LEGACY-Y-BROWNFIELD.md` («Estado: Borrador»).
- `agenda/MEJORAS-METODO.md`: M-28 a **Hecha**.

### Cómo se validó
La ventana de las dos formas por clave no es prudencia genérica: con el título de columna corriendo en todo el documento aparecían dos falsos positivos —la columna «Estado» del backlog de mejoras y otra de `software/PLAN-PRUEBAS.md`, que son estados de otra cosa—. Acotarla al encabezado los eliminó sin perder ningún hallazgo real.

Sobre el árbol previo a las correcciones, el check reproduce los seis hallazgos; sobre el corregido, 0 ERROR. Dos deformaciones deliberadas —`Owner:` y `Deriva de:` en el encabezado de un documento limpio— detectadas; una línea de prosa en el mismo encabezado mencionando «SSOT» y «estado», no detectada. `./tools/check_docs.py` y `--staged` en 0 ERROR, 1 WARN (M-08).

### Por qué esto es entrada de método y no hallazgo de investigación
Cambia un verificador y una regla del registro. Los cuerpos de los cinco documentos corregidos no se tocaron.

### Deuda abierta
- Detecta la anotación, no la paráfrasis: «este documento manda sobre X» sigue sin verificador, igual que `scope-home`.
- La detección por clave exige que la clave abra el renglón. El `Estado: Activo` a mitad de oración que hubo que corregir a mano no se habría detectado.
- Sin cambios: M-22 y M-25 en `Propuesta`; M-24(2) sin aprobar; M-26 y M-08 sin decidir.

### Planteo de la mejora, migrado de `agenda/MEJORAS-METODO.md` (2026-08-23)

Texto tal como estaba escrito en el backlog **antes** de este cierre: diagnostico, forma propuesta y reservas. Se trae aca por M-29, que deja en el backlog solo el puntero. No modifica nada de lo asentado arriba.

#### M-28 — Encabezados que reproducen campos del registro

`estado`, `ssot_level`, `owner` y `deriva_de` son campos que `SPECS_REGISTRY.md` declara para **todo** documento. Cuando un documento los repite en su encabezado crea una segunda fuente del mismo dato, que puede desincronizarse sin que nada lo señale. No depende de que el documento sea original o derivado: el registro es dueño de esos cuatro campos en los dos casos.

Casos vivos, detectados en la auditoría de encabezados del 2026-08-23:

1. `docs-y-investigacion/GUIA-INICIO-PROYECTO-INVESTIGACION.md` abre con una tabla que trae columnas `ssot_level` y `owner`. Mezcla dos campos del registro con dos que no lo son (`Creacion`, `Version`), así que el arreglo es recortar columnas, no borrar la tabla.
2. `software/SDD-EN-LEGACY-Y-BROWNFIELD.md` abre con «Estado: Borrador».
3. Cuatro documentos de línea B abren con «Deriva de: X». Tres coinciden con el registro; el cuarto —`software/RELACION-SPEC-VS-EPICA.md`— afirmaba una derivación que el registro había borrado el 2026-08-03, y se corrigió el 2026-08-23. Ese caso es la evidencia de que la clase no es teórica: el registro cambió, el encabezado no, y la divergencia sobrevivió cinco meses sin que nada la marcara.

Los casos 1 y 2 coinciden hoy con el registro. Eso no los vuelve correctos, los vuelve **todavía no divergentes** — el estado exacto en que estaba `software/00-INDEX.md` antes de la auditoría de M-14, que lo encontró diciendo «Borrador» sobre un documento ya `Activo`.

**Hecha el 2026-08-23**, en el orden que el caso pedía: primero el check, después la corrección de lo que encontró. La regla vigente vive en `SPECS_REGISTRY.md` §Reglas globales, y alcanza a más campos que los cuatro del planteo de arriba; el alcance del check, sus tres formas de detección y sus límites —detecta la anotación, no la paráfrasis, y exige que la clave abra el renglón—, en su docstring.

## La regla de alcance pasa de cuatro campos a ocho (2026-08-23) — COMPLETADA

**Acción**: `SPECS_REGISTRY.md` §Reglas globales. La regla que reservaba al registro los campos de spec cubría `proposito`, `incluye`, `excluye` y `validacion`; ahora cubre también `ssot_level`, `estado`, `owner` y `deriva_de`. Parte normativa de M-28.

### Qué se encontró
Los cuatro campos que faltaban se prohibían caso por caso —sólo en la spec de los dos índices de línea— y por eso el resto del repositorio no estaba alcanzado por ninguna regla escrita. Los casos vivos que lo mostraron: una tabla de cabecera con `ssot_level` y `owner`, un encabezado con «Estado: Borrador», y una línea «Deriva de: X» que sobrevivió cinco meses a que el registro borrara ese campo.

Radio medido antes de escribir la regla, con el reconocedor de `excluded-field` sobre los 50 documentos: dos hallazgos, y uno es la excepción declarada (la tabla de rol del `00-INDEX.md` de raíz). La regla global no rompe nada.

### Qué cambió
- `SPECS_REGISTRY.md` §Reglas globales: la regla nombra los ocho campos, deja `path` afuera —una ruta se reproduce en cada link—, declara la excepción única y limita el encabezado a una línea de identidad, nombrando las tres formas prohibidas: línea `Campo: valor`, tabla de cabecera y anotación junto a un link.
- `agenda/MEJORAS-METODO.md`: M-28 registra la regla escrita y lo que falta para verificarla.

### Cómo se validó
`./tools/check_docs.py` y `--staged` en 0 ERROR, 1 WARN (M-08). La regla es normativa: hoy no suma verificación, y eso queda dicho.

### Por qué esto es entrada de método y no hallazgo de investigación
Cambia una regla del registro. No mueve ningún dato ni ninguna conclusión de investigación.

### Deuda abierta
- La regla no está verificada: `excluded-field` sigue leyendo el `excluye` de cada spec, así que sólo alcanza a los dos índices de línea. Cablearlo a la regla global es lo que la vuelve universal (M-28).
- `annotation_slots` no reconoce la línea de encabezado `Campo: valor`, y `owner`/`deriva_de` no tienen valores válidos que buscar: la forma general es detectar por clave (M-28).
- Las exclusiones per-spec de los dos índices quedan escritas aunque la regla global ya las cubra, porque son el cableado actual del check. Se borran junto con el cableado nuevo, no antes.
- Dos encabezados siguen sin limpiar: `docs-y-investigacion/GUIA-INICIO-PROYECTO-INVESTIGACION.md` y `software/SDD-EN-LEGACY-Y-BROWNFIELD.md`.

## Barrido de encabezados: M-05 cerrada, M-28 abierta (2026-08-23) — COMPLETADA

**Acción**: barrido de los encabezados de los 45 documentos autorados. M-05 se cierra con un caso corregido; la clase distinta que el barrido encontró se da de alta como M-28.

### Qué se encontró
M-05 apuntaba a encabezados que enumeran su `incluye`/`excluye` en vez de dejar el alcance en el registro. Su caso conocido —`comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md`— ya cumplía. Apareció uno vivo que no estaba anotado: `software/RELACION-SPEC-VS-EPICA.md` declaraba en su línea `Alcance:` una exclusión —la transferencia del razonamiento a Línea A— que su `excluye` registrado no tenía. Ningún otro encabezado del repositorio enumera su alcance.

El mismo documento traía además «Deriva de: `ANALISIS-SPEC-KIT.md`», y el registro no le declara `deriva_de` desde el 2026-08-03: M-13 se lo quitó al concluir que era relación forzada —«un análisis paralelo con evidencia externa propia», dice esa entrada— y corrigió el registro sin bajar al documento. La divergencia sobrevivió cinco meses sin que nada la marcara.

Esa segunda cosa no es de la clase de M-05: no es alcance restado, es un **campo del registro reproducido** en un encabezado. El barrido encontró dos casos más de esa clase, hoy coincidentes con el registro.

### Qué cambió
- `software/RELACION-SPEC-VS-EPICA.md`: encabezado reducido a identidad —fecha y línea—, sin la derivación falsa ni la exclusión. Bloque `[SDD-Check]` nuevo al pie; el anterior no se toca, que es registro datado.
- `SPECS_REGISTRY.md`: la exclusión «transferencia del razonamiento a Línea A» pasa al `excluye` de la spec de ese documento, que es donde el alcance vive. Nada se pierde al limpiar el encabezado.
- `agenda/MEJORAS-METODO.md`: M-05 a **Hecha** con el resultado del barrido; **M-28** dada de alta —encabezados que reproducen `estado`, `ssot_level`, `owner` o `deriva_de`— con sus casos y la ruta barata para cerrarla.

### Cómo se validó
Barrido mecánico de las primeras líneas de cada `.md` autorado y cruce de cada hallazgo contra su entrada del registro. Se verificó que ningún otro documento sostuviera la derivación borrada: `software/00-INDEX.md` y `RELACION-FR-VS-SC-Y-COBERTURA.md` lo citan sin llamarlo derivado. `./tools/check_docs.py` y `--staged` en 0 ERROR, 1 WARN (M-08).

### Por qué esto es entrada de método y no hallazgo de investigación
Cierra un ítem de método, abre otro y mueve un campo de alcance al registro. El cuerpo del documento reconciliado no se tocó y ninguna conclusión de investigación cambia.

### Deuda abierta
- M-28 sin ejecutar: dos encabezados siguen reproduciendo campos del registro, hoy coincidentes con él. La reserva a decidir antes de escribir la exclusión spec por spec es si conviene declararla como regla global del registro.
- Sin cambios: M-22 y M-25 en `Propuesta`; M-24(2) sin aprobar; M-26 y M-08 sin decidir.

### Planteo de la mejora, migrado de `agenda/MEJORAS-METODO.md` (2026-08-23)

Texto tal como estaba escrito en el backlog **antes** de este cierre: diagnostico, forma propuesta y reservas. Se trae aca por M-29, que deja en el backlog solo el puntero. No modifica nada de lo asentado arriba.

#### M-05 — Encabezados que restatan su alcance

La regla de alcance en un solo lugar (`SPECS_REGISTRY.md` §Reglas globales) admite una línea de identidad en el encabezado, no la enumeración de `incluye`/`excluye`. Caso conocido: `comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md`. Migración al tocar cada documento, sin barrido masivo.

**Hecha el 2026-08-23.** La clase distinta que el barrido encontró se dio de alta como **M-28**.

## `sdd-check-fields` pasa a mirar `templates/` (2026-08-23) — COMPLETADA

**Acción**: M-27 dada de alta y ejecutada. El check deja de saltear `templates/`; `historial/` conserva la exención con su motivo escrito en el código.

### Qué se encontró
Leyendo la implementación al ejecutar M-24 apareció que el check saltea tres orígenes. `AGENTS.md` es el SSOT del bloque y no puede violarse a sí mismo; `historial/` registra entregas pasadas que MUST NOT reescribirse hacia atrás, así que un WARN ahí no sería accionable. `templates/` no tenía justificación equivalente y era el peor lugar donde no mirar: un template es método, se copia en cada experimento, y una definición reproducida ahí se propaga sola a cada instancia futura sin volver a pasar por revisión.

La reserva —que un template legítimamente muestra la forma de lo que se llena— no se sostuvo, por dos motivos independientes: los templates actuales hablan del bloque en prosa y no enumeran sus campos, y la regla instancia/definición que el check ya tenía cubre el caso hipotético.

### Qué cambió
- `tools/check_docs.py`: `templates/` sale de la lista de orígenes salteados de `check_sdd_check_fields`; el comentario explica por qué `historial/` se queda y por qué esto salió barato.
- `agenda/MEJORAS-METODO.md`: M-27 dada de alta y cerrada en la misma entrega.

### Cómo se validó
Primero se midió el costo: quitar la exención **no produjo ningún hallazgo** en el árbol, que es lo que hizo la decisión barata — no había deuda que pagar, sólo un hueco que cerrar antes de que alguien lo usara. Después, validación en las dos direcciones sobre `templates/EXPERIMENTO.md`: una enumeración de cuatro campos del bloque dispara el WARN en la línea correcta, y la misma enumeración precedida del literal `[SDD-Check]` no dispara. Árbol restaurado; `./tools/check_docs.py` y `--staged` en 0 ERROR, 1 WARN (M-08).

### Por qué esto es entrada de método y no hallazgo de investigación
Cambia el alcance de un verificador. No mueve ningún dato ni ninguna conclusión de investigación.

### Deuda abierta
- Ampliar el origen no amplía la clase detectada: el check sigue viendo sólo enumeraciones de campos del `[SDD-Check]`, y una regla reproducida en prosa fuera de su SSOT sigue sin verificador (M-24(2), sin aprobar).
- Sin cambios: M-22 y M-25 en `Propuesta`; M-26, M-08 y M-05 sin decidir.

### Planteo de la mejora, migrado de `agenda/MEJORAS-METODO.md` (2026-08-23)

Texto tal como estaba escrito en el backlog **antes** de este cierre: diagnostico, forma propuesta y reservas. Se trae aca por M-29, que deja en el backlog solo el puntero. No modifica nada de lo asentado arriba.

#### M-27 — `sdd-check-fields` no miraba `templates/`

El check saltea tres orígenes: `AGENTS.md`, que es el SSOT del bloque y por eso no puede violarse a sí mismo; `historial/sdd.md`; y `templates/`. Los dos primeros están bien. El tercero era el peor lugar posible para no mirar: un template **es** método, se copia en cada experimento, y una definición reproducida ahí se propaga sola a cada instancia futura sin volver a pasar por ninguna revisión.

Detectado el 2026-08-23 leyendo la implementación al ejecutar M-24, no por un caso vivo. Se abrió y se cerró el mismo día porque medirlo costó menos que discutirlo.

La reserva razonable era que un template legítimamente muestra la forma de lo que se llena, así que quitar la exención podría inundar de falsos positivos. No ocurre, por dos motivos independientes: los templates de hoy hablan del bloque en prosa y no enumeran sus campos —quitar la exención no cambió nada en el árbol—, y la regla instancia/definición que el check ya tenía cubre el caso hipotético: un template que muestre el bloque para llenar lleva el literal `[SDD-Check]` al lado y no dispara.

`historial/sdd.md` conserva la exención con motivo propio, ahora escrito en el código: el historial registra entregas pasadas y MUST NOT reescribirse hacia atrás, así que un WARN ahí no sería accionable.

Lo que este ítem **no** cierra es lo que M-24 dejó dicho: el check sigue viendo sólo enumeraciones de campos del `[SDD-Check]`. Ampliar el origen no amplía la clase detectada.

**Hecha el 2026-08-23.**

## `excluded-field` deja de mirar solo tablas (2026-08-23) — COMPLETADA

**Acción**: M-23 ejecutada. El check que impide reproducir `estado` o `ssot_level` fuera del registro pasa a reconocer también la anotación puesta junto a un link en una lista. Ninguna regla cambia: la regla ya estaba escrita en el `validacion` de la spec —«ningún link ni tabla anota `ssot_level`/rol»— y el check sólo cubría la mitad «tabla».

### Qué se encontró
El punto ciego se había detectado el 2026-08-22 auditando los tres `00-INDEX.md`: `software/00-INDEX.md` anotaba el rol de tres documentos en ítems de lista y el repositorio estaba en 0 ERROR. Se corrigió a mano y quedó como M-23.

Al implementar apareció lo que la propuesta no sabía: el diseño enunciado —«escanear cualquier línea de contenido»— produce un falso positivo en el corpus actual. `docs-y-investigacion/00-INDEX.md:17` dice «Un modelo operativo SDD liviano, sin CI obligatorio…» bajo «Resultado esperado», prosa que no anota el rol de nadie. Exigir que la línea contenga un link markdown separa la entrada de índice de la frase que menciona la palabra, y coincide con la regla tal como el registro la escribió.

### Qué cambió
- `tools/check_docs.py`: reconocedor nuevo `annotation_slots`, que devuelve las ranuras donde una anotación sería una anotación — celda de tabla (igualdad exacta, como antes) o texto que sigue a un link en un ítem de lista (palabra completa). El check pasa por `strip_code_fences`, que antes no aplicaba.
- Función renombrada `check_excluded_fields_in_tables` → `check_excluded_fields`: el sufijo dejó de ser cierto, y conservarlo habría reincidido en lo que la entrada anterior de este historial acababa de corregir.
- `agenda/MEJORAS-METODO.md`: M-23 a **Hecha**, con el diseño ejecutado y su diferencia respecto del propuesto.

El id del check no cambia, así que `CONSTITUTION.md` no requiere enmienda: el Principio I ya lo nombra y su cobertura se amplía sin que la declaración deje de ser cierta.

### Cómo se validó
Worktree histórico sobre `b24549a` —el commit anterior a la corrección manual—, la misma técnica de la Fase 12: el check reproduce el caso real, `software/00-INDEX.md:20`, «link anota `ssot_level`/rol (SSOT)». Sobre el árbol actual, cuatro deformaciones deliberadas en el mismo índice: `Activo` junto a un link, detectado; `Deriva de X.md`, no detectado; una frase con «operativo» y «SSOT» sin link, no detectada; una anotación dentro de un bloque de código, no detectada. Árbol restaurado; `./tools/check_docs.py` y `--staged` en 0 ERROR, 1 WARN (M-08).

### Por qué esto es entrada de método y no hallazgo de investigación
Cambia un verificador. No mueve ningún dato ni ninguna conclusión de investigación.

### Deuda abierta
- El check detecta el **valor** del campo, no su paráfrasis: de las tres anotaciones que el índice de línea B tenía, reproduce una y no ve las dos «Deriva de X.md». Cerrarlo exige decidir antes qué paráfrasis cuentan como anotación, que es pregunta sobre el registro y no sobre el check. Mismo límite que `scope-home`.
- Sigue sin ítem la exención de `templates/` en `sdd-check-fields`, anotada ayer en el docstring.
- Sin cambios: M-22 y M-25 en `Propuesta`; M-26, M-08 y M-05 sin decidir.

### Planteo de la mejora, migrado de `agenda/MEJORAS-METODO.md` (2026-08-23)

Texto tal como estaba escrito en el backlog **antes** de este cierre: diagnostico, forma propuesta y reservas. Se trae aca por M-29, que deja en el backlog solo el puntero. No modifica nada de lo asentado arriba.

#### M-23 — `excluded-field` escaneaba solo tablas, no listas

El check (`M-09`) solo escanea líneas que empiezan con `|` — filas de tabla markdown. `software/00-INDEX.md` reproducía el rol (`ssot_level`) de tres documentos en una lista con guiones (`- [link] — SSOT de...`, `- [link] — ... Deriva de X.`), forma que la spec de ese índice prohíbe igual que una tabla, pero que el check no reconoce por no ser tabla.

Detectado el 2026-08-22 en una auditoría de los tres `00-INDEX.md` contra `SPECS_REGISTRY.md`: cobertura de specs completa (0 archivo sin registrar, 0 spec sin archivo), pero esta anotación de rol en prosa pasó los checks existentes sin ruido — mismo patrón que motivó `M-09` (duplicación de SSOT no detectada por los checks de entonces). Corregido a mano en la misma auditoría.

Forma de la mejora: generalizar el escaneo de `check_excluded_fields_in_tables` a cualquier línea de contenido (no solo `|...|`), buscando los valores válidos de `estado`/`ssot_level` como palabra completa cerca de un link, no solo dentro de celdas de tabla. Riesgo a evitar: falsos positivos con menciones legítimas de la palabra "SSOT" fuera de una anotación de rol (por ejemplo, en prosa explicativa).

**Hecha el 2026-08-23.** **El diseño enunciado arriba se ejecutó más angosto, y el corpus dio la razón**: se exige el link en vez de barrer cualquier línea de contenido, que es lo que distingue una entrada de índice de una frase que menciona la palabra. El límite resultante —detecta el valor del campo, no su paráfrasis— está declarado en el docstring del check.

## `normative-block` pasa a llamarse `sdd-check-fields` (2026-08-23) — COMPLETADA

**Acción**: M-24 ejecutada. Renombre del check y corrección de lo que se afirmaba que cubría, en el script, en `CONSTITUTION.md` (v0.2.4, enmienda PATCH) y en `AGENTS.md`. Ninguna regla cambia y el check detecta exactamente lo mismo que antes.

### Qué se encontró
El nombre prometía la categoría entera —cualquier bloque normativo reproducido fuera de su SSOT— y la implementación cubre una sola cosa: ítems de lista que enumeran tres o más campos del bloque `[SDD-Check]`. La distancia entre las dos descripciones ya había quedado anotada como deuda el 2026-08-22, cuando cinco reglas re-enunciadas en `AGENTS.md` pasaron con el repositorio en 0 ERROR.

Al ejecutar apareció la razón para ir más allá de corregir la prosa: `CONSTITUTION.md` declaraba `normative-block` en el campo `Verificador:` del Principio I. Ahí el nombre no es una descripción sino la respuesta a «qué cubre este principio», y se lee cada vez que alguien audita cobertura — mucho más seguido que un docstring.

Dos puntos ciegos más, encontrados leyendo la implementación y **no** cerrados acá: `sdd-check-fields` escanea sólo ítems de lista y `excluded-field` escanea sólo filas de tabla, de modo que cada uno ignora justo la forma que el otro cubre; y `sdd-check-fields` saltea `templates/`, que es donde una definición reproducida se propaga a cada experimento.

### Qué cambió
- `tools/check_docs.py`: id `normative-block` → `sdd-check-fields`, función `check_normative_block` → `check_sdd_check_fields`, docstring del módulo con el motivo del renombre y docstring del check con su alcance exacto y sus tres puntos ciegos.
- `CONSTITUTION.md` v0.2.3 → v0.2.4 (PATCH: aclara redacción, no cambia el invariante). El `Verificador:` del Principio I nombra el id nuevo y agrega qué **no** cubre: la reproducción de una regla en prosa fuera de su SSOT, que es la forma más común de violar ese principio.
- `AGENTS.md` §Al cerrar una iteración: la descripción del WARN dice lo que el check hace.
- `agenda/MEJORAS-METODO.md`: M-24 a **Hecha**, menciones de M-09 al nombre nuevo con la nota del renombre.

### Cómo se validó
El renombre se corrió **en rojo a propósito**: id cambiado en el script y constitución todavía sin tocar. `constitucion` falló con «principio "I. SSOT único por tema" declara el check `normative-block`, que este script no emite» — el lazo que M-15 dejó armado, disparando sobre un caso real y no sobre una deformación deliberada. Propagado el cambio, `./tools/check_docs.py` queda en 0 ERROR y 1 WARN (el de M-08, preexistente).

Las entradas viejas de este historial conservan el nombre `normative-block` a propósito: el historial registra lo que pasó cuando pasó y MUST NOT reescribirse hacia atrás.

### Por qué esto es entrada de método y no hallazgo de investigación
Cambia el verificador de un principio y el texto de la constitución. No mueve ningún dato ni ninguna conclusión de investigación.

### Deuda abierta
- La reproducción de una regla en prosa fuera de su SSOT sigue sin verificador; ampliar el check exige antes un criterio mecánico de «bloque normativo», y M-24(2) queda sin aprobar por eso.
- El punto ciego simétrico de `excluded-field` (sólo tablas) es M-23, y se abarata extrayendo el reconocedor de forma de línea que hoy está duplicado en los dos checks.
- La exención de `templates/` en `sdd-check-fields` no tiene ítem propio: anotada en el docstring, pendiente de decidir si se quita — un template legítimamente muestra la forma de lo que se llena.
- Sigue en pie del 2026-08-22: «qué decisión habilita» sin campo en el bloque `[SDD-Check]` (M-26), y el tratamiento de A-04 sin commit fijado (M-25, reformulada el 2026-08-23 junto con M-22, ambas en `Propuesta`).

### Planteo de la mejora, migrado de `agenda/MEJORAS-METODO.md` (2026-08-23)

Texto tal como estaba escrito en el backlog **antes** de este cierre: diagnostico, forma propuesta y reservas. Se trae aca por M-29, que deja en el backlog solo el puntero. No modifica nada de lo asentado arriba.

#### M-24 — `normative-block` cubría bastante menos de lo que su nombre prometía

`AGENTS.md` lo describía como «la definición de un bloque normativo reproducida fuera de su SSOT». La implementación detecta una sola cosa: enumeraciones de los campos del bloque `[SDD-Check]`. Las dos descripciones no son la misma, y la ancha era la que el asistente leía.

Detectado el 2026-08-22: una revisión de `AGENTS.md` encontró cinco reglas re-enunciadas ahí en vez de referenciadas —la regla de propagación, el léxico normativo, el formato de commit, el límite del verificador y la disambiguación—, y **ninguna de las cinco es detectable por el check**, porque ninguna es una enumeración de campos del `[SDD-Check]`. El repositorio estaba en 0 ERROR y no dijo nada. Es el mismo patrón que M-23 y que el propio M-09: el hueco no está en lo que el check hace, sino entre lo que hace y lo que se cree que hace.

Dos formas posibles, y no son la misma mejora:

1. **Barata y honesta**: ajustar la descripción de `AGENTS.md` y el docstring para que digan lo que el check realmente hace. Cierra la falsa confianza sin tocar código. Es el piso, y conviene hacerlo aunque se haga también lo otro.
2. **Cara y de valor incierto**: ampliar el check a otros bloques normativos. Requiere primero decidir qué es un «bloque normativo» de forma mecánica —el `[SDD-Check]` lo es porque tiene delimitadores y campos con nombre; la regla de propagación es prosa— y sin esa definición no hay qué implementar. Riesgo alto de falsos positivos: toda referencia legítima menciona el tema que referencia.

**Recomendación: hacer (1) y dejar (2) sin aprobar** hasta que exista un criterio mecánico de «bloque normativo» que no sea una lista a mano —que es exactamente la deriva que `emitted_check_ids()` evita un nivel más arriba. La regla de disparadores del registro (§Reglas globales) cubre hoy este terreno por vía humana, y la spec de `AGENTS.md` ya tiene el check de validación correspondiente.

**Hecha el 2026-08-23, con (1) ampliada y (2) sin aprobar.** La forma (1) fue un paso más allá de corregir la descripción: el check se renombró, porque el identificador se lee cada vez que alguien mira qué cubre un principio.

Lo que el renombre **no** arregla quedó escrito donde se lee —el campo `Verificador:` del Principio I y el docstring del check—, no acá. El historial conserva el nombre viejo en las entradas anteriores, a propósito. La exención de `templates/` que este trabajo dejó anotada se cerró al día siguiente como **M-27**; el punto ciego simétrico de `excluded-field`, como **M-23**.

## §Qué NO hacer queda declarado como índice por modo de falla (2026-08-22) — COMPLETADA

**Acción**: encabezado nuevo y tres punteros faltantes en `AGENTS.md` §Qué NO hacer. Ninguna norma cambia.

### Qué se encontró
La revisión que motivó el alta de `CONVENCIONES.md` marcó esta sección como redundante: tres de sus seis ítems repiten en negativo algo que otra sección del mismo documento ya dice. Releída contra la regla de disparadores instalada ese mismo día, la conclusión se invierte. Los seis ítems son disparadores —ninguno define nada, todos nombran una regla que vive en otro documento— y los seis son de la clase de error **silencioso** que la regla admite en la capa residente: nadie nota que copió un alcance ni que reescribió una hipótesis.

Lo que la sección es, en realidad, es un **segundo índice** sobre el mismo conjunto, ordenado por modo de falla en vez de por fase. Se gana el lugar porque el protocolo está ordenado cronológicamente y hay reglas sin fase: los Principios V y VI aplican al diseñar, al enmendar y al cerrar, así que disolver la sección los dejaría sin dónde vivir en `AGENTS.md`.

El defecto real era otro: tres ítems no nombraban dónde vive su regla, y un índice cuya mitad se lee como norma autónoma puede divergir del protocolo sin que nada lo señale.

### Qué cambió
- Encabezado que declara la sección como índice por modo de falla, sin norma nueva.
- Los tres ítems huérfanos nombran su fuente: §Reglas globales y §Tabla SSOT del registro, `templates/RESULTADO-EXPERIMENTO.md`, y el Principio VII con §Disambiguación.

### Cómo se validó
`./tools/check_docs.py` en verde. Se verificó además que las palabras agregadas no coincidan con el vocabulario de la regla PASS de A-04 (`experimentos/a04-conducta-agente/PRUEBA-PISO-RUIDO-A4.md`, líneas 185-193), que está definido a propósito sobre términos ausentes de `AGENTS.md` para sobrevivir al test del backlog alta #6: sólo se agregaron punteros a documentos internos.

### Por qué esto es entrada de método y no hallazgo de investigación
Toca el protocolo del asistente. No mueve ningún dato ni ninguna conclusión.

### Deuda abierta
- «MUST — cada cambio debe indicar qué decisión habilita» sigue sin campo en el bloque `[SDD-Check]`.
- El check `normative-block` sólo detecta enumeraciones de campos del `[SDD-Check]`, bastante menos de lo que su nombre promete.
- El runbook de A-04 no fija con qué commit de `AGENTS.md` se entrega el tratamiento. Nada se invalida —ni la pasada 1 ni la 1b produjeron dato de H1 válido—, pero una pasada 2 MUST declarar qué versión entregó.

---

## Alta de `CONVENCIONES.md`, la capa de forma sale del registro (2026-08-22) — COMPLETADA

**Acción**: alta de un SSOT nuevo, mudanza de las convenciones de léxico y forma desde `SPECS_REGISTRY.md` y `AGENTS.md`, regla global nueva sobre qué puede vivir en la capa residente, enmienda PATCH de la constitución (0.2.2 → 0.2.3) y corrección de una regla de colocación que el repositorio no cumplía.

### Qué se encontró
Una revisión de `AGENTS.md` encontró cinco reglas re-enunciadas ahí en vez de referenciadas: la regla de propagación, el léxico normativo, el formato de commit, el límite del verificador y la disambiguación. Todas verificadas contra el árbol: cuatro eran duplicación real. La causa no era descuido — `AGENTS.md` era la única capa que el asistente tiene siempre en contexto, así que toda regla cuya ausencia duele en el momento de decidir terminaba copiada ahí.

Debajo apareció la causa estructural: `SPECS_REGISTRY.md` hacía dos trabajos, alcance por documento (qué se le exige a cada pieza) y forma de salida (§Norma de interpretación y parte de §Reglas globales). La forma no tenía hogar declarado, y por eso «nomenclatura de archivos» vivía suelta en `AGENTS.md` sin que ningún check pudiera notarlo: la constitución decía que las convenciones de forma viven en `SPECS_REGISTRY.md` **y** `AGENTS.md`, sin declarar cuál.

### Qué cambió
- **Alta**: `CONVENCIONES.md`, SSOT de léxico y forma, con spec aprobada antes de escribirlo (Principio IV). Transversal a la cadena de precedencia, no un eslabón de ella: ante choque con alcance o procedimiento, cede. Mismo patrón que `REFERENCIAS.md` —un catálogo consultado desde cualquier documento en el momento de escribir— que es el precedente que justificó darle documento propio en vez de una sección más del registro.
- **Mudanza**: §Norma de interpretación, fechas, emoticones y ortografía salen del registro; markdown, nomenclatura de archivos, léxico y formato de commit salen de `AGENTS.md`. Los orígenes quedan como puntero, no como copia. La regla de carpetas de experimento se partió: el patrón de nombre es forma y se mudó, cuándo abrir una y qué necesita spec adentro es alcance y se quedó.
- **Regla global nueva**: «la capa residente contiene disparadores, no definiciones» (operativa del Principio I). Un disparador dice cuándo ir y a dónde; una definición dice qué es. Una definición sólo puede residir en `AGENTS.md` si su ausencia produce un error **silencioso**, y aun así como línea mínima. Sin este criterio escrito, las copias vuelven — es lo que explica que hubieran aparecido cinco.
- **Enmienda constitucional (PATCH, 0.2.3)**: §Qué NO es pasa a nombrar el hogar único; el `Detalle:` del Principio I suma `CONVENCIONES.md` como sede de la clase «convención». Ningún invariante cambia.
- **Corrección de regla, no mudanza**: la colocación decía que el término normativo va al inicio de la sentencia seguido de `—`. El repositorio la usa 15 veces así y **37** como predicado dentro de la oración (`<sujeto> MUST <verbo>`), entre ellas §Precedencia y §Reglas globales del propio registro y la constitución. La regla era descriptivamente falsa y se veía recién al consolidarla al lado de su propio uso. Se reformuló para admitir las dos formas, y la definición de los tres términos pasó a tabla para que se lea como glosario —mención— y no como tres normas incumplidas.
- **`AGENTS.md`**: los cuatro puntos de duplicación quedan como disparador. El límite del verificador ahora apunta al docstring de `check_docs.py` y a §Límite honesto, que es donde el registro ya decía que vive.

### Cómo se validó
`./tools/check_docs.py` en verde: 50 documentos, 47 specs, 0 ERROR, 1 WARN (el de emoticones de `PREREG-B7.md`, que es M-08 y está vivo a propósito). Antes de escribir el documento nuevo se verificó regla por regla, con grep sobre los cuatro documentos raíz, que cada pieza a mudar existiera hoy en un solo lugar: así fue en todas salvo el léxico normativo, que ya estaba duplicado entre registro y protocolo. Dos borradores del documento se descartaron por repetir contenido que ya vivía en otro lado —la cadena de precedencia, el patrón de nombre de carpetas, la cadencia de commits— es decir, por cometer el vicio que el cambio venía a corregir. Después de mudar se verificó que ningún puntero quedara colgado.

### Por qué esto es entrada de método y no hallazgo de investigación
Se dio de alta un documento normativo, se movieron reglas entre SSOTs, se agregó una regla global y se enmendó la constitución. No toca ningún dato ni ninguna conclusión de A-04, B-06 ni B-07.

### Deuda abierta
- §Qué NO hacer de `AGENTS.md` sigue sin decidir: tres de sus seis ítems son eco de otra sección del mismo documento y tres son la única aparición de su regla. O se declara sección de recap y los tres huérfanos se anclan donde aplican, o se poda. Tiene interacción con A-04, que mide conducta bajo este protocolo, así que podar sin criterio declarado toca su variable independiente.
- «MUST — cada cambio debe indicar qué decisión habilita» no tiene campo en el bloque `[SDD-Check]`: es un MUST sin lugar mecánico donde satisfacerse ni verificarse.
- El check `normative-block` promete por su nombre más de lo que implementa: sólo detecta enumeraciones de campos del `[SDD-Check]`, así que ninguna de las cinco duplicaciones de esta entrada podía ser detectada por él. Candidato a M-.

---

## Una carpeta por experimento, mas el alta del resumen no tecnico de A-04 (2026-08-22) — COMPLETADA

**Accion**: reorganizacion de `experimentos/` en subcarpetas por experimento, regla nueva en `SPECS_REGISTRY.md`, dos patrones de `tools/check_docs.py` actualizados, extension de la excepcion M-13 a los resultados, y alta de un documento autorado con su spec aprobada.

### Que se encontro
`experimentos/` tenia diez archivos de tres experimentos distintos en un solo plano, y la pertenencia de cada uno solo se leia del sufijo de su nombre (`-A4`, `-B6`, `-B7`). Con A-04 cerrando su segunda pasada y sumando documentos, el plano dejaba de escalar.

### Que cambio
- **Estructura**: `experimentos/a04-conducta-agente/`, `experimentos/b06-circuito-testigo/`, `experimentos/b07-formato-hibrido/`. Los nombres de archivo se conservan; el nombre corto de cada carpeta sale del titulo de su documento de diseño y no se inventa. Movidos con `git mv`, asi que el historial de cada archivo se conserva.
- **Regla**: §Reglas globales del registro fija la convencion —`<id en minuscula sin guion><guion><nombre corto>`— y aclara que la carpeta **no** cambia que necesita spec: la exencion sigue atada al prefijo del nombre de archivo.
- **Verificador**: los dos patrones de exencion de `check_docs.py` admiten el segmento de carpeta intermedio, con el limite anotado en el codigo.
- **Rutas**: 31 rutas de spec, 83 menciones en 18 archivos, y todos los enlaces relativos de los diez documentos movidos, que ganaron un nivel de profundidad.
- **Alta**: `experimentos/a04-conducta-agente/RESUMEN-EJECUTIVO.md`, reencuadre del cierre de A-04 para un publico que no trabaja en el proyecto, con spec propuesta y **aprobada antes de escribirlo** (Principio IV). Entra como `derivado` de `RESULTADO-EXPERIMENTO-A4.md`, con la obligacion de resincronizar declarada en los dos extremos. Su spec separa explicitamente **afirmacion** nueva —prohibida— de **explicacion** nueva —analogias, orden del relato, que se elige contar—, que es lo que el documento aporta.

### Como se valido
`./tools/check_docs.py` en verde (0 ERROR; el unico WARN es el de emoticones de `PREREG-B7.md`, que es M-08 y esta vivo a proposito). El backstop fue quien encontro el hueco de diseño del alta: `deriva_de` MUST apuntar a un origen con spec registrada, y los resultados estan exentos por generarse desde template, asi que la referencia quedaba colgada. Es exactamente el caso que M-13 ya habia resuelto para los diseños; se extendio esa misma excepcion a los resultados y se dio de alta la entrada minima de `RESULTADO-EXPERIMENTO-A4.md`.

### Por que esto es entrada de metodo y no hallazgo de investigacion
Se cambio donde viven los documentos, una regla del registro, un verificador y el alta de una spec. Nada de esto toca ningun dato ni ninguna conclusion de A-04, B-06 ni B-07 — los diez documentos movidos no cambiaron una sola afirmacion.

### Deuda abierta
Si aparecen mas documentos de divulgacion, conviene decidir si son una clase con su propia regla en el registro —que documentos admiten reencuadre para otro publico, y con que obligacion de resincronizar— en vez de una spec por caso.

---

## A-04 pasada 1b — ampliacion de alcance del runbook al segundo harness (2026-08-22) — COMPLETADA

**Accion**: ampliacion del alcance de una spec registrada y de su fila SSOT en `SPECS_REGISTRY.md`, mas la propagacion documental del cierre de la pasada 1b a cinco documentos.

### Que se encontro
La spec de `experimentos/a04-conducta-agente/PRUEBA-PISO-RUIDO-A4.md` y su fila en la tabla SSOT lo declaraban «runbook de la **pasada 1**». Desde la enmienda 2 (2026-08-16) ese mismo runbook gobierna tambien la pasada 1b, que corrio entera bajo el: escalera propia, lectura admisible entre harnesses y confundido harness/familia-de-modelo viven en sus enmiendas 2 y 3. El registro quedo atras del documento que gobierna — la clase de deriva que el registro existe para no tener.

### Que cambio
- `SPECS_REGISTRY.md`: `proposito` de la spec de `PRUEBA-PISO-RUIDO-A4.md` y su fila de la tabla SSOT pasan a declarar las **pasadas 1 y 1b**, con la aclaracion de que lo propio de la 1b vive en las enmiendas.
- `experimentos/a04-conducta-agente/PRUEBA-PISO-RUIDO-A4.md`: encabezado alineado con el alcance real.
- `experimentos/a04-conducta-agente/RESULTADO-EXPERIMENTO-A4.md`: reestructurado para alojar las dos pasadas bajo un titulo comun, sin tocar el contenido datado de la pasada 1 — sus secciones bajan un nivel y nada mas.

### Como se valido
`./tools/check_docs.py` en verde (0 ERROR; el unico WARN es el de emoticones de `PREREG-B7.md`, que es M-08 y esta vivo a proposito). El gate de commit fue el que **encontro** esta entrada: bloqueo el primer intento del cierre por `metodo-historial`, contra un `[SDD-Check]` que habia clasificado el cambio de registro como no-metodo. Es el segundo caso registrado de un verificador corrigiendo un juicio del asistente sobre su propio cambio.

### Por que esto es entrada de metodo y no hallazgo de investigacion
Lo que se asienta aca es el cambio de **alcance declarado** de una spec — Principio VI. El **hallazgo** de la pasada 1b —techo replicado, veredicto NO APTO por banda— vive en `experimentos/a04-conducta-agente/RESULTADO-EXPERIMENTO-A4.md` y no toca el metodo: la 1b no evalua `H1` y no habilita ninguna afirmacion sobre si el protocolo funciona.

### Deuda abierta
Tres items nuevos migrados desde el cierre: `agenda/BACKLOG-INVESTIGACION.md` #16 (la calibracion no tiene resolucion para la compuerta que decide), mas el `d` comprometido por deriva de version y la reserva de aislamiento de la 1b, que quedan declarados en la deuda del resultado. La contraparte de metodo del primero ya estaba dada de alta como M-22, sin implementar.

---

## A-04 pasada 1 — alta del experimento y del runbook (2026-08-15) — COMPLETADA

**Accion**: alta de dos documentos en `experimentos/`, dos specs y dos filas SSOT en `SPECS_REGISTRY.md`, seccion nueva en `docs-y-investigacion/PLAN-PRUEBAS.md`, tres items del backlog marcados en ejecucion, cinco items de deuda migrados al backlog, y M-21 propuesta.

### Que se encontro
El backlog tenia la pregunta dada de alta desde el 2026-08-02 —alta #8, si el protocolo cambia la conducta del agente— y nunca se habia corrido. La mitad automatica del metodo tiene rastro de que se paga sola (M-01 encontro dos derivas reales en su primera corrida; M-09, M-10, M-13 y M-14 encontraron mas). La mitad ceremonial no tiene un solo dato a favor.

### Que cambio
Se ejecuto la **pasada 1**: solo el piso de ruido del instrumento, sin brazo tratamiento, que es lo que exige el backlog alta #7 desde B-07. El brazo control es inconstruible dentro de este repositorio —`CLAUDE.md` hace `@AGENTS.md`, y borrar los documentos daria otro repo, no el mismo repo sin protocolo—, asi que corrio sobre fixture sintetico en el repo de datos hermano `../experimentosdd-a4/`, con el precedente de `experimentosdd-b7/`.

Veredicto: **NO APTO por techo**. El brazo control dio 12/12, sobre dos versiones del fixture y tres escalones de modelo. Detalle y evidencia en `experimentos/a04-conducta-agente/RESULTADO-EXPERIMENTO-A4.md`.

### Como se valido
`./tools/check_docs.py` en verde. Los tres checks de «Propagacion» corridos con su salida, no de memoria. La prediccion fechada se escribio antes del primer rep y se contrasto despues: acerto el modo de falla (techo, no piso) y fallo el veredicto. La unica enmienda al diseño esta fechada y declarada **pre-dato**.

### Por que esto es entrada de metodo y no hallazgo de investigacion
Lo que se asienta aca es el alta de documentos y specs —cambio de registro, Principio VI—. El **hallazgo** vive en el resultado del experimento y no toca el metodo: la pasada 1 no evalua `H1` y no habilita ninguna afirmacion sobre si el protocolo funciona.

### Deuda abierta
Cinco items migrados a `agenda/BACKLOG-INVESTIGACION.md` (#9 a #13): que hace cara a una conducta para un agente moderno, si el techo es de un harness o de todos, `H1` sin evaluar, la regla de puntuacion sin ejercitar, y el regimen de permisos sin terminal. Mas M-21: `metodo-historial` sobre-dispara en altas de contenido del registro — esta misma entrada es un caso, y se acepta la friccion en vez de aflojar un verificador recien entregado.

---

## M-19 — Cablear el backstop al commit, fail-closed y versionado (2026-08-15) — COMPLETADA

**Acción**: gate de commit versionado más un check nuevo y una corrección de dos documentos, aprobada por el usuario junto con M-20. Cierra también M-07.

### Qué se encontró
El repositorio investiga gates que fallan abierto —`agenda/BACKLOG-INVESTIGACION.md` prioridad alta #4, nacido del hallazgo de B-07— y su propia verificación fallaba abierta por diseño: `tools/check_docs.py` existía desde M-01 y corría **solo si alguien se acordaba**. Nada distinguía un commit verificado de uno que nadie miró.

El cableado estaba anotado como pendiente desde M-01 con una dependencia declarada: «requiere decidir M-02 primero». La dependencia resultó **falsa**, y verlo fue la mitad del trabajo. Correr el backstop al commit es la capa 2 del enforcement de tres capas (verificar la salida); el gate de autoría `.sdd/current-doc` de M-02 es la capa 3 (autorizar la entrada). La capa 2 no necesita saber qué spec gobierna la edición. Además cubre por sí sola uno de los tres modos de falla que el análisis de sdd-first ya había documentado: la escritura por `Bash`, que escapa a todo hook `PreToolUse` y solo se atrapa al commit.

### Qué se cambió
- `tools/githooks/pre-commit`: gate versionado, activado con `git config core.hooksPath tools/githooks`. Corre `check_docs.py --staged` y bloquea el commit si hay ERROR. Tres decisiones, cada una contra un modo de falla observado: fail-closed en la resolución del intérprete, versionado en el árbol en vez de copiado a `.git/hooks/`, y heartbeat propio.
- `tools/check_docs.py`: check `gate` (ERROR). Verifica que el hook exista, que `core.hooksPath` lo apunte y que tenga permiso de ejecución — las tres formas de quedar desconectado sin aviso.
- `CONSTITUTION.md`: «Límite honesto» declara que el backstop ahora corre en cada commit, y lo que el gate igual no puede — el bypass explícito del operador.
- `AGENTS.md`: deja de decir que la verificación corre solo a pedido; el comando de instalación del gate en §Comandos útiles.
- `comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md`: la premisa «sin CI» sigue siendo cierta, pero se aclara que **sin CI dejó de significar sin verificación automática**. Con eso cierra M-07.

### Cómo se validó
- **`gate` en rojo antes de instalar.** La primera corrida, con el hook ya escrito y `core.hooksPath` sin configurar, dio `1 ERROR` con el comando de instalación en el mensaje. Tras configurarlo, verde. Es el caso del clon fresco, que es donde el gate del testigo fallaba abierto.
- **Fail-closed del hook.** Con el `PATH` conteniendo git pero ningún intérprete de Python, el hook sale 1 en vez de dejar pasar el commit — la línea exacta que en el testigo era `exit 0`.

Árbol final: `45 documentos, 42 specs — 0 ERROR, 1 WARN` (el WARN es M-08, preexistente).

### Deuda abierta
- **El gate se saltea con el flag de bypass de git**, que es la excepción de `AGENTS.md` §Excepciones ejercida a mano. Nada lo detecta ni puede detectarlo desde adentro del hook; lo que sí se detecta es la desconexión (`gate`). Un `pre-push` o un CI serían el siguiente escalón, y su criterio ya está escrito en `comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md`.
- **El gate verifica el árbol de trabajo, no el índice.** Un commit parcial puede pasar en verde con el índice en rojo. No se hizo stash/restore a propósito: es el ciclo con el que sdd-first se ganó falsos bloqueos.
- **`core.hooksPath` es config local, no versionada.** El gate se versiona; su activación no. Por eso existe el check `gate`, que convierte «no instalado» en ERROR visible en vez de silencio.
- El check `gate` no tiene regresión automatizada, igual que los de M-15, M-18 y M-20: cuarto ritual manual consecutivo, y el candidato natural a darse de alta como mejora propia.

### Planteo de la mejora, migrado de `agenda/MEJORAS-METODO.md` (2026-08-23)

Texto tal como estaba escrito en el backlog **antes** de este cierre: diagnostico, forma propuesta y reservas. Se trae aca por M-29, que deja en el backlog solo el puntero. No modifica nada de lo asentado arriba.

#### M-07 — Revisar la premisa "sin CI"

`AGENTS.md` e `comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md` describen un contexto sin CI. Sigue siendo cierto, pero desde 2026-07-31 hay git, y eso habilita `pre-commit` como sustrato tool-agnóstico para M-01 y M-02. Revisar ambos documentos cuando esas mejoras se implementen, no antes.

**Hecha el 2026-08-15**, junto con M-19.

#### M-19 — Cablear el backstop al commit, fail-closed y versionado

La incoherencia más cara del repositorio: investiga gates que fallan abierto (`BACKLOG-INVESTIGACION.md` prioridad alta #4, hallazgo de B-07) y su propia verificación fallaba abierta por diseño — `check_docs.py` corría solo si alguien se acordaba, así que nada distinguía un commit verificado de uno que nadie miró.

Contraparte de investigación: `BACKLOG-INVESTIGACION.md` alta #4 pedía «cómo detectar que un gate está caído (heartbeat / self-test)». El check `gate` es una respuesta parcial y ejecutada, no la cierra: detecta el gate desconectado, no el gate presente que no verifica lo que dice verificar.

**Hecha el 2026-08-15.** Las tres decisiones de diseño y los dos límites del gate —verifica el árbol de trabajo y no el índice, y el flag de bypass lo saltea— están declarados en `tools/githooks/pre-commit`.

---

## M-20 — Verificador ejecutable para el Principio VI (2026-08-15) — COMPLETADA

**Acción**: check nuevo más enmienda constitucional de patch (v0.2.1 → v0.2.2), aprobada por el usuario al elegir esta mejora junto con M-19.

### Qué se encontró
El segundo pendiente que M-01 dejó anotado —«un check del criterio de separación método/investigación, que hoy nada verifica»— era el `Verificador: ninguno` del Principio VI, y de los tres principios que seguían sin verificador era el único mecanizable. `AGENTS.md` §Al cerrar una iteración obliga desde siempre a asentar el cambio de método en el historial, más reciente arriba, y nada lo miraba: la separación método/contenido dependía enteramente de que el autor se acordara, que es justo lo que un principio no puede permitirse.

### Qué se cambió
- `tools/check_docs.py`: check `metodo-historial` (ERROR) y modo `--staged`. Si el commit toca método —`AGENTS.md`, `CONSTITUTION.md`, `SPECS_REGISTRY.md`, `CLAUDE.md`, `templates/`, `tools/`— entonces el historial MUST traer una entrada nueva y MUST quedar arriba. `agenda/` no dispara a propósito: proponer una mejora no es adoptarla, y el historial asienta adopciones. `tools/` sí dispara, porque cambiar el verificador de un principio es cambiar el método tanto como cambiar el principio.
- `CONSTITUTION.md` v0.2.2: Principio VI pasa de `ninguno` a `metodo-historial`, con la nota de qué mitad queda sin cubrir; «Límite honesto» actualizado a cinco de siete.

### La decisión que había que tomar
M-18 dejó escrito que M-16 estaba «bloqueada por la decisión de si el backstop puede depender de git». La respuesta que M-20 fija: **puede, en un modo opcional que degrada**. `--staged` suma los checks con contexto de commit; sin git el script sigue corriendo entero salvo esos, y el principio vuelve a no tener verificador — lo cual queda declarado en su propio campo `Verificador:` en vez de ser una sorpresa. Con eso **M-16 se desbloquea**.

### Cómo se validó
Tres deformaciones deliberadas sobre el índice, una por decisión de diseño: con `tools/check_docs.py` en el índice y el historial fuera, falla nombrando los archivos de método tocados; con el historial en el índice pero sin encabezado de entrada nuevo, falla distinto; con la entrada agregada al final en vez de arriba, falla por posición y cita cuál sigue siendo la primera. Árbol restaurado y 0 ERROR.

### Deuda abierta
- El check verifica que la entrada exista y quede arriba, **no que clasifique bien**. Que un cambio sea método y no hallazgo, y la dirección simétrica del principio —que un hallazgo no mueva el método sin decisión explícita y fechada—, siguen siendo juicio humano.
- Quedan **III y V** sin verificador. III (M-16) ya no está bloqueada. V —el sellado experimental— es una promesa sobre el orden entre pensar y ver, y sigue sin observador mecánico posible.

### Planteo de la mejora, migrado de `agenda/MEJORAS-METODO.md` (2026-08-23)

Texto tal como estaba escrito en el backlog **antes** de este cierre: diagnostico, forma propuesta y reservas. Se trae aca por M-29, que deja en el backlog solo el puntero. No modifica nada de lo asentado arriba.

#### M-20 — Verificador del Principio VI

El Principio VI declaraba `Verificador: ninguno` con el diagnóstico escrito desde M-01: «un check del criterio de separación método/investigación quedó pendiente y sigue sin darse de alta». `AGENTS.md` §Al cerrar una iteración obliga desde siempre a asentar el cambio de método en el historial, más reciente arriba, y nada lo miraba.

**Hecha el 2026-08-15.** Decidió de paso lo que M-18 había dejado abierto —que el backstop MAY depender de git, en un modo opcional que degrada— y con eso **M-16 quedó desbloqueada**.

---

## M-18 — Ningún documento `Activo` conserva un `[NEEDS CLARIFICATION]` abierto (2026-08-15) — COMPLETADA

**Acción**: check nuevo en el backstop más enmienda constitucional de patch (v0.2.0 → v0.2.1), aprobada por el usuario al elegir esta mejora sobre el resto del backlog.

### Qué se encontró
M-15 había cerrado el mismo día dejando cuatro principios con `Verificador: ninguno`, y el de VII venía con su propio diagnóstico escrito: el marcador `[NEEDS CLARIFICATION]` es grep-able desde que se adoptó de Spec Kit [R10], el registro declara `estado` por documento desde el principio, y nadie había cruzado las dos cosas. `AGENTS.md` §Disambiguación obliga a resolver el marcador antes de considerar el documento `Activo`; hasta acá solo se verificaba la mitad barata —que el marcador se pudiera encontrar—, no la que importa.

### Qué se cambió
- `tools/check_docs.py`: check `clarificacion` (ERROR). Un documento cuya spec declara `Activo` —incluido el default de no escribir el campo— no puede conservar un marcador con su pregunta escrita. Los bloques de código se ignoran; los spans inline **no**, porque un marcador vivo entre backticks sigue abierto.
- `CONSTITUTION.md` v0.2.1: Principio VII pasa de `ninguno` a `clarificacion`, con la nota de qué mitad del principio queda sin cubrir; «Límite honesto» actualizado a cuatro de siete.
- `AGENTS.md`: las dos afirmaciones sobre lo que cubre el backstop.
- `agenda/MEJORAS-METODO.md`: M-18 dada de alta y cerrada; el párrafo de resultado de M-15 lleva una nota de actualización en vez de reescribirse.

### Calibración, que fue el trabajo real
El corpus menciona la convención en unos treinta lugares y no tiene ni un marcador vivo, así que el riesgo entero del check era el falso positivo. El discriminante elegido es la pregunta: un marcador trae `:` y texto propio; las menciones traen elipsis o el metavariable entre ángulos. Se verificó sobre las ocho formas con `:` presentes en el árbol, todas placeholders.

### Cómo se validó
Cinco deformaciones deliberadas, cada una probando una decisión de diseño distinta: marcador vivo en documento `Activo` (detectado), el mismo entre backticks (detectado — los backticks no eximen), marcador dentro de un bloque de código (no detectado, es ejemplo citado), marcador vivo en un documento `Borrador` (no detectado, ahí es legítimo), y el check renombrado en el script (detectado por `constitucion`, que es el lazo de M-15 cerrándose sobre la declaración nueva). Árbol restaurado y `python3 tools/check_docs.py` → `45 documentos, 42 specs — 0 ERROR, 1 WARN` (el WARN es M-08, preexistente).

### Deuda abierta
- **Hueco conocido y declarado**: los documentos exentos de spec (`EXPERIMENTO-*`, `RESULTADO-EXPERIMENTO-*`) no tienen `estado` que consultar y quedan fuera, justo donde los marcadores reales más aparecen. Cerrarlo exige decidir antes qué significa `Activo` para un documento exento — pregunta sobre el registro, no sobre el check.
- El check no observa el caso en que se interpretó en silencio y nunca hubo marcador. Es la mitad que `agenda/BACKLOG-INVESTIGACION.md` prioridad alta #8 propone medir sobre conducta.
- Quedan III, V y VI sin verificador. El más accionable sigue siendo III (M-16), bloqueado por la decisión de si el backstop puede depender de git.

### Planteo de la mejora, migrado de `agenda/MEJORAS-METODO.md` (2026-08-23)

Texto tal como estaba escrito en el backlog **antes** de este cierre: diagnostico, forma propuesta y reservas. Se trae aca por M-29, que deja en el backlog solo el puntero. No modifica nada de lo asentado arriba.

#### M-18 — Ningún documento `Activo` conserva un `[NEEDS CLARIFICATION]` abierto

Origen: el resultado de M-15, que dejó al Principio VII declarando `Verificador: ninguno` con esta frase — «el marcador es grep-able, pero nada verifica que se haya resuelto antes de declarar un documento activo». Las dos piezas necesarias ya existían por separado: el marcador es grep-able desde que se adoptó de Spec Kit [R10], y el registro ya declara `estado` por documento. La mejora es cruzarlas.

**Hecha el 2026-08-15.** Los dos límites del check —qué cuenta como marcador, y los documentos exentos de spec que quedan fuera justo donde más marcadores aparecen— están declarados en `tools/check_docs.py` y no se reproducen acá.

Lo que el check **no** cubre del principio: el caso en que el asistente interpretó en silencio y nunca hubo marcador. Eso sigue sin observador mecánico, y es la mitad que la contraparte de investigación mide sobre conducta (`BACKLOG-INVESTIGACION.md` prioridad alta #8).

---

## M-15 — Cada principio declara un verificador ejecutable, o declara que no tiene (2026-08-15) — COMPLETADA

**Acción**: enmienda constitucional (v0.1.0 → v0.2.0) más un check nuevo, aprobada por el usuario tras el análisis de sdd-first.

### Qué se encontró
Los siete principios declaraban `Enforcement:` y los siete nombraban prosa: «revisión editorial», «checks de post-generación de `AGENTS.md`», «campo `validacion` de cada spec». `tools/check_docs.py` existía desde M-01 y cubría parte de eso, pero ningún principio lo nombraba: nada distinguía un principio con mecanismo de uno que depende de que alguien se acuerde. Origen del patrón: sdd-first [R39] SPEC-020, que nació al descubrir que declarar un principio nuevo producía «enforcement decorativo» sin aviso (`software/analisis/ANALISIS-SDD-FIRST.md`, C1).

Además, `AGENTS.md` afirmaba que el repositorio no tenía verificación determinista — falso desde el 2026-07-31 y en contradicción con su propia §Al cerrar una iteración, que obliga a correr el backstop.

### Qué se cambió
- `CONSTITUTION.md` v0.2.0: campo `Verificador:` en los siete principios, con nota de alcance cuando la cobertura es parcial; §Alcance del preámbulo lo declara; «Límite honesto» reescrito con el estado real (tres de siete cubiertos, ninguno juzga adecuación) en vez de la afirmación global anterior.
- `tools/check_docs.py`: check `constitucion` (ERROR) — falla si un principio no declara el campo, si declara `ninguno` y checks a la vez, o si nombra un check que el script no emite. Los ids válidos se derivan de la fuente del propio script; solo se leen como declaración los nombres anteriores al em dash, para que la nota de alcance sea prosa libre.
- `AGENTS.md`: premisa corregida y el nuevo check agregado a lo que cubre el backstop.
- `SPECS_REGISTRY.md`: la spec de `CONSTITUTION.md` incorpora el campo en `incluye` y un ítem de `validacion`.
- `agenda/MEJORAS-METODO.md`: M-15 pasa a **Hecha**, con el resultado de la primera pasada.

### Resultado, que es el dato que la mejora buscaba
**Tres de siete principios tienen verificador, uno solo de forma sustantiva.** I y II quedan parciales; IV es el único bien cubierto. III, V, VI y VII declaran `ninguno`. El campo no mecaniza nada nuevo: hace visible qué parte del método se sostiene sola y cuál no.

### Cómo se validó
Se corrió el check en rojo antes de escribir el campo (7 ERROR, uno por principio) y contra dos deformaciones deliberadas —un check inexistente y el campo renombrado—, ambas detectadas. Árbol restaurado y `python3 tools/check_docs.py` → `45 documentos, 42 specs — 0 ERROR, 1 WARN` (el WARN es M-08, preexistente).

### Deuda abierta
- Cuatro principios sin verificador. El más accionable es III, que es M-16.
- M-07 avanza pero no cierra: `AGENTS.md` quedó corregido, `comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md` sigue pendiente.
- El check verifica que el verificador **exista**, no que **alcance**: que `spec-coverage` baste para sostener el Principio IV sigue siendo juicio humano.

### Planteo de la mejora, migrado de `agenda/MEJORAS-METODO.md` (2026-08-23)

Texto tal como estaba escrito en el backlog **antes** de este cierre: diagnostico, forma propuesta y reservas. Se trae aca por M-29, que deja en el backlog solo el puntero. No modifica nada de lo asentado arriba.

#### M-15 — Cada principio declara un verificador ejecutable, o declara que no tiene

Los siete principios de `CONSTITUTION.md` declaran `Enforcement:` y los siete nombran prosa: «checks de post-generación de `AGENTS.md`», «revisión editorial», «campo `validacion` de cada spec». `tools/check_docs.py` existe y cubre parte de eso, pero ningún principio lo nombra y nada verifica que la relación entre principio y verificador sea otra cosa que una intención escrita.

Propuesta: que cada principio nombre el check de `check_docs.py` que lo cubre, o `ninguno` cuando nada lo cubra, y que `check_docs.py` verifique que los nombrados existen. Lo que produce no es enforcement universal —un repositorio documental sin CI no puede mecanizar «no formular una hipótesis después de ver el resultado»— sino **visibilidad de qué principio tiene mecanismo y cuál depende de que alguien se acuerde**.

Origen: sdd-first [R39] declara ese vínculo en el config y verifica que el paso esté cableado y haya corrido; su SPEC-020 nació justamente al descubrir que un principio nuevo obtenía «enforcement decorativo» sin aviso (`software/analisis/ANALISIS-SDD-FIRST.md` C1). Contraparte de investigación: `BACKLOG-INVESTIGACION.md` prioridad alta #4 (gates que fallan abierto) y #3 (umbral de control manual a automatizado).

**Hecha el 2026-08-15.** Qué principio tiene verificador hoy y cuál declara `ninguno` se lee en `CONSTITUTION.md`, campo `Verificador:`; este backlog no lo reproduce, porque el conteo cambia cada vez que se cierra una mejora.

---

## Incorporación de sdd-first al corpus como caso del propio linaje (2026-08-15) — COMPLETADA

**Acción**: alta de una fuente nueva en `fuentes-externas/` (enlace `sdd-first`, agregado por el usuario) y su análisis con el mismo instrumento que Spec Kit, Superpowers y OpenSpec.

### Qué se encontró
sdd-first ([R39], commit `ebfbd67`) **no pasa el filtro de procedencia** de `software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md`: es del mismo autor, generaliza el tooling del testigo (`check_traceability.py`, `sdd_gate.py`, `check_constitution.py` son los scripts que M-01 y M-02 registran con origen «testigo») y arrastra vocabulario nacido acá (`[SDD-Check]`, el par `hibrido`/`casero` de B-07, la forma de principio de `CONSTITUTION.md`) más la difusión desde Spec Kit ya declarada (`analyze`, `clarify`). No suma linaje y el conteo sigue en cuatro. Su valor es otro: es el único caso donde este método está ejecutado por código de punta a punta, incluidos mecanismos que acá son prosa y uno que acá ya falló — la prioridad alta #4 del backlog (gate fail-open silencioso durante todo B-07) está pagada allá en ingeniería.

Hallazgo con consecuencia inmediata: el chequeo de **mtime** que M-02 daba por diseño se implementó en esa fuente y falló en las dos direcciones (bloqueó flujo legítimo, y un `touch` lo satisfacía). Implementar M-02 como estaba escrito era repetir un error ya pagado.

### Qué se cambió
- `REFERENCIAS.md`: alta de [R39], con versión anclada, naturaleza declarada (repositorio propio, no fuente externa; MUST NOT contarse como linaje ni citarse como evidencia) y reserva de vendorizado (el enlace apunta a un directorio de trabajo vivo, no a un snapshot).
- `software/analisis/ANALISIS-SDD-FIRST.md`: documento nuevo, con la procedencia resuelta antes de la lectura, el mapeo sobre el instrumento v1 sin filas nuevas y seis conclusiones marcadas como lectura o candidata (ninguna aprobada).
- `SPECS_REGISTRY.md`: spec del documento nuevo, con validación explícita de que ninguna coincidencia se presente como convergencia.
- `software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md`: fila de procedencia que registra el caso como **No** — primer rechazo escrito de la regla 1, anotado para que el corolario «la mayoría de los métodos nuevos no suman linaje» sea verificable. Ningún veredicto por fila cambia.
- `agenda/MEJORAS-METODO.md`: M-02 incorpora la corrección de diseño (mtime descartado, criterio de contenido en su lugar, tres modos de falla adicionales); alta de M-15, M-16 y M-17 en estado `Propuesta`.
- `software/00-INDEX.md`: puntero al análisis nuevo.

### Cómo se validó
`python tools/check_docs.py` — 0 ERROR (ver corrida al cierre de la iteración).

### Deuda abierta
- M-15, M-16 y M-17 quedan en `Propuesta`, sin aprobación del usuario.
- Por qué el kit dejó caer `[NEEDS CLARIFICATION]` no está declarado en la fuente y el análisis no lo resuelve.
- La deuda previa de `CONVERGENCIA-IMPLEMENTACIONES-SDD.md` sigue intacta: Kiro sin leer, dimensión «cómo llega el método al agente» sin veredicto, corpus observacional de OpenSpec sin dar de alta.

---

## M-14 — Índices de línea duplicaban `proposito`/`estado` fuera del registro (2026-08-03) — COMPLETADA

**Acción**: auditoría de coherencia (usuario + asistente) sobre la tabla SSOT y las specs, disparada por revisión manual del proyecto.

### Qué se encontró
`software/00-INDEX.md` anotaba "Estado: Borrador" junto al link a `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md`, mientras `SPECS_REGISTRY.md` declara `estado: Activo` para ese documento desde el 2026-06-06 (vía confirmada y ejecutada). Contradicción directa entre un índice operativo y su SSOT. Causa raíz: la spec de `docs-y-investigacion/00-INDEX.md` y `software/00-INDEX.md` no prohibía explícitamente parafrasear `proposito` ni anotar `estado` junto a cada link — a diferencia de la regla ya vigente para el `00-INDEX.md` de raíz, que exige tabla de rol en vez de propósito. Las descripciones de `software/00-INDEX.md` §Análisis de frameworks también parafraseaban de cerca el `proposito` registrado de cada documento enlazado (ej. `ANALISIS-SPEC-KIT.md`).

### Qué se cambió
- `SPECS_REGISTRY.md`: spec de `docs-y-investigacion/00-INDEX.md` y `software/00-INDEX.md` suma `excluye` (ni `proposito` parafraseado ni `estado` anotado junto a cada link — ambos viven solo en el registro) y dos ítems de `validacion` que lo verifican.
- `software/00-INDEX.md`: descripciones de §Análisis de frameworks y §Análisis temáticos recortadas a punteros breves (qué tipo de contenido es, no qué dice); quitadas las dos anotaciones de `Estado` (`DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` y `SDD-EN-LEGACY-Y-BROWNFIELD.md`).
- `docs-y-investigacion/00-INDEX.md` no requirió cambios de contenido — ya era una lista sin descripciones ni estado.

### Cómo se validó
`python tools/check_docs.py` — `44 documentos, 41 specs — 0 ERROR, 1 WARN` (el WARN es el de emoticones de `PREREG-B7.md`, preexistente y sin relación — M-08).

### Deuda abierta
- M-05 y M-08 siguen abiertas como prioridades baja.

### Planteo de la mejora, migrado de `agenda/MEJORAS-METODO.md` (2026-08-23)

Texto tal como estaba escrito en el backlog **antes** de este cierre: diagnostico, forma propuesta y reservas. Se trae aca por M-29, que deja en el backlog solo el puntero. No modifica nada de lo asentado arriba.

#### M-14 — Índices de línea duplicaban `proposito`/`estado`

Una auditoría de coherencia encontró que `software/00-INDEX.md` anotaba "Estado: Borrador" para `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` mientras el registro ya declaraba `estado: Activo` desde el 2026-06-06 — contradicción directa entre el índice y su SSOT. Causa raíz: la spec de los dos índices de línea no prohibía explícitamente que las descripciones junto a cada link parafrasearan el `proposito` registrado ni que anotaran `estado`, a diferencia de la regla ya vigente para el `00-INDEX.md` de raíz.

**Hecha el 2026-08-03.** Es el antecedente directo de M-28, que veinte días después generalizó la prohibición a todo documento.

---

## M-13 — `deriva_de` apunta a documentos que no son SSOT (2026-08-03) — COMPLETADA

**Acción**: relevamiento completo de las 7 specs vigentes con `ssot_level: derivado` (disparado al decidir la naturaleza de `CONVERGENCIA-IMPLEMENTACIONES-SDD.md` el 2026-08-02), y resolución combinando reclasificación de origen, alta de spec faltante y una regla nueva sobre `deriva_de`.

### Qué se encontró
Las 7 specs `derivado` vigentes violaban la definición literal ("`deriva_de` apunta al SSOT de origen") en tres patrones: (1) destino declarado `operativo` — `COMPARATIVA-SPECKIT-VS-TESTIGO.md` y `RELACION-FR-VS-SC-Y-COBERTURA.md`, ambos apuntando a `ANALISIS-SPEC-KIT.md`; (2) derivado-de-derivado — `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` → `COMPARATIVA-SPECKIT-VS-TESTIGO.md` y `PREREG-B7.md` → `PRUEBA-REGENERABILIDAD-B7.md`; (3) destino sin entrada en el registro — `PRUEBA-REGENERABILIDAD-B7.md` y `PRUEBA-OBSERVACIONAL-B7.md`, ambos apuntando a `EXPERIMENTO-B7-formato-hibrido.md`, exento de spec por generarse desde template.

Un octavo caso (`RELACION-SPEC-VS-EPICA.md` → `ANALISIS-SPEC-KIT.md`) resultó ser un error de modelado distinto: a diferencia de los otros, su contenido no sintetiza `ANALISIS-SPEC-KIT.md` — es un análisis paralelo con evidencia externa propia, forzado a "derivar" de algo con lo que no tiene relación real. Se corrigió aparte, quitándole `deriva_de` y dejándolo `operativo` independiente, antes de decidir la regla general.

### Qué se cambió
- `SPECS_REGISTRY.md` §Campo ssot_level: `deriva_de` ya no exige que el origen sea `SSOT` — MUST ser `SSOT` o `derivado` (permite cadena de más de un salto), nunca `operativo` ni un documento sin entrada. Se documentó el criterio para distinguir cadena legítima (cada eslabón declara una faceta distinta: qué/cómo/valores) de mal modelado (forzar una relación para evitar clasificar el rol real).
- `SPECS_REGISTRY.md` §Docs excluidos: excepción nueva — un `EXPERIMENTO-*.md` citado como `deriva_de` por otro documento MUST tener entrada mínima en el registro (conserva la exención de `incluye`/`excluye` detallados).
- `software/analisis/ANALISIS-SPEC-KIT.md` reclasificado de `operativo` a `SSOT` (resuelve 2 de los 7 casos) y sumado a la Tabla SSOT.
- Alta de `experimentos/b07-formato-hibrido/EXPERIMENTO-B7-formato-hibrido.md` en el registro, `ssot_level: SSOT`, entrada mínima por la excepción nueva (resuelve otros 2 casos) y sumado a la Tabla SSOT.
- Los 2 casos de derivado-de-derivado quedan cubiertos por la regla de cadena, sin tocar sus specs.
- `tools/check_docs.py`: `check_spec_fields` ahora valida que el destino de `deriva_de` tenga spec registrada y `ssot_level` en `{SSOT, derivado}`, no solo que exista en disco y no cicle.

### Cómo se validó
`python tools/check_docs.py` — `44 documentos, 41 specs — 0 ERROR, 1 WARN` (el WARN es el de emoticones de `PREREG-B7.md`, preexistente y sin relación — M-08).

### Deuda abierta
- M-05 y M-08 siguen abiertas como prioridades baja y media.
- La excepción de entrada mínima para `EXPERIMENTO-*.md` es puntual (M-13); si aparecen más casos de documentos exentos de spec citados como origen, revisar si conviene generalizarla en vez de repetirla caso a caso.

### Planteo de la mejora, migrado de `agenda/MEJORAS-METODO.md` (2026-08-23)

Texto tal como estaba escrito en el backlog **antes** de este cierre: diagnostico, forma propuesta y reservas. Se trae aca por M-29, que deja en el backlog solo el puntero. No modifica nada de lo asentado arriba.

#### M-13 — `deriva_de` apunta a documentos que no son SSOT

De 7 specs `derivado` vigentes, 6 violaban la definición literal de `deriva_de` en tres patrones —destino `operativo`, derivado-de-derivado, destino sin entrada— y la séptima (`RELACION-SPEC-VS-EPICA.md`) resultó ser un error de modelado distinto: relación forzada, no síntesis real. Emparentada con M-11, que también toca coherencia del registro contra sí mismo.

**Hecha el 2026-08-03.** La regla vigente —origen `SSOT` o `derivado`, nunca `operativo` ni sin registrar, con cadena permitida bajo condición— vive en `SPECS_REGISTRY.md`, campo `deriva_de`.

---

## Fase 13 — Higiene de archivo y validación de SSOTs, M-11 y M-12 (2026-08-03) — COMPLETADA

**Acción**: implementar la verificación mecánica de la higiene de los archivos (fines de línea, BOM y saltos de línea finales) y la validación cruzada de la tabla de SSOT contra las existencias en el disco y las declaraciones en el registro.

### Qué se agregó
Dos funciones de verificación (`check_file_hygiene` y `check_ssot_table`) integradas al script base `tools/check_docs.py`:
- **`higiene` (ERROR)**: Valida la ausencia de firmas BOM invisibles (requiere UTF-8 puro), prohíbe el uso de CRLF (para uniformidad en el control de cambios de git independientemente de la plataforma) y requiere que todo archivo con contenido termine con un salto de línea limpio (`\n`). Cada validación emite mensajes resolubles y accionables.
- **`ssot-table` (ERROR)**: Protege la cadena de SSOT, validando que todo documento declarado como central (`SSOT`) en la tabla exista físicamente en su ruta y cuente con su especificación en `SPECS_REGISTRY.md`. 
- Se realizó una mejora de plataforma cruzada en el `main()` de `check_docs.py` para garantizar que la salida estándar use `UTF-8` en entornos donde la consola de Windows utiliza `cp1252`, e instruir a la resolución de referencias saltarse paths a `fuentes-externas/` que causan falsos positivos en el sistema operativo.

### Cómo se validaron y qué encontraron
Durante la primera ejecución, casi la totalidad del repositorio (45 archivos) emitió alarmas de `ERROR [higiene]... tiene finales de linea CRLF`.
Para reparar el problema sin recurrir a modificaciones manuales propensas al error y dejar el proyecto saneado, se empleó un comando que reemplazó masivamente todo `\r\n` por `\n` en los archivos marcados por el script.

En la segunda ejecución luego del proceso de saneado, los verificadores retornaron un paso exitoso: `44 documentos, 40 specs — 0 ERROR, 1 WARN` confirmando la validez del instrumento y la nueva sanidad del proyecto.

### Deuda abierta
- **El script base sigue careciendo de test automatizados y funcionales.** Se planteó explícitamente agregar `pytest` a su desarrollo o un comando en la bandera `--selftest`, pero por economía en esta fase se optó por respetar su alcance y postergar esta iniciativa como ticket nuevo.
- M-05, M-08 y M-13 siguen abiertas como prioridades medias y bajas.

### Planteo de la mejora, migrado de `agenda/MEJORAS-METODO.md` (2026-08-23)

Texto tal como estaba escrito en el backlog **antes** de este cierre: diagnostico, forma propuesta y reservas. Se trae aca por M-29, que deja en el backlog solo el puntero. No modifica nada de lo asentado arriba.

#### M-11 — Validar la tabla SSOT

El registro declara una tabla SSOT y nada verificaba su coherencia contra el disco ni contra las specs. Emparentada con M-13, que también toca coherencia del registro contra sí mismo.

**Hecha el 2026-08-03**, junto con M-12: `tools/check_docs.py` asegura que los paths de la tabla existan en disco y coincidan con un `path` registrado.

#### M-12 — Higiene de archivo

CRLF mezclado, BOM y ausencia de newline final. Origen concreto: en la Fase 11 un barrido de referencias convirtió CRLF a LF en `docs-y-investigacion/GUIA-INICIO-PROYECTO-INVESTIGACION.md`, único archivo del repo con ese final de línea, inflando su diff de 3 a 418 líneas. Se detectó por el diffstat, no por el backstop.

**Hecha el 2026-08-03**, junto con M-11.

---

## Fase 12 — El backstop aprende a ver duplicación y rutas, M-09 y M-10 (2026-07-31) — COMPLETADA

**Acción**: cerrar los dos huecos que la Fase 11 dejó documentados. Los dos casos serios de duplicación que esa fase corrigió habían pasado los ocho checks existentes sin ruido, y `check_links` solo miraba links markdown mientras el repositorio referencia sobre todo con backticks.

### Qué se agregó
Tres checks nuevos (10 en total) y una corrección:
- `ssot-collision` (WARN): cruza el concepto de cada fila de la tabla SSOT contra las viñetas de `incluye` de las demás specs.
- `normative-block` (WARN): detecta la definición del bloque `[SDD-Check]` reproducida fuera de `AGENTS.md`, distinguiendo *instancia* —una entrega que cierra con el bloque lleno, legítima en cualquier documento— de *definición*.
- `rutas` (ERROR): resuelve las rutas escritas en backticks, con la regla de cuatro casos de M-10.
- `check_links` corregido: ignoraba bloques y spans de código, así que marcaba como roto cualquier ejemplo de sintaxis markdown citado en prosa. Lo detectó el propio checker sobre el texto de M-10, que cita esa sintaxis.

### Cómo se validaron
No alcanza con que un check esté en verde: hay que probar que **detecta lo que dice detectar**. Se creó un worktree temporal en el commit anterior a la Fase 11, se copió el script nuevo sobre ese árbol viejo y se corrió: `ssot-collision` reprodujo el caso D1 en sus dos filas —líneas A y B— y `normative-block` reprodujo el D2. Sin esa prueba, dos checks que no encuentran nada son indistinguibles de dos checks rotos.

### Qué encontraron en el árbol actual
Dos hallazgos vivos en la primera corrida, ambos corregidos en la misma entrega:
- **`docs-y-investigacion/PLAN-PRUEBAS.md` A-02 reproducía los cuatro campos del bloque `[SDD-Check]`** — el hermano exacto del caso D2, en un documento que la auditoría manual de la Fase 11 no había mirado. La auditoría humana recorrió la raíz; este estaba en una línea.
- **`agenda/BACKLOG-INVESTIGACION.md` citaba `../investigaIA/...`**, ruta correcta mientras el archivo vivía en la raíz y falsa desde que la Fase 11 lo bajó un nivel. El barrido de referencias de esa fase no podía verlo: solo reescribía nombres de archivos movidos, no rutas cuyo significado cambia al mover el archivo que las contiene. Una reorganización rompe dos clases de referencia, y la Fase 11 solo trató una.

Calibración: la ventana hacia atrás de `normative-block` pasó de 6 a 20 líneas —un bloque lleno tiene ocho campos y los últimos quedaban fuera del alcance del literal `[SDD-Check]`— y `resolve_ref` ganó un cuarto caso, la ruta relativa que sale de la raíz y apunta a un repositorio hermano.

### Deuda abierta
- **M-11 y M-12 quedan diferidas** y aprobadas: validar la tabla SSOT contra el disco, e higiene de archivo (CRLF, BOM, newline final).
- El script sigue **sin tests propios**. La Fase 10 ya había afinado la heurística de precedencia contra tres falsos positivos y hoy se calibró `normative-block` contra siete; ninguna de esas calibraciones está protegida contra regresión. La técnica del worktree histórico funcionó bien y es la base natural de un `--selftest`, pero no se implementó.
- `ssot-collision` solo mira el campo `incluye` de las specs. Una duplicación entre dos documentos cuyas specs no la declaran —el caso más probable, porque nadie escribe en la spec que va a duplicar— se le escapa entera.
- M-05 y M-08 siguen abiertas desde fases anteriores.

### Planteo de la mejora, migrado de `agenda/MEJORAS-METODO.md` (2026-08-23)

Texto tal como estaba escrito en el backlog **antes** de este cierre: diagnostico, forma propuesta y reservas. Se trae aca por M-29, que deja en el backlog solo el puntero. No modifica nada de lo asentado arriba.

#### M-09 — Señales de duplicación entre SSOTs

Dos checks nuevos en el backstop, ambos WARN, ambos originados en la Fase 11: los dos casos serios de duplicación que esa fase corrigió habían pasado los ocho checks existentes sin ruido.

- `ssot-collision`: cruza la columna *Concepto* de la tabla SSOT contra los campos `incluye` de las demás specs. Detecta que dos specs se declaren dueñas del mismo tema. Habría señalado el caso D1 (la spec de `comun/MARCO-COMPARATIVO-DOS-LINEAS.md` declaraba `incluye: metricas por linea` mientras la tabla SSOT asignaba esas métricas a los dos `NECESIDADES-Y-METRICAS.md`).
- `sdd-check-fields` (así desde M-24; se llamó `normative-block` hasta el 2026-08-23): detecta que la definición de un bloque normativo —hoy el `[SDD-Check]`, cuyo SSOT es `AGENTS.md`— se reproduzca enumerada fuera de su SSOT. Distingue *instancia* de *definición*: una entrega que cierra con el bloque lleno es legítima en cualquier documento; lo que no lo es, es listar los campos como definición. Habría señalado el caso D2.

**Límite: son señales para revisión humana, no veredictos.** El script conserva su límite declarado —presencia y forma, no adecuación— y por eso los dos checks emiten WARN: marcan candidatos a mirar, no violaciones probadas. Ampliar el límite del script a *adecuación* sería otra decisión y no se toma acá.

**Hecha el 2026-07-31.**

#### M-10 — Verificar rutas escritas en backticks

`check_links` valida solo la sintaxis markdown `[texto](destino.md)`, pero este repositorio referencia sobre todo con backticks (`` `comun/X.md` ``). Esas rutas no se verificaban, así que la reorganización de la Fase 11 pudo haber dejado referencias muertas sin que el backstop dijera nada.

Regla de resolución en tres casos, elegida para no producir falsos positivos con el proyecto testigo, cuya estructura de directorios es homónima de la nuestra:

1. Ruta con prefijo relativo explícito (``, `./`): se resuelve contra el directorio del documento. Es intención de navegación inequívoca.
2. Ruta cuyo primer segmento es un directorio **de este repositorio**: se resuelve contra la raíz.
3. Cualquier otro primer segmento (`docs/`, `specs/`, `memory/`, `.b7/`): es de otro repositorio, se ignora.

Un backtick sin barra es una mención por nombre, no una ruta, y no se verifica.

Se agregó un cuarto caso durante la implementación: una ruta relativa que **sale de la raíz** apunta a un repositorio hermano y tampoco se verifica.

**Hecha el 2026-07-31.**

---

## Fase 11 — Deduplicación de SSOT y reorganización de la raíz (2026-07-31) — COMPLETADA

**Acción**: auditar los 16 `.md` de la raíz buscando contenido duplicado entre SSOTs y agrupar la raíz por naturaleza. Detonante: la raíz mezclaba cinco naturalezas distintas (gobernanza, contenido común, operativos, backlogs, registro histórico) en un solo nivel, mientras las dos líneas sí tenían directorio propio.

### Duplicación encontrada y corregida

- **Métricas por línea, con dos SSOT declarados a la vez.** La spec de `comun/MARCO-COMPARATIVO-DOS-LINEAS.md` declaraba `incluye: metricas por linea`, pero la tabla SSOT asignaba las métricas de cada línea a su `NECESIDADES-Y-METRICAS.md`. El solapamiento medido era de 3 de 4 métricas en línea A y 3 de 4 en línea B, más las listas de necesidades (4 de 5 casi literales en B) y de riesgos. `MARCO` quedó reducido a la tabla de eje diferencial —objetivo, artefactos, familia de métricas— y remite al SSOT de cada lado. Antes de borrar se migraron los dos ítems que **no** tenían contraparte en destino: «consistencia terminológica sostenida por SSOT único» y la métrica «tiempo de localización de evidencia», ambos a `docs-y-investigacion/NECESIDADES-Y-METRICAS.md`.
- **Bloque de salida del asistente, con deriva ya consumada.** `comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md` reproducía cuatro campos del `[SDD-Check]`, cuyo SSOT es `../AGENTS.md`, y la copia estaba vieja: le faltaban `Cobertura`, `Deuda arrastrada` y `Riesgos/reservas`. Es el mismo modo de fallo que la Fase 8 midió en `00-INDEX.md`, en un documento que nadie había mirado. Reemplazado por referencia.
- **Navegación triplicada.** El mismo conjunto de documentos vivía en `README.md` §Estructura, en la ruta de lectura de `00-INDEX.md` y en su tabla de estructura, y ya había divergido: el README omitía `experimentos/`, `templates/`, `tools/`, `CLAUDE.md` y `AGENTS.md`, y presentaba el roadmap cerrado al mismo nivel que los SSOT vivos. El README pasó a ser lo que su spec siempre dijo —entrada humana y breve— y delega el listado en el índice; `00-INDEX.md` fusionó ruta y estructura en una tabla con orden, link y rol, más una segunda tabla disjunta con el resto.
- **Criterio de separación método/investigación**, enunciado dos veces: `agenda/BACKLOG-INVESTIGACION.md` parafraseaba la tabla de `agenda/MEJORAS-METODO.md`. Reducido a una línea con puntero.

### Reorganización

`comun/` (seis SSOT transversales), `agenda/` (los dos backlogs vivos) y el roadmap cerrado a `historial/`. El prefijo `06-` era vestigio de una numeración 01–05 inexistente: `06-BACKLOG-INVESTIGACION-FUTURA.md` pasó a `agenda/BACKLOG-INVESTIGACION.md`. La raíz quedó con gobernanza y entrada: constitución, registro, protocolo, adaptador, README, índice y referencias.

### Cómo se validó
`tools/check_docs.py` en verde (0 ERROR, 1 WARN — el de M-08) antes de cada uno de los tres commits. Además, dos barridos escritos para esta fase: uno que resuelve todo link markdown contra el filesystem (0 rotos sobre 41 documentos) y otro que verifica que cada `path` del registro existe. La reescritura masiva de referencias reveló un efecto colateral que hay que anotar: el script convirtió CRLF a LF en `docs-y-investigacion/GUIA-INICIO-PROYECTO-INVESTIGACION.md`, único archivo del repo con ese final de línea, inflando su diff de 3 a 418 líneas; se restauró antes de commitear. Un barrido mecánico sobre documentos puede cambiar cosas que el backstop no mira.

### Deuda abierta
- **M-05 sigue abierta**: `comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md` conserva el encabezado que restata su alcance. Se tocaron sus referencias, no su encabezado; la limpieza oportunística no se aplicó.
- **M-08 sigue abierta** (emoticones de `PREREG-B7.md`), único WARN vivo.
- El backstop **no detecta esta clase de duplicación**: los dos casos serios de hoy —dos SSOT para el mismo tema y una copia derivada de un bloque normativo— pasaron sus ocho checks sin ruido. Verifica presencia y forma; el solapamiento semántico entre SSOTs sigue siendo trabajo humano. Candidato a mejora de método, no dado de alta todavía.
- `comun/` no tiene `00-INDEX.md` propio, a diferencia de las dos líneas. Se decidió no crearlo para no agregar superficie de navegación; si `comun/` crece, revisar.

---

## Fase 10 — Backstop determinista de documentación, M-01 (2026-07-31) — COMPLETADA

**Acción**: implementar la primera capa de verificación mecánica del repositorio, portando a un repo documental la capa 2 del enforcement de tres capas del testigo (`docs/SDD-ENFORCEMENT.md`).

### Qué hace
`tools/check_docs.py`, stdlib pura, dos severidades (ERROR falla; WARN informa, o falla con `--strict`). Ocho checks: cobertura de spec con exenciones declaradas; el registro no apunta a archivos inexistentes; links internos; `[Rxx]` usadas contra el catálogo y sin duplicados; valores válidos de `ssot_level`/`estado` y coherencia de `deriva_de`; ciclos en la cadena `deriva_de`; alcance en un solo lugar (campos de spec fuera del registro); cadena de precedencia; emoticones.

Límite heredado y declarado en el propio docstring: **verifica presencia y forma, no adecuación**. Que un documento tenga spec no dice que la spec lo describa bien.

### Qué encontró la primera corrida
41 documentos, 6 ERROR y 22 WARN. Desglose honesto:
- **2 ERROR eran deriva real**, ambos de la misma clase y ambos de un día de antigüedad: `software/analisis/ANALISIS-SPEC-KIT.md` C4 decía «nuestra precedencia `SPECS_REGISTRY.md`» y `templates/RESULTADO-EXPERIMENTO.md` decía «Es precedencia 1» sobre el registro, que desde la Fase 8 es precedencia 2. Los dos documentos habían sido revisados a mano el mismo día, dentro de la propagación de la Fase 8, y los dos se escaparon.
- **1 ERROR era un hueco anterior**: `experimentos/b07-formato-hibrido/PREREG-B7.md` sin spec registrada. Es un pre-registro autorado, no generado desde template, así que la exención de `experimentos/` no lo alcanza — el mismo criterio que el 2026-07-30 obligó a registrar los runbooks. Se le escribió spec (`derivado` de `PRUEBA-REGENERABILIDAD-B7.md`), con la advertencia explícita de que describe un documento sellado y MUST NOT usarse para reescribirlo.
- **3 ERROR eran falsos positivos** del check de precedencia: disparaba dentro de bloques de código, no reconocía «esta constitución» escrito en prosa, y usaba una ventana que no miraba hacia atrás. Corregido: se ignoran los fences, se acepta la palabra además del nombre de archivo, y la ventana va de −4 a +12 líneas.
- **20 WARN eran ruido de diseño**: «spec sin campo `owner`» en casi todas. En un repo de un solo equipo, escribir 25 veces el mismo owner es ruido; se declaró en el registro que `owner` ausente significa `proyecto SDD` y se quitó el check. Los 2 WARN restantes (specs sin `proposito` en bloques que declaran dos paths) se corrigieron escribiendo el campo.

Estado final: **0 ERROR, 1 WARN** — los emoticones de `PREREG-B7.md`, que quedan vivos a propósito porque son M-08, decisión pendiente sobre un documento sellado.

### Cómo se validó
La corrección de los falsos positivos se verificó contra los dos positivos verdaderos: tras afinar la heurística, ambos siguen detectándose. El check se corrió también con `--strict` para confirmar que la única diferencia es el WARN esperado.

### Deuda abierta
- El checker **no verifica su propio criterio de separación** método/investigación (Fase 9): nada impide dar de alta una tarea de método en el backlog de investigación.
- No está cableado a `pre-commit`; hay que acordarse de correrlo. Cablearlo depende de decidir M-02.
- Sigue sin cubrir adecuación: los dos positivos verdaderos de hoy fueron de forma. Una spec que describe mal a su documento pasa igual.

### Planteo de la mejora, migrado de `agenda/MEJORAS-METODO.md` (2026-08-23)

Texto tal como estaba escrito en el backlog **antes** de este cierre: diagnostico, forma propuesta y reservas. Se trae aca por M-29, que deja en el backlog solo el puntero. No modifica nada de lo asentado arriba.

#### M-01 — Backstop determinista de documentación

Script local (sin CI) que verifica lo que hoy son checkboxes aspiracionales del campo `validacion`: todo `.md` autorado tiene spec registrada o cae en una exención declarada; el registro no apunta a archivos inexistentes; links internos vivos; `[Rxx]` usadas ⊆ `REFERENCIAS.md`; `deriva_de` existe y no es circular; `estado` y `ssot_level` con valores válidos; cadena de precedencia coherente con `CONSTITUTION.md` entre los documentos que la declaran.

Es la capa 2 del enforcement de tres capas del testigo (`docs/SDD-ENFORCEMENT.md`), portada a un repo documental. Límite heredado y explícito: verifica **presencia y forma, no adecuación** — que un documento tenga spec no dice que la spec lo describa bien.

Contraparte de investigación: `BACKLOG-INVESTIGACION` exploratoria «evaluación automática parcial sin CI», y prioridad alta «umbral de control manual a automatizado». Ejecutar M-01 produce dato para ambas; no las cierra.

**Hecha el 2026-07-31.** Los dos pendientes que dejó abiertos —cablearlo al commit y un check del criterio método/investigación— se cerraron el 2026-08-15 como **M-19** y **M-20**, y con ellos la dependencia de M-02 declarada entonces, que resultó falsa.

---

## Fase 9 — Separación de agenda de método y agenda de investigación (2026-07-31) — COMPLETADA

**Acción**: dar un hogar priorizado a las mejoras de método pendientes de la Fase 8, sin mezclarlas con las preguntas abiertas de investigación.

### Diagnóstico
La lista de mejoras existía solo como prosa en la Fase 8 y en la conversación que la produjo — el modo de fallo que el proyecto combate (deuda sin índice, que muere en silencio). El destino que parecía natural, `ROADMAP-MEJORAS-SDD.md`, no servía por dos razones independientes: está declarado **CERRADO / HISTÓRICO** desde 2026-06-01 con la advertencia de que su contenido en presente describe el estado previo a la Fase 1, y su `proposito` lo ata a una fuente única (proyecto "Transformacion AI-Native Org") que no es la nuestra. El otro candidato, `../agenda/BACKLOG-INVESTIGACION.md`, es agenda de **investigación**: mezclarle tareas de método contradice el Principio VI recién ratificado.

Además, la revisión del backlog encontró tres solapamientos reales con lo nuevo:
- Exploratoria #1 «evaluación automática parcial sin CI» **era** la mejora M-01, en estado exploratorio pese a estar aprobada — conflicto de estado.
- Transferencia Spec Kit #2 (marcador `[NEEDS CLARIFICATION]`) figuraba como candidato **y ya estaba adoptado** en `AGENTS.md`.
- Enriquecimientos R25/R30 #3 (modelo confirmado/inferido/gap) es una convención de escritura — método, no pregunta.

### Cambios aplicados
- **`../agenda/MEJORAS-METODO.md` (nuevo)**: criterio de separación explícito frente al backlog, tabla de estado con IDs `M-01`..`M-08` (prioridad, estado, origen, destino) y detalle por mejora. Estados: `Propuesta` / `Aprobada` / `Hecha` / `Descartada`; una mejora que se aprueba no cambia de documento, cambia de estado.
- **`../agenda/BACKLOG-INVESTIGACION.md`**: encabezado que declara su naturaleza (preguntas que se cierran con evidencia, no con una edición) y remite a `../agenda/MEJORAS-METODO.md`; exploratoria #1 reformulada como la pregunta que M-01 permite responder, con la construcción del script migrada; transferencia Spec Kit #2 marcada como adoptada; R25/R30 #3 migrado a M-06.
- **`SPECS_REGISTRY.md`**: spec de `../agenda/MEJORAS-METODO.md`; `incluye`/`excluye`/`validacion` del backlog reescritos con el criterio de separación; spec de `ROADMAP-MEJORAS-SDD.md` marcada como registro histórico cerrado que no recibe items nuevos; fila en la tabla SSOT.
- **`00-INDEX.md`** y **`README.md`**: alta del documento nuevo y rol de cada backlog diferenciado.

### Cómo se validó
Links internos: 0 rotos. Los tres solapamientos detectados quedaron con una sola representación cada uno: M-01 como tarea con su pregunta hermana en el backlog, el marcador `[NEEDS CLARIFICATION]` como adoptado, y M-06 en un solo documento. `BACKLOG-INVESTIGACION` alta #4 (gates que fallan abierto) se mantuvo del lado de investigación y se citó desde M-02 como requisito de diseño fail-closed, sin duplicar su contenido.

### Deuda abierta
- M-01 a M-08 sin ejecutar; M-01 es el próximo por valor.
- El criterio de separación es una regla escrita más, sin verificación: nada impide dar de alta una tarea de método en el backlog. Lo atraparía M-01 solo si se le agrega un check específico.

---

## Fase 8 — Versionado, constitución y alcance en un solo lugar (2026-07-31) — COMPLETADA

**Acción**: incorporar al repositorio de análisis las mejoras de método maduradas en el proyecto testigo `evaluador-flujo-intent`, empezando por las que no requieren tooling.

### Diagnóstico
Comparación del repo contra el testigo (HEAD `ded63e5`). La higiene documental estaba sana —0 links internos rotos, 36/36 referencias `[Rxx]` definidas—, pero faltaban tres piezas de método: (1) ninguna capa de invariantes por encima del registro, de modo que reglas duras (propagación, nacida del incidente B-07) convivían al mismo nivel que convenciones de forma; (2) el repo **no estaba versionado en ningún nivel**, sin baseline ni diff antes de tocar los documentos de mayor precedencia; (3) el alcance de cada documento estaba duplicado — medido: **11 filas de `00-INDEX.md` repetían el `proposito` del registro y 5 ya habían derivado**, perdiendo la procedencia de `ROADMAP-MEJORAS-SDD.md` y el alcance «contexto del repositorio» de `AGENTS.md`.

### Cambios aplicados
- **Versionado**: `git init` en `SDD/` con baseline `499c44a` (40 archivos) antes de cualquier edición. `.gitignore` excluye `fuentes-externas/` (material vendored con `.git` anidado; su versión sigue anclada en `REFERENCIAS.md`), caches y config local del asistente.
- **`CONSTITUTION.md` (nuevo, v0.1.0)**: siete invariantes con la anatomía del testigo —invariante autocontenido + `Enforcement` + `Detalle`— más governance semver, fase pre-1.0 y procedimiento de enmienda. Principios: I SSOT único por tema; II trazabilidad de afirmación a fuente; III propagación bidireccional; IV documento autorado, spec registrada; V integridad del registro experimental; VI separación método/contenido; VII preguntar antes que interpretar. Declara explícitamente su **límite honesto**: el enforcement es humano y a pedido.
- **Precedencia a cuatro niveles** (`CONSTITUTION.md` → `SPECS_REGISTRY.md` → `AGENTS.md` → criterio), con división de trabajo declarada: la constitución dice *qué nunca cede*, el registro *cómo se aplica hoy*.
- **Regla de alcance en un solo lugar** (`SPECS_REGISTRY.md` §Reglas globales, operativa del Principio I): `proposito`/`incluye`/`excluye`/`validacion` viven solo en el registro; el índice declara **rol**, no propósito; el encabezado de un doc puede llevar una línea de identidad pero no enumerar incluye/excluye. Migración oportunística para los encabezados preexistentes.
- **`00-INDEX.md` a navegación pura**: se eliminó la columna «Contenido» y también el «Mapa de SSOTs», que duplicaba la tabla SSOT del registro. La tabla quedó en el registro y no en el índice porque de ella depende la regla de propagación, y ahí tiene precedencia 2.
- **`AGENTS.md` reescrito** (119 → 118 líneas, con más contenido y menos duplicación): orden de lectura que arranca por la constitución, sección «Al cerrar una iteración» (registro, historial, commit), sección «Qué NO hacer» con cada ítem anclado a su principio. Se eliminó la reproducción de la regla de propagación —que el propio documento declaraba delegada al registro tres líneas antes— y las convenciones de forma, ahora referenciadas.
- **Propagación**: `software/analisis/ANALISIS-SPEC-KIT.md` (fila de autoridad del mapeo + nota fechada en C4: se adoptó la parte declarativa del patrón, no la ejecutable, y la pregunta de C4 sigue abierta); `software/00-INDEX.md` y `docs-y-investigacion/00-INDEX.md` (repetían la cadena de precedencia sin la constitución); `README.md`.

### Cómo se validó
Links internos: 0 rotos antes y después. Cadena de precedencia coherente en los cuatro documentos que la mencionan. La medición de divergencia del `proposito` se hizo con script contra el registry, no a ojo. La spec de `CONSTITUTION.md` se escribió en el mismo lote que el documento — inversión del Principio IV que se declara acá como excepción de bootstrap, no como precedente.

### Deuda abierta
- **P3 y P4 sin implementar**: backstop determinista (`check_docs.py`) y gate de autoría, las dos capas que convertirían el `validacion` de checkbox en verificable. Aprobadas como mejora de método, no como experimento. Mientras no existan, la constitución se cumple por disciplina.
- **P5 y P7 sin abrir**: playbooks agnósticos de asistente y formato/compactación de documentos.
- Los **encabezados de documento** que restatan su alcance (al menos `../comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md`) siguen duplicando: migración oportunística, no barrido.
- `AGENTS.md` e `../comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md` describen un contexto **sin CI**; sigue siendo cierto, pero ahora hay git, y eso habilita `pre-commit` como sustrato de P3/P4. Revisar ambos cuando se implementen.

---

## Fase 7 — Aparato de evaluación de B-07: R6, degradación de H2 y criterio reformulado (2026-07-29) — COMPLETADA

**Acción**: cerrar las deudas que el cierre de B-07 dejó en su propio aparato de medición, sin tocar ningún valor medido ni el veredicto.

### Cambios
- **Alta de `R6` (verificación funcional manual)** en el SSOT del experimento + §3.7 del runbook. Motivo: `R1` se automatizó con `pytest`, luego midió **sólo el subconjunto pytest-verificable**; la doctrina del propio testigo asigna los `FR` de UI y de consistencia documental a verificación visual (relación requisito↔verificador **N:M**). `R6` exige recorrido guionado pre-registrado y observación de **comportamiento, no de fuente** (el fuente des-ciega el formato). No se midió en B-07.
- **Medición exploratoria post-cierre, NO ciega**, de los 13 requisitos de `SPEC-013` que quedaron fuera del denominador: **9 eran mecanizables** (5 por gate objetivo del repo, 4 por suites que existen en `ENV-REF` pero quedaron fuera de `TESTS-F013`) y están **satisfechos en ambas celdas** ⇒ el espacio no medido no escondía señal. Sensibilidad al denominador: extendido 25→34, la brecha por requisito pasa de 100/64 a **100/74** — misma dirección, menor magnitud. Quedan **4 requisitos sin ningún dato**, todos de UI.
- **`H2` degradada a descriptiva.** Dos motivos independientes: su ratio upfront/reactivo **no es computable** (`[NEEDS CLARIFICATION]` no existe en la anatomía casero — es **`N/A`, no `0`**), y su variable de salida está **confundida con el tratamiento** (una práctica documental altera la visibilidad de su propio resultado; los conteos crudos van en dirección contraria a H2). Se conserva la lectura cualitativa.
- **Anti-patrón nuevo en `BACKLOG-INVESTIGACION` #6**: *variable de salida que es artefacto del propio tratamiento (confusión de visibilidad)*, con el corolario operativo **`N/A` ≠ 0** y el test de diseño «¿la variable de salida sobreviviría si el tratamiento no existiera?».
- **Criterio de éxito REFORMULADO** —la deuda que venía abierta desde la Fase 5— en **(a)** prueba de regenerabilidad contra `R1`–`R6` (unidad intra-feature; `R1` mayor + `R2` menor + **≥1 secundaria independiente** en el mismo sentido y ninguna en contra, admisibles `R4`/`R5`/`R6`, `R3` excluida por no ser independiente de `R1`; empate ⇒ no concluyente; veredicto global sólo con ≥2 features discriminantes; **guarda de confusión** con techo *"no atribuible al formato"*) y **(b)** corpus observacional contra **`H1`+`H3`** (sólo Tier A; no-solapamiento de rangos; techo **descriptivo**), más **regla de cierre a dos veredictos**. Ambos pasan la comprobación de satisfacibilidad.
- **§Propagacion escrita en `RESULTADO-EXPERIMENTO-B7.md`** —faltaba, y era la deuda 4.5 real— con los **tres checks efectivamente corridos** y triaje de 11 filas. Corregido también el encabezado stale *"(propuestas, NO aplicadas)"*: 3 de 4 cambios al marco **ya estaban aplicados**.

### Verificación
Aplicar el criterio (a) a la prueba ya ejecutada **reproduce el veredicto existente** (H4 no sostenida, F001 no concluyente, techo "no atribuible"): lo que cambia es que el criterio pasa de **no evaluable en bloque** a **evaluable**. Confirmado empíricamente que **ningún check de propagación basta solo**: los 4 archivos que devolvió el check 3 estaban ya cubiertos o justificados, y los 5 realmente afectados por estos cambios **no aparecen en el check 3**.

### Deuda abierta
- **Camino crítico para cerrar B-07 integralmente**: reescribir `experimentos/b07-formato-hibrido/PRUEBA-OBSERVACIONAL-B7.md` como runbook real (le faltan «Definicion operacional» y Fase 0 sellada; su corte debe fijarse en `3f1ed33` porque el ciclo de vida del corpus es **pre-git**) → **medir `H1` y `H3`** → cerrar con los dos veredictos.
- `R6` sin recorrido guionado pre-registrado; 4 requisitos de UI de `SPEC-013` sin dato.
- Desambiguar formato vs. procedencia (Hallazgo 2) **requiere corrida nueva**: es otro experimento, no una tarea de cierre.
- La reserva de método queda declarada: el criterio (a) se redactó conociendo los resultados; gobierna réplicas y no reabre el veredicto.

---

## Fase 6 — Propagación al cerrar un experimento (2026-07-29) — COMPLETADA

**Acción**: cerrar el hueco estructural que dejó ver el cierre de B-07 — un experimento produce conocimiento nuevo **sin modificar ningún SSOT**, así que la regla de propagación no se disparaba y la sincronización dependía del recuerdo de quien cerraba.

### Diagnóstico
Al cerrar B-07 (2026-07-28) el `[SDD-Check]` listó tres derivados y los tres se sincronizaron; la lista se había armado de memoria y omitió cuatro documentos —entre ellos `software/LINEAS-INVESTIGACION.md`, que es **SSOT** y quedó atrás de su propio derivado `PLAN-PRUEBAS.md`. Tres causas independientes:
1. `experimentos/` está exento de spec (`SPECS_REGISTRY.md` §Docs excluidos) ⇒ fuera del grafo SSOT ⇒ nada dispara.
2. La regla de propagación era **unidireccional** (SSOT → derivados), pero el conocimiento de una ejecución entra por abajo y tiene que subir. Contradecía la tesis bidireccional del propio proyecto (`../comun/SDD-ADAPTATIVO-VS-CASCADA.md`).
3. `Derivados a revisar` se poblaba de memoria, sin índice.

### Cambios aplicados
- **`templates/RESULTADO-EXPERIMENTO.md`**: sección **«Propagacion» obligatoria**, con **tres checks** y tabla de triaje. (1) grep del ID en `SPECS_REGISTRY.md` — las cláusulas `incluye`/`excluye` suelen justificarse con el estado del experimento; (2) el SSOT dueño de la hipótesis y sus derivados según la tabla SSOT — único check que ve a quien afirma el estado **sin declararlo como deuda**; (3) `grep -rl "Deuda arrastrada.*<ID>"` — captura documentos lejanos que ningún índice conecta con el experimento.
- **`templates/EXPERIMENTO.md`**: sección **«Documentos que esperan este resultado»**, contraparte del check 3 en el pre-registro.
- **`templates/RESULTADO-EXPERIMENTO.md` §Deuda arrastrada**: la deuda no resuelta MUST migrar a `../agenda/BACKLOG-INVESTIGACION.md` antes de cerrar. "Re-explicitarse en el siguiente cierre" ataba la deuda a que existiera otro experimento; si no lo hay, muere en silencio.
- **`AGENTS.md`**: regla de propagación **ascendente** en §Criterios de calidad mínima, y check de post-generación para el cierre de experimentos.
- **`SPECS_REGISTRY.md`**: la regla, donde tiene precedencia 1 — propagación ascendente y disparador por cierre de experimento, con la aclaración de que la exención de `experimentos/` es de **spec propia**, no de **propagación**. Se corrigió además la columna «Quien referencia» de ambos `PLAN-PRUEBAS.md`, que decía `templates/` (dirección invertida) siendo que el plan se apoya en esa columna como índice inverso.

### Cómo se validó
Prueba en seco de los tres checks contra el cierre real de B-07: reproducen exactamente los cuatro documentos corregidos a mano el 2026-07-29. **El check 3 aislado sólo encuentra dos** —`COMPARATIVA` y `DECISION`, que sí habían declarado deuda desde 2026-05-28— y no ve a `LINEAS-INVESTIGACION` ni al registry, que afirmaban el estado sin anotarlo como pendiente. Ese punto ciego, detectado por la propia verificación, es el motivo de que el mecanismo tenga tres checks y no uno.

### Deuda abierta
- Los tres checks son **manuales** (proyecto sin CI): nada impide cerrar un experimento salteándolos. Es el mismo modo de fallo que el anti-patrón *gate fail-open* que B-07 dejó registrado en `BACKLOG-INVESTIGACION` #4.
- Sin cobertura para documentos que afirman el estado de un experimento **y** no están en el registry **y** no declararon deuda. No hay caso conocido; el riesgo se declara.
- ~~Sigue abierto de la Fase 5: reformular el Criterio de éxito de B-07 (requiere decisión del usuario) y registrar el anti-patrón *fail-open* como regla del marco.~~ **CERRADO en la Fase 7 (2026-07-29)**: criterio reformulado en (a)/(b) y anti-patrón *fail-open* ya en `BACKLOG-INVESTIGACION` #4.

---

## Fase 5 — Ejecución y cierre de B-07 (prueba de regenerabilidad) (2026-07-11 → 2026-07-28) — COMPLETADA

**Acción**: ejecución completa del runbook `experimentos/b07-formato-hibrido/PRUEBA-REGENERABILIDAD-B7.md` sobre el proyecto testigo, en un directorio de trabajo externo al repo (`/datum1/Descargas/Claudio/experimentosdd-b7/`, bitácora append-only propia). Cierre en `experimentos/b07-formato-hibrido/RESULTADO-EXPERIMENTO-B7.md`.

### Qué se ejecutó
- **Fase 0** — pre-registro sellado en el tag `b7/prereg-v1`; 4 specs del 2×2 (2 auténticas + 2 traducidas spec→spec por un `Traductor` independiente); `SELLO-CIEGO` generado y custodiado por el usuario, nunca visible para el orquestador.
- **Fase 1** — dos baselines por sustracción (`b7/base-f001-v1`, `b7/base-f013-v2`), validados con gate objetivo (compila + frontera completa + verificación de ausencia).
- **Fase 2** — 4 regeneraciones one-shot en sesiones frescas, salidas en ramas ciegas `b7/run-a..d`. Tasa `VOID` 1/5.
- **Fase 3 y 3-bis** — métricas `R1`–`R5` en las 4 celdas, con *tooling* determinista y re-ejecutable; lazo de reparación acotado (`K=3`).
- **Fase 4** — des-ciego, proyección de `R1` a requisitos en F013 (mapeo construido a ciegas y congelado con hash antes de aplicarse), veredicto y resultado.

### Resultado
En la única feature que discriminó (F013) el formato **casero** superó al híbrido en `R1`, `R2` y `R5`; F001 empató en las cinco métricas. **H4 no queda sostenida, pero tampoco refutada**: en F013 el eje formato está perfectamente confundido con el eje spec auténtica/traducida, y una sola ronda de reparación borra la diferencia (las 4 celdas llegan a 100%). **Decisión: Ajustar** — no se adopta ni se descarta el formato híbrido.

### Cambios al sistema SDD aplicados a raíz del experimento
- **`templates/EXPERIMENTO.md`**: sección **«Definicion operacional» obligatoria** (denominador, aislamiento, validación del instrumento, granularidad, admisibilidad de reconciliaciones, regla de agregación, tratamiento del empate, independencia entre métricas, quién mide) y **«Criterio de exito» reforzado** con comprobación de satisfacibilidad. Origen: el pre-registro de B-07 fijaba *qué* medir pero no *cómo*, y acumuló **ocho enmiendas post-hoc** al runbook.
- **`SPECS_REGISTRY.md`**: la spec de los templates incorpora esos dos checks; se agregaron los campos `path` faltantes en las dos entradas combinadas (templates e índices de línea), que los hacían invisibles a cualquier verificación mecánica de cobertura.
- **`software/PLAN-PRUEBAS.md`** y **`experimentos/b07-formato-hibrido/EXPERIMENTO-B7-formato-hibrido.md`**: estado de B-07 sincronizado (de "pre-registrado" a métrica primaria cerrada), con la distinción explícita entre la prueba de regenerabilidad (cerrada) y el corpus observacional de secundarias (sin medir).

### Deuda abierta
- **Reformular el Criterio de éxito de B-07** en `EXPERIMENTO-B7-formato-hibrido.md` (SSOT): resultó **no evaluable** — no define agregación y su cláusula "≥2 secundarias" mezcla las del corpus observacional con las de la prueba. Nota fechada ya inscrita en el doc; la reformulación **requiere decisión del usuario**.
- **Desambiguar formato vs. procedencia**: es el límite principal del resultado y no es reparable con los datos existentes.
- **Hallazgos transferibles** ya registrados en `../agenda/BACKLOG-INVESTIGACION.md`: gates de gobernanza que fallan abierto (#4) y régimen de permisos en experimentos de regeneración (#5).

---

## Verificación en fuente completa de R25/R30/R33/R34 (2026-07-10)

**Acción**: lectura completa de las cuatro fuentes vendored en `fuentes-externas/` (LaTeX arXiv) que estaban sin verificar en fuente completa; auditoría de todas las citas `[Rxx]` que dependen de ellas.

### Veredicto: las cuatro siguen siendo relevantes; ninguna cita requirió corrección
- **[R25] Reversa** (`arXiv-2605.18684v1/`): el uso en `software/SDD-EN-LEGACY-Y-BROWNFIELD.md` (existe trabajo formal en retro-specs legacy para agentes) es fiel y modesto. Anotada su naturaleza en `REFERENCIAS.md`: caso exploratorio único COBOL→Go incompleto (9/11 tareas; sin paridad final ni cutover), sin comparación controlada — no citar como evidencia de efectividad.
- **[R30] Piskala** (`arXiv-2602.00180v1/`): technical report de autor único, no peer-reviewed. Las tres citas en `../comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md` (intent drift, contrato multi-agente, regeneración reduce divergencia) están respaldadas textualmente. Anotado: su cifra "hasta 50 % menos errores" viene de secundarias — no usar como dato primario. Bonus para B-07: taxonomía spec-first/spec-anchored/**spec-as-source** (la regenerabilidad primaria de B-07 es su nivel spec-as-source).
- **[R33] Rosa et al.** (`arXiv-2601.03878v1/`): confirmado todo lo citado en `experimentos/b07-formato-hibrido/EXPERIMENTO-B7-formato-hibrido.md` (tarea aislada between-subjects, endpoint/prompts/parámetros fijos, métricas, TaskId como blocking factor). Precisión anotada: es protocolo Stage 1 **sin resultados aún**; el modelo se elegirá open-weight en ejecución.
- **[R34] RepoExec** (`arXiv-2406.11927v4/`): confirmado literal en abstract ("smaller context sizes can be misleading", 18 modelos, pretrained vs instruction-tuned, DIR). Autor primero corregido: Le Hai et al. (no Nguyen). Hallazgo adicional anotado: correlación pass@1↔DIR y riesgo de reimplementar dependencias en vez de invocarlas.

### Actualizaciones en positivo aplicadas (aprobadas por el usuario)
- `experimentos/b07-formato-hibrido/EXPERIMENTO-B7-formato-hibrido.md`: (1) H4 encuadrada en la taxonomía spec-first/spec-anchored/spec-as-source [R30] — la regenerabilidad primaria es el test operativo del nivel spec-as-source, lo que da escala graduada al resultado; (2) métrica **R4 nueva** (invocación vs. reimplementación de contratos de la frontera in-spec, análogo del DIR [R34]) — captura el modo de fallo "verde en R1, limpio en R2, pero mal integrado al sistema"; (3) precisión de fidelidad: [R33] fija endpoint/prompts/parámetros (no seed; modelo a elegir en ejecución; Stage 1 sin resultados).
- `../agenda/BACKLOG-INVESTIGACION.md`: sección nueva "Enriquecimientos diferidos desde verificación de fuentes R25/R30" (regla de rigor mínimo y pitfalls de [R30]; modelo confirmado/inferido/gap de [R25] como convención candidata de Línea A).

---

## Actualización clon Spec Kit [R10]: v0.8.13 → v0.12.11.dev0 (2026-07-10)

**Acción**: `git pull` deliberado del clon vendored `fuentes-externas/spec-kit/` (`a08af08` 2026-05-22 → `983a87f` 2026-07-10; 374 commits, 4 versiones menores 0.9→0.12).

### Diff dirigido contra `software/analisis/ANALISIS-SPEC-KIT.md` (basado en snapshot v0.8.13)
- **Ninguna conclusión invalidada.** Tesis "Power Inversion", coverage mapping de `/speckit.analyze` (C1), C2 y C3 siguen vigentes.
- **Cambio conceptual 1 — Artículos IV, V y VI ahora explícitamente *project-defined governance*** (`spec-driven.md` upstream; CHANGELOG 0.11.6). Refuerza, no contradice, el enfoque del testigo (gate de integridad de la constitución). La estructura de 9 artículos se mantiene estable.
- **Cambio conceptual 2 — comando nuevo `/speckit.converge`** (0.11.2, documentado 0.11.10). No cubierto por el análisis; candidato a incorporar si se re-analiza el set de comandos.
- **Resto = infraestructura, no conceptual**: script types Python en templates, `specify self upgrade` / `specify bundle`, git como extensión opt-in (0.10.0, elimina `--no-git`), `/speckit.analyze` en subagente forkeado (0.11.3), múltiples integraciones de agentes y presets de governance.

### Pendiente (deuda arrastrada)
- `ANALISIS-SPEC-KIT.md` sigue anclado a v0.8.13; incorporar `/speckit.converge` y la aclaración de artículos project-defined requiere edición aprobada (no ejecutada en esta actualización).

---

## Fase 4 — Catálogo de escenarios que justifican SDD (2026-06-06) — COMPLETADA

**Alcance**: consolidar, con investigación web, el catálogo de problemas/escenarios que hacen necesario SDD hoy, separando modos de fallo (cualitativo) de cifras (cuantitativo).

### Archivos creados
- `../comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md` (SSOT, común): causas raíz transversales; escenarios por línea A, B y transversales; mapa escenario → eje SDD. Referencia `ESTADISTICAS` (cifras) y `SDD-ADAPTATIVO-VS-CASCADA` (cascada) sin duplicarlos.

### Archivos modificados
- `REFERENCIAS.md`: alta de [R28] (dplooy, marcada como secundaria), [R29] (Red Hat Developer), [R30] (arXiv "From Code to Contract").
- `../comun/ESTADISTICAS-TENDENCIAS-EVOLUCION.md` (SSOT): nueva subsección "Calidad del código generado por IA y señal de adopción SDD" con cifras secundarias [R28] marcadas como tales.
- `SPECS_REGISTRY.md`: spec nueva para `../comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md`; alta en tabla SSOT.
- `00-INDEX.md`: ruta recomendada, estructura y mapa de SSOTs.

### Reserva
Las cifras de [R28] son de fuente divulgativa (secundaria); marcadas como tales y pendientes de verificar contra fuente primaria antes de elevar su peso argumental. Deuda arrastrada hasta esa verificación.

---

## Fase 3 — Aplicacion de mejoras B-06 y comparativa Spec Kit/testigo (2026-06-01) — COMPLETADA

**Alcance**: cierre de la "Decision pendiente" de Fase 2 (dos propuestas de B-06 aprobadas y aplicadas), formalizacion del experimento B-07 y de la comparativa Spec Kit vs. testigo.

### Decisiones aplicadas (propuestas de B-06, antes pendientes)
1. **"Deuda arrastrada" formalizada como artefacto del marco.** Campo `Deuda arrastrada` anadido al bloque `[SDD-Check]` (`CLAUDE.md`) y seccion homonima en `templates/RESULTADO-EXPERIMENTO.md`. Mecanismo anti-cascada: re-explicitar lo diferido hasta resolverlo.
2. **Umbral de cascada reformulado de absoluto a relativo.** `../comun/SDD-ADAPTATIVO-VS-CASCADA.md` (SSOT) reemplazo "30 dias absolutos" por "2-3 iteraciones o ciclos de cierre"; los 30 dias quedan solo como equivalencia de referencia. Derivados revisados: implicaciones por linea y senales de salud, ya alineadas.

### Archivos creados
- `software/COMPARATIVA-SPECKIT-VS-TESTIGO.md` — comparacion en 5 dimensiones (derivado de `ANALISIS-SPEC-KIT.md`); enlazada desde `software/00-INDEX.md`.
- `experimentos/b07-formato-hibrido/EXPERIMENTO-B7-formato-hibrido.md` — pre-registro del experimento de formato hibrido (Spec Kit vs. casero) sobre el testigo.

### Archivos modificados
- `CLAUDE.md`: campos `Cobertura` y `Deuda arrastrada` en el bloque `[SDD-Check]`; convencion `[NEEDS CLARIFICATION]`.
- `../comun/SDD-ADAPTATIVO-VS-CASCADA.md` (SSOT): ventana de inactividad relativa; mecanismo "Deuda arrastrada"; aclaracion regenerabilidad vs. adaptatividad.
- `software/LINEAS-INVESTIGACION.md` y `software/PLAN-PRUEBAS.md`: alta de hipotesis/experimento B7.
- `SPECS_REGISTRY.md`: specs nuevas para `COMPARATIVA-SPECKIT-VS-TESTIGO.md`.

### Revision de consistencia (este mismo cierre)
- `ROADMAP-MEJORAS-SDD.md` marcado como **CERRADO/HISTORICO**: sus mejoras 1-10 ya vivian en `SPECS_REGISTRY.md`/`CLAUDE.md` desde Fase 1; el doc se conserva como registro pero ya no se lee en presente.
- `../comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md` (SSOT): GitHub Spec Kit recategorizado de Linea A a **Linea B (software)**, coherente con su caracterizacion "Linea-B-nativo" en `ANALISIS-SPEC-KIT.md`.
- `REFERENCIAS.md`: alta de `[R19]` (Karpathy LLM Wiki) para resolver una colision de ID en `BACKLOG-INVESTIGACION` (citaba el gist como `[R01]`).
- Correcciones menores: renumeracion de la ruta en `00-INDEX.md`; conteo de archivos en Fase 1.

---

## Fase 2 — Analisis de GitHub Spec Kit (2026-05-24) — COMPLETADA

**Alcance**: Investigacion del repositorio GitHub Spec Kit (v0.8.13, [R10]), creacion del analisis comparativo para Linea B y reordenamiento del material fuente externo.

### Decision: separar material fuente externo
Se introduce el directorio `fuentes-externas/` para repositorios externos clonados (vendored), separandolos de los docs autorados por el proyecto. El clon `software/spec-kit/` se movio a `fuentes-externas/spec-kit/` (con su `.git` intacto para `git pull` en re-analisis). Registrado como exclusion en `SPECS_REGISTRY.md`.

### Archivos creados
- `software/analisis/ANALISIS-SPEC-KIT.md` — analisis del flujo de Spec Kit, mapeo contra nuestro protocolo y conclusiones C1-C5 para Linea B. Linea A diferida.

### Archivos modificados
- `SPECS_REGISTRY.md`: exclusion de `fuentes-externas/`; spec nueva para `software/analisis/ANALISIS-SPEC-KIT.md`.
- `REFERENCIAS.md`: [R10] anclado a version v0.8.13 (consultada 2026-05-21) + ruta del clon vendored y politica de actualizacion.
- `../comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md` (SSOT): entrada Spec Kit enriquecida con flujo de comandos y link al analisis.
- `software/00-INDEX.md`: seccion "Analisis de frameworks" con link al doc.
- `../agenda/BACKLOG-INVESTIGACION.md`: item "Transferencia de conceptos de Spec Kit a Linea A" (diferido).

### Hallazgo principal
Convergencia alta entre Spec Kit y nuestro protocolo (lenguaje normativo, gate de autoridad, manejo explicito de ambiguedad, validacion de consistencia continua). `/speckit.analyze` valida empiricamente el diseno de nuestro bloque `[SDD-Check]`. Tension abierta: la "Power Inversion" (spec ejecutable que genera codigo) es mas radical que nuestra posicion actual (spec como representacion del conocimiento) — conecta con el backlog de umbral manual->automatizado.

### Continuacion: compatibilidad documental + proyecto testigo

**Bloque 1 (compatibilidad, solo docs)** — aplicado en `CLAUDE.md`:
- Convencion `[NEEDS CLARIFICATION: ...]` para marcar incertidumbre en borradores (candidato C2 del analisis).
- Campo `Cobertura` anadido al bloque `[SDD-Check]`, espejando el coverage mapping de `/speckit.analyze` (candidato C1).

**Decision: proyecto testigo oficial de Linea B.**
Se designa `agent-test-suite` (`../../../test_circuito_intents/agent_test_suite/`) como sujeto experimental. Es un proyecto Python real que adopto nuestra variante SDD (derivada de este proyecto). Razon: este repo es meta/docs y no puede ejecutar su propio Plan de Pruebas (metricas DORA, defectos) — `experimentos/` estaba vacio por falta de sujeto. Registrado en `software/PLAN-PRUEBAS.md`.

**Primer experimento ejecutado y cerrado (observacional):** `experimentos/b06-circuito-testigo/EXPERIMENTO-B6-circuito-testigo.md` + `experimentos/b06-circuito-testigo/RESULTADO-EXPERIMENTO-B6.md`. Veredicto: hipotesis B6 SOSTENIDA en este caso (circuito de aprendizaje activo). Metrica primaria 40% (estricta) / 60% (amplia) de specs activas revisadas tras ejecucion; deuda arrastrada re-explicitada sin abandono; `[SDD-Check]` en 100% de iteraciones. Caveats: muestra minima (estudio de caso), sesgo de confirmacion (el testigo derivo su SDD de este proyecto), umbral de 30 dias no informativo a esta velocidad. Dos mejoras candidatas al marco propio surgidas del experimento (ver "Decision pendiente").

**Decision pendiente (del usuario):** _[RESUELTA en Fase 3, 2026-06-01: ambas propuestas fueron aprobadas y aplicadas.]_ dos propuestas de cambio al marco SDD derivadas de B-06:
1. Formalizar "Deuda arrastrada" como artefacto del marco (template de resultado y/o `[SDD-Check]`).
2. Reformular el umbral de cascada de "30 dias absolutos" a un criterio relativo a la velocidad del proyecto — toca el SSOT `../comun/SDD-ADAPTATIVO-VS-CASCADA.md`, requiere aprobacion y revision de derivados.

### Archivos modificados/creados (continuacion)
- `CLAUDE.md` (modificado): Bloque 1.
- `software/PLAN-PRUEBAS.md` (modificado): seccion "Proyecto testigo" + experimento B-06.
- `experimentos/b06-circuito-testigo/EXPERIMENTO-B6-circuito-testigo.md` (creado): diseno del experimento (excluido del registry — generado desde template).

---

## Fase 1 — Consolidacion del sistema (2026-03-01) — COMPLETADA

**Alcance**: Unificacion de archivos de protocolo, cobertura completa de specs, eliminacion de duplicacion SSOT y enriquecimiento del registro.

### Archivos eliminados
- `AGENTS.md` — absorbido por `CLAUDE.md`
- `PROTOCOLO_ASISTENTES.md` — absorbido por `CLAUDE.md`

### Archivos creados
- `ROADMAP-MEJORAS-SDD.md` — analisis comparativo con proyecto "Transformacion AI-Native Org"
- `historial/sdd.md` — este archivo

### Archivos modificados

**`CLAUDE.md`** (reescrito):
- Absorbe contenido unico de `AGENTS.md` (comandos, convenciones de commits) y `PROTOCOLO_ASISTENTES.md` (pasos durante generacion, criterios de calidad, excepciones)
- Agrega `MUST NOT` al paso 4 del protocolo (no proponer alternativas sin aprobacion)
- Agrega seccion "Disambiguacion" (MUST preguntar, MUST NOT anticipar)
- Agrega checks genericos de post-generacion (refs, no duplicacion, no contradiccion SSOT, derivados)
- Agrega seccion "Ciclo de vida de specs" (proponer spec antes de doc, senalar divergencias, marcar deprecados)
- Elimina tabla SSOT y niveles ssot_level (ahora solo en `SPECS_REGISTRY.md`)

**`SPECS_REGISTRY.md`**:
- Agrega campo `deriva_de` al bloque de ssot_level (trazabilidad de derivados)
- Agrega seccion "Campo `estado`" (Activo / Borrador / Deprecado)
- Agrega seccion "Profundidad de spec" con 3 niveles (minima / estandar / extendida)
- Agrega seccion "Docs excluidos del registro"
- Tabla SSOT: columna "Derivados/Referencias" renombrada a "Quien referencia" con datos precisos
- Reglas globales: referencia tabla de profundidad en lugar de listar campos fijos
- 4 specs nuevas: `SPECS_REGISTRY.md`, `CLAUDE.md`, `../agenda/BACKLOG-INVESTIGACION.md`, `ROADMAP-MEJORAS-SDD.md`

**`REFERENCIAS.md`**:
- Elimina R19, R20, R21 (referencias a proyecto externo "Transformacion AI-Native Org")
- Elimina seccion "Fuentes internas (proyecto origen)"

**5 archivos con referencias actualizadas** (de `PROTOCOLO_ASISTENTES.md` a `CLAUDE.md`):
- `00-INDEX.md`, `README.md`, `SPECS_REGISTRY.md`, `software/00-INDEX.md`, `docs-y-investigacion/00-INDEX.md`

### Decision: SSOT unico para tabla y niveles ssot_level
`SPECS_REGISTRY.md` es el SSOT autoritativo de la tabla SSOT y la definicion de niveles. `CLAUDE.md` referencia en lugar de repetir. Detectado como contradiccion del principio SSOT — resuelto en esta fase.
