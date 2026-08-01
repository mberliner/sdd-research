# Resultado Experimento B-07: Prueba de regenerabilidad del formato híbrido

## Metadata

- ID experimento: B-07 (prueba de regenerabilidad, métrica primaria de H4)
- Fecha cierre: 2026-07-28
- Responsable: proyecto SDD (analisis)
- Sujeto: `agent-test-suite` (proyecto testigo, ver `../software/PLAN-PRUEBAS.md`)
- Diseño: 2×2 por traducción (Feature × Formato), pre-registrado en `PREREG-B7.md`, sellado en el tag `b7/prereg-v1` y enmendado antes de la primera corrida en `b7/prereg-v2` (ver Evidencia adjunta)
- Procedimiento: `PRUEBA-REGENERABILIDAD-B7.md` (runbook)
- Artefactos de ejecución: `/datum1/Descargas/Claudio/experimentosdd-b7/` (fuera de este repo), bitácora append-only en `BITACORA.md`

> **Alcance.** Este documento cierra la **prueba de regenerabilidad**, no el experimento B-07 completo. Las métricas secundarias del SSOT (`EXPERIMENTO-B7-formato-hibrido.md §Metricas`: Cobertura H1, Ambigüedad temprana H2, Divergencia spec↔código, Fronteras H3, Costo de redacción, Specs vivas) **no se miden acá** — ver Hallazgo 7.

### Des-ciego (Fase 4.1)

| RUN | celda | formato | procedencia de la spec |
|---|---|---|---|
| A | F013-CAS | casero | **traducida** (`Traductor` fable-5 desde `SPEC-F013-HIB`) |
| B | F001-CAS | casero | auténtica (`af7109b`) |
| C | F013-HIB | híbrida | **auténtica** (`d12e6f3`, "reescritura compacta") |
| D | F001-HIB | híbrida | traducida (`Traductor` fable-5 desde `SPEC-F001-CAS`) |

---

## Resultado cuantitativo

### Tablero completo

| métrica | F013-CAS (A) | F013-HIB (C) | gana | F001-CAS (B) | F001-HIB (D) | gana |
|---|---|---|---|---|---|---|
| **R1** % tests aceptación, estricta *(criterio)* | **100%** (47/47) | 83% (39/47) | CAS | 93% (28/30) | 93% (28/30) | empate |
| R1 con shim *(sensibilidad)* | 100% | 94% | CAS | 93% | 93% | empate |
| R1 % requisitos, estricta | **100%** (25/25) | 64% (16/25) | CAS | n/a | n/a | n/a |
| R1 % requisitos, con shim | 100% | 88% (22/25) | CAS | n/a | n/a | n/a |
| **R2** lecturas fuera de frontera (refinada) | **6** | 9 | CAS | 0 | 0 | empate |
| R3 rondas de reparación | 0 | 1 | *(derivado de R1)* | 1 | 1 | empate |
| R1 post-reparación | 100% | 100% | empate | 100% | 100% | empate |
| R4 contratos invocados | 6/6 | 6/6 | empate | 2 inv / 1 reimpl | 2 inv / 1 reimpl | empate |
| **R5** adherencia SDD | **0.67** | 0.33 | CAS | 1.00 | 1.00 | empate |

Las dos filas *"% requisitos"* usan denominador **25** (los 38 requisitos de `SPEC-013` menos los 13 sin caso de aceptación en `TESTS-F013`, §3.2-ter). Análisis de sensibilidad al denominador en §Medición exploratoria post-cierre: con 9 de esos 13 recuperados mecánicamente queda **100% vs 74%** sobre 34 — misma dirección, menor magnitud.

`R1` en F001 no admite granularidad de requisito: `SPEC-001` no define IDs `FR`/`SC` en **ninguna** versión (ver Hallazgo 5). `R3=0` en la celda A está **forzado por definición** (runbook §3b.1: `R1=100%` ⇒ `R3=0`), luego no es señal independiente de `R1`.

### Métrica primaria (R1 + R2), por feature — regla de `PRUEBA-REGENERABILIDAD-B7.md §4.3-bis`

- **F013** — `R1(CAS) > R1(HIB)` **y** `R2(CAS) < R2(HIB)`, ambas estrictas ⇒ **el formato casero supera al híbrido en esta feature**. Dirección **contraria a H4**.
- **F001** — empate en las cinco métricas ⇒ **no concluyente**. Por §4.3-bis regla 2, un empate no es evidencia en ninguna dirección y **MUST NOT** leerse como refutación.
- **Sin veredicto global**: §4.3-bis prohíbe agregar features (baselines, *vintage*, complejidad y espacio de requisitos distintos; la unidad de inferencia del diseño es el contraste intra-feature).

### Criterio de éxito de B-07

**NO se cumple, y además NO es evaluable en bloque.**

- La spec híbrida —sujeto del criterio— **no supera en `R1`+`R2` en ninguna feature**: pierde en F013 y empata en F001.
- La cláusula *"mejorar ≥2 secundarias"* es **no satisfacible con este instrumento**: de las tres secundarias medidas (`R3`, `R4`, `R5`), `R4` no separa en ninguna celda y `R3` no es independiente de `R1`, luego el máximo alcanzable es **1**.
- `UMBRAL` quedó pre-registrado como evaluación cualitativa sin corte numérico, así que no aporta filtro.

La no-evaluabilidad es **en sí un resultado**: el criterio se redactó para el experimento B-07 amplio y no para esta prueba.

> **[Actualización 2026-07-29 — el criterio fue reformulado; la deuda queda CERRADA.]**
> `EXPERIMENTO-B7-formato-hibrido.md` §Criterio de exito ahora separa **(a)** la prueba de regenerabilidad (contra `R1`–`R6`) de **(b)** el corpus observacional (`H1`+`H3`), más una **regla de cierre** que obliga a dos veredictos. La cláusula no satisfacible «≥2 secundarias» se reemplazó por «**≥1 secundaria independiente** en el mismo sentido y ninguna en contra», con conjunto admisible `R4`/`R5`/`R6`.
> **Efecto sobre este resultado: ninguno en el veredicto.** Aplicar (a) a lo ejecutado reproduce lo mismo — F013 no cumple la condición 1 (el híbrido pierde en `R1`) ⇒ **H4 no sostenida**; F001 empata ⇒ **no concluyente**; una sola feature discriminante ⇒ **sin veredicto global**; guarda de confusión ⇒ techo **"no atribuible al formato"**. Lo que cambia es el **estado del criterio**: pasa de *no evaluable en bloque* a **evaluable**, y su parte (a) da **"no sostenida"** en lugar de un vacío. La parte (b) sigue **sin medir** (`H1` y `H3` pendientes).
> Reserva declarada: la reformulación se redactó conociendo estos resultados; gobierna réplicas y **no reabre este veredicto**. Ver la nota de método en el changelog del SSOT.

