# Prueba de Regenerabilidad 2×2 — Runbook (B-07)

## Propósito

Runbook **ejecutable paso a paso** de la métrica PRIMARIA de `EXPERIMENTO-B7-formato-hibrido.md`: **regenerabilidad** (reconstruir el código desde la spec sola). Diseño **2×2 balanceado por traducción** sobre dos features (SPEC-001 casero-auténtica, SPEC-013 híbrida-auténtica), con celdas traducidas cruzadas.

Este doc **no redefine** las métricas ni la hipótesis: esas viven en `EXPERIMENTO-B7-formato-hibrido.md` (SSOT). Aquí solo se **operacionaliza** el "cómo correrlo". La sonda forward de SPEC-009 queda **excluida** de esta versión (fase posterior).

> **Estado:** diseño pre-ejecución. Los cuatro inputs bloqueantes quedaron **RESUELTOS (2026-07-10)** (ver §Inputs bloqueantes). Pendiente: correr Fase 0 (pre-registro) y Fase 1 (armado de ambientes).

---

## Glosario de nombres

Código operativo corto (se usa en el cuerpo) + nombre descriptivo formal.

### Features
- `F001` — **"Modo simple (un caso por pantalla)"**. SPEC-001; origen **casero**; implementada pre-git (~2026-05-22).
- `F013` — **"Selección de adaptador de cliente para plataformas alternativas"**. SPEC-013; origen **híbrido**; implementada 2026-07-03 (commits `9f89369`..`d12e6f3`).

### Formatos
- `CAS` — **casero**: anatomía pre-SPEC-004. **[Precisión 2026-07-29]** "congelada 2026-05-24" es inexacto: las specs casero se editaron después de esa fecha (detalle en `PRUEBA-OBSERVACIONAL-B7.md` §Reglas criticas 7). **No cambia ningún resultado de esta prueba**: la unidad de inferencia es el contraste **intra-feature**, y las dos celdas de `F001` parten del mismo texto (la híbrida es su traducción), luego ambas heredan idéntica evolución. Se corrige la afirmación, no el veredicto.
- `HIB` — **híbrido**: anatomía Spec Kit — User Story priorizada + `FR-NNN MUST` + `SC-NNN` medibles + Given/When/Then + coverage mapping.

### Celdas del 2×2 (Feature × Formato)
- `F001-CAS` — **"Modo simple, spec casero auténtica"** (SPEC-001 congelada). *Existe.*
- `F001-HIB` — **"Modo simple, spec híbrida traducida"**. *A construir (Fase 0).*
- `F013-CAS` — **"Adaptador, spec casero traducida"**. *A construir (Fase 0).*
- `F013-HIB` — **"Adaptador, spec híbrida auténtica"** (SPEC-013 compacta `d12e6f3`). *Existe.*

### Specs (artefactos)
- `SPEC-F001-CAS`, `SPEC-F013-HIB` — **auténticas**, tomadas de `ENV-REF`.
- `SPEC-F001-HIB`, `SPEC-F013-CAS` — **traducidas** en Fase 0 (spec→spec).

### Fronteras in-spec (contratos humanos fijos = único contexto del modelo además de la spec)
- `FRONTERA-F013` — interfaz del puerto `AgentClient`, `CredentialProvider`/`TokenProvider`, punto de wiring de composition roots, config `AGENT_CLIENT_TYPE`.
- `FRONTERA-F001` — **RESUELTO (2026-07-10)**, extraída de la propia declaración `Depende de:` de SPEC-001 + su referencia a schema externo:
  1. **SPEC-000-naming** — regla de nomenclatura agnóstica (nombres no pueden referenciar proveedor/framework UI/formato de serialización/protocolo de auth) + lista canónica de tokens prohibidos + tabla de excepciones (config externa, docs, métodos que implementan contratos de librería externa como `.json()`, tokens de formato en tests).
  2. **SPEC-000-bootstrap** — estructura de directorios (`src/domain/`, `src/adapters/`, `src/build/`, `src/dashboard/`, `specs/`, `docs/`, `tests/unit/`, `tests/integration/`) y tooling bloqueante en hook de commit (`ruff`, `mypy --strict` sobre `src/`, linter de naming, `import-linter` con regla `domain/` no importa de `adapters/`/`dashboard/`).
  3. **`schemas/FI_Orquestador_Input.schema.json`** — schema externo del agente; SPEC-001 lo referencia para el campo `datos_requeridos.otros.message` ↔ `datos_otros_mensaje` de `TestCase`.

### Baselines
- `BASE-F001` — **"Baseline por sustracción"**: **rama del repo original** (mismo clon que `BASE-F013`) desde su **commit más antiguo**; sobre la rama se remueven F001 **y todo lo agregado con posterioridad a F001** en uno o más commits, dejando la base común pre-F001 (infra agnóstica + `FRONTERA-F001`). La sustracción se decide **a mano** (F001 es pre-git) y queda **materializada como commits de la rama**. Misma **estrategia de partida** que `BASE-F013`. Aislamiento **por instrumentación** (R2), igual que `BASE-F013`.
- `BASE-F013` — **"Baseline por sustracción"**: **rama del repo original** que parte del proyecto completo **a hoy** (`ENV-REF` HEAD, `8bff08c`) y remueve la **huella de F013** (código, tests, `specs/SPEC-013`, y su **derrame fuera de frontera** — ver §1.3), dejando el proyecto **como si F013 nunca se hubiera hecho**. Aislamiento **por instrumentación** (R2). Misma **estrategia de partida** que `BASE-F001` (sustracción desde el proyecto completo por contrafáctico "la feature nunca existió"); **simétrico**. *(Cambio 2026-07-12: se abandona el checkout del padre de `9f89369` (`9fd3954`) porque no entregaba "el repo entero menos F013" sino un rebobinado de 19 commits con la spec de F013 a medio escribir — violaba §0.7 "ambiente libre de spec del feature" y §Aislamiento "sustracción desde el proyecto completo". Re-iteración de Fase 1 bajo §1.5.e: `b7/base-f013-v2`, re-clonar; sello `b7/prereg-v1` intacto.)*

### Workspaces (clon fresco, 1 por celda)
- De `BASE-F001`: `WS-F001-CAS`, `WS-F001-HIB`.
- De `BASE-F013`: `WS-F013-CAS`, `WS-F013-HIB`.

### Runs ciegos
- `RUN-A` / `RUN-B` / `RUN-C` / `RUN-D` — etiquetas neutras. El mapa `RUN→celda` se sella en `SELLO-CIEGO` (rol Custodio) y solo se revela en Fase 4.

### Instrumentos de test
- `TESTS-F001`, `TESTS-F013` — suites de aceptación **levantadas de `ENV-REF`**, aplicadas **post-regeneración** (nunca antes).

### Salidas
- `OUT-<RUN>` — código regenerado por cada run.
- `SCORE-<RUN>` — planilla R1-R4 por run.
- `RESULTADO-EXPERIMENTO-B7.md` — consolidación final (usa `../templates/RESULTADO-EXPERIMENTO.md`).

### Ambientes (ubicaciones físicas)
- `ENV-REF` (**X**) — proyecto completo, **read-only**. Fuente de specs auténticas, fronteras y tests.
- `ENV-F001` (**Y**) — aloja `BASE-F001` y sus 2 workspaces.
- `ENV-F013` (**Z**) — aloja `BASE-F013` y sus 2 workspaces.

### Roles
- `Traductor` — escribe `SPEC-F001-HIB` y `SPEC-F013-CAS` **spec→spec, sin leer `src/`**. **SHOULD ≠ `Regenerador`** (si traduce quien luego regenera, tiende a regenerar hacia su propia redacción). **No** puntúa.
- `Reconstructor` — modelo **independiente** (distinto del `Regenerador` y de su sesión) que produce el corte inicial de **ambos baselines por sustracción**: para `BASE-F001` parte del commit más antiguo y remueve F001 + todo lo posterior; para `BASE-F013` parte del proyecto a hoy y remueve la **huella de F013** (§1.3). Su `MODELO`+versión y `PROMPT` se pre-registran (0.1); su salida se congela como tag y pasa el gate objetivo de §1.5.c. **SHOULD ≠ `Regenerador`**; **MAY** coincidir con el `Traductor` (el sesgo de base cancela intra-feature, ver §4.4). **No** regenera ni puntúa. *(Cambio 2026-07-12: antes solo aplicaba a `BASE-F001`; `BASE-F013` dejó de ser checkout git para volverse sustracción simétrica.)*
- `Regenerador` — el `MODELO` fijo bajo `HARNESS` fijo. No ve tests ni código previo. En las 4 celdas es el **mismo modelo** en **sesiones frescas independientes** (memoria cero entre runs).
- `Puntuador` — puntúa R1-R4 a ciegas sobre `RUN-A..D`. **SHOULD ≠ `Regenerador`** (nadie puntúa su propia salida). No conoce el `SELLO-CIEGO` (§3.5: tampoco `prereg` ni el manifiesto).
- `Custodio` — guarda `SELLO-CIEGO`, las `FRONTERA-*` y el pre-registro (`b7/prereg-vN`). Único que resuelve `spec_hash`→spec→formato; controla el acceso al `run-manifest.yaml`.

