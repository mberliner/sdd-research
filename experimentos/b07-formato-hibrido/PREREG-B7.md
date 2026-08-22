# Pre-registro B-07 — Inputs congelados de la prueba de regenerabilidad 2×2

## Propósito

Contiene **los artefactos que MUST congelarse antes de la Fase 1** del runbook `PRUEBA-REGENERABILIDAD-B7.md`: constantes, el PROMPT de regeneración, las fronteras in-spec y el mapeo de tests. Es el contenido humano-legible que la Fase 0.7 sella como tag `b7/prereg-vN` en el clon del testigo.

Este doc **no** redefine hipótesis ni métricas (viven en `EXPERIMENTO-B7-formato-hibrido.md`, SSOT) ni el procedimiento (vive en `PRUEBA-REGENERABILIDAD-B7.md`, runbook). Solo **fija los valores**.

> **Estado:** borrador de pre-registro. Solo se construyó lo *necesario y buildable sin invadir roles de ejecución*: constantes, PROMPT de regeneración, FRONTERA-F013, definición R2, lista R4, mapeo de tests. **Pendiente de ejecución (roles `Traductor`/`Reconstructor`):** las 2 specs traducidas (0.4) y la reconstrucción de BASE-F001 (1.2). El armado de prep de este doc es **model-agnóstico** y separado de la sesión de scoring del `Puntuador`.

---

## Ciclo de vida y congelamiento (cuándo se puede ajustar este doc)

El límite duro de todo ajuste es **el primer `RUN` de Fase 2**, no el armado de ambientes. Ajustar un input *después* de ver salidas de regeneración invalida la atribución método→resultado (runbook §0.7, §1.5.e). El contenido se divide en dos clases:

- **Congelado en `v1`** (antes de Fase 1; no depende del ambiente): constantes de modelo y `K` (§1), **PROMPT de regeneración** (§2) y **prompt de reparación** (§2.1), definición operativa R2 (§4), lista de contratos R4 (§5), las 4 specs y el `SELLO-CIEGO`. MUST NOT cambiarse salvo re-sello completo `b7/prereg-vN+1`, y solo si **aún no arrancó ninguna `RUN`**.
- **Atestiguado por ambiente** (se completa/verifica en Fase 1, antes del 1er `RUN`): hashes de los tags `b7/base-fNNN-vN` (§1.5.f), confirmación de targets de `TESTS-*` contra `ENV-REF` (§6), y correcciones de **frontera** (§3) que el **gate objetivo** §1.5.c destape (p. ej. un contrato que la base necesita y no estaba listado). Esto es corregir el *instrumento*, no el *resultado* — legítimo mientras no haya corrido ningún `RUN`; se materializa como `vN+1`.

**Regla:** iniciada la Fase 2, el tag activo queda **inmutable**; todo hallazgo posterior se registra como reserva en `RESULTADO-EXPERIMENTO-B7.md`, nunca como re-corte de este doc.

> **Nota de ambiente (2026-07-12, pre-1er RUN — clase "atestiguado por ambiente", §18):**
> **(a) Método de `BASE-F013`:** se abandona el **checkout puro** de `9fd3954` (registrado en §"Pendiente" como `v1`) y se adopta **sustracción desde hoy menos la huella de F013** (runbook §1.3, reescrito). Motivo: el checkout era un rebobinado de 19 commits con `SPEC-013` a medio escribir (1 US), violaba §0.7 ("ambiente libre de spec del feature") y la simetría de §Aislamiento. Se materializará como `b7/base-f013-v2` (§1.5.e); **el sello `b7/prereg-v1` NO se toca** (specs, PROMPT, R2, R4, tests-mapping intactos).
> **(b) Reserva de frontera (US2):** `FRONTERA-F013` (§3.2, extraída del puerto `AgentClient`) **no contiene a F013 por completo** — **US2** (`endpoint_url`) se derrama a la persistencia (`SPEC-005`/`SPEC-006`), fuera del puerto. **No se redefine la frontera** (sigue siendo el puerto); en su lugar la huella de US2 se **remueve del baseline** (§1.3). Al interpretar R2, las lecturas del `Regenerador` hacia SPEC-005/006 al regenerar US2 son legítimas.
> **(c) Verificación diferida:** el mapeo `TESTS-F013` (§6) y las anclas "preexiste en `9fd3954`" deben **re-verificarse contra `b7/base-f013-v2`** al construirlo (los módulos no-F013 deben seguir presentes); es corrección de instrumento pre-RUN, no cambio de resultado.
> **(d) `BASE-F001` se confirma intacto (`v1` = `6debd93`):** NO se lleva a "hoy". Por ser feature **raíz**, su contrafáctico ("F001 nunca existió") collapsa a la era **bootstrap** (vintage 2026-06-13, `python 3.11`); la infra de hoy es downstream de que F001 existiera, así que importarla contaminaría el baseline de la raíz. Queda una **reserva de infra-vintage** (F001 py3.11 vs F013 py3.13) que pesa solo en la comparación cruzada F001↔F013 (ya reservada por complejidad); el contraste intra-feature es inmune. Detalle en runbook §4.4.

