# Prueba Observacional del Corpus B-07 — Runbook (H1, H3)

## Propósito

Protocolo paso a paso para medir las hipótesis **`H1` (cobertura)** y **`H3` (fronteras)** sobre el corpus observacional de B-07. Es el hermano observacional de `PRUEBA-REGENERABILIDAD-B7.md`, que cubre la métrica primaria.

- SSOT de hipótesis, métricas y criterio: **`EXPERIMENTO-B7-formato-hibrido.md`**. Este doc es SSOT del **cómo**, no del qué.
- Criterio aplicable: **(b)** de `EXPERIMENTO-B7-formato-hibrido.md` §Criterio de exito.
- `H2` quedó **degradada a descriptiva** (2026-07-29) y MUST NOT integrar el criterio; se reporta como contexto cualitativo (§Fase 3).
- `H4` no se mide acá: se cerró en `RESULTADO-EXPERIMENTO-B7.md`.

**Naturaleza del estudio: retrospectivo y observacional.** No hay asignación, no hay ciego posible —el tratamiento *es* el artefacto visible— y el techo de conclusión es **descriptivo**. MUST NOT enunciarse ningún resultado como efecto del formato.

## Glosario

### Brazos

- **CAS-OBS** = `SPEC-001`, `SPEC-002`, `SPEC-003` (formato casero). **NO están congeladas al 2026-05-24** — ver §Reglas criticas 7 y `obs/prereg/ENMIENDAS.md` Enmienda 2. Se miden en el estado del corte, con su evolución posterior incorporada y declarada.
- **HIB-OBS** = `SPEC-004`, `SPEC-005`, `SPEC-006`, `SPEC-008` (formato híbrido; escritas 2026-05-25, cerradas 2026-06-06).
- Excluida `SPEC-007` (estado `notas`, fuera de secuencia). Excluida `SPEC-013` (entró al 2×2 primario, no al corpus observacional).

### Corte observacional

**`3f1ed33`** ("Importa proyecto agent_test_suite", 2026-06-13) del repo testigo. MUST medirse ahí, no sobre el texto vigente de las specs.

Razón: **todo el ciclo de vida del corpus es pre-git**. El repo se inicializó el 2026-06-13 (`248636a`) y el corpus cerró el 2026-06-06. Las 7 specs entran en un solo commit y todo lo posterior es edición tardía (`SPEC-004` tiene toques hasta 2026-07-07). MUST declararse la deriva 2026-06-06 a 2026-06-13 como límite: el corte es el estado versionado más cercano al cierre del corpus, no el cierre mismo.

**Medido en Fase 1 (2026-07-29): el corte difiere del texto vigente en 3 de las 4 specs híbridas.** `SPEC-004` 11 IDs en el corte vs 12 hoy; `SPEC-005` 13 y 13; `SPEC-008` 12 vs 14; y **`SPEC-006` 49 en el corte (34 `FR-` + 15 `SC-`) contra 34 hoy, con los dos esquemas —plano y multi-HU— conviviendo**. El corte es el estado *más desordenado*: la consolidación ocurrió después. Esto vindica medir en el corte y **agrava el outlier**: 49 contra 11/13/12 de sus hermanas de brazo es un spread de 4x, no de 2.5x como se estimó sobre el texto vigente, lo que vuelve al *leave-one-out* todavía más necesario.

### Tiers de evidencia

- **Tier A, mecánico y auditable** desde el artefacto congelado y el código: `H1`, `H3`. **Sólo Tier A integra el criterio (b)**.
- **Tier B, narrativo e indicativo**: `H2` (revisiones reactivas) y **costo de redacción**. Se reportan como contexto; MUST NOT sostener ni no-sostener ninguna hipótesis.

### Roles

- **Extractor-1** y **Extractor-2**: producen de forma independiente el inventario de requisitos y el mapeo requisito a verificador. SHOULD — modelos o sesiones distintas entre sí y del orquestador; MUST — sin acceso a las hipótesis ni al criterio (reciben sólo la regla de extracción y el material).
- **Orquestador**: corre el tooling determinista (`H3`, agregación, sensibilidad), consolida y reporta. MUST NOT producir el inventario por su cuenta.
- **Custodio** (usuario): sella la Fase 0 y decide ante desacuerdo irreducible entre extractores.

## Reglas críticas de medición (por qué el diseño es así)

1. **`N/A` no es `0`.** Cuando una métrica cuenta ocurrencias de una sección o convención que sólo una de las dos anatomías contempla (`FR-`/`SC-`, ausentes en casero; `[NEEDS CLARIFICATION]`, ídem), el brazo sin la convención MUST registrarse como **`N/A`** y MUST NOT entrar a promedio ni ratio. Reportarlo como `0` convierte una asimetría de anatomía en un valor medido y produce una tautología a favor del tratamiento. Precedente: `PRUEBA-REGENERABILIDAD-B7.md` §3.6-bis descartó dos ítems de `R5` por esta razón. Anti-patrón general en `../06-BACKLOG-INVESTIGACION-FUTURA.md` §Prioridad alta 6.

