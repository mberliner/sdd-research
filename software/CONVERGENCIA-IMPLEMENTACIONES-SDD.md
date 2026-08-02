# Convergencia entre implementaciones de SDD

Fecha: 2026-08-02.
Casos leídos: GitHub Spec Kit v0.8.13 / v0.12.11 [R10], Superpowers v6.2.0 [R37], y el proyecto testigo `evaluador-flujo-intent` (artefactos reales al 2026-08-02, HEAD `6b0d0d7`, 70 commits, constitución v0.6.0).
Alcance: Línea B (software).

SSOT de qué elementos del método SDD son invariantes entre implementaciones independientes y cuáles no. La caracterización individual de cada caso vive en `ANALISIS-SPEC-KIT.md` y `ANALISIS-SUPERPOWERS.md`; acá se lee a través de ellos.

---

## Por qué existe este documento

`ANALISIS-SPEC-KIT.md` venía afirmando que la convergencia entre Spec Kit y nuestro protocolo era alta y que eso reforzaba la hipótesis B6. Esa afirmación tenía dos problemas que este documento corrige.

El primero es de conteo. Los puntos eran dos, y el tercer actor que solía sumarse —el testigo— **deriva de este repositorio**, con sesgo de confirmación declarado en B-06. La incorporación de Superpowers agrega el primer punto que no nació ni de nuestro método ni del de Spec Kit.

El segundo es de archivo. El tema "qué es invariante entre implementaciones" estaba afirmado dentro de un documento cuyo alcance declarado es un solo framework. Su dueño natural es este documento.

**Encuadre que este documento NO hereda.** `COMPARATIVA-SPECKIT-VS-TESTIGO.md` caracteriza a Spec Kit como "el estándar de referencia" en una comparación pareada. Esa jerarquía es propia de aquella comparación y acá no se asume: los tres casos se leen con el mismo instrumento y ninguno es la vara de los otros.

---

## El instrumento y su procedencia

**Instrumento v1** — las ocho filas del mapeo de `ANALISIS-SPEC-KIT.md`, fijadas el **2026-05-24**, más de un año antes de que Superpowers se incorporara al análisis. Esto importa: con libertad para elegir qué comparar, la convergencia se fabrica. El instrumento es anterior a dos de los tres casos y no se le agregó ni se le redefinió ninguna fila después de leerlos.

Las divergencias se reportan con el mismo detalle que las convergencias. Un relevamiento que solo cuenta coincidencias no mide convergencia: la busca.

**Linajes, no implementaciones.** Para efectos de independencia hay **tres linajes**, no cuatro fuentes: Spec Kit; Superpowers; y la línea de este repositorio junto con el testigo, que no son independientes entre sí. Toda afirmación de invariancia de abajo se cuenta sobre linajes.

---

## Veredicto por fila

| # | Concepto | Spec Kit | Superpowers | Testigo / este repo | Veredicto |
|---|----------|----------|-------------|---------------------|-----------|
| 1 | Fuente de autoridad no-negociable | `constitution.md` + Constitution Check como gate | Precedencia declarada (usuario > skills > default); autoridad en el humano, sin artefacto | `CONSTITUTION.md` v0.6.0 + `check_constitution.py`; acá `CONSTITUTION.md` v0.1.0 | **Parcial** |
| 2 | Lenguaje normativo | `MUST` en FR y plantillas [R04] | `MUST`, `HARD-GATE`, "Iron Law"; sin citar RFC 2119 | `MUST` en 12 de 17 specs del testigo; `MUST`/`SHOULD`/`MAY` acá [R04] | **Converge** |
| 3 | Manejo de ambigüedad | `[NEEDS CLARIFICATION]` + `/speckit.clarify` | Conversacional: una pregunta por mensaje, gate de aprobación; sin marcador | `[NEEDS CLARIFICATION]` en 7 specs del testigo + playbook `clarify`; adoptado acá | **Converge el principio, diverge el instrumento** |
| 4 | Validación de consistencia | `/speckit.analyze`, read-only cross-artefacto | `verification-before-completion` + revisión por subagente contra la spec | `check_traceability.py` (determinista) + `[SDD-Check]`; acá `check_docs.py` | **Converge** |
| 5 | Trazabilidad requisito a verificador | Coverage mapping FR/SC a tareas | Ledger de tareas y revisión por tarea; sin coverage mapping | Coverage mapping FR a test, verificado por script en specs `active` | **Parcial** |
| 6 | Circuito de aprendizaje | Declarado ("bidirectional feedback"), no instrumentado | Instrumentado sobre los **documentos de método**, con medición conductual | Instrumentado sobre las **specs**: `Deuda arrastrada` (49 ocurrencias en el historial del testigo), Principio III acá | **Diverge en el objeto** |
| 7 | Registro de specs | Carpeta por feature `specs/[###-feature]/` | Archivos fechados, sin registro ni estado | Registro central por capacidad, con `estado` y `ssot_level` | **Diverge** |
| 8 | Personalización | Presets y extensions | Plugins independientes + adaptadores por harness | `ssot_level`, niveles de profundidad, generación de adaptadores | **Parcial** |