### Constantes pre-registradas
- `MODELO` + versión (**bloqueante**); seed/temperatura si el harness los expone.
- `HARNESS` + versión.
- `PROMPT` — plantilla de regeneración, congelada e idéntica entre celdas.
- `UMBRAL` — sobrecosto de redacción: **RESUELTO (2026-07-10)** — sin corte numérico, evaluación cualitativa (tiempo/extensión/iteraciones observados, sin umbral binario).

### Versionado git (nombres de rama y tag)
Un solo clon del repo del testigo aloja todo lo versionado:
- **Ramas de baseline (persistentes):** `b7/base-f001`, `b7/base-f013` — registro iterable del ambiente (§1.5).
- **Tags de baseline (congelados):** `b7/base-f001-vN`, `b7/base-f013-vN` — punto único de clonado de los workspaces.
- **Tag de pre-registro:** `b7/prereg-vN` — agrupa las 4 specs (con hash + procedencia), fronteras, constantes y `SELLO-CIEGO` (§0.7).
- **Ramas de run (ciegas):** `b7/run-a`..`b7/run-d` — salida `OUT-<RUN>` por celda, partiendo del tag de baseline; el mapa `run→celda` vive en `SELLO-CIEGO` (§2.4).

---

## Diseño 2×2

|  | `CAS` (casero) | `HIB` (híbrido) |
|---|---|---|
| **F001** | `F001-CAS` — auténtica | `F001-HIB` — traducida |
| **F013** | `F013-CAS` — traducida | `F013-HIB` — auténtica |

- **Estimando principal (efecto-formato):** media(`F001-HIB`, `F013-HIB`) − media(`F001-CAS`, `F013-CAS`).
- **Lectura por-feature:** contraste dentro de `F001` y dentro de `F013`, para ver si el signo se sostiene.
- **Por qué balanceado (auténtico en diagonal, traducido fuera):** cada formato tiene 1 celda auténtica + 1 traducida → el sesgo de traducción se reparte, no carga sobre un brazo. El contraste **intra-feature** es limpio porque las dos celdas de un feature comparten `BASE-*` y `FRONTERA-*`; **solo cambia el formato de la spec**.

---

## Protocolo paso a paso

**Orden de ejecución (MUST secuencial entre fases):** Fase 0 → Fase 1 → Fase 2 → Fase 3 → Fase 4. Las **4 specs** (auténticas + traducidas) se crean y sellan **en Fase 0** (0.4 + 0.7), antes de armar los baselines; no dependen de los ambientes. Fase 1 solo consume la spec ya sellada al clonar los workspaces (1.4).

### FASE 0 — Pre-registro (congelar antes de tocar nada)

MUST — nada de esta fase puede cambiarse una vez iniciada la Fase 1.

- **0.1** Fijar constantes `MODELO`+versión, `HARNESS`+versión, `PROMPT`, seed/temp. *(bloqueante: `MODELO`)*. Fijar también el **`MODELO-RECONSTRUCTOR`+versión y su `PROMPT`** (rol `Reconstructor`, §1.2) — SHOULD distinto del `MODELO` para no compartir sesgo con el `Regenerador`.
- **0.2** Fijar `UMBRAL` de sobrecosto. *(bloqueante)*
- **0.3** Extraer y pre-registrar `FRONTERA-F013` (de SPEC-013 + código en `ENV-REF`) y `FRONTERA-F001` *(bloqueante: requiere abrir SPEC-001)*. Cada frontera lista los contratos explícitos que entran como contexto — **nunca** código regenerado.
- **0.4** Traducir (rol `Traductor`, **spec→spec, sin `src/`**):
  - `SPEC-F001-HIB` desde `SPEC-F001-CAS`, con anatomía híbrida de la era SPEC-004/008.
  - `SPEC-F013-CAS` desde `SPEC-F013-HIB`, con convenciones casero **congeladas al 2026-05-24**.
- **0.5** Completar el **Checklist de pre-registro** de `EXPERIMENTO-B7-formato-hibrido.md` (todas las casillas).
- **0.6** Generar `SELLO-CIEGO`: asignar `RUN-A..D` ↔ celdas al azar; sellar con el `Custodio`.
- **0.7** **Versionar las specs de prueba (tag `b7/prereg-vN`).** El `Custodio` sella el pre-registro como un tag, **separado de las ramas de baseline** (el ambiente queda libre de spec del feature):
  - Agrupa las **4 specs** + las 2 `FRONTERA-*` + constantes (`MODELO`, `HARNESS`, `PROMPT`, `UMBRAL`) + `SELLO-CIEGO`.
  - **Procedencia por spec:**
    - Auténticas (`SPEC-F001-CAS`, `SPEC-F013-HIB`): registrar el **commit/ref de `ENV-REF`** de donde se levantan; snapshotear la copia dentro del pre-registro para que sea autocontenido.
    - Traducidas (`SPEC-F001-HIB`, `SPEC-F013-CAS`): commit del `Traductor`, registrando la **spec origen** de cada una.
  - **Hash por spec:** listar el hash (blob sha de git / sha256) de las 4. MUST — congeladas al iniciar Fase 1.
  - **Re-versionado:** cambiar una spec cambia un **input del experimento** → reabrir el sello y emitir `b7/prereg-vN+1` (más pesado que el re-tag de baseline de §1.5.e); válido solo si aún no arrancó ninguna `RUN`.

*Salida de fase:* pre-registro inmutable sellado en `b7/prereg-vN` = 4 specs (2 auténticas + 2 traducidas, con hash y procedencia), 2 fronteras, constantes, sello.

### FASE 1 — Preparación de ambientes

- **1.1** `ENV-REF` (X): copia **read-only** del proyecto completo del testigo. Fuente de `SPEC-*` auténticas, `FRONTERA-*` y `TESTS-*`.
- **1.2** `BASE-F001` (sustracción por modelo independiente): en el mismo clon del repo del testigo (§1.3), crear la rama `b7/base-f001` desde el **commit más antiguo**. El **`Reconstructor`** (modelo independiente pre-registrado, §0.1) **remueve F001 + todo lo agregado con posterioridad a F001**, en commits sobre la rama, dejando la base común pre-F001 (infra agnóstica + `FRONTERA-F001`). *Por qué un modelo y no a mano:* no existe estado histórico pre-F001 (F001 es pre-git), así que la base es una **reconstrucción**; delegarla a un modelo independiente reemplaza el sesgo de curador humano por un procedimiento pre-registrado y reproducible. Verificar que en disco quedan solo infraestructura pre-F001 y `FRONTERA-F001`, que el resto resuelve; **congelar como tag** (§1.5).
- **1.3** `BASE-F013` (sustracción por modelo independiente): en el mismo clon del repo del testigo, crear la rama `b7/base-f013` desde **hoy** (`ENV-REF` HEAD, `8bff08c`). El **`Reconstructor`** (§0.1) remueve, en commits sobre la rama, la **huella de F013**, dejando el proyecto **como si F013 nunca se hubiera hecho**. *Por qué a hoy y no el padre de `9f89369`:* el checkout de `9fd3954` no era "el repo entero menos F013" sino un rebobinado de 19 commits (docs/constitución/registry viejos + `specs/SPEC-013` a medio escribir, 1 US) → violaba §0.7 y §Aislamiento. Partir de hoy y sustraer aísla F013 contra el ambiente **actual**, que es lo que la métrica quiere medir.

  **Definición operativa de "huella de F013"** (lo que MUST removerse):
  - **Código:** `SyncHttpAgentClient`, `AgentClientFactory`, `StaticCredentialProvider`, y las adiciones de F013 a `PlatformConfig` (`CLIENT_TYPE_SYNC_HTTP`, `_REQUIRED_VARS_BY_CLIENT`, dispatch por `AGENT_CLIENT_TYPE`) + wiring. *Nota:* `PlatformConfig` en sí **se conserva** (infra agnóstica pre-F013, solo `remote_async`); no es señal de ausencia.
  - **Tests:** `TESTS-F013` (mapeo en `PREREG-B7.md §6`).
  - **Spec:** `specs/SPEC-013-client-adapter-selection.md` se remueve **por completo** (§0.7: el ambiente queda libre de la spec del feature; la spec vive solo en la `.b7/SPEC.md` inyectada por celda). El baseline queda así **agnóstico al formato** (CAS/HIB) por construcción.
  - **Derrame fuera de frontera — US2 (clave):** F013-US2 (trazabilidad de `endpoint_url`) **escapa a la persistencia**: agregó el campo `endpoint_url` a `SuiteResult` en [[SPEC-005-run-persistence]], la columna homónima en [[SPEC-006-batch-suite]], y su código/tests. En el checkout previo (`9fd3954`, ya descartado como baseline) esas specs estaban **limpias de F013** (0 refs); a hoy cargan 5 y 7 menciones respectivamente — evidencia de que el `endpoint_url` es huella de F013, no evolución neutral. MUST removerse ese delta (specs + código + tests) — de lo contrario el baseline pre-contamina US2 y sesga la regenerabilidad al alza. La spec input **mantiene 3 US** (US2 incluida): el `Regenerador` debe regenerar también ese esquema, guiado por la spec.
  - **Referencias colgadas (scrub) — huella "clase A":** docs que se conservan pero **apuntan** a SPEC-013 o a clases de F013: `SPEC-002` (línea "adaptadores alternativos… viven en SPEC-013"), `SPEC-003`, `docs/ARCHITECTURE.md`, `docs/AGENT-INVOCATION.md`, `docs/IDEAS.md`, `docs/SPEC-FORMAT.md` (re-apuntar el ejemplo de formato compacto — hoy es SPEC-013), `SPECS_REGISTRY.md` (quitar la fila SPEC-013), `.env.example` (quitar el bloque `AGENT_CLIENT_TYPE`/`ALT_CLIENT_*`), `historial/sdd.md` (podar las entradas de F013). Estos docs **se traen a hoy** (evolución neutral) y se les quita solo el puntero a F013.

  Todo lo **no-huella** (constitución, pipelines, infra, requirements, naming, specs 001-004/008/010-012) se conserva **a hoy** (`8bff08c`). Verificar ausencia (las cuatro señales de código de arriba) + ausencia de `endpoint_url`/US2 + ausencia de `specs/SPEC-013` y de referencias colgadas a SPEC-013 + que el resto resuelve; **congelar como tag** (§1.5).