2. **El *Coverage mapping* MUST NOT ser el instrumento de `H1`: es el tratamiento.** Sólo el brazo híbrido lo tiene. Medir cobertura leyendo la tabla que un solo brazo posee es la misma falacia del punto 1. El numerador se establece con un mapeo requisito a verificador construido con **la misma regla en los dos brazos**.

3. **Cada formato aporta su propia anatomía de requisitos.** El estudio mide los formatos **como se practicaron**, no una versión normalizada: normalizar la atomización descartaría parte del tratamiento. El precio es que la granularidad de los denominadores puede diferir entre brazos, y por eso §Definicion operacional obliga a reportarla y a correr la variante de sensibilidad.

4. **Imposibilidad de cegado, y qué se hace en su lugar.** El formato es obvio al mirar el artefacto. Compensaciones: mecanizar todo lo mecanizable, extracción por dos roles independientes que no conocen las hipótesis, regla de extracción sellada antes de ver el corpus, y congelado por hash de todo inventario antes de aplicarlo.

5. **Confusión estructural, y el techo que impone.** El brazo casero se escribió antes, con menos madurez de repo y sobre features distintas, y el gate `check_traceability.py` existió **sólo** sobre el brazo híbrido (apareció el 2026-06-06). Formato está confundido con tiempo, madurez, feature y enforcement. **Veredicto máximo alcanzable: descriptivo.** Vocabulario admitido: *"consistente con"*, *"no consistente con"*, *"no concluyente"*.

6. **HARKing en `H3`.** El split `SPEC-006` a `006+008` es la observación que **generó** `H3` y MUST NOT usarse como su confirmación. De ahí que `H3` se mida con un indicador topológico independiente extraído del código.

7. **El brazo control NO está congelado, y no se filtra. [Enmienda 2, 2026-07-29]** La Fase 1 verificó que las tres specs
   casero se editaron después del congelamiento declarado del 2026-05-24: `SPEC-001` con 7 revisiones `rev.2026-05-25` más una
   `rev.2026-05-27`; `SPEC-002` y `SPEC-003` con entradas de historial hasta el **2026-06-08**, posterior al cierre del corpus
   híbrido; y las tres referencian specs posteriores, varias híbridas. **Se mide el corte tal cual.** Razón: el contenido
   agregado son bloques `**Pendiente (rev.…)**` con casillas completadas que, bajo la Regla C y `DEF-VERIFICADOR.md`, cuentan
   como **declaraciones de verificación**, luego la contaminación **mejora la cobertura del control** y sesga **en contra de
   `H1`**. El signo del sesgo es conocido, así que filtrarlo movería el resultado hacia la hipótesis a sabiendas. MUST — si `H1`
   favorece al híbrido, reportar que lo hace **a pesar** de un control mejorado post-congelamiento; si favorece al casero, la
   contaminación queda como **explicación alternativa declarada**. MUST — reportar por spec el conteo de referencias a
   identificadores de otros documentos (Enmienda 1), que mide cuánta ontología ajena absorbió el control.

## Definicion operacional

Sección obligatoria por `../templates/EXPERIMENTO.md`. Todo lo de acá MUST quedar sellado en Fase 0 antes de tocar el corpus.

### Unidad de requisito (denominador)

| brazo | denominador |
|---|---|
| **CAS-OBS** | **aserciones normativas atómicas del cuerpo** de la spec (secciones de dominio, validación, integración): una oración o *bullet* que impone una obligación verificable sobre el comportamiento del sistema. Las condiciones alternativas explícitas cuentan por separado. |
| **HIB-OBS** | los **`FR-` y `SC-` declarados**, cada ID una vez. Ambos son requisitos: los `SC-` son criterios de resultado medibles enunciados en el cuerpo. La tabla de *Coverage mapping* **no** es un segundo inventario. |

**Disparador de la unidad — [Enmienda 1, 2026-07-29]:** el criterio que decide qué fila de la tabla aplica es la
**declaración propia**, no la presencia de un token. Una spec cae en la fila híbrida si **introduce identificadores como
etiquetas de sus propios requisitos**; una mención que atribuye el identificador a otro documento (cita, enlace `[[...]]`,
referencia cruzada) **no** la mueve de fila y se registra como `token-descartado` con razón `referencia-a-otro-documento`.
Motivo: `SPEC-003` (casero, sin IDs propios) contiene `` [[SPEC-003b-rejected-response]] FR-002 ``, y con el disparador
literal habría quedado medida con **denominador 1**. MUST — esas referencias se **cuentan y reportan por spec**: miden cuánta
ontología ajena absorbió el brazo control (ver §Reglas criticas 7).

Reglas comunes:

