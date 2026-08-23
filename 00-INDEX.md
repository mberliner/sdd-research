# 00 - Index

Navegación del proyecto: dónde está cada cosa, en qué orden leerla y qué rol cumple.

El **alcance** de cada documento, los campos de su spec y el **mapa tema → SSOT** viven en [SPECS_REGISTRY.md](./SPECS_REGISTRY.md); acá no se reproducen. Qué campos son y cuál es la única excepción: su §Reglas globales.

## Ruta recomendada

| # | Documento | Rol |
|---|---|---|
| 1 | [README.md](./README.md) | operativo — entrada al proyecto |
| 2 | [CONSTITUTION.md](./CONSTITUTION.md) | SSOT — invariantes; precedencia 1 |
| 3 | [SPECS_REGISTRY.md](./SPECS_REGISTRY.md) | SSOT — registro de specs; precedencia 2 |
| 4 | [AGENTS.md](./AGENTS.md) | SSOT — protocolo del asistente; precedencia 3 (`CLAUDE.md` lo importa) |
| 5 | [comun/MARCO-COMPARATIVO-DOS-LINEAS.md](comun/MARCO-COMPARATIVO-DOS-LINEAS.md) | SSOT |
| 6 | [comun/SDD-ADAPTATIVO-VS-CASCADA.md](comun/SDD-ADAPTATIVO-VS-CASCADA.md) | SSOT |
| 7 | [comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md](comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md) | SSOT |
| 8 | [comun/ESTADISTICAS-TENDENCIAS-EVOLUCION.md](comun/ESTADISTICAS-TENDENCIAS-EVOLUCION.md) | SSOT |
| 9 | [comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md](comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md) | SSOT |
| 10 | [comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md](comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md) | SSOT |
| 11 | [docs-y-investigacion/00-INDEX.md](./docs-y-investigacion/00-INDEX.md) | operativo — índice de la línea A |
| 12 | [software/00-INDEX.md](./software/00-INDEX.md) | operativo — índice de la línea B |
| 13 | [agenda/BACKLOG-INVESTIGACION.md](agenda/BACKLOG-INVESTIGACION.md) | operativo — preguntas abiertas de investigación |
| 14 | [agenda/MEJORAS-METODO.md](agenda/MEJORAS-METODO.md) | operativo — mejoras al método del repo (`M-NN`) |
| 15 | [REFERENCIAS.md](./REFERENCIAS.md) | SSOT — catálogo `[Rxx]` |
| 16 | [CONVENCIONES.md](./CONVENCIONES.md) | SSOT — léxico y forma; transversal, se consulta al escribir |

## Resto de la estructura

| Directorio / archivo | Rol |
|---|---|
| `CLAUDE.md` | operativo — adaptador de Claude Code (`@AGENTS.md`) |
| `00-INDEX.md` | operativo — este índice |
| `comun/` | SSOTs transversales a las dos líneas (filas 5 a 10) |
| `agenda/` | operativo — los dos backlogs vivos (filas 13 y 14) |
| `docs-y-investigacion/` | línea A — SSOTs de agenda, métricas y plan experimental |
| `software/` | línea B — SSOTs de agenda, métricas y plan experimental; derivados de análisis |
| `experimentos/<id>-<nombre>/` | diseños, runbooks y resultados, una carpeta por experimento |
| `templates/` | operativo — plantillas de experimento y de cierre |
| `historial/` | operativo — log evolutivo de fases y cambios de método; incluye `ROADMAP-MEJORAS-SDD.md`, registro histórico cerrado (2026-06-01) |
| `tools/` | verificación determinista del repositorio (`check_docs.py`) |
| `fuentes-externas/` | material fuente externo (vendored); fuera del registro y del versionado |