### Medición exploratoria post-cierre (2026-07-29) — los 13 requisitos fuera del denominador

`R1` se automatizó con `pytest`, luego midió **sólo el subconjunto pytest-verificable** de `SPEC-013`: el mapeo de §3.2-ter dejó **13 de 38 requisitos** fuera del denominador por no tener caso de aceptación en `TESTS-F013`. A raíz del alta de `R6` (`EXPERIMENTO-B7-formato-hibrido.md` §Metricas, 2026-07-29) se relevó ese espacio. **Naturaleza de esta medición: exploratoria y NO ciega** — se ejecuta con el sello ya revelado y el orquestador sabe qué celda es cada formato. MUST NOT integrarse a `R1`, ni al criterio de éxito, ni al veredicto; su función es dimensionar cuánto del espacio de la spec quedó sin ver.

El triaje de los 13 muestra que la etiqueta *"sin cobertura"* mezclaba tres cosas y **9 de 13 eran mecanizables**:

| clase | requisitos | instrumento | F013-CAS (A) | F013-HIB (C) |
|---|---|---|---|---|
| Gate objetivo del repo | `FR-US1-004`, `FR-US1-007`, `FR-US1-008`, `FR-US2-005`, `FR-US3-008` | `check_naming.py src tests`; `mypy --strict`; `lint-imports`; diff nulo en `trace_panel.py` | **5/5 verde** | **5/5 verde** |
| Suite existente en `ENV-REF`, fuera de `TESTS-F013` | `FR-US2-002`, `FR-US2-003`, `SC-US2-002`, `SC-US2-003` | `test_result.py` + `test_file_run_repository.py` de `ENV-REF` | **4/4 satisfechos** | **4/4 satisfechos** |
| Irreductiblemente manual | `SC-US1-004`, `FR-US2-004`, `SC-US2-004`, `SC-US3-004` | recorrido funcional en el dashboard con caso real | **sin medir** | **sin medir** |

Validación del instrumento de la segunda clase, por la regla de §3.2-bis: las dos suites difieren del baseline en +58 líneas (`endpoint_url` aparece 9 y 8 veces en `ENV-REF`, **0** en `b7/base-f013-v2`); contra `ENV-REF` dan **29/29 verde** y contra el baseline **4 rojos / 25 verdes** ⇒ discriminan, y los 4 fallos mapean **1:1** con los 4 requisitos de la fila. Ambas celdas: 29/29.

Tres lecturas:

1. **El espacio no medido no escondía señal discriminante.** Los 9 requisitos recuperados están satisfechos en **ambas** celdas. Empate ⇒ no aporta dirección (§4.3-bis regla 2), y en particular **no revierte ni refuerza** el resultado de F013.
2. **`[CORRECCIÓN DE MAGNITUD]` La brecha por requisito estaba inflada por el denominador estrecho.** Extendiendo el denominador de 25 a 34 con los 9 recuperados: **A = 34/34 (100%)**, **C = 25/34 (74%)** — contra el 64% reportado sobre 25. La afirmación de que *"la brecha se ensancha al pasar a granularidad de requisito"* (100/83 por test → 100/64 por requisito) **se sostiene en dirección pero se atenúa en magnitud**: sobre el denominador extendido es 100/74. Los valores de la tabla de arriba **no se modifican** (son los del instrumento pre-registrado y validado); esto es análisis de sensibilidad al denominador, y refuerza el Hallazgo 7.
3. **Sólo 4 de 38 requisitos son genuinamente manuales, y los cuatro están en el dashboard.** Coincide exactamente con la doctrina del propio testigo (`historial/sdd.md`: los `FR` de UI se verifican por revisión visual, no con `pytest`) y con su práctica (SPEC-007 y SPEC-008 cerraron sus `SC` sólo con verificación visual confirmada por el usuario). Ese es el universo de `R6` y **queda sin medir en B-07**: es la única parte del espacio de requisitos de `SPEC-013` sobre la que el experimento no tiene ningún dato.

Evidencia: `experimentosdd-b7/scores/R6-EXPLORATORIO-F013.json` (comandos, hashes de gates, salidas y commits medidos) + registro en `BITACORA.md`. Reproducible desde los tags publicados: `b7/run-a-out`, `b7/run-c-out`, `b7/base-f013-v2` y `8bff08c`; los worktrees de medición fueron scratch y se removieron.

---

## Resultado cualitativo

### Hallazgos

**1. La dirección del efecto es contraria a H4, en la única feature que discriminó.** Tres métricas separan en F013 —`R1`, `R2` y `R5`— y las tres apuntan al mismo lado: la celda casero regeneró más completo, consultó menos fuera de la frontera y adhirió más al proceso SDD del propio proyecto. La convergencia de tres instrumentos independientes es la parte sólida del resultado.

**2. `[LÍMITE PRINCIPAL]` Formato y procedencia están perfectamente confundidos.** En F013 la celda ganadora (CAS) es la **traducida** y la perdedora (HIB) es la **auténtica**. El diseño en diagonal existía justamente para repartir el sesgo de traducción entre formatos, pero **sólo cancela si ambas features aportan señal** — y F001 empató. Con una sola feature discriminante, el diagonal no cierra y quedan tres explicaciones compatibles con los mismos datos, **indistinguibles con este diseño**:

   a. **Efecto de formato** — el casero regenera mejor.
   b. **Efecto de traducción** — el `Traductor` (fable-5), al reescribir `SPEC-013` al formato casero, la mejoró: desambiguó, explicitó, expandió. El efecto sería del *acto de traducir*, no del formato destino.
   c. **Defecto del artefacto auténtico** — la `SPEC-013` auténtica es literalmente una *"reescritura compacta"*; compactar pudo haber removido información.

   La explicación (c) tiene apoyo interno independiente: la celda HIB necesitó **9** lecturas fuera de la frontera contra **6** de la CAS, es decir fue a buscar afuera lo que su spec no le daba; y ya estaban registrados como reserva previa los 13 requisitos de `SPEC-013` sin cobertura de test y la derrama de US2 hacia la persistencia. **MUST — este resultado no puede atribuirse al formato sin desambiguar (a), (b) y (c).**

**3. La mitad del diseño quedó muda.** F001 empata en las cinco métricas, hasta en los dos tests rojos idénticos (`TestCase.expected()` ausente y `marcadores` sin coerción a tupla). Dos lecturas incompatibles: el formato sólo importa donde hay superficie de integración; o F001 es demasiado simple para discriminar. **El experimento no puede elegir entre ellas.** Consecuencia práctica: el 2×2 aportó, de hecho, un solo contraste.

