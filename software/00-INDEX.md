# Linea B - Software

## Pregunta central
Como aplicar SDD para convertir especificaciones en software confiable, verificable y evolutivo.

## Gobernanza SDD de esta linea
1. La cadena de precedencia (`../CONSTITUTION.md` -> `../SPECS_REGISTRY.md` -> `../AGENTS.md`) MUST regir tambien esta linea; su definicion vive en `../SPECS_REGISTRY.md` §Precedencia y no se reproduce aca.
2. Las excepciones SHOULD justificarse explicitamente en resultados de experimento.

## Lectura sugerida
1. [LINEAS-INVESTIGACION.md](./LINEAS-INVESTIGACION.md)
2. [NECESIDADES-Y-METRICAS.md](./NECESIDADES-Y-METRICAS.md)
3. [PLAN-PRUEBAS.md](./PLAN-PRUEBAS.md)

## Análisis de frameworks
- [ANALISIS-SPEC-KIT.md](./ANALISIS-SPEC-KIT.md) — metodología de GitHub Spec Kit mapeada contra nuestro protocolo SDD; conclusiones para Línea B. Fuente vendored en [../fuentes-externas/spec-kit/](../fuentes-externas/spec-kit/).
- [ANALISIS-SUPERPOWERS.md](./ANALISIS-SUPERPOWERS.md) — metodología de Superpowers mapeada contra nuestro protocolo SDD; su método de evaluación conductual de documentación y la posición spec-anchored. Fuente vendored en [../fuentes-externas/superpowers/](../fuentes-externas/superpowers/).
- [ANALISIS-OPENSPEC.md](./ANALISIS-OPENSPEC.md) — metodología de OpenSpec mapeada contra nuestro protocolo SDD; su filtro de procedencia, la separación spec vigente / delta propuesto y la instrucción servida por herramienta. Fuente vendored en [../fuentes-externas/OpenSpec/](../fuentes-externas/OpenSpec/).
- [CONVERGENCIA-IMPLEMENTACIONES-SDD.md](./CONVERGENCIA-IMPLEMENTACIONES-SDD.md) — SSOT: qué elementos del método SDD son invariantes entre implementaciones independientes y cuáles no, leído sobre cuatro casos con un instrumento común.
- [COMPARATIVA-SPECKIT-VS-TESTIGO.md](./COMPARATIVA-SPECKIT-VS-TESTIGO.md) — comparación en 5 dimensiones (implementación SDD, artefactos, funcionalidad, beneficios, debilidades) entre Spec Kit y el proyecto testigo `evaluador-flujo-intent` (ex `agent-test-suite`). Deriva de ANALISIS-SPEC-KIT.md.
- [DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md](./DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md) — documento de decisión A (adoptar Spec Kit) vs. B (portar /clarify+/analyze y sumar un hook de enforcement determinista): esfuerzo, ventajas, desventajas y recomendación condicionada. Deriva de COMPARATIVA-SPECKIT-VS-TESTIGO.md. Estado: Borrador.
- [RELACION-SPEC-VS-EPICA.md](./RELACION-SPEC-VS-EPICA.md) — relación y diferencias entre "spec" (sentido Spec Kit y sentido gobernanza local) y los artefactos ágiles épica/historia de usuario, con discusión externa. Deriva de ANALISIS-SPEC-KIT.md.
- [RELACION-FR-VS-SC-Y-COBERTURA.md](./RELACION-FR-VS-SC-Y-COBERTURA.md) — por qué FR y SC no son 1 a 1 (ejes distintos, cardinalidad N:M) y por qué la cobertura no es "un test por requisito", con ejemplos del testigo. Deriva de ANALISIS-SPEC-KIT.md.

## Análisis temáticos
- [SDD-EN-LEGACY-Y-BROWNFIELD.md](./SDD-EN-LEGACY-Y-BROWNFIELD.md) — cuándo y cómo aplicar specs retrospectivas a código legacy (brownfield); casos, ventajas/riesgos, observado vs. deseado, con evidencia externa. Estado: Borrador.

## Resultado esperado
Un marco pragmatico de requisitos, contratos y pruebas ligado a resultados de entrega (calidad, flujo, estabilidad).
