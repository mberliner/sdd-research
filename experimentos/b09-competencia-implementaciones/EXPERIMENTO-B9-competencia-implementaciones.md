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

Tres, independientes, cada una evaluada por separado. Ninguna se funde con otra en el veredicto.

- **H1 (primaria).** Al menos un brazo con metodo SDD alcanza una proporcion de e2e sellados aprobados **mayor** que el brazo control sin metodo, en al menos una de las dos rondas.
- **H2.** En la ronda de evolucion (R2), los brazos cuyo mecanismo es **estado o enforcement** —OpenSpec (contabilidad de capacidades) y sdd-first (gate fail-closed)— producen **menos regresion** sobre los e2e de R1 que el control y que Spec Kit (ceremonia orquestada).
- **H3.** Superpowers consume **mas tokens por corrida** que cualquier otro brazo, con independencia de su resultado en H1.

H3 no es una hipotesis sobre SDD: es la unica objecion de terceros del corpus que se puede convertir en medicion barata en este mismo diseño (`ORIENTACION-PRACTICA-IMPLEMENTACIONES-SDD.md` §4 quinquies, [R47]). Entra porque el dato se produce igual, no porque el experimento exista para eso.

**Lo que ninguna de las tres afirma.** Ninguna dice cual metodo es mejor. H1 pregunta si el metodo compra algo contra no tener metodo; H2 pregunta si dos mecanismos distintos se comportan distinto en la ronda donde su mecanismo aplica. Un resultado nulo en H1 —ningun brazo supera al control— es un resultado, y probablemente el mas importante que este diseño puede producir.

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

### Fase 0.A — caracterizacion de interfaces y ensayo general

**Corre primero, antes que cualquier otra cosa.** Todo el resto del diseño asume dos cosas que hoy estan sin verificar: que cada brazo **se puede invocar** bajo condiciones sellables, y que su producto **se puede medir** con el mismo instrumento que los demas. Si alguna de las dos falla, falla a mitad de tanda, que es el peor momento — es la misma sorpresa que bloqueo la Fase 0 de A-04, donde la sonda de contexto resulto no ser portable (`../../../experimentosdd-a4/entorno/ENTORNO-1B.md`).

**Producto de la fase: una ficha de interfaz por brazo**, con seis campos y ninguno inferido:

| campo | que responde | por que es bloqueante |
|---|---|---|
| **Entrada** | Que recibe el brazo y en que forma: texto suelto, archivo, comando de scaffolding previo, estructura de directorios esperada | Si dos brazos no pueden recibir el mismo enunciado, la neutralidad se rompe en el primer paso |
| **Secuencia de invocacion** | Los comandos o pedidos exactos, en orden, tomados de la documentacion oficial de esa herramienta | Es la **definicion del tratamiento**, no una mitigacion: lo que se compara es cada metodo ejercido como su propio autor lo indica |
| **Condicion de termino** | Como declara el brazo que termino — tareas completas, cambio listo para archivar, coverage mapping satisfecho, workflow cerrado, o el agente diciendo que termino | Sin esto, cada brazo se detiene en un punto arbitrario elegido por el operador |
| **Tope duro** | Limite de turnos, tokens y reloj tras el cual la corrida se corta | Un brazo que no termina nunca no puede bloquear la tanda |
| **Artefacto entregado** | Que queda en el workspace y como se lanza | Es el otro extremo del contrato: sin esto la suite no tiene contra que correr |
| **Contabilidad de costo** | Si el consumo es legible de forma **identica** para todos los brazos, si **incluye subagentes**, y si expone entrada fresca, lectura de cache y salida por separado | Si no, `S2` no es comparable y **H3 no se puede evaluar**; MUST decidirse aca y no al mirar los datos. Protocolo completo en §Protocolo de medicion de costo |

**El contrato universal tiene dos extremos y hasta ahora este diseño solo escribio uno.** El de salida —el contrato de invocacion del sistema generado— ya estaba. El de entrada no: lo unico neutral entre brazos es el **enunciado**, y todo lo que viene despues es especifico de cada herramienta. Eso no es un defecto que haya que emparejar. Emparejarlo seria peor: obligar a Spec Kit a arrancar como arranca OpenSpec es medir una version mutilada de los dos. Lo neutral es el **enunciado y el criterio de terminacion**; lo especifico es la secuencia, y va sellada tal como la escribe la documentacion de cada fuente.

