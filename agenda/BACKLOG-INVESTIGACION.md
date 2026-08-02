# Backlog de Investigacion Futura

Agenda de **preguntas abiertas** sobre SDD: se cierran con evidencia (experimento o analisis), no con una edicion.

Los cambios al **metodo** de este repositorio viven en `MEJORAS-METODO.md`, que es donde se declara el criterio de separacion entre ambos backlogs y como conviven los items con contraparte de los dos lados (Principio VI).

## Prioridad alta
1. Medir variabilidad entre asistentes IA en tareas de especificacion.
2. Identificar campos minimos de spec por tipo de documento.
3. Definir umbral objetivo para pasar de control manual a control automatizado.
7. **Medir el piso de ruido del instrumento antes de reportar una brecha (alta, 2026-07-31).** Cuando la medicion la produce una sesion de modelo, la misma unidad medida dos veces con la misma regla da valores distintos. En B-07 (b) esa discrepancia resulto de **5 a 8 veces** la brecha entre brazos que se pretendia leer, y dejo `H1` NO CONCLUYENTE. Procedimiento barato: correr el **brazo control dos veces** bajo la misma regla y reportar la discrepancia junto al resultado; si es del orden de la brecha, no hay señal que reportar. Corolario: una comparacion cuya direccion **cambia con la convencion de conteo** no es propiedad del corpus sino de la medicion. Evidencia: `../experimentos/RESULTADO-EXPERIMENTO-B7.md` §Resultado del criterio (b).
4. **Gates de gobernanza que fallan ABIERTO: deteccion y diseno fail-closed.** Origen: hallazgo en B-07 (`../experimentos/PRUEBA-REGENERABILIDAD-B7.md` §4.4-bis). El hook `PreToolUse` del proyecto testigo resuelve su interprete (`.venv/bin/python`, `Scripts/python.exe`, `where python`) y termina en `[ -f "$PYBIN" ] || exit 0` — **si no encuentra interprete, sale 0 y permite la edicion**. En los 4 workspaces del experimento no habia `.venv`, asi que el gate **nunca se ejecuto** y el enforcement estuvo caido **en silencio**: se creyo activo durante todo el diseno. Preguntas: como detectar que un gate esta caido (heartbeat / self-test del enforcement / assert de arranque); cuando un gate debe fallar **cerrado** (bloquear) en vez de abierto y que costo operativo tiene; como versionar el enforcement para que no dependa de artefactos no versionados (un venv local). Nota: falla abierto **justo en el entorno menos preparado** (clon limpio, sin instalar) — el peor momento posible. Aplica a cualquier proyecto SDD con enforcement por hooks, no solo al testigo.
5. Disenar el regimen de permisos/harness en experimentos de regeneracion para que midan el modelo y no el harness. Origen: **halt-on-permission** observado en B-07 (`../experimentos/PRUEBA-REGENERABILIDAD-B7.md` §2.7): con Bash denegado para preservar la pureza one-shot de R1, el modelo a veces trata el montaje del entorno (`venv`) como prerequisito bloqueante y **aborta pidiendo aprobacion** en vez de degradar a "escribir codigo sin verificar" — produciendo una corrida nula (VOID) de forma estocastica. Preguntas: como neutralizar la auto-verificacion sin sesgar R1 (denegar Bash vs. sandbox read-only vs. venv pre-montado neutro); como garantizar degradacion graceful en vez de aborto; a partir de que tasa de VOID el regimen de permisos domina la varianza y amenaza la comparabilidad. Aplica a **cualquier** experimento de regeneracion one-shot, no solo B-07.