---

## 1. Constantes (§0.1 del runbook)

| Constante | Valor | Notas |
|---|---|---|
| `MODELO` (Regenerador) | **claude-sonnet-5** | harness Claude Code, `effortLevel: medium`; sin seed/temp expuestos |
| `MODELO-PUNTUADOR` | **claude-opus-5** | scorer R1-R4, ciego a sello/prereg/manifiesto. *Sustituye a `claude-opus-4-8` (2026-07-28, deprecado por el proveedor); ver nota abajo.* |
| `MODELO-TRADUCTOR` | **claude-fable-5** | 0.4, spec→spec sin `src/` |
| `MODELO-RECONSTRUCTOR` | **claude-fable-5** | 1.2, BASE-F001; MAY coincidir con Traductor |
| `HARNESS` | Claude Code | no se varía en Fase 1 |
| `UMBRAL` | cualitativo, sin corte numérico | tiempo/extensión/iteraciones observados |
| `K` (tope de reparación R3) | **3** | rondas máximas del lazo post-R1; si no converge → `R3=K`, `R1_post<100%` |

Los tres roles no-Regenerador usan modelos **≠ `MODELO`** → `SHOULD ≠ Regenerador` satisfecho literalmente.

> **Nota de sustitución de `MODELO-PUNTUADOR` (2026-07-28, post-Fase 2 — clase "constante NO consumida"):**
> `claude-opus-4-8` fue **deprecado por el proveedor**; el rol pasa a **`claude-opus-5`** (disponibilidad verificada en el harness el 2026-07-28).
> **Por qué NO abre corrida nueva:** la regla de §1 ("después del 1er `RUN` el cambio abre una corrida nueva") aplica a constantes **ya consumidas** por las salidas — paradigmáticamente `MODELO` (Regenerador), que produjo los 4 `OUT`. `MODELO-PUNTUADOR` **no había puntuado nada** al momento del swap: R1 (§3.2-bis), R2 (§3.4-bis) y R5 (§3.6-bis) se extrajeron **mecánicamente** con herramientas deterministas del orquestador (`logs/r1_run.py`, `r2_extract.py`, `r5_extract.py`), y `scores/` solo contenía sus JSON. No hay puntajes mezclados entre dos scorers, que es el riesgo que la regla protege.
> **Invariantes preservados:** `Puntuador SHOULD ≠ MODELO` (opus-5 ≠ sonnet-5) ✓; ceguera a sello/prereg/manifiesto intacta (no depende del modelo) ✓; `Traductor`/`Reconstructor` sin cambio ✓.
> **Alcance del swap:** solo **R4** (único ítem pendiente del Puntuador) y, si se decide operarlo con el Puntuador, el lazo de reparación de Fase 3-bis (§3b.5 lo permite explícitamente al Custodio también).
> **Reserva:** un swap de scorer sería un confusor serio si R4 se hubiera puntuado parcialmente con el modelo anterior. MUST — si en algún momento se re-corre R4, re-correrlo **completo** con un único modelo, nunca celda por celda con scorers distintos.