- MUST — un *bullet* de §Criterios de aceptación del casero entra al denominador **sólo si introduce una obligación ausente del cuerpo**; si no, es **verificador**, no requisito. Razón verificada en el artefacto: los §Criterios de aceptación del casero son una **declaración informal de verificadores** (*"Tests unitarios cubren: ... (30 tests)"*, *"mypy --strict verde"*), y uno solo de sus *bullets* puede cubrir varias aserciones del cuerpo.
- MUST — los criterios de **tooling** (`mypy` verde, `ruff`, `check_naming`, `lint-imports`, cobertura mayor o igual a X) se inventarían **aparte en ambos brazos** y quedan **fuera** del denominador: no son requisitos sobre el comportamiento del sistema y su verificador es trivial, así que incluirlos infla la cobertura del casero, sesgo **en contra** de `H1`. MUST reportarse cuántos se excluyeron por spec.
- MUST — reportar el **conteo de unidades por spec de ambos brazos** junto al resultado, para que la comparabilidad de granularidad sea visible al lector y no un supuesto.

### Verificador declarado (numerador)

Un requisito **tiene verificador** si existe al menos uno de:

1. **test** que lo ejerce (unitario o de integración, en el corte);
2. **gate ejecutable** del *pipeline* que lo verifica (`tools/*.py`, `mypy`, `lint-imports`);
3. **verificación visual o documental registrada** (confirmación asentada en la spec o en `historial/sdd.md`).

Un requisito sin ninguna de las tres cuenta como **sin verificador**. `H1` = proporción de requisitos sin verificador, por spec.

Fundamento de la clase 3: la doctrina del propio testigo declara la relación requisito a verificador como **N:M** y asigna los requisitos de UI y de consistencia documental a *"revisión/verificación visual, no `pytest`"* (`historial/sdd.md`, 2026-06-06).

### Indicador de `H3` (topológico, independiente)

Por spec, sobre el corte y a partir de las rutas `src/` que la spec cita explícitamente (verificado: las 7 specs citan entre 2 y 5):

- **Colisión de archivos**: nº de archivos `src/` citados por **más de una** spec del mismo brazo. Frontera sucia = dos specs escriben el mismo módulo.
- **Capas cruzadas**: nº de capas hexagonales distintas (`domain`, `ports`, `application`, `adapters`, `dashboard`, `runner`) que toca la spec.
- **Fan-out de imports nuevos**: aristas de import que el delta de la spec agrega entre módulos.

MUST — normalizar capas cruzadas y fan-out por **nº de archivos citados** por la spec, para no medir tamaño de feature en vez de limpieza de frontera. MUST — reportar crudo y normalizado.

### Validación de los instrumentos (antes de puntuar)

- **Inventario de requisitos**: MUST correr los dos extractores sobre **una spec de calibración de cada brazo** y reportar el **acuerdo** (unidades coincidentes sobre total). Desacuerdo mayor al 20% implica que la regla de extracción es ambigua y MUST refinarse **antes** de inventariar el resto, con la refinación fechada.
- **Mapeo requisito a verificador del brazo híbrido**: MUST validarse cruzando contra `tools/check_traceability.py`, que es el gate propio del proyecto sobre esa relación. Divergencia se registra y **prevalece el gate** (misma regla que `PRUEBA-REGENERABILIDAD-B7.md` §3.3-bis).
- ~~**`H3`**: MUST verificarse que el extractor de rutas reproduce, para `SPEC-006` y `SPEC-008`, el split conocido `006` a `006+008`. Si no lo detecta, el instrumento no ve fronteras.~~ **[Enmienda 7, 2026-07-31] ANULADA: contradice §Reglas criticas de medicion 6**, que prohíbe usar el split como confirmación de `H3` por ser la observación que lo generó. La compuerta pedía validar el instrumento contra esa misma observación, y además contra un evento interno al brazo de tratamiento. **No se reemplaza:** fabricar ahora una compuerta con los valores de `H3` ya calculados sería el mismo HARKing por otra puerta. `H3` **sigue puntuando** —una métrica pre-registrada no sale porque su compuerta resultó inválida— pero queda **sin validación de instrumento**, y eso MUST reportarse con su resultado junto al defecto de resolución registrado en `experimentosdd-b7/obs/prereg/ENMIENDAS.md` §Enmienda 7.

### Granularidad, agregación y empate

- **[Enmienda 5, 2026-07-30] `H1` se calcula DOS VECES, una por extractor, y no se consolida.** Cada
  `H1(En)` usa el denominador **y** los juicios de verificador del inventario de ese extractor. Toda la
  maquinaria de abajo —medianas, distribución, *leave-one-out*, variante neutral, piso de ruido— se corre
  completa sobre cada uno. **La dirección MUST sostenerse en los dos; si divergen, `H1` es NO
  CONCLUYENTE** y la divergencia es el hallazgo. Motivo medido con 9 pares: el desacuerdo de la Regla A
  entre extractores es **sistemático y direccional** (`E1` atomiza más fino que `E2` en 4 de 5 pares),
  luego consolidar es elegir granularidad, y esa elección fija el denominador **sólo en el brazo casero**.
  El umbral de acuerdo pasa de compuerta a **propiedad reportada**; MUST seguir reportándose por spec.
