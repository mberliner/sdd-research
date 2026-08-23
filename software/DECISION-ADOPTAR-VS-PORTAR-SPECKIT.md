# Decision: adoptar Spec Kit (A) vs. portar /clarify+/analyze + hook (B)

Fecha: 2026-06-06.
Fuentes: GitHub Spec Kit v0.8.13 (consultada 2026-05-21) [R10]; clone vendored en `../fuentes-externas/spec-kit/`; artefactos reales del testigo `evaluador-flujo-intent` (ex `agent-test-suite`; `../../../test_circuito_intents/evaluador-flujo-intent/`).
Alcance: Linea B (software). Via B confirmada y ejecutada en el testigo (2026-06-06; ver seccion 9). Actualizado 2026-06-21: ver §9.1 — el testigo adopto git+CI y universalizo el SDD a cualquier asistente IA, lo que corrige dos supuestos de este doc. Actualizado 2026-07-09: ver §9.2 — pipeline 9→14 pasos con bootstrap de hooks auto-reparable + cobertura con umbral, constitucion v0.6.0 (Principio VI), y SPEC-013 (primer adaptador de plataforma alternativa) implementada. Actualizado 2026-07-29: ver §9.3 — **cierra el paso 5 de §8**, B-07 (Eje 1, regenerabilidad) medido y cerrado el 2026-07-28. Actualizado 2026-07-31: **B-07 cerrado integralmente** — su corpus observacional se midio y el criterio (b) quedo resuelto (`H1` NO CONCLUYENTE, `H3` no consistente con la hipotesis). La decision de B-07 es **AJUSTAR**, coherente con la via B ya confirmada en este doc: las convenciones de Spec Kit en uso se conservan **por su valor de metodo, no por evidencia medida de superioridad**, y asi MUST enunciarse. Ver `../experimentos/b07-formato-hibrido/RESULTADO-EXPERIMENTO-B7.md` §Resultado del criterio (b).

Este documento es **decisorio** (que hacer), no descriptivo (como son ambos). La caracterizacion de Spec Kit vs. el testigo en cinco dimensiones vive en `COMPARATIVA-SPECKIT-VS-TESTIGO.md` y aqui se **referencia, no se repite**.

---

## 1. Decision a tomar

El testigo ya practica un SDD maduro pero le falta la pieza que Spec Kit resuelve mejor: **deteccion activa de specs/US/FR faltantes** antes de codear (`/clarify`, `/analyze`). La pregunta es por que via incorporarla:

- **A — Adoptar Spec Kit**: instalar el toolkit (`specify init`) y migrar la gobernanza del testigo a su estructura.
- **B — Portar e instrumentar**: portar `/clarify`+`/analyze` al formato `SPEC-NNN` del testigo y sumar un **hook de enforcement determinista** que Spec Kit no provee.

La decision habilita el siguiente paso de la Linea B: integrar deteccion de cobertura sin perder la gobernanza ya construida.

## 2. Las dos vias

- **A — Adoptar Spec Kit**: `specify init` instala slash commands (integracion nativa de Claude Code en `src/specify_cli/integrations/claude/`), scripts de orquestacion (`create-new-feature.sh`, `setup-plan.sh`, `setup-tasks.sh`, `check-prerequisites.sh`) y el pipeline completo `constitution -> specify -> clarify -> checklist -> plan -> tasks -> analyze -> implement`. Requiere reubicar `CONSTITUTION.md`, las specs y el registry a su layout por feature.
- **B — Portar e instrumentar**: adaptar los prompts de `/clarify` y `/analyze` a la estructura `specs/SPEC-NNN-slug` + `SPECS_REGISTRY.md` del testigo, y agregar un hook `PreToolUse` que bloquee la edicion de `src/` sin spec vigente declarada.

## 3. Constantes (igual en A y B)

Dos hechos aplican a ambas vias y por eso se sacan de la comparacion:

- **El hook determinista es net-new en ambas.** Spec Kit **no** lo trae. Sus "hooks" (`.specify/extensions.yml`, claves `hooks.before_analyze`/`hooks.after_clarify`) son **encadenamiento de prompts cooperativo** que ejecuta el agente leyendo el prompt: advisory y salteable, no un interlock determinista a nivel sistema. El gate duro es aporte propio se elija A o B.
- **El testigo (al 2026-06-06) no era git.** Los scripts de Spec Kit asumen **branch-por-feature** (`create-new-feature.sh` crea rama y directorio por feature). Adoptar A arrastra ese supuesto. _Actualizacion 2026-06-21:_ el testigo **ya adopto git + CI + pre-commit** (ver §9.1); esto **no revierte** la decision B —los scripts de Spec Kit siguen imponiendo branch-y-directorio **por feature**, incompatible con el registry central por capacidad— pero **invalida el argumento "sin git"** como motivo. La eleccion de B se sostiene ahora por el **fit con la gobernanza central**, no por ausencia de git.