> **SSOT de asignación modelo↔rol.** Esta tabla es el **único** lugar (doc) con IDs de modelo concretos; su espejo **ejecutable** es `experimentosdd-b7/custodio/constantes.env` (lo lee el lanzador con `source`). Cambiar un modelo = editar la fila **y** la línea del `.env`. El resto del pre-registro, el runbook y el experimento refieren siempre por **rol** (`Regenerador`/`Puntuador`/`Traductor`/`Reconstructor`) o por **constante** (`MODELO`, `MODELO-PUNTUADOR`, …), nunca por ID. Los IDs que aparezcan en changelogs o bloques `[SDD-Check]` son **registro histórico** (lo que se decidió en esa fecha), no config viva — no se editan.
>
> **Para cambiar o deprecar un modelo:** editar SOLO la fila correspondiente de esta tabla; ningún otro punto necesita tocarse. Si el cambio ocurre **después** de sellar `b7/prereg-v1` pero **antes** del 1er `RUN` → re-sello `vN+1`. **Después** del 1er `RUN`, el modelo es una constante ya consumida → el cambio abre una **corrida nueva**, no una edición (el resultado se compara a igual modelo). Regla de independencia a preservar en cualquier swap: `Puntuador`, `Traductor` y `Reconstructor` **SHOULD ≠ `MODELO`**; `Traductor` y `Reconstructor` MAY coincidir entre sí.

### Prompts por rol
- **Regeneración** (`Regenerador`): **congelado e idéntico entre celdas** — ver §2. Es la única plantilla que debe pre-craftearse (el Regenerador es ciego al runbook; solo recibe spec+frontera+prompt).
- **Reconstructor / Traductor**: NO se pre-craftean. Su instrucción **es la sección del runbook** (§1.2 / §0.4); MUST **registrarse el texto exacto usado** al ejecutar (trazabilidad). Justificación: la corrección del Reconstructor la valida un gate objetivo (§1.5.c) y su sesgo cancela intra-feature; la del Traductor la mitiga la diagonal balanceada + disciplina spec→spec.

---

## 2. PROMPT de regeneración (congelado, idéntico entre las 4 celdas)

Plantilla única con un slot `{SPEC_PATH}` (ruta de la spec de trabajo). El texto envolvente MUST ser byte-idéntico en las 4 celdas. **El modelo trabaja con contexto pleno del proyecto** (aislamiento **por medición**, no por construcción — runbook §Aislamiento): la spec se lee de su ruta natural en `specs/`, no se inyecta; el repo entero (menos el feature) está en disco y toda lectura fuera del allowlist (§4) se cuenta como R2.

**Neutralidad R4:** la plantilla enuncia que el código base del proyecto está disponible, **sin ordenar** invocar los contratos ni reimplementarlos — reusar o duplicar queda como decisión del modelo, que es justo lo que R4 mide. Coachear el reuso invalidaría R4.

```text
Sos un ingeniero trabajando en este proyecto Python (arquitectura hexagonal, proceso
Spec-Driven Development). Tu tarea es IMPLEMENTAR la especificación `{SPEC_PATH}`,
produciendo el código de producción que la satisface.

- Seguí el proceso y las convenciones del PROPIO proyecto, documentados en el repo
  (`AGENTS.md`, `CONSTITUTION.md`, `specs/SPEC-000-*`, arquitectura). No uses ninguna
  guía externa a este proyecto.
- El código base del proyecto (dominio, adaptadores, composition roots) está presente
  y disponible.
- Si algo no está en la spec ni en el proyecto y te obliga a asumir, anotalo como
  comentario `# SUPUESTO: <qué asumiste y por qué>` en el código.

Implementá ahora la especificación.
```

Los `# SUPUESTO:` y el log de archivos abiertos alimentan **R2** (lo que el modelo tuvo que inferir/consultar fuera de la frontera).

### 2.1 PROMPT de reparación (para el lazo de R3, congelado, idéntico entre celdas)

Se usa **solo en Fase 3-bis**, después de medir R1. Cada ronda entrega la salida actual + **los fallos de test** (no los archivos de test completos; invariantes al formato → no filtran formato). Slots por ronda: `{OUT_ACTUAL}` (código regenerado hasta ahora) y `{FALLOS_TEST}` (salida de fallos, sin el código fuente de los tests).

```text
El siguiente código de producción implementa una funcionalidad pero falla algunas
verificaciones automáticas. Corregilo para que todas pasen, sin reescribirlo de cero
salvo que sea necesario.

Reglas:
1. Trabajás SOLO con el código de abajo y los fallos reportados. No dispongas de los
   archivos de test ni de ningún otro archivo del repositorio.
2. Devolvé el código de producción corregido completo.

## Código actual
{OUT_ACTUAL}

## Fallos reportados
{FALLOS_TEST}

Corregí ahora.
```

Se corre en sesión fresca del `MODELO` (§1), hasta `K=3` rondas o hasta que `TESTS-<feature>` esté todo verde. `R3` = nº de rondas ejecutadas.

