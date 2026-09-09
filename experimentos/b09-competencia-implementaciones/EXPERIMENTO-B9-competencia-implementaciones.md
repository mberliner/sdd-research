# Experimento B-09: competencia de implementaciones SDD sobre objetivo sintetico

## Metadata
- ID: B-09
- Linea: software
- Fecha inicio: 2026-09-06
- Responsable: proyecto SDD
- **Estado: BORRADOR PRE-SELLO.** Las hipotesis de abajo estan escritas y **todavia no selladas**. Ninguna corrida de brazo tratamiento MUST ejecutarse antes del sello (Principio V). Antes del sello MAY correr unicamente la Fase 0.A —caracterizacion de interfaces, sobre un enunciado descartable— y la Fase 0.B de calibracion, esta ultima solo sobre el brazo control.

## Pregunta que lo origina

`../../software/ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md` §7 abre con: «**Como se comportan en un proyecto real.** Ninguna se corrio: las cuatro se leyeron de clones vendored». Todo el corpus de linea B sobre implementaciones adoptables es lectura de mecanismo. Este experimento las corre.

## Hipotesis

Cuatro, independientes, cada una evaluada por separado. Ninguna se funde con otra en el veredicto. **Cada una declara sobre qué rondas se evalúa**: un cuantificador implícito es un grado de libertad que se resuelve al ver los datos.

- **H1 (primaria).** Al menos un brazo con método SDD alcanza una proporción de e2e sellados aprobados **mayor** que el brazo control sin método, **en al menos una** de las dos rondas.
- **H2a (OpenSpec).** **En R2**, OpenSpec —contabilidad de capacidades— produce **menos regresión** sobre los e2e de R1 que el control y que Spec Kit (ceremonia orquestada).
- **H2b (sdd-first).** **En R2**, sdd-first —gate fail-closed— produce **menos regresión** sobre los e2e de R1 que el control y que Spec Kit.
- **H3.** Superpowers consume **más tokens por corrida** que cualquier otro brazo, **en las dos rondas**, con independencia de su resultado en H1.

**Por qué H2 está partida en dos, y la decisión es pre-sello.** La redacción inicial afirmaba de una sola vez que los dos mecanismos de estado o *enforcement* —OpenSpec y sdd-first— regresionan menos, lo que exigía la conjunción simultánea de cuatro desigualdades sobre dos herramientas distintas. Si un mecanismo reducía la regresión y el otro no, no había veredicto definido. Son dos mecanismos y son dos afirmaciones: se evalúan por separado, como ya se hace entre H1 y H3. Ninguna corrida de tratamiento existía al decidirlo.

H3 no es una hipótesis sobre SDD: es la única objeción de terceros del corpus que se puede convertir en medición barata en este mismo diseño (`ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md` §4 quinquies, [R47]). Entra porque el dato se produce igual, no porque el experimento exista para eso. Su cuantificador es **las dos rondas** porque «este método consume más» es una afirmación sobre el método: un brazo que sólo es el más caro en una de las dos rondas no la sostiene.

**Lo que ninguna de las cuatro afirma.** Ninguna dice cuál método es mejor. H1 pregunta si el método compra algo contra no tener método; H2a y H2b preguntan si un mecanismo se comporta distinto en la ronda donde ese mecanismo aplica. Un resultado nulo en H1 —ningún brazo supera al control— es un resultado, y probablemente el más importante que este diseño puede producir.

## Diseno

Cinco brazos, dos rondas, tres repeticiones por celda. **30 corridas**, cada una un proyecto generado entero.

### Brazos

| Brazo | Fuente | Mecanismo que aporta | Ronda donde su mecanismo puede mostrarse |
|---|---|---|---|
| **C0** control | ninguno | ninguno — enunciado y a codificar | ambas (linea base) |
| **T1** Spec Kit | [R10] | ceremonia orquestada por CLI, ciclo por feature | R1 (greenfield es su orientacion declarada) |
| **T2** OpenSpec | [R38] | capacidad durable + delta como unidad de cambio | R2 (cambio sobre sistema existente es su orientacion declarada) |
| **T3** sdd-first | [R39] | gate fail-closed sembrado en el repositorio | R2 (un gate previene, no empuja) |
| **T4** Superpowers | [R37] | conducta del agente: router de ceremonia + TDD | ambas, pagando en contexto |

**Poblacion, y por que difiere de la de `ORIENTACION-PRACTICA`.** Alli la poblacion es «lo que alguien podria evaluar o adoptar», seis casos. Aca la poblacion es **lo que se puede correr hoy**, y eso deja fuera dos:

- **Kiro** [R44]: el metodo lo trae un IDE. No hay forma de invocarlo desde un harness de linea de comandos con el resto de las condiciones selladas iguales. Excluido por imposibilidad de sello, no por ser cerrado.
- **Tessl** [R46]: *Framework* en beta cerrada. No se consigue. Es el caso que mas interesaria —el unico que regenera— y su ausencia MUST declararse junto a cualquier lectura del resultado.

**Superpowers entra como brazo simple y no como factor.** Su ortogonalidad —gobierna al agente, no al artefacto— lo habilita a combinarse con T1 o T2 en un diseño factorial de ocho celdas. Ese factorial es **fase 2** y esta condicionado a que los brazos simples discriminen: un factorial sobre brazos que no se separan entre si es ilegible.

**sdd-first entra sin castigo previo.** Es del mismo autor que este repositorio [R39], y esa autocorrelacion se declara como confundido. Pero el canal por el que la autoria sesga —el juicio de quien evalua— esta cerrado por diseño: la puntuacion es el codigo de salida de una suite sellada antes de que corra ningun brazo, sin intervencion humana. Queda un residuo real y es otro: **quien escribe el enunciado tambien escribio sdd-first**, y podria elegir sin proponerselo un objetivo con su forma. Se acota calibrando el enunciado **solo contra el brazo control** (Fase 0.B) y se declara. Asimetria de lectura que MUST aplicarse: si T3 pierde, el resultado es mas creible que cualquier otro de este corpus, porque va contra el interes de quien midio; si gana, la ventaja MUST leerse con la reserva puesta.

### Rondas

- **R1 — greenfield.** Del enunciado sellado al codigo, en workspace limpio.
- **R2 — evolucion.** Sobre el workspace que dejo **ese mismo rep** en R1 —nunca sobre un workspace comun— se entrega el requisito adicional sellado, y se vuelve a correr la suite **entera**: los e2e de R1 mas los del requisito nuevo.

R2 no es un agregado: es la mitad que decide la equidad del diseño. Una unica ronda greenfield premia a la orientacion declarada de Spec Kit (`ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md`, D1) y le da a OpenSpec y a sdd-first un escenario donde su mecanismo no puede ejercerse. Sin R2 el resultado seria un artefacto del fixture.

### Objetivo: enunciado sintetico propio

- **Enunciado**: escrito para este experimento, sellado antes del primer rep de tratamiento.
- **Suite e2e**: escrita para este experimento, sellada, **nunca visible para ningun brazo**.
- **Requisito de R2**: escrito y sellado junto con lo anterior, y no derivable del enunciado de R1.

**Por que sintetico y no una suite publica preexistente.** Se evaluaron dos candidatas de suite ajena y verificadas —`toml-test`, caja negra por stdin/stdout, y Todo-Backend, suite HTTP apuntada a una URL—. Las dos tienen el mismo defecto fatal para este diseño: son objetivos populares, y por lo tanto abundantes en el entrenamiento de los modelos. El riesgo dominante no es la contaminacion en abstracto sino su consecuencia, el **techo del brazo control**: si C0 pasa casi todo sin metodo, ninguna ceremonia puede mostrar diferencia y el experimento cierra sin veredicto. Es exactamente el modo en que A-04 cerro NO APTO dos veces (`../a04-conducta-agente/RESULTADO-EXPERIMENTO-A4.md`), y el item #9 de `../../agenda/BACKLOG-INVESTIGACION.md` lo dejo escrito: **la conducta medida tiene que ser cara para el harness**.

El costo de elegir sintetico esta declarado y es real: **la suite deja de ser ajena**. Quien evalua la escribio. Lo que sostiene su validez no es la independencia de autoria sino tres propiedades mecanicas: se sella antes de correr, ningun brazo la ve, y se puntua sin juicio.

### Contrato de invocacion

El enunciado sellado MUST fijar **como se invoca el sistema generado** (ejecutable y forma de entrada/salida, o puerto y rutas). No es un detalle de operacion: es lo que elimina por construccion la reconciliacion post-hoc entre lo que el brazo produjo y lo que la suite espera. Un brazo que no respeta el contrato puntua lo que puntue la suite, y no se repara.

**El enunciado sellado MUST fijar tambien el runtime.** Lenguaje y versión, y el comando exacto de construcción y arranque. Si cada brazo elige *stack* libremente, el contenedor de evaluación puede fallar por incompatibilidad de infraestructura, y esa falla se leería como `0` del brazo: sería contaminación del dato por una causa ajena al método. El runtime es parte del enunciado y por lo tanto es idéntico para todos los brazos, `C0` incluido; el contenedor donde se puntúa se sella contra ese mismo runtime (§Sello).

### Fase 0.A — caracterizacion de interfaces y ensayo general

**Corre primero, antes que cualquier otra cosa.** Todo el resto del diseño asume dos cosas que hoy estan sin verificar: que cada brazo **se puede invocar** bajo condiciones sellables, y que su producto **se puede medir** con el mismo instrumento que los demas. Si alguna de las dos falla, falla a mitad de tanda, que es el peor momento — es la misma sorpresa que bloqueo la Fase 0 de A-04, donde la sonda de contexto resulto no ser portable (`../../../experimentosdd-a4/entorno/ENTORNO-1B.md`).

**Corre antes que Fase 0.B, y el orden no es indiferente.** El ensayo de 0.A usa un enunciado *estructuralmente análogo* al real, así que el enunciado real MUST existir al menos en borrador cuando 0.A empieza; y 0.B lo ajusta hasta tres veces. De ahí el invariante que hace válida la analogía hacia atrás: **los ajustes de 0.B MUST NOT alterar el contrato de invocación —runtime incluido— ni el orden de magnitud del enunciado**, que son el eje sobre el que se construyó el análogo. Si un ajuste los altera, las fichas de interfaz ya cerradas se re-verifican antes del sello.

**Producto de la fase: una ficha de interfaz por brazo**, con siete campos y ninguno inferido:

