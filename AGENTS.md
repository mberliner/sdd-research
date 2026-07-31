# Assistant

This file provides guidance to AI assistants when working in this repository.

## Propósito del Repositorio

Este repositorio investiga **Spec-Driven Development (SDD)** en dos líneas paralelas:

- **Línea A (docs-y-investigacion/)**: SDD aplicado a análisis, conocimiento y documentos de decisión. Foco en consistencia semántica, trazabilidad de fuentes y calidad argumental.
- **Línea B (software/)**: SDD aplicado a requisitos ejecutables, APIs, contratos y entrega. Foco en comportamiento correcto, seguridad y confiabilidad.

No hay CI ni tooling de automatización. Todo opera en modo **"Markdown + asistentes IA"**.

## Protocolo Obligatorio para Asistentes

### Antes de generar o modificar

1. **Leer la spec del documento** en `SPECS_REGISTRY.md` antes de escribir.
2. **Verificar `Incluye/Excluye`** de la spec antes de agregar contenido.
3. Si no hay spec: **proponer spec mínima y esperar aprobación** antes de proceder.
4. Si la solicitud contradice la spec: **detener y explicitar el conflicto**. MUST NOT proceder ni proponer alternativas sin aprobación explícita del usuario.

### Durante la generación

1. Mantener coherencia con SSOTs activos.
2. Citar fuentes con IDs `[Rxx]` cuando haya afirmaciones factuales.
3. Minimizar duplicación entre documentos — referenciar el SSOT correspondiente.
4. MAY proponer mejoras de spec cuando se detecte ambigüedad.

### Disambiguación

- MUST preguntar al usuario si la spec tiene ambigüedad, en lugar de interpretar.
- MUST NOT anticipar ambigüedad agregando texto a la spec sin aprobación.
- MAY marcar incertidumbre puntual dentro de un borrador con `[NEEDS CLARIFICATION: <pregunta>]` cuando no bloquea el resto del trabajo. El marcador es grep-able y MUST resolverse (preguntando al usuario) antes de considerar el documento `Activo`. Convención adoptada de GitHub Spec Kit [R10] (ver `software/ANALISIS-SPEC-KIT.md`, C2).

### Post-generación (salida obligatoria)

MUST — los checks genéricos deben verificarse antes de entregar:
- [ ] Referencias internas no rotas
- [ ] No duplica contenido de ningún SSOT (referencia, no copia)
- [ ] No contradice SSOTs activos
- [ ] Si el doc modificado es SSOT: derivados listados en "Derivados a revisar"
- [ ] Si la entrega cierra un experimento: "Derivados a revisar" poblado con los tres checks de «Propagacion» (`templates/RESULTADO-EXPERIMENTO.md`), no de memoria

MUST — toda entrega debe cerrar con este bloque:

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

El campo `Cobertura` espeja el *coverage mapping* de `/speckit.analyze` [R10]: declara si todo requisito o afirmación del cambio queda respaldado por un derivado/tarea, o lista los huecos. Convención adoptada de GitHub Spec Kit (ver `software/ANALISIS-SPEC-KIT.md`, C1).

El campo `Deuda arrastrada` lista lo diferido en esta entrega; MUST re-explicitarse en entregas siguientes hasta resolverse, para evitar abandono silencioso (anti-cascada). Práctica derivada del experimento B-06 (`experimentos/RESULTADO-EXPERIMENTO-B6.md`).

### Criterios de calidad mínima

- MUST — cada cambio debe indicar qué decisión habilita.
- SHOULD — cada cifra o afirmación externa debe tener referencia `[Rxx]`.
- MUST — los cambios en SSOT deben disparar revisión de derivados.
- MUST — un resultado que responde una pregunta abierta de un SSOT debe propagarse **primero al SSOT y después a sus derivados**. La regla anterior sólo cubre la dirección descendente; el conocimiento producido por una ejecución entra por abajo y tiene que subir. Al cerrar B-07 se actualizó `software/PLAN-PRUEBAS.md` (derivado) dejando `software/LINEAS-INVESTIGACION.md` (su SSOT) afirmando lo contrario.

### Ciclo de vida de specs

- SHOULD proponer el cambio en la spec antes de modificar el doc.
- MUST si se detecta divergencia spec vs. doc: señalarlo y proponer reconciliación al usuario.
- SHOULD si se depreca un doc: marcar su spec con `estado: Deprecado` antes de archivar.

### Excepciones

MAY — omitir parte del protocolo si el usuario lo pide explícitamente y asume el riesgo.

## Arquitectura de Documentos

Tabla SSOT, niveles `ssot_level` y regla de propagación: ver `SPECS_REGISTRY.md` (SSOT de esta información).

### Templates disponibles en `templates/`

- `EXPERIMENTO.md`: plantilla para diseñar experimentos (hipótesis, diseño, métricas, criterio de éxito).
- `RESULTADO-EXPERIMENTO.md`: plantilla para cerrar experimentos.

Los resultados van en `experimentos/` (directorio separado).

## Reglas de Escritura

- SHOULD — toda afirmación factual externa debe tener referencia `[Rxx]` de `REFERENCIAS.md`.
- MUST — todo cambio documental debe mapearse a una spec registrada en `SPECS_REGISTRY.md`.
- Minimizar duplicación entre documentos — referenciar el SSOT correspondiente.
- Lenguaje normativo: `MUST` = obligatorio, `SHOULD` = recomendado fuerte, `MAY` = opcional.

## Comandos Útiles

```bash
rg --files                                                           # listar contenido rastreado
rg "\[R[0-9]{2}\]" *.md docs-y-investigacion/*.md software/*.md     # inspeccionar uso de referencias
rg -n "TODO|FIXME" .                                                 # pendientes
sed -n '1,220p' SPECS_REGISTRY.md                                    # revisar reglas de spec antes de editar
```

## Convenciones

- Markdown como formato fuente; secciones cortas y escaneables.
- Lenguaje normativo: `MUST`/`SHOULD`/`MAY` MUST aparecer al inicio de la sentencia, seguido de `—` y el enunciado (ej. `MUST — cada cambio debe indicar qué decisión habilita.`).
- Nombres de archivo: mayúsculas, separados por guión (ej. `PLAN-PRUEBAS.md`).
- Commits: `docs: <resumen imperativo corto>` (ej. `docs: align PLAN-PRUEBAS with SSOT metrics`).
- SHOULD — los PRs deben incluir: propósito, archivos modificados, SSOT/derivados afectados, notas de validación.

## Precedencia de Fuentes

1. `SPECS_REGISTRY.md` — alcance y validación por documento (mayor precedencia).
2. Este archivo (`AGENTS.md`) — protocolo de ejecución diaria.
3. Criterio del asistente — solo cuando no haya conflicto con 1 y 2.