---

## 3. Fronteras in-spec (§0.3)

Único contexto entregado al `Regenerador` además de la spec. Escritas por humano, **nunca** código regenerado.

### 3.1 FRONTERA-F001 (foundational — pocos contratos externos)

F001 es fundacional: *crea* `TestCase` y `ports.py`, no consume muchas interfaces previas. Su frontera son reglas + estructura + el schema del agente:

1. **SPEC-000-naming** — invariante de nomenclatura agnóstica (identificadores no referencian proveedor/framework UI/serialización/protocolo de auth) + tokens prohibidos + excepciones.
2. **SPEC-000-bootstrap** — estructura `src/{domain,adapters,build,dashboard}`, `specs/`, `tests/{unit,integration}` + hooks bloqueantes (`ruff`, `mypy --strict` sobre `src/`, linter de naming, `import-linter` con `domain/` ↛ `adapters/`/`dashboard/`).
3. **`schemas/FI_Orquestador_Input.schema.json`** — schema externo; SPEC-001 lo referencia para `datos_requeridos.otros.message` ↔ `TestCase.datos_otros_mensaje`.

*Reserva declarada:* F001 tiene menos contratos que F013 (complejidad F001≠F013) → el 2×2 lo compensa balanceando por traducción, no por pareo de dificultad.

### 3.2 FRONTERA-F013 (extraída de `ports.py` + SPEC-013)

Contratos existentes en el padre de `9f89369` que F013 consume/extiende (el delta a regenerar NO se incluye):

1. **Puerto `AgentClient`** (`src/domain/ports.py`, `Protocol`) — 5 métodos, firma vigente:
   - `send(form: dict[str, Any], conversation_id: str | None = None) -> AgentResponse`
   - `wait_for_completion(thread_id: str, timeout_seconds: int) -> bool`
   - `get_thread_messages(thread_id: str) -> list[dict[str, Any]]`
   - `get_final_response(thread_id: str, fallback_content: str) -> AgentResponse`
   - `get_trace(thread_id: str) -> AgentTrace`
2. **`AgentResponse`** (`src/domain/ports.py`, dataclass) — tipo de retorno que el adaptador construye.
3. **Puerto `CredentialProvider`** (`src/domain/ports.py`, `Protocol`) — `get() -> str`.
4. **`PlatformConfig` base pre-F013** (`src/adapters/platform_config.py`) — infra agnóstica que solo conoce `remote_async`. Es la clase que F013 **extiende** (agrega `AGENT_CLIENT_TYPE`, `CLIENT_TYPE_SYNC_HTTP`, `_REQUIRED_VARS_BY_CLIENT`, dispatch). Se entrega la base **sin** esas adiciones.
5. **Punto de wiring / composition root** (`src/dashboard/app.py`) — donde se instancia el cliente; FR-US1-008 relaja la anotación al puerto abstracto.
6. **Contrato de config** — variables de entorno `AGENT_CLIENT_TYPE`, `ES_*` (remote_async), `ALT_CLIENT_*` (sync_http).

---

## 4. Definición operativa dentro/fuera de la frontera (para R2 reproducible)

**Principio (adaptación B-07):** la **SPEC declara su propio contexto**. Lo que la spec referencia o el proyecto exige como proceso es contexto **legítimo** (dentro); tener que leer algo que la spec **no** declaró es la señal de que la spec no se bastó (R2).

- **Dentro** (no cuenta como R2): (a) la `SPEC-<celda>` de trabajo (`.b7/SPEC.md` + su copia natural `specs/SPEC-0NN-…md`); (b) los contratos de la `FRONTERA-<feature>` de §3; (c) las **specs que la spec de trabajo declara/referencia** explícitamente (`Depende de:`, `[[SPEC-xxx]]`) **y que existen en el baseline**; (d) los **docs de proceso/convención SDD del propio proyecto** (`AGENTS.md`, `CONSTITUTION.md`, `CLAUDE.md`, `specs/SPEC-000-*`, `docs/ARCHITECTURE.md`). Consultar las reglas del proyecto y las dependencias declaradas es el **comportamiento esperado de un contribuidor SDD**, no una fuga.
- **Fuera** (cada acceso = **+1 R2**): abrir los **internos de código de *otras* features** (p. ej. `src/adapters/remote_agent_client.py` por dentro, `src/adapters/file_run_repository.py`) o una **spec que la spec de trabajo no referencia**, cualquier **test**, historial git, o consultar al usuario. También cuenta como "inferencia fuera" cada `# SUPUESTO:` donde el modelo suplió información ausente.
- El **transcript** de la sesión de Fase 2 (log de `Read`/`Grep`/`Glob`) es la evidencia; **crítico en `WS-F013-*`** (el repo entero en disco). El allowlist ejecutable vive en `logs/frontera-<feature>.allowlist` (lo aplica `logs/r2_extract.py`); enumera la frontera + proceso SDD + las specs declaradas por la spec.

