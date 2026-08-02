# Análisis: Superpowers y su relación con nuestra investigación SDD (Línea B)

Fecha: 2026-08-02.
Fuente: Superpowers v6.2.0, commit `44c9b2d` (consultada 2026-08-02) [R37]. Clon local vendored en `../fuentes-externas/superpowers/`.
Alcance: Línea B (software).

---

## Contexto

Superpowers es una metodología de desarrollo empaquetada como skills componibles para agentes de codificación, con respaldo comercial (Prime Radiant) y distribución por marketplace de plugins. Se sirve a 11 harnesses desde un set único de 14 skills, con un archivo de protocolo `AGENTS.md` y adaptadores finos por asistente.

Este documento la caracteriza y la mapea contra nuestro protocolo (`../AGENTS.md`, `../SPECS_REGISTRY.md`), del mismo modo y con el mismo instrumento que `ANALISIS-SPEC-KIT.md` hizo con GitHub Spec Kit [R10]. La lectura cruzada de las tres implementaciones —Spec Kit, Superpowers y el proyecto testigo— **no** vive acá: es un tema propio, con su SSOT en `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`.

Importa por qué se la mira ahora. La afirmación de convergencia que este proyecto viene sosteniendo se apoyaba en dos puntos, y uno de ellos —el testigo— deriva de este repositorio, con sesgo de confirmación declarado en B-06. Superpowers es el primer punto que no nació ni de nuestro método ni del de Spec Kit.

---

## Tesis central: no hay Power Inversion

Spec Kit plantea que la spec es el artefacto primario que **genera** el código, y el código la última milla regenerable (`ANALISIS-SPEC-KIT.md`, Power Inversion). Superpowers no sostiene eso. Su spec es un documento de diseño fechado (`docs/superpowers/specs/YYYY-MM-DD-<tema>-design.md`) que produce un plan, y el plan produce código que después se mantiene: nada se regenera desde la spec.

En la taxonomía de Piskala [R30] es **spec-anchored**, no *spec-as-source*. Esto importa para C3 de `ANALISIS-SPEC-KIT.md`, que dejaba abierta la tensión entre "spec como generador" y "spec como representación del conocimiento": Superpowers documenta que la posición intermedia se sostiene en un producto real y activo, no solo como concesión de un contexto sin CI.

---

## Flujo de trabajo

El flujo nuclear son tres skills encadenadas, más un conjunto de skills de disciplina que se disparan solas por descripción.

| Orden | Skill | Función | Artefacto |
|-------|-------|---------|-----------|
| 1 | `brainstorming` | Elicitar la spec por diálogo: una pregunta por mensaje, 2-3 enfoques con recomendación, diseño presentado por secciones con aprobación de cada una | `docs/superpowers/specs/YYYY-MM-DD-<tema>-design.md` |
| 2 | `writing-plans` | Traducir la spec a plan de tareas del tamaño de un ciclo de test, escrito para un ingeniero sin contexto del proyecto | `docs/superpowers/plans/YYYY-MM-DD-<feature>.md` |
| 3 | `subagent-driven-development` | Ejecutar el plan con un subagente fresco por tarea, revisión por tarea (cumplimiento de spec + calidad) y revisión final de rama | código + ledger de progreso |

Rasgos de diseño relevantes:

- **Gate duro previo a todo código.** `brainstorming` declara que no se invoca ninguna skill de implementación ni se escribe código hasta que el diseño esté presentado y aprobado, explícitamente "para todo proyecto, sin importar la simpleza percibida".
- **Contexto construido, no heredado.** Los subagentes nunca reciben el historial de la sesión: se les arma exactamente el contexto que necesitan. Es una decisión de aislamiento que también preserva el contexto del coordinador.
- **Skills auto-disparadas.** El campo `description` de cada skill describe el momento de uso, no la capacidad, de modo que el disparo lo decide el agente al reconocer la situación.
- **Verificación con evidencia como ley.** `verification-before-completion` prohíbe afirmar que algo pasa sin haber corrido el comando en ese mismo mensaje.
- **Tablas de racionalización.** Cada skill de disciplina lista las excusas observadas y su refutación, en vez de reforzar la regla en abstracto.

---

## El método que más aporta: evaluación conductual de la documentación

Es el aporte distintivo de esta fuente y no tiene equivalente en Spec Kit ni en el testigo.

`../fuentes-externas/superpowers/skills/writing-skills/testing-skills-with-subagents.md` define un ciclo RED→GREEN→REFACTOR aplicado a documentos de método: correr escenarios de presión **sin** el documento y capturar las racionalizaciones textuales del agente; escribir el documento contra esas fallas concretas; correr **con** el documento y verificar cumplimiento; cerrar las racionalizaciones nuevas que aparezcan. El criterio de diseño de los escenarios es combinar tres o más presiones simultáneas (tiempo, costo hundido, autoridad, agotamiento) y forzar una elección explícita entre opciones concretas.