---

## Qué resulta invariante y qué no

### Invariante sobre los tres linajes

- **Lenguaje normativo explícito** (fila 2). Los tres lo adoptan; solo dos citan RFC 2119, así que lo invariante es la práctica, no la norma que la respalda.
- **Un mecanismo de consistencia antes de cerrar** (fila 4). Los tres tienen uno y los tres lo ubican en el mismo punto del ciclo —antes de declarar terminado—, con mecanismos completamente distintos: análisis read-only cross-artefacto, gate conductual con evidencia fresca, y verificación determinista de estructura y cobertura. Es la convergencia más fuerte del relevamiento, precisamente porque las soluciones no se parecen.
- **Precedencia explícita de instrucciones** (fila 1, forma débil). Los tres declaran un orden de autoridad. Lo que **no** es invariante es quién la encarna: dos la ponen en un artefacto del proyecto, uno en el humano de la sesión.
- **Extensión sin tocar el núcleo** (fila 8, forma débil). Los tres prevén adaptación por una capa externa.

### No invariante, y un caso de difusión mal leída

- **El marcador de ambigüedad no es convergencia: es difusión.** `[NEEDS CLARIFICATION]` aparece en tres de las cuatro fuentes, pero tiene **un solo origen independiente**: lo inventó Spec Kit, este repositorio lo adoptó deliberadamente (`ANALISIS-SPEC-KIT.md`, C2) y el testigo lo heredó de acá. El único linaje verdaderamente independiente que quedaba —Superpowers— **no lo tiene**, y resuelve el mismo problema por diálogo previo. Contar esas tres apariciones como convergencia independiente habría sido un error de conteo; la práctica converge, el instrumento no.
- **El coverage mapping tiene el mismo problema** (fila 5). Nuestro campo `Cobertura` fue adoptado explícitamente de Spec Kit (C1), y el linaje independiente restante no lo implementa.
- **El registro de specs diverge de plano** (fila 7): tres soluciones incompatibles —carpeta por feature, registro central, archivos fechados— para el mismo problema. El único invariante que queda es débil: las specs son archivos versionados que viven junto al artefacto que gobiernan.

### La divergencia más informativa: el objeto del circuito de aprendizaje

`COMPARATIVA-SPECKIT-VS-TESTIGO.md` cerró su síntesis sobre dos ejes ortogonales, regenerabilidad y adaptatividad. Superpowers no entra limpio en ese marco: es débil en regenerabilidad —no regenera nada— y su circuito de adaptatividad **no corre sobre las specs del proyecto sino sobre sus propios documentos de método**, medido por conducta de agentes en sesiones frescas.

Eso sugiere un tercer eje que los dos existentes no capturan: **sobre qué objeto corre el feedback**. Un SDD puede instrumentar el aprendizaje sobre el contrato (las specs se revisan tras la ejecución), sobre el método (el protocolo se revisa según cómo se comporta quien lo lee), o sobre ninguno. Los tres linajes ocupan casillas distintas: el testigo y este repositorio, el contrato; Superpowers, el método; Spec Kit declara el circuito pero no lo instrumenta en ninguno de los dos.

Este documento propone el eje, no lo cierra: se apoya en tres casos y la asignación de casillas sale de leer artefactos, no de medir.

---

## Qué se puede y qué no se puede inferir de esto

**Se puede inferir consenso de diseño.** Tres linajes independientes que llegan a lenguaje normativo y a un gate de consistencia previo al cierre, con mecanismos distintos, indican que esos dos elementos resuelven un problema real y recurrente del trabajo asistido por IA.

**No se puede inferir eficacia, y este proyecto tiene evidencia propia de que la distinción no es teórica.** Que varios equipos coincidan en una práctica muestra acuerdo, no que la práctica funcione — el mismo criterio que aplicamos a fuentes secundarias como [R28] y [R30]. Y hay un caso medido en casa: B-07 puso a prueba justamente el elemento donde la anatomía de Spec Kit debía ganar —la regenerabilidad— y cerró **sin ventaja del formato híbrido** (`../experimentos/RESULTADO-EXPERIMENTO-B7.md`). La convergencia de diseño y el desempeño medido están desacoplados.

**Consecuencia para B6.** La afirmación previa —que la convergencia refuerza la hipótesis B6— MUST leerse en forma más chica. B6 hipotetiza que los tests ligados a specs *detectan divergencia entre contrato y realidad antes de producción*: eso es una afirmación causal sobre un mecanismo, y ninguna cantidad de coincidencia entre frameworks la sostiene. Lo que la convergencia sí respalda es algo más modesto y aun así útil: que el problema que B6 aborda es reconocido de forma independiente por quienes construyen estas herramientas.

---

## Cómo se incorpora un caso nuevo