| campo | que responde | por que es bloqueante |
|---|---|---|
| **Entrada** | Que recibe el brazo y en que forma: texto suelto, archivo, comando de scaffolding previo, estructura de directorios esperada | Si dos brazos no pueden recibir el mismo enunciado, la neutralidad se rompe en el primer paso |
| **Secuencia de invocacion** | Los comandos o pedidos exactos, en orden, tomados de la documentacion oficial de esa herramienta, **empezando por el comando de instalacion de su canal oficial** | Es la **definicion del tratamiento**, no una mitigacion: lo que se compara es cada metodo ejercido como su propio autor lo indica. El canal de instalacion es parte de eso y no un preliminar de operacion: es lo que fija que se sella (§Sello, «Cada brazo por su canal») |
| **Condicion de termino** | Como declara el brazo que termino — tareas completas, cambio listo para archivar, coverage mapping satisfecho, workflow cerrado, o el agente diciendo que termino | Sin esto, cada brazo se detiene en un punto arbitrario elegido por el operador |
| **Tope duro** | Limite de turnos, tokens y reloj tras el cual la corrida se corta. Los de turnos y reloj MAY ser por brazo; el de **tokens MUST ser comun a todos** y se calibra acá, generoso (§Protocolo de medicion de costo) | Un brazo que no termina nunca no puede bloquear la tanda. Y un tope de tokens por brazo decidiría H3 por un parámetro del operador, porque `S2` se cuenta hasta el tope |
| **Respuesta a prompts interactivos** | La cadena **única y sellada** con que se responde a toda pregunta que la herramienta haga en runtime, y la constancia de que el brazo avanza con ella. Propuesta: «Procedé con las asunciones mínimas derivables del enunciado; no hay información adicional disponible.» | T1 (`/speckit.clarify`) y T4 (confirmaciones de fase) están diseñados para preguntarle al operador. Si el operador contesta con conocimiento de dominio, inyecta información que `C0` nunca recibe: no es habilidad de conducción, es contaminación del tratamiento. Detalle y reserva en §Riesgos, punto 3 |
| **Artefacto entregado** | Que queda en el workspace y como se lanza | Es el otro extremo del contrato: sin esto la suite no tiene contra que correr |
| **Contabilidad de costo** | Si el consumo es legible de forma **identica** para todos los brazos, si **incluye subagentes**, y si expone entrada fresca, lectura de cache y salida por separado | Si no, `S2` no es comparable y **H3 no se puede evaluar**; MUST decidirse aca y no al mirar los datos. Protocolo completo en §Protocolo de medicion de costo |

**El contrato universal tiene dos extremos y hasta ahora este diseño solo escribio uno.** El de salida —el contrato de invocacion del sistema generado— ya estaba. El de entrada no: lo unico neutral entre brazos es el **enunciado**, y todo lo que viene despues es especifico de cada herramienta. Eso no es un defecto que haya que emparejar. Emparejarlo seria peor: obligar a Spec Kit a arrancar como arranca OpenSpec es medir una version mutilada de los dos. Lo neutral es el **enunciado y el criterio de terminacion**; lo especifico es la secuencia, y va sellada tal como la escribe la documentacion de cada fuente.

**El ensayo general corre sobre un enunciado descartable, NUNCA sobre el real.** Un ensayo sobre el enunciado sellado lo expondria a los brazos y quemaria el sello: dejaria de ser una primera corrida. El ensayo usa un enunciado **estructuralmente analogo y de contenido distinto** —mismo tipo de contrato de invocacion, tamaño comparable— y sus resultados **MUST NOT usarse como dato** de ninguna metrica. Se descarta entero al terminar; lo unico que sobrevive son las siete fichas y el veredicto de factibilidad.

**El instrumento que puntua el ensayo es un smoke-test auxiliar, no la suite sellada.** La suite sellada está atada al enunciado real y es invisible para los brazos, así que no puede puntuar un ensayo sobre un enunciado descartable. Para eso se escribe un **smoke-test mínimo del enunciado descartable: una o dos aserciones de entrada/salida**, cuyo único trabajo es probar que el circuito construir → ejecutar → capturar código de salida cierra. MUST NOT construirse una suite e2e completa del enunciado descartable: duplicaría el trabajo del fixture antes del sello.

- Su veredicto es **binario, go/no-go, y nunca un puntaje**. Un puntaje del ensayo sobrevive en la memoria de quien lo vio aunque el archivo se descarte, y ahí deja de ser cierto que ningún brazo fue observado antes del sello.
- MAY aprovecharse para **ejercitar el procedimiento de validación del instrumento** sin tocar la suite real: correr el smoke-test contra un esqueleto vacío descartable y verificar que da 0. Es lo único que prueba ese procedimiento antes de que el sello dependa de él (§Definicion operacional, «Validacion del instrumento»).

**Veredicto por brazo, y es go/no-go.** Un brazo entra a la poblacion definitiva solo si sus siete campos estan completos y el ensayo produjo un artefacto que el smoke-test pudo puntuar. La ficha de interfaz de cada brazo admitido se sella junto con el fixture.

- **Dos corridas por brazo, y la regla es asimetrica.** Una sola corrida no distingue una falla intermitente de invocación de una imposibilidad real. **Una falla ⇒ se investiga y se repite; dos ⇒ el brazo se excluye, con el modo de falla escrito.** La asimetría tiene motivo: un falso positivo se paga con un INEJECUTABLE a mitad de tanda, que ya tiene regla escrita; un falso negativo se paga publicando «esta herramienta no se puede invocar de forma sellable», que es una afirmación pública sobre software de terceros.
- **La poblacion que sobrevive condiciona que hipotesis siguen vivas**, y con qué piso de autoría se sella: §Criterio de exito, «Admisibilidad por hipotesis».

### Que pasa si la imposibilidad aparece igual, a mitad de camino

La regla se escribe ahora, antes de que el caso exista, porque improvisarla despues es exactamente por donde entran los grados de libertad post-hoc.

- **Si aparece en Fase 0.A** (antes del sello): el brazo **queda fuera de la poblacion**, con el motivo escrito. Y eso no es una perdida silenciosa: «no se pudo invocar de forma sellable» es un **hecho sobre la herramienta** y se reporta como tal, de la misma clase que el que ya deja a Kiro afuera. Un metodo que no se puede ejercer de forma reproducible es informacion para quien evalua adoptarlo.
- **Si aparece despues del sello, con tandas en curso**: el brazo se declara **INEJECUTABLE**, sus celdas se anulan, y la bateria **continua con los demas**. Se reporta con el punto exacto donde fallo.
  - MUST NOT dispararse un rediseño del fixture. El enunciado no se toca: a esa altura ya hay datos de tratamiento vistos.
  - MUST NOT ajustarse la secuencia de invocacion del brazo para que funcione. Cambiar el tratamiento despues de ver como le fue es reemplazar el experimento por otro. Si la secuencia corregida vale la pena, es una **pasada distinta**, con enmienda fechada y su propio sello.
  - Un brazo INEJECUTABLE **no descalifica** la bateria de su harness: los demas brazos siguen comparandose contra el control, con la poblacion reducida declarada en el veredicto.
  - **Que distingue esta bateria incompleta de la que §Replicacion por harness descarta entera.** No es cuántas celdas faltan: es **quién eligió** que faltaran. Una batería **parcial por elección del operador** —correr algunos brazos acá y otros allá— se descarta entera, porque esa elección es el grado de libertad post-hoc que la regla existe para cerrar. Una batería **parcial por INEJECUTABLE**, en cambio, es completa en el único sentido que importa: se intentaron los cinco brazos, y el que falló lo hizo por una causa documentada, con el punto exacto registrado y sin que nadie eligiera dónde correrlo. La primera se descarta; la segunda vale con la población reducida declarada. La fila «completitud de bateria por harness» de §Sello aplica exactamente esta distinción.
- **Si el problema es de medicion y no de invocacion** —el brazo produjo algo pero la suite no lo puede puntuar—: no hay adaptador. El contrato de invocacion es parte del enunciado sellado, asi que incumplirlo puntua lo que puntue la suite, normalmente `0`. Es resultado, no incidente.
- **Si el brazo agota el tope duro sin declararse terminado**: es **entrega fallida**, no VOID. Se puntua el artefacto que haya quedado. La distincion importa y va sellada: VOID es cuando falla el **instrumento** —el harness aborto, se corto por permisos, error de entorno—; agotar el tope es cuando falla el **brazo**, y eso es exactamente lo que el experimento existe para observar.

### Fase 0.B — calibracion de dificultad, y la frontera con el Principio V

Con enunciado propio la dificultad es una variable de diseño. Eso resuelve el techo **y** abre la puerta a fabricar el resultado. Las dos cosas son el mismo mecanismo, separadas unicamente por estas siete condiciones, que MUST cumplirse todas:

1. La **banda objetivo del control** se declara antes de la primera corrida de calibracion. Valor propuesto, a sellar: `C0` en R1 pasa entre **40% y 80%** de los e2e de R1.
2. La calibracion ve **exclusivamente** datos del brazo `C0`. Ningun brazo tratamiento corre hasta que enunciado, suite y requisito de R2 estan sellados y hasheados.
3. El **tope de rondas de ajuste** se declara antes y se cumple. Valor propuesto, a sellar: **3**. Si a la tercera el control no cae en banda, B-09 cierra sin correr tratamientos y reporta el hallazgo de calibracion.
4. Sellado el fixture, los tratamientos corren una vez. No hay edicion del sello despues del primer rep de tratamiento.
5. **La calibracion tambien corre R2 sobre `C0`, y con piso declarado.** H2a y H2b son NO CONCLUYENTE por piso si ningún brazo regresiona, y el diseño exige verificar antes de sellar que exista margen; sin correr R2 sobre el control no hay forma de producir ese dato. Piso propuesto, a sellar: **`S1(C0) ≥ 1` en la mayoría de los reps de calibración**.
6. **Regla de parada de R2, y es lo que impide fabricar H2.** Se sella el **primer** candidato de requisito de R2 que cumple el piso; MUST NOT seguir ajustándose para aumentar `S1(C0)`. El motivo es que el sesgo tiene dirección conocida: H2a y H2b piden `S1` menor que `S1(C0)`, así que «más regresión del control» es «más fácil que la hipótesis se sostenga», y optimizar en esa dirección es exactamente la búsqueda que el Principio V prohíbe. Orden fijo: R2 se calibra **sólo sobre un candidato que ya cayó en banda en R1**, y si no aparece margen se ajusta **el requisito de R2**, nunca el enunciado de R1 — moverlo invalidaría la banda ya alcanzada y reiniciaría el conteo de la condición 3, que cubre el par R1+R2 y no cada ronda por separado.
7. **Ninguna corrida de calibracion es dato.** Las corridas de `C0` que consuma esta fase —en R1 y en R2— existieron para calibrar y **MUST NOT reutilizarse como línea base de `C0`** en ningún veredicto: la línea base de un experimento no se elige entre varias candidatas conociendo cuál favorece a una hipótesis. Se conservan como bitácora de calibración, no como celdas (§Plan de captura de datos).