## 4. Hallazgo que mueve la aguja

El formato de spec de ambos es **casi identico**: User Story con `Priority`/`Why`/`Independent Test`, `Acceptance Scenarios` Given/When/Then, `FR-###` MUST [R04], `Key Entities`, `SC-###` medibles, `Assumptions`. El testigo adopto esa anatomia desde SPEC-004 (formato hibrido; ver `COMPARATIVA-SPECKIT-VS-TESTIGO.md`, tabla 1).

Consecuencia: el costo no esta en el **formato** sino en el **layout y la orquestacion**. Eso **abarata B** (el port de `/clarify` es casi directo) y **des-riesga el contenido de A** (las specs no hay que reescribirlas, solo reubicarlas y partirlas en `spec.md`/`plan.md`/`tasks.md`).

## 5. Comparacion por criterios

| Criterio | A — Adoptar Spec Kit | B — Portar + hook |
|---|---|---|
| Funcionalidad | Pipeline completo (8 comandos) + extensiones + 30+ agentes, mantenido upstream. Da **mas** que clarify+analyze. | Solo lo portado (realista: clarify + analyze). El resto es manual, uno por uno. |
| Esfuerzo one-time | Install trivial, pero **migracion** de ~13 specs + constitucion + registry al layout por feature (split `spec`/`plan`/`tasks`, `memory/constitution.md`). **Medio-alto.** | Adaptar 2 prompts a paths/secciones `SPEC-NNN` + sustituto de `check-prerequisites` + re-target de `/analyze` FR->tests. Sin migrar specs. **Bajo-medio.** |
| Esfuerzo ongoing | Bajo: upstream mantiene prompts/plantillas; se hace pull. Pero se mantiene el mapeo/divergencia. | Propio para siempre: fork de los prompts, sin mejoras upstream automaticas (drift). |
| Fit con el repo | **Forzado.** Duplica o pelea con gobernanza que Spec Kit no tiene (registry vigente, `check_naming`, `lint-imports`, pipeline, `[SDD-Check]`, anti-cascada *Deuda arrastrada*). | **Excelente.** Se atornilla a lo existente, cero reestructura. |
| Riesgo | Mayor radio: reestructura, lock-in a convenciones de Spec Kit, dos sistemas SDD solapados. | Menor radio. Riesgo = calidad del port (perder matices) + drift respecto a upstream. |
| Mantenimiento | GitHub mantiene los prompts; se actualiza por pull. Se mantiene la migracion y la divergencia local. | Se mantiene el fork de prompts; no llega mejora upstream sola. |
| Valor para la demo SDD | "Asi se hace SDD con tooling estandar de industria." | "SDD propio con dientes (hook determinista) que Spec Kit no tiene." |

Nota: `/analyze` en A funciona as-is porque consume `tasks.md`; en B requiere el unico re-targeteo sustancial — mapear **FR -> tests** en vez de FR -> tasks, porque el testigo usa tests + Coverage mapping como equivalente de `tasks.md`.

## 6. Dimension nueva: enforcement determinista (el hook)

Ningun doc previo cubre esto. La `COMPARATIVA` distingue el **gate de contenido** de Spec Kit (Constitution Check: conflicto con principio MUST es CRITICAL) del **gate de integridad** del testigo (`check_constitution.py`: verifica que cada principio referencia un SSOT y que su enforcement esta cableado), pero **ninguno de los dos previene** codear sin spec — solo lo detectan a posteriori.