- **1.4** Clonar cada baseline **×2** desde su **tag congelado** (§1.5) → `WS-F001-CAS`, `WS-F001-HIB` (de `b7/base-f001-vN`); `WS-F013-CAS`, `WS-F013-HIB` (de `b7/base-f013-vN`). Los 4 workspaces MUST derivar del **mismo tag** por feature → idénticos por construcción.
- **1.5** **Versionado reproducible del baseline (rama + tag) + lazo de mejora.** Cada baseline se versiona en git para poder **recrearlo a demanda** y **corregirlo hasta que esté correcto para las pruebas** antes de sellar:
  - **1.5.a — Un clon del repo original para ambos baselines.** Ambas ramas viven en el **mismo clon del repo del testigo** (§1.3). Cada baseline es una **rama del original**: la sustracción se expresa como historia de git en ese repo.
  - **1.5.b — Rama de armado (persistente).** Crear la rama de trabajo, que **persiste** durante toda la Fase 1:
    - `b7/base-f013` desde **hoy** (`ENV-REF` HEAD, `8bff08c`); sobre la rama, los commits del `Reconstructor` (§1.3) que remueven la **huella de F013** hasta dejar el proyecto "como si F013 nunca se hubiera hecho".
    - `b7/base-f001` desde el **commit más antiguo** del repo; sobre la rama, los commits del `Reconstructor` (§1.2) que remueven F001 + todo lo posterior hasta dejar la base pre-F001.
    - Toda corrección del baseline vive en su rama; la rama es el registro iterable del ambiente.
  - **1.5.c — Lazo de mejora (iterar hasta correcto, gate objetivo).** Iterar en la rama hasta que el baseline **resuelva**: para `BASE-F001`, base pre-F001 que compila/resuelve con `FRONTERA-F001` completa; para `BASE-F013`, proyecto-a-hoy-menos-huella-F013 que resuelve con la verificación de ausencia de §1.3 (cuatro señales de código + sin `endpoint_url`/US2 + sin `specs/SPEC-013` + sin referencias colgadas a SPEC-013). Criterio de "correcto" = **el baseline compila/resuelve y la frontera está completa** — es un **gate objetivo** (independiente del `Reconstructor`), así que **ambas** reconstrucciones se validan por criterio, no por confianza en el modelo. La rama contiene el proyecto **menos el feature y su huella** (código, tests, spec, derrame fuera de frontera), que es la ausencia que el experimento mide.
  - **1.5.d — Congelar como tag.** Cuando el baseline queda correcto, etiquetar el commit: `b7/base-f001-vN`, `b7/base-f013-vN` (empezar en `v1`). El tag es el **punto único de clonado** de §1.4 y el artefacto recreable a demanda (`git checkout b7/base-f001-v1` reconstruye el ambiente bit a bit).
  - **1.5.e — Re-congelar (versionado).** MAY volver a la rama, corregir y emitir `vN+1` **solo si aún no comenzó ninguna `RUN` de Fase 2**. Al re-taggear MUST re-clonar los 4 workspaces desde el nuevo tag (§1.4) para mantener la identidad. Una vez iniciada Fase 2, el tag activo queda **inmutable** y todo hallazgo posterior se registra como reserva, no como re-corte.
  - **1.5.f — Pre-registrar.** El `Custodio` anota en el pre-registro (Fase 0) el `MODELO`/`HARNESS` y, al cerrar Fase 1, el **hash del tag** `vN` de cada baseline realmente usado, para trazabilidad.

*Salida:* 4 workspaces frescos, **sin tests del feature y sin el código del feature**, cada uno derivado de un **tag de baseline congelado** (`b7/base-f001-vN`, `b7/base-f013-vN`) recreable a demanda.

### FASE 2 — Regeneración (4 runs independientes, sesión fresca; paralelizables, nunca encadenados)

**Precondición (MUST, antes de la 1ª RUN real, no-retorno):** hacer un **dry-run** en un ws descartable (o en `F001`) que confirme que una sesión del `MODELO` (`Regenerador`) **navega la gobernanza sin trabarse** (declara `.sdd/current-spec`, registra la spec, edita la spec, y el gate `sdd_gate.py` la deja implementar `src/`), y que el **transcript resultante alimenta `r2_extract.py`** correctamente. Si el modelo se traba de verdad en el gate, evaluar asistencia mínima (p. ej. pre-registrar una fila neutra) **antes** de la 1ª RUN. El dry-run se descarta (no cuenta como RUN).

Para cada `WS-<celda>` (referido por su etiqueta ciega `RUN-x`):

- **2.1** **Preparación de la celda (lanzador `custodio/regenerar.sh`, scriptado — el orquestador no lee la spec):** copiar `.b7/SPEC.md` a su **ruta natural** `specs/SPEC-0NN-<nombre>.md` y marcarla **git-excluida** (`.git/info/exclude`), para que el contexto de trabajo sea natural pero el **formato no quede en el commit `OUT`** (→ `Puntuador` ciego). Ensamblar el `PROMPT` fijo (PREREG §2) apuntando a esa ruta.
- **2.1-bis** **Consistencia de entorno entre celdas (celdas en fechas distintas MAY):** las 4 celdas son independientes y sin encadenamiento (baseline = tag congelado, spec/PROMPT fijos), así que **pueden correrse en fechas distintas sin contaminación cruzada**. El único confound es la **deriva del entorno de ejecución** (bump silencioso del alias del modelo, o CLI actualizada) entre corridas. El lanzador **fija la referencia en la 1ª celda** (`logs/ENTORNO-REF.yaml`: modelo + versión de CLI) y en las siguientes **compara y aborta pidiendo confirmación** si algo cambió. SHOULD correr las 4 en la misma ventana; si van en fechas distintas, MUST verificar que los 4 `run-manifest.yaml` coincidan en `model` **y** `harness` antes de puntuar, o declarar la desviación como **reserva** en el RESULTADO.
- **2.2** Sesión **limpia** del `MODELO` bajo `HARNESS`, con **acceso pleno al proyecto** (el aislamiento es **por medición**, no por construcción — §Aislamiento). El modelo implementa la spec **siguiendo el proceso y las convenciones SDD del propio repositorio** (incluida su **gobernanza activa**: el hook `sdd_gate.py` bloquea `src/` sin spec declarada+registrada+editada → el modelo declara/registra la spec y luego implementa; el gate es **auto-correctivo** y su navegación se mide en **R5**). **No** se pre-declara la spec (para que R5 sea real). **No usa guías externas** ni ve `TESTS-<feature>` (removidos del baseline, §1.3); MAY escribir sus propios tests (proceso SDD), que **no** son el instrumento de R1.
- **2.3** El modelo regenera el **delta del feature** → `OUT-RUN-x`. Se captura el **transcript** (log de `Read`/`Grep`/`Glob` + tool-uses) para alimentar **R2** (§PREREG 4) y **R5** (§PREREG 5.1).
- **2.4** Versionar la salida en una **rama de run ciega**: partir del **tag de baseline** correspondiente y commitear **solo `src/`** (`git add src/`) como `OUT-RUN-x` en `b7/run-<a|b|c|d>` (etiqueta neutra). **MUST NOT** commitear la spec copiada, `.sdd/current-spec`, cambios a `SPECS_REGISTRY.md` ni los tests del modelo — **revelan formato**; quedan en el working tree para R5. Agregar en la raíz un `run-manifest.yaml` (grep-able). **Eje ciego = formato** (`CAS`/`HIB`): el feature es inocultable, así que el manifiesto MAY revelar feature/baseline y MUST NOT permitir inferir el **formato** — el `spec_hash` es opaco sin `b7/prereg` y el `Puntuador` no lo tiene.

  ```yaml
  run: RUN-A                       # etiqueta ciega (sin celda ni formato)
  feature: F001                    # visible; NO revela formato
  baseline:
    tag: b7/base-f001-v1
    commit: <sha>
  prereg:
    tag: b7/prereg-v1
    spec_hash: <sha256>            # opaco sin prereg; resuelve solo el Custodio
  regenerador:
    modelo: <MODELO+versión>
    harness: <HARNESS+versión>
    prompt_hash: <sha del PROMPT congelado>
    seed: <valor o null>
  ejecucion:
    timestamp: <ISO-8601>
    R2_lecturas_fuera_frontera: <n o ref al log>
    R3_iteraciones: <n>
    esfuerzo: <tiempo / notas para UMBRAL>
  ```

  **Reproducibilidad declarada:** el manifiesto reconstruye el **ambiente + los inputs** bit a bit; la **salida del modelo NO es reproducible** (no-determinismo del harness) — se preserva versionando `OUT-RUN-x`, no re-generándolo.