> **Alcance de la referencia (R2 vs [R34]):** RepoExec [R34] es un benchmark a **nivel de función** que *provee* las dependencias directas y mide su uso con el **DIR** (= nuestro **R4**); su modelo **no recorre el repo** y no contempla docs de proceso. B-07 estudia regenerabilidad en un **flujo SDD real** (feature entero, contexto natural), así que **R2 es una adaptación propia** de la noción de "frontera de contexto" [R34] + "tarea aislada / configuración fija" [R33]: mide si la spec fue **auto-suficiente** dentro del contexto que ella misma declara. `DIR/R4` queda como la métrica de uso-de-contexto anclada literalmente en [R34].

---

## 5. Lista de contratos para R4 (invocado vs. reimplementado)

Por cada contrato, el `Puntuador` clasifica el código regenerado como *invocado* (importa/usa la interfaz provista) o *reimplementado* (define una versión propia equivalente).

**F013:**
| Contrato | "Invocado" = | "Reimplementado" = |
|---|---|---|
| Puerto `AgentClient` | el nuevo `SyncHttpAgentClient` satisface el `Protocol` importado | define su propia interfaz paralela |
| `AgentResponse` | construye/retorna el tipo provisto | define un dataclass equivalente propio |
| Puerto `CredentialProvider` | `StaticCredentialProvider` implementa el `Protocol` provisto | define su propio contrato de credencial |
| `PlatformConfig` | extiende la clase existente | redefine la config desde cero |

**F001:** contrato principal = el mapeo al schema `FI_Orquestador_Input.schema.json` (`datos_requeridos.otros.message`). Menos contratos que F013 (reserva §3.1).

---

## 5.1 R5 — Adherencia al proceso/gobernanza SDD (secundaria) [R35]

Mide si el `OUT` siguió el **proceso SDD del propio proyecto** (regenerabilidad como test de gobernanza, [R35]). El proyecto trae enforcement **activo** en el baseline: hook `PreToolUse` → `tools/sdd_gate.py` (bloquea editar `src/` sin spec declarada+registrada+editada-tras-declarar) + `tools/check_traceability.py`. R5 lo **extrae mecánicamente el orquestador** desde el transcript de Fase 2 + el working tree (**no** el `Puntuador` ciego — el transcript contiene la spec, que revela formato; los ítems son **objetivos** (¿se escribió tal archivo? ¿se editó el hook?), así que la exposición al formato no los sesga). Checklist por RUN:

| Ítem | Full | Parcial | 0 |
|---|---|---|---|
| Declaró `.sdd/current-spec` antes de tocar `src/` | proactivo | reactivo (tras bloqueo del gate) | nunca |
| Registró la spec en `SPECS_REGISTRY.md` | sí | — | no |
| Produjo tests trazables a FR/SC (convención del proyecto) | sí | parcial | no |
| Respetó el enforcement | no lo tocó | — | **bypass** (deshabilitó el hook / editó `.claude/settings.json` / forzó el gate) |

Score = fracción de ítems cumplidos (bypass del enforcement es la violación más grave). **Neutralidad:** el `PROMPT` (§2) apunta a los docs de proceso del repo pero **no enumera** estos pasos → la adherencia se mide, no se coachea. R5 es **secundaria** (no entra en el criterio primario R1+R2; es de las "≥2 secundarias"). Plausiblemente sensible al formato (spec más clara → proceso más limpio), que es la señal que B-07 busca.

**Ceguera:** declaración, registro, spec copiada y tests del modelo **revelan formato** → el lanzador **commitea solo `src/`** en la rama de run; R5 se observa del working tree/transcript, nunca del commit ciego. (En F013 `.sdd/current-spec` está gitignored, así que ni siquiera es staged; en F001 es trackeado pero `git add src/` no lo incluye.)