**El ensayo general corre sobre un enunciado descartable, NUNCA sobre el real.** Un ensayo sobre el enunciado sellado lo expondria a los brazos y quemaria el sello: dejaria de ser una primera corrida. El ensayo usa un enunciado **estructuralmente analogo y de contenido distinto** —mismo tipo de contrato de invocacion, tamaño comparable— y sus resultados **MUST NOT usarse como dato** de ninguna metrica. Se descarta entero al terminar; lo unico que sobrevive son las seis fichas y el veredicto de factibilidad.

**Veredicto por brazo, y es go/no-go.** Un brazo entra a la poblacion definitiva solo si sus seis campos estan completos y el ensayo produjo un artefacto que la suite pudo puntuar. La ficha de interfaz de cada brazo admitido se sella junto con el fixture.

### Que pasa si la imposibilidad aparece igual, a mitad de camino

La regla se escribe ahora, antes de que el caso exista, porque improvisarla despues es exactamente por donde entran los grados de libertad post-hoc.

- **Si aparece en Fase 0.A** (antes del sello): el brazo **queda fuera de la poblacion**, con el motivo escrito. Y eso no es una perdida silenciosa: «no se pudo invocar de forma sellable» es un **hecho sobre la herramienta** y se reporta como tal, de la misma clase que el que ya deja a Kiro afuera. Un metodo que no se puede ejercer de forma reproducible es informacion para quien evalua adoptarlo.
- **Si aparece despues del sello, con tandas en curso**: el brazo se declara **INEJECUTABLE**, sus celdas se anulan, y la bateria **continua con los demas**. Se reporta con el punto exacto donde fallo.
  - MUST NOT dispararse un rediseño del fixture. El enunciado no se toca: a esa altura ya hay datos de tratamiento vistos.
  - MUST NOT ajustarse la secuencia de invocacion del brazo para que funcione. Cambiar el tratamiento despues de ver como le fue es reemplazar el experimento por otro. Si la secuencia corregida vale la pena, es una **pasada distinta**, con enmienda fechada y su propio sello.
  - Un brazo INEJECUTABLE **no descalifica** la bateria de su harness: los demas brazos siguen comparandose contra el control, con la poblacion reducida declarada en el veredicto.
- **Si el problema es de medicion y no de invocacion** —el brazo produjo algo pero la suite no lo puede puntuar—: no hay adaptador. El contrato de invocacion es parte del enunciado sellado, asi que incumplirlo puntua lo que puntue la suite, normalmente `0`. Es resultado, no incidente.
- **Si el brazo agota el tope duro sin declararse terminado**: es **entrega fallida**, no VOID. Se puntua el artefacto que haya quedado. La distincion importa y va sellada: VOID es cuando falla el **instrumento** —el harness aborto, se corto por permisos, error de entorno—; agotar el tope es cuando falla el **brazo**, y eso es exactamente lo que el experimento existe para observar.

### Fase 0.B — calibracion de dificultad, y la frontera con el Principio V

Con enunciado propio la dificultad es una variable de diseño. Eso resuelve el techo **y** abre la puerta a fabricar el resultado. Las dos cosas son el mismo mecanismo, separadas unicamente por estas cuatro condiciones, que MUST cumplirse todas:

1. La **banda objetivo del control** se declara antes de la primera corrida de calibracion. Valor propuesto, a sellar: `C0` en R1 pasa entre **40% y 80%** de los e2e de R1.
2. La calibracion ve **exclusivamente** datos del brazo `C0`. Ningun brazo tratamiento corre hasta que enunciado, suite y requisito de R2 estan sellados y hasheados.
3. El **tope de rondas de ajuste** se declara antes y se cumple. Valor propuesto, a sellar: **3**. Si a la tercera el control no cae en banda, B-09 cierra sin correr tratamientos y reporta el hallazgo de calibracion.
4. Sellado el fixture, los tratamientos corren una vez. No hay edicion del sello despues del primer rep de tratamiento.

**La banda se verifica en cada harness; el fixture se calibra en uno solo.** La calibracion —ajustar el enunciado hasta que el control caiga en banda— ocurre **una vez**, en el primer harness, y termina con el sello. Todo harness posterior corre su propio `C0` y se comprueba contra la **misma** banda ya declarada: si cae adentro, su bateria es APTA; si cae afuera, el **harness** es NO APTO, se declara y sus datos no entran al veredicto. Lo que nunca se hace es mover el fixture para acomodar a un harness — a esa altura ya hay datos de tratamiento vistos, y ajustar seria la busqueda que el Principio V prohibe.

