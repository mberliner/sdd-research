# Comparativa: GitHub Spec Kit vs. proyecto testigo (`evaluador-flujo-intent`)

Fecha: 2026-05-26. Actualizado: 2026-07-09; sincronizado con el cierre de B-07 el 2026-07-29.
Deriva de: `ANALISIS-SPEC-KIT.md` (SSOT del flujo interno de Spec Kit).
Fuentes: GitHub Spec Kit v0.8.13 (consultada 2026-05-21) [R10]; artefactos reales del testigo `evaluador-flujo-intent` (ex `agent-test-suite`; `../../../test_circuito_intents/evaluador-flujo-intent/`), observados al 2026-07-09 (HEAD `8bff08c`, 64 commits).

> Nota de premisa (2026-06-21): el testigo se reorganizo sobre la premisa **SDD universal primero, adaptadores por ambiente despues**: `AGENTS.md` es el SSOT del protocolo (lo leen opencode/Cursor/Codex/Aider/Gemini CLI por convencion; Claude Code via `@AGENTS.md`); el cuerpo semantico de `/analyze` y `/clarify` vive neutro en `docs/playbooks/` y cada asistente recibe un wrapper fino (`.claude/skills/`, `.opencode/command/`). Ademas el testigo **ya adopto git + CI + pre-commit**. Las celdas y bullets que asumian "sin git/sin CI" / "Claude-only" se corrigen abajo; los bloques `[SDD-Check]` datados previos quedan como registro de su fecha.
Alcance: Linea B (software).

---

## 1. Implementacion de SDD

| Dimension | Spec Kit | Proyecto testigo |
|---|---|---|
| Tesis sobre la spec | "Power Inversion": la spec es el artefacto *primario* que **genera** el codigo; el codigo es "ultima milla" regenerable/desechable (pivotar = regenerar desde la spec) | Spec = "mejor representacion actual del conocimiento" + **spec viva** (spec -> ejecucion -> observacion -> ajuste); el codigo **no se regenera desde la spec**: se mantiene y evoluciona, y la spec se reconcilia con el (circuito bidireccional). La regenerabilidad es justo lo que midio B-07: cerrado 2026-07-28 sin ventaja del formato hibrido |
| Motor del flujo | CLI `specify` + slash commands ejecutados por el agente; asume git + CI implicito | "Markdown + asistentes IA" + **pipeline local** (`tools/pipeline_local.sh`, **14 pasos** al 2026-07-09: **paso 0 = bootstrap de hooks git** + constitucion + **trazabilidad SDD** + ruff (lint+format) + `mypy --strict` + naming + `lint-imports` + **skills multi-tool (`gen_skill_adapters --check`)** + bandit + **pytest split unit/integration** + **dos gates de cobertura: src ≥80%, domain ≥96%**) + **git + pre-commit + CI** (GitHub Actions `ci.yml`, dispara **solo ante cambios de codigo** — `src/`,`tests/`,`tools/`,deps — **no** ante `docs/`/`specs/`/`historial/`; alineado local↔CI con Python 3.13 + mypy/streamlit pineados). Actualizado 2026-06-21: la deuda de entorno (`git init`/`pre-commit install`) quedo **saldada**. |
| Organizacion de specs | **Carpeta por feature** `specs/[###-feature]/` (invariante; `spec.md`+`plan.md`+`tasks.md`) + **rama por feature** (por defecto con git; degrada a dir-only sin git, numeracion secuencial o `--timestamp`) | **Registro central** `specs/SPECS_REGISTRY.md` por **capacidad** (`SPEC-NNN-slug`), agnostico a git/rama. Detalle: §1.1 |
| Formato de spec | Anatomia fija: User Story (P1/P2/P3) + `FR-NNN MUST` [R04] + `SC-NNN` + Given/When/Then + coverage mapping | **Casero** hasta SPEC-003; **hibrido** (adopta la anatomia de Spec Kit) desde SPEC-004; **estandar multi-HU propio** (cada HU encapsulada de inicio a fin + FR/SC prefijados `FR-US1-NNN`) formalizado en `docs/SPEC-FORMAT.md` |

### 1.1 Profundizacion: organizacion de specs — feature/rama vs. registro central

Los dos modelos optimizan ejes distintos. **Feature/rama** organiza por el **trabajo** (lo que se hace ahora); **registro central** organiza por el **sistema** (lo que el producto sabe hacer). Precision sobre Spec Kit (verificado en `create-new-feature.sh` v0.8.13 [R10]): el invariante es la **carpeta por feature** `specs/[###-feature]/`; la **rama** es el comportamiento por defecto **con git** (`HAS_GIT`) y degrada a solo-directorio sin git. La numeracion sale del maximo entre carpetas y ramas.

**Spec por feature/rama (Spec Kit)**

- Beneficios:
  - **Aislamiento y paralelismo**: cada feature es autocontenida (`spec`/`plan`/`tasks` juntos); trabajos distintos no tocan el mismo archivo → cero contencion.
  - **Mapea 1:1 con git/PR/CI**: una rama = una feature = un review; encaja en el flujo de entrega de software.
  - **Escala horizontal**: agregar feature = agregar carpeta, sin tocar lo existente; numeracion automatizada por el tooling.
  - **Contexto acotado** para el asistente IA: lee una carpeta, no un indice que crece sin techo.
  - **MVP incremental**: User Stories priorizadas (P1/P2/P3) empujan entrega por rebanadas.
- Desventajas:
  - **Sin vista global**: "que specs existen / cual es el SSOT de X / que esta activo" obliga a recorrer carpetas.
  - **Conflicto/duplicacion entre features ciego**: `/analyze` opera dentro de una feature; el solapamiento o contradiccion **entre** features no lo detecta nadie automaticamente.
  - **Cambios transversales sin hogar**: lo que cruza varias features (o toca el metodo) no encaja en "una feature".
  - **Ciclo de vida difuso**: las features cerradas se acumulan como carpetas; "spec viva"/deprecacion no tiene un lugar central.
  - **Deriva entre features invisible**: la reconciliacion spec↔codigo es por-feature.

**Registro centralizado (testigo)**

- Beneficios:
  - **Vista global de un vistazo**: el `SPECS_REGISTRY` muestra estado, formato, `ssot_level`, iteracion y dependencias `[[id]]` de todas las specs en una tabla.
  - **Deteccion de conflicto/duplicacion y propagacion SSOT nativas**: todo en un indice → la regla "cambio en SSOT → revisar derivados" tiene donde apoyarse.
  - **Hogar para specs vivas + anti-cascada**: *Deuda arrastrada* y reconciliacion cross-spec viven en el registry/historial (Eje 2, donde el testigo lidera).
  - **Agnostico a git/rama/asistente**: funciona en cualquier transporte; sostuvo al testigo antes de tener git y sigue valiendo con git.
  - **Capacidad estable**: el ID `SPEC-NNN-slug` sobrevive a las features; no se fragmenta en carpetas efimeras.