**La validacion del instrumento abre esta fase y se repite en cada ronda de ajuste.** La suite tiene que discriminar antes de que sus números signifiquen algo, así que la validación contra los dos controles conocidos (§Definicion operacional) MUST correrse **antes** de la primera corrida de calibración: sin ella, una banda de `C0` fuera de rango no distingue un enunciado mal calibrado de una suite que no mide. Y no es un paso único: cada ronda de ajuste cambia el enunciado, y con él la suite **y la implementación de referencia**, que es una solución de ese enunciado. La validación es condición de cierre de cada ronda, no un trámite de apertura.

**La banda se verifica en cada harness; el fixture se calibra en uno solo.** La calibracion —ajustar el enunciado hasta que el control caiga en banda— ocurre **una vez**, en el primer harness, y termina con el sello. Todo harness posterior corre su propio `C0` y se comprueba contra la **misma** banda ya declarada: si cae adentro, su bateria es APTA; si cae afuera, el **harness** es NO APTO, se declara y sus datos no entran al veredicto. Lo que nunca se hace es mover el fixture para acomodar a un harness — a esa altura ya hay datos de tratamiento vistos, y ajustar seria la busqueda que el Principio V prohibe.

**Por que esto no es lo que A-04 prohibio.** El `MUST NOT` de A-04 veda subir la presion del escenario despues de ver una tasa, buscando una configuracion donde el tratamiento pueda mostrarse — eso es busqueda. Aca el ajuste ocurre **antes de que exista un solo dato de tratamiento**, contra un unico brazo, con banda y tope declarados por adelantado. Es calibracion de dificultad de item contra un control ciego. La frontera es fina y la señal de que se cruzo es una sola: estar ajustando el enunciado despues de ver como le fue a algun brazo que no sea `C0`.

### Replicacion por harness

El harness **MAY ser mas de uno**, y esa es la unica via disponible para atacar el confundido mas grave del diseño. Pero entra bajo una condicion que no admite excepcion:

> **Un harness que corre, corre la bateria completa.** Los cinco brazos, las dos rondas y los tres reps. Un harness parcial **por eleccion del operador** no aporta dato y su corrida se descarta entera. Un harness al que le falta un brazo por **INEJECUTABLE declarado**, con su punto de falla registrado, no es parcial en este sentido y sus datos valen con la poblacion reducida declarada (§Que pasa si la imposibilidad aparece igual).

La condicion no es burocratica. Si un harness pudiera correr solo algunos brazos, la eleccion de cuales correr en cual seria un grado de libertad post-hoc: bastaria con completar en un segundo harness el brazo al que le fue mal en el primero. La bateria completa cierra esa puerta por construccion.

**Que se puede leer con dos harnesses y que no.** La regla la fijo A-04 y se hereda textual (`../a04-conducta-agente/PRUEBA-PISO-RUIDO-A4.md`): **las tasas absolutas entre harnesses MUST NOT compararse; solo son comparables los deltas dentro de cada harness.** Aplicado aca:

- **Admisible**: comparar la **direccion** del delta brazo-contra-`C0` obtenido en el harness A con la direccion del mismo delta en el harness B. Es una lectura categorica —replica o no replica—, no una diferencia de magnitudes.
- **MUST NOT**: afirmar que un harness produce mejores resultados que otro, ni promediar celdas de harnesses distintos, ni leer una diferencia de magnitud entre ellos como dato.

**Lo que la replicacion compra, y es mucho.** Con un solo harness, todo resultado de B-09 es «metodo X bajo este harness» y no hay como distinguir un efecto del metodo de un efecto del andamiaje. Con la bateria repetida entera en un segundo harness —que trae ademas otra familia de modelo—, una direccion que se sostiene en los dos descarta a la vez «es este harness» y «es este modelo». Es exactamente la forma de evidencia que A-04 pasada 1b produjo sobre el techo, y la mas fuerte que este repositorio sabe construir hoy.

**Lo que no compra.** El confundido harness/familia-de-modelo sigue siendo inseparable **dentro** de cada harness: cada uno trae su modelo y no se los puede cruzar. La replicacion no separa esos dos ejes, los hace **menos probables como explicacion unica**. Es una diferencia real y MUST escribirse asi.

**El fixture se sella una sola vez, globalmente.** Un segundo harness MUST NOT disparar recalibracion del enunciado, la suite ni el requisito de R2. Si el control de ese harness cae fuera de la banda declarada, el **harness** es NO APTO y su bateria se declara y se excluye del veredicto; el fixture no se mueve. Recalibrar por harness reabriria la puerta que la Fase 0.B cierra: seria ajustar la dificultad con datos de tratamiento ya vistos en el primer harness.

**Orden y contaminacion.** Las baterias corren independientes, sin workspace, cache ni artefacto compartido. El orden en que se corren los harnesses se registra y se declara; no se controla.

### Muestra y duracion

- Por harness: 5 brazos × 2 rondas × 3 reps = **30 corridas**, mas las de `C0` que consuma la verificacion de banda.
- Minimo para cerrar: **un** harness completo. Cada harness adicional suma 30 corridas y sube el techo de lo afirmable un escalon.
- Duracion: por estimar tras la Fase 0.A, que es la primera vez que se conocera el costo real de una corrida.

`n`=3 por celda es chico y se declara como limitacion desde el diseño. Alcanza para leer **dispersion**, no para estimar tasas. Es la resolucion minima que exige el item #7 del backlog: si el rango entre los 3 reps de un brazo es del orden de la diferencia entre brazos, no hay señal que reportar.

## Sello

| componente | que queda sellado (valor o identificador) | escalon | mecanismo | que hace el verificador si diverge |
|---|---|---|---|---|
| tratamiento — los cuatro brazos | **dos** identificadores por brazo: el identificador inmutable de origen que admita **su** canal oficial de distribucion, **y** el hash del artefacto ya instalado en la tanda. Los valores concretos son producto de Fase 0.A y se registran por tanda, no se fijan aca | 1 + 2 | cada brazo se instala por el canal que su propia documentacion prescribe, en una ruta privada por tanda, nunca desde un arbol de trabajo local ni desde un puntero movil; el hash se toma **despues** de instalar. Detalle del criterio abajo, «Cada brazo por su canal» | detiene el rep y explicita identificador y hash esperados vs. obtenidos. Si el canal de un brazo difiere entre harnesses, registra la divergencia de hash y no detiene la bateria |
| ficha de interfaz por brazo | los siete campos de Fase 0.A, hasheados: entrada, secuencia de invocacion, condicion de termino, tope duro, respuesta a prompts interactivos, artefacto entregado, contabilidad de costo | 1 + 2 | se fija en Fase 0.A sobre un enunciado descartable y se sella junto al fixture; la secuencia sale de la documentacion oficial de cada fuente, no de nuestra invencion; el tope de tokens es un valor unico comun a todos los brazos y la respuesta a prompts es una cadena unica comun | detiene si el hash no coincide, y explicita que campo cambio |
| fixture — enunciado, suite e2e, requisito R2 | hash de los tres archivos | 1 + 2 | archivos de solo lectura fuera del workspace del rep; el workspace recibe **solo** el enunciado | detiene si algun hash cambia entre reps |
| instrumentos de validacion — implementacion de referencia y esqueleto vacio | hash de los dos artefactos | 1 + 2 | viven donde vive el fixture, fuera del workspace del rep, y **ningun brazo los ve en ningun momento**: la implementacion de referencia es una solucion completa del enunciado sellado, asi que su fuga es equivalente a filtrar la suite. Se rehacen y se re-hashean en cada ronda de ajuste de Fase 0.B | detiene si algun hash cambia entre reps, o si la validacion 100%/0% no reproduce |
| contenedor de evaluacion | identificador de imagen o receta de entorno, con el runtime del enunciado | 1 + 2 | la suite corre siempre en ese contenedor, sin red y sin acceso a este repositorio; no se re-resuelven dependencias entre reps | detiene y registra la divergencia de entorno de puntuacion |
| entorno de ejecucion | workspace limpio por rep, `env -i`, `HOME` temporal, sin fuentes de ajustes heredadas, **y el inventario de lo que el harness tiene activo al abrir el rep** | 1 + 2 | patron heredado de A-04 pasada 1b, que verifico que ninguna instruccion de proyecto, usuario ni memoria llega al rep; extendido al estado que los brazos **instalan** fuera del workspace, abajo en «Estado que el brazo deja fuera del workspace» | detiene y registra la fuga detectada, o la divergencia entre el inventario y el brazo en curso |
| harness y modelo | version efectiva **al abrir cada tanda**, no al escribir este diseño | 3 | se registra por tanda; una diferencia entre tandas es legitima y se declara junto al resultado | ninguno — declarado sin verificador |
| completitud de bateria por harness | 5 brazos × 2 rondas × 3 reps, **menos los brazos declarados INEJECUTABLE con su punto de falla registrado** | 2 | el runbook verifica que la bateria de un harness este entera antes de admitir sus datos al veredicto, y que toda celda faltante tenga su declaracion de INEJECUTABLE fechada | descarta la bateria completa de ese harness si falta una celda **sin** esa declaracion — que es la bateria parcial por eleccion del operador; con la declaracion presente, admite la bateria con la poblacion reducida declarada |

**Cada brazo por su canal, y emparejar los canales seria el error.** La redacción anterior sellaba «el commit del clon vendored» de los cuatro tratamientos como si compartieran unidad de distribución. No la comparten: cada fuente distribuye su método como quiere —repositorio, paquete publicado en un registro de lenguaje, plugin del harness— y esa elección es de su autor, no nuestra. Adoptar una unidad única para los cuatro —el repositorio, digamos, por ser la más prolija de hashear— mediría en los demás una variante que ningún adoptante ejerce, contra la definición de tratamiento de este diseño: cada método **ejercido como su propio autor lo indica** (§Fase 0.A, «Secuencia de invocacion»).

Lo que se empareja no es el canal sino el **piso de reproducibilidad**, y por eso se sellan dos cosas y no una:

1. **Identificador inmutable de origen** — la forma que ese canal admita: tag, versión publicada, commit. Nunca un puntero móvil: un alias de «lo último», una rama, un enlace del sistema de archivos a un árbol de trabajo.
2. **Hash del artefacto ya instalado en la tanda**, no del origen. Es el que cierra el hueco real: un identificador de origen no captura las dependencias transitivas que la instalación resuelve, y lo que el brazo ejerce es lo instalado. Es además la única forma común a canales heterogéneos, porque se toma del resultado y no de la procedencia.

