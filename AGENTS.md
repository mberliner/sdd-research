# Protocolo SDD para asistentes IA

> **SSOT del protocolo del asistente.** Los asistentes que buscan `AGENTS.md` por
> convención (opencode, Cursor, Codex, Aider, Gemini CLI…) lo leen directo; Claude Code
> lo recibe vía `@AGENTS.md` en `CLAUDE.md`. Precedencia 3: por debajo de
> [`CONSTITUTION.md`](CONSTITUTION.md) (invariantes) y [`SPECS_REGISTRY.md`](SPECS_REGISTRY.md)
> (alcance por documento).

Repositorio de investigación sobre Spec-Driven Development en dos líneas paralelas —
`docs-y-investigacion/` (línea A) y `software/` (línea B); la diferencia entre ambas es
SSOT de `comun/MARCO-COMPARATIVO-DOS-LINEAS.md`. Hay git desde 2026-07-31, pero **no hay CI ni
verificación determinista**: todo check de este protocolo es humano y a pedido.

## Antes de cualquier cambio

1. Leé `CONSTITUTION.md`. Ningún documento ni spec puede violar un principio; si hay conflicto, se ajusta la spec, no el principio.
2. Leé `00-INDEX.md` para ubicarte en la estructura.
3. Leé la spec del documento en `SPECS_REGISTRY.md` —incluidas la tabla SSOT y las reglas globales— antes de escribir.
4. Verificá `incluye`/`excluye` de esa spec antes de agregar contenido.
5. Si no hay spec: **proponé spec mínima y esperá aprobación** antes de proceder.
6. Si la solicitud contradice la spec: **detené y explicitá el conflicto**. MUST NOT proceder ni proponer alternativas sin aprobación explícita del usuario.

## Durante el cambio

- Mantené coherencia con los SSOTs activos.
- Citá fuentes con IDs `[Rxx]` de `REFERENCIAS.md` en toda afirmación factual externa (Principio II).
- Referenciá el SSOT en lugar de reproducirlo, entre documentos y dentro de uno (Principio I).
- MAY proponer mejoras de spec cuando detectes ambigüedad.

### Disambiguación

- MUST preguntar al usuario si la spec tiene ambigüedad, en lugar de interpretar.
- MUST NOT anticipar ambigüedad agregando texto a la spec sin aprobación.
- MAY marcar incertidumbre puntual dentro de un borrador con `[NEEDS CLARIFICATION: <pregunta>]` cuando no bloquea el resto del trabajo. El marcador es grep-able y MUST resolverse antes de considerar el documento `Activo`. Convención adoptada de GitHub Spec Kit [R10] (ver `software/ANALISIS-SPEC-KIT.md`, C2).

## Post-generación (salida obligatoria)

MUST — verificar antes de entregar:
- [ ] Referencias internas no rotas
- [ ] No duplica contenido de ningún SSOT (referencia, no copia)
- [ ] No contradice SSOTs activos
- [ ] Si el doc modificado es SSOT: derivados listados en "Derivados a revisar"
- [ ] Si la entrega cierra un experimento: "Derivados a revisar" poblado con los tres checks de «Propagacion» (`templates/RESULTADO-EXPERIMENTO.md`), no de memoria

MUST — toda entrega cierra con este bloque:

```text
[SDD-Check]
- Spec leida: SI/NO
- Incluye/Excluye verificado: SI/NO
- Validaciones aplicadas: <lista>
- SSOT afectado: <ninguno|archivo>
- Derivados a revisar: <lista o ninguno>
- Cobertura: <completa | requisitos/SSOT sin derivado o tarea asociada>
- Deuda arrastrada: <pendientes diferidos, o ninguno>
- Riesgos/reservas: <texto breve>
```

- `Cobertura` espeja el *coverage mapping* de `/speckit.analyze` [R10]: declara si todo requisito o afirmación del cambio queda respaldado por un derivado/tarea, o lista los huecos. Convención adoptada de GitHub Spec Kit (ver `software/ANALISIS-SPEC-KIT.md`, C1).
- `Deuda arrastrada` lista lo diferido; MUST re-explicitarse en entregas siguientes hasta resolverse (anti-cascada). Derivado del experimento B-06 (`experimentos/RESULTADO-EXPERIMENTO-B6.md`).

## Al cerrar una iteración