- Desventajas:
  - **Punto de contencion**: el registry es un solo archivo → trabajo concurrente = merge conflicts sobre el.
  - **Crece y pesa**: a mas specs, mas caro de leer (consume contexto) y mas facil que quede desactualizado vs. codigo.
  - **Menos aislamiento**: editar specs distintas igual toca el indice central.
  - **No mapea solo a branch/PR/CI**: necesita convencion anadida para "que spec estas tocando" → de ahi `.sdd/current-spec` (ver `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` §9.1).
  - **Tooling propio (fork)**: numeracion manual (riesgo de colision/reuso de IDs, ocurrido en el corte hibrido), sin mejora upstream automatica.

**Cuando gana cada uno.** Feature/rama: equipo grande y paralelo, flujo PR/CI maduro, features bien aisladas, prioridad en throughput. Centralizado: equipo chico, fuerte necesidad de consistencia/trazabilidad global, muchas capacidades que se referencian entre si, y cuando el riesgo principal es la cascada encubierta (`../comun/SDD-ADAPTATIVO-VS-CASCADA.md`).

**Sintesis del eje.** No son excluyentes: feature/rama optimiza **aislamiento y paralelismo**; el registro central optimiza **visibilidad y adaptatividad**. El testigo eligio centralizado y **compro de vuelta** lo que perdia: `.sdd/current-spec` recupera el "que estoy tocando ahora" que la rama daba gratis, sin fragmentar el indice. El costo que paga es la contencion sobre un archivo y el peso creciente del registry — aceptable en proyecto chico, problematico si escalara el equipo.

## 2. Artefactos

**Spec Kit** (generados por sus comandos): `memory/constitution.md`, `spec.md`, `plan.md`, `research.md`, `data-model.md`, `contracts/`, `tasks.md`, `checklist`; mas *presets* y *extensions* como mecanismo de adaptacion.

**Testigo** (artefactos reales en el repo, al 2026-07-09): `CONSTITUTION.md` (**v0.6.0, enmienda 2026-07-05** — suma el **Principio VI "SSOT unico por tema"**) + `tools/check_constitution.py`, `specs/SPECS_REGISTRY.md` + 17 specs `SPEC-NNN` (**14 activas + 3 en `draft`**: SPEC-009 ejecucion paralela, SPEC-011 agente bajo prueba, SPEC-012 evaluador de traduccion; **SPEC-013 seleccion de adaptador de cliente promovida draft→active tras implementarse 2026-07-03**) mas el indice `00-INDEX`, `docs/` (ARCHITECTURE + ADRs incl. **ADR-005** refactor de capas, PRODUCT, **SPEC-FORMAT**, AGENT-INVOCATION, DEVELOPMENT, CONTRIBUTING, SDD-ENFORCEMENT, **IDEAS** y **SKILLS-MULTITOOL**, + `docs/playbooks/` con el cuerpo neutro de analyze/clarify), **`historial/sdd.md`** con seccion *Deuda arrastrada*, `tools/` (check_constitution.py, check_naming.py, **`bootstrap_hooks.py`**, pipeline_local.sh de 14 pasos, `sdd_gate.py` multi-transporte, **`gen_skill_adapters.py`**, `check_traceability.py`, probes de diagnostico), adaptadores de asistente (`.agents/skills/`, `.claude/skills/`, `.opencode/command/` + `.opencode/plugin/sdd-gate.js`), `schemas/` (contrato del agente), `runs/` (detalle + estadistica datados), `tests/` (**271 funciones de test** en verde, split unit/integration con cobertura con umbral src ≥80% / domain ≥96%), codigo hexagonal (`domain/` con `metrics.py`/`agent_trace.py`, `adapters/` con **`SyncHttpAgentClient` + `AgentClientFactory`** (SPEC-013), `build/`, `dashboard/`, `runner.py`), `CLAUDE.md` + `AGENTS.md` (SSOT del protocolo).

Funcionalidad cubierta hoy: modo simple (un caso por pantalla — SPEC-001 — o desde archivo — SPEC-004), modo batch (headless `src/runner` + dashboard) con **parada manual de la corrida** que conserva los casos completados (SPEC-006 US3, 2026-06-01), persistencia de runs, metricas de suite (matriz de confusion 5x5 + accuracy por clase + % sin clasificacion), traza de ejecucion del agente — simple (SPEC-007) y por caso en batch (SPEC-010) — y, desde 2026-07-03, **seleccion de adaptador de cliente para plataformas alternativas** (SPEC-013): un `SyncHttpAgentClient` REST sincronico convive con el cliente async remoto detras del puerto `AgentClient`, elegido por `AGENT_CLIENT_TYPE` via `AgentClientFactory` — primer perfil de plataforma alternativo que valida empiricamente el diseno puertos/adaptadores (Principio II).

Diferencia clave: el testigo formaliza **artefactos de metodo que Spec Kit no tiene** — `historial/sdd.md` con *Deuda arrastrada* (mecanismo anti-cascada), `SPEC-FORMAT.md` (SSOT del propio metodo de escritura de specs) y, desde 2026-06-28, `docs/IDEAS.md` (SSOT de ideas **pre-spec**, con convencion de puntero: al promoverse a spec la entrada deja de re-describir alcance para no duplicar SSOT ni divergir — cubre el hueco de "hogar de ideas crudas" que en Spec Kit no tiene lugar central). A esto se suma la **portabilidad del metodo entre asistentes** instrumentada (no solo declarada): `docs/SKILLS-MULTITOOL.md` + `tools/gen_skill_adapters.py` generan los wrappers divergentes (`.claude/skills/`, `.opencode/command/`) desde la fuente unica `.agents/skills/`, con un gate `--check` anti-drift en el pipeline. Desde 2026-07-05 el metodo tambien **regula la compacidad de sus propias specs**: `SPEC-FORMAT.md` exige un bloque **Resumen ejecutivo** (3-4 lineas) al inicio de cada spec, adopta la "regla de mirada de usuario" en las User Stories y prescribe migracion **oportunistica** (al tocar una spec por otro motivo, no en una campana masiva). SPEC-013 es la referencia viva (−46% palabras sin cambio normativo). Esto materializa el nuevo **Principio VI ("SSOT unico por tema", constitucion v0.6.0)**, que extiende el *by-reference* hacia adentro de la spec: un detalle compartido por varios requisitos se declara una vez y se referencia, y los principios no se re-declaran como `FR` de cuerpo entero.

## 3. Funcionalidad

