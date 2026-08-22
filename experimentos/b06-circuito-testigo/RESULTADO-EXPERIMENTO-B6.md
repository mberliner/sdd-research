# Resultado Experimento B-06: Circuito de aprendizaje en el proyecto testigo

## Metadata
- ID experimento: B-06
- Fecha cierre: 2026-05-24
- Responsable: proyecto SDD (analisis)
- Sujeto: `agent-test-suite` (proyecto testigo, ver `../../software/PLAN-PRUEBAS.md`)
- Corte de datos: estado del testigo al 2026-05-24 (specs/, SPECS_REGISTRY.md, historial/sdd.md)

> **Nota (2026-06-01):** al corte, `../../comun/SDD-ADAPTATIVO-VS-CASCADA.md` usaba un umbral de inactividad de **30 dias absolutos**. El hallazgo 3 de abajo motivo su reformulacion a un criterio **relativo** (2-3 iteraciones), aplicada despues (ver Fase 3 en `../../historial/sdd.md`). Las menciones a "30 dias" reflejan el umbral vigente al corte.

## Resultado cuantitativo

### Inventario al corte
- Specs `active`: 5 — `SPEC-000-naming`, `SPEC-000-bootstrap`, `SPEC-001`, `SPEC-002`, `SPEC-003`.
- Specs `draft` con archivo: 1 — `SPEC-007` (creada 2026-05-24).
- Specs `draft` planeadas sin archivo: 3 — `SPEC-004`, `SPEC-005`, `SPEC-006`.

### Metrica primaria: specs `active` revisadas tras ejecucion/verificacion
Dos lecturas (se reportan ambas por rigor):

- **Estricta** (revision del propio archivo de la spec, posterior a su creacion, disparada por ejecucion): 2/5 = **40%**.
  - `SPEC-002`: "revisada 2026-05-23 tras verificacion e2e" (archivo modificado 2026-05-23 17:54). Disparador: verificacion end-to-end.
  - `SPEC-000-naming`: revisada en Iter 2 para añadir `json` a "Identificadores permitidos" al implementar el cliente (`requests.Response.json()`).
- **Amplia** (spec moldeada por una observacion de ejecucion, aunque la edicion ocurra al redactarla): 3/5 = **60%**.
  - Añade `SPEC-003`: absorbio el caso "indeterminado" tras el smoke de Iter 2, que revelo que el agente responde "flow has started" en vez de clasificar (entrada historial "Iter 2 follow-up").

### Metricas secundarias
- **Antiguedad de drafts vs. umbral 30 dias** (`../../comun/SDD-ADAPTATIVO-VS-CASCADA.md`): ningun draft supera 30 dias. NO INFORMATIVO: el proyecto tiene ~2-3 dias (Iter 0-3 todas el 2026-05-22). El umbral absoluto no discrimina a esta velocidad.
- **Tasa de resolucion/re-explicitacion de deuda arrastrada**: la deuda se re-explicita en las 4 iteraciones, nunca se abandona en silencio.
  - Resuelta: smoke real (Iter 2 follow-up, el usuario lo corrio), integracion del adapter al dashboard (Iter 3).
  - Persistente pero transparente: `mypy --strict`, `lint-imports`, `pre-commit install` — arrastradas Iter 0→1→2→3 por falta de instalacion en el entorno, re-declaradas cada vez.
- **Presencia de bloque `[SDD-Check]`**: 100% de las iteraciones (0,1,2,3) + bloques en pivot y snapshot de cierre.
- **Divergencia spec<->codigo (muestreo)**: `SPEC-002` describe recuperacion async del resultado via historial de thread, pero el e2e real esta BLOQUEADO (agente devuelve placeholder; streaming probe sin ejecutar). La brecha esta documentada como deuda e hipotesis vigentes — divergencia explicita, no oculta.

## Resultado cualitativo