- **2.5** Registrar en caliente:
  - **R2** — lecturas fuera de frontera (log de archivos abiertos; **crítico en `BASE-F013`**, donde el repo entero está en disco).
  - Tiempo/esfuerzo (para evaluar `UMBRAL`).
  - *(R3 NO se mide aquí — se mide en Fase 3-bis, lazo post-R1; ver abajo.)*
- **2.6** **Ventana de prueba manual (opcional, cualitativa).** Apenas commiteada la celda (`src/` en `b7/run-x`) se abre una ventana para que el **Custodio** ejercite a mano la funcionalidad regenerada (dashboard `streamlit run src/dashboard/app.py`, o CLI `python -m src.runner --in <casos> --out runs/`), probando el feature de esa celda: **F013** = selección de adaptador de cliente; **F001** = carga de un caso por pantalla. Es un **sanity check cualitativo**, NO el instrumento de R1 (ese es la suite oculta, §3.1–3.2). Invariantes:
  - **MUST NOT** commitear nada de la prueba (`git add`/`commit` en `ws/run-x`) ni tocar `src/` del OUT medido — el `OUT-RUN-x` es un **commit inmutable**; la medición re-hace `checkout` de ese commit, así que el working tree puede ensuciarse sin afectar el resultado. Deps en `.venv/` efímero + `runs/` (git-excluidos).
  - **No rompe la ceguera**: el Custodio ya tiene el `SELLO-CIEGO`; el eje ciego (formato del documento spec) no se filtra por ejercitar el *runtime*. El **Puntuador** sigue entrando limpio.
  - **Si revela un bug**: MUST NOT parchearlo a mano en el WS. Si lo captura la suite oculta → entra por R1 + reparación R3 (Fase 3-bis). Si la suite no lo cubre → observación cualitativa en el RESULTADO (posible motivo para ampliar la suite en un experimento futuro).

- **2.7** **Manejo de corridas nulas (VOID) — [enmienda 2026-07-28, post-hoc].** *Regla añadida durante la Fase 2 tras observar el 1er intento de `run-d` (F001), que terminó `success` pero con 0 cambios en `src/`. NO estaba pre-registrada; se documenta aquí como enmienda fechada del runbook (NO en `PREREG-B7.md`, que está sellado en `b7/prereg-v1`). Detalle de ejecución en `experimentosdd-b7/BITACORA.md`.*
  - **Definición (trigger OBJETIVO, no por resultado):** una corrida es **VOID** si y solo si (a) produce **0 cambios en `src/`** (0 `Edit`/`Write` sobre `src/` en el transcript) **Y** (b) la sesión termina emitiendo una **pregunta de aprobación** al humano (en headless `-p` nadie responde → la sesión cierra sin regenerar). Causa conocida: **halt-on-permission** — el modelo trata el montaje del entorno (`python3 -m venv`) como prerequisito bloqueante, la política de permisos lo deniega (Bash bloqueado por diseño, §coherencia R1) y **algunas veces** aborta pidiendo aprobación en vez de degradar a "escribir código sin verificar" (comportamiento estocástico del harness).
  - **Por qué se anula (no es dato):** R1 mide % de spec satisfecha por **código generado**; un VOID **no generó código** → es una **no-corrida** (aborto de infraestructura), no una regeneración de baja calidad. La causa es el harness, no el formato ni la spec; puntuarla mediría el harness y rompería la simetría con las celdas que sí produjeron `src/`. **MUST NOT** descartarse por score bajo — solo por el trigger objetivo de arriba (un VOID no es un intento malo, es un no-intento).
  - **Procedimiento:** MUST — (1) **archivar** el transcript nulo como `logs/OUT-RUN-<x>.VOID-<n>.transcript.jsonl` (evidencia, NO borrar); (2) `git -C ws/run-<x> reset --hard <baseline>` (revierte el commit nulo, `.b7/` intacto); (3) **re-correr idéntico** — mismo `PROMPT`, mismos permisos, mismo modelo/harness (no rompe el prompt fijo ni la simetría). Cap **N=3** intentos VOID por celda. Todos los transcripts VOID se conservan y se listan en el RESULTADO.
  - **Umbral de alarma:** si la **tasa de VOID** es alta (varias celdas o >1 intento reiterado), el régimen de permisos —no el formato— estaría dominando la varianza → **amenaza a la comparabilidad del 2×2**; MUST — detenerse y re-evaluar el régimen antes de puntuar, declarándolo como reserva.

MUST — NO mostrar `TESTS-*` al modelo en esta fase (si los ve, codea hacia el test). La salida de esta fase es la que fija **R1 one-shot**.

*Salida:* 4 `OUT-RUN-x` versionados en `b7/run-a..d` (ciegos) + logs (incl. transcripts `VOID-n` archivados si los hubo).

### FASE 3 — Medición (a ciegas)

- **3.1** Traer `TESTS-<feature>` de `ENV-REF` a cada `WS` y correr contra `OUT-RUN-x`.
- **3.2** **R1 (one-shot)** = % de `SC`/`FR` satisfechos por `OUT-RUN-x` **tal cual salió de Fase 2**, antes de cualquier reparación; los tests son la automatización que los verifica. Si hay mismatch de nombres por API: reconciliar con un **shim delgado pre-registrado** y contarlo como **R2/R4**, **no** como fallo de R1.
- **3.2-bis** **Definición operacional de R1 — [enmienda 2026-07-28, post-hoc].** *Decidida al ejecutar 3.1–3.2, ante tres huecos del texto original: (i) el "shim delgado pre-registrado" nunca se pre-registró (no había forma de saber qué mismatch aparecería); (ii) no estaba fijado el denominador; (iii) no estaba definido el aislamiento del clon de medición. NO redefine la métrica de PREREG (sellada en `b7/prereg-v1`); la **operacionaliza**. Implementada en `logs/r1_run.py`. Detalle en `experimentosdd-b7/BITACORA.md`.*
  - **Aislamiento del clon de medición (MUST):** correr el instrumento sobre un **clon fresco de la rama ciega `b7/run-x`**, NO sobre `ws/run-x`. El working tree de Fase 2 contiene los tests que escribió el propio modelo, la spec inyectada (`.b7/`) y estado de sesión; la rama tiene solo `src/` + manifiesto = la condición de medición pretendida. Ídem baselines (desde sus tags).
  - **Denominador canónico (MUST):** el conjunto de tests se fija corriendo el instrumento sobre `ENV-REF` (HEAD), donde el delta existe y **MUST salir 100% verde** — si no, el instrumento es inválido. Un test **no colectado** en una celda (módulo ausente o import roto) cuenta **`ausente` = fallo**, no se descuenta del total. Sin esta regla el denominador sería variable y una celda que no implementó nada saldría **beneficiada** (un archivo entero colapsa a un solo error de colección en vez de N tests rojos).
  - **Validación del instrumento (MUST, antes de puntuar):** correr las suites contra **ambos baselines**. La parte de *aceptación del delta* MUST dar **0%** (si pasa sin el delta, no mide la regeneración) y la parte de *regresión de la base* MUST dar **100%**. En suites mixtas (`test_platform_config.py`, PREREG §6) esto separa mecánicamente qué tests son aceptación y cuáles regresión.
  - **Criterio de shim admisible (reemplaza al "pre-registrado" inexistente):** un shim MAY reconciliar un mismatch **si y solo si** existe en el `OUT` un elemento con la **misma semántica que el test verifica** y distinta nomenclatura/procedencia; el shim MUST ser un **alias sin lógica** (si el comportamiento no estuviera, los tests siguen rojos), MUST vivir versionado en `logs/shims/<RUN>.conftest.py` y MUST documentar en su docstring qué reconcilia y por qué es admisible. MUST NOT shimearse una **ausencia** (el elemento no existe bajo ningún nombre) ni una diferencia de **tipo, invariante o comportamiento**.
  - **Reporte en dos variantes (MUST):** `R1-estricta` (sin shims) y `R1-con-shim` (sensibilidad), análogo a crudo/refinado en R2 (§3.4-bis). **El criterio primario se evalúa sobre la estricta.** Razón: no se puede saber, sin romper el ciego, si la spec de la celda **nombraba** el elemento en cuestión; si un formato lo nombraba y el otro no, el shim **borraría efecto del tratamiento**. La comparación de ambas variantes se interpreta en Fase 4.
  - **Granularidad `test` ≠ `SC`/`FR`:** un test MAY verificar varios comportamientos y aborta en la primera aserción roja (observado: `test_construye_caso_valido` valida 4 cosas, falla en la 4ª). El % de tests es la **cifra mecánica**; el % de `SC`/`FR` requiere un **mapeo test→SC/FR único por feature** (idéntico en sus dos celdas → neutral al formato) y se construye en Fase 4, separado de la medición.