| Capacidad | Spec Kit | Testigo |
|---|---|---|
| Gate de autoridad | **Constitution Check** de contenido (todo conflicto con un principio MUST es CRITICAL) | `check_constitution.py`: **gate de *integridad***, no de contenido — verifica que cada principio referencia un SSOT existente y que su enforcement esta cableado en el pipeline |
| Validacion de consistencia | `/speckit.analyze` read-only: duplicacion, ambiguedad, gaps de cobertura, conflictos | Bloque **`[SDD-Check]`** por iteracion + checks post-generacion manuales |
| Circuito spec<-aprendizaje (feedback loop) | "Bidirectional Feedback" **declarado como principio** (`spec-driven.md`) pero **no instrumentado**: ningun comando ingiere senales de uso/produccion; el loop se cierra **re-ejecutando `specify`/`clarify`** con lo aprendido (humano-mediado) y la propia doc lo deja "a disciplina del equipo" | **Instrumentado**: campo `Deuda arrastrada` (re-explicitado hasta resolverse) + `historial/sdd.md` + specs vivas; B-06 verifico el circuito **activo** (specs ajustadas en horas, deuda nunca abandonada) |
| Manejo de ambiguedad | `[NEEDS CLARIFICATION]` + `/speckit.clarify` (<=5 preguntas) | `[NEEDS CLARIFICATION]` (adoptado de Spec Kit) + "MUST preguntar al usuario" |
| Coverage mapping | Nativo (FR/SC -> task IDs) | Adoptado en specs hibridas; obligatorio desde SPEC-004 |
| Ejecucion / enforcement | `/speckit.implement`; tests acoplados | `pipeline_local.sh` (14 pasos): bootstrap de hooks git + constitucion + trazabilidad SDD + ruff + `mypy --strict` + naming agnostico + `lint-imports` + gate anti-drift de skills + bandit + pytest unit/integration + cobertura con umbral (src ≥80% / domain ≥96%) |
| Alcance de agentes | 30+ agentes, instalacion uv/pipx/air-gapped, presets/extensions | 1 proyecto; verificacion funcional en **dashboard real** + probes e2e |

## 4. Beneficios

**Spec Kit**
- Metodo maduro, reutilizable y portable (30+ agentes, instalacion sencilla).
- Flujo end-to-end completo con **gates ejecutables** y `analyze` que automatiza la consistencia cruzada.
- Coverage mapping nativo; User Stories independientes empujan **MVP incremental**.
- Extensible sin tocar el tooling (presets/extensions).
- Apunta a **regenerabilidad** (spec -> codigo).

**Testigo**
- Ajustado a su contexto (equipo chico, **proveedor-agnostico**: el proveedor concreto vive aislado en `adapters/`) y **asistente-agnostico** (2026-06-21): el protocolo es SSOT unico en `AGENTS.md` con cuerpo neutro en `docs/playbooks/`; cada asistente IA (Claude, opencode, Cursor…) entra por un wrapper fino, sin reescribir el metodo. El gate `sdd_gate.py` es **multi-transporte** (argv/env/stdin) para servir a cualquier asistente y a pre-commit con el mismo veredicto. Al 2026-07-01 esa agnosticidad dejo de depender de wrappers a mano: (a) `gen_skill_adapters.py` **genera** los adaptadores divergentes desde `.agents/skills/` con `--check` anti-drift en el pipeline (verificado: Codex y Antigravity convergen al formato skill de Claude; opencode es el unico que sigue con *command* explicito); y (b) el gate preventivo de opencode quedo cableado como plugin (`.opencode/plugin/sdd-gate.js`), **verificado E2E en opencode real**, alcanzando paridad con el `PreToolUse` de Claude — cierra la deuda #1 de la universalizacion. El plugin evoluciono a **multi-tool y fail-closed** (2026-06-25): intercepta `edit`/`write`/`multiedit`/`apply_patch`, parsea cabeceras de patch estilo Codex, y **bloquea** si no logra ejecutar el gate (Python ausente o stub de la Store) en vez de permitir en silencio.
- **Specs vivas demostradas empiricamente** (B-06: circuito activo, specs ajustadas en horas, no congeladas).
- *Deuda arrastrada* previene la **cascada encubierta** (`../comun/SDD-ADAPTATIVO-VS-CASCADA.md`) — **instrumenta el feedback bidireccional que Spec Kit solo declara**: vuelve el pendiente un artefacto obligatorio en vez de dejarlo a disciplina.
- **Constitution-by-reference**: invariante en la constitucion, detalle en el SSOT -> evita duplicacion divergente; la constitucion **sobrevive a un cambio de agente**. Desde v0.6.0 (2026-07-05) el **Principio VI ("SSOT unico por tema")** eleva el *by-reference* a invariante general y lo extiende hacia adentro de las specs (un detalle compartido se declara una vez; los principios se citan con link, no se re-declaran como `FR`), instrumentado en `SPEC-FORMAT.md` + revision editorial + `docs/playbooks/analyze.md`.
- Pragmatismo: toma la anatomia de spec de Spec Kit **sin** su superficie operativa (CLI, branches por feature, 30+ integraciones).

## 5. Debilidades

**Spec Kit**
- Asume software con git/CI implicito; `specs/[###-feature]/` + branch automatico **no aporta** en contexto sin CI.
- Superficie operativa grande (CLI + 30+ integraciones) innecesaria para proyectos pequenos.
- Acoplamiento spec -> codigo -> tests con **costo/beneficio no medido** en equipos chicos (riesgo de fatiga de checklists).
- **Linea-B-nativo**: sin soporte para documentos de analisis/conocimiento.
- "Power Inversion" es una posicion fuerte **que no quedo validada** en este contexto: B-07 midio su componente de regenerabilidad (2026-07-28) y **no encontro ventaja** del formato hibrido — sin refutarla tampoco (ver `../experimentos/RESULTADO-EXPERIMENTO-B7.md`).
- **Feedback bidireccional declarado pero no instrumentado**: el circuito spec<-aprendizaje depende de la disciplina del equipo (re-ejecutar `specify`/`clarify`), no de un artefacto obligatorio. El riesgo de cascada encubierta queda contenido solo por habito, no por mecanismo (ver `../comun/SDD-ADAPTATIVO-VS-CASCADA.md`).

