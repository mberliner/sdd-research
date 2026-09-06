# Análisis: edición colaborativa de documentos con agentes de IA (Línea A)

Fecha: 2026-09-06.
Fuente: Lehmann, Shauchenka & Buschek — *Collaborative Document Editing with Multiple Users and AI Agents* (ACM CHI 2026; arXiv 2509.11826v2) [R53]. Estudio académico con revisión por pares, vendored en `../fuentes-externas/arXiv-2509.11826v2/`.
Alcance: Línea A (docs e investigación).

---

## Contexto

El paper no es sobre SDD: es un estudio de HCI sobre edición colaborativa de texto con IA. Se cita acá porque es el antecedente académico más directo, y con evidencia primaria verificable, sobre una pregunta que Línea A comparte de fondo — cómo un equipo comparte la autoría y la edición de un documento con un agente de IA, no solo cómo una persona lo hace sola.

Los autores construyen un prototipo de editor colaborativo con dos objetos nuevos y compartidos: **perfiles de agente** (personas de IA configurables) y **tareas de agente** (delegación explícita, visible a todo el equipo). Las respuestas del agente aparecen en la función de comentarios ya existente del editor, no como edición directa del texto. Lo despliegan como *technology probe* durante una semana a 30 participantes en 14 equipos, y analizan logs de interacción más entrevistas grupales semiestructuradas.

Dos preguntas de investigación ordenan el estudio: cómo los co-autores **crean** agentes de IA en un entorno colaborativo (RQ1), y cómo **interactúan** con esos agentes compartidos (RQ2).

---

## Qué mide el estudio, y qué no

Es un estudio **cualitativo y exploratorio**, sin baseline comparativo — decisión explícita de los autores para maximizar el tiempo de los participantes con las funciones nuevas del prototipo. La muestra son escritores académicos (facultad y estudiantes), no representativa de la población general, aunque cubre un rango de experiencia. Salvo un grupo, los integrantes de cada equipo ya se conocían entre sí antes del estudio.

Esto acota qué se puede leer del estudio: reporta **comportamiento observado y percepción declarada** en una ventana de una semana, no eficacia medida de ninguna práctica, y no generaliza a equipos que no se conocen o a dominios fuera de la escritura académica/colaborativa. Los propios autores lo marcan como límite y piden trabajo futuro con muestras más grandes y un despliegue de largo plazo.

---

## Hallazgos centrales

### 1. Los perfiles de agente son territorio del creador

Aunque el diseño permitía a cualquiera editar el perfil de cualquier agente, los participantes casi nunca lo hicieron. Los autores lo leen como territorialidad de escritura (el perfil revela necesidades y preferencias de quien lo escribió, y funciona como un lugar interpersonal, no una acción efímera como apretar un botón) y como una extensión de literatura previa sobre por qué las personas evitan colaborar sobre ciertos objetos (roles de "creador" y "usuario", responsabilidad y crédito).

### 2. Los agentes creados y sus salidas sí son recurso compartido

La distinción central del paper es esta: autoría de la creación del agente vs. uso del agente una vez creado. Un participante crea un agente pensando en el equipo, y el equipo lo usa e integra sus salidas libremente, incluidas las de agentes creados por otra persona. Las salidas del agente (lo que aparece en los comentarios) funcionan como "objeto común" del equipo; el perfil del agente, no.

### 3. Preferencia por control manual sobre autonomía

El prototipo permitía dos modos de disparo de tareas: autónomo (por intervalo, inactividad, todos desconectados, guardado del documento, o después de varias ediciones) y manual (botón, o atajo en la barra de selección de texto). Los participantes prefirieron el control manual. Los comentarios iniciados por agentes de forma autónoma se aceptaron con mucha menor frecuencia que los iniciados por un usuario: los participantes reportaron sentirse abrumados cognitiva y visualmente por intervenciones de IA a nivel de todo el documento, fuera de su foco actual.

### 4. Cuántos agentes: uno por eficiencia, varios por perspectiva

Los equipos deliberaron sobre cuántos agentes crear, con variación incluso dentro de un mismo equipo. Quienes valoraban el uso de IA por su **valor funcional** (velocidad, eficiencia — p. ej. revisar gramática) preferían un solo agente genérico. Quienes valoraban el **valor de perspectiva** (puntos de vista distintos, roles) preferían varios agentes específicos. Algunos participantes conectaron ambos valores: crear un agente con rol/persona específico es una inversión que mejora el *prompting* futuro, porque precarga un objetivo explícito y reduce ambigüedad.

### 5. Los agentes no se tratan como miembros del equipo

Del análisis combinado cuantitativo y cualitativo: los participantes no trataron a los agentes como colaboradores. Les aplicaron normas de autoría y propiedad, los integraron en estructuras de responsabilidad y coordinación existentes (es decir, los trataron como material o herramienta, no como par independiente), y los usaron sobre todo para tareas de tipo herramienta (revisión gramatical) aunque el diseño habilitaba usos más amplios.

