# Reporte de Mejoras SDD

Fecha: 2026-03-01.
Fuente: análisis comparativo con proyecto "Transformacion AI-Native Org" — SPECS_REGISTRY.md, CLAUDE.md, historial/sdd.md.

> **Estado: CERRADO / HISTÓRICO (2026-06-01).** Las mejoras 1–10 de este reporte se implementaron en la **Fase 1** de consolidación del sistema (2026-03-01) y viven hoy en `SPECS_REGISTRY.md` y `CLAUDE.md`; la mejora 11 (tests del sistema SDD) evolucionó hacia los experimentos B-06/B-07 sobre el proyecto testigo. El detalle de qué quedó aplicado está en `historial/sdd.md`. Este documento se conserva como registro auditable del análisis original; **el contenido en presente ("Situación actual…", "Mejora…") describe el estado previo a la Fase 1, no el estado actual del repositorio.**

---

## Contexto

El proyecto "Transformacion AI-Native Org" completó dos fases de implementación SDD (piloto de 10 docs + consolidación) con tests de verificación documentados. Este reporte extrae las prácticas ausentes en el presente proyecto y las formula como mejoras accionables.

---

## Área 1: Uso de SSOT

### 1.1 Campo `deriva_de` ausente en specs de derivados

**Situación actual**: Las specs de documentos `derivado` no tienen campo explícito que indique su SSOT de origen.

**Problema**: La regla de propagación ("si cambia un SSOT, sus derivados MUST revisarse") es imposible de aplicar mecánicamente porque no hay forma de saber qué docs derivan de cuál SSOT sin leer todos los docs.

**Mejora**: Agregar campo `deriva_de` en cada spec con `ssot_level: derivado`. Ejemplo:

```
| deriva_de | `MARCO-COMPARATIVO-DOS-LINEAS.md` |
```

**Impacto**: Hace la propagación trazable y el bloque `[SDD-Check]` puede listar derivados con precisión.

---

### 1.2 Tabla SSOT sin columna "Quién referencia"

**Situación actual**: La tabla SSOT en `CLAUDE.md` tiene columnas Concepto / SSOT / Derivados.

**Problema**: No es fácil evaluar el impacto de cambiar un SSOT porque no se sabe qué documentos lo citan.

**Mejora**: Agregar columna "Quién referencia" a la tabla SSOT. El proyecto de referencia la usa para listar explícitamente qué docs apuntan a cada SSOT, habilitando un análisis de impacto inmediato.

---

### 1.3 Specs sin campos `owner`, `refresh`, `audiencia` y `estado`

**Situación actual**: Las specs en `SPECS_REGISTRY.md` solo tienen: `path`, `propósito`, `ssot_level`, `incluye`, `excluye`, `validación`.

**Problema**: Falta accountability (quién mantiene el doc), cadencia de actualización (cuándo revisarlo) y estado del ciclo de vida (activo/borrador/deprecado).

**Mejora**: Agregar los 4 campos a specs nuevas y existentes:

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `owner` | Responsable de mantener el doc | `Línea A` |
| `refresh` | Cuándo revisarlo | `Por evento` / `Mensual` / `Trimestral` |
| `audiencia` | A quién está dirigido | investigador, asistente IA, ambos |
| `estado` | Ciclo de vida | `Activo` / `Borrador` / `Deprecado` |

---

### 1.4 Sin niveles de profundidad de spec definidos

**Situación actual**: Todas las specs tienen el mismo nivel de detalle.

**Problema**: Un índice operativo no necesita la misma spec que un SSOT central con múltiples derivados.

**Mejora**: Definir tres niveles en `SPECS_REGISTRY.md`:

| Nivel | Campos | Aplicar a |
|-------|--------|-----------|
| Mínima | 5 campos (path, propósito, ssot_level, owner, validación) | índices, plantillas |
| Estándar | ~12 líneas | SSOTs simples, derivados |
| Extendida | ~20 líneas + requisitos con checkboxes | SSOTs críticos con múltiples derivados |

---

### 1.5 Sin lista de docs excluidos del registro

**Situación actual**: No hay criterio explícito sobre qué no necesita spec.

**Problema**: Ambigüedad sobre si archivos de datos, logs o fuentes originales necesitan spec.

**Mejora**: Agregar sección en `SPECS_REGISTRY.md`:

```
## Docs excluidos del registro (no necesitan spec)
- Archivos fuente originales (.pdf, .docx, .xlsx)
- Reportes auto-generados (.conversion_report.json)
- Notas de sesión sin estructura formal
```

---

## Área 2: Uso de Docs SDD (Protocolo)

### 2.1 Sin ciclo de vida de specs

**Situación actual**: El protocolo cubre pre-generación, durante y post-generación, pero no el mantenimiento de la spec en sí.

**Problema**: Cuando una spec diverge del doc real (por evolución del contenido), no hay regla clara de qué hacer.