**Testigo**
- **Muestra minima** (1 proyecto, ~13 specs activas en semanas): evidencia indicativa, no generalizable.
- **Sesgo de confirmacion**: derivo su SDD de este mismo proyecto (declarado en B-06).
- Gobernanza casera: el check de constitucion valida integridad, **no** que el codigo respete los principios (eso queda en linter/tests/review).
- ~~Tooling manual sin CI -> deuda de entorno persistente: `pre-commit install` / `git init` pendientes.~~ **SALDADA (2026-06-21)**: el testigo adopto git, `pre-commit` (con hook `sdd-gate` acotado a `^src/`) y CI (GitHub Actions). La debilidad ahora es otra: la **superficie de adaptadores por ambiente** (wrappers `.claude/`+`.opencode/`+`.agents/`, plugin JS de opencode, tres transportes del gate) suma mantenimiento propio, a cambio de no atar el metodo a un solo asistente. Al 2026-06-28 esa superficie esta **parcialmente domada** por `gen_skill_adapters.py` (fuente unica + gate anti-drift), pero el generador mismo, el plugin y las rutas de Codex/Antigravity (tomadas de docs oficiales, aun sin validar contra instalacion real) son codigo propio a sostener.
- **Divergencia spec↔codigo latente, detectada por auditoria manual, no por gate.** La auditoria del 2026-07-01 (7 hallazgos) encontro que el puerto `CredentialProvider` existia en `src/domain/ports.py` (implementado por `TokenProvider`) y era citado por SPEC-011/013 como "puerto existente", pero **ninguna spec lo gobernaba** — hueco de trazabilidad (Principio V) que el `check_traceability` del pipeline no atrapo. Se reconcilio registrandolo en SPEC-002 (ahora SSOT de la interfaz del puerto `AgentClient`). Evidencia de que el Eje 2 (adaptatividad) del testigo funciona — el hueco se cerro en horas — pero tambien de que este tipo de divergencia (una entidad en el codigo sin spec que la gobierne, direccion **codigo→spec**) escapa a los **dos** motores automatizables del problema: ni el `check_traceability.py` del testigo (determinista y automatico en pipeline/CI, pero verifica spec→registro/tests — no recorre `src/` buscando entidades sin spec) ni el `/analyze` de Spec Kit (read-only, **a demanda**, compara spec/plan/tasks entre si **sin leer codigo** y solo dentro de una feature) lo detectan. Hoy requiere un barrido humano consciente del codigo en ambos metodos. Nota: `/analyze` no es "el gate automatico" — es un comando invocado por el agente; el equivalente automatico del testigo es `check_traceability`, cuyo punto ciego es justamente la direccion codigo→spec. _Actualizacion 2026-07-09 — secuencia exacta del cierre (SPEC-013):_ (1) **2026-06-25** se registra SPEC-013 en `draft` (`c60ac14`); (2) **2026-06-28→07-02** se refina el contrato sin codigo — firma `send` unificada (`b49bc99`), desacople de SPEC-011 adoptando `send(form: dict)` (`b62852b`), mapeo entrada/respuesta `FR-010/011` (`1d28897`), contrato sync transparente `FR-012` + manejo de fallos `FR-013` (`9fd3954`); (3) **2026-07-03** se implementa US1 en una sola tanda y en orden de dependencias — `PlatformConfig` lee `AGENT_CLIENT_TYPE` → `StaticCredentialProvider` → `SyncHttpAgentClient` → `AgentClientFactory` → composition roots (`9f89369`→`eb9cbc9`), y se cierra con `SC-004` confirmado → `active` (`30fde19`); (4) **2026-07-03** US2 (`endpoint_url` bajo test) + US3 (`get_trace` sintetiza la traza del pipeline sincrono) cerradas con prueba funcional OK (`0b7fede`); (5) **2026-07-05** reescritura compacta piloto (−46% palabras, sin cambio normativo, `d12e6f3`). Con esto el gobierno del puerto queda cubierto por SPEC-002 (interfaz `AgentClient`) + SPEC-013 (`AgentClientFactory`/`StaticCredentialProvider`) y el hueco puntual cierra; pero el **punto ciego metodologico** —una entidad en `src/` sin spec no la atrapa ningun motor automatico— **persiste** y sigue dependiendo de auditoria humana.
- Formato mixto (casero <=SPEC-003 + hibrido >=SPEC-004) -> inconsistencia transitoria entre specs, parcialmente mitigada al migrar SPEC-006 al estandar multi-HU.
- Divergencia spec<->codigo conocida: correlacion `run_id -> flow instance_id` sin verificar empiricamente (SPEC-007 FR-008), hoy resuelta por fallback de recencia; el aplanado de sub-flows (`children`) queda fuera de alcance.

---

## Sintesis

Spec Kit es el **estandar de referencia**: completo, ejecutable y portable, pero pesado y atado a software con CI. El testigo es una **adaptacion pragmatica viva** que conserva lo barato y valioso de Spec Kit (anatomia de spec, `[NEEDS CLARIFICATION]`, coverage mapping, gate de autoridad) y agrega lo que su contexto exige (anti-cascada via *Deuda arrastrada*, agnosticismo de proveedor **y de asistente IA**, gate de integridad liviano), al precio de ser un caso unico de baja generalizabilidad. Nota 2026-06-21: el testigo ya no opera "sin CI" — adopto git + CI + pre-commit; lo que distingue su via sigue siendo la gobernanza (registry central, anti-cascada, gates cableados) y, ahora, la **portabilidad del metodo entre asistentes** (SSOT `AGENTS.md` + adaptadores). El experimento **B-07** (`../experimentos/EXPERIMENTO-B7-formato-hibrido.md`) puso eso a prueba: al 2026-07-28 el aporte fuerte de Spec Kit — regenerar el codigo desde la spec — **no supero** al formato casero en este proyecto (`../experimentos/RESULTADO-EXPERIMENTO-B7.md`).

### Dos ejes independientes (evitar comparar en un solo eje)

> **Nota 2026-08-02.** Un tercer caso —Superpowers [R37]— no entra limpio en estos dos ejes: es débil en regenerabilidad y corre su circuito de feedback sobre los documentos de método, no sobre las specs. `CONVERGENCIA-IMPLEMENTACIONES-SDD.md` propone por eso un tercer eje (sobre qué objeto corre el aprendizaje). La síntesis pareada de abajo sigue válida para los dos casos que compara; no se reescribe.

La comparacion se aclara separando dos preguntas que suelen mezclarse (ver `../comun/SDD-ADAPTATIVO-VS-CASCADA.md`, "Aclaracion: invertir la jerarquia no es anticipar el conocimiento"):

- **Eje 1 — regenerabilidad** ("¿la spec genera el codigo?"): Spec Kit apuesta fuerte (Power Inversion, codigo regenerable); el testigo no regenera, reconcilia. Es el eje que midio **B-07**: cerrado el 2026-07-28 en "ajustar / no concluyente", **sin ventaja del hibrido** (ver `../experimentos/RESULTADO-EXPERIMENTO-B7.md`).
- **Eje 2 — adaptatividad** ("¿la spec se actualiza con lo aprendido?"): aqui el testigo va **mas lejos**, porque instrumenta el feedback (`Deuda arrastrada` + historial + specs vivas, B-06), mientras Spec Kit lo declara como principio pero lo deja a disciplina.

