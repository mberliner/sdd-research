# Protocolo SDD para asistentes IA

> **SSOT del protocolo del asistente.** Los asistentes que buscan `AGENTS.md` por
> convención (opencode, Cursor, Codex, Aider, Gemini CLI…) lo leen directo; Claude Code
> lo recibe vía `@AGENTS.md` en `CLAUDE.md`. Precedencia 3: por debajo de
> [`CONSTITUTION.md`](CONSTITUTION.md) (invariantes) y [`SPECS_REGISTRY.md`](SPECS_REGISTRY.md)
> (alcance por documento).

Repositorio de investigación sobre Spec-Driven Development en dos líneas paralelas —
`docs-y-investigacion/` (línea A) y `software/` (línea B); la diferencia entre ambas es
SSOT de `comun/MARCO-COMPARATIVO-DOS-LINEAS.md`. Hay git desde 2026-07-31 y **no hay CI**: la única
verificación determinista es `tools/check_docs.py`, que corre a pedido y también en cada commit
—vía el gate `tools/githooks/pre-commit`, desde 2026-08-15— y cubre cinco de los siete
principios (`CONSTITUTION.md`, campo `Verificador:`). Todo lo demás de este protocolo es humano.

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
- `Deuda arrastrada` lista lo diferido; MUST re-explicitarse en entregas siguientes hasta resolverse (anti-cascada). Derivado del experimento B-06 (`experimentos/b06-circuito-testigo/RESULTADO-EXPERIMENTO-B6.md`).

## Al cerrar una iteración

1. Corré el backstop `tools/check_docs.py` con el intérprete de Python del entorno (`python`, `python3` o `py -3` según la plataforma; requiere 3.8+) y dejá el resultado en verde (0 ERROR). Cubre la parte mecánica de los checks de arriba: cobertura de spec, links markdown y rutas escritas en backticks, `[Rxx]`, campos de spec, alcance en un solo lugar, que ningún documento anote en su encabezado un campo que el registro reserva (`SPECS_REGISTRY.md` §Reglas globales), cadena de precedencia, que cada principio de la constitución declare un `Verificador:` que exista, y que ningún documento `Activo` conserve un `[NEEDS CLARIFICATION]` abierto. Qué verifica y qué MUST NOT pretender verificar: su propio docstring; el límite general, `CONSTITUTION.md` §Límite honesto. Dos checks emiten WARN como señal para que la mires, no como veredicto: `ssot-collision` (dos specs que se declaran dueñas del mismo tema) y `sdd-check-fields` (los campos del bloque `[SDD-Check]` enumerados como definición fuera de su SSOT — sólo eso: ninguna otra regla reproducida en prosa la ve nadie). Un WARN de esos MUST revisarse antes de entregar: o se corrige la duplicación, o se explica por qué no lo es. El backstop corre además solo, al commit, si el gate está instalado (`git config core.hooksPath tools/githooks`, una vez por clon); el propio backstop verifica que lo esté y falla si no. En modo commit suma un check que acá no corre: que un cambio de método traiga su entrada de historial (paso 3).
2. Actualizá `SPECS_REGISTRY.md` si cambió el alcance, el estado o la lista de documentos.
3. Si el cambio es de **método** (protocolo, registro, templates, constitución): agregá una entrada **al principio** de `historial/sdd.md` — más reciente arriba — con fecha, acción, cambios, cómo se validó y deuda abierta (Principio VI).
4. Si enmendaste `CONSTITUTION.md`: seguí su procedimiento de enmienda completo (versión, historial, propagación, verificación).
5. Commiteá, un commit por pieza revisable. Formato del mensaje: `CONVENCIONES.md` §Mensajes de commit.

## Criterios de calidad mínima

- MUST — cada cambio debe indicar qué decisión habilita.
- MUST — si tocaste un SSOT o cerraste un experimento, aplicá la regla de propagación (Principio III): `SPECS_REGISTRY.md` §Regla de propagacion.
- SHOULD — cada cifra o afirmación externa tiene referencia `[Rxx]`.

## Ciclo de vida de specs

- SHOULD proponer el cambio en la spec antes de modificar el doc.
- MUST si se detecta divergencia spec vs. doc: señalarlo y proponer reconciliación al usuario.
- SHOULD si se depreca un doc: marcar su spec con `estado: Deprecado` antes de archivar.

## Qué NO hacer

Índice por modo de falla, no norma nueva: el protocolo de arriba está ordenado por fase y
los modos de falla no respetan la cronología. Cada ítem dispara una regla definida en otro
lado y nombra dónde; ninguno agrega norma.

- No escribir ni modificar un documento autorado sin spec registrada (Principio IV).
- No copiar el alcance de un documento ni el mapa tema → SSOT fuera del registro (`SPECS_REGISTRY.md` §Reglas globales y §Tabla SSOT).
- No cerrar un experimento sin correr los tres checks de «Propagacion» (`templates/RESULTADO-EXPERIMENTO.md`).
- No formular ni reescribir una hipótesis después de ver el resultado que la evalúa (Principio V).
- No cambiar el método y presentarlo como hallazgo de investigación, ni al revés (Principio VI).
- No interpretar una ambigüedad en silencio (Principio VII; §Disambiguación).

## Excepciones

MAY — omitir parte del protocolo si el usuario lo pide explícitamente y asume el riesgo.

## Templates disponibles en `templates/`

- `EXPERIMENTO.md`: diseño de experimentos (hipótesis, diseño, métricas, criterio de éxito, documentos que esperan el resultado).
- `RESULTADO-EXPERIMENTO.md`: cierre de experimentos (incluye la sección «Propagacion» obligatoria).

Los resultados van en `experimentos/`. Los runbooks de método de ese directorio **no** están exentos de spec: ver `SPECS_REGISTRY.md` §Docs excluidos.

## Comandos útiles

```bash
./tools/check_docs.py                                                # backstop determinista (Linux/Mac; Windows: py -3 tools\check_docs.py)
git config core.hooksPath tools/githooks                             # instalar el gate de commit (una vez por clon)
rg --files                                                           # listar contenido rastreado
rg "\[R[0-9]{2}\]" -g '*.md'                                         # inspeccionar uso de referencias
rg -n "NEEDS CLARIFICATION|TODO|FIXME" .                             # pendientes y ambigüedades abiertas
sed -n '1,120p' SPECS_REGISTRY.md                                    # reglas globales y precedencia
git log --oneline                                                    # historial de cambios versionados
```

## Convenciones

Léxico normativo, forma de los documentos, nombres y formato de commit: `CONVENCIONES.md`.
Se consulta al escribir, no al arrancar.