**Por que esto no es lo que A-04 prohibio.** El `MUST NOT` de A-04 veda subir la presion del escenario despues de ver una tasa, buscando una configuracion donde el tratamiento pueda mostrarse — eso es busqueda. Aca el ajuste ocurre **antes de que exista un solo dato de tratamiento**, contra un unico brazo, con banda y tope declarados por adelantado. Es calibracion de dificultad de item contra un control ciego. La frontera es fina y la señal de que se cruzo es una sola: estar ajustando el enunciado despues de ver como le fue a algun brazo que no sea `C0`.

### Replicacion por harness

El harness **MAY ser mas de uno**, y esa es la unica via disponible para atacar el confundido mas grave del diseño. Pero entra bajo una condicion que no admite excepcion:

> **Un harness que corre, corre la bateria completa.** Los cinco brazos, las dos rondas y los tres reps. Un harness parcial no aporta dato y su corrida se descarta entera.

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
| tratamiento — T1 Spec Kit | commit del clon vendored en `../../fuentes-externas/spec-kit/` | 1 + 2 | se extrae del commit sellado a una ruta privada por tanda, no se copia del arbol de trabajo | detiene el rep y explicita commit esperado vs. obtenido |
| tratamiento — T2 OpenSpec | commit del clon en `../../fuentes-externas/OpenSpec/` | 1 + 2 | idem T1 | idem |
| tratamiento — T3 sdd-first | commit del clon en `../../fuentes-externas/sdd-first/` | 1 + 2 | idem T1 | idem |
| tratamiento — T4 Superpowers | commit del clon en `../../fuentes-externas/superpowers/` | 1 + 2 | idem T1 | idem |
| ficha de interfaz por brazo | los seis campos de Fase 0.A, hasheados: entrada, secuencia de invocacion, condicion de termino, tope duro, artefacto entregado, contabilidad de costo | 1 + 2 | se fija en Fase 0.A sobre un enunciado descartable y se sella junto al fixture; la secuencia sale de la documentacion oficial de cada fuente, no de nuestra invencion | detiene si el hash no coincide, y explicita que campo cambio |
| fixture — enunciado, suite e2e, requisito R2 | hash de los tres archivos | 1 + 2 | archivos de solo lectura fuera del workspace del rep; el workspace recibe **solo** el enunciado | detiene si algun hash cambia entre reps |
| entorno de ejecucion | workspace limpio por rep, `env -i`, `HOME` temporal, sin fuentes de ajustes heredadas | 1 + 2 | patron heredado de A-04 pasada 1b, que verifico que ninguna instruccion de proyecto, usuario ni memoria llega al rep | detiene y registra la fuga detectada |
| harness y modelo | version efectiva **al abrir cada tanda**, no al escribir este diseño | 3 | se registra por tanda; una diferencia entre tandas es legitima y se declara junto al resultado | ninguno — declarado sin verificador |
| completitud de bateria por harness | 5 brazos × 2 rondas × 3 reps | 2 | el runbook verifica que la bateria de un harness este entera antes de admitir sus datos al veredicto | descarta la bateria completa de ese harness, no las celdas faltantes |