- **Que aporta el hook**: un `PreToolUse` que dispara **antes** de que un `Edit`/`Write` toque `src/`. Es el unico punto del flujo anterior a que el codigo exista. Verifica que haya una spec vigente declarada para el cambio; si no, **bloquea la edicion** y obliga a crear la spec primero.
- **Por que es net-new**: como se dijo en la seccion 3, los "hooks" de Spec Kit son encadenamiento de prompts (salteable), y `/analyze` es STRICTLY READ-ONLY (reporta, no bloquea). El interlock duro no existe en ninguno.
- **Limite honesto**: el hook verifica **presencia** de spec, no **adecuacion**. Detectar que un cambio introduce un requisito nuevo sin FR sigue necesitando juicio — lo aporta el skill (`/analyze`/`/clarify`, probabilistico) y, en ultima instancia, la revision humana. El hook hace **obligatorio** correr ese juicio; no lo reemplaza.
- **Tie-back concreto**: el cambio de `run_id` del testigo (unicidad multiusuario) introdujo un requisito **sin FR** y se colo code-first, aun tocando SPEC-005. Un check de "cambio toca una spec" lo habria dejado pasar; `/clarify` —cuyo taxonomy incluye "Identity & uniqueness rules" y "Conflict resolution (concurrent edits)"— probablemente lo habria detectado en tiempo de spec, y el hook habria forzado a correrlo.

Esto refuerza el **Eje 2 (adaptatividad)** donde el testigo ya lidera (ver `COMPARATIVA-SPECKIT-VS-TESTIGO.md`, "Dos ejes independientes"): el hook convierte la deteccion de cobertura de un paso *recomendado* en uno *no-salteable*.

## 7. Recomendacion (condicionada)

- SHOULD — elegir **B** para la realidad actual del testigo. El proyecto ya es un Spec Kit hecho a mano con piezas que Spec Kit no tiene (registry, gates cableados, anti-cascada); migrar a A haria **perder o duplicar** esa gobernanza para ganar dos prompts que se portan barato, y el aporte diferencial (el hook) se construye igual en ambas vias.
- SHOULD — complementar B con una **via hibrida**: dejar el clone vendored como **fuente de cosecha** y traer a mano las mejoras upstream de los prompts cuando aparezcan, sin pagar la migracion.
- MAY — elegir **A** solo si el objetivo cambia a **estandarizar SDD a nivel organizacion** sobre una herramienta mantenida externamente, o a onboardear gente que ya usa Spec Kit. En ese escenario, el costo de migracion se justifica por uniformidad y soporte upstream.

## 8. Consecuencias y proximos pasos

Si se confirma B:

1. MUST — portar los prompts de `/clarify` y `/analyze` adaptados a la estructura `SPEC-NNN` + `SPECS_REGISTRY.md`, como skills del proyecto.
2. MUST — re-targetear `/analyze` para mapear `FR-###`/`SC-###` contra **tests** y el Coverage mapping, en lugar de `tasks.md`.
3. MUST — cablear el hook `PreToolUse` sobre `Edit|Write` con matcher `src/**`, apoyado en un check determinista en `tools/` que valide spec vigente declarada.
4. SHOULD — repuntar el enforcement del Principio V (trazabilidad) del testigo hacia ese check, dejandolo a la par de los principios I/II/III (hoy apunta a un doc).
5. SHOULD — registrar el resultado como evidencia del Eje 2 y conectarlo con B-07 (Eje 1, regenerabilidad). **Ejecutado 2026-07-28**: ver §9.3.

## 9. Estado de implementacion (via B ejecutada en el testigo, 2026-06-06)

La recomendacion B se ejecuto en el sujeto testigo. Esto cierra empiricamente los pasos 1-4 de la seccion 8 y aporta evidencia del **Eje 2 (adaptatividad/enforcement)**. Fuentes: `agent-test-suite/historial/sdd.md` (entradas 2026-06-06) y `agent-test-suite/docs/SDD-ENFORCEMENT.md`.

**Enforcement de tres capas construido** (defensa en profundidad; ninguna capa sola alcanza):

| Capa | Artefacto en el testigo | Momento | Determinista |
|---|---|---|---|
| Hook de autoria | `tools/sdd_gate.py` (`PreToolUse`, matcher `Edit`/`Write`) | antes de tocar `src/` | Si |
| Backstop de pipeline | `tools/check_traceability.py` (step "trazabilidad SDD") | en `pipeline_local.sh` | Si |
| Deteccion semantica | skills `/clarify` y `/analyze` (`.claude/commands/`) | a pedido, en redaccion | No (LLM) |

El hook es el unico punto **anterior** a que el codigo exista (sin git no hay `pre-commit`); el check corre sobre todo el repo pero a posteriori; las skills aportan el juicio de adecuacion que ningun script da. El hook **obliga** a correr ese juicio, no lo reemplaza.