- **3.2-ter** **Mapeo test→SC/FR — [enmienda 2026-07-28, post-hoc].** *Decidida al construir el mapeo que §3.2-bis difirió a Fase 4. Implementada en `logs/mapeo_f013.py` + `logs/r1_por_requisito.py`.*
  - **F001: el mapeo NO es construible.** `SPEC-001` **no define IDs de requisito en ninguna versión** (ni la congelada `af7109b` ni HEAD): sus criterios de aceptación son bullets en prosa y varios no son verificables por el instrumento (`mypy --strict` verde, `ruff` verde, cobertura 100%). El instrumento `tests/unit/test_test_case.py` no cita ningún ID. MUST — R1 de F001 se reporta en **granularidad de test**; MUST NOT fabricarse un espacio de IDs que el corpus nunca tuvo. No perjudica la señal primaria: el contraste es **intra-feature** y ambas celdas comparten instrumento. Es una asimetría real entre los dos formatos-auténticos, no un defecto de medición — y es en sí un dato sobre el formato casero de esa época.
  - **F013: el mapeo se construye a ciegas y se congela.** MUST — el paquete se arma **sólo con `ENV-REF`** (`SPEC-013` auténtica `d12e6f3` + las 4 suites), sin salidas de corrida, manifiesto, sello ni resultados de R1–R5. MUST — sesión aislada (`cwd` vacío, sin herramientas, sin *settings*), material inline. MUST — el resultado se congela con **sha256 registrado en `BITACORA.md` antes** de aplicarse a resultado alguno; el aplicador verifica el hash y aborta si cambió. Preferido por encima de un subagente, que heredaría la sesión del orquestador y podría leer las corridas del disco.
  - **Regla de satisfacción (MUST):** un requisito está satisfecho si **todos** los casos de aceptación mapeados a él pasan — un requisito no se cumple "en parte". Denominador = requisitos con ≥1 caso de aceptación en el instrumento; los que ninguna suite cubre (verificados por *pipeline*, manuales, o cuyo SSOT es otra spec) quedan **fuera**, ni satisfechos ni fallados. MUST — la regla amplifica: un test rojo puede tumbar varios requisitos, así que el % por requisito no es comparable con el % por test y ambos MUST reportarse.
  - **Reserva (ceguera del orquestador rota en F001) — [hallazgo 2026-07-28].** Construir el mapeo exige leer la estructura de la spec auténtica, y eso **des-cegó F001 para el orquestador**: como `SPEC-001` no tiene IDs en ninguna versión, una celda cuyo `OUT` cita `FR-nnn`/`SC-nnn` recibió necesariamente la traducción híbrida. **No invalida nada medido** — R1–R5 estaban fijadas y commiteadas antes, y el mapeo no toma ningún input de las corridas, así que carece de grado de libertad sesgable. **F013 no se ve afectado**: sus dos celdas usan la misma convención de IDs, luego no hay inferencia posible. MUST declararse en el RESULTADO.
- **3.3** **R4** = por cada contrato de `FRONTERA-<feature>`: *invocado* (usa la interfaz provista) vs *reimplementado* (define versión propia) — inspección de `OUT`.
- **3.3-bis** **Definición operacional de R4 — [enmienda 2026-07-28, post-hoc].** *Decidida al ejecutar 3.3. NO redefine la métrica de PREREG §5; la **operacionaliza**. Implementada en `logs/r4_score.py`.*
  - **Paquete del Puntuador (MUST):** solo `FRONTERA-<feature>.md` + la rúbrica de PREREG §5 + el diff `baseline..OUT` **restringido a `src/`**. MUST NOT incluirse el `run-manifest.yaml` (lleva `spec_hash`), la spec, la rama `b7/prereg`, el `SELLO-CIEGO` ni los resultados de R1/R2/R5. Una sesión fresca por celda, sin estado compartido. El **feature** es visible (inocultable: el código lo delata); el **formato** no.
  - **Escala:** `invocado` | `reimplementado` | `parcial` (invoca en un punto y duplica en otro) | `no_aplica`. Salida JSON con **evidencia `archivo:línea` obligatoria** por contrato — es lo que hace auditable un juicio de modelo.
  - **Validación cruzada contra gate objetivo (MUST donde exista):** si el contrato tiene un verificador ejecutable en el propio repo (p. ej. `tools/check_naming.py` para SPEC-000-naming), MUST correrse y **prevalece sobre el juicio del Puntuador**. Razón: el gate **es** la operacionalización que el proyecto le da a su propio contrato; un Puntuador más estricto que el contrato mide su criterio, no el contrato. MUST — registrar el juicio crudo del Puntuador junto al corregido (trazabilidad, igual que crudo/refinado en §3.4-bis).
  - **Reserva de ceguera:** los docstrings del `OUT` MAY citar IDs de requisito (`FR-005` vs `FR-US1-005`) cuya convención podría correlacionar con el formato. No es removible sin alterar el artefacto medido, y el Puntuador no tiene las specs para mapear convención→formato. Se declara y se revisa en Fase 4.
- **3.4** Consolidar **R2** desde los logs de Fase 2 (R3 se produce en Fase 3-bis).
- **3.4-bis** **Definición operacional de R2 — [enmienda 2026-07-28, post-hoc].** *Refinamiento decidido durante la extracción de R2 de Fase 3, tras observar que el extractor crudo `logs/r2_extract.py` **sobre-cuenta**. NO redefine la métrica de PREREG §4 (sellado en `b7/prereg-v1`); la **operacionaliza**. Detalle de la corrida en `experimentosdd-b7/BITACORA.md`.*
  - **Problema:** `r2_extract.py` cuenta lecturas de archivos fuera del allowlist, pero **no distingue** (i) leer internos de OTRA feature de (ii) **releer lo que la propia celda acaba de escribir** (read-after-write) ni (iii) `git diff/show <archivo propio>` (el extractor mezcla `Read` con un heurístico bash de `cat/head/tail/git show/git diff`). Evidencia: **run-b=0 vs run-d=3 para la misma feature (F001)** — los 3 de run-d son sus propios archivos del `OUT`. La diferencia mide conducta de *read-after-write*, no aislamiento.
  - **R2 refinado (MUST al consolidar):** R2 = lecturas de **internos de OTRA feature** (`src/` pre-existente fuera de la frontera declarada + specs de feature no declaradas + lecturas fuera del ws), **EXCLUYENDO**: (a) el **delta propio del `OUT`** — objetivo, = `git diff <baseline> <OUT>` — porque releer lo que uno produjo no cruza la frontera; (b) los **tests propios** de la celda — el modelo MAY escribir sus tests (§2.2, proceso SDD) y la suite oculta `TESTS-<feature>` **no está** en el baseline (§1.3), así que no puede leerla. El conteo de **lecturas de tests propios se traslada a R5** como observación de proceso, no a R2.
  - **Reporte:** MUST — registrar el conteo **crudo** y el **refinado** por celda, para trazabilidad y análisis de sensibilidad (la lectura estricta de PREREG §4 —"cualquier `tests/`"— es el límite superior; el refinado es la señal de aislamiento). El eje ciego (formato) es **intra-feature**, donde ambas celdas comparten baseline y conducta esperada → el refinamiento no favorece un formato sobre otro.
  - **Implementación:** `logs/r2_extract.py` **v2** ya materializa esta definición — computa el delta propio con `git diff <baseline> HEAD` + `git status` (baseline del `run-manifest.yaml`) y emite buckets `xfeature | own | own-tests | outside-ws | inside`, con `R2_refinado = |xfeature|` y el crudo al lado. Re-analizar es determinístico sobre los transcripts congelados (no re-corre el modelo). Backup de la v1 en `logs/r2_extract.py.v1-bak`.
  - Conecta con la reserva de frontera de §4.4 (lecturas a SPEC-005/006 al regenerar US2 = legítimas, no R2).