Este documento está hecho para crecer, y el modo de hacerlo crecer es donde se pierde la honestidad si no está escrito. Tres reglas.

### 1. Primero la procedencia, después la lectura

MUST — todo caso nuevo declara su procedencia antes de contarse. La pregunta no es qué tiene, sino **si lo inventó o lo heredó**: ¿cita, forkea o deriva de alguno de los casos ya presentes?

Un método que adopta la anatomía de otro **no agrega un linaje, agrega una copia**, y sumarlo como punto de convergencia repite el error que este documento corrigió en la fila 3. Puede tener interés por otros motivos —madurez, adopción, ergonomía— y entonces su lugar es `../comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md` o un análisis individual propio, no una columna acá.

El corolario incomoda y por eso conviene tenerlo escrito: **la mayoría de los métodos SDD nuevos no van a sumar linaje**, porque el campo converge por difusión desde pocos orígenes. Un documento de convergencia que crece sin filtro mide popularidad, no invariancia.

### 2. Las dimensiones fuera del instrumento se registran, no se puntúan

Si un caso nuevo hace algo que ninguna de las ocho filas contempla, MUST NOT agregarse una fila para alojarlo: una fila fabricada a medida del caso que la motiva garantiza que ese caso destaque en ella. La observación se registra fuera de la tabla, visible y sin veredicto, hasta que se decida si merece instrumento nuevo.

### 3. Ampliar el instrumento abre versión, y obliga a re-correr todo

MUST — si una dimensión registrada demuestra importar, se fija un **instrumento v2** fechado y se re-corren **todos** los casos contra él, declarando la versión en cada lectura. MUST NOT ampliarse la v1 en caliente: leer unos casos con ocho filas y otros con nueve produce una tabla que no compara nada.

Es el mismo régimen que el proyecto aplica a los experimentos sellados —enmienda fechada y motivada, nunca edición silenciosa (Principio V)—, trasladado a un instrumento de análisis. La diferencia con un experimento es que acá el costo de re-correr es leer documentos, no producir datos: es caro en atención, barato en todo lo demás.

---

[SDD-Check]
- Spec leida: SI (spec registrada en `../SPECS_REGISTRY.md` para este doc; alta en la tabla SSOT)
- Incluye/Excluye verificado: SI - no reproduce la caracterizacion individual de ningun caso (referencia a `ANALISIS-SPEC-KIT.md` y `ANALISIS-SUPERPOWERS.md`), no reproduce la comparacion pareada de cinco dimensiones, y no toma decisiones de adopcion
- Validaciones aplicadas: instrumento declarado con su fecha de origen (2026-05-24), anterior a dos de los tres casos; ninguna fila agregada ni redefinida despues de leer los casos; divergencias reportadas con el mismo detalle que las convergencias; caracterizacion del testigo derivada de sus artefactos reales al HEAD `6b0d0d7` (17 specs, 12 con `MUST`, 7 con `[NEEDS CLARIFICATION]`, 49 ocurrencias de `Deuda arrastrada`, `check_traceability.py`), no copiada de la comparativa; encuadre «estandar de referencia» declarado como no heredado; refs internas verificadas; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: este documento pasa a ser SSOT del tema; `software/ANALISIS-SPEC-KIT.md` deja de sostener la afirmacion de convergencia y la referencia
- Derivados a revisar: `software/ANALISIS-SPEC-KIT.md` (afirmacion de convergencia e inferencia hacia B6, corregidas en la misma entrega); `software/COMPARATIVA-SPECKIT-VS-TESTIGO.md` (su marco de dos ejes queda incompleto ante el tercer caso; se le añade puntero, no se reescribe su sintesis)
- Cobertura: completa - las ocho filas tienen veredicto, cada afirmacion de invariancia declara sobre cuantos linajes se cuenta, y el procedimiento de incorporacion cubre los tres casos que lo tensionan (caso heredado, dimension fuera del instrumento, ampliacion del instrumento). Ampliacion 2026-08-02: seccion «Como se incorpora un caso nuevo» e instrumento etiquetado v1, con enmienda del `incluye` y la `validacion` de la spec en la misma entrega
- Deuda arrastrada: Kiro y Tessl, nombrados en [R20] y aun sin pasar por el filtro de procedencia de la seccion nueva, son los dos candidatos conocidos y no estan dados de alta en ningun backlog; el tercer eje queda propuesto y sin cerrar, apoyado en tres casos y en lectura de artefactos, no en medicion; `software/LINEAS-INVESTIGACION.md` B6 conserva su enunciado original, que este documento acota pero no reescribe; la inconsistencia de `deriva_de` detectada en el registro es `M-13`, ajena a este doc
- Riesgos/reservas: dos de los tres casos se caracterizan desde snapshots vendored, no desde correr los sistemas; el tercero es un repositorio propio, con el sesgo de confirmacion de B-06 ya declarado; el conteo por linajes reduce a tres puntos lo que a primera vista parecian cuatro, y con tres puntos ninguna afirmacion de invariancia es fuerte