Los ejes son **ortogonales**: un SDD puede ser fuerte en regenerabilidad y debil en adaptatividad, o viceversa. Solo el Eje 2 determina el riesgo de cascada encubierta. Por eso "cual SDD es mejor" no tiene respuesta unica: Spec Kit lidera el Eje 1 **en el papel**, pero al medirlo en este contexto la ventaja no aparecio (B-07, 2026-07-28); el testigo lidera el Eje 2 (con evidencia de caso unico). La sintesis comparativa queda **saldada** sobre estos dos ejes; del Eje 1 ya hay datos de regenerabilidad — lo que sigue sin medirse es el **corpus observacional** de las secundarias (cobertura, ambiguedad temprana, fronteras, costo de redaccion).

---

[SDD-Check]
- Spec leida: SI (spec registrada en SPECS_REGISTRY.md para este doc; deriva de ANALISIS-SPEC-KIT.md)
- Incluye/Excluye verificado: SI (comparacion en 5 dimensiones; no re-analiza el flujo interno de Spec Kit ni anticipa resultados de B-07)
- Validaciones aplicadas: refs internas verificadas; afirmaciones externas ancladas en [R04][R10]; testigo caracterizado desde sus artefactos reales (CONSTITUTION, SPEC-FORMAT, SPECS_REGISTRY, pipeline_local.sh, check_constitution.py); sin emoticones; fechas YYYY-MM-DD; no duplica SSOT
- SSOT afectado: ninguno (doc derivado de ANALISIS-SPEC-KIT.md)
- Derivados a revisar: ninguno; SHOULD anadirse enlace desde software/00-INDEX.md (operativo)
- Cobertura: completa para las 5 dimensiones pedidas (implementacion, artefactos, funcionalidad, beneficios, debilidades)
- Deuda arrastrada: la dimension "regenerabilidad" (Power Inversion) sigue sin evidencia — depende de ejecutar B-07
- Riesgos/reservas: Spec Kit caracterizado desde el analisis interno (snapshot v0.8.13), no desde corrida en vivo; el testigo es estudio de caso con sesgo de confirmacion declarado (B-06)

---

[SDD-Check] — actualizacion 2026-05-28
- Spec leida: SI (spec en SPECS_REGISTRY.md reconciliada: se quito "aclaracion de categorias" del `incluye` antes de borrarla del doc)
- Incluye/Excluye verificado: SI (se elimino la seccion "Aclaracion previa" a pedido del usuario; se actualizaron datos del testigo al 2026-05-28; el enfoque comparativo se retomara despues)
- Validaciones aplicadas: estado del testigo tomado de su `historial/sdd.md` real (hasta 2026-05-28: 14 specs, 207 tests, pipeline 8/8, traza simple+batch, matriz de confusion, estandar multi-HU); el bloqueo del placeholder de SPEC-002 figura resuelto; refs internas y [R04][R10] intactas; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: ninguno (doc derivado); spec del propio doc actualizada en SPECS_REGISTRY.md
- Derivados a revisar: ninguno
- Cobertura: completa para lo pedido (borrar aclaracion + actualizar info del testigo); la sintesis comparativa queda pendiente de retomar
- Deuda arrastrada: retomar la comparacion/sintesis con el usuario; B-07 (regenerabilidad / Power Inversion) sigue sin evidencia empirica
- Riesgos/reservas: estado del testigo verificado por historial, no por corrida en vivo en esta sesion

---

[SDD-Check] — actualizacion 2026-05-28 (precision spec/CI)
- Spec leida: SI (sin cambio de incluye/excluye; correccion cae en "tabla comparativa por dimension")
- Incluye/Excluye verificado: SI (se corrigieron dos celdas de la tabla 1: "Tesis sobre la spec" y "Motor del flujo")
- Validaciones aplicadas: redaccion verificada contra artefactos reales del testigo — `tools/pipeline_local.sh` (8 pasos, invocacion manual `bash tools/pipeline_local.sh`) y `historial/sdd.md` (`pre-commit install`/cableado del hook a git pendiente); se reemplazo "el codigo se edita a mano" (impreciso: el codigo lo genera el asistente IA) por "no se regenera desde la spec; se mantiene y la spec se reconcilia"; se reemplazo "sin CI" por "pipeline local invocado manualmente, sin CI remoto disparado por git"
- SSOT afectado: ninguno (doc derivado); las demas menciones de "sin CI" (beneficios/debilidades/sintesis) quedan consistentes con la aclaracion de la celda "Motor del flujo"
- Derivados a revisar: ninguno
- Cobertura: completa para lo pedido (correccion de las dos celdas)
- Deuda arrastrada: B-07 (regenerabilidad / Power Inversion) sigue sin evidencia empirica; retomar la sintesis comparativa con el usuario
- Riesgos/reservas: pipeline del testigo verificado por lectura de `pipeline_local.sh`, no ejecutado en vivo en esta sesion

---

[SDD-Check] — actualizacion 2026-05-28 (incorporacion de hallazgos + saldo de sintesis)
- Spec leida: SI (SPECS_REGISTRY.md: la incorporacion cae en "tabla comparativa por dimension" + "sintesis de la relacion entre ambos y su conexion con B-06/B-07")
- Incluye/Excluye verificado: SI — se añadio fila "Circuito spec<-aprendizaje" a la tabla 3 (Funcionalidad), un punto en Debilidades de Spec Kit, refuerzo en Beneficios del testigo y una subseccion "Dos ejes independientes" en la Sintesis; no se re-analiza el flujo interno de Spec Kit ni se anticipan resultados de B-07
- Validaciones aplicadas: feedback de Spec Kit anclado en fuente real (`spec-driven.md` L57 principio / L63 "discipline"; comandos specify/clarify/analyze) [R10]; instrumentacion del testigo anclada en CLAUDE.md (Deuda arrastrada) y RESULTADO-EXPERIMENTO-B6.md; ortogonalidad remitida a ../comun/SDD-ADAPTATIVO-VS-CASCADA.md (SSOT); refs [R04][R10] intactas; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: ninguno (doc derivado de ANALISIS-SPEC-KIT.md); coherente con la subseccion nueva de ../comun/SDD-ADAPTATIVO-VS-CASCADA.md actualizada esta sesion
- Derivados a revisar: ninguno; SHOULD enlazar desde software/00-INDEX.md (operativo, pendiente)
- Cobertura: completa — los 3 hallazgos de la sesion incorporados; la deuda "retomar la sintesis comparativa" queda SALDADA sobre dos ejes (regenerabilidad / adaptatividad)
- Deuda arrastrada: Eje 1 (regenerabilidad / Power Inversion) sigue sin evidencia empirica — depende de ejecutar B-07; enlace desde software/00-INDEX.md pendiente
- Riesgos/reservas: Spec Kit caracterizado sobre snapshot v0.8.13 (no corrida en vivo); testigo es estudio de caso con sesgo de confirmacion declarado (B-06)

---