- **3.5** El `Puntuador` trabaja sobre `RUN-A..D` **sin conocer** el `SELLO-CIEGO`, y **sin acceso a `b7/prereg` ni al `run-manifest.yaml`**: mide **R1/R2/R4** sobre `OUT-RUN-x` + `TESTS-<feature>`. Sin `prereg`, el `spec_hash` del manifiesto es opaco → el formato queda ciego aunque el feature sea visible.
- **3.6** **R5** (adherencia SDD, `PREREG §5.1`, `[R35]`) lo extrae **mecánicamente el orquestador** del transcript de Fase 2 + el working tree (declaró `.sdd/current-spec`, registró la spec, produjo tests, no bypasseó el enforcement). **No lo puntúa el Puntuador ciego** (el transcript revela formato); los ítems son objetivos, la exposición no sesga.
- **3.6-bis** **Definición operacional de R5 — [enmienda 2026-07-28, post-hoc].** *Revisión decidida al extraer R5, tras descubrir que la premisa de enforcement de PREREG §5.1 es falsa tal como se ejecutó (ver reserva mayor en §4.4). NO reescribe PREREG (sellado en `b7/prereg-v1`); lo **operacionaliza**. Implementado en `logs/r5_extract.py`.*
  - **R5 = promedio de 3 ítems puntuables** (1/0 cada uno): (1) **declaró `.sdd/current-spec`** — reinterpretado como declaración **voluntaria**, ya que el gate nunca pudo obligar; la distinción *proactivo/reactivo* de PREREG §5.1 queda **sin sentido operativo** (no hubo bloqueos que provocaran reacción); (2) **registró la spec en `SPECS_REGISTRY.md`** — validable de forma independiente con el gate propio del proyecto, `tools/check_traceability.py`; (3) **produjo tests** (existencia).
  - **Ítem 4 de PREREG §5.1 ("respetó el enforcement / no bypass") — RETIRADO por no evaluable.** Con el gate fail-open no hay nada que bypassear: daría 1.0 a las cuatro celdas. Se reporta como información, no como puntaje.
  - **MUST NOT puntuar "tests prometidos por la spec que existen".** Que la spec **liste** tests depende de que el formato tenga *Coverage mapping* — es decir, **del tratamiento**: donde no lo hay el ítem es *no aplicable*, que no equivale a 0, y promediarlo castigaría a un formato por una sección que su anatomía no contempla. SHOULD — reportarlo como **observación cualitativa**: es señal alineada con la hipótesis de B-07 (una spec más estructurada crea una **promesa verificable**; la otra no genera nada que chequear).
  - **MUST NOT puntuar "tests que citan `FR-`/`SC-`".** Los baselines **no son uniformes** en esa convención (F013: 8/20 tests preexistentes la usan; **F001: 0/3**), así que exigirla penalizaría a un vintage por una práctica que no tiene. Se reporta sin puntuar.

- **3.7** **R6 (verificación funcional manual) — [alta 2026-07-29; NO se aplicó en la corrida de 2026-07-28].** Cubre el complemento de `R1`: `R1` se automatiza con `pytest`, luego mide sólo el subconjunto pytest-verificable del espacio de requisitos, y el resto sale del denominador por la regla de §3.2-ter. Definición en `EXPERIMENTO-B7-formato-hibrido.md` §Metricas.
  - **Universo (MUST):** exactamente los requisitos que el mapeo declara `requisitos_sin_test`. MUST NOT re-verificarse manualmente lo que ya cubre `R1` (duplicaría instrumento y abriría grado de libertad).
  - **Triaje previo obligatorio (MUST), en 3 clases** — de la corrida de B-07 se aprende que la etiqueta "sin cobertura" **mezcla tres cosas distintas** y sólo una es realmente manual:
    1. **verificable por gate objetivo del repo** (`check_naming.py`, `mypy --strict`, `lint-imports`, ausencia de diff en un módulo que la spec declara intacto) ⇒ se mide **mecánicamente**, no entra a `R6`;
    2. **cubierto por una suite que existe en `ENV-REF` pero quedó fuera de `TESTS-<feature>`** ⇒ se recupera como instrumento de `R1` extendido, previa **validación contra ambos baselines** (§3.2-bis); no entra a `R6`;
    3. **irreductiblemente manual** (UI, caso real, consistencia documental) ⇒ **este es el universo de `R6`**.
  - **Recorrido guionado (MUST pre-registrarse):** pasos idénticos entre celdas, con resultado esperado escrito por requisito **antes** de ejecutarlo; el operador registra observado vs esperado, sin reformular el paso en caliente.
  - **Ceguera (MUST):** observar **comportamiento**, nunca el fuente — los docstrings del `OUT` citan IDs de requisito cuya convención correlaciona con el formato (misma reserva que §3.3-bis). SHOULD — operador ≠ orquestador y sin acceso al pre-registro ni al sello.
  - **Reporte (MUST):** `n=1`, evidencia de juicio; MUST NOT pesar más que `R1`. Empate ⇒ no aporta dirección.

*Salida:* `SCORE-RUN-A..D` (R1, R2, R4 por Puntuador ciego; R5 mecánico por orquestador; R6 por operador, desde la próxima corrida).

### FASE 3-bis — Lazo de reparación (produce R3; después de fijar R1)

MUST — correr **después** de registrar R1 (§3.2), para no contaminarlo. Por cada `RUN-x`, sobre `OUT-RUN-x`:

- **3b.1** Correr `TESTS-<feature>`. Si todo verde → `R3=0`, fin.
- **3b.2** Si hay fallos: sesión **fresca** del `MODELO` (mismo harness; ID en `PREREG-B7.md §1`), con el **prompt de reparación congelado** (`PREREG-B7.md §2.1`), entregándole `OUT` actual + **solo los fallos de test** (nunca el código fuente de los tests → invariante al formato, no filtra el ciego). Recibir `OUT` corregido, versionar sobre `b7/run-x` (commit de reparación etiquetado).
- **3b.3** Repetir 3b.1–3b.2 hasta que `TESTS-<feature>` pase o se alcance `K=3` rondas.
- **3b.4** `R3` = nº de rondas ejecutadas. Si no converge en `K`: `R3=K`, anotar `R1_post<100%` (cuántos SC/FR quedaron rojos).
- **3b.5** El lazo lo puede operar el `Puntuador` o el Custodio; **no** requiere ver la spec ni el formato (solo OUT + fallos) → no rompe el ciego.

- **3b-bis** **Definición operacional del lazo — [enmienda 2026-07-28, post-hoc].** *Decidida al ejecutar 3b.1. NO redefine la métrica de PREREG §5; la **operacionaliza**. Implementada en `logs/r3_repair.py`.*
  - **Criterio de convergencia**: MUST — aceptación del delta, **variante estricta** (sin shim), coherente con §3.2-bis que fija la estricta como criterio primario de R1. La variante con shim no gobierna el lazo.
  - **Detalle de fallos entregado**: MUST — `pytest --tb=short`, idéntico en las 4 celdas. Incluye la línea de aserción del test y la cadena hasta el código de producción; **no** entrega los archivos de test. Justificación: con `--tb=line` varios fallos no permiten localizar el bug en el propio código (p. ej. una excepción lanzada por un stub del test), lo que inflaría `R3` por falta de información en vez de por calidad de la regeneración. El nivel es constante entre celdas → no sesga la comparación. Las rutas absolutas del entorno de medición se sanean; el contenido técnico no se altera.
  - **Formato de los slots**: MAY — el operador encuadra `{OUT_ACTUAL}` como bloques `### ARCHIVO: <ruta>` + código cercado, para que la respuesta sea parseable. El **texto envolvente del prompt congelado (`PREREG §2.1`) MUST permanecer byte-idéntico**; el encuadre es contenido de slot, idéntico en las 4 celdas, y no agrega instrucciones. Si una respuesta no resulta parseable, MUST abortarse esa ronda y registrarse — MUST NOT interpretarse a mano.
  - **Aislamiento de la sesión**: MUST — `cwd` vacío, sin herramientas de lectura/escritura/búsqueda y sin *settings* de usuario, de modo que el modelo no pueda acceder al repositorio (lo exige la regla 1 del prompt congelado).
  - **Versionado**: MUST — rama `b7/rep-x` derivada de `b7/run-x`, un commit y un tag `b7/run-x-rep<N>` por ronda. La rama `b7/run-x` **no se mueve**: fija el `OUT` one-shot que produjo R1. La medición se hace en un clon aparte para que los tests inyectados nunca queden commiteados.
  - **Reserva de ceguera (arrastrada de §3.3-bis)**: el `OUT` de cada celda cita IDs de requisito en sus propios docstrings, y las convenciones de ID difieren entre formatos. La sesión de reparación puede por tanto inferir el formato **de su propio código**. Es inevitable sin editar el `OUT`, lo que corrompería la medición. Es una reserva **más débil** que la de R4: aquí el lector es el reparador, no el puntuador, y ninguna instrucción liga su conducta al formato. MUST declararse en el RESULTADO.