**Reserva (asimetría `.sdd/current-spec`):** en el proyecto **bootstrap** (F001) el archivo `.sdd/current-spec` está **trackeado** (placeholder con comentarios de ayuda); en **hoy** (F013) está **gitignored** y **ausente** del baseline. Es evolución real del proyecto, no un artefacto. Efecto posible: en F001 el modelo puede **ver** el placeholder al explorar y declarar **proactivo**, mientras en F013 tiende a descubrir el gate al ser bloqueado (**reactivo**) — un sesgo en el ítem proactivo/reactivo de R5. **Se cancela en el contraste intra-feature** (constante dentro de cada feature); solo pesaría en la comparación cruzada F001↔F013 (ya reservada). **Decisión (2026-07-12):** se **deja la diferencia** (es el estado auténtico de cada vintage); si al analizar R5 aparece un efecto atribuible a esto, se evalúa una **prueba adicional** equalizando el affordance.

---

## 6. Mapeo de tests de aceptación (§Fase 3.1)

Suites levantadas de `ENV-REF`, aplicadas **post-regeneración**. El `Custodio` confirma imports/targets de cada archivo contra `ENV-REF` antes de sellar.

**Confirmación contra `ENV-REF` (2026-07-11, HEAD `8bff08c`):**

- **TESTS-F001:** `tests/unit/test_test_case.py` (13 funciones ≈ 30 casos colectados vía `parametrize` — consistente con el "(30 tests)" de SPEC-001; sin cambios desde `af7109b`, instrumento estable). (El formulario del dashboard es verificación visual/manual de SPEC-001, no suite automatizada.)
  - *Removido* `tests/unit/test_case_loader.py`: pertenece a SPEC-004 (importa `src/build/case_loader.py`, funcionalidad posterior a F001) — no es aceptación de SPEC-001 y su target no existirá en `WS-F001-*`.
- **TESTS-F013:** `tests/unit/test_agent_client_factory.py`, `tests/unit/test_sync_agent_client.py`, `tests/integration/test_sync_client_run_one.py` (las tres **nuevas en F013** = aceptación pura del delta); `tests/unit/test_platform_config.py` (**mixta**: preexiste en `9fd3954`, F013 le agrega 98 líneas — la parte nueva es aceptación del delta, la preexistente actúa como regresión de la base).
  - *Removido* `tests/unit/test_token_provider.py`: preexiste en `9fd3954` **sin cambios** por F013 — pasa en verde sobre el baseline solo, no mide la regeneración.
  - Módulos preexistentes que las suites importan (`platform_config`, `remote_agent_client`, `token_provider`, `message_builder`, `run_suite`, `classification_evaluator`) verificados presentes en `9fd3954`; `sync_agent_client` y `agent_client_factory` ausentes (delta a regenerar, correcto).

---

## Pendiente antes de sellar `b7/prereg-vN`

**Congelado en `v1` (antes de Fase 1):**
- [x] **SPEC-F001-HIB** y **SPEC-F013-CAS** traducidas por `Traductor` (§1), spec→spec (§0.4) — hecho 2026-07-11 (fable-5, instrucción autocontenida sin acceso a repo; hashes y procedencia en `experimentosdd-b7/repo/b7-prereg/PROCEDENCIA.md`). SPEC-F001-CAS congelada en `af7109b` por decisión del Custodio (evita la evolución post-F001 de `c482a95`).
- [x] Completar el Checklist de pre-registro de `EXPERIMENTO-B7` y generar `SELLO-CIEGO` (§0.5/0.6) — sello generado por el Custodio 2026-07-11, sha256 `a90cd5fa…63e6f0`; el único checkbox abierto del checklist ("contexto = sesión fresca") es procedimental y se aplica en Fase 2.