1. Corré el backstop `tools/check_docs.py` con el intérprete de Python del entorno (`python`, `python3` o `py -3` según la plataforma; requiere 3.8+) y dejá el resultado en verde (0 ERROR). Cubre la parte mecánica de los checks de arriba: cobertura de spec, links, `[Rxx]`, campos de spec, alcance en un solo lugar y cadena de precedencia. **Verifica presencia y forma, no adecuación** — que un doc tenga spec no dice que la spec lo describa bien; eso sigue siendo tuyo.
2. Actualizá `SPECS_REGISTRY.md` si cambió el alcance, el estado o la lista de documentos.
3. Si el cambio es de **método** (protocolo, registro, templates, constitución): agregá una entrada **al principio** de `historial/sdd.md` — más reciente arriba — con fecha, acción, cambios, cómo se validó y deuda abierta (Principio VI).
4. Si enmendaste `CONSTITUTION.md`: seguí su procedimiento de enmienda completo (versión, historial, propagación, verificación).
5. Commiteá con `docs: <resumen imperativo corto>`, un commit por pieza revisable.

## Criterios de calidad mínima

- MUST — cada cambio debe indicar qué decisión habilita.
- MUST — los cambios en SSOT disparan revisión de derivados, y los resultados de una ejecución suben al SSOT antes de bajar a sus derivados. Regla completa y su procedimiento: `SPECS_REGISTRY.md` §Regla de propagacion (Principio III).
- SHOULD — cada cifra o afirmación externa tiene referencia `[Rxx]`.

## Ciclo de vida de specs

- SHOULD proponer el cambio en la spec antes de modificar el doc.
- MUST si se detecta divergencia spec vs. doc: señalarlo y proponer reconciliación al usuario.
- SHOULD si se depreca un doc: marcar su spec con `estado: Deprecado` antes de archivar.

## Qué NO hacer

- No escribir ni modificar un documento autorado sin spec registrada (Principio IV).
- No copiar el alcance de un documento fuera de `SPECS_REGISTRY.md`, ni el mapa tema → SSOT fuera de su tabla SSOT.
- No cerrar un experimento sin correr los tres checks de «Propagacion».
- No formular ni reescribir una hipótesis después de ver el resultado que la evalúa (Principio V).
- No cambiar el método y presentarlo como hallazgo de investigación, ni al revés (Principio VI).
- No interpretar una ambigüedad en silencio.

## Excepciones

MAY — omitir parte del protocolo si el usuario lo pide explícitamente y asume el riesgo.

## Templates disponibles en `templates/`

- `EXPERIMENTO.md`: diseño de experimentos (hipótesis, diseño, métricas, criterio de éxito, documentos que esperan el resultado).
- `RESULTADO-EXPERIMENTO.md`: cierre de experimentos (incluye la sección «Propagacion» obligatoria).

Los resultados van en `experimentos/`. Los runbooks de método de ese directorio **no** están exentos de spec: ver `SPECS_REGISTRY.md` §Docs excluidos.

## Comandos útiles

```bash
./tools/check_docs.py                                                # backstop determinista (Linux/Mac; Windows: py -3 tools\check_docs.py)
rg --files                                                           # listar contenido rastreado
rg "\[R[0-9]{2}\]" *.md docs-y-investigacion/*.md software/*.md     # inspeccionar uso de referencias
rg -n "NEEDS CLARIFICATION|TODO|FIXME" .                             # pendientes y ambigüedades abiertas
sed -n '1,120p' SPECS_REGISTRY.md                                    # reglas globales y precedencia
git log --oneline                                                    # historial de cambios versionados
```

## Convenciones

- Markdown como formato fuente; secciones cortas y escaneables.
- Lenguaje normativo: `MUST` = obligatorio, `SHOULD` = recomendado fuerte, `MAY` = opcional. MUST aparecer al inicio de la sentencia, seguido de `—` y el enunciado (ej. `MUST — cada cambio debe indicar qué decisión habilita.`).
- Nombres de archivo: mayúsculas, separados por guión (ej. `PLAN-PRUEBAS.md`).
- Commits: `docs: <resumen imperativo corto>` (ej. `docs: align PLAN-PRUEBAS with SSOT metrics`), sin firma de asistente.
- Convenciones de forma restantes (fechas, ortografía, sin emoticones): `SPECS_REGISTRY.md` §Reglas globales.