**4. Una ronda de retroalimentación borra la diferencia.** Las cuatro celdas llegan a `R1_post = 100%` con `R3 ≤ 1`, sin regresión de la base. La brecha de 8 tests de la celda HIB —la mayor del experimento— desaparece con un único ciclo que sólo le entrega los fallos, nunca los tests. Si el ciclo de trabajo real incluye ejecutar tests, la diferencia de formato observada en el *one-shot* **no sobrevive al primer rebote**. Es la observación de mayor consecuencia práctica del experimento y la que más lo relativiza.

**5. Los dos formatos auténticos no comparten ontología de requisitos.** `SPEC-001` (casero, vintage 2026-05) **no define un solo ID `FR`/`SC`** — sus criterios de aceptación son bullets en prosa y varios ni siquiera son verificables por la suite (`mypy --strict` verde, `ruff` verde, cobertura 100%). `SPEC-013` (híbrida) sí los define, y hasta trae su propia tabla de trazabilidad. Esto impide expresar `R1` en la misma unidad para las dos features, y es en sí un dato sobre el formato casero de esa época: no ofrece un asidero para trazabilidad automatizable.

**6. `[TRANSFERIBLE]` Un gate de gobernanza que falla abierto no gobierna.** El hook `PreToolUse` del testigo resuelve el intérprete y termina en `[ -f "$PYBIN" ] || exit 0`: si no lo encuentra, **sale 0 y permite la edición**. Ninguna de las 4 celdas tenía `.venv` (crearlo requería Bash, denegado por diseño), así que `tools/sdd_gate.py` **nunca se ejecutó**. La premisa de `PREREG §5.1` ("el proyecto trae enforcement activo") es falsa tal como se ejecutó. Es idéntico en las 4 celdas, así que el contraste intra-feature sobrevive, pero el hallazgo excede a B-07: un gate que degrada a permisivo justo en el entorno menos preparado es un agujero de enforcement silencioso. Registrado en `../agenda/BACKLOG-INVESTIGACION.md`.

**7. `[REFLEXIVO]` El pre-registro no sobrevivió al contacto con la ejecución.** La prueba acumuló **ocho enmiendas post-hoc** al runbook (§2.7, §3.2-bis, §3.2-ter, §3.3-bis, §3.4-bis, §3.6-bis, §3b-bis, §4.3-bis). Ninguna redefine una métrica del pre-registro sellado —todas la *operacionalizan*— y todas están fechadas y justificadas, que es la disciplina correcta. Pero el volumen es la señal: un pre-registro que fija *qué* medir sin fijar *cómo* deja abierto casi todo lo que importa (denominador, aislamiento, granularidad, criterio de admisibilidad de shims, regla de agregación). Dos de esas enmiendas —§3.2-bis y §4.3-bis— corrigieron huecos que, resueltos después de ver los resultados, habrían permitido ajustar el criterio al dato. Es el aprendizaje metodológico más caro de esta prueba.

### Incidentes

- **`VOID` en la 1ª corrida de RUN-D.** Terminó pidiendo aprobación sin tocar `src/` (artefacto estocástico del harness). Anulada y re-corrida idéntica según la regla codificada en §2.7. Tasa `VOID` total: 1/5.
- **Ceguera del orquestador rota en F001 (Fase 4, pre-revelación).** Construir el mapeo test→SC/FR exige leer la estructura de la spec auténtica; como `SPEC-001` no tiene IDs en ninguna versión, una celda cuyo `OUT` cita `FR-nnn`/`SC-nnn` recibió necesariamente la traducción híbrida. La inferencia (`RUN-D` = híbrida) resultó **correcta** al revelarse el sello. **No invalida nada medido**: `R1`–`R5` estaban fijadas y commiteadas antes, y el mapeo no toma ningún input de las corridas, luego carece de grado de libertad sesgable. F013 permaneció ciego hasta 4.1.
- **Modelo del `Puntuador` deprecado a mitad de ejecución** (`claude-opus-4-8` → `claude-opus-5`). No reabrió ninguna corrida: al momento del cambio el `Puntuador` no había puntuado nada (`R1`/`R2`/`R5` salen de *tooling* determinista), así que no hay puntajes mezclados entre scorers.
- **El `Puntuador` fue más estricto que el contrato en `R4`.** Marcó `parcial` a `RUN-D` en `SPEC-000-naming` por `import streamlit`, pero `tools/check_naming.py` —el gate objetivo del propio proyecto— pasa en las 4 celdas: su AST sólo inspecciona identificadores *definidos*. Se codificó que el gate objetivo prevalece y se registran ambos (§3.3-bis).
- **La adjudicación del shim de `RUN-C` la hizo el orquestador, no el `Puntuador`**, pese a que §3.5 asigna `R1`/`R2`/`R4` al `Puntuador`. Es una de las razones por las que el criterio primario corre sobre la variante **estricta**, no sobre la del shim.
- **Ronda de reparación descartada en `RUN-B`.** El primer disparo llamó al modelo y abortó al commitear (el entorno no tenía identidad git). No se registró resultado; se relanzó completo y esa ronda se regeneró. La salida del modelo es estocástica, así que la descartada no es idéntica a la que cuenta.
- **Error de hecho en §4.3-bis, corregido antes de leer el resultado.** La enmienda afirmaba que `R3` no separaba en ninguna celda; en F013 vale 0 y 1. La corrección (no computar `R3` como secundaria, por no ser independiente de `R1`) es direccionalmente inocua: la híbrida no pasa el filtro `R1`+`R2` con ninguna forma de contar.

---

## Decisión

**Ajustar.**

- **No se adopta** una preferencia por el formato híbrido: la evidencia disponible apunta en contra, no a favor.
- **No se descarta** el formato híbrido: el Hallazgo 2 impide atribuir el efecto al formato, y el Hallazgo 4 muestra que la diferencia observada no sobrevive a una sola ronda de retroalimentación.
- Lo que sí se ajusta es el **aparato de evaluación**: el criterio de éxito de B-07 y el nivel de detalle exigido a un pre-registro.

`H4` (la spec híbrida es mejor fuente de regeneración) queda **no sostenida por esta prueba**, con la reserva explícita de que la prueba no la refuta: su única feature discriminante confunde formato con procedencia.

---

## Cambios al marco SDD

> **Estado (verificado 2026-07-29):** 3 de 4 **APLICADOS**. El encabezado anterior de esta sección decía *"(propuestas, NO aplicadas)"* y quedó stale tras la pasada del 2026-07-28.