[SDD-Check] — actualizacion 2026-06-01 (cierre de deuda de enlace)
- Spec leida: SI (sin cambio de incluye/excluye)
- Incluye/Excluye verificado: SI (solo se salda deuda de proceso arrastrada en bloques previos)
- Validaciones aplicadas: verificado que el enlace a este doc YA existe en `software/00-INDEX.md` (seccion "Analisis de frameworks")
- SSOT afectado: ninguno (doc derivado)
- Derivados a revisar: ninguno
- Cobertura: completa
- Deuda arrastrada: RESUELTA — "enlazar desde software/00-INDEX.md", arrastrada en los bloques del 2026-05-28, esta cerrada (el enlace existe). El Eje 1 (regenerabilidad / Power Inversion) sigue sin evidencia: depende de ejecutar B-07
- Riesgos/reservas: ninguna nueva

---

[SDD-Check] — actualizacion 2026-06-01 (datos del testigo)
- Spec leida: SI (sin cambio de incluye/excluye; "caracteriza al testigo desde sus artefactos reales")
- Incluye/Excluye verificado: SI (solo se refrescan datos del testigo en seccion 2 y debilidades; no se re-analiza el flujo de Spec Kit ni se anticipa B-07)
- Validaciones aplicadas: estado tomado del testigo real al 2026-06-01 — `specs/SPECS_REGISTRY.md` (14 specs SPEC-NNN: 13 activas incl. SPEC-002b/003b hibridas, SPEC-009 draft; + 00-INDEX), `historial/sdd.md` (Iter 2026-06-01: SPEC-006 US3 parada manual batch; pipeline verde con 209 tests; `check_constitution` OK), ausencia de `.git` confirmada (pre-commit/git init siguen pendientes); refs [R04][R10] intactas; fechas YYYY-MM-DD
- SSOT afectado: ninguno (doc derivado de ANALISIS-SPEC-KIT.md)
- Derivados a revisar: ninguno
- Cobertura: completa — actualizados nº de tests (207→209), specs nuevas (002b/003b), SPEC-006 US3, y precision de la deuda de entorno (lint-imports ya integrado; persiste pre-commit/git init)
- Deuda arrastrada: Eje 1 (regenerabilidad / Power Inversion) sigue sin evidencia empirica — depende de ejecutar B-07
- Riesgos/reservas: estado del testigo verificado por su `SPECS_REGISTRY.md` + `historial/sdd.md` y listado de archivos, no por corrida en vivo del dashboard en esta sesion

---

[SDD-Check] — actualizacion 2026-06-21 (premisa SDD universal + adopcion git/CI; rename del testigo)
- Spec leida: SI (sin cambio de incluye/excluye; cae en "tabla comparativa por dimension" + "caracteriza al testigo desde sus artefactos reales")
- Incluye/Excluye verificado: SI (se corrigen hechos en present-tense que quedaron falsos; no se re-analiza el flujo interno de Spec Kit ni se anticipan resultados de B-07)
- Validaciones aplicadas: estado tomado del testigo real al 2026-06-21 — `git log` (16 commits, ultimo `f29c77a` "universaliza el SDD para cualquier asistente IA"); `AGENTS.md` (SSOT del protocolo; `CLAUDE.md`->`@AGENTS.md`); `docs/playbooks/{analyze,clarify}.md` (cuerpo neutro) + wrappers `.claude/skills/` y `.opencode/command/`; `tools/sdd_gate.py` multi-transporte (argv/env/stdin) + hook pre-commit `sdd-gate` (`^src/`); `.github/workflows/ci.yml` (dispara solo ante codigo, no docs/specs/historial); `tools/pipeline_local.sh` 9 pasos (sumo "trazabilidad SDD"); 204 funciones de test; `CONSTITUTION.md` v0.5.2 (enmienda 2026-06-13); refs [R04][R10] intactas; fechas YYYY-MM-DD
- Cambios concretos: (1) rename `agent-test-suite`->`evaluador-flujo-intent` en titulo/header/path; (2) celda "Motor del flujo": pipeline 8->9 pasos + git/CI/pre-commit, deuda de entorno saldada; (3) beneficio testigo: agnosticismo extendido proveedor->proveedor+asistente (SSOT AGENTS.md, playbooks neutros, gate multi-transporte); (4) debilidad "deuda de entorno sin CI" marcada SALDADA y reemplazada por "superficie de adaptadores por ambiente"; (5) sintesis: se quito "sin CI" y se agrego portabilidad del metodo entre asistentes
- SSOT afectado: ninguno (doc derivado de ANALISIS-SPEC-KIT.md); el `proposito` del registry para este doc nombra al testigo `agent-test-suite` -> actualizado a `evaluador-flujo-intent` en `SPECS_REGISTRY.md` (misma sesion)
- Derivados a revisar: `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` (constante "el testigo hoy no es git" + §9 "sin git no hay pre-commit" + paths) — actualizado en la misma sesion; `experimentos/EXPERIMENTO-B7-formato-hibrido.md` (rename + specs nuevas, sin cambiar la metrica primaria)
- Cobertura: completa para la reconciliacion de premisa y la adopcion git/CI; el Eje 1 (B-07) queda fuera de alcance (no es lo pedido)
- Deuda arrastrada: Eje 1 (regenerabilidad / Power Inversion) sigue SIN evidencia empirica — B-07 no concluible; umbral de exito aun `[NEEDS CLARIFICATION]`
- Riesgos/reservas: estado del testigo verificado por git/artefactos en disco, no por corrida en vivo; la universalizacion es reciente (commit del 2026-06-21) y aun no probada en un asistente distinto de Claude en este analisis

---

[SDD-Check] — actualizacion 2026-06-21 (profundizacion del eje "organizacion de specs")
- Spec leida: SI (incluye "tabla comparativa por dimension"; la nueva §1.1 profundiza la fila "Organizacion de specs" de la dimension 1, no agrega una dimension nueva ni re-analiza el flujo interno de Spec Kit)
- Incluye/Excluye verificado: SI (no duplica las 5 dimensiones — expande una fila ya existente; no anticipa resultados de B-07; el detalle de `.sdd/current-spec` se referencia a DECISION §9.1, no se copia)
- Validaciones aplicadas: modelo Spec Kit verificado en codigo real `fuentes-externas/spec-kit/scripts/bash/create-new-feature.sh` v0.8.13 [R10] — invariante = carpeta por feature, rama condicional a `HAS_GIT` (degrada sin git, numeracion secuencial/`--timestamp`); se corrigio la celda "Organizacion de specs" (antes "branch git automatico", impreciso) a "carpeta por feature (invariante) + rama por defecto con git"; modelo testigo desde `SPECS_REGISTRY.md`; sin emoticones; fechas YYYY-MM-DD; lenguaje normativo
- SSOT afectado: ninguno (doc derivado de ANALISIS-SPEC-KIT.md)
- Derivados a revisar: ninguno
- Cobertura: completa para lo pedido (beneficios vs desventajas de ambos modelos de organizacion + condiciones de aplicabilidad + sintesis del eje)
- Deuda arrastrada: Eje 1 (regenerabilidad / B-07) sigue sin evidencia empirica — no afectado por esta entrega
- Riesgos/reservas: Spec Kit caracterizado sobre snapshot v0.8.13 vendored, no corrida en vivo