Dos consecuencias que se siguen de esto y MUST aplicarse sin excepción por brazo:

- Si el canal oficial de un brazo **no admite** identificador inmutable, no se improvisa uno: el hash del artefacto instalado pasa de comprobación a único anclaje, y esa reducción se declara. Que un método no se distribuya de forma pinneable es un hecho reportable sobre esa herramienta, de la misma clase que el que deja a Kiro fuera de la población (§Brazos).
- Si el canal oficial de un brazo **difiere entre harnesses**, su artefacto puede diferir entre baterías **por el canal y no por el harness**, que es justo lo que §Replicacion por harness existe para leer. El hash lo vuelve detectable —dos hashes distintos se ven— pero no lo elimina; si difieren, MUST declararse junto a cualquier lectura entre harnesses.

**Escalon 3, declarado sin verificador.** Dentro de un harness, este y su familia de modelo son **inseparables**: A-04 pasadas 1 y 1b lo establecieron (`../a04-conducta-agente/RESULTADO-EXPERIMENTO-A4.md`, item #10 del backlog). Con un solo harness, todo resultado de B-09 es «metodo X **bajo este harness**», nunca «metodo X», y MUST escribirse asi en el resultado y no en una nota al pie. La unica mitigacion disponible es la replicacion de la bateria entera en un segundo harness (§Replicacion por harness), que no separa los dos ejes pero los vuelve menos plausibles como explicacion unica.

**Dos entornos, dos filas, y no se cumplen con el mismo mecanismo.** La tabla los sella por separado y conviene decir por qué, porque fusionarlos es el error fácil. El **contenedor de evaluacion** es donde corre la suite, sin red y sin acceso a este repositorio, y su exigencia dura es que no se re-resuelvan dependencias entre reps a lo largo de las 30 corridas: una imagen sella eso mejor que una receta, y por eso la fila admite las dos formas pero la imagen es la vía recomendada. El **entorno de ejecucion** es donde corre el brazo, y ahí la exigencia es la opuesta: los brazos **necesitan** red —instalan por su propio canal (§Sello, «Cada brazo por su canal»)— y terminal, así que se aísla con el patrón de A-04 —workspace limpio, `env -i`, `HOME` temporal— y no encapsulándolo. Un brazo cuyo método vive como plugin del harness ni siquiera puede encapsularse sin salirse de su canal oficial.

**Estado que el brazo deja fuera del workspace.** El aislamiento por workspace limpio alcanza para el brazo que siembra su metodo **dentro** del proyecto, y no alcanza para ninguno de los que se **instalan**: una herramienta global o un plugin del harness aterrizan en el entorno del usuario, no en el proyecto, y por lo tanto sobreviven al rep que los instalo. La regla, entonces, es general y no un cuidado especial de un brazo: **todo estado que un brazo deja fuera del workspace —herramientas globales, plugins, skills, caches de instalacion— es parte del rep y muere con el.** El `HOME` temporal de la fila es el mecanismo; lo que sigue es por que no basta con tenerlo.

- **El caso peor no es un tratamiento contaminando a otro: es cualquiera contaminando a `C0`.** Un metodo que se instala como plugin puede traer un *hook* de arranque de sesion, es decir, activarse **sin que nadie lo invoque**. Si sobrevive a su rep, el brazo siguiente lo ejerce sin saberlo; y si ese brazo es el control, la linea base deja de ser «sin metodo» y H1 —la unica hipotesis que responde la pregunta que origina el experimento— se evalua contra una referencia falsa. No se veria como un error: se veria como un control que rindio mejor de lo esperado.
- **Verificacion positiva por rep, porque «deberia estar limpio» no es dato.** Antes de cada corrida se inventaria lo que el harness tiene activo —herramientas en el PATH, plugins, skills— y MUST coincidir **exactamente** con el brazo en curso; para `C0`, vacio. El inventario se conserva por rep (§Plan de captura). Es la misma clase de sonda con que A-04 pasada 1b verifico que ninguna instruccion heredada llegaba al rep, y es lo que convierte el aislamiento en algo verificado y no supuesto.
- **El aislamiento obliga a reinstalar por rep, y eso mueve la granularidad del hash.** Con `HOME` temporal, un brazo que se instala lo hace de nuevo en cada rep. Para un canal sin identificador inmutable (§Riesgos 3-quinquies) eso abre contaminacion **hacia adentro**, entre reps del mismo brazo: dos reps podrian ejercer versiones distintas. Por eso el hash del artefacto instalado se toma **por rep** y no por tanda — es lo unico que vuelve esa deriva detectable.
- **MUST NOT resolverse por orden de corrida.** «Correr ultimo al brazo que ensucia» no es un mecanismo: el orden se registra y no se controla (§Replicacion por harness), y la primera re-corrida por VOID lo rompe.

**La autenticacion es el punto donde este aislamiento puede ceder, y es bloqueante de Fase 0.A.** Un `HOME` temporal no lleva credenciales, y un harness que exige inicio de sesion interactivo no arranca sin ellas. Las dos salidas obvias son malas: renunciar al `HOME` temporal reabre todo lo anterior, y responder a un login interactivo por rep convierte 30 corridas en un procedimiento manual irreproducible. Lo que MUST establecerse en Fase 0.A, antes del sello, es si cada harness admite **autenticacion no interactiva** —credencial inyectada por entorno o equivalente— y, de admitirla, montar en el `HOME` temporal **solo** lo que autentica y **nada** de configuracion, plugins ni skills del usuario: la credencial es lo unico que legitimamente cruza el aislamiento. Dos condiciones que van con eso: la credencial MUST NOT quedar en ningun artefacto conservado —los transcripts y workspaces se archivan como dato (§Plan de captura)—, y si un harness **no** admite autenticacion no interactiva, eso es un hecho sobre ese harness y decide si puede alojar una bateria, del mismo modo que la banda de `C0` decide si es APTO.

**Regimen de permisos.** A diferencia de B-07, aca los brazos **necesitan** terminal: los CLI de T1 y T2 son el metodo. El regimen se hereda de A-04 —lista de permitidos con degradacion graceful, que sostuvo 0 VOID en dos harnesses— y no de B-07, cuyo `halt-on-permission` produjo corridas nulas estocasticas (item #5 del backlog). MUST definirse en el runbook, no aca.

## Metricas

- **Primaria — `P`**: proporcion de e2e de la suite sellada que aprueban, por brazo y por ronda.
- **Secundarias**:
  - **`S1` regresion**: e2e que aprobaban en R1 y fallan en R2, dentro del **mismo rep**, contados sobre el **subconjunto común** del par comparado: los e2e de R1 que **los dos brazos** de esa comparación aprobaron en R1. El subconjunto se recomputa para cada par y es, por construcción, idéntico para los dos miembros del par.
    - **Por qué no es un conteo crudo sobre toda la suite.** Un brazo con mal desempeño en R1 tiene techo de regresión bajo —si aprobó 1 de 10, su `S1` máximo es 1— y uno con buen R1 puede acumular más regresión en términos absolutos aunque su mecanismo de evolución sea mejor. Un conteo crudo premiaría estructuralmente al brazo que rindió peor en R1, que es lo contrario de lo que H2a y H2b preguntan.
    - **Por qué el subconjunto común y no una tasa.** Normalizar por la base de cada brazo (`regresados / aprobados-en-R1`) arregla el techo pero introduce el sesgo inverso —romper 1 de 1 da 100%, romper 1 de 8 da 12,5%— y vuelve a `S1` una función del valor de `P` en R1. El subconjunto común iguala el denominador **por construcción** y no por división: los dos brazos se miden sobre exactamente los mismos e2e.
    - **No computable.** Si el subconjunto común de un par tiene menos de **3** e2e —valor propuesto, a sellar—, ese par no es comparable en ese rep. Consecuencias en §Criterio de exito, «Admisibilidad por hipotesis».
  - **`S2` costo**: tokens consumidos por corrida, reportados en tres componentes —entrada fresca, lectura de cache, salida— mas su total, que es el valor primario. Protocolo en §Protocolo de medicion de costo.
  - **`S3` reloj**: tiempo de pared por corrida.
  - **`S4` nulidad**: proporcion de corridas VOID por brazo.

### Protocolo de medicion de costo (`S2`)

Sin esto `S2` no mide el costo del **metodo** sino el regimen de contabilidad del **harness**, y H3 seria un artefacto de instrumentacion. Todo lo de abajo MUST resolverse en Fase 0.A, antes del sello.

**Frontera de la corrida.** Se cuenta desde la primera invocacion de la secuencia sellada del brazo hasta su condicion de termino o su tope duro, lo que ocurra antes.

| entra | no entra |
|---|---|
| comandos de scaffolding del propio brazo (`specify init`, `openspec init`, siembra de sdd-first) | nuestra instrumentacion: hashes, montaje del workspace, copia del tratamiento |
| todos los turnos del agente, incluidos los reintentos que el brazo decida por su cuenta | la corrida de la suite e2e, que ocurre fuera del workspace y no es costo del brazo |
| **todo lo consumido por subagentes**, atribuido a la corrida que los lanzo | las corridas VOID, que se re-corren y no acumulan |

**El tope de tokens es comun a todos los brazos, y ese es el unico campo de la ficha que no admite variacion por brazo.** El tope duro (§Fase 0.A, ficha de interfaz) fija límites de turnos, tokens y reloj. Los de turnos y reloj MAY fijarse por brazo: no son la unidad de `S2`. El de **tokens** MUST ser único, común y sellado, porque `S2` se cuenta hasta la condición de término **o el tope**, y un tope por brazo haría que H3 —la hipótesis de que un brazo consume más que los demás— se decidiera por un parámetro que fija el operador brazo por brazo. Un tope más bajo para T4 la refuta por construcción; uno más alto la confirma por construcción. El valor se calibra en Fase 0.A —la primera vez que se conoce el costo real de una corrida— y se fija **generoso**: su función es impedir que un brazo bloquee la tanda, no discriminar entre brazos.

**`S2` censurado.** Una corrida que alcanza el tope de tokens produce un `S2` que es una **cota inferior**, no un valor, y se marca como censurado en el dato crudo. H3 MUST NOT sostenerse sobre celdas censuradas: si T4 topea y los demás no, lo afirmable es «T4 alcanzó el techo de tokens y ningún otro brazo lo alcanzó», que es categórico y más fuerte que comparar números truncados. La censura no cambia el trato de esa corrida para `P`: agotar el tope sigue siendo entrega fallida y puntúa (§Definicion operacional).

**La linea de subagentes no es un tecnicismo: decide H3.** El modo de falla reportado de Superpowers es precisamente lanzar muchos subagentes ([R47], «it started a workflow that spawned like a 100 sub agents»). Un contador que no atribuya el consumo del subagente a la corrida padre subcontaria de forma sistematica **justo al brazo del que trata H3**. Fase 0.A MUST verificarlo explicitamente, no asumirlo.

**Descomposicion obligatoria.** `S2` se reporta siempre en tres componentes —entrada fresca, lectura de cache y salida— y ademas como total. La primaria es el total; la descomposicion **nunca** se omite.

El motivo no es prolijidad. Los brazos ceremoniales releen su propia spec muchas veces, asi que generan mucha lectura de cache, que es la clase de token mas barata. Un unico numero que la sume a peso completo **castiga a los brazos ceremoniales por una propiedad del harness**, no por una del metodo; uno que la excluya los favorece por lo mismo. Con los tres componentes publicados, cualquier lector puede recomputar bajo la ponderacion que quiera, y el sesgo deja de estar escondido en un total.

**Fuente y verificacion.**

1. **Primaria**: el reporte del propio harness — admisible **solo si** Fase 0.A verifico que incluye subagentes y que expone los tres componentes.
2. **Cruzada**: el uso reportado por el proveedor, acotado por ventana temporal, sobre un subconjunto declarado de reps. Es grueso y diferido, pero es independiente del harness y cuenta todo. Sirve como comprobacion de orden de magnitud, no como valor de reemplazo.
3. **Si ninguna de las dos sirve**: `S2` queda **descriptiva** y **H3 se retira del criterio de exito antes del sello**. `S3` (reloj) MUST NOT usarse como sustituto: confunde costo con latencia del proveedor.

**Esquema de contabilidad, versionado.** Como se cuentan los tokens cambia entre versiones de harness, y la version es escalon 3 —se sella al abrir cada tanda, no al escribir este diseño—. Por rep se registra el esquema de contabilidad vigente; un cambio a mitad de bateria se declara junto al resultado como confundido conocido y no removido.

**Entre harnesses no se comparan valores de `S2`.** Hereda sin excepcion la regla de §Replicacion por harness: distintos harnesses cuentan cosas distintas, y normalizarlos seria fabricar un numero. Lo unico comparable es la **direccion** —si el brazo mas caro es el mismo en los dos— y esa lectura es categorica.

## Documentos que esperan este resultado

| documento | que afirma hoy | que lo cambiaria |
|---|---|---|
| `../../software/ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md` §7 | «Como se comportan en un proyecto real. Ninguna se corrio» y «Cual funciona mejor. Ninguna fuente reporta medicion» | Cualquier veredicto de H1, incluido el nulo: pasaria a existir una medicion propia, con su alcance declarado |
| `../../software/ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md` §6 | La tabla de orientacion por escenario dice cual mecanismo atiende cada situacion, y declara dos veces que no ordena por calidad | Un resultado con señal daria, por primera vez, dato de desempeño para alguna de esas filas — o confirmaria que no lo hay |
| `../../software/PLAN-PRUEBAS.md` | Criterio de adopcion: «adoptar practica cuando mejora al menos 2 metricas clave» | H1, H2a y H2b son las primeras metricas de esa clase medidas sobre implementaciones ajenas y no sobre el testigo |
| `../../agenda/BACKLOG-INVESTIGACION.md` #6 | Que toda metrica cuyo tratamiento altere la observabilidad del resultado es inutilizable, y que faltan fuentes independientes del artefacto | Un e2e que pasa o falla es independiente del artefacto documental de cualquier brazo. Si el diseño se sostiene, es el primer caso del corpus que escapa al anti-patron |

SHOULD — cada documento listado declara la espera en su propio `Deuda arrastrada`, nombrando `B-09`.

## Definicion operacional

- **Denominador.** Fijo y comun a todos los brazos: la cantidad de e2e de la suite sellada. En R1, los e2e de R1; en R2, los de R1 mas los del requisito nuevo. **No varia entre brazos** y no se recalcula por lo que cada brazo haya producido — un denominador que dependiera del entregable beneficiaria al brazo que produjo menos.
  - **Un proyecto que no arranca puntua `0`, no `N/A`.** Fallar todos los e2e es el resultado correcto de un sistema que no corre, y `0` es el valor verdadero.
  - **VOID es otra cosa y se excluye del denominador de `P`.** Una corrida es VOID si falla el **instrumento**: el harness aborto sin producir ningun intento de codigo —halt-on-permission, error de entorno, corte del proveedor—. VOID no es un `0`: es una corrida que no ocurrio. Se cuenta en `S4` y se re-corre. La regla de VOID MUST escribirse en el runbook **antes** del primer rep, y la decision de VOID es la unica intervencion humana del circuito de puntuacion.
    - **Se adjudica a ciegas del puntaje.** La decisión se toma **desde el transcript, antes de correr la suite** sobre ese workspace, y el orden se registra por rep. Es la única forma de que «falló el instrumento» no se vuelva la puerta por la que se rescata un rep flojo de un brazo favorito: una vez visto el puntaje, la clasificación deja de ser independiente del resultado.
    - **Las re-corridas tienen tope.** Valor propuesto, a sellar: **2** por celda. Agotado el tope, la celda se reporta como **VOID persistente**, entra a `S4` y no se re-corre más. Sin tope, «re-correr hasta que salga» es un grado de libertad sin fondo y `S4` deja de ser interpretable como métrica.
  - **Agotar el tope duro NO es VOID: es entrega fallida y puntua.** Si el brazo consumio su limite de turnos, tokens o reloj sin alcanzar su condicion de termino, se puntua el artefacto que haya quedado. Falla el **brazo**, no el instrumento, y eso es precisamente lo que el experimento existe para observar. Confundir las dos cosas borraria del dato el modo de falla mas plausible de la ceremonia cara.
  - **Un brazo INEJECUTABLE no puntua.** Si un brazo admitido en Fase 0.A resulta no invocable durante las tandas, sus celdas se anulan —no valen `0`— y su exclusion se declara en el veredicto con el punto exacto de la falla. Ver §Que pasa si la imposibilidad aparece igual.
- **Aislamiento de la medicion.** La suite corre **fuera** del workspace del rep, contra el artefacto entregado, en el contenedor sellado (§Sello), sin acceso a la red ni a este repositorio. Ningun brazo tiene acceso de lectura a la suite en ningun momento — ni a la implementacion de referencia, que es una solucion completa del enunciado y se protege igual que la suite.
- **Estado de R1 inmutable antes de R2.** R2 corre sobre el workspace que dejó ese mismo rep, así que el estado al cierre de R1 —código entregado y salida cruda de la suite— MUST conservarse inmutable antes de aplicar el requisito de R2. Sin ese congelamiento, `S1` no es auditable: qué e2e aprobaban antes del cambio deja de ser verificable después del cambio. El mecanismo concreto es de runbook.
- **Validacion del instrumento — MUST correrse antes de puntuar nada, y en cada ronda de ajuste.** La suite sellada se corre contra dos controles conocidos: (a) una implementacion de referencia deliberadamente completa, que MUST dar 100%; y (b) un esqueleto vacio que respeta el contrato de invocacion y no hace nada, que MUST dar 0%. Si la suite no discrimina esos dos extremos, no es instrumento y B-09 no corre. Es **prerrequisito de Fase 0.B** —una banda de `C0` fuera de rango no distingue enunciado mal calibrado de suite que no mide— y **condicion de cierre de cada ronda de ajuste**, porque cada ajuste del enunciado cambia la suite y la implementacion de referencia.
- **Granularidad de reporte.** Por **celda** — harness × brazo × ronda —, que es la unidad de la metrica. No se reporta un valor agregado por brazo entre rondas: R1 y R2 miden cosas distintas y promediarlas mezcla unidades no comparables. Tampoco se agrega entre harnesses, por el mismo motivo y con mas fuerza (§Replicacion por harness).
- **Admisibilidad de reconciliaciones.** Ninguna sobre el codigo entregado, nunca. El contrato de invocacion es parte del enunciado sellado, asi que el desajuste que en otros diseños obligaria a reconciliar aca esta eliminado por construccion. MAY reconciliarse un unico caso: que el brazo entregue el ejecutable en una ruta distinta a la declarada **habiendola documentado**; se reporta la variante cruda **y** la reconciliada, con el criterio primario sobre la cruda.
- **Regla de agregacion.** Veredicto **por celda**. H1 se evalua brazo contra `C0` dentro de la misma ronda **y dentro del mismo harness**. MUST NOT agregarse brazos entre si, ni rondas entre si, ni harnesses entre si. Con mas de un harness apto, el veredicto se emite **por harness** y despues se declara si las direcciones **replican** — lectura categorica de dos palabras, replica o no replica, nunca una diferencia de magnitud.
- **Tratamiento del empate.** Empate de medianas entre los dos brazos comparados se declara **NO CONCLUYENTE**, nunca refutacion. El **solapamiento de rangos** no produce por si solo no-veredicto: se declara dentro del enunciado y el veredicto queda sujeto a la sensibilidad *leave-one-out* (§Criterio de exito, «Regla de comparacion»), que es donde vive la regla completa.
- **Independencia entre metricas.** `S1` (regresion) y `P` de R2 **comparten datos**: los e2e de R1 estan en el denominador de `P` en R2. `S1` MUST NOT computarse como evidencia adicional sobre `P` de R2. H2a y H2b se evaluan contra `S1` y H1 contra `P`; ningun veredicto usa las dos para la misma afirmacion.
  - **Acoplamiento residual del subconjunto común, declarado.** El denominador de `S1` se **selecciona** con los resultados de R1 de los dos brazos comparados, así que depende de `P` en R1 — no de `P` en R2, que es la que el párrafo anterior protege. El acoplamiento es de **selección de ítems**, no de valor: qué e2e entran al conteo lo deciden los datos de R1, y cuánto regresiona cada brazo lo deciden los de R2. MUST declararse junto a cualquier lectura de H2a o H2b, y es el precio de igualar el denominador por construcción en vez de por división.
- **Denominador y frontera de `S2`.** No es una proporcion sino un conteo, y su definicion operacional completa —que entra, que no, descomposicion en tres componentes, fuente primaria y cruzada, y esquema de contabilidad versionado— vive en §Protocolo de medicion de costo. MUST resolverse en Fase 0.A.
- **Quien mide.** Nadie. La puntuacion de `P` y `S1` es el codigo de salida de la suite; `S2` y `S3` los reporta el harness bajo el protocolo de §Protocolo de medicion de costo. La unica decision humana es declarar VOID, y su regla se sella antes de correr. Es la primera metrica de este repositorio que no requiere acuerdo entre puntuadores — la deuda que A-04 arrastro dos pasadas.

## Criterio de exito

### Regla de comparacion, comun a las cuatro hipotesis

Toda comparación entre dos brazos —tratamiento contra `C0`, o tratamiento contra tratamiento— se resuelve con la **misma** regla, declarada una sola vez acá y referenciada por cada condición:

> La dirección se lee sobre la **mediana de los 3 reps** de la celda. Sostenerla exige además las tres obligaciones de abajo; si alguna no se cumple, el veredicto es **NO CONCLUYENTE**.

1. **Distribución completa.** MUST reportarse los 3 reps de cada brazo, no sólo la mediana.
2. **Solapamiento declarado dentro del enunciado del veredicto**, no en nota al pie. Redacción obligada cuando los rangos solapan: «tendencia consistente con `Hn`, con rangos solapados».
3. **Sensibilidad *leave-one-out*.** Si al quitar **cualquiera** de los 3 reps la dirección de la mediana se invierte, el veredicto es NO CONCLUYENTE.

**De donde sale, y por que no es no-solapamiento de rangos.** Se hereda de B-07 (`../b07-formato-hibrido/EXPERIMENTO-B7-formato-hibrido.md` §Criterio de exito (b)), que llegó a esta regla **derogando** la anterior: con `n` chico, exigir no-solapamiento de rangos deja el resultado en NO CONCLUYENTE **por construcción y no por el dato**. B-09 corre con `n`=3 por celda —el mismo problema— así que hereda la solución en lugar de repetir el error. La decisión se toma sin ninguna corrida de tratamiento a la vista.

**Ambiguedad que esta regla cierra.** Las dos formulaciones que convivían en este documento no son la misma prueba: `A = {0, 4, 10}` contra `B = {11, 12, 21}` tiene diferencia de medianas 8, **menor** que el rango intra-brazo de 10, y sin embargo los rangos `[0,10]` y `[11,21]` **no solapan**. Queda una sola regla; los demás lugares la referencian y no la reproducen.

**Costo declarado.** Las tres obligaciones **bajan la probabilidad de que este experimento emita dirección**, y eso se acepta a sabiendas: una dirección que sólo sobrevive eligiendo el rep favorable no es un resultado. Es la misma comprobación que B-07 se obligó a hacer al relajar la regla.

### Admisibilidad por hipotesis

Cada hipótesis necesita brazos distintos vivos, así que la población mínima no es un número global:

| hipotesis | brazos que MUST estar vivos | por que |
|---|---|---|
| H1 | `C0` + al menos un tratamiento | se evalúa con los tratamientos que sobrevivan |
| H2a | `C0`, T1, T2 | T1 es **comparador** de la condición, no contexto |
| H2b | `C0`, T1, T3 | idem |
| H3 | los cinco | la condición es «supera a los otros cuatro»: con un brazo caído es incomputable |

- **Tercera categoria de veredicto: NO EVALUABLE POR POBLACION.** Si un brazo requerido no sobrevive a Fase 0.A, o cae INEJECUTABLE durante las tandas, la hipótesis que lo necesita se declara **no evaluable por población**. Es distinto de refutada y distinto de NO CONCLUYENTE, que son veredictos **sobre el dato**; éste es un veredicto sobre la población y MUST NOT leerse como evidencia en ninguna dirección. Cae en la misma categoría la hipótesis cuyo par comparado quede **no computable** por subconjunto común insuficiente (§Metricas, `S1`) en la mayoría de los reps.
- **Piso de poblacion para sellar.** MUST sobrevivir `C0` y **al menos dos tratamientos de autoría ajena**. Si entre los tratamientos sólo sobrevive T3, B-09 **no sella** y reporta hallazgo de factibilidad: la única mitigación declarada del confundido de autoría (§Brazos, «sdd-first entra sin castigo previo») es la comparación contra tratamientos que no escribió quien evalúa, y sin al menos dos de ellos el diseño pierde lo que sostiene su lectura.

### Condiciones

- **Condicion H1.** Sostenida si **al menos un brazo tratamiento** supera a `C0` en `P` **en al menos una ronda**, bajo la §Regla de comparacion.
  - Metricas que la componen: `P`.
  - Satisfacibilidad: si. Existe un resultado posible del diseño que la cumple (p. ej. `C0` con reps 48/50/52 y T1 con 72/75/78: medianas 50 y 75, estable bajo *leave-one-out*) y otro que la niega.
- **Condicion H2a (OpenSpec) y H2b (sdd-first).** Cada una sostenida si, **en R2**, `S1` del brazo es **menor** que `S1` de `C0` **y** que `S1` de T1 —cada par sobre su propio subconjunto común (§Metricas)— bajo la §Regla de comparacion. Se evalúan por separado y ningún veredicto de una condiciona al de la otra.
  - **Conjuncion parcial.** Si el brazo cumple contra uno de los dos comparadores y no contra el otro, la hipótesis **no está sostenida** —la condición es una conjunción— y el veredicto MUST declarar contra cuál comparador se dio la dirección. No es refutación del mecanismo: es una condición que no se cumplió, y la mitad que sí se cumplió se reporta como tal.
  - Metricas que la componen: `S1`.
  - Satisfacibilidad: si. Requiere que la calibracion deje margen de regresion posible — si ningun brazo regresiona, la hipótesis es NO CONCLUYENTE por piso, y eso MUST verificarse en Fase 0.B antes de sellar.
- **Condicion H3.** Sostenida si el `S2` total de T4 supera al de los otros cuatro brazos **en las dos rondas**, bajo la §Regla de comparacion.
  - **Divergencia entre rondas ⇒ NO CONCLUYENTE**, con las dos direcciones declaradas por ronda. «Este método consume más» es una afirmación sobre el método; un brazo que sólo es el más caro en una de las dos rondas no la sostiene.
  - **Celdas censuradas.** H3 MUST NOT sostenerse sobre celdas donde algún brazo alcanzó el tope de tokens: ahí `S2` es cota inferior y no valor (§Protocolo de medicion de costo). Lo afirmable en ese caso es categórico —qué brazos alcanzaron el techo y cuáles no— y se reporta así.
  - Metricas que la componen: `S2`.
  - Satisfacibilidad: si, condicionada a que Fase 0.A valide la contabilidad de costo; si no la valida, H3 se retira del criterio antes del sello (§Protocolo de medicion de costo, punto 3).
- **Regla de cierre.** B-09 cierra con **cuatro veredictos independientes** —H1, H2a, H2b, H3—, nunca fundidos, y la decision declara el peso relativo. H1 pesa mas que las otras tres: es la unica que responde la pregunta que origina el experimento. H2a y H2b pesan igual entre si; que una se sostenga y la otra no es un resultado sobre **mecanismos distintos**, no una contradiccion.
- **Regla de cierre con mas de un harness apto.** Los cuatro veredictos se emiten **por harness** y despues se declara, para cada hipotesis, si la direccion **replica**. Escala de lo afirmable, de menor a mayor: un harness ⇒ «bajo este harness»; dos o mas que replican ⇒ la direccion no se explica solo por el harness ni solo por la familia de modelo; dos o mas que **no** replican ⇒ el resultado es **propiedad del andamiaje y no del metodo**, que es un hallazgo y no un fracaso, y probablemente el mas util que este diseño puede producir para el resto de la agenda.

## Riesgos

1. **Techo del control** — `C0` pasa casi todo y ningun brazo puede mostrar diferencia. Es el modo en que A-04 cerro dos veces. Mitigado por la banda de Fase 0.B, y el enunciado sintetico existe para poder mitigarlo.
2. **Piso** — el enunciado es tan dificil que todos los brazos quedan cerca de 0 y el instrumento tampoco discrimina. La misma banda de Fase 0.B lo cubre por el otro extremo.
3. **Efecto de operador** — un brazo pierde porque lo manejamos mal, no porque su metodo sea peor. Mitigado sellando la ficha de interfaz de cada brazo, con su secuencia de invocacion tomada de la documentacion oficial de esa fuente. **No queda eliminado**: la habilidad para conducir cada herramienta es parte de lo medido y MUST declararse.
3-a. **Los brazos con fase interactiva corren en regimen degradado, y esa reserva pesa sobre H1.** T1 y T4 están diseñados para preguntarle al operador en runtime, y la respuesta enlatada de la ficha (§Fase 0.A) los deja ejercer esa fase sin la información que un usuario real aportaría. La alternativa —que el operador conteste con conocimiento de dominio— sería peor: inyectaría en el tratamiento información que `C0` nunca recibe. Pero la enlatada no es neutral: `/speckit.clarify` existe precisamente para extraer contexto, así que lo medido es Spec Kit con su fase de clarificación degradada. **Si T1 o T4 pierden, esta reserva MUST acompañar al resultado con la misma fuerza que la asimetría de lectura declarada para T3**, y no como nota al pie.
3-bis. **Un brazo no se puede invocar, o su producto no se puede medir.** Es el riesgo que Fase 0.A existe para descubrir **antes** del sello, y la razon por la que esa fase corre primero y sobre un enunciado descartable. Si aparece igual a mitad de tanda, la regla ya esta escrita —brazo INEJECUTABLE, celdas anuladas, bateria sigue, fixture intacto— y su valor es justamente estar escrita de antemano: improvisarla con datos a la vista es el grado de libertad post-hoc mas facil de cometer sin notarlo.
3-ter. **La contabilidad de tokens no es identica entre brazos, o no incluye subagentes.** Si Fase 0.A muestra que `S2` no se lee del mismo modo para todos, **H3 no se puede evaluar** y MUST retirarse del criterio de exito antes del sello, no al ver los datos. El caso mas probable y mas dañino es que el contador no atribuya el consumo de subagentes a la corrida padre, porque subcontaria justo al brazo del que trata H3. No afecta a H1, H2a ni H2b. Detalle en §Protocolo de medicion de costo.
3-quater. **`S2` como numero unico puede medir el harness y no el metodo.** Los brazos ceremoniales releen su propia spec y generan mucha lectura de cache; un total que la pondere a peso completo los castiga por una propiedad del regimen de cache, y uno que la excluya los favorece por lo mismo. Mitigado publicando siempre los tres componentes por separado, de modo que la ponderacion quede a la vista y sea recomputable. **No queda eliminado**: la primaria sigue siendo un total y esa eleccion es discutible.
3-quinquies. **T4 se distribuye como plugin del harness, y eso lo deja sin las dos garantias que los otros canales dan por sentadas.** Su documentacion [R37] prescribe una via de instalacion **distinta por harness**, y ninguna de esas vias documenta un pin de version: actualizar es reinstalar, que es la definicion de un puntero movil. Dos consecuencias, y no son la misma.

- **La que se resuelve sellando.** Sin identificador inmutable, el contenido puede cambiar entre reps sin que nada lo registre. Fase 0.A MUST establecer si alguna via admite un ref fijo; si ninguna lo admite, el **hash del artefacto instalado** (§Sello) pasa de comprobacion a unico anclaje, y esa reduccion se declara.
- **La que no se resuelve sellando, y pesa sobre §Replicacion por harness.** Como el canal difiere por harness, el artefacto de T4 puede diferir entre baterias **por el canal y no por el harness**, que es exactamente la lectura que la replicacion existe para producir: si la direccion de H3 no replica, no se distingue «es el harness», «es la familia de modelo» y «era otra version del brazo». El hash lo vuelve detectable, no lo elimina.

Lo que **no** es un riesgo, contra lo que una version anterior de este documento afirmaba: los harnesses previstos soportan plugins, asi que T4 no queda INEJECUTABLE por falta de soporte y H3 no pierde poblacion por esa via. Se corrigio al verificar la documentacion de instalacion de la fuente.

**Decision tomada, y es una desviacion declarada.** T4 entra **cargado por sesion desde un directorio local**, no instalado por el canal de su autor. Eso resuelve los tres problemas a la vez —no queda estado en el entorno del usuario, el directorio es hasheable, y no depende de un canal sin pin— al precio de dejar de ejercer el metodo tal como su autor lo distribuye. El artefacto es el mismo y lo que cambia es por donde entra, pero **la desviacion MUST acompañar cualquier lectura de un resultado de T4**, con la misma fuerza que la asimetria de lectura declarada para T3 y la reserva de regimen degradado de 3-a. El mecanismo concreto y su evidencia viven en [`ENTORNO-HARNESS-B9.md`](ENTORNO-HARNESS-B9.md).

3-sexies. **El estado que un brazo instala fuera del workspace puede contaminar al brazo siguiente, y el candidato a contaminado que importa es `C0`.** No es riesgo de un brazo sino de una clase: todo metodo que se instala —herramienta global, plugin, skill— sobrevive al workspace que lo pidio, y un plugin con *hook* de arranque se activa sin invocacion explicita. La linea base contaminada no produce un error visible, produce un control que parece rendir de mas, y con eso H1 se evalua contra una referencia falsa. Mitigado por `HOME` temporal por rep mas inventario de entorno verificado antes de cada corrida (§Sello, «Estado que el brazo deja fuera del workspace»). **No queda eliminado por el sello solo**: depende de que la verificacion se corra, que es trabajo del runbook.

3-septies. **La autenticacion del harness puede ser incompatible con el aislamiento, y eso decide si un harness puede alojar una bateria.** Un `HOME` temporal no lleva credenciales; un harness que exige inicio de sesion interactivo no arranca sin ellas, y responder un login por rep convierte 30 corridas en un procedimiento manual irreproducible. Fase 0.A MUST establecer si cada harness admite autenticacion no interactiva antes del sello. Es riesgo de **factibilidad**, no de validez: si no la admite, el problema no es que el dato salga sesgado sino que la bateria no se puede correr ahi de forma sellable — y eso se reporta como hecho sobre el harness.

**Estado del relevamiento, y la decision que dejo.** El primer harness tiene via no interactiva y el segundo no la tiene confirmada: sus propias fuentes oficiales se contradicen y el pedido sigue abierto en su repositorio ([`ENTORNO-HARNESS-B9.md`](ENTORNO-HARNESS-B9.md), donde vive la evidencia). El segundo harness **se mantiene**, autenticado una vez de forma interactiva, corriendo despues contra el almacen de credenciales del sistema — que cumple el criterio de que la credencial sea lo unico que cruza, porque ese almacen no lleva configuracion ni plugins. Lo que no cumple es el sello: esa bateria **depende de un estado de maquina que no se sella**, y esa dependencia MUST declararse junto a cualquier resultado suyo y junto a toda lectura de replicacion que lo incluya. Se descarto la via de clave de API de ese harness por un motivo de diseño y no de comodidad: cambiaria el backend de modelo, es decir **cual es** la familia de modelo de esa bateria, que es una variable del experimento (§Sello, escalon 3) y no un detalle de acceso.

4. **Confundido de harness y familia de modelo** — inseparable **dentro** de cada harness, escalon 3, declarado. Mitigable solo por replicacion de la bateria entera en un segundo harness, que no lo separa pero lo vuelve menos plausible como explicacion unica.
5. **Autoria del fixture** — enunciado y suite los escribe quien evalua, y quien evalua tambien escribio T3. Acotado por sellado previo, invisibilidad de la suite para los brazos y puntuacion sin juicio; **no eliminado**.
6. **`n`=3** — resolucion para dispersion, no para tasas. Declarado.
7. **Costo** — 30 corridas por harness, cada una un proyecto entero. Es el experimento mas caro del repositorio, y la replicacion lo multiplica por la cantidad de harnesses. Orden de recorte, si el presupuesto obliga: primero se recortan **harnesses** —bajando el techo de lo afirmable, que es una perdida declarable—, despues **reps**, declarando la perdida de resolucion. **Nunca** se recorta R2, que es lo que sostiene la equidad entre brazos, ni la completitud de una bateria, que es lo que impide elegir post-hoc que brazo corre en que harness.
8. **Ausencia de los dos casos cerrados** — Kiro y Tessl no corren. Tessl es el unico que regenera desde la spec, y su ausencia significa que B-09 **no dice nada** sobre el paradigma *spec-as-source*. Esa pregunta vive en el item #20 del backlog y MUST NOT leerse contestada por aca.

## Plan de captura de datos

- Repositorio de datos externo `experimentosdd-b9/`, siguiendo el patron de `experimentosdd-a4/` y `experimentosdd-b7/`: este repositorio conserva diseño, runbook y resultado; los workspaces generados, transcripts, hashes de sello y bitacora de tanda viven alla.
- **De Fase 0.A se conservan las fichas de interfaz y el veredicto go/no-go por brazo, y se descarta todo lo demas.** El enunciado descartable, sus workspaces y sus puntajes no se archivan como dato: existieron para probar que el circuito cierra, y conservarlos invita a leerlos despues como si fueran resultados.
- Por rep se conserva: hash del fixture, **identificador inmutable de origen del tratamiento y hash del artefacto instalado** —los dos, por §Sello, y el segundo tomado por rep—, **el inventario de entorno del rep** (§Sello, «Estado que el brazo deja fuera del workspace»), version efectiva de harness y modelo, transcript completo, workspace entregado, salida cruda de la suite, y `S2`/`S3`. Ningun artefacto conservado MUST contener credenciales.
- **De Fase 0.B se conserva la bitacora de calibracion —cada candidato de enunciado, su `P(C0)` en R1 y su `S1(C0)` en R2— y ninguna de esas corridas entra al veredicto** como celda de `C0` (§Fase 0.B, condición 7). La bitácora existe para que la calibración sea auditable, no para aportar línea base.
- El runbook de medicion —`PRUEBA-*.md`— es documento autorado y **MUST tener spec registrada** antes de escribirse (`../../SPECS_REGISTRY.md` §Docs excluidos). Este diseño no la reemplaza. Lo que este diseño le deja resuelto y el runbook MUST recoger, sin volver a decidirlo:
  - la regla de VOID, con su adjudicación ciega del puntaje y su tope de re-corridas (§Definicion operacional);
  - el régimen de permisos, heredado de A-04 y no de B-07 (§Sello, «Regimen de permisos»);
  - el mecanismo concreto de congelamiento del estado de R1 antes de aplicar el requisito de R2;
  - **verificación de determinismo de la suite**: la validación 100%/0% es binaria y de una sola corrida, y no prueba que la suite sea estable; MUST correrse más de una vez antes de sellar, y una suite no determinista no es instrumento;
  - **verificación de aislamiento para las CLIs nuevas**: la fila «entorno de ejecucion» de §Sello hereda el patrón que A-04 pasada 1b verificó para su propio harness, y `specify`, `openspec`, `sdd-first` y `superpowers` no fueron verificadas bajo ese régimen. La herencia está declarada, no verificada, y confirmarla es trabajo de Fase 0.A o del runbook;
  - **el mecanismo de doble sello por canal**: cómo se obtiene el hash del artefacto instalado en cada canal, y qué se hace con un brazo cuyo canal no admita identificador inmutable o difiera entre harnesses (§Sello, «Cada brazo por su canal»; §Riesgos 3-quinquies);
  - **el inventario de entorno por rep y su verificación**: qué se enumera, cómo se compara contra el brazo en curso y qué se hace ante una divergencia — el sello lo exige, pero es la corrida del runbook la que lo convierte en verificación efectiva (§Sello, «Estado que el brazo deja fuera del workspace»);
  - **el manejo de credenciales**: la vía no interactiva que Fase 0.A haya establecido por harness, y el mecanismo por el que la credencial no llega a ningún artefacto conservado.

## Referencias

- [R10] GitHub Spec Kit — brazo T1.
- [R37] obra/superpowers — brazo T4.
- [R38] Fission-AI/OpenSpec — brazo T2.
- [R39] mberliner/sdd-first — brazo T3. **Mismo autor que este repositorio.**
- [R44] Kiro — excluido de la poblacion por imposibilidad de sello.
- [R46] Tessl — excluido de la poblacion por indisponibilidad.
- [R47] Hilos publicos de practica — origen de la objecion de consumo que H3 convierte en medicion.

## Registro de cambios del documento

### 2026-09-09 (segunda) — relevado el entorno, dos decisiones que el diseño debia registrar

El pendiente de autenticacion y aislamiento que dejo la entrada anterior se releva contra la ayuda de los binarios y la documentacion oficial de los dos harnesses. La evidencia, con su procedencia marcada, vive en [`ENTORNO-HARNESS-B9.md`](ENTORNO-HARNESS-B9.md) —documento nuevo, con spec registrada—; aca quedan solo las dos decisiones, que son de diseño porque tocan que se mide.

- **T4 entra cargado por sesion desde un directorio local**, no por el canal de distribucion de su autor. Cierra los tres problemas de 3-quinquies de una vez —sin estado residual, hasheable, sin depender de un canal sin pin— y a cambio deja de ejercer el metodo tal como se distribuye. Desviacion declarada, con el mismo peso de lectura que las reservas de T3 y de 3-a.
- **El segundo harness se mantiene con autenticacion interactiva previa.** No tiene via no interactiva confirmada —sus fuentes oficiales se contradicen— y correr contra el almacen de credenciales del sistema cumple el criterio de la credencial como unica cosa que cruza, pero deja esa bateria dependiendo de un estado de maquina no sellado. Se declara. Se descarto su via de clave de API porque cambiaria la familia de modelo de esa bateria, que es variable del experimento y no detalle de acceso.

Queda registrado ademas un hallazgo que no cambia una regla pero si el regimen de corrida: el modo minimo del primer harness, que a primera vista era el aislamiento ideal, **desactiva el mecanismo por el que T4 se activa**, y aplicarlo solo a algunos brazos romperia la igualdad de condiciones que hace comparables las celdas. Se corre sin ese modo, igual para los cinco brazos.

### 2026-09-09 — el sello nombraba una unidad de tratamiento que no existe, y el aislamiento no cubria lo que los brazos instalan

Al planificar Fase 0.A se inspeccionaron los cuatro tratamientos para escribir su secuencia de invocacion. El relevamiento invalido una premisa del §Sello y, al seguir el hilo de como se instala cada brazo, dejo a la vista un segundo hueco que el diseño no cubria: que hace el aislamiento con el estado que un brazo deja **fuera** del workspace.

**Primer hueco — la unidad de tratamiento.** El documento sellaba «el commit del clon vendored en `fuentes-externas/<herramienta>/`» para los cuatro. Dos hechos lo desmienten:

- **En `fuentes-externas/` no hay clones.** Hay cuatro enlaces del sistema de archivos a arboles de trabajo ubicados fuera de este repositorio. Un enlace asi no lo resuelve ningun otro clon —lo que anularia §Replicacion por harness— y el arbol apuntado puede moverse entre reps sin registro. El caso mas expuesto es T3, que apunta al arbol de trabajo vivo de quien evalua, que es justamente el brazo con el confundido de autoria declarado.
- **Los brazos no comparten unidad de distribucion.** Cada fuente publica su metodo por el canal que su autor eligio —repositorio, paquete en un registro de lenguaje, plugin del harness— y ninguno de esos canales es «el clon». Sellar el repositorio para los cuatro, por ser la unidad mas prolija de hashear, mediria en varios de ellos una variante que ningun adoptante ejerce, contra la definicion de tratamiento del propio diseño.

**Segundo hueco — el alcance del aislamiento.** La fila «entorno de ejecucion» sellaba workspace limpio y `HOME` temporal, heredados de A-04, donde el tratamiento era una instruccion y no un programa a instalar. Aca tres de los cuatro brazos **se instalan**, y una herramienta global o un plugin aterrizan en el entorno del usuario, no en el proyecto: sobreviven al rep que los instalo. El mecanismo sellado ya los cubre —viven bajo `HOME`— pero el diseño no lo declaraba ni exigia verificarlo, y el caso peor no es un tratamiento contaminando a otro sino cualquiera contaminando a `C0`, porque un plugin con *hook* de arranque se activa sin invocacion explicita y una linea base contaminada no produce un error visible. Detras de eso aparecio ademas la tension con la autenticacion, que es la unica cosa que legitimamente necesita cruzar el `HOME` temporal.

**Ninguna corrida de tratamiento existia al corregirlo** (Principio V): el documento sigue en BORRADOR PRE-SELLO y Fase 0.A no empezo. La correccion se escribe como regla y no como inventario: **que canal usa cada brazo, y con que valores, es producto de Fase 0.A y se registra por tanda**; lo que el diseño fija es el piso que todo canal debe cumplir.

| que cambio | donde |
|---|---|
| las cuatro filas de tratamiento colapsan en una regla: **dos** identificadores por brazo —el inmutable que admita su canal, y el hash del artefacto ya instalado—, con los valores concretos diferidos a Fase 0.A | §Sello (tabla y «Cada brazo por su canal») |
| el canal de instalacion se declara parte de la secuencia de invocacion, no un preliminar de operacion | §Fase 0.A (ficha de interfaz) |
| contenedor de evaluacion y entorno de ejecucion se distinguen explicitamente: exigencias opuestas, mecanismos distintos, y un brazo que vive como plugin del harness no puede encapsularse sin salir de su canal | §Sello («Dos entornos») |
| dos casos que la regla general MUST cubrir: canal sin identificador inmutable —el hash pasa a unico anclaje, declarado— y canal que **difiere entre harnesses**, donde el artefacto puede variar por el canal y no por el harness, que es justo lo que la replicacion existe para leer | §Sello («Cada brazo por su canal») y §Riesgos 3-quinquies |
| por rep se conservan los dos identificadores, no solo el commit; el runbook recoge el mecanismo de doble sello y su aplicacion al brazo distribuido como plugin | §Plan de captura |
| el aislamiento se extiende al estado que los brazos **instalan** fuera del workspace, con inventario de entorno verificado por rep, hash del artefacto tomado por rep, y la prohibicion de resolverlo por orden de corrida | §Sello («Estado que el brazo deja fuera del workspace»), §Riesgos 3-sexies, §Plan de captura |
| la autenticacion no interactiva del harness pasa a bloqueante de Fase 0.A: es lo unico que legitimamente cruza el `HOME` temporal, y un harness que no la admita no puede alojar una bateria de forma sellable | §Sello (mismo bloque) y §Riesgos 3-septies |

**Una correccion de mas y una reserva que sigue viva.** Una version intermedia de esta entrada afirmaba que el brazo distribuido como plugin podia quedar INEJECUTABLE por falta de soporte del harness; verificada la documentacion de la fuente, los harnesses previstos lo soportan y esa afirmacion se retiro. Lo que no se retira: que un brazo documente un modo de arranque no interactivo MUST NOT leerse como que cancela la reserva de §Riesgos 3-a, que es sobre su fase de clarificacion y no sobre su arranque.

### 2026-09-07 — revision pre-sello, dos pasadas de correccion

Tres pasadas de revisión sobre el borrador del 2026-09-06 produjeron 18 observaciones, que se resolvieron en dos correcciones a este documento: la primera sobre §Hipotesis, §Metricas y §Criterio de exito —qué se afirma y cómo se decide—, la segunda sobre §Fase 0.A, §Fase 0.B, §Sello, §Definicion operacional, §Riesgos y §Plan de captura —cómo se produce el dato—. **Ninguna corrida de tratamiento existía al decidirlas** (Principio V): el documento seguía y sigue en BORRADOR PRE-SELLO. Los identificadores `P*` son los de la revisión y se conservan para que las decisiones sean rastreables; el documento de trabajo que los originó se eliminó al integrarse.

**Aceptado e incorporado.**

| id | qué corregía | dónde quedó |
|---|---|---|
| P1.1 | `S1` como conteo crudo premiaba al brazo con peor R1, por techo de regresión bajo | §Metricas (subconjunto común) y §Definicion operacional (acoplamiento residual) |
| P1.2 | H2 fundía dos mecanismos en una hipótesis, sin veredicto definido si sólo uno se sostenía | §Hipotesis (H2a/H2b) y §Criterio de exito (conjunción parcial, regla de cierre) |
| P1.3 | «batería completa» e «INEJECUTABLE no descalifica» se contradecían, también en la tabla de Sello | §Que pasa si la imposibilidad, §Replicacion por harness y fila del §Sello |
| P1.4 | 0.B no producía el dato de regresión que H2 exige verificar antes de sellar | §Fase 0.B, condiciones 5, 6 y 7 |
| P1.5 | el tope duro era por brazo, y `S2` se cuenta hasta el tope: H3 se decidía por un parámetro del operador | §Protocolo de medicion de costo, §Fase 0.A (ficha) y §Criterio de exito (censura) |
| P1.6 | VOID, única decisión humana, sin ciego y con re-corridas sin tope | §Definicion operacional (VOID) |
| P1.7 | la regla de comparación era ambigua y reinstalaba el no-solapamiento que B-07 derogó con `n` chico | §Criterio de exito, «Regla de comparacion» |
| P1.8 | la población mínima tras 0.A no estaba fijada, y un número global no sirve | §Criterio de exito, «Admisibilidad por hipotesis» |
| P1.9 | runtime, implementación de referencia y contenedor de evaluación sin sellar | §Contrato de invocacion, §Sello (dos filas nuevas), §Definicion operacional |
| P2.1 | T1 y T4 preguntan en runtime; contestarles inyecta información que `C0` no recibe | §Fase 0.A (séptimo campo de la ficha) y §Riesgos 3-a |
| P2.2 | el veredicto de 0.A exigía puntuar un ensayo para el que no existía instrumento | §Fase 0.A (smoke-test auxiliar) |
| P2.3 | la validación del instrumento no estaba ubicada en la secuencia, y es un bucle | §Fase 0.B y §Definicion operacional |
| P2.4 | H2 y H3 no declaraban sobre qué rondas se evalúan | §Hipotesis y §Criterio de exito |
| P2.8 | el orden 0.A → 0.B no estaba declarado, y no son independientes | §Fase 0.A (invariante de la analogía) |
| P3.1 | el go/no-go de 0.A no decía si se basa en una corrida o varias | §Fase 0.A (dos corridas, regla asimétrica) |
| P3.3, P3.5 | determinismo de la suite y aislamiento de las CLIs nuevas, sin verificar | §Plan de captura, como requisitos que MUST recoger el runbook |
| P3.4 | el estado de R1 podía no conservarse antes de aplicar R2 | §Definicion operacional |

**Rechazado, con motivo.** Cuatro observaciones no se incorporaron:

1. *«Contradicción entre veredicto por celda y el cierre de H1»*: no la hay. «En al menos una ronda» es un OR lógico entre comparaciones de celda; lo que §Definicion operacional prohíbe es promediar o sumar celdas en un número compuesto, no razonar sobre más de una.
2. *«Falta de fases canónicas 0-4 del repositorio»*: afirmación hecha sin citar texto de `../a04-conducta-agente/PRUEBA-PISO-RUIDO-A4.md` ni de `../b07-formato-hibrido/EXPERIMENTO-B7-formato-hibrido.md`. No se verificó que esa convención exista; si existe, se incorpora citándola.
3. *«Acoplamiento R1→R2 sin resolver»*: matizado. `P` en R2 se define sobre todos los e2e, así que recuperar en R2 un test roto en R1 sí se refleja. Lo asimétrico es `S1`, que sólo cuenta pasa→falla, y eso es P1.1 y no un hallazgo aparte.
4. *«Ambigüedad de la unidad temporal de `S2`»*: no la hay. «Corrida» está definida en §Diseno (30 corridas = 5 × 2 × 3) y acotada en §Protocolo de medicion de costo. Lo que sobrevivió del punto es el cuantificador sobre rondas, que es P2.4.

**Deuda que esta revision deja abierta.** La regla de comparación con `n` chico (P1.7) no es propia de B-09: B-07 ya la decidió y todo experimento futuro con `n` de este orden va a volver a decidirla. Queda registrada como candidata a mejora de método en `../../agenda/MEJORAS-METODO.md`, **sujeta a la experiencia de correr B-09**: se propone como regla general del repositorio recién si sobrevive a un uso real, no antes.