**Atestiguado por ambiente (Fase 1, antes del 1er `RUN`; admite `vN+1`):**
- [x] Confirmar imports/targets de las suites de §6 contra `ENV-REF` — hecho 2026-07-11 (dos correcciones: fuera `test_case_loader.py` de TESTS-F001 y `test_token_provider.py` de TESTS-F013; ver §6).
- [x] Anotar hashes de `b7/base-f001-vN` / `b7/base-f013-vN` (§1.5.f) — 2026-07-11:
  `b7/base-f001-v1` = `6debd935521767094fa5dea93fe9dbcd38cade71` (3 commits de sustracción sobre `3f1ed33`);
  `b7/base-f013-v1` = `9fd3954912e9a9b85a980bc3a57256fd8363a378` (checkout puro, 0 commits) — **SUPERADO (2026-07-12):** ver Nota de ambiente (a). Gates verdes de v1 verificados en su momento (240 tests; mypy con override `--python-version 3.13`).
  **`b7/base-f013-v2` = `3c467b629d5ff55b52cfc1e9a6bd0889b3cb0995`** (2026-07-12, **vigente**): sustracción desde hoy (`8bff08c`) menos huella de F013, 1 commit (`3c467b6`), rama `b7/base-f013`. Reconstructor = **fable-5** (sesión externa aislada, instrucción `logs/INSTRUCCION-RECONSTRUCTOR-F013.md`). **Gate objetivo re-corrido por el orquestador (venv py3.13 externo):** ruff ✔, mypy --strict ✔ (25 files, sin override), check_naming ✔, lint-imports 2/2 KEPT ✔, **pytest 256 passed** ✔, **grep de ausencia de F013 = 0** ✔, `specs/SPEC-013` ausente, `src/domain/ports.py` (FRONTERA-F013) **sin diff vs 8bff08c**. Tag `v1` intacto.
- [x] Aplicar correcciones de frontera (§3) que el gate objetivo §1.5.c destape — no hubo: ambas fronteras resultaron completas tal como estaban.
- [x] Registrar el texto exacto de instrucción usado por `Reconstructor` y `Traductor` — 2026-07-11: `experimentosdd-b7/logs/INSTRUCCION-TRADUCTOR-*.md` e `INSTRUCCION-RECONSTRUCTOR-F001.md`.

**Rutas físicas de ambientes (runbook §Fase 1), base `/datum1/Descargas/Claudio/experimentosdd-b7/`:**
`ENV-REF` = `env-ref/` (read-only, HEAD `8bff08c`); repo versionado = `repo/` (ramas y tags `b7/*`); `ENV-F001`/`ENV-F013` = `ws/run-{a..d}/` (los clona el Custodio por celda según el sello, script `custodio/clonar_ws.sh`). Bitácora de ejecución: `BITACORA.md`.

---

## Referencias

- Hipótesis y métricas (SSOT): `EXPERIMENTO-B7-formato-hibrido.md`.
- Procedimiento paso a paso (runbook): `PRUEBA-REGENERABILIDAD-B7.md`.
- Base metodológica: tarea aislada + configuración fija [R33]; frontera de contexto y DIR [R34] (`../../REFERENCIAS.md`).

---

[SDD-Check]
- Spec leida: SI (SPECS_REGISTRY.md L54 — experimentos/ exento de spec propia; EXPERIMENTO-B7 SSOT de hipótesis/métricas; runbook SSOT del cómo)
- Incluye/Excluye verificado: SI — solo fija valores congelados de Fase 0 (constantes, PROMPT, fronteras, R2/R4, tests); NO redefine hipótesis/métricas/procedimiento; NO incluye las traducciones ni la reconstrucción (roles de ejecución fable-5)
- Validaciones aplicadas: FRONTERA-F013 extraída por lectura directa de `src/domain/ports.py` y SPEC-013 en el testigo; FRONTERA-F001 de la declaración `Depende de:` de SPEC-001; PROMPT neutral respecto a R4; commits ancla ya verificados; refs [R33][R34]; fechas YYYY-MM-DD; lenguaje normativo MUST
- SSOT afectado: ninguno (doc nuevo de experimentos/, exento de registro)
- Derivados a revisar: EXPERIMENTO-B7 (checklist a sincronizar + puntero a este doc); runbook §0.1/Inputs (puntero a este doc)
- Cobertura: completa para los inputs congelables ahora; quedan 4 ítems de "Pendiente antes de sellar" que requieren ejecución de roles o confirmación del Custodio
- Deuda arrastrada: (1) traducir las 2 specs cruzadas (fable-5); (2) reconstruir BASE-F001 (fable-5); (3) confirmar suites contra ENV-REF; (4) sincronizar checklist de EXPERIMENTO-B7 (marcador stale de MODELO)
- Riesgos/reservas: complejidad F001≠F013 (frontera F001 más liviana); un PROMPT poco realista bajaría la señal absoluta sin invalidar el contraste; la confirmación de targets de test queda al Custodio