Dos propiedades lo vuelven relevante para las deudas metodológicas de este repositorio:

- **La variable de salida es conducta observada en sesión fresca**, no un artefacto documental: qué opción eligió el agente, cuántas herramientas gastó. Es una fuente independiente del artefacto, que es justamente lo que el anti-patrón de confusión de visibilidad —`../agenda/BACKLOG-INVESTIGACION.md`, prioridad alta #6— declara faltante.
- **Corre repeticiones por celda con scoring manual.** El eval de workspace usó 5 subagentes frescos por brazo, 25 repeticiones en total, cada respuesta leída entera. Es el procedimiento que la prioridad alta #7 del mismo backlog pide para conocer el piso de ruido antes de reportar una brecha.

Dos casos concretos, con su archivo de origen para que sean re-verificables:

- **Efecto medido de borrar prosa** (`../fuentes-externas/superpowers/RELEASE-NOTES.md`, v6.2.0): eliminar una sección argumentativa de la skill de TDD degradó la conducta test-first de 8/10 a 5/10 bajo presión, corroborado en dos familias de modelos. Revirtieron el corte y conservaron los argumentos redistribuidos. Es un tamaño de efecto de referencia y una advertencia directa para `M-04` de `../agenda/MEJORAS-METODO.md`: compactar documentos de método tiene un costo conductual que hoy no medimos.
- **Un cierre que no reescribió su hipótesis** (`../fuentes-externas/superpowers/docs/superpowers/specs/2026-07-06-sdd-plan-scoped-workspace-eval-results.md`): la falla hipotetizada —adopción ciega de un registro de progreso ajeno— **no se reprodujo** en ninguna de las 25 repeticiones. En vez de reformular, el documento declara qué reclama y qué no ("what this GREEN round claims, and only claims"), reporta que el mecanismo cambió pero el conteo crudo de herramientas no bajó, y deja el cambio apoyado en razones estructurales con firma del mantenedor. Es Principio V ejecutado por un tercero.

Límite que MUST acompañar cualquier uso de esto: los evals son internos y autoreportados, con n chico y scoring del propio equipo [R37]. Se porta el **procedimiento**; los resultados no se asumen.

---

## Mapeo: Superpowers vs. nuestro protocolo SDD

Se usa el mismo instrumento de ocho filas que `ANALISIS-SPEC-KIT.md`, fijado el 2026-05-24, más de un año antes de que esta fuente se examinara.

| Concepto | Superpowers | Nuestro proyecto |
|----------|-------------|------------------|
| Fuente de autoridad no-negociable | Precedencia declarada: instrucciones del usuario > skills > conducta por defecto. La autoridad última es el humano, no un artefacto del proyecto | `../CONSTITUTION.md` > `../SPECS_REGISTRY.md` > `../AGENTS.md`: la autoridad es del proyecto y sobrevive al cambio de asistente |
| Lenguaje normativo | `MUST`, `ALWAYS`/`NEVER`, bloques `<HARD-GATE>` y "Iron Law"; sin referencia a RFC 2119 | `MUST`/`SHOULD`/`MAY` al inicio de sentencia (`../AGENTS.md`) [R04] |
| Manejo de ambigüedad | Conversacional: una pregunta por mensaje antes de escribir, con gate de aprobación. **Sin marcador de incertidumbre dentro del documento** | `[NEEDS CLARIFICATION: ...]` grep-able + MUST preguntar (`../AGENTS.md`) |
| Validación de consistencia | `verification-before-completion` (evidencia fresca antes de toda afirmación) + revisión por subagente contra la spec en cada tarea y al cerrar la rama | Bloque `[SDD-Check]` por entrega + backstop determinista `../tools/check_docs.py` |
| Trazabilidad requisito a tarea | Ledger de progreso por plan y revisión por tarea contra su spec; **sin coverage mapping** requisito a verificador | Campo `Cobertura` del `[SDD-Check]` + regla de propagación (`../SPECS_REGISTRY.md`) |
| Circuito de aprendizaje | Fuerte, pero **sobre los documentos de método**: evals, tablas de racionalización, bucle de corrección con cortacircuitos. La spec de proyecto es un documento fechado que no se revisa tras la ejecución | Sobre las specs: propagación bidireccional (Principio III) y `Deuda arrastrada` |
| Registro de specs | Archivos fechados en `docs/superpowers/specs/`; sin registro central, sin campo de estado, sin nivel SSOT | `../SPECS_REGISTRY.md` central por documento, con `estado` y `ssot_level` |
| Personalización | Plugins independientes + adaptadores por harness; el núcleo rechaza explícitamente lo específico de dominio | Niveles de profundidad de spec y `ssot_level` |