**Sustituto git-less de "rama por feature": `.sdd/current-spec`.** Como el testigo no usa git (constante de seccion 3), el gate no puede apoyarse en branch-por-feature. El sustituto es un archivo `.sdd/current-spec` en la raiz que declara la `SPEC-NNN` vigente; el hook valida que exista en `specs/` y este registrada en `SPECS_REGISTRY.md` antes de permitir editar `src/`. Patron reutilizable para repos sin git.

**Enmienda constitucional (Principio V), bifasica.** El testigo subio el Principio V de aspiracion a regla de admision: `0.4.0` (texto — "un cambio de comportamiento sin spec vigente no se integra" + distincion producto/framework: los cambios al propio metodo SDD no van como `SPEC-NNN`, se rigen por la constitucion y `docs/`) y `0.5.0` (repunte del `Enforcement:` al check + hook, dejando el Principio V a la par de I/II/III). Verificacion: pipeline 9/9, 226 tests.

**Evidencia — el gate determinista atrapo una deriva real.** Al habilitar `check_traceability.py`, el check afloro que SPEC-007 declaraba `FR-012` **sin fila en su Coverage mapping** (feature implementada, tabla incompleta), reconciliado en el acto. Confirma que el backstop captura divergencia spec↔codigo que el ojo dejo pasar; complementa el caso `run_id` de la seccion 6 (miss code-first que el hook habria forzado a frenar).

**Limite reconfirmado (presencia, no adecuacion).** El testigo formalizo el limite honesto de la seccion 6 en su SSOT de metodo `docs/SDD-ENFORCEMENT.md`: ni hook ni check juzgan si la spec **describe bien** el cambio; ese juicio queda en `/analyze`/`/clarify` y en la revision humana.

**Lo que cierra de la seccion 8:** pasos 1-4 ejecutados. El paso 5 (conectar con B-07, Eje 1 regenerabilidad) estaba abierto al momento de esta seccion; **se cerro el 2026-07-28** — ver §9.3.

## 9.1 Actualizacion 2026-06-21 (premisa: SDD universal primero, adaptadores por ambiente despues)

El testigo se reorganizo sobre una premisa explicita: **el SDD se especifica una sola vez de forma universal y despues se adapta a cada ambiente**, en lugar de atarlo a un asistente. Esto corrige dos supuestos de este doc (la "constante" git de §3 y el encuadre git-less de §9) y refina —no revierte— la recomendacion B. Fuentes: `git log` del testigo (commit `f29c77a`, 2026-06-21) y sus artefactos en disco.

**Cambios de fondo en el testigo:**

| Antes (≤2026-06-06) | Ahora (2026-06-21) |
|---|---|
| Sin git; el hook `PreToolUse` era el unico punto pre-codigo | **git + CI** (GitHub Actions `ci.yml`, dispara solo ante codigo, no docs/specs) + **pre-commit** con hook `sdd-gate` |
| Protocolo del agente acoplado a `CLAUDE.md` (Claude-only) | **`AGENTS.md` = SSOT universal** del protocolo (opencode/Cursor/Codex/Aider/Gemini lo leen por convencion; Claude via `@AGENTS.md`) |
| Skills `/clarify` `/analyze` en `.claude/commands/` | **Cuerpo semantico neutro en `docs/playbooks/`** + wrappers finos por asistente (`.claude/skills/`, `.opencode/command/`) |
| `sdd_gate.py` invocado como hook de Claude | `sdd_gate.py` **multi-transporte** (argv/env/stdin): mismo veredicto desde el hook de Claude, otro asistente o pre-commit |

**Lectura sobre la decision A vs B:**

- La capa universal del testigo (`AGENTS.md` + `docs/playbooks/` + gate multi-transporte) es **exactamente la generalizacion** que la via B insinuaba: portar la deteccion de cobertura sin atarla al tooling de un proveedor. B no solo se sostiene: **se profundizo** hacia portabilidad entre asistentes, algo que A (Spec Kit, hoy con integracion nativa por-asistente en `src/specify_cli/integrations/`) resuelve por instalacion per-agente, no por SSOT unico neutro.
- El sustituto git-less `.sdd/current-spec` (§9) **persiste** aunque ya haya git: sigue cumpliendo "declarar la SPEC vigente" para el hook `PreToolUse`, que corre **antes** del commit (pre-commit/CI son posteriores). El reencuadre correcto: `.sdd/current-spec` no es "para repos sin git" sino **"para el momento de autoria, anterior a git"**; el gate ahora tiene **tres momentos** (autoria via hook, commit via pre-commit `sdd-gate`, push/PR via CI).
- La "constante 2" de §3 ("el testigo hoy no es git") queda **historica**: valida al 2026-06-06, falsa hoy. El argumento que movia a B no era la ausencia de git sino el **fit con el registry central por capacidad** (incompatible con el branch-por-feature de los scripts de Spec Kit); ese argumento intacto.