1. **APLICADO (2026-07-29)** — **Reformular el Criterio de éxito de B-07** en `EXPERIMENTO-B7-formato-hibrido.md` (SSOT de hipótesis y métricas) para que sea evaluable por la prueba que efectivamente se ejecuta: separar las secundarias del experimento amplio de las secundarias de la prueba de regenerabilidad (`R3`/`R4`/`R5`/`R6`), y fijar la regla de agregación por feature. Es cambio a un SSOT → requiere revisar derivados y aprobación. **APLICADO (2026-07-29)**: `R6` dada de alta como secundaria independiente, **H2 degradada a descriptiva** ⇒ secundarias del corpus observacional = **H1, H3 y costo**, y el **criterio reformulado y redactado** en el SSOT — (a) contra `R1`–`R6` con guarda de confusión, (b) contra `H1`+`H3` con techo descriptivo, más regla de cierre a dos veredictos. Ambos pasan la comprobación de satisfacibilidad.
2. **APLICADO (2026-07-28)** — **Exigir que un pre-registro fije la definición operacional, no sólo la métrica.** Checklist mínima derivada de las ocho enmiendas: denominador, aislamiento del entorno de medición, granularidad de reporte, criterio de admisibilidad de reconciliaciones (*shims*), regla de agregación entre celdas, y qué se hace ante un empate. Decisión que habilita: que las decisiones de medición se tomen antes de ver los datos y no después. **Materializado** en `../templates/EXPERIMENTO.md` §«Definicion operacional» y en el check correspondiente de `../SPECS_REGISTRY.md`.
3. **APLICADO (2026-07-28)** — **Adoptar la regla "empate ⇒ no concluyente"** como convención de los experimentos del marco. Evita que una celda muda se lea como refutación. **Materializado** en `../templates/EXPERIMENTO.md` §Definicion operacional, ítem «Tratamiento del empate».
4. **APLICADO (2026-07-28)** — **Registrar el patrón "gate fail-open"** como anti-patrón del marco de gobernanza: un *enforcement* cuya precondición opcional falta MUST fallar cerrado o declararse inoperante, nunca degradar a permisivo en silencio. **Materializado** en `../agenda/BACKLOG-INVESTIGACION.md` §Prioridad alta 4.
5. **APLICADO (2026-07-29)** — **Registrar el anti-patrón "variable de salida que es artefacto del propio tratamiento"** (confusión de visibilidad), derivado de la degradación de H2: cuando el tratamiento es una práctica documental y la variable de salida es ella misma un artefacto documental, el formato altera la **observabilidad** de su propio resultado. Corolario operativo: **`N/A` ≠ 0**. Test de diseño: ¿la variable de salida sobreviviría si el tratamiento no existiera? **Materializado** en `../agenda/BACKLOG-INVESTIGACION.md` §Prioridad alta 6.

---

## Propagacion

Los tres checks de `../templates/RESULTADO-EXPERIMENTO.md` §Propagacion, corridos el **2026-07-29** (esta sección faltaba: el cierre del 2026-07-28 armó su lista de derivados **de memoria**, que es precisamente el fallo que la sección existe para prevenir).

- **Check 1** (`grep -n "B-07" SPECS_REGISTRY.md`): líneas 35, 75, 257, 377, 380, 403.
- **Check 2** (estructural): el SSOT que enuncia la hipótesis es `../software/LINEAS-INVESTIGACION.md` §B7; su derivado registrado es `../software/PLAN-PRUEBAS.md`.
- **Check 3** (`grep -rl "Deuda arrastrada.*B-07"`): `software/COMPARATIVA-SPECKIT-VS-TESTIGO.md`, `software/ANALISIS-SPEC-KIT.md`, `software/DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md`, `experimentos/PREREG-B7.md`.

| documento | qué afirmaba | estado nuevo | hecho |
|---|---|---|---|
| `EXPERIMENTO-B7-formato-hibrido.md` **(SSOT de hipótesis y métricas)** | H2 comparable con ratio upfront/reactivo; métricas `R1`–`R5`; criterio contra H1/H2/H3 | `R6` dada de alta; **H2 degradada a descriptiva** y ratio retirado; criterio (b) pendiente enunciado contra H1/H3 | **sincronizado** (2026-07-29) |
| `software/LINEAS-INVESTIGACION.md` **(SSOT de agenda línea B)** | pregunta de H2 **ABIERTA** | **NO RESPONDIBLE tal como está planteada** | **sincronizado** (2026-07-29) |
| `software/PLAN-PRUEBAS.md` §B-07 | secundarias del corpus = H1/H2/H3 + costo + specs vivas; métricas `R1`–`R5` | alta de `R6` + medición exploratoria; secundarias reducidas a **H1, H3 y costo** | **sincronizado** (2026-07-29) |
| `experimentos/PRUEBA-REGENERABILIDAD-B7.md` | Fase 3 sin `R6` | §3.7 con `R6` + triaje obligatorio en 3 clases | **sincronizado** (2026-07-29) |
| `experimentos/PRUEBA-OBSERVACIONAL-B7.md` | H2 reactivo medible sólo por `historial/sdd.md`; `0/0/0` como valor | fuente primaria = `## Historial` de cada spec; **`N/A` ≠ 0**; H2 degradada ⇒ sin cifra comparable | **sincronizado** (2026-07-29) |
| `../agenda/BACKLOG-INVESTIGACION.md` | 5 ítems en prioridad alta | +6: anti-patrón de confusión de visibilidad | **sincronizado** (2026-07-29) |
| `software/DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` | §9.3 correcta; enumera "ambiguedad temprana" entre las secundarias pendientes de medir | sigue correcta en lo sustantivo (H2 tampoco se midió); la enumeración recibe nota fechada de degradación | **sincronizado** (2026-07-29) |
| `software/COMPARATIVA-SPECKIT-VS-TESTIGO.md` | último `[SDD-Check]` declara la deuda como *"reformular el Criterio de exito"* + *"corpus observacional"* | **exacto, sin cambios**: sigue siendo la deuda vigente. Sus bloques anteriores (líneas 140/152/164) dicen *"sin evidencia"* pero son **registro datado** y MUST NOT reescribirse | **no aplica** — ya sincronizado el 2026-07-28 |
| `software/ANALISIS-SPEC-KIT.md` | matcheó el check 3 por un bloque antiguo; su último `[SDD-Check]` declara deuda de refs `[R33]`/`[R34]`, ajena a B-07 | sin afirmación de estado de B-07 que corregir | **no aplica** — falso positivo del check 3 |
| `experimentos/PREREG-B7.md` | pre-registro sellado en `b7/prereg-v1`/`v2` | **intocable por diseño**: es el artefacto sellado; `R6` y la degradación de H2 son posteriores y viven en el SSOT y el runbook | **no aplica** — sellado |
| `SPECS_REGISTRY.md` | referencia los resultados sin copiarlos; el check de línea 257 ya exige «Definicion operacional» | ninguna afirmación de estado vencida | **no aplica** |