*Salida:* `R3` por run; `OUT` reparado versionado aparte del `OUT` one-shot que fijó R1.

### FASE 4 — Análisis y cierre

- **4.1** El `Custodio` revela `SELLO-CIEGO` → desanonimizar `RUN→celda`.
- **4.2** Calcular el **estimando de formato** + la **lectura por-feature**.
- **4.3** Evaluar contra el **Criterio de éxito** de B-07. **[Actualizado 2026-07-29]** El criterio fue **reformulado en el SSOT** (`EXPERIMENTO-B7-formato-hibrido.md` §Criterio de exito): la parte aplicable acá es **(a)**, enunciada contra `R1`–`R6`, con unidad de inferencia intra-feature, cláusula «**≥1 secundaria independiente** en el mismo sentido y ninguna en contra» (admisibles `R4`/`R5`/`R6`; `R3` excluida por no ser independiente de `R1`), empate ⇒ no concluyente, veredicto global sólo con ≥2 features discriminantes, y **guarda de confusión** con techo *"no atribuible al formato"*. MUST — evaluar contra (a), **no** contra la redacción original (*"superar en R1 y R2 + mejorar ≥2 secundarias + `UMBRAL`"*), cuya cláusula de secundarias era no satisfacible. §4.3-bis abajo queda como **registro datado** de cómo se resolvió el problema antes de existir (a); MUST NOT reescribirse.
- **4.3-bis** **Regla de evaluación del criterio de éxito — [enmienda 2026-07-28, post-hoc, CON EL SELLO AÚN CERRADO].** *El texto de 4.3 tiene dos huecos que sólo se ven al llegar con las cinco métricas en la mano: no dice si el criterio se evalúa **por feature** o **agregado**, y su cláusula "≥2 secundarias" no tiene referente definido. Resolverlos **después** de revelar el sello sería ajustar el criterio al resultado.*
  - **Protección aplicada (MUST):** esta enmienda se escribe conociendo las **magnitudes** de R1–R5 pero **no su dirección** — el sello sigue cerrado y en F013 (la única feature que separa) el orquestador ignora cuál celda es `CAS` y cuál `HIB`. Toda regla de abajo MUST ser **simétrica en la dirección**: se enuncia sin nombrar formato ganador, de modo que no puede favorecer a H4 ni a su negación. La ceguera rota de F001 (§3.2-ter) no la compromete: F001 empata en las cinco métricas, luego no aporta dirección a ninguna regla.
  - **Agregación: por feature, MUST NOT agrupar.** Las dos features tienen baselines, *vintage*, complejidad y —según §3.2-ter— hasta espacio de requisitos distintos; §4.4 ya las declara no comparables entre sí. Además la unidad de inferencia del diseño es el **contraste intra-feature**, que es lo que cancela el sesgo de reconstrucción. Promediar las dos features mezclaría magnitudes inconmensurables. MUST — se emiten **dos veredictos**, uno por feature, y MUST NOT declararse un veredicto global único.
  - **Empate ⇒ no concluyente, MUST NOT leerse como fallo.** Si en una feature ambas celdas dan lo mismo, esa feature **no aporta evidencia en ninguna dirección**. MUST NOT contarse como refutación de H4 ni como confirmación.
  - **"Superar en R1 y R2" (MUST):** en una feature, un formato supera si `R1` es **estrictamente mayor** y `R2` **estrictamente menor** (menos lecturas fuera de la frontera) que el otro. Las dos condiciones a la vez; una sola no alcanza.
  - **Variante y granularidad de R1 para el criterio (MUST):** la **estricta** (§3.2-bis) en **granularidad de test**. Razón de simetría: F001 no admite granularidad de requisito (§3.2-ter), y sólo la de test existe en ambas features. La proyección por requisito de F013 se reporta como lectura adicional, no como criterio. *(Esta elección es direccionalmente inocua: en F013 ambas granularidades ordenan las celdas igual — 100 vs 83 y 100 vs 64 — así que la regla no cambia de ganador según cuál se tome.)*
  - **"≥2 secundarias": cláusula NO SATISFACIBLE por este diseño (MUST declararse así).** Las secundarias que enumera `EXPERIMENTO-B7-formato-hibrido.md §Metricas` (Cobertura H1, Ambigüedad temprana H2, Divergencia spec↔código, Fronteras H3, Costo de redacción, Specs vivas) pertenecen al experimento B-07 **amplio**, no a esta prueba de regenerabilidad, y **ninguna se mide acá**. Las secundarias efectivamente medidas son **R3, R4 y R5** — tres. **R4 no separa en ninguna celda.** *(Corrección 2026-07-28, posterior a la revelación del sello: la versión original de esta enmienda afirmaba que R3 tampoco separaba. Es **falso**: en F013 vale `0` y `1`. Pero ese `0` está **forzado por definición** — §3b.1 fija `R3=0` cuando `R1` ya es 100% —, luego R3 **no es independiente de R1** y contarlo como secundaria propia **duplica la primaria**. MUST — R3 se reporta, MUST NOT computarse como una de las "≥2 secundarias".)* Máximo alcanzable: **1** (R5). MUST — reportarse como cláusula **no evaluable** con este instrumento; MUST NOT reinterpretarse la lista de secundarias para que dé ≥2. *La corrección es direccionalmente inocua: el sujeto del criterio es la spec **híbrida**, que no pasa el filtro R1+R2 en ninguna feature, así que el veredicto no depende de cómo se cuenten las secundarias.*
  - **Consecuencia (MUST):** el **Criterio de éxito de B-07 no es evaluable en bloque** con esta prueba. MUST NOT declararse B-07 "superado" ni "refutado" contra él. MUST — el RESULTADO reporta (a) el veredicto R1+R2 por feature, (b) el estado de las secundarias medidas, (c) esta cláusula como no evaluable, y (d) la evidencia cruda. La no evaluabilidad del criterio es **en sí un resultado**: indica que el criterio se redactó para un experimento más ancho que el que esta prueba ejecuta, y su reformulación queda como deuda de `EXPERIMENTO-B7-formato-hibrido.md` (SSOT de hipótesis y métricas).
  - **Límite de fuerza (MUST):** `n=1` por celda, sin repetición. El contraste de una feature mezcla efecto-formato con la varianza estocástica de una única generación, y el diseño **no puede separarlos**. MUST — cualquier veredicto se enuncia como evidencia de una corrida, nunca como afirmación estadística.