**Lo que NO cambia:** al 2026-06-21 la metrica PRIMARIA de B-07 (regenerabilidad desde spec) seguia sin medirse y el paso 5 de la seccion 8 continuaba abierto (**se cerro despues, el 2026-07-28** — §9.3). La universalizacion es del **Eje 2** (adaptatividad/portabilidad del enforcement), no del Eje 1.

## 9.2 Actualizacion 2026-07-09 (maduracion del motor + primer adaptador de plataforma implementado)

Desde el corte del 2026-07-01 el testigo avanzo ~40 commits (`5fbb04a`..`8bff08c`, 64 en total). Tres cambios tocan directamente la decision B. Fuentes: `git log` del testigo, `CONSTITUTION.md` v0.6.0, `tools/pipeline_local.sh`, `specs/SPECS_REGISTRY.md`.

1. **El pipeline crecio de 9 a 14 pasos y cerro la ultima deuda de entorno.** El **paso 0 es ahora `bootstrap_hooks.py`**: el propio pipeline instala los hooks git si faltan, de modo que la capa de commit del enforcement (pre-commit `sdd-gate`) ya no depende de un `pre-commit install` manual — el argumento de "deuda de entorno" que §9.1 declaro saldado queda ademas **auto-reparable**. Se sumaron un gate anti-drift de skills (`gen_skill_adapters --check`), el split `pytest unit`/`integration` como gates y **dos gates de cobertura** (src ≥80%, domain ≥96%), con CI alineado local↔CI (Python 3.13 + mypy/streamlit pineados). El enforcement de tres capas de §9 no cambia de forma; gana robustez operativa.

2. **Constitucion v0.6.0 — Principio VI "SSOT unico por tema".** Eleva el *constitution-by-reference* a invariante general y lo extiende hacia adentro de las specs. No altera la recomendacion B, pero refuerza su premisa: el metodo se sostiene en referencias a SSOTs unicos, no en duplicacion — exactamente lo que hace portable el enforcement entre asistentes (§9.1).

3. **SPEC-013 implementada y `active` (2026-07-03): la via B especificando una capacidad nueva de punta a punta.** Primer **perfil de plataforma alternativa** — `SyncHttpAgentClient` (REST sincronico) junto al cliente async remoto, detras del puerto `AgentClient`, elegido por `AGENT_CLIENT_TYPE` via `AgentClientFactory`. Relevante para esta decision por dos motivos: (a) es evidencia de que la gobernanza central por capacidad (registry + `.sdd/current-spec` + gate) **escala a una feature nueva sin el layout por-feature de Spec Kit**; (b) cierra el puerto `CredentialProvider` que la auditoria del 2026-07-01 hallo huerfano de spec — la interfaz queda gobernada por SPEC-002 + SPEC-013. Persiste, eso si, el **punto ciego** ya documentado: una entidad en `src/` sin spec no la atrapa `check_traceability` (direccion codigo→spec); sigue requiriendo auditoria humana.

**Lo que NO cambia:** al 2026-07-09 el paso 5 de la seccion 8 (Eje 1, regenerabilidad de B-07) seguia sin medirse (**se cerro el 2026-07-28** — §9.3). Todo lo de arriba es Eje 2 (adaptatividad/enforcement).

## 9.3 Cierre del paso 5 — B-07 medido (2026-07-28)

El paso 5 de §8 queda **cerrado**. La componente de regenerabilidad de B-07 se ejecuto completa (diseno 2x2 balanceado por traduccion, 4 celdas, metricas R1-R5) y cerro en **"ajustar / no concluyente"**. Fuente: `../experimentos/b07-formato-hibrido/RESULTADO-EXPERIMENTO-B7.md`; runbook `../experimentos/b07-formato-hibrido/PRUEBA-REGENERABILIDAD-B7.md`.