Lectura del mapeo: convergencia fuerte en lenguaje normativo y en validación de consistencia; parcial en autoridad, ambigüedad y personalización; divergencia en trazabilidad, registro y —la más interesante— en el **objeto** del circuito de aprendizaje. El veredicto de invariancia leído sobre las tres implementaciones vive en `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, no acá.

---

## Conclusiones para Línea B

### C1. La posición spec-anchored tiene un caso de producción

C3 de `ANALISIS-SPEC-KIT.md` dejó abierto hasta dónde conviene mover el entregable hacia "regenerable desde spec". Superpowers ocupa el punto medio deliberadamente y con producto vivo. Sumado a que B-07 cerró sin ventaja del formato híbrido en regenerabilidad (`../experimentos/RESULTADO-EXPERIMENTO-B7.md`), refuerza que la posición intermedia de este proyecto es una elección defendible y no una carencia. **Candidata**, no cambio aprobado: no hay medición comparada entre las tres posiciones.

### C2. El circuito de aprendizaje puede correr sobre el método, no solo sobre las specs

Nuestro Principio III instrumenta propagación sobre las specs y sus derivados. Superpowers instrumenta un bucle sobre sus propios documentos de método, con medición conductual. Son loops complementarios, no rivales: nosotros no tenemos ninguno del segundo tipo, y `../CONSTITUTION.md` declara que su enforcement es humano y a pedido. La pregunta que esto abre está dada de alta en `../agenda/BACKLOG-INVESTIGACION.md` (prioridad alta #8).

### C3. Ausencia de marcador de ambigüedad, con el mismo principio detrás

Superpowers llega al mismo principio que nosotros —no asumir, preguntar— por una vía distinta: gate conversacional antes de escribir, en vez de marcador dentro del documento. Esto **no** debilita nuestro `[NEEDS CLARIFICATION]`: son instrumentos para momentos distintos, uno para la elicitación y otro para la incertidumbre que sobrevive al borrador. Vale como recordatorio de que el marcador no cubre la etapa previa a que exista documento.

### C4. Evidencia externa para la portabilidad entre asistentes

Superpowers sirve 11 harnesses desde un set único con adaptadores finos, y su documentación de aceptación exige demostrar que el bootstrap carga en sesión real, no que los archivos estén copiados. Es evidencia externa de que el patrón `AGENTS.md` como SSOT más adaptadores —que este repositorio y el testigo ya practican— escala más allá de un caso propio, y sostiene `M-03` de `../agenda/MEJORAS-METODO.md`.

### C5. Lo que NO conviene adoptar tal cual

- El registro de specs por archivo fechado, sin estado ni nivel SSOT: es más pobre que nuestro registro central y reintroduce el problema de "qué specs existen y cuál está vigente".
- La autoridad última puesta en el humano de la sesión: para una investigación que quiere sobrevivir al cambio de asistente, la autoridad tiene que ser un artefacto del proyecto.
- El volumen de la biblioteca de skills: 14 skills auto-disparadas tienen un costo de contexto por sesión que la propia fuente reconoce y viene recortando. Un repositorio documental no necesita esa superficie.

---

[SDD-Check]
- Spec leida: SI (spec registrada en `../SPECS_REGISTRY.md` para este doc)
- Incluye/Excluye verificado: SI - la lectura cruzada de tres implementaciones queda excluida y remitida a `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`; el diseño del experimento derivado queda fuera; no se re-analiza el flujo de Spec Kit
- Validaciones aplicadas: version anclada en `../REFERENCIAS.md` [R37]; cada cifra citada declara su archivo de origen en el clon vendored; los evals se presentan como precedente de metodo y no como evidencia de efectividad; mapeo corrido sobre las ocho filas fijadas el 2026-05-24; refs internas verificadas; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: ninguno (doc operativo)
- Derivados a revisar: ninguno; `CONVERGENCIA-IMPLEMENTACIONES-SDD.md` consume este documento como insumo, no deriva de el
- Cobertura: completa - las cinco conclusiones mapean a filas del mapeo o a secciones de caracterizacion, y cada una declara si es candidata o solo lectura
- Deuda arrastrada: el pronostico de divergencia por fila se verifico acá, pero el veredicto de invariancia entre las tres implementaciones queda pendiente del documento de convergencia; los evals de la fuente no fueron ejecutados, solo leidos sus reportes
- Riesgos/reservas: analisis sobre snapshot v6.2.0 commit `44c9b2d`; fuente autoreportada, sin peer review y con interes comercial; la caracterizacion sale de leer skills, release notes y docs internos, no de correr el sistema en vivo