- Unidad de reporte = **la spec**. MUST reportarse la distribución completa por spec de los dos brazos.
- Comparación entre brazos = **mediana**, con **solapamiento declarado dentro del enunciado** del veredicto.
- MUST — sensibilidad ***leave-one-out***: si quitar cualquier spec individual invierte la dirección de la mediana, el veredicto es **NO CONCLUYENTE**.
- Medianas iguales implica **NO CONCLUYENTE**.
- MUST NOT promediarse dentro de un brazo ni fundirse `H1` con `H3` en un índice.

### Independencia entre métricas

`H1` y `H3` se calculan de fuentes distintas (inventario de requisitos vs topología de archivos) y MUST reportarse por separado. Comparten un solo insumo, el mapeo spec a archivos, así que un error ahí las afecta a ambas: MUST declararse como **modo de fallo común**.

### Variante de sensibilidad (obligatoria)

Además del cálculo primario con la anatomía de cada formato, MUST computarse `H1` con la **unidad neutral aplicada a los dos brazos** (aserciones normativas atómicas también en el híbrido, ignorando sus IDs). Uso: control de la asimetría de granularidad.

**Regla de decisión: la fija el SSOT.** Las cuatro cláusulas viven en `EXPERIMENTO-B7-formato-hibrido.md` §Criterio de exito (b) desde el 2026-07-30 (antes estaban sólo acá, sin veredicto declarado ante divergencia). Resumen operativo, sin duplicar el normativo:

- **Coincidencia de dirección ⇒ preocupación por granularidad descartada**, pero sólo si **ninguna** de las dos variantes invierte dirección en su *leave-one-out*: MUST correrse el `LOO` sobre las dos.
- **Divergencia de dirección ⇒ `H1` NO CONCLUYENTE**, y la divergencia se reporta como el hallazgo. MUST NOT resolverse eligiendo una de las dos.
- **Piso de ruido:** MUST reportarse la discrepancia **casero-primaria vs. casero-neutral** (mismo brazo, misma Regla A, sesiones distintas) junto a `H1`. Si es del mismo orden que la brecha casero-vs-híbrido, `H1` es **NO CONCLUYENTE**.
- MUST NOT — la variante neutral **no se promueve a primaria** después de ver los dos resultados. El cálculo primario es y sigue siendo el de la anatomía propia de cada formato.
- No aplica a `H3`: su indicador es topológico y no usa unidad de requisito.

**Instrumento — [Enmienda 3, 2026-07-30].** Aplicar la unidad neutral al brazo híbrido es aplicar la
**Regla A** a documentos que declaran identificadores, lo que el disparador sellado prohíbe y lo que
`extractor_run_v2.py` no podía pedir: **la variante obligatoria no tenía instrumento**. Se agrega un
**selector de regla externo** (`extractor_run_v3.py --regla {auto,A,B}`, `--variante {primaria,neutral}`)
que fija la regla con precedencia sobre el disparador, sin tocar el texto de la regla, la Regla C, la
Regla D, `DEF-VERIFICADOR.md` ni el formato de salida. Dos condiciones obligatorias:

- MUST — en la variante neutral se corren **los dos brazos** con `--regla A` explícita, las 7 specs, 14
  sesiones. Reutilizar los inventarios primarios del casero (que ya son Regla A) sería más barato pero
  dejaría a los dos brazos con **texto de instrucción distinto dentro de la misma variante**, y así una
  diferencia observada sería atribuible al prompt: anularía el control que la variante existe para dar.
  Verificado que el bloque del selector agrega **+1392 bytes idénticos a las 7 specs**.
- MUST — la variante neutral escribe en espacio de nombres propio (`INVENTARIO-NEUTRAL-*`) y la
  herramienta aborta antes de invocar al modelo si el destino existe. Ninguna salida primaria puede
  sobrescribirse.

**Subproducto de la simetría: piso de ruido del instrumento.** Correr el casero también con `--regla A`
lo deja **medido dos veces con la misma regla** (sólo cambia el bloque del selector, inerte donde no hay
identificadores). Esa segunda medición no es gasto: cuantifica el **ruido de sesión de extractor** sobre
`H1`, y su consecuencia sobre el veredicto está pre-registrada arriba. Doble uso: verifica además que el
bloque del selector es efectivamente inerte en documentos sin identificadores — si el casero se moviera
mucho, el bloque no es inerte y eso MUST reportarse como defecto de instrumento.

Texto de la enmienda y su verificación de no-regresión: `experimentosdd-b7/obs/prereg/ENMIENDAS.md`
§Enmienda 3.

### Quién mide

Inventario y mapeo: Extractor-1 y Extractor-2, independientes y sin las hipótesis. `H3`, agregación, medianas y *leave-one-out*: orquestador, con tooling determinista y re-ejecutable. Desacuerdo irreducible entre extractores: lo resuelve el Custodio y se registra.

## Protocolo paso a paso

### FASE 0 — Pre-registro y sellado (antes de tocar el corpus)