**Que dio.** En la unica feature que discrimino (F013) el formato **casero** supero al hibrido en R1, R2 y R5; F001 empato en las cinco metricas. H4 **no queda sostenida, sin ser refutada**, con dos reservas que el propio resultado declara: en F013 el eje formato esta **confundido** con el eje spec autentica/traducida, y **una sola ronda de reparacion borra la diferencia** (las 4 celdas llegan a 100%). `n = 1` por celda: no es afirmacion estadistica.

**Que significa para esta decision.** Nada la revierte. La via B se eligio por **fit con el registry central por capacidad**, no por una apuesta a la regenerabilidad; el resultado retira el unico argumento pendiente que podia haber inclinado la balanza hacia A —"Spec Kit regenera mejor"— al no encontrar esa ventaja en este contexto. La recomendacion B queda **reforzada por ausencia de contraevidencia**, no por evidencia positiva a su favor: son cosas distintas y conviene no confundirlas.

**Lo que sigue abierto.** El **corpus observacional** de las metricas secundarias de B7 (cobertura requisito->derivado, ~~ambiguedad temprana~~ —**degradada a descriptiva el 2026-07-29**, ver `../experimentos/b07-formato-hibrido/EXPERIMENTO-B7-formato-hibrido.md` §Hipotesis H2: su ratio no es computable y su variable de salida esta confundida con el tratamiento—, fronteras, costo de redaccion, specs vivas) **no se midio**: las preguntas 2 y 3 de `LINEAS-INVESTIGACION.md` §B7 siguen sin datos. Y el **Criterio de exito** de `../experimentos/b07-formato-hibrido/EXPERIMENTO-B7-formato-hibrido.md` resulto no evaluable; su reformulacion requiere decision del usuario.

## 10. Referencias internas

Referencia, no copia:

- `COMPARATIVA-SPECKIT-VS-TESTIGO.md` — comparacion descriptiva en 5 dimensiones y los dos ejes (regenerabilidad / adaptatividad).
- `ANALISIS-SPEC-KIT.md` — SSOT del flujo interno de Spec Kit (comandos y artefactos).
- `../comun/SDD-ADAPTATIVO-VS-CASCADA.md` — anti-patron cascada encubierta y circuitos de aprendizaje (sustenta el valor del enforcement no-salteable).

---

[SDD-Check]
- Spec leida: SI (spec minima propuesta y registrada en SPECS_REGISTRY.md para este doc; deriva de COMPARATIVA-SPECKIT-VS-TESTIGO.md)
- Incluye/Excluye verificado: SI (decision A/B + esfuerzo/ventajas/desventajas + dimension del hook; NO re-comparacion de 5 dimensiones ni re-analisis del flujo interno de Spec Kit ni resultados de B-07)
- Validaciones aplicadas: no duplica las 5 dimensiones (referencia COMPARATIVA); version de Spec Kit anclada en [R10]; cada via con esfuerzo + ventajas + desventajas; recomendacion condicionada (cuando A / cuando B); caracterizacion de Spec Kit desde el clone vendored y de [R10]; testigo desde sus artefactos reales; sin emoticones; fechas YYYY-MM-DD; lenguaje normativo MUST/SHOULD/MAY
- SSOT afectado: ninguno (doc derivado de COMPARATIVA-SPECKIT-VS-TESTIGO.md)
- Derivados a revisar: ninguno; se agrega enlace desde software/00-INDEX.md (operativo)
- Cobertura: completa para lo pedido (tabla comparativa A vs B en seccion 5 + dimension del hook + recomendacion)
- Deuda arrastrada: el port de /clarify+/analyze, el hook PreToolUse y el repunte del Principio V se IMPLEMENTARON en el testigo (2026-06-06, ver seccion 9); resta el paso 5 de la seccion 8 — Eje 1 (B-07, regenerabilidad) sigue sin evidencia
- Riesgos/reservas: Spec Kit caracterizado sobre snapshot v0.8.13 (clone vendored), no corrida en vivo; la recomendacion B asume que el objetivo sigue siendo el proyecto unico testigo, no estandarizacion organizacional

---