**Escalon 3, declarado sin verificador.** Dentro de un harness, este y su familia de modelo son **inseparables**: A-04 pasadas 1 y 1b lo establecieron (`../a04-conducta-agente/RESULTADO-EXPERIMENTO-A4.md`, item #10 del backlog). Con un solo harness, todo resultado de B-09 es «metodo X **bajo este harness**», nunca «metodo X», y MUST escribirse asi en el resultado y no en una nota al pie. La unica mitigacion disponible es la replicacion de la bateria entera en un segundo harness (§Replicacion por harness), que no separa los dos ejes pero los vuelve menos plausibles como explicacion unica.

**Regimen de permisos.** A diferencia de B-07, aca los brazos **necesitan** terminal: los CLI de T1 y T2 son el metodo. El regimen se hereda de A-04 —lista de permitidos con degradacion graceful, que sostuvo 0 VOID en dos harnesses— y no de B-07, cuyo `halt-on-permission` produjo corridas nulas estocasticas (item #5 del backlog). MUST definirse en el runbook, no aca.

## Metricas

- **Primaria — `P`**: proporcion de e2e de la suite sellada que aprueban, por brazo y por ronda.
- **Secundarias**:
  - **`S1` regresion**: cantidad de e2e de R1 que aprobaban en R1 y fallan en R2, dentro del **mismo rep**.
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
| `../../software/PLAN-PRUEBAS.md` | Criterio de adopcion: «adoptar practica cuando mejora al menos 2 metricas clave» | H1 y H2 son las primeras metricas de esa clase medidas sobre implementaciones ajenas y no sobre el testigo |
| `../../agenda/BACKLOG-INVESTIGACION.md` #6 | Que toda metrica cuyo tratamiento altere la observabilidad del resultado es inutilizable, y que faltan fuentes independientes del artefacto | Un e2e que pasa o falla es independiente del artefacto documental de cualquier brazo. Si el diseño se sostiene, es el primer caso del corpus que escapa al anti-patron |

SHOULD — cada documento listado declara la espera en su propio `Deuda arrastrada`, nombrando `B-09`.

## Definicion operacional

- **Denominador.** Fijo y comun a todos los brazos: la cantidad de e2e de la suite sellada. En R1, los e2e de R1; en R2, los de R1 mas los del requisito nuevo. **No varia entre brazos** y no se recalcula por lo que cada brazo haya producido — un denominador que dependiera del entregable beneficiaria al brazo que produjo menos.
  - **Un proyecto que no arranca puntua `0`, no `N/A`.** Fallar todos los e2e es el resultado correcto de un sistema que no corre, y `0` es el valor verdadero.
  - **VOID es otra cosa y se excluye del denominador de `P`.** Una corrida es VOID si falla el **instrumento**: el harness aborto sin producir ningun intento de codigo —halt-on-permission, error de entorno, corte del proveedor—. VOID no es un `0`: es una corrida que no ocurrio. Se cuenta en `S4` y se re-corre. La regla de VOID MUST escribirse en el runbook **antes** del primer rep, y la decision de VOID es la unica intervencion humana del circuito de puntuacion.
  - **Agotar el tope duro NO es VOID: es entrega fallida y puntua.** Si el brazo consumio su limite de turnos, tokens o reloj sin alcanzar su condicion de termino, se puntua el artefacto que haya quedado. Falla el **brazo**, no el instrumento, y eso es precisamente lo que el experimento existe para observar. Confundir las dos cosas borraria del dato el modo de falla mas plausible de la ceremonia cara.
  - **Un brazo INEJECUTABLE no puntua.** Si un brazo admitido en Fase 0.A resulta no invocable durante las tandas, sus celdas se anulan —no valen `0`— y su exclusion se declara en el veredicto con el punto exacto de la falla. Ver §Que pasa si la imposibilidad aparece igual.
- **Aislamiento de la medicion.** La suite corre **fuera** del workspace del rep, contra el artefacto entregado, en un contenedor o proceso sin acceso a la red ni a este repositorio. Ningun brazo tiene acceso de lectura a la suite en ningun momento.
- **Validacion del instrumento — MUST correrse antes de puntuar nada.** La suite sellada se corre contra dos controles conocidos: (a) una implementacion de referencia deliberadamente completa, que MUST dar 100%; y (b) un esqueleto vacio que respeta el contrato de invocacion y no hace nada, que MUST dar 0%. Si la suite no discrimina esos dos extremos, no es instrumento y B-09 no corre.
- **Granularidad de reporte.** Por **celda** — harness × brazo × ronda —, que es la unidad de la metrica. No se reporta un valor agregado por brazo entre rondas: R1 y R2 miden cosas distintas y promediarlas mezcla unidades no comparables. Tampoco se agrega entre harnesses, por el mismo motivo y con mas fuerza (§Replicacion por harness).
- **Admisibilidad de reconciliaciones.** Ninguna sobre el codigo entregado, nunca. El contrato de invocacion es parte del enunciado sellado, asi que el desajuste que en otros diseños obligaria a reconciliar aca esta eliminado por construccion. MAY reconciliarse un unico caso: que el brazo entregue el ejecutable en una ruta distinta a la declarada **habiendola documentado**; se reporta la variante cruda **y** la reconciliada, con el criterio primario sobre la cruda.
- **Regla de agregacion.** Veredicto **por celda**. H1 se evalua brazo contra `C0` dentro de la misma ronda **y dentro del mismo harness**. MUST NOT agregarse brazos entre si, ni rondas entre si, ni harnesses entre si. Con mas de un harness apto, el veredicto se emite **por harness** y despues se declara si las direcciones **replican** — lectura categorica de dos palabras, replica o no replica, nunca una diferencia de magnitud.
- **Tratamiento del empate.** Empate, o solapamiento entre el rango de los 3 reps de los dos brazos comparados, se declara **NO CONCLUYENTE**. Nunca refutacion.
- **Independencia entre metricas.** `S1` (regresion) y `P` de R2 **comparten datos**: los e2e de R1 estan en el denominador de `P` en R2. `S1` MUST NOT computarse como evidencia adicional sobre `P` de R2. H2 se evalua contra `S1` y H1 contra `P`; ningun veredicto usa las dos para la misma afirmacion.
- **Denominador y frontera de `S2`.** No es una proporcion sino un conteo, y su definicion operacional completa —que entra, que no, descomposicion en tres componentes, fuente primaria y cruzada, y esquema de contabilidad versionado— vive en §Protocolo de medicion de costo. MUST resolverse en Fase 0.A.
- **Quien mide.** Nadie. La puntuacion de `P` y `S1` es el codigo de salida de la suite; `S2` y `S3` los reporta el harness bajo el protocolo de §Protocolo de medicion de costo. La unica decision humana es declarar VOID, y su regla se sella antes de correr. Es la primera metrica de este repositorio que no requiere acuerdo entre puntuadores — la deuda que A-04 arrastro dos pasadas.

## Criterio de exito

- **Condicion H1.** Sostenida si **al menos un brazo tratamiento** supera a `C0` en `P`, en al menos una ronda, y la diferencia entre las medianas de los 3 reps es **mayor que el rango intra-brazo** de los dos brazos comparados. Solapamiento ⇒ NO CONCLUYENTE.
  - Metricas que la componen: `P`.
  - Satisfacibilidad: si. Existe un resultado posible del diseño que la cumple (p. ej. `C0` en 50% con rango 5 puntos, T1 en 75% con rango 5 puntos) y otro que la niega.
- **Condicion H2.** Sostenida si `S1` de T2 y de T3 es **menor** que `S1` de `C0` **y** que `S1` de T1, bajo la misma regla de solapamiento.
  - Metricas que la componen: `S1`.
  - Satisfacibilidad: si. Requiere que la calibracion deje margen de regresion posible — si ningun brazo regresiona, H2 es NO CONCLUYENTE por piso, y eso MUST verificarse en Fase 0.B antes de sellar.
- **Condicion H3.** Sostenida si `S2` de T4 supera a `S2` de los otros cuatro brazos, bajo la misma regla de solapamiento.
  - Metricas que la componen: `S2`.
  - Satisfacibilidad: si.
- **Regla de cierre.** B-09 cierra con **tres veredictos independientes**, nunca fundidos, y la decision declara el peso relativo. H1 pesa mas que H2 y H3: es la unica que responde la pregunta que origina el experimento.
- **Regla de cierre con mas de un harness apto.** Los tres veredictos se emiten **por harness** y despues se declara, para cada hipotesis, si la direccion **replica**. Escala de lo afirmable, de menor a mayor: un harness ⇒ «bajo este harness»; dos o mas que replican ⇒ la direccion no se explica solo por el harness ni solo por la familia de modelo; dos o mas que **no** replican ⇒ el resultado es **propiedad del andamiaje y no del metodo**, que es un hallazgo y no un fracaso, y probablemente el mas util que este diseño puede producir para el resto de la agenda.

## Riesgos

1. **Techo del control** — `C0` pasa casi todo y ningun brazo puede mostrar diferencia. Es el modo en que A-04 cerro dos veces. Mitigado por la banda de Fase 0.B, y el enunciado sintetico existe para poder mitigarlo.
2. **Piso** — el enunciado es tan dificil que todos los brazos quedan cerca de 0 y el instrumento tampoco discrimina. La misma banda de Fase 0.B lo cubre por el otro extremo.
3. **Efecto de operador** — un brazo pierde porque lo manejamos mal, no porque su metodo sea peor. Mitigado sellando la ficha de interfaz de cada brazo, con su secuencia de invocacion tomada de la documentacion oficial de esa fuente. **No queda eliminado**: la habilidad para conducir cada herramienta es parte de lo medido y MUST declararse.
3-bis. **Un brazo no se puede invocar, o su producto no se puede medir.** Es el riesgo que Fase 0.A existe para descubrir **antes** del sello, y la razon por la que esa fase corre primero y sobre un enunciado descartable. Si aparece igual a mitad de tanda, la regla ya esta escrita —brazo INEJECUTABLE, celdas anuladas, bateria sigue, fixture intacto— y su valor es justamente estar escrita de antemano: improvisarla con datos a la vista es el grado de libertad post-hoc mas facil de cometer sin notarlo.
3-ter. **La contabilidad de tokens no es identica entre brazos, o no incluye subagentes.** Si Fase 0.A muestra que `S2` no se lee del mismo modo para todos, **H3 no se puede evaluar** y MUST retirarse del criterio de exito antes del sello, no al ver los datos. El caso mas probable y mas dañino es que el contador no atribuya el consumo de subagentes a la corrida padre, porque subcontaria justo al brazo del que trata H3. No afecta a H1 ni a H2. Detalle en §Protocolo de medicion de costo.
3-quater. **`S2` como numero unico puede medir el harness y no el metodo.** Los brazos ceremoniales releen su propia spec y generan mucha lectura de cache; un total que la pondere a peso completo los castiga por una propiedad del regimen de cache, y uno que la excluya los favorece por lo mismo. Mitigado publicando siempre los tres componentes por separado, de modo que la ponderacion quede a la vista y sea recomputable. **No queda eliminado**: la primaria sigue siendo un total y esa eleccion es discutible.
4. **Confundido de harness y familia de modelo** — inseparable **dentro** de cada harness, escalon 3, declarado. Mitigable solo por replicacion de la bateria entera en un segundo harness, que no lo separa pero lo vuelve menos plausible como explicacion unica.
5. **Autoria del fixture** — enunciado y suite los escribe quien evalua, y quien evalua tambien escribio T3. Acotado por sellado previo, invisibilidad de la suite para los brazos y puntuacion sin juicio; **no eliminado**.
6. **`n`=3** — resolucion para dispersion, no para tasas. Declarado.
7. **Costo** — 30 corridas por harness, cada una un proyecto entero. Es el experimento mas caro del repositorio, y la replicacion lo multiplica por la cantidad de harnesses. Orden de recorte, si el presupuesto obliga: primero se recortan **harnesses** —bajando el techo de lo afirmable, que es una perdida declarable—, despues **reps**, declarando la perdida de resolucion. **Nunca** se recorta R2, que es lo que sostiene la equidad entre brazos, ni la completitud de una bateria, que es lo que impide elegir post-hoc que brazo corre en que harness.
8. **Ausencia de los dos casos cerrados** — Kiro y Tessl no corren. Tessl es el unico que regenera desde la spec, y su ausencia significa que B-09 **no dice nada** sobre el paradigma *spec-as-source*. Esa pregunta vive en el item #20 del backlog y MUST NOT leerse contestada por aca.

## Plan de captura de datos

- Repositorio de datos externo `experimentosdd-b9/`, siguiendo el patron de `experimentosdd-a4/` y `experimentosdd-b7/`: este repositorio conserva diseño, runbook y resultado; los workspaces generados, transcripts, hashes de sello y bitacora de tanda viven alla.
- **De Fase 0.A se conservan las fichas de interfaz y el veredicto go/no-go por brazo, y se descarta todo lo demas.** El enunciado descartable, sus workspaces y sus puntajes no se archivan como dato: existieron para probar que el circuito cierra, y conservarlos invita a leerlos despues como si fueran resultados.
- Por rep se conserva: hash del fixture, commit del tratamiento, version efectiva de harness y modelo, transcript completo, workspace entregado, salida cruda de la suite, y `S2`/`S3`.
- El runbook de medicion —`PRUEBA-*.md`— es documento autorado y **MUST tener spec registrada** antes de escribirse (`../../SPECS_REGISTRY.md` §Docs excluidos). Este diseño no la reemplaza.

## Referencias

- [R10] GitHub Spec Kit — brazo T1.
- [R37] obra/superpowers — brazo T4.
- [R38] Fission-AI/OpenSpec — brazo T2.
- [R39] mberliner/sdd-first — brazo T3. **Mismo autor que este repositorio.**
- [R44] Kiro — excluido de la poblacion por imposibilidad de sello.
- [R46] Tessl — excluido de la poblacion por indisponibilidad.
- [R47] Hilos publicos de practica — origen de la objecion de consumo que H3 convierte en medicion.