- **0.1** Fijar el corte: `git worktree` del testigo en **`3f1ed33`**, read-only. Registrar hash.
- **0.2** Congelar por `sha256`, **antes de correrlos**: la regla de extracción de unidades, la definición de verificador con sus 3 clases, la lista de patrones de *tooling* a excluir, y los scripts de `H3`. Registrar los hashes en la bitácora.
- **0.3** Declarar la **predicción por métrica** (dirección esperada de `H1` y `H3`).
- **0.4** Redactar las instrucciones autocontenidas de Extractor-1 y Extractor-2: material inline, sin acceso al repo, sin las hipótesis, sin el criterio. Registrar el texto exacto.
- **0.5** **SELLO** del Custodio sobre 0.1 a 0.4. Después de este punto, cualquier cambio a las definiciones es **enmienda fechada y post-hoc**, con el mismo régimen que las ocho enmiendas de la prueba primaria.

### FASE 1 — Construcción del corpus congelado

- **1.1** Extraer del corte las 7 specs de los dos brazos y las rutas `src/` que cada una cita.
- **1.2** Construir el **mapeo spec a archivos** desde las rutas citadas. MUST — declarar los archivos que ninguna spec cita y los citados por más de una (insumo directo de `H3`).
- **1.3** Inventariar los tests y gates existentes en el corte: son el universo de verificadores de las clases 1 y 2.
- **1.4** Recontar en el corte los IDs del brazo híbrido. MUST — verificar ahí el estado del espacio de IDs de `SPEC-006` (renumeración multi-HU) y de `SPEC-008` (esquema mixto), no en el texto vigente.

### FASE 2 — Medición Tier A

- **2.1** **Inventario de requisitos** por los dos extractores, en sesiones independientes. Calibración y acuerdo primero (§Validacion de los instrumentos), inventario completo después. Congelar cada inventario por `sha256` **antes** de calcular nada. **[Enmienda 5, 2026-07-30] MUST NOT consolidarse los dos inventarios en uno**: `H1` se computa por separado con el de cada extractor y la dirección debe sostenerse en ambos (ver §Definicion operacional, Granularidad). El texto previo mandaba congelar «el inventario consolidado»; consolidar resultó ser **elegir una granularidad** con el dato a la vista, y sólo en el brazo casero.
- **2.1-bis** **[Enmienda 6, 2026-07-31] Entrega parcial de una sesión: se rescata el bloque faltante, no se re-corre.** Si una sesión emite el inventario de requisitos y no los juicios de verificador, el par NO se re-corre: el denominador ya está congelado y una re-corrida **selecciona sobre la variable medida** —la sesión trunca por volumen de salida, y el volumen lo fija cuán fino atomiza el extractor, luego sólo completa si atomiza más grueso—. Se rescatan únicamente los juicios, entregando el bloque de requisitos byte a byte como entrada cerrada, con cobertura exacta de ids exigida. MUST — declararse junto al resultado de esa celda que el juicio lo emitió una sesión distinta de la que atomizó. Ocurrió una vez, en `SPEC-006` neutral E1. Texto e instrumento: `experimentosdd-b7/obs/prereg/ENMIENDAS.md` §Enmienda 6.
- **2.2** **Mapeo requisito a verificador**, misma regla en los dos brazos. Validación cruzada del brazo híbrido contra `tools/check_traceability.py`.
- **2.3** **`H1`** = proporción sin verificador, por spec. Reportar medianas por brazo, distribución completa, conteo de unidades por spec y *tooling* excluido.
- **2.4** **`H3`** = colisión de archivos, capas cruzadas y fan-out, crudo y normalizado, por spec. Reportar medianas por brazo.
- **2.5** **Variante de sensibilidad** de `H1` con unidad neutral en ambos brazos.
- **2.6** ***Leave-one-out*** sobre `H1` y `H3`.

### FASE 3 — Contexto Tier B (no puntúa)

- **3.1** **`H2`, cualitativo.** *Qué* tuvo que agregar cada brazo después: en el casero, los bloques `**Pendiente (rev.…)**` que suman criterios de aceptación faltantes; en el híbrido, los `[NEEDS CLARIFICATION]` declarados y cuándo se resolvieron. MUST NOT construirse ninguna cifra comparable: la variable de salida es un artefacto documental y el tratamiento es un régimen de documentación, luego el formato altera la observabilidad de su propio resultado ("revisó menos" es indistinguible de "documentó menos sus revisiones") y no hay fuente independiente porque git no cubre la ventana. MUST — reportar el conteo de `[NEEDS CLARIFICATION]` como **descripción de un solo brazo**, con el casero en `N/A`, nunca en `0`.
  - Dato de contexto ya verificado: las 7 specs de ambos brazos llevan `## Historial` con entradas fechadas (6/8/4 en CAS, 7/7/10/4 en HIB) y el casero marca además `rev.YYYY-MM-DD` in-line (8/0/2). Es una convención **compartida** por los dos formatos; se conserva como descripción, sin cifra comparable.
- **3.2** **Costo de redacción**, cualitativo y sin umbral: extensión, iteraciones y tiempo observados según `historial/sdd.md`. No puntúa; MAY modular la decisión final de la regla de cierre, y si lo hace MUST declararse cómo.