[SDD-Check] — actualizacion 2026-06-21 (premisa SDD universal + git/CI; rename del testigo)
- Spec leida: SI (incluye/excluye sin cambio; las correcciones caen en "definicion de las dos vias" y "consecuencias accionables"; la §9.1 extiende el estado de implementacion sin re-comparar 5 dimensiones ni re-analizar Spec Kit)
- Incluye/Excluye verificado: SI (no se duplican las 5 dimensiones — se referencia COMPARATIVA; no se anticipan resultados de B-07)
- Validaciones aplicadas: estado del testigo al 2026-06-21 verificado en disco — `git log` (commit `f29c77a` universalizacion), `AGENTS.md` (SSOT protocolo), `docs/playbooks/` + wrappers `.claude/skills/`/`.opencode/command/`, `tools/sdd_gate.py` multi-transporte, `.pre-commit-config.yaml` (hook `sdd-gate` `^src/`), `.github/workflows/ci.yml`; refs [R10] intactas; fechas YYYY-MM-DD; lenguaje normativo MUST/SHOULD/MAY
- Cambios concretos: (1) rename `agent-test-suite`->`evaluador-flujo-intent` (header/paths); (2) §3 constante 2 marcada historica — "no es git" valido al 2026-06-06, falso hoy; argumento de B re-anclado en fit con registry central, no en ausencia de git; (3) nueva §9.1 con la premisa "universal primero, adaptadores despues", tabla antes/ahora, reencuadre de `.sdd/current-spec` (momento de autoria, no "repos sin git") y los tres momentos del gate (autoria/commit/CI)
- SSOT afectado: ninguno (doc derivado de COMPARATIVA); `proposito` del registry actualizado al nuevo nombre del testigo en `SPECS_REGISTRY.md` (misma sesion)
- Derivados a revisar: ninguno aguas abajo de DECISION; COMPARATIVA actualizada en paralelo (misma sesion); EXPERIMENTO-B7 anotado (rename + specs nuevas)
- Cobertura: completa para la reconciliacion pedida (premisa universal + git/CI); el Eje 1 (B-07) fuera de alcance
- Deuda arrastrada: paso 5 de §8 (conectar con B-07, regenerabilidad) sigue ABIERTO; metrica primaria sin medir; umbral `[NEEDS CLARIFICATION]`
- Riesgos/reservas: universalizacion reciente (2026-06-21), aun no ejercitada en un asistente distinto de Claude dentro de este analisis; verificada por artefactos en disco, no por corrida multi-asistente

---

[SDD-Check] — actualizacion 2026-07-09 (maduracion del motor + SPEC-013 implementada)
- Spec leida: SI (incluye/excluye sin cambio; la nueva §9.2 extiende el "estado de implementacion" — dimension propia de este doc — sin re-comparar las 5 dimensiones ni re-analizar el flujo de Spec Kit)
- Incluye/Excluye verificado: SI (no duplica COMPARATIVA — referencia; no anticipa resultados de B-07)
- Validaciones aplicadas: estado del testigo al 2026-07-09 verificado en disco — `git log` (HEAD `8bff08c`, 64 commits; secuencia SPEC-013 `c60ac14`..`d12e6f3`), `CONSTITUTION.md` v0.6.0 (Principio VI), `tools/pipeline_local.sh` (14 pasos, paso 0 = `bootstrap_hooks.py`, cobertura con umbral src ≥80%/domain ≥96%), `specs/SPECS_REGISTRY.md` (SPEC-013 `active` impl.2026-07-03); refs [R10] intactas; fechas YYYY-MM-DD; lenguaje normativo
- Cambios concretos: (1) header +linea "Actualizado 2026-07-09"; (2) nueva §9.2 con los tres cambios que tocan la decision B — pipeline 9→14 con bootstrap auto-reparable (deuda de entorno ahora auto-reparable), Principio VI, SPEC-013 como via B especificando una capacidad nueva end-to-end y cerrando el puerto huerfano
- SSOT afectado: ninguno (doc derivado de COMPARATIVA, actualizada en paralelo esta misma sesion)
- Derivados a revisar: EXPERIMENTO-B7 — corpus congelado, propuesta de nota sobre puerto huerfano pendiente de aprobacion del usuario (no editado aun)
- Cobertura: completa para lo pedido (incorporar maduracion del motor + primer adaptador implementado)
- Deuda arrastrada: paso 5 de §8 (Eje 1 / regenerabilidad de B-07) sigue ABIERTO; metrica primaria sin medir; umbral `[NEEDS CLARIFICATION]`; nota B-07 pendiente de aprobacion
- Riesgos/reservas: verificado por git/artefactos en disco y lectura de `pipeline_local.sh`, no por corrida en vivo del pipeline en esta sesion

---

