# Proyectos Lideres y Frameworks Relevantes

## 1) Docs e investigacion

### MADR (ADR en Markdown)
- Tipo: registro estructurado de decisiones.
- Valor: permite trazabilidad de decisiones y contexto en formato liviano.
- Fuente: [R13].

### RFC 2119
- Tipo: lenguaje normativo para requisitos (MUST, SHOULD, MAY).
- Valor: reduce ambiguedad en specs y criterios.
- Fuente: [R04].

### ISO/IEC/IEEE 29148
- Tipo: referencia de ingenieria de requisitos.
- Valor: base formal para calidad de requisitos y especificaciones.
- Fuente: [R03].

## 2) Software

### GitHub Spec Kit
- Tipo: flujo spec-first para trabajo asistido por IA; toolkit Linea-B-nativo (CLI `specify` + comandos slash constitution/specify/clarify/plan/tasks/analyze/implement). Sin soporte nativo para documentos de analisis/conocimiento (transferencia a Linea A diferida — ver `../agenda/BACKLOG-INVESTIGACION.md`).
- Valor: convenciones claras de idea a especificacion antes de ejecutar; gate de autoridad (constitution), manejo explicito de ambiguedad (`[NEEDS CLARIFICATION]`) y validacion de consistencia continua (`/speckit.analyze`).
- Analisis detallado y mapeo contra nuestro protocolo: `../software/ANALISIS-SPEC-KIT.md`.
- Fuente: [R10].

### Superpowers (obra/superpowers)

- Tipo: metodología SDD empaquetada como skills componibles para agentes de codificación, servida a múltiples asistentes desde un set único. Flujo: `brainstorming` (elicitar la spec por diálogo, con gate duro que prohíbe escribir código antes de la aprobación) → `writing-plans` → `subagent-driven-development` (un subagente fresco por tarea, más revisión por tarea y revisión final de rama).
- Valor: tercera implementación de SDD independiente de Spec Kit y del proyecto testigo, que converge en gate de autoridad, lenguaje normativo y verificación con evidencia antes de declarar completitud. Diverge en un punto de interés: no regenera el código desde la spec (*spec-anchored*, no *spec-as-source* [R30]), de modo que la posición intermedia queda documentada en producción. Practica evaluación conductual de sus propios documentos con subagentes frescos.
- Analisis detallado y mapeo contra nuestro protocolo: `../software/ANALISIS-SUPERPOWERS.md`.
- Fuente: [R37].

### OpenSpec (Fission-AI/OpenSpec)

- Tipo: sistema SDD distribuido como CLI npm, con adaptadores generados para más de 30 asistentes. Flujo: `/opsx:explore` (opcional, sin compromiso) → `/opsx:propose` (genera en un paso propuesta, delta de specs, diseño y tareas) → `/opsx:apply` → `/opsx:verify` → `/opsx:archive`. Separa `openspec/specs/` (verdad vigente) de `openspec/changes/` (deltas propuestos), y al archivar fusiona el delta aprobado en la spec.
- Valor: cuarto caso del relevamiento de convergencia y linaje independiente de Spec Kit por fecha de origen. Su rasgo distintivo es de entrega y no de contenido: la instrucción de método no se lee de un documento sino que la sirve una herramienta bajo demanda (`openspec instructions <artefacto> --json`), con las reglas del proyecto en `openspec/config.yaml`. Se posiciona explícitamente como brownfield-first frente al sesgo greenfield de los otros toolkits. Es *spec-anchored*, no *spec-as-source* [R30].
- Analisis detallado y mapeo contra nuestro protocolo: `../software/ANALISIS-OPENSPEC.md`.
- Fuente: [R38].

### OpenAPI Initiative
- Tipo: contract-first para APIs.
- Valor: contrato compartido entre equipos, tooling amplio.
- Fuente: [R06].

### AsyncAPI
- Tipo: contract-first para eventos y arquitecturas asincronas.
- Valor: estandariza interfaces event-driven.
- Fuente: [R14].

### Cucumber / Gherkin
- Tipo: behavior-first (BDD).
- Valor: conecta requisitos funcionales con escenarios verificables.
- Fuente: [R07].

### Pact Foundation
- Tipo: contract testing.
- Valor: evita roturas entre consumidor y proveedor en integraciones.
- Fuente: [R08].

## 3) Marcos de gobernanza y riesgo transversales

### NIST AI RMF + Generative AI Profile
- Uso: gestionar riesgos IA en decisiones y productos.
- Fuente: [R01], [R02].

### ISO/IEC 42001
- Uso: sistema de gestion de IA (gobernanza organizacional).
- Fuente: [R05].

## 4) Conclusiones para este hub
- Para docs/investigacion: priorizar MADR + lenguaje normativo (RFC 2119) + base de requisitos (ISO/IEC/IEEE 29148).
- Para software: priorizar Spec Kit + OpenAPI/AsyncAPI + Pact + BDD.
- En ambos casos: marco de riesgo IA explicito para uso de asistentes.