---

[SDD-Check] — actualizacion 2026-07-01 (hallazgos del testigo desde 2026-06-21 hasta hoy)
- Spec leida: SI (SPECS_REGISTRY.md, spec de este doc; la actualizacion cae en "caracteriza al testigo desde sus artefactos reales" de las dimensiones 2/4/5; no re-analiza el flujo interno de Spec Kit ni anticipa B-07)
- Incluye/Excluye verificado: SI — se refrescan §2 (artefactos), §4 (beneficios) y §5 (debilidades) con los 8 commits nuevos del testigo (`9e1abd1`..`5fbb04a`); no se agrega dimension nueva ni se duplica el catalogo de frameworks
- Validaciones aplicadas: estado tomado del testigo real al 2026-07-01 — `git log` (HEAD `5fbb04a`, 24 commits), `specs/SPECS_REGISTRY.md` (17 specs SPEC-NNN: 13 activas + 4 draft incl. la nueva SPEC-013), `historial/sdd.md` (entradas 2026-06-21 gate opencode, 2026-06-28 skills multi-asistente, 2026-07-01 auditoria de 7 hallazgos), `docs/{IDEAS,SKILLS-MULTITOOL,SDD-ENFORCEMENT}.md`, `tools/gen_skill_adapters.py`, `.opencode/plugin/sdd-gate.js`, `CONSTITUTION.md` v0.5.2, 204 funciones de test; refs [R04][R10] intactas; sin emoticones; fechas YYYY-MM-DD
- Cambios concretos: (1) §2: CONSTITUTION v1.0.0→v0.5.2, 14→17 specs (+SPEC-011/012/013 draft), artefactos nuevos (IDEAS, SKILLS-MULTITOOL, gen_skill_adapters, playbooks, plugin opencode), 209→204 funciones de test; (2) "Diferencia clave": IDEAS.md como tercer artefacto de metodo + portabilidad entre asistentes instrumentada; (3) §4: agnosticismo de asistente ahora generado (anti-drift) + gate opencode E2E multi-tool/fail-closed; (4) §5: superficie de adaptadores "parcialmente domada" + nueva debilidad de divergencia spec↔codigo detectada por auditoria manual (puerto `CredentialProvider` huerfano de spec)
- SSOT afectado: ninguno (doc derivado de ANALISIS-SPEC-KIT.md)
- Derivados a revisar: `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` — revisado en esta sesion: su "~13 specs" (activas) y el reencuadre git/`.sdd/current-spec` (§9.1, 2026-06-21) siguen vigentes, no requiere cambio. `experimentos/EXPERIMENTO-B7-formato-hibrido.md` — su corpus experimental esta **congelado** (control SPEC-001/002/003 vs. tratamiento SPEC-004/005/006/008), NO incorpora SPEC-013; lo relevante es su metrica secundaria *divergencia spec↔codigo*, que gana un nuevo dato con el puerto `CredentialProvider` huerfano hallado en la auditoria del 2026-07-01 (SHOULD registrarse alli como incidencia, junto al caso SPEC-002↔003 del baseline)
- Cobertura: completa para lo pedido (registrar hallazgos y mejoras del testigo del periodo 2026-06-21→2026-07-01); el hallazgo de la auditoria del testigo (puerto huerfano) queda como debilidad/observacion, sin proponer accion sobre el testigo (fuera de alcance de este analisis)
- Deuda arrastrada: Eje 1 (regenerabilidad / Power Inversion) sigue SIN evidencia empirica — depende de ejecutar B-07; validar paridad del metodo en un asistente distinto de Claude (opencode) mas alla del gate sigue pendiente
- Riesgos/reservas: estado del testigo verificado por git/artefactos en disco, no por corrida en vivo del dashboard ni de opencode en esta sesion

---

[SDD-Check] — actualizacion 2026-07-09 (hallazgos del testigo 2026-07-01→2026-07-09)
- Spec leida: SI (SPECS_REGISTRY.md, spec de este doc; la actualizacion cae en "caracteriza al testigo desde sus artefactos reales" de las dimensiones 1/2/3/4/5; no re-analiza el flujo interno de Spec Kit ni anticipa B-07)
- Incluye/Excluye verificado: SI — se refresca el estado real del testigo (~40 commits nuevos, `5fbb04a`..`8bff08c`); no se agrega dimension nueva ni se duplica el catalogo de frameworks
- Validaciones aplicadas: estado tomado del testigo real al 2026-07-09 — `git log` (HEAD `8bff08c`, 64 commits), `CONSTITUTION.md` **v0.6.0** (Principio VI, enmienda 2026-07-05), `specs/SPECS_REGISTRY.md` (14 activas + 3 draft; SPEC-013 `active` impl.2026-07-03), `docs/SPEC-FORMAT.md` (compacidad + Resumen ejecutivo + regla de mirada de usuario), `tools/pipeline_local.sh` (**14 pasos** verificados por lectura: bootstrap hooks, skills `--check`, pytest unit/integration, cobertura src ≥80% / domain ≥96%), **271** funciones de test contadas en `tests/`; secuencia SPEC-013 anclada en commits datados (`c60ac14`..`d12e6f3`); refs [R04][R10] intactas; sin emoticones; fechas YYYY-MM-DD
- Cambios concretos: (1) header HEAD `5fbb04a`/24→`8bff08c`/64, fecha 2026-07-09; (2) celda "Motor del flujo": 9→14 pasos + cobertura con umbral + Python 3.13/pins; (3) §2 artefactos: CONSTITUTION v0.5.2→v0.6.0+Principio VI, 204→271 tests, SPEC-013 draft→active, ADR-005, `bootstrap_hooks.py`, adaptadores `SyncHttpAgentClient`/`AgentClientFactory`; (4) funcionalidad cubierta +SPEC-013 (perfil de plataforma alternativa sync); (5) "Diferencia clave" +compacidad de specs + Principio VI; (6) §3 tabla enforcement 14 pasos; (7) §4 constitution-by-reference +Principio VI; (8) §5 debilidad puerto huerfano: secuencia exacta del cierre SPEC-013 + punto ciego metodologico que persiste
- SSOT afectado: ninguno (doc derivado de ANALISIS-SPEC-KIT.md)
- Derivados a revisar: `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` — actualizado en esta misma sesion (§9/§9.1: pipeline 14 pasos, cobertura con umbral, SPEC-013 como adaptador implementado). `experimentos/EXPERIMENTO-B7-formato-hibrido.md` — corpus congelado, NO incorpora SPEC-013; propuesta de nota (metrica secundaria divergencia spec↔codigo) mostrada al usuario para aprobacion antes de editar
- Cobertura: completa para lo pedido (incorporar novedades del testigo 2026-07-01→2026-07-09 a Linea B)
- Deuda arrastrada: Eje 1 (regenerabilidad / Power Inversion) sigue SIN evidencia empirica — B-07 no concluible; umbral de exito aun `[NEEDS CLARIFICATION]`; nota B-07 sobre puerto huerfano pendiente de aprobacion del usuario
- Riesgos/reservas: estado del testigo verificado por git/artefactos en disco y lectura de `pipeline_local.sh`, no por corrida en vivo del pipeline ni del dashboard en esta sesion