Contraste con el check 3 según manda el template: los cuatro archivos que devolvió el grep estaban **ya cubiertos o justificados**; los cinco documentos realmente afectados por los cambios de hoy **no aparecen en el check 3** —los encontró el check 2 más el rastro de los cambios— lo que confirma que ningún check basta solo.

---

## Evidencia adjunta

- **Pre-registro sellado**: tag `b7/prereg-v1` (`a075729`); `SELLO-CIEGO` sha256 `a90cd5fa…63e6f0`, generado y custodiado por el usuario; procedencia y hashes de las 4 specs en `b7-prereg/PROCEDENCIA.md`.
- **Pre-registro vigente en Fase 2**: tag `b7/prereg-v2` (`439b110`, 2026-07-12). Enmienda **anterior a toda corrida** (la primera es del 2026-07-28) que cambia **sólo** `PREREG-B7.md`: prompt de contexto pleno, `R2` redefinida como contexto declarado por la spec, e incorporación de `R5`. Las 4 specs y el `SELLO-CIEGO` quedan byte-idénticos a `v1`, por eso el sha256 del sello no se mueve. **Es esta versión la que gobernó la regeneración**, verificado mecánicamente: el slot `{SPEC_PATH}` del prompt no existe en `v1`, y los dos `prompt_sha256` de los manifiestos (`991fb6a3…` para F013, `dbc24fe6…` para F001) se reproducen exacto desde `logs/PROMPT-REGENERACION.tpl`. Reproducir el experimento desde `v1` **no** replicaría lo ejecutado.
- **Baselines**: `b7/base-f001-v1` = `6debd93`; `b7/base-f013-v2` = `3c467b6` (ambos por sustracción, gates objetivos verdes).
- **Salidas one-shot**: ramas ciegas `b7/run-a` (`ad7b82d`), `b7/run-b` (`d7e0988`), `b7/run-c` (`aee46cf`), `b7/run-d` (`e49169d`); sólo `src/` + manifiesto.
- **Salidas reparadas**: `b7/rep-b` (`4ab8df0`), `b7/rep-c` (`3ad2e3c`), `b7/rep-d` (`4ff4f78`), tags `b7/run-x-rep1`.
- **Scores**: `scores/R1-*.json` (incl. `CANON` y `BASE` de validación del instrumento), `R1REQ-*.json`, `R3-*.json`, `R4-*.json`.
- **Mapeo test→requisito de F013**: `logs/MAPEO-F013.json`, construido a ciegas y congelado con sha256 `a5772bfb…6c38b5` **registrado antes** de aplicarse.
- **Tooling** (determinista, re-ejecutable): `logs/r1_run.py`, `r1_por_requisito.py`, `r2_extract.py`, `r3_repair.py`, `r4_score.py`, `r5_extract.py`, `mapeo_f013.py`; shim documentado en `logs/shims/RUN-C.conftest.py`.
- **Bitácora append-only** con cada decisión fechada: `experimentosdd-b7/BITACORA.md`.
- Base metodológica externa: tarea aislada + configuración fija [R33]; frontera de contexto y reimplementación [R34]; regenerabilidad como test de gobernanza [R35]; taxonomía spec-first/anchored/as-source [R30].

---

## Deuda arrastrada

> Actualizada 2026-07-29. Convención anti-cascada (B-06): lo diferido se re-explicita hacia adelante hasta resolverse.

- **arrastrado** — Desambiguar formato vs. procedencia (Hallazgo 2). Vías: (a) repetir con una feature **discriminante** donde la auténtica sea casero y la traducida híbrida; (b) medir retención de información traducida-vs-auténtica con independencia de la regeneración. Requiere corrida nueva: es otro experimento, no una tarea de cierre.
- **resuelto (2026-07-29)** — **Criterio de éxito reformulado y redactado** en `EXPERIMENTO-B7-formato-hibrido.md` (SSOT): (a) prueba de regenerabilidad contra `R1`–`R6`, unidad intra-feature, «≥1 secundaria independiente en el mismo sentido y ninguna en contra», **guarda de confusión**; (b) corpus observacional contra `H1`+`H3` con regla de no-solapamiento y techo **descriptivo**; regla de cierre a **dos veredictos**. Desbloquea la reescritura del runbook observacional.
- **nuevo (2026-07-29)** — **`R6` sin recorrido guionado pre-registrado.** La métrica está de alta pero su instrumento no existe; aplica a la próxima corrida. Casilla abierta en el Checklist de pre-registro del SSOT.
- **nuevo (2026-07-29)** — **4 requisitos de `SPEC-013` sin ningún dato**: `SC-US1-004`, `FR-US2-004`, `SC-US2-004`, `SC-US3-004`. Los cuatro son de UI/caso real en el dashboard; son el universo propio de `R6` y la única parte del espacio de requisitos de la feature sobre la que el experimento no tiene medición alguna.
- ~~**nuevo (2026-07-29)** — **`PRUEBA-OBSERVACIONAL-B7.md` no es todavía un runbook ejecutable**: le faltan la sección «Definicion operacional» y una Fase 0 sellada.~~ **RESUELTO (2026-07-29, verificado 2026-07-30)** — el documento se reescribió como runbook ejecutable con §Definicion operacional completa, Fases 0 a 4, roles y glosario; **Fase 0 sellada** (`hash_de_hashes 0eb6ee72…e673`, 9 artefactos) y corte fijado en **`3f1ed33`**, tal como pedía esta deuda. Quedó además **registrado en `SPECS_REGISTRY.md`** (2026-07-30) junto a `PRUEBA-REGENERABILIDAD-B7.md`: ninguno tenía spec, porque la exención de `experimentos/` cubre lo *generado desde templates* y un runbook no lo es.
- **RESUELTO (2026-07-31)** — **`H1` y `H3` medidos; criterio (b) cerrado.** 28 sesiones, 14 pares, corte `3f1ed33`. `H1` **NO CONCLUYENTE** por tres vías simultáneas (divergencia entre variantes de unidad, inversión bajo `LOO` en la primaria y en los dos extractores, piso de ruido de 5 a 8 veces la brecha); `H3` **no consistente** con la hipótesis en los tres ejes, robusto bajo `LOO`, con las reservas de instrumento declaradas. Ver §Resultado del criterio (b). **Deuda nueva que deja:** (i) `H3` sin validación de instrumento tras anularse su compuerta por HARKing (Enmienda 7); (ii) modo de fallo común `src/dashboard/app.py` (citado por 4/4 híbridas y 1/3 caseras) **no descartado**, y su sensibilidad **no se corrió** por no estar pre-registrada; (iii) el hueco C1 de `software/ANALISIS-SPEC-KIT.md` **sigue abierto**, ahora con motivo medido. Texto previo de esta entrada, conservado abajo como registro datado.
- ~~**arrastrado, actualizado 2026-07-30** — **H1 y H3 sin medir**:~~ es lo único que resta para cerrar B-07 integralmente, y está **en ejecución**, no detenido. Fase 1 completa, calibración pasada (acuerdo 0.951 / 1.000), inventario de **3 de 7 specs**, **22 sesiones** de extractor restantes. **Corrección de esta entrada:** decía que `H1` precisa unidad de requisito *neutral al formato*; la decisión del 2026-07-29 fue la **opuesta y deliberada** — el cálculo primario usa **la anatomía propia de cada formato**, porque el estudio mide los formatos *como se practicaron*, y la unidad neutral quedó como **variante de sensibilidad obligatoria**, no como unidad primaria. Desde el 2026-07-30 esa variante tiene instrumento (Enmienda 3, selector de regla externo) y regla de decisión en el SSOT: divergencia entre variantes deja `H1` **NO CONCLUYENTE**, igual que un piso de ruido de instrumento comparable a la brecha entre brazos. Para `H3` sigue en pie el indicador topológico independiente (el split `SPEC-006`→`008` generó la hipótesis y no puede confirmarla).
- **resuelto** — Sincronizar derivados: checklist de `EXPERIMENTO-B7-formato-hibrido.md` y `../software/PLAN-PRUEBAS.md §B-07`.
- **nuevo** — Elegir una feature de control que discrimine, para que un futuro 2×2 no quede con la mitad muda (Hallazgo 3).
- **arrastrado** — Gate SDD *fail-open* del testigo (§4.4-bis): no se corrige retroactivamente en B-07; queda como hallazgo transferible en `../agenda/BACKLOG-INVESTIGACION.md` #4.
- **arrastrado** — Sonda *forward* de `SPEC-009` (test-first sobre spec no implementada), diferida desde el diseño.
- **resuelto** — Los 4 inputs bloqueantes del runbook (`MODELO`, `UMBRAL`, `FRONTERA-F001`, commit padre).
- **resuelto** — La contradicción "regeneración ciega vs. iterar hasta pasar tests", cerrada por la separación `R1` one-shot / `R3` lazo acotado.