- **4.4** Registrar reservas: sesgo de traducción (mitigado por diagonal); **método de corte del baseline** — **ambos** baselines se cortan por **sustracción** vía `Reconstructor` (contrafáctico "la feature nunca existió"): `F001` parte del commit más antiguo (collapsa a infra pre-F001 por ser fundacional), `F013` parte de hoy y remueve su huella (queda rico, por ser feature-hoja). La reserva residual es la **fidelidad de reconstrucción de ambos**, acotada por dos vías: (a) la valida un **gate objetivo** (compila/resuelve + frontera completa + verificación de ausencia, §1.5.c), no la confianza en el modelo; (b) el sesgo de reconstrucción es **común a las dos celdas de un feature** (comparten baseline) → **se cancela en el contraste intra-feature** (el efecto-formato), y solo pesa en la comparación cruzada `F001` vs `F013`; complejidad `F001`≠`F013`; muestra mínima. **Reserva adicional (frontera):** `FRONTERA-F013` (extraída del puerto `AgentClient` en `ports.py`) **no contiene a F013 por completo** — US1 y US3 caen dentro del puerto/`get_trace`, pero **US2 se derrama a la persistencia** ([[SPEC-005-run-persistence]]/[[SPEC-006-batch-suite]], campo `endpoint_url`), fuera de la frontera. La huella de US2 se remueve del baseline (§1.3) para no pre-contaminarlo; al interpretar **R2** debe recordarse que las lecturas del `Regenerador` hacia SPEC-005/006 al regenerar US2 son legítimas y esperables. **Reserva adicional (infra-vintage, asimetría F001↔F013):** por ser raíz, el contrafáctico de `F001` ("nunca existió") **collapsa a la era bootstrap** — su infra (constitución, tooling, `pyproject` con `python 3.11`, sin `SPEC-FORMAT`/`ci.yml`/hooks posteriores) queda a vintage **2026-06-13**, mientras la de `F013` queda a **hoy** (`python 3.13`, etc.). **No se corrige** trayendo `F001` a hoy: la infra de hoy es **causalmente downstream** de que F001 (y sus 12 features) existieran, así que importarla contaminaría el baseline de la raíz con su propia descendencia; además exigiría podar refs a SPEC-001..013 de todos los docs (alto riesgo R2) y metería convenciones anacrónicas (formato híbrido `SPEC-FORMAT`, piloteado sobre SPEC-013). La asimetría de vintage pesa **solo en la comparación cruzada** `F001` vs `F013` (ya reservada por complejidad); el contraste **intra-feature** (efecto-formato, señal primaria) es inmune porque las dos celdas de cada feature comparten baseline. *(Decisiones 2026-07-12: `F013` pasó de checkout a sustracción — antes esta reserva decía "checkout git en F013 sin sesgo de reconstrucción"; y `BASE-F001` se **confirma intacto** (`v1`=`6debd93`) como contrafáctico correcto de la raíz — deuda de alineación **cerrada**, no requiere rebuild.)*
- **4.4-bis** **RESERVA MAYOR (enforcement fail-open) — [hallazgo 2026-07-28].** La premisa de `PREREG §5.1` — *"el proyecto trae enforcement **activo** en el baseline"* — es **falsa tal como se ejecutó**. El hook `PreToolUse` de `.claude/settings.json` resuelve el intérprete como `$CLAUDE_PROJECT_DIR/.venv/bin/python` (o `Scripts/python.exe`, o `where python`) y termina en **`[ -f "$PYBIN" ] || exit 0`** — es decir, **fail-open**: si no encuentra intérprete, **sale 0 y permite la edición**. En las 4 celdas **no existe `.venv`** (crearlo requería Bash, denegado por diseño en Fase 2, §2.7) → **`tools/sdd_gate.py` nunca se ejecutó y el gate nunca bloqueó**. Evidencia: `run-a` y `run-c` escribieron 9–10 archivos de `src/` **sin declarar** `.sdd/current-spec`, algo imposible con el gate operativo.
  - **Efecto en R5:** los ítems 1 y 4 de `PREREG §5.1` cambian de significado — el 1 pasa a medir declaración **voluntaria** (no navegación del gate) y el 4 queda **degenerado** (retirado, §3.6-bis).
  - **Alcance acotado:** la condición es **idéntica en las 4 celdas** (ningún ws tiene `.venv`) → el **contraste intra-feature** (efecto-formato, señal primaria) **no se invalida**. Interactúa con la reserva de asimetría `.sdd/current-spec` ya registrada (en F001 el placeholder existe y es trackeado → hay *affordance* para declarar; en F013 está ausente y gitignored → sin affordance **y** sin gate que obligue), que pesa solo en el cruce F001↔F013.
  - **MUST — no se corrige retroactivamente:** montar `.venv` y re-correr rompería el `OUT` one-shot que fijó R1. Se declara como reserva y se considera **condición del experimento**, no defecto de una celda.
  - **Hallazgo transferible (no de B-07):** un gate de gobernanza que depende de un intérprete opcional y **sale 0** al no encontrarlo es un **agujero de enforcement silencioso** — falla abierto justo en el entorno menos preparado. Registrado en `../06-BACKLOG-INVESTIGACION-FUTURA.md`.
- **4.5** Consolidar en `RESULTADO-EXPERIMENTO-B7.md` usando `../templates/RESULTADO-EXPERIMENTO.md`.

---

## Aislamiento por ambiente (simétrico)

Ambos baselines se derivan por **sustracción desde el proyecto completo** y comparten el mismo modelo de aislamiento **por medición**:

- **`WS-F001-*` (sustracción):** el proyecto completo **menos F001 y todo lo posterior** está en disco; el código de F001 no existe (fue removido), así que su fuga es imposible, y toda lectura **fuera del allowlist** (frontera + proceso SDD + spec de trabajo, §PREREG 4) se **cuenta como R2**.
- **`WS-F013-*` (sustracción):** el proyecto completo **a hoy menos la huella de F013** está en disco; el código de F013 fue removido (fuga imposible), y toda lectura **fuera del allowlist** (§PREREG 4) se **cuenta como R2**. La huella removida incluye el **derrame de US2** a la persistencia (§1.3), fuera del puerto `AgentClient`. El modelo trabaja con **contexto pleno** siguiendo el proceso SDD del repo (§2.2); R2 mide cuánto se metió en **otras features**.

Diferencia residual: ambos cortes son **sustracción por `Reconstructor`**; difieren solo en el punto de partida por la posición del feature en el grafo de dependencias (`F001` fundacional → collapsa a pre-F001; `F013` hoja → hoy menos huella). Ambos quedan versionados por tag (§1.5) y recreables a demanda.

---

## Inputs bloqueantes (MUST resolverse antes de Fase 1)

1. ~~`MODELO` + versión~~ **RESUELTO:** asignación modelo↔rol (todos los roles) en `PREREG-B7.md §1` (SSOT — se cambia/depreca ahí). Harness Claude Code, `effortLevel: medium` (default vigente, status quo). Seed/temperatura: no expuestos por este harness, no aplica.
2. ~~`UMBRAL` de sobrecosto de redacción~~ **RESUELTO (2026-07-10):** evaluación cualitativa, sin umbral numérico.
3. ~~`FRONTERA-F001`~~ **RESUELTO (2026-07-10):** ver definición en §Glosario ("Fronteras in-spec").
4. ~~Confirmar el commit padre exacto de `9f89369`~~ **RESUELTO (2026-07-10) y luego SUPERADO (2026-07-12):** el padre es `9fd3954912e9a9b85a980bc3a57256fd8363a378`, pero **ya no se usa como baseline**: el checkout de ese commit resultó ser un rebobinado de 19 commits (docs viejos + `SPEC-013` a medio escribir), no "el repo entero menos F013". `BASE-F013` pasó a **sustracción desde hoy** (§1.3). Se conserva el hallazgo válido: `PlatformConfig` pre-existe a F013 (infra agnóstica); la señal de ausencia es su dispatch por `AGENT_CLIENT_TYPE`, no la clase.

---

## Referencias

- Experimento y métricas (SSOT): `EXPERIMENTO-B7-formato-hibrido.md`.
- **Inputs congelados (constantes, PROMPT de regeneración, fronteras, R2/R4, tests): `PREREG-B7.md`** — lo que la Fase 0.7 sella en `b7/prereg-vN`.
- Estrategia de medición y frontera in-spec: ídem, §"Estrategia de medición de la regenerabilidad".
- Base metodológica externa: tarea aislada + configuración fija [R33]; frontera de contexto y DIR/reimplementación (base de R4) [R34]; Power Inversion / regenerabilidad como test de gobernanza [R35]; taxonomía spec-first/anchored/as-source [R30] (`../REFERENCIAS.md`).
- Template de cierre: `../templates/RESULTADO-EXPERIMENTO.md`.

---

[SDD-Check]
- Spec leida: SI (SPECS_REGISTRY.md línea 54 — contenido de `experimentos/` exento de spec propia, generado desde templates; EXPERIMENTO-B7 como fuente de hipótesis/métricas; templates/EXPERIMENTO.md y RESULTADO-EXPERIMENTO.md)
- Incluye/Excluye verificado: SI — runbook operacional de la métrica primaria de B-07; NO redefine hipótesis ni métricas (referencia a EXPERIMENTO-B7); SPEC-009 forward EXCLUIDA de esta versión
- Validaciones aplicadas: nombres del cuerpo consistentes con el glosario; cada celda del 2×2 mapea a WS+RUN+SCORE; cada métrica R1-R4 tiene un paso que la produce; refs [R30][R33][R34][R35] verificadas en REFERENCIAS.md; fechas YYYY-MM-DD; lenguaje normativo MUST; 4 inputs bloqueantes marcados [NEEDS CLARIFICATION], sin fingir resolución
- SSOT afectado: ninguno propio (doc de `experimentos/`, exento de registro); EXPERIMENTO-B7 recibe puntero + enmienda de corpus en la misma entrega
- Derivados a revisar: EXPERIMENTO-B7-formato-hibrido.md (puntero + enmienda de corpus + riesgos nuevos); software/PLAN-PRUEBAS.md §B-07 (línea de puntero)
- Cobertura: completa para el diseño; la ejecución (correr los 4 RUN) queda pendiente de los 4 inputs bloqueantes
- Deuda arrastrada: (1) MODELO+versión; (2) UMBRAL; (3) FRONTERA-F001; (4) commit padre de 9f89369 — RESUELTO y luego SUPERADO (2026-07-12): `BASE-F013` pasó de checkout a sustracción desde hoy (§1.3); (5) alinear `BASE-F001` al criterio "proyecto completo − feature" — **CERRADA (2026-07-12):** ya alineado; por ser raíz su contrafáctico collapsa a la era bootstrap, se confirma `v1` intacto sin rebuild (§4.4)
- Riesgos/reservas: sesgo de traducción (mitigado por diagonal balanceada); baselines simétricos (ambos = proyecto completo → sustracción por `Reconstructor`, aislamiento por medición); reserva residual = fidelidad de la reconstrucción de **ambos** baselines, acotada por gate objetivo + cancelación intra-feature; **`FRONTERA-F013` no contiene US2** (derrame a persistencia SPEC-005/006 — removido del baseline, §1.3/§4.4); manifiesto de run RESUELTO (run-manifest.yaml, ciego por formato, Puntuador sin prereg); complejidad F001≠F013; muestra mínima (2 features, 1 proyecto)
