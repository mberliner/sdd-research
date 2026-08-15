# Implementacion Inicial para Contexto Actual (sin CI)

## Contexto de partida
- Equipo trabaja principalmente con asistentes IA sobre Markdown.
- No hay pipeline CI instalado para validacion automatica. Sigue siendo cierto al 2026-08-15, pero **sin CI ya no significa sin verificacion automatica**: hay git desde 2026-07-31 y un backstop local que corre en cada commit (`../tools/check_docs.py` mas el gate `../tools/githooks/pre-commit`). El escalon que falta es el remoto —nada verifica lo que se empuja—, y el criterio para darlo esta abajo.
- Se busca valor inmediato con baja friccion operativa.

## Decisiones de enfoque
1. Mantener formato Markdown como formato primario de specs.
2. Priorizar disciplina operativa antes que tooling.
3. Separar practicas por tipo de proyecto (docs vs software).

## Mejora priorizada para docs e investigacion
- Cobertura de specs en documentos criticos.
- Bloque de salida obligatorio del asistente por entrega. Su definicion y sus campos son SSOT de `../AGENTS.md` (bloque `[SDD-Check]`); aca solo se prioriza adoptarlo, no se enumera.
- Revision mensual liviana de vigencia, contradicciones y placeholders.

## Mejora priorizada para software
- Requisito minimo: cada historia critica con criterio verificable.
- Empezar contract-first en APIs nuevas o con mayor deuda.
- Checklist de calidad para codigo asistido por IA (tests, seguridad, compatibilidad).

## Roadmap 0-90 dias

### 0-30 dias
- Definir baseline de metricas por linea.
- Correr 1 experimento corto por linea.
- Normalizar plantillas de experimento y resultado.

### 31-60 dias
- Ajustar protocolo segun resultados.
- Escalar practicas que mejoraron metrica principal.
- Documentar anti-patrones detectados.

### 61-90 dias
- Consolidar guia operativa por linea.
- Decidir si alguna automatizacion minima ya esta justificada.

## Criterio para evaluar si conviene pasar a YAML/CI mas adelante
Solo considerar cuando se cumplan simultaneamente:
- Volumen alto de cambios concurrentes.
- Errores recurrentes no resueltos con disciplina manual.
- Capacidad del equipo para mantener tooling sin frenar entrega.