---

## Próximos pasos

> Actualizado 2026-07-29.

1. ~~Sincronizar los derivados listados en Deuda arrastrada.~~ **HECHO** — triaje completo en §Propagacion.
2. ~~Llevar al usuario las 4 propuestas de "Cambios al marco SDD" para decisión.~~ **HECHO** — las 4 aprobadas y aplicadas, más una quinta (anti-patrón de confusión de visibilidad).
3. ~~Reescribir `PRUEBA-OBSERVACIONAL-B7.md` como runbook ejecutable.~~ **HECHO (2026-07-29)** — runbook completo con §Definicion operacional, Fase 0 sellada, Fases 1 a 4 y §Documentos que esperan este resultado; corte fijado en `3f1ed33`. Pendiente: **ejecutar** la Fase 0 (sellado) y las Fases 1 a 4.
4. **Medir `H1` y `H3`** sobre el corpus observacional y cerrar B-07 con los **dos veredictos** que exige la regla de cierre. Es lo único que resta para el cierre integral.
5. **Decidir sobre el Hallazgo 2** (desambiguar formato vs. procedencia): requiere **corrida nueva** con una feature discriminante donde la auténtica sea casero, luego es otro experimento y no una tarea de cierre de B-07.

---

```text
[SDD-Check]
- Spec leida: SI (SPECS_REGISTRY.md L54 — contenido de experimentos/ generado desde template, exento de spec propia; EXPERIMENTO-B7-formato-hibrido.md = SSOT de hipótesis y métricas; PRUEBA-REGENERABILIDAD-B7.md = SSOT del procedimiento)
- Incluye/Excluye verificado: SI — cierra la prueba de regenerabilidad; NO redefine hipótesis ni métricas (eso es del SSOT); NO aplica los cambios al marco, solo los propone
- Validaciones aplicadas: veredicto derivado aplicando literalmente §4.3-bis (por feature, ambas condiciones estrictas, empate = no concluyente, R1 estricta en granularidad de test); todas las cifras trazadas a scores/*.json; procedencia de cada celda cruzada con PROCEDENCIA.md; commits y tags verificados; template de RESULTADO-EXPERIMENTO respetado incl. marcado nuevo|arrastrado|resuelto; refs [R30][R33][R34][R35] existentes en REFERENCIAS.md; fechas YYYY-MM-DD
- SSOT afectado: ninguno (doc nuevo de experimentos/); EXPERIMENTO-B7-formato-hibrido.md queda con deuda de reformulación, no modificado acá
- Derivados a revisar: EXPERIMENTO-B7-formato-hibrido.md (checklist + criterio de éxito), ../software/PLAN-PRUEBAS.md §B-07, ../agenda/BACKLOG-INVESTIGACION.md #4
- Cobertura: completa — las 5 métricas tienen valor en las 4 celdas y cada una mapea a un paso del runbook que la produjo; el criterio de éxito se reporta como no evaluable con su justificación, no se omite
- Deuda arrastrada: ver sección homónima (4 nuevos, 2 arrastrados, 2 resueltos)
- Riesgos/reservas: la confusión formato×procedencia (Hallazgo 2) es estructural y no reparable con los datos existentes — condiciona toda lectura causal del resultado; n=1 por celda, sin repetición, luego el contraste mezcla efecto-formato con varianza estocástica de una única generación y ninguna afirmación acá es estadística; F001 no discriminó, así que el 2×2 aportó un solo contraste efectivo; ocho enmiendas post-hoc al runbook (todas fechadas y operacionales, ninguna redefine el pre-registro sellado); ceguera del orquestador rota en F001 antes de 4.1
```

---

# Resultado del criterio (b) — corpus observacional (cerrado 2026-07-31)

> Segundo de los **dos veredictos** que exige la regla de cierre de `EXPERIMENTO-B7-formato-hibrido.md`.
> MUST NOT fundirse con el de (a) ni promediarse. Runbook: `PRUEBA-OBSERVACIONAL-B7.md`. Datos, sello,
> enmiendas y bitácora: repo `experimentosdd-b7/`. Corte observacional `3f1ed33`.
> **Techo de conclusión: descriptivo**, por la confusión estructural declarada (formato confundido con
> tiempo, madurez de repo, feature y presencia del gate `check_traceability.py`, que existió sólo sobre
> el brazo híbrido).

## Ejecución

28 sesiones de extractor (7 specs × 2 extractores × 2 variantes de unidad), 14 pares, `n = 3` specs en
CAS-OBS contra `4` en HIB-OBS. Auditoría de integridad: 28 inventarios, 0 hallazgos. Sello de Fase 0
verificado 9/9 en cada etapa. Siete enmiendas post-sello, todas fechadas y aditivas.

## `H1` (cobertura) — **NO CONCLUYENTE**

