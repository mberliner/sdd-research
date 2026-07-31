# 00 - Index

Navegación del proyecto: dónde está cada cosa y en qué orden leerla.

El **alcance** de cada documento (`proposito`, `incluye`, `excluye`, `validacion`) y el **mapa tema → SSOT** viven en [SPECS_REGISTRY.md](./SPECS_REGISTRY.md); acá no se reproducen.

## Ruta recomendada

1. [README.md](./README.md) — qué es el proyecto
2. [CONSTITUTION.md](./CONSTITUTION.md) — principios no-negociables (leer antes de proponer un doc o un cambio de método)
3. [AGENTS.md](./AGENTS.md) — protocolo para asistentes IA (`CLAUDE.md` lo importa)
4. [SPECS_REGISTRY.md](./SPECS_REGISTRY.md) — alcance y validación por documento, tabla SSOT y reglas de propagación
5. [MARCO-COMPARATIVO-DOS-LINEAS.md](./MARCO-COMPARATIVO-DOS-LINEAS.md)
6. [SDD-ADAPTATIVO-VS-CASCADA.md](./SDD-ADAPTATIVO-VS-CASCADA.md)
7. [ESCENARIOS-QUE-JUSTIFICAN-SDD.md](./ESCENARIOS-QUE-JUSTIFICAN-SDD.md)
8. [ESTADISTICAS-TENDENCIAS-EVOLUCION.md](./ESTADISTICAS-TENDENCIAS-EVOLUCION.md)
9. [PROYECTOS-LIDERES-Y-FRAMEWORKS.md](./PROYECTOS-LIDERES-Y-FRAMEWORKS.md)
10. [IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md](./IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md)
11. [docs-y-investigacion/00-INDEX.md](./docs-y-investigacion/00-INDEX.md) — línea A
12. [software/00-INDEX.md](./software/00-INDEX.md) — línea B
13. [06-BACKLOG-INVESTIGACION-FUTURA.md](./06-BACKLOG-INVESTIGACION-FUTURA.md)
14. [REFERENCIAS.md](./REFERENCIAS.md)

## Estructura del proyecto

| Directorio / archivo | Rol |
|---|---|
| `CONSTITUTION.md` | SSOT — invariantes; precedencia 1 |
| `SPECS_REGISTRY.md` | SSOT — registro de specs; precedencia 2 |
| `AGENTS.md` | SSOT — protocolo del asistente; precedencia 3 |
| `CLAUDE.md` | operativo — adaptador de Claude Code (`@AGENTS.md`) |
| `README.md` | operativo — entrada al proyecto |
| `00-INDEX.md` | operativo — este índice |
| `MARCO-COMPARATIVO-DOS-LINEAS.md` | SSOT |
| `SDD-ADAPTATIVO-VS-CASCADA.md` | SSOT |
| `ESCENARIOS-QUE-JUSTIFICAN-SDD.md` | SSOT |
| `ESTADISTICAS-TENDENCIAS-EVOLUCION.md` | SSOT |
| `PROYECTOS-LIDERES-Y-FRAMEWORKS.md` | SSOT |
| `IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md` | SSOT |
| `REFERENCIAS.md` | SSOT — catálogo `[Rxx]` |
| `06-BACKLOG-INVESTIGACION-FUTURA.md` | operativo — backlog |
| `ROADMAP-MEJORAS-SDD.md` | operativo — mejoras identificadas |
| `docs-y-investigacion/` | línea A — SSOTs de agenda, métricas y plan experimental |
| `software/` | línea B — SSOTs de agenda, métricas y plan experimental; derivados de análisis |
| `experimentos/` | diseños, runbooks y resultados de experimentos |
| `templates/` | operativo — plantillas de experimento y de cierre |
| `historial/` | operativo — log evolutivo de fases y cambios de método |
| `fuentes-externas/` | material fuente externo (vendored); fuera del registro y del versionado |