### FASE 4 — Análisis, cierre y propagación

- **4.1** Evaluar contra el criterio **(b)** de `EXPERIMENTO-B7-formato-hibrido.md`. MUST — respetar el techo descriptivo y la redacción obligada ante solapamiento.
- **4.2** Consolidar reservas: confusión estructural, imposibilidad de cegado, `n` mínima, deriva del corte, modo de fallo común del mapeo spec a archivos, y costo evidencial de la regla relajada.
- **4.3** Escribir el resultado sobre `../templates/RESULTADO-EXPERIMENTO.md`, incluida su sección «Propagacion» con los tres checks corridos.
- **4.4** Cerrar B-07 con los **dos veredictos** que exige la regla de cierre del SSOT: el de (a), ya emitido, y el de (b). MUST NOT fundirse; la decisión declara el peso relativo.

## Documentos que esperan este resultado

Contraparte del check 3 de `../templates/RESULTADO-EXPERIMENTO.md` §Propagacion, declarada acá antes de medir:

- `EXPERIMENTO-B7-formato-hibrido.md` — SSOT; su §Metricas secundarias y su criterio (b) quedan resueltos por esta prueba.
- `../software/LINEAS-INVESTIGACION.md` §B7 — SSOT de agenda; su pregunta 2 (cobertura) queda respondida y su pregunta 3 ya está marcada como no respondible.
- `../software/PLAN-PRUEBAS.md` §B-07 — estado del experimento.
- `../software/COMPARATIVA-SPECKIT-VS-TESTIGO.md` y `../software/DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` — ambos declaran deuda abierta por el corpus observacional.
- `../software/ANALISIS-SPEC-KIT.md` — hueco C1 (cobertura), que `H1` mide.
- `RESULTADO-EXPERIMENTO-B7.md` — su §Deuda arrastrada nombra `H1` y `H3` sin medir.

## Referencias

- SSOT de hipótesis, métricas y criterio: `EXPERIMENTO-B7-formato-hibrido.md`
- Runbook de la métrica primaria, hermano de este: `PRUEBA-REGENERABILIDAD-B7.md`
- Resultado de la métrica primaria: `RESULTADO-EXPERIMENTO-B7.md`
- Hueco C1 (cobertura) y C3: `../software/ANALISIS-SPEC-KIT.md`
- Anti-patrones del marco: `../06-BACKLOG-INVESTIGACION-FUTURA.md`
- Plantillas: `../templates/EXPERIMENTO.md`, `../templates/RESULTADO-EXPERIMENTO.md`

---

### Registro de cambios del documento

- **2026-07-31 (Fase 2.4: `H3` calculado; Enmienda 7, contradicción interna del propio documento)** —
  fijadas primero, a ciegas y commiteadas antes de existir el instrumento, la regla de conteo de `H1`,
  los nueve nombres de salida y el umbral del piso de ruido (`piso(E) >= 0.5 × brecha(E)` en cualquiera
  de los dos extractores fuerza NO CONCLUYENTE, elegido estricto a propósito); escrito y validado el
  contador (`tools/h1_conteo.py`, 28 de 28 celdas OK, **sin emitir ningún numerador**). `H3` se computó
  sobre el corte con la herramienta sellada, y al ir a aplicar su compuerta apareció que **contradice
  §Reglas criticas de medicion 6 de este mismo documento**: pedía validar el instrumento contra el split
  `006` a `006+008`, que es la observación que **generó** `H3` y que la regla 6 prohíbe usar como su
  confirmación. **Enmienda 7** (no viaja al extractor): la compuerta se **anula y no se reemplaza**;
  `H3` sigue puntuando, sin validación de instrumento y con su defecto de resolución declarado —las 7
  specs citan entre 2 y 5 archivos, `SPEC-005` y `SPEC-006` citan el mismo conjunto y salen idénticas,
  y `src/dashboard/app.py` lo citan las cuatro híbridas y domina su colisión. **Reserva:** la
  contradicción se detectó con los valores de `H3` ya calculados, pero su fundamento es **textual** y
  verificable leyendo el documento, sin mirar un solo número; lo que se descarta por inadmisible es
  elegir entre las dos lecturas posibles de «reproducir el split», que sí habría sido una elección con
  el resultado a la vista. Falla de método declarada: el Paso 0 afirmó que sobre `H3` no quedaba
  ninguna decisión abierta, y la condición de aprobación de la compuerta debió fijarse a ciegas ahí.