Proporción de unidades de requisito **sin verificador declarado**, mediana por brazo, por extractor y
sin consolidar (Enmienda 5).

| celda | CAS-OBS | HIB-OBS | dirección | margen | *leave-one-out* |
|---|---|---|---|---|---|
| E1 primaria | 0.1071 | 0.0896 | HIB menor | −0.018 | **invierte** (`SPEC-001`, `SPEC-002`) |
| E2 primaria | 0.0417 | 0.0294 | HIB menor | −0.012 | **invierte** (`SPEC-001`, `SPEC-004`, `SPEC-005`) |
| E1 neutral | 0.2143 | 0.2448 | HIB **mayor** | +0.030 | no invierte |
| E2 neutral | 0.0400 | 0.0952 | HIB **mayor** | +0.055 | no invierte |

Distribución completa por spec, conteo de unidades y *tooling* excluido: `obs/out/H1-CONTEO-*.json` y
`obs/out/METRICAS-OBS-*.json`. Rangos **solapados en las cuatro celdas**.

**Se disparan tres de las cuatro vías pre-registradas hacia NO CONCLUYENTE:**

1. **Divergencia entre variantes de unidad.** La primaria da HIB menor; la neutral, HIB mayor. La regla
   del SSOT es terminante: *"Divergencia de dirección ⇒ `H1` NO CONCLUYENTE (…) MUST NOT resolverse
   eligiendo una de las dos; la divergencia **es** el hallazgo."* La dirección de `H1` no es propiedad
   del corpus sino de la convención de medición.
2. **Inversión bajo *leave-one-out*** en la variante primaria, en **los dos** extractores.
3. **Piso de ruido comparable a la brecha.** La misma spec del control, medida dos veces con la **misma**
   Regla A, se mueve **0.131** (E1) y **0.098** (E2), contra brechas entre brazos de 0.018 y 0.012: el
   ruido del instrumento es de **5 a 8 veces** el efecto buscado. `piso(E1) = 0.0357` contra un umbral
   de `0.0088` (`obs/out/PISO-RUIDO.json`).

**La cuarta vía NO se dispara, y es informativa:** los dos extractores **coinciden** en dirección dentro
de cada variante. La divergencia no es ruido de modelo — **es la regla de conteo**. Es exactamente la
distinción que la Enmienda 5 existía para permitir: consolidar habría producido el mismo número sin
poder atribuirlo.

**Magnitudes, que MUST leerse con el veredicto.** El margen de la variante primaria (0.012 a 0.018) es
del orden de **una** unidad de requisito cambiando de lado en una spec de ~28, y su inversión bajo `LOO`
al quitar `SPEC-001` es de **+0.0003**: un empate, no una inversión sustantiva. La variante neutral tiene
márgenes de 2 a 4 veces mayores y **no invierte en ninguna** de las 7 omisiones ni en ninguno de los dos
extractores. **La variante que no es la primaria es la robusta.** MUST reportarse; **MUST NOT** usarse
para promoverla (regla 1 de la variante de sensibilidad).

Contra la predicción sellada, que anticipaba `H1` menor en HIB: la primaria coincide pero no sobrevive
al `LOO`; la neutral contradice y es estable.

## `H3` (fronteras) — **NO CONSISTENTE con la hipótesis**

Indicador topológico independiente sobre el corte, normalizado por nº de archivos citados. `H3` sería
**consistente** si la mediana fuera **menor** en el híbrido. Es **mayor en los tres ejes**.

| eje | CAS-OBS | HIB-OBS | dirección | solapamiento | *leave-one-out* |
|---|---|---|---|---|---|
| colisión de archivos | 0.400 | 0.750 | HIB mayor | sí | no invierte |
| capas cruzadas | 0.600 | 1.000 | HIB mayor | sí | no invierte |
| fan-out de imports | 2.20 | 9.75 | HIB mayor | **no** | no invierte |

Enunciado con la redacción obligada ante solapamiento: **tendencia no consistente con `H3`, con rangos
solapados** en colisión y capas cruzadas; en fan-out la separación es **completa** (CAS 2.0–6.0 contra
HIB 8.0–10.5) y ninguna omisión individual invierte ninguno de los tres ejes.

**Tres reservas que acotan fuerte esta lectura:**

- **`H3` quedó sin validación de instrumento.** Su única compuerta pre-registrada —reproducir el split
  `SPEC-006` a `006+008`— se **anuló** (Enmienda 7) por contradecir la regla crítica de medición 6 del
  propio runbook, que prohíbe usar ese split como confirmación por ser la observación que **generó**
  `H3`. No se reemplazó: fabricar una compuerta con los valores ya calculados sería el mismo HARKing por
  otra puerta.
- **Resolución pobre.** Las 7 specs citan entre 2 y 5 archivos, luego el normalizado avanza a saltos de
  0.33 y 0.5. `SPEC-005` y `SPEC-006` citan el **mismo** conjunto y reciben valores **idénticos** en los
  tres ejes: el instrumento no las distingue.
- **Modo de fallo común, y probablemente dominante.** `src/dashboard/app.py` lo citan las **cuatro**
  specs híbridas y **una sola** de las tres caseras. Es un punto de entrada de dashboard con muchos
  imports, así que empuja hacia arriba la colisión **y** el fan-out del brazo híbrido por una razón
  arquitectónica —dónde vive el punto de entrada— y no por limpieza de frontera. **No se recomputó `H3`
  excluyéndolo**: esa sensibilidad no está pre-registrada y elegirla ahora sería una decisión analítica
  tomada con el veredicto a la vista. Queda registrada como ítem obligatorio de pre-registro para
  cualquier réplica.

## Tier B (contexto, no puntúa)

- **`H2` descriptivo.** Las 6 ocurrencias de `[NEEDS CLARIFICATION]` del brazo híbrido (1/2/1/2) están
  **todas dentro de `## Historial`; cero en el cuerpo**: al corte no queda deuda de ambigüedad abierta,
  son el registro de ambigüedades declaradas y ya resueltas. Casero **`N/A`**, nunca `0`. Refuerza el
  motivo de la degradación: lo observable no es cuánta ambigüedad hubo sino cuánta se **documentó y se
  cerró**, y sólo un brazo tiene la convención para documentarla.
- **Costo de redacción.** El híbrido cuesta ~64% más palabras por spec en la mediana (1655 contra 1008),
  con `SPEC-006` outlier en 3827. Confundido con feature, momento y madurez. No puntúa y **no moduló**
  esta decisión.

## Veredicto (b)

**El corpus observacional NO sostiene que el formato híbrido produzca mejor cobertura ni fronteras más
limpias, y en fronteras apunta en sentido contrario.**