**Mejora**: Agregar al protocolo en `CLAUDE.md`:

```
### Ciclo de vida de specs
- SHOULD: proponer cambio en la spec antes de modificar el doc.
- MUST: si se detecta divergencia spec vs. doc, señalarlo y proponer reconciliación al usuario.
- SHOULD: si se depreca un doc, marcar spec como `estado: Deprecado` antes de archivar.
```

---

### 2.2 Sin reglas de disambiguación conversacional

**Situación actual**: No hay instrucción sobre qué hacer cuando una spec tiene ambigüedad.

**Problema**: El asistente puede interpretar la ambigüedad y proceder — generando contenido que viola la spec sin saberlo.

**Mejora**: Agregar al protocolo:

```
### Disambiguación
- MUST: preguntar al usuario si la spec tiene ambigüedad, en lugar de interpretar.
- MUST NOT: anticipar ambigüedad agregando texto a la spec sin aprobación.
```

---

### 2.3 Regla de violación de scope sin MUST NOT explícito

**Situación actual**: El paso 4 del protocolo dice "detener y explicitar el conflicto".

**Problema**: Sin "MUST NOT proceder ni proponer alternativas", el asistente puede inventar workarounds (patrón documentado en el proyecto de referencia: Test 3 — fallido inicialmente).

**Mejora**: Endurecer el paso 4:

```
4. Si la solicitud contradice la spec: MUST detenerse y explicitar el conflicto.
   MUST NOT proceder ni proponer alternativas sin aprobación explícita del usuario.
```

---

### 2.4 Post-generación sin checklist de validación genérica

**Situación actual**: El bloque `[SDD-Check]` tiene 6 campos pero no hay una lista de verificaciones estándar que siempre aplicar.

**Problema**: El campo "Validaciones aplicadas" queda vago — el asistente no sabe qué verificar por defecto.

**Mejora**: Agregar al protocolo una lista de checks genéricos obligatorios:

```
### Validación post-generación (checks genéricos)
- [ ] Referencias internas no rotas
- [ ] No duplica contenido de ningún SSOT (referencia, no copia)
- [ ] No contradice SSOTs activos
- [ ] Cambios en SSOT: derivados listados en "Derivados a revisar"
```

---

### 2.5 Sin historial de implementación SDD

**Situación actual**: No existe registro de fases, tests o ajustes al sistema SDD del propio proyecto.

**Problema**: No hay forma de saber qué funcionó, qué falló y qué correcciones se aplicaron al protocolo — impide mejora iterativa.

**Mejora**: Crear `historial/sdd.md` con estructura:

```
## Fase N — Nombre (fecha) — estado
- Alcance
- Archivos creados/modificados
- Tests ejecutados

## Tests
- Test X — descripción — PASADO/FALLIDO
  - Acción
  - Resultado
  - Corrección aplicada
```

---

### 2.6 Sin tests del sistema SDD

**Situación actual**: No hay tests diseñados para verificar que el protocolo funciona.

**Problema**: Es imposible saber si los asistentes respetan el protocolo sin evidencia empírica.

**Mejora**: Diseñar al menos 2 tests iniciales:

| Test | Descripción | Condición |
|------|-------------|-----------|
| Test 1 — Doc sin spec | Solicitar modificar un doc sin spec → verificar que el asistente propone spec mínima antes de proceder | Próxima vez que haya un doc sin spec |
| Test 2 — Violación de scope | Solicitar contenido que viole el campo Excluye → verificar que el asistente se detiene y no propone workarounds | Cualquier doc con Excluye definido |
| Test 3 — Propagación | Modificar un SSOT → verificar que el asistente lista derivados en [SDD-Check] | Próxima modificación a SSOT |

---

## Resumen de mejoras por prioridad

| # | Mejora | Archivo a modificar | Esfuerzo |
|---|--------|---------------------|----------|
| 1 | Campo `deriva_de` en specs de derivados | `SPECS_REGISTRY.md` | bajo |
| 2 | MUST NOT en violación de scope | `CLAUDE.md` | bajo |
| 3 | Checks genéricos post-generación | `CLAUDE.md` | bajo |
| 4 | Ciclo de vida de specs | `CLAUDE.md` | bajo |
| 5 | Disambiguación conversacional | `CLAUDE.md` | bajo |
| 6 | Campos `owner`, `refresh`, `estado`, `audiencia` en specs | `SPECS_REGISTRY.md` | medio |
| 7 | Niveles de profundidad de spec | `SPECS_REGISTRY.md` | medio |
| 8 | Docs excluidos del registro | `SPECS_REGISTRY.md` | bajo |
| 9 | Columna "Quién referencia" en tabla SSOT | `CLAUDE.md` | medio |
| 10 | Crear `historial/sdd.md` | nuevo archivo | medio |
| 11 | Diseñar y ejecutar tests SDD | `historial/sdd.md` | alto |