---

## Decisiones de diseño con razón explícita

Dos decisiones del prototipo están justificadas en el paper con una razón que vale la pena registrar porque no es obvia:

- **Los agentes responden por comentario, no editando el texto directo.** La justificación es que las ediciones directas cargan significado social (trabajo previo sobre *tracking* de cambios), y presentar una sugerencia como comentario — con apertura para descartarla — es más apropiado, sobre todo cuando los co-autores no se conocen bien entre sí.
- **Un agente por defecto (`@aiAuthor`) disponible sin crear uno propio.** Baja la barrera de entrada: no hace falta pasar por la creación de un perfil para obtener ayuda de IA, que los propios autores citan como una tarea difícil incluso para usuarios individuales.

---

## Qué es transferible como hipótesis para Línea A, y qué no

**Es transferible como hipótesis a poner a prueba, no como hallazgo ya válido acá**, porque el paper mide un editor colaborativo genérico con agentes conversacionales, y este repositorio es un caso distinto: un solo autor humano trabajando con un asistente de código (Claude Code) sobre documentos versionados en git, con spec y checklist antes que "agente con perfil".

Lo que sí es candidato a contrastar contra la experiencia de este repositorio:

- La distinción **autoría-vs-uso** (creación individual, consumo compartido) no tiene equivalente directo acá porque no hay multi-usuario real trabajando en paralelo sobre los mismos documentos. Es una dimensión que este repositorio no puede probar con su corpus actual — dato para `agenda/BACKLOG-INVESTIGACION.md` si se quiere diseñar un experimento con más de un autor humano.
- La **preferencia por control manual sobre autonomía**, y el rechazo a intervenciones fuera de foco, es coherente con el propio protocolo de este repositorio: `AGENTS.md` exige que el asistente pare y pregunte ante ambigüedad (§Disambiguación) en vez de escribir de forma autónoma y amplia. El paralelo es sugerente pero no es evidencia — son dos objetos de estudio distintos (un chat colaborativo humano-humano-IA vs. un protocolo de un solo operador humano).
- La deliberación **uno vs. varios agentes** no tiene análogo directo: este repositorio no usa "agentes con perfil" sino un protocolo escrito (`AGENTS.md`) que cualquier asistente lee igual. La pregunta de fondo — ¿especializar o generalizar el soporte de IA? — sí resuena con la existencia de agentes especializados por lenguaje en la infraestructura del usuario (ver `~/.claude/agents-lib/`), pero comparar ambos requeriría un diseño de experimento propio, no una lectura del paper.

**No es transferible, y no corresponde forzarlo:** cualquier cifra de aceptación de comentarios, de uso de funciones, o de puntaje SUS/CSI del prototipo. Son medidas de un sistema y una tarea que este repositorio no reproduce.

---

## Conclusión para Línea A

El aporte de este paper a Línea A no es un mecanismo para portar, es **vocabulario y una distinción verificada empíricamente** — autoría individual vs. uso compartido, control manual vs. iniciativa autónoma — que Línea A puede usar para nombrar con precisión fenómenos que todavía no midió en su propio corpus. Ninguna de las cinco secciones anteriores habilita, por sí sola, un cambio de método: eso requeriría un experimento propio con un diseño que hoy no existe.

---

[SDD-Check]
- Spec leida: SI (spec registrada en `../SPECS_REGISTRY.md` para este doc, dada de alta en la misma iteracion)
- Incluye/Excluye verificado: SI — no se citan decisiones de adopción de método (no hay ninguna que proponer todavía), no se reproduce detalle de implementación del prototipo ajeno al hallazgo
- Validaciones aplicadas: version anclada en `../REFERENCIAS.md` [R53], vendored en `../fuentes-externas/arXiv-2509.11826v2/`; toda cifra citada (N=30, 14 equipos, una semana) es del paper, marcada como tal; distinción explícita entre lo que el estudio midió y lo que es lectura propia para Línea A (sección homónima); sin emoticones; refs internas verificadas con `../tools/check_docs.py`
- SSOT afectado: ninguno (doc operativo)
- Derivados a revisar: ninguno — este análisis no da de alta ítems de agenda; si se decide diseñar el experimento con más de un autor humano que sugiere la sección de transferibilidad, corresponde a una iteración futura sobre `../agenda/BACKLOG-INVESTIGACION.md`
- Cobertura: completa — los cinco hallazgos y las dos decisiones de diseño del paper quedan caracterizados, y la sección de transferibilidad distingue explícitamente qué es hipótesis y qué queda fuera
- Deuda arrastrada: ninguna
- Riesgos/reservas: es un estudio cualitativo de una semana sin baseline y con muestra no representativa, según lo declaran los propios autores; ninguna comparación con este repositorio es evidencia de nada, es lectura de vocabulario compartido