- `H1`: **NO CONCLUYENTE.** Tres vías simultáneas. No hay dirección que afirmar.
- `H3`: **NO CONSISTENTE con la hipótesis**, tendencia robusta bajo `LOO` en los tres ejes, con rangos
  solapados en dos de ellos y separación completa en fan-out — pero **sin validación de instrumento** y
  con un **modo de fallo común no descartado** (`app.py`) que puede explicar buena parte de la
  diferencia.

**Lectura admitida (techo descriptivo):** *no consistente con `H3`*; *no concluyente* para `H1`. **MUST
NOT** enunciarse como efecto del formato: en este corpus el formato está confundido con tiempo, madurez,
feature y enforcement.

**Lo que sí queda establecido, y es el aporte más sólido de (b):** la dirección de `H1` **depende de la
convención de conteo**, y el ruido de sesión del instrumento es de 5 a 8 veces la brecha que se pretendía
medir. Cualquier estudio futuro que compare cobertura entre formatos de spec **MUST** medir su piso de
ruido antes de reportar una brecha; sin eso, una diferencia del tamaño de la que buscábamos es
indistinguible de ruido de una sola sesión de extracción.

## Cierre de B-07 — los dos veredictos

MUST NOT fundirse ni promediarse.

| | veredicto | techo |
|---|---|---|
| **(a) regenerabilidad** (cerrado 2026-07-28) | H4 **no sostenida** en F013, F001 **no concluyente**, una sola feature discriminante ⇒ **sin veredicto global** | *no atribuible al formato* (guarda de confusión) |
| **(b) corpus observacional** (cerrado 2026-07-31) | `H1` **NO CONCLUYENTE**; `H3` **no consistente** con la hipótesis | descriptivo |

**No apuntan en sentidos opuestos:** ninguno de los dos sostiene la hipótesis del formato híbrido, y (b)
además apunta en contra en fronteras. Se reporta así, sin resolver por elección.

## Decisión

**Propuesta: AJUSTAR, no adoptar ni descartar.** Peso relativo declarado, como exige la regla de cierre:
**(a) pesa más que (b)**, porque (a) mide el efecto sobre la regenerabilidad —el mecanismo por el que el
formato tendría valor— con un diseño 2×2 controlado, mientras (b) es observacional, retrospectivo, con
`n` de 3 contra 4, sin cegado posible y con el formato confundido con cuatro ejes. `H3` de (b) entra a la
decisión **sólo como señal de que no hay evidencia a favor**, no como evidencia en contra: perdió su
compuerta y tiene un modo de fallo común sin descartar. `H1` **no entra**: no emitió dirección. El costo
de redacción (~64% más palabras) **no moduló** esta decisión y así se declara.

Fundamento: dos criterios independientes, ninguno sostiene la hipótesis, y ninguno la refuta con fuerza
suficiente para descartar el formato. Lo que el conjunto sí sostiene es que **las convenciones adoptadas
de Spec Kit que ya están en uso** (`[NEEDS CLARIFICATION]`, *coverage mapping*, `Cobertura` en el
`[SDD-Check]`) se conservan por su valor de método, no por evidencia de superioridad medida.

> **CONFIRMADA por el Custodio el 2026-07-31.** El veredicto de (b) es del Orquestador y es mecánico; la
> ponderación entre (a) y (b) es del proyecto, y se confirmó explícitamente antes de propagar.

## Propagacion (criterio (b))

Los tres checks, corridos el 2026-07-31 — no de memoria.

- **Check 1** (`grep -n "B-07" SPECS_REGISTRY.md`): 9 coincidencias. Relevantes: línea 87 (tabla SSOT,
  protocolo de medición), líneas 550 y 573 (specs de los dos runbooks), líneas 455 y 478.
- **Check 2** (estructural): SSOT de la hipótesis = `EXPERIMENTO-B7-formato-hibrido.md`. Sus referenciantes
  en la tabla SSOT: `software/PLAN-PRUEBAS.md`, `software/LINEAS-INVESTIGACION.md`, `00-INDEX.md`.
  **MUST sincronizarse el SSOT antes que sus derivados.**
- **Check 3** (grep de deuda declarada, excluyendo `experimentos/`):
  `software/DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md`, `software/COMPARATIVA-SPECKIT-VS-TESTIGO.md`.
- **Contraste contra §Documentos que esperan este resultado** del runbook (SHOULD): el check 3 devuelve
  **2** de los **6** declarados. No aparecen `EXPERIMENTO-B7-formato-hibrido.md`,
  `software/LINEAS-INVESTIGACION.md`, `software/PLAN-PRUEBAS.md` ni `software/ANALISIS-SPEC-KIT.md` —
  los tres primeros porque el check 2 los cubre por estructura, y `ANALISIS-SPEC-KIT.md` porque ya no
  declara la deuda en forma grep-able (en el cierre de (a) había matcheado por un bloque antiguo).
  **La divergencia confirma el motivo por el que los tres checks son obligatorios:** el check 3 aislado
  habría encontrado 2 de 6.

| documento | qué afirmaba | estado nuevo | hecho |
|---|---|---|---|
| `EXPERIMENTO-B7-formato-hibrido.md` **(SSOT)** | criterio (b) enunciado, sin resultado | (b) resuelto: `H1` NO CONCLUYENTE, `H3` no consistente; regla de cierre satisfecha con dos veredictos | **sincronizado** |
| `software/LINEAS-INVESTIGACION.md` §B7 **(SSOT de agenda)** | pregunta 2 (cobertura) **abierta** | respondida como **no concluyente por convención de conteo**, con el piso de ruido como hallazgo transferible | **sincronizado** |
| `software/PLAN-PRUEBAS.md` §B-07 | experimento en ejecución | B-07 **cerrado** con dos veredictos | **sincronizado** |
| `software/COMPARATIVA-SPECKIT-VS-TESTIGO.md` | deuda abierta por el corpus observacional | deuda **cerrada**; se anota con bloque `[SDD-Check]` nuevo, sin reescribir los anteriores | **sincronizado** |
| `software/DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` | §9.3 enumera el corpus entre lo pendiente de medir | corpus medido; la decisión de fondo (Ajustar) se alinea con §9.3 | **sincronizado** |
| `software/ANALISIS-SPEC-KIT.md` | hueco C1 (cobertura) sin evidencia | `H1` no emitió dirección: el hueco C1 **sigue abierto**, ahora con motivo medido | **sincronizado** |
| `../agenda/BACKLOG-INVESTIGACION.md` | 6 ítems en prioridad alta | +7: **medir el piso de ruido del instrumento antes de reportar una brecha** | **sincronizado** |
| `experimentos/PREREG-B7.md` | pre-registro sellado | **intocable por diseño** | **no aplica** — sellado |
| `SPECS_REGISTRY.md` | referencia resultados sin copiarlos | ninguna afirmación de estado vencida; las specs de los dos runbooks siguen correctas | **no aplica** |