[SDD-Check] — sincronizacion 2026-07-29 (cierre del paso 5 de §8: B-07 medido)
- Spec leida: SI (SPECS_REGISTRY.md, spec de este doc). El `excluye` "resultados de B-07" se conserva: §9.3 **referencia** el resultado y su consecuencia decisoria, no transcribe el analisis. Ese `excluye` se corrigio en el registry, que lo justificaba con "(aun no ejecutado)" — premisa hoy falsa; la exclusion sigue vigente por la regla de no duplicar SSOT.
- Incluye/Excluye verificado: SI — §9.3 cae en "consecuencias accionables" y "estado de implementacion", dimensiones propias de este doc; no re-compara las 5 dimensiones (viven en COMPARATIVA) ni re-analiza el flujo de Spec Kit
- Validaciones aplicadas: se corrigieron **solo afirmaciones de cuerpo en presente** (§8 paso 5, §9, §9.1, §9.2), re-fechandolas en vez de borrarlas para que se lea que eran ciertas a su fecha; los bloques `[SDD-Check]` datados quedan **intactos** como registro (regla anti-cascada de B-06: la deuda se re-explicita hacia adelante, no se reescribe hacia atras); refs [R10] intactas; fechas YYYY-MM-DD; lenguaje normativo
- Cambios concretos: (1) header +"Actualizado 2026-07-29 → §9.3"; (2) §8 paso 5: "sigue sin evidencia" → "Ejecutado 2026-07-28"; (3) §9, §9.1, §9.2: las tres frases "sigue sin medirse" pasan a pasado con puntero a §9.3; (4) **§9.3 nueva**: que dio B-07, que significa para la decision, y que sigue abierto
- SSOT afectado: ninguno por este doc (derivado de COMPARATIVA, sincronizada en la misma tanda). En la misma tanda se corrigio `software/LINEAS-INVESTIGACION.md` (SSOT de agenda linea B), que habia quedado **atras de su propio derivado** `PLAN-PRUEBAS.md`
- Derivados a revisar: ninguno — este doc no tiene derivados registrados
- Cobertura: completa — las 4 afirmaciones de estado en presente quedan corregidas y el paso 5 de §8, que era la unica deuda estructural de este doc, queda cerrado con seccion propia
- Deuda arrastrada: reformular el **Criterio de exito** de `../experimentos/b07-formato-hibrido/EXPERIMENTO-B7-formato-hibrido.md` (SSOT; no evaluable, requiere decision del usuario); el **corpus observacional** de las secundarias de B7 sigue sin medirse; el umbral `[NEEDS CLARIFICATION]` arrastrado desde 2026-07-09 queda **absorbido** por esa reformulacion; propuestas 3 y 4 del marco sin aplicar
- Riesgos/reservas: §9.3 afirma que la via B queda reforzada **por ausencia de contraevidencia**, no por evidencia a favor — la distincion es deliberada y no debe colapsarse al citarla. El resultado es `n = 1` por celda con formato confundido con procedencia en F013.

---

[SDD-Check] — cierre de deuda declarada (2026-07-29)
- Spec leida: SI (SPECS_REGISTRY.md; este doc es derivado de `COMPARATIVA-SPECKIT-VS-TESTIGO.md`)
- Incluye/Excluye verificado: SI — no cambia la decision adoptar-vs-portar ni §9.x; sólo cierra la deuda que el bloque anterior dejó explícita, más la nota fechada de H2 en §"Lo que sigue abierto"
- Validaciones aplicadas: verificado en el SSOT `../experimentos/b07-formato-hibrido/EXPERIMENTO-B7-formato-hibrido.md` §Criterio de exito que la reformulación está redactada, y en §Hipotesis que `H2` quedó degradada a descriptiva
- SSOT afectado: ninguno por este doc
- Derivados a revisar: ninguno — este doc no tiene derivados registrados
- Cobertura: completa para el cierre de esta deuda
- Deuda arrastrada: **CERRADA** — reformular el Criterio de exito de B-07 (hecho 2026-07-29: (a) contra `R1`–`R6`, (b) contra `H1`+`H3`, regla de cierre a dos veredictos). **SIGUE ABIERTA** — el corpus observacional de las secundarias de B7 (`H1`, `H3`, costo de redaccion, specs vivas) no se midio, luego las preguntas 2 y 3 de `LINEAS-INVESTIGACION.md` §B7 siguen sin datos; `H2` ya no cuenta como secundaria puntuable.
- Riesgos/reservas: el criterio (a) se redacto conociendo los resultados de la prueba ya cerrada; gobierna replicas y no reabre el veredicto