- **2026-07-31 (Fase 2 COMPLETA; Enmienda 6, nacida del último tramo)** — cerrados los 13 tramos,
  **28 sesiones, 14 pares**. El último (`SPEC-006` neutral) falló de un modo que el guardián no
  cubría: E1 emitió sus 91 unidades de requisito y cerró el turno anunciando que seguía "en la próxima
  respuesta", que en `claude -p` no existe. No fue el tope de salida (ya estaba en 64000, la salida
  pesó 31 KB, `stop_reason=end_turn`) ni la captura (los 4 mensajes se capturaron enteros): el modelo
  se auto-limitó. Como el guardián sólo exigía el bloque `requisitos`, el artefacto se publicó y el
  acuerdo se calculó con **`pares_comparables: 0`** —un número sin numerador de `H1`— sin señal de
  error; el guardián ahora exige los dos bloques y la medición inválida quedó en `out/INVALIDO/`.
  **Enmienda 6** (no viaja al extractor): se rescata el bloque faltante en vez de re-correr, porque
  re-correr **selecciona sobre lo medido** —sólo completa quien atomiza más grueso, y justo en el brazo
  de Regla A, la variante neutral y la spec *outlier*, el eje de la Enmienda 5—, mientras que el
  rescate no puede mover un denominador ya congelado. Cobertura 91/91 exacta; el `ACUERDO` resultó
  **idéntico** (0.6197) al calculado sobre el artefacto truncado, que es la comprobación de que el
  denominador no se movió, y el acuerdo de verificador pasó de 0 pares comparables a **44, con
  0.8636**. **Reserva declarada:** a diferencia de las enmiendas 3 a 5, ésta **no se decidió con cero
  dato a la vista** (el Orquestador ya había visto las 91 unidades y el 0.6197); lo que la hace
  admisible es que la opción elegida es la que impide que ese número influya en el resultado.
  Desviación de régimen en **1 de 28** sesiones, a reportar con esa celda. Auditoría de integridad
  28/28 sin hallazgos; sello 9 de 9. Dato del cierre, sin ninguna proporción de `H1` calculada
  todavía: el brazo híbrido da **1.000 exacto en sus 4 specs** bajo Regla B (primaria) y **cae en las
  4** al forzarle Regla A (neutral: 0.694 / 0.769 / 0.758 / 0.620), o sea que su reproducibilidad
  perfecta es efecto de la regla y no del formato — que es exactamente lo que la variante de
  sensibilidad existía para poder distinguir.
- **2026-07-30 (Fase 2 en ejecución: enmiendas 4 y 5, nacidas de la medición)** — 9 pares medidos
  (`SPEC-001/002/003/004/005/008` primaria, `SPEC-001/003/005` neutral) y dos enmiendas que el propio dato
  obligó. **Enmienda 4** (viaja al extractor): carga de prueba para los §Criterios de aceptación del
  casero, tras `SPEC-002` con desacuerdo 0.296 causado casi enteramente por esa sección (E1 contó 16
  bullets, E2 cero). Funcionó — al re-correr, los dos extractores contaron **exactamente 1**, los
  restantes se reclasificaron a declaraciones de verificación (3/6 a 17/21) y el acuerdo subió a 0.846;
  `SPEC-003` mejoró su acuerdo de verificador a 1.000 y `SPEC-001` de 0.545 a 0.833. **Enmienda 5** (no
  viaja al extractor): `H1` se calcula **por extractor, sin consolidar**, porque el desacuerdo restante
  resultó **sistemático y direccional** —`E1` atomiza más fino que `E2` en 4 de 5 pares de Regla A,
  mientras los 3 de Regla B dan 1.000— luego consolidar sería elegir granularidad con el dato a la vista y
  sólo en el brazo casero. El umbral de acuerdo pasa de compuerta a propiedad reportada, **debilitamiento
  declarado como tal**, justificado por reemplazarlo con una exigencia más dura (que la dirección
  sobreviva a las dos granularidades) y por cortar la escalera de enmiendas de regla de conteo. Efecto
  lateral: se disuelven dos decisiones que habrían sido del Custodio con el dato a la vista (adjudicar el
  acuerdo de verificador, y dirimir los tres pares que exceden el umbral). Validada además la **Enmienda
  3**: `SPEC-005` bajo `--regla A` produce 31/21 aserciones de prosa en vez de sus 13 identificadores.
- **2026-07-30 (regla de decisión de la variante, y registro de este doc en `SPECS_REGISTRY.md`)** —
  revisión de la variante posterior a la Enmienda 3, con cuatro huecos hallados y tres cerrados por
  decisión del usuario, **sin ninguna proporción calculada**: (1) **divergencia entre variantes ⇒ `H1`
  NO CONCLUYENTE** —el texto anterior sólo decía qué *no* hacer ("MUST NOT resolverse eligiendo una")
  sin declarar veredicto, que es el hueco que después se llena con el dato a la vista—; (2) la
  coincidencia de dirección descarta la preocupación por granularidad **sólo si ambas variantes son
  estables al *leave-one-out***, para cerrar el escape de una coincidencia frágil; (3) **piso de ruido
  del instrumento**: la re-medición del casero con la misma Regla A cuantifica el ruido de sesión de
  extractor y, si es del mismo orden que la brecha entre brazos, `H1` es NO CONCLUYENTE. El cuarto hueco
  era de redacción: que la variante no aplique a `H3` estaba implícito y se explicitó. **Las cuatro
  cláusulas se propagaron primero al SSOT** (`EXPERIMENTO-B7-formato-hibrido.md` §Criterio de exito (b))
  y acá queda el resumen operativo, no el normativo. En la misma entrega este documento y
  `PRUEBA-REGENERABILIDAD-B7.md` quedaron **registrados en `SPECS_REGISTRY.md`**: estaban sin spec
  porque la exención de `experimentos/` cubre lo *generado desde templates* y un runbook no lo es —
  hueco de la regla, ahora aclarado en §Docs excluidos.