---

[SDD-Check] — sincronizacion 2026-07-29 (cierre de B-07 propagado)
- Spec leida: SI (SPECS_REGISTRY.md, spec de este doc). El `excluye` "resultados de B-07" se conserva: aqui se **referencia** el resultado, no se copia. Ese mismo `excluye` se corrigio en el registry, que justificaba la exclusion con "(aun no ejecutado)" — premisa hoy falsa; la exclusion sigue vigente por la regla de no duplicar SSOT.
- Incluye/Excluye verificado: SI — no se agrega dimension nueva, no se re-analiza el flujo interno de Spec Kit, no se transcriben metricas de B-07
- Validaciones aplicadas: se corrigieron **solo afirmaciones de cuerpo en presente** (§debilidades Spec Kit, §sintesis, §dos ejes x2); los bloques `[SDD-Check]` datados 2026-05-28→2026-07-09 quedan **intactos** como registro de su fecha, coherente con la nota de premisa del encabezado y con la regla anti-cascada de B-06 (la deuda se re-explicita hacia adelante, no se reescribe hacia atras); refs [R04][R10] intactas; sin emoticones; fechas YYYY-MM-DD
- Cambios concretos: (1) header +"sincronizado con el cierre de B-07"; (2) §sintesis: B-07 pasa de "decidira con datos" a "puso a prueba — no supero"; (3) §debilidades Spec Kit: "hoy 0% implementado" → medido sin ventaja; (4) §Eje 1: "hoy sin evidencia" → cerrado 2026-07-28; (5) §ortogonalidad: lo pendiente de datos ya no es el Eje 1 sino el corpus observacional de las secundarias
- SSOT afectado: ninguno por este doc (derivado de ANALISIS-SPEC-KIT.md). En la misma tanda se corrigio `software/LINEAS-INVESTIGACION.md` (SSOT de agenda linea B), que habia quedado **atras de su propio derivado** `PLAN-PRUEBAS.md`
- Derivados a revisar: `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` — sincronizado en esta misma tanda (§9.3 nueva, cierra el paso 5 de §8)
- Cobertura: completa para la sincronizacion — las 4 afirmaciones de estado en presente de este doc quedan corregidas y referenciadas al resultado
- Deuda arrastrada: reformular el **Criterio de exito** de `../experimentos/EXPERIMENTO-B7-formato-hibrido.md` (SSOT; resulto no evaluable, requiere decision del usuario); el **corpus observacional** de las secundarias de B7 sigue sin medirse; propuestas 3 y 4 del marco sin aplicar
- Riesgos/reservas: el resultado de B-07 es `n = 1` por celda con formato confundido con procedencia en F013 — este doc lo refleja como "no aparecio la ventaja", que **no** equivale a "el hibrido es peor"; leerlo asi seria sobre-interpretar

---

[SDD-Check] — cierre de deuda declarada (2026-07-29)
- Spec leida: SI (SPECS_REGISTRY.md; este doc es derivado de `ANALISIS-SPEC-KIT.md`)
- Incluye/Excluye verificado: SI — no cambia contenido comparativo; sólo cierra la deuda que el bloque anterior dejó explícita
- Validaciones aplicadas: verificado en el SSOT `../experimentos/EXPERIMENTO-B7-formato-hibrido.md` §Criterio de exito que la reformulación está redactada y pasa la comprobación de satisfacibilidad
- SSOT afectado: ninguno por este doc
- Derivados a revisar: ninguno
- Cobertura: completa para el cierre de esta deuda
- Deuda arrastrada: **CERRADA** — reformular el Criterio de exito de B-07: hecho el 2026-07-29, separado en (a) prueba de regenerabilidad contra `R1`–`R6` y (b) corpus observacional contra `H1`+`H3`, con regla de cierre a dos veredictos. **SIGUE ABIERTA** — el **corpus observacional** de las secundarias (`H1`, `H3`, costo) no se midio; `H2` fue degradada a descriptiva el 2026-07-29 y ya no integra criterio. La dimension "regenerabilidad" **ya tiene evidencia** (`../experimentos/RESULTADO-EXPERIMENTO-B7.md`): los bloques `[SDD-Check]` previos de este doc que la declaran "sin evidencia" son registro datado y MUST NOT reescribirse.
- Riesgos/reservas: el criterio (a) se redacto conociendo los resultados de la prueba ya cerrada; gobierna replicas y no reabre el veredicto (reserva declarada en el SSOT)

```text
[SDD-Check]  (2026-07-31 — cierre integral de B-07)
- Spec leida: SI
- Incluye/Excluye verificado: SI
- Validaciones aplicadas: los bloques anteriores de este documento son registro datado y NO se reescribieron; el cierre de deuda se anota agregando este bloque, segun templates/RESULTADO-EXPERIMENTO.md §Propagacion
- SSOT afectado: ninguno
- Derivados a revisar: ninguno
- Cobertura: completa para el cierre de esta deuda
- Deuda arrastrada: **CERRADA** — el corpus observacional de las secundarias se midio el 2026-07-31. `H1` (cobertura) **NO CONCLUYENTE**: su direccion depende de la convencion de conteo (la anatomia propia de cada formato favorece al hibrido, la unidad neutral lo desfavorece, y los dos extractores coinciden dentro de cada variante) y el piso de ruido del instrumento resulto de 5 a 8 veces la brecha entre brazos. `H3` (fronteras) **no consistente con la hipotesis** en los tres ejes, robusto al leave-one-out. Costo de redaccion: el hibrido cuesta ~64% mas palabras por spec en la mediana, cualitativo y sin umbral. B-07 cierra con dos veredictos y decision **AJUSTAR**. Detalle: `../experimentos/RESULTADO-EXPERIMENTO-B7.md` §Resultado del criterio (b)
- Riesgos/reservas: techo de conclusion **descriptivo** — el formato esta confundido con tiempo, madurez de repo, feature y presencia del gate check_traceability.py; `H3` perdio su compuerta de validacion de instrumento y tiene un modo de fallo comun (`src/dashboard/app.py`, citado por las 4 specs hibridas y 1 de las 3 caseras) que no se descarto
```