6. **Anti-patron: variable de salida que es artefacto del propio tratamiento (confusion de visibilidad).** Origen: degradacion de H2 en B-07 (`../experimentos/EXPERIMENTO-B7-formato-hibrido.md`, changelog 2026-07-29). Cuando el tratamiento es un **formato o regimen de documentacion** y la variable de salida es **ella misma un artefacto documental** (revisiones de spec registradas, specs revisadas tras ejecucion, requisitos declarados), el tratamiento altera la **observabilidad** del resultado y no solo el resultado: un formato que obliga a documentar hace mas visibles sus propias revisiones, asi que "revisó menos" es indistinguible de "documento menos sus revisiones". Sin fuente independiente del artefacto la metrica es inutilizable como evidencia, y los conteos crudos pueden apuntar en direccion **contraria** a la hipotesis por puro artefacto de medicion (en B-07: entradas de `## Historial`, media 6.0 casero vs 7.0 hibrido). Familia de casos ya observados: H2 (este), los dos items que `R5` tuvo que descartar por depender del tratamiento (`../experimentos/PRUEBA-REGENERABILIDAD-B7.md` §3.6-bis), y la asimetria de ontologia del Hallazgo 5 (`../experimentos/RESULTADO-EXPERIMENTO-B7.md`). Corolario operativo asociado: **`N/A` no es `0`** — contar ocurrencias de una seccion que solo una anatomia contempla convierte una asimetria de formato en un valor medido y produce una tautologia a favor del tratamiento. Preguntas: como detectar esta confusion **en el diseno** (¿la variable de salida sobreviviria si el tratamiento no existiera?); que fuentes independientes del artefacto sirven de control (historia de VCS, telemetria, observador externo) y que hacer cuando no existen; que clase de hipotesis sobre formatos son testeables de raiz y cuales solo admiten lectura cualitativa. Aplica a **cualquier** experimento donde el tratamiento sea una practica documental — es decir, a buena parte de la agenda SDD.