- **2026-07-30 (Enmienda 3: la variante de sensibilidad pasa a ser ejecutable)** — se detectó que la
  §Variante de sensibilidad, **obligatoria desde el sello**, no tenía instrumento: su cálculo exige
  Regla A sobre documentos con identificadores, que el disparador sellado prohíbe y que
  `extractor_run_v2.py` no podía pedir. Agregado el **selector de regla externo**
  (`tools/extractor_run_v3.py`, `--regla` y `--variante`), documentado en `obs/prereg/ENMIENDAS.md`
  §Enmienda 3. Tres decisiones tomadas **sin ninguna proporción calculada** (al 2026-07-30 no existe
  `CONSOLIDADO-H1.json` y faltan 4 de las 7 specs del inventario primario): (1) **simetría obligatoria**,
  la variante neutral re-corre los dos brazos, 14 sesiones en vez de 8, eligiendo la opción **más
  costosa** de las dos disponibles; (2) la **Enmienda 3 no viaja al extractor** —el paquete incluía
  `ENMIENDAS.md` completo, así que agregarla habría cambiado el material de las 8 sesiones primarias
  faltantes respecto del que vieron las 6 ya hechas, asimetría entre specs causada por una enmienda que
  no cambia ninguna regla de conteo—, resuelto con el marcador `FIN-MATERIAL-EXTRACTOR` y una regla de
  ubicación para enmiendas futuras; (3) el cálculo **primario no cambia** y la neutral MUST NOT
  promoverse. No-regresión verificada sobre las 7 specs: `v3 --variante primaria` reproduce **byte a
  byte** los 7 paquetes ya congelados en `in/`, luego los 6 inventarios producidos con la v2 quedan
  válidos y no se re-corren; el sello de Fase 0 sigue verificando **9 de 9**. Trabajo restante declarado:
  **22 sesiones** (8 primarias + 14 neutrales).
- **2026-07-29 (Fase 0 sellada, Fase 1 ejecutada, enmiendas 1 y 2)** — Fase 0 **sellada** por el Custodio
  (`hash_de_hashes 0eb6ee72…e673`, 9 artefactos, corte `3f1ed33`). Fase 1 ejecutada: 24 archivos `src/` en el corte de los
  cuales 12 no los cita ninguna spec de los brazos, 4 citados por más de una en **ambos** brazos, 20 archivos y **202
  funciones** de test, 10 gates. Dos enmiendas post-sello aprobadas por el usuario, aditivas (los 9 artefactos sellados quedan
  intactos y `sha256sum -c` sigue verificando 9 de 9): **Enmienda 1**, el disparador de unidad pasa de presencia de token a
  declaración propia, porque `SPEC-003` cita un `FR-` de otra spec y habría quedado con denominador 1; **Enmienda 2**, el brazo
  control **no está congelado** al 2026-05-24 y se mide igual, sin filtrar, declarando que la contaminación lo favorece. Texto
  completo en `experimentosdd-b7/obs/prereg/ENMIENDAS.md`; el paquete de extractor pasa a armarse con
  `tools/extractor_run_v2.py`.
- **2026-07-29 (reescritura como runbook ejecutable)** — el documento pasa de notas de diseño a runbook. Agregadas: §Definicion operacional completa (obligatoria por `../templates/EXPERIMENTO.md`: unidad, denominador, numerador, validación de instrumentos, granularidad, agregación, empate, independencia, sensibilidad, quién mide), **Fase 0 sellada**, Fases 1 a 4, §Documentos que esperan este resultado, §Glosario y §Roles. Corregido el **error factual** de la versión anterior, que mandaba *"checkout de commits previos al 6 de junio"*: **no existen**, el repo testigo se inicializó el 2026-06-13, luego el corte es **`3f1ed33`** con la deriva declarada. Incorporadas las decisiones del usuario del mismo día: unidad de medida por anatomía propia de cada formato, tres clases de verificador, y **regla de comparación relajada** a mediana con solapamiento declarado más *leave-one-out*. `H2` baja a Tier B sin cifra comparable (degradada a descriptiva en el SSOT). Se conservan del documento anterior sus cuatro reglas críticas y la nota `N/A` distinto de `0`, ahora integradas en §Reglas criticas de medicion.
- **2026-07-29 (corrección de la fuente de `H2`)** — la versión previa afirmaba que la revisión reactiva sólo era rastreable por `historial/sdd.md`. Es falso: las 7 specs de ambos brazos llevan `## Historial` con entradas fechadas, y el casero marca además `rev.YYYY-MM-DD` in-line. Quedó sin efecto operativo al degradarse `H2`, pero el dato se conserva en §Fase 3 porque describe una convención compartida por los dos formatos.
