# SDD en Legacy y Brownfield

Estado: Borrador. Fecha: 2026-06-05. Línea: B (software).

Spec: ver `SPECS_REGISTRY.md` → `software/SDD-EN-LEGACY-Y-BROWNFIELD.md`.

## Propósito

Responder cuándo y cómo conviene escribir **specs retrospectivas** (retro-specs)
para código legacy, y con qué forma. El análisis se ancla en evidencia externa y
se diferencia del análisis del flujo de Spec Kit (`software/ANALISIS-SPEC-KIT.md`).

Terminología: *legacy* se usa aquí en el sentido de Michael Feathers —código sin
red de pruebas automáticas de regresión— no como sinónimo de "código viejo" [R23].

## Tesis

La retro-spec conviene como **inversión selectiva dirigida por dolor**, no como
ejercicio de documentar todo el sistema. El error clásico es tratarla como un
proyecto documental exhaustivo; el acierto es tratarla como captura de
conocimiento donde más arde, y en software su forma canónica es **ejecutable**
(tests de caracterización), no prosa.

## Cuándo SÍ conviene (casos)

| Caso | Por qué paga |
|------|--------------|
| Zona de cambio frecuente | La spec se amortiza en cada cambio futuro del módulo. |
| Bus factor 1 (conocimiento en una cabeza) | Materializa lo tácito antes de perderlo. |
| Comportamiento cuestionado ("¿bug o feature?") | Congela la intención y zanja discusiones recurrentes. |
| Antes de refactor o reescritura | Da un contrato observable para no romper lo que importa. Caso de uso primario en la literatura [R23]. |
| Superficie con cumplimiento o seguridad | La spec es exigible y rastreable; aquí escala a proyecto formal [R27]. |
| Frontera entre sistemas | El contrato de integración es lo más caro de descubrir por reverse engineering. |

## Cuándo NO conviene

- MUST NOT — documentar código estable que nadie toca: congela esfuerzo sin retorno.
- Código en muerte anunciada (a deprecar en meses).
- Como big-bang documental del sistema entero: produce specs genéricas,
  desactualizadas al nacer, que nadie lee. La academia coincide en que la
  extracción **completa y automática** es ilusoria; lo realista es
  especificación **parcial aumentada por comprensión humana** [R24].
- Cuando no puedes verificar la spec contra el comportamiento real: una retro-spec
  no validada transmite falsa confianza y decae ("documentation decay") [R26].

## Ventajas

- Rescata intención perdida: el código dice *qué* hace, no *por qué*.
- Red de seguridad para refactor: caracteriza el comportamiento esperado antes de tocar [R23].
- Reduce bus factor y acelera onboarding.
- Base directa para *characterization tests*.
- El acto de escribir la spec revela contradicciones e incoherencias.

## Desventajas y riesgos

- **Fosilizar bugs**: documentar lo que el código hace hoy puede consagrar sus
  defectos como "spec". Mitigación: ver distinción observado vs. deseado.
- Costo de reverse engineering subestimado.
- Falsa precisión si la spec no se valida contra el sistema [R26].
- Doble fuente de verdad si el código evoluciona y la spec no: crea la divergencia
  que el protocolo del proyecto combate con SSOT (ver `AGENTS.md`).
- Deriva de alcance: empezar por un módulo y querer especificar todo.

## Distinción crítica: comportamiento observado vs. deseado

El núcleo de la disciplina (Feathers) es que un *characterization test* documenta
**lo que el sistema realmente hace, no lo que desearías que hiciera** [R23]. La
retro-spec captura primero el comportamiento actual —incluidos sus defectos— para
no romperlos sin querer durante el refactor; la decisión de "corregir o preservar"
se toma después, conscientemente.

MUST — toda retro-spec de legacy debe marcar cada afirmación como **observada**
(lo que hace) o **deseada** (lo que debería hacer). Cuando no se sabe si algo es
intención o accidente, usar el marcador grep-able `[NEEDS CLARIFICATION: ...]`
(convención del proyecto, ver `AGENTS.md`).

## Forma canónica en software: ejecutable, no prosa

La corriente dominante sostiene que en software la retro-spec correcta es
**ejecutable** (tests de caracterización), porque la prosa estática decae [R23][R26].
La prosa se reserva para lo que los tests no expresan: el *por qué*, las decisiones
de negocio y las restricciones regulatorias.

Recomendación operativa:

1. SHOULD — no especificar el sistema, sino el **próximo cambio**: retro-spec
   *just-in-time*, disparada por una tarea real (bug, feature, refactor).
2. MUST — acompañar la spec con *characterization tests* que la anclen al
   comportamiento real; sin verificación, la spec es opinión.
3. SHOULD — trazarla como SSOT desde el día uno para no crear divergencia.
4. SHOULD — escalar el peso de la retro-spec con la criticidad del sistema: para
   sistemas críticos o regulados aplica el modelo de proyecto formal [R27]; para
   código vivo, el modelo incremental dirigido por dolor [R23][R26].

## Tensión no resuelta por las fuentes

La academia y la ingeniería de sistemas (IEEE, INCOSE) tratan la retro-spec como
**proyecto de ingeniería costoso** [R24][R27]; la corriente ágil la trata como
**actividad incremental dirigida por dolor** [R23][R26]. No hay contradicción:
el eje que las separa es la **criticidad/cumplimiento** del sistema. Este doc
adopta el enfoque incremental como default y reserva el formal para superficies
críticas.

## Relevancia para IA (frontera 2026)

Existe trabajo formal sobre retro-specs legacy **consumibles por agentes de IA**:
Reversa, un framework de *reverse documentation engineering* que convierte software
legacy en especificaciones operativas trazables para agentes [R25]. Conecta con la
agenda de Línea B sobre specs como contrato para asistentes IA.

## Conexión con experimentación (Línea B)

Hipótesis candidata: *la retro-spec (spec mínima + characterization tests) reduce
el costo o el error del próximo cambio en un módulo legacy, frente a tocarlo sin
spec*. Métrica primaria: defectos introducidos o tiempo de comprensión por cambio.
La formalización como experimento queda **diferida** a `software/PLAN-PRUEBAS.md` y
su priorización a `06-BACKLOG-INVESTIGACION-FUTURA.md`.

## Nota relacionada: enforcement SDD sin git

Un repo legacy puede carecer de git (o de `pre-commit`), lo que rompe el supuesto
"rama por feature" de los flujos SDD estándar. El proyecto testigo resolvió esto
con un sustituto git-less (archivo `.sdd/current-spec` + hook `PreToolUse`): ver
`software/DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` §9. Es enforcement, no retro-spec
—fuera del alcance de este doc— pero relevante al aplicar SDD sobre código sin
tooling moderno.

## Alcance diferido

- Transferencia a Línea A (retro-spec de documentos/conocimiento legacy): diferida
  a `06-BACKLOG-INVESTIGACION-FUTURA.md`.
- Diseño del experimento B: diferido a `software/PLAN-PRUEBAS.md`.

## Referencias

Catálogo completo en `REFERENCIAS.md`. Usadas aquí: [R23] (Feathers,
characterization testing), [R24] (IEEE, reverse engineering a requisitos), [R25]
(Reversa, specs legacy para IA), [R26] (Ambler, agile/lean documentation y decay),
[R27] (INCOSE, evolución de sistemas legacy).