8. **¿El protocolo del asistente cambia la conducta del agente? Medirlo sobre conducta, no sobre documentos (alta, 2026-08-02).** Todo el método de este repositorio está sin evaluar: `../CONSTITUTION.md` declara que su enforcement es humano y a pedido, y nadie midió si leer el protocolo produce alguna diferencia de comportamiento. La pregunta es directa: ¿un agente que opera con `../AGENTS.md` —y en particular con el bloque `[SDD-Check]`— verifica antes de afirmar, y pregunta en vez de interpretar, más que uno que no lo tiene?

   Lo que vuelve la pregunta abordable hoy es que existe un diseño ajeno y probado para medirla: el ciclo RED→GREEN sobre documentación de [R37] —correr escenarios de presión **sin** el documento, capturar las racionalizaciones textuales, correr **con** el documento y comparar—, con dos propiedades que atacan de frente dos deudas de esta agenda. Primero, la variable de salida es **conducta observada en sesión fresca** (qué opción eligió el agente, cuántas herramientas gastó), no un artefacto documental: es la fuente independiente del artefacto que el anti-patrón de arriba (#6) declara faltante, y por lo tanto la única variante de la pregunta que escapa a la confusión de visibilidad. Segundo, corre varias repeticiones por celda con scoring manual, que es exactamente el procedimiento que #7 pide para conocer el piso de ruido antes de reportar una brecha.

   Precedente de tamaño de efecto para dimensionar el diseño: borrar una sección de prosa de un documento de método hizo caer la conducta esperada de 8/10 a 5/10, corroborado en dos familias de modelos [R37]. Sirve además como advertencia sobre la compactación de documentos, que es la contraparte de método `M-04` en `MEJORAS-METODO.md`: si compactar degrada conducta de forma medible, compactar a ciegas tiene un costo desconocido.

   Reservas de diseño: los evals de la fuente son internos y autoreportados, así que se porta el **procedimiento**, no sus resultados; y la elección de escenarios de presión es un grado de libertad que MUST sellarse antes de ver datos (Principio V).

## Prioridad media
1. Evaluar impacto de lenguaje normativo (MUST/SHOULD/MAY) en calidad de salida.
2. Analizar costo/beneficio de contract-first en servicios legacy.
3. Evaluar fatiga operacional por checklists en equipos pequenos.

## Prioridad exploratoria
1. Que gana y que pierde un repo documental al pasar de verificacion humana a evaluacion automatica parcial sin CI (scripts locales): que clase de deriva atrapa y cual se le escapa. *(La construccion del script es mejora de metodo — `MEJORAS-METODO.md` M-01, aprobada el 2026-07-31; aca queda la pregunta que su ejecucion permite responder.)*
2. Generar indice de madurez SDD de doble eje (docs vs software).
3. Comparar frameworks emergentes orientados a agentes IA.

## Circuitos de aprendizaje y cascada encubierta (prioridad alta)

1. Medir tasa de divergencia entre specs y documentos derivados en proyectos activos.
2. Identificar señales tempranas de congelamiento de spec (cascada encubierta) y definir umbral de alarma.
3. Comparar calidad de decision en proyectos con revision de spec cadenciada vs sin cadencia.
4. Definir la cadencia minima de revision de specs por tipo de proyecto (docs vs software).

## LLM Wiki (Karpathy) como SDD automatizado — tension no resuelta (prioridad alta)

Origen: caso I-021 en `../../investigaIA/casos/llm-wiki-karpathy/RESULTADO-llm-wiki-karpathy.md` (repositorio hermano)

El patron LLM Wiki de Karpathy [R19] es SDD Linea A implementado con delegacion total al LLM: la capa raw/ es la matriz de fuentes, la wiki/ es el cuerpo de SSOTs derivados, y CLAUDE.md es la spec operativa del mantenedor. La diferencia critica es que el mantenedor es la IA, no un humano.

Esto abre preguntas de investigacion directas para SDD:

1. **Clausula de autonomia**: que operaciones de ingesta pueden ser autonomas (el LLM escribe directamente sobre la wiki) y cuales requieren aprobacion humana explicita antes de modificar un SSOT? Criterio propuesto de partida: autonoma si la pagina afectada es derivada (ssot_level=derivado); requiere aprobacion si es SSOT primario.

2. **Amplificacion del riesgo de alucinacion**: SDD Linea A identifica "alucinacion o extrapolacion no sustentada" como riesgo tipico. En LLM Wiki el blast radius es mayor — el error se escribe directamente en el SSOT y puede propagarse a paginas derivadas antes de ser detectado. Pregunta: que mecanismos de linting automatico son suficientes como sustituto de la revision humana pre-commit?

3. **CLAUDE.md como spec SDD ejecutable**: el archivo CLAUDE.md del patron Karpathy cumple la misma funcion que una spec SDD (define alcance, incluye/excluye, reglas de consistencia). Pregunta: puede formalizarse un subconjunto de la especificacion SDD como instrucciones ejecutables para un agente LLM? Esto conecta con el item "Definir umbral objetivo para pasar de control manual a control automatizado" (prioridad alta, arriba).

4. **Metricas de calidad para wikis mantenidas por IA**: el patron carece de metricas formales (critica documentada en LLM Wiki v2). SDD tiene metricas para Linea A (tasa de hallazgos sin fuente primaria, tasa de contradicciones detectadas). Pregunta: son esas metricas suficientes para evaluar una wiki mantenida por IA, o se necesitan metricas adicionales especificas (ej. tasa de alucinaciones estructurales, tasa de supersedencias incorrectas)?

## Transferencia de conceptos de Spec Kit a Linea A (prioridad media)

Origen: `../software/ANALISIS-SPEC-KIT.md` (analisis de GitHub Spec Kit v0.8.13 [R10]).

Spec Kit es Linea-B-nativo (no tiene funcion nativa para documentos de analisis/conocimiento). Diferido: desarrollar la transferencia a Linea A solo cuando Linea B avance y haya claridad. Conceptos candidatos a transferir:

1. `/speckit.checklist` ("unit tests for English"): validar completitud, claridad y consistencia de requisitos en prosa. Aplicabilidad a checks de calidad de documentos de investigacion (Linea A).
2. ~~Marcador `[NEEDS CLARIFICATION: ...]` como convencion comun a ambas lineas (candidato C2 del analisis).~~ **ADOPTADO**: vive en `../AGENTS.md` §Disambiguacion, comun a ambas lineas.
3. Modelo presets/extensions como via para adaptar un toolkit Linea-B a flujos de documentacion.

Cuando un concepto de esta lista pasa de candidato a decision de adopcion, deja de ser pregunta de investigacion: se da de alta en `MEJORAS-METODO.md` con su estado.

## Fuente reservada: "From Spark to Fire" (multi-agente) — para uso futuro (prioridad exploratoria)

Paper vendored en `fuentes-externas/arXiv-2603.04474v1/` ("From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration"). **No es referencia activa** (descartado de B-07 el 2026-07-09: su topología es un grafo de colaboración multi-agente con propagación adversarial hacia *falso consenso*, ajena al pipeline lineal de un solo modelo que mide la regenerabilidad de B-07). Se conserva porque encaja en tres líneas que el proyecto podría abrir:

1. **Orquestación multi-agente del propio método SDD.** Si el SDD llegara a coordinar varios agentes IA colaborando (uno redacta spec, otro implementa, otro revisa), su modelo de propagación (grafo de dependencias, condición temprana de amplificación β·ρ(A) > δ) y su capa de gobernanza por genealogía (procedencia de afirmaciones, screening tri-estado, rollback forzado) serían directamente aplicables a la confiabilidad de esa colaboración. Conecta con "Medir variabilidad entre asistentes IA" (prioridad alta, arriba).
2. **Cascada encubierta en topología multi-agente.** Formaliza cómo errores menores se "solidifican en falso consenso a nivel de sistema" — análogo multi-agente de la cascada encubierta de `../comun/SDD-ADAPTATIVO-VS-CASCADA.md`. Candidato a cross-ref si esa línea se extiende más allá del circuito humano-mediado.
3. **Modelo de amenazas de pipelines SDD.** Su encuadre de ataque (inyección de un error atómico "role-consistent" que evade validación) es una referencia de threat-modeling si se analiza la manipulación adversarial de specs o de mensajes entre agentes.

## Enriquecimientos diferidos desde verificación de fuentes R25/R30 (prioridad media)

Origen: verificación en fuente completa de R25 y R30 (2026-07-10, ver `../historial/sdd.md`). Ambas fuentes traen material que **refuerza sin corregir** documentos existentes; se difiere su incorporación para no engordar SSOTs sin una decisión que lo habilite.

1. **Regla de decisión de rigor mínimo [R30] → candidata para `../comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md`.** Piskala formula una "Golden Rule": *usar el mínimo nivel de rigor de especificación que elimine la ambigüedad del contexto* — spec-first para desarrollo inicial asistido por IA, spec-anchored para sistemas productivos de vida larga, spec-as-source solo cuando el tooling de generación es maduro y confiable. Complementa el catálogo de escenarios con una regla de *cuánto* SDD aplicar, no solo *cuándo*. Incluye además el anti-catálogo (cuándo SDD es overkill: prototipos descartables, proyectos solo/cortos, exploración, CRUD simple).
2. **Catálogo de pitfalls [R30] → candidato a cross-ref desde `../comun/SDD-ADAPTATIVO-VS-CASCADA.md`.** Cinco fallas predecibles al adoptar SDD: sobre-especificación (spec que es pseudo-código), *specification rot* (la spec deriva del código por falta de enforcement — el análogo directo de la cascada encubierta), spec como burocracia, complejidad de tooling, y falsa confianza (tests de spec verdes no garantizan software correcto si la spec está mal). Refuerzan la tesis del doc sin contradecirla.
3. **Modelo de confianza confirmado/inferido/gap [R25].** Migrado el 2026-07-31 a `MEJORAS-METODO.md` M-06: es una convención de escritura, es decir método, no pregunta de investigación.

## Criterio de priorizacion
- Impacto en riesgo o calidad.
- Esfuerzo real del equipo.
- Reusabilidad entre lineas de investigacion.
- Dependencias tecnicas.