### Hallazgos
1. **Circuito de aprendizaje ACTIVO (caso positivo).** La evidencia cualitativa es contundente: las specs se ajustan a la ejecucion en horas, no se congelan. Casos: SPEC-002 (e2e→revision), SPEC-000-naming (implementacion→allowlist), SPEC-003 (observacion de runtime→semantica "indeterminado"), y el "Pivot post-Iter-0" que reordeno todo el registry tras una aclaracion del usuario.
2. **Anti-cascada por transparencia de deuda.** El mecanismo "Deuda arrastrada" del `historial/sdd.md` del testigo es el instrumento que mas claramente previene la cascada encubierta: hace explicito lo diferido en cada cierre de iteracion y lo re-declara hasta resolverlo. Nuestro marco no tiene este artefacto formalizado.
3. **El umbral de 30 dias es inadecuado para proyectos de alta velocidad.** El testigo itera en horas; un umbral absoluto de 30 dias nunca se gatillaria aunque hubiera congelamiento. Confirma empiricamente la nota de `../../comun/SDD-ADAPTATIVO-VS-CASCADA.md`: "la cadencia correcta es una variable del proyecto, no un estandar fijo".
4. **Distincion deuda de producto vs. deuda de tooling.** La de producto (funcionalidad/scope) se resuelve rapido; la de entorno (mypy/lint-imports/pre-commit) persiste — transparente, pero acumulandose. Es una señal de alarma leve, no una cascada.

### Incidentes
- El sujeto derivo su SDD de este proyecto (sesgo de confirmacion declarado en el diseño). Los hallazgos descriptivos (que paso) son solidos; los interpretativos (por que) deben leerse con esa reserva.
- Muestra minima (5 specs activas, 1 proyecto, 3 dias). Estudio de caso, NO evidencia generalizable.

## Decision
- **Ajustar.** La hipotesis B6 queda SOSTENIDA en este caso (circuito activo). El experimento no justifica cambios al marco por si solo (muestra minima), pero arroja dos mejoras candidatas claras al marco SDD propio, a evaluar con el usuario.

## Cambios al marco SDD (propuestas, NO aplicadas)
1. **Formalizar "Deuda arrastrada" como artefacto del marco.** Incorporar una seccion de deuda explicita por iteracion en `templates/RESULTADO-EXPERIMENTO.md` y/o en el bloque `[SDD-Check]`, espejando la practica del testigo. Decision que habilita: prevenir abandono silencioso de pendientes (anti-cascada).
2. **Reformular el umbral de cascada como relativo a la velocidad del proyecto.** Reemplazar "30 dias absolutos" en `../../comun/SDD-ADAPTATIVO-VS-CASCADA.md` (SSOT) por un criterio relativo (ej. N iteraciones sin tocar una spec activa, o multiplo de la cadencia de iteracion observada). Es un cambio a un SSOT → requiere revisar derivados y aprobacion del usuario.

## Evidencia adjunta
- `historial/sdd.md` del testigo: Iter 0, Pivot post-Iter-0, Iter 1, Iter 2, Iter 2 follow-up (smoke real), Iter 3, snapshot de cierre.
- `specs/SPEC-002-agent-client.md`: cabecera "Iter 2 (revisada 2026-05-23 tras verificacion e2e)".
- Fechas de archivo: `SPEC-002` 2026-05-23 17:54; resto 2026-05-22; `SPEC-007` 2026-05-24.

## Deuda arrastrada
<!-- Pendientes diferidos al cerrar. MUST re-explicitarse en el siguiente cierre hasta resolverse (anti-cascada). Marcar cada item como nuevo | arrastrado | resuelto. -->
- [nuevo, al cierre 2026-05-24] Decision del usuario sobre las dos propuestas de "Cambios al marco SDD" (Deuda arrastrada como artefacto; umbral de cascada relativo). **[RESUELTO 2026-06-01: ambas aprobadas y aplicadas — ver Fase 3 en `../../historial/sdd.md`.]**
- [nuevo, al cierre] Re-correr B-06 como serie temporal si el testigo sigue activo varias semanas, para que el umbral de antiguedad sea informativo. **[arrastrado — sigue pendiente.]**

## Proximos pasos
1. Llevar las dos propuestas de "Cambios al marco SDD" al usuario para decision (la #2 toca un SSOT).
2. Re-correr B-06 como serie temporal si el testigo sigue activo varias semanas — entonces el umbral de antiguedad si seria informativo.
3. Considerar el experimento intervencional (Opcion B previa): implementar una spec `draft` del testigo (SPEC-004/005) con spec-kit y comparar contra la baseline casera.
