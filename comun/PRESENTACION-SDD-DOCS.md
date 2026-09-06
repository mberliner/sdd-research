---
marp: true
theme: default
class: lead
paginate: true
backgroundColor: #fff
header: ''
style: |
  header {
    color: #888;
    font-size: 0.5em;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    top: 0.4em;
  }
  section {
    padding-top: 1.6em;
  }
---

# Spec-Driven Development (SDD) para Documentación
## Cómo generar información de calidad con colaboración, versionado e IA

---

<!-- _header: '**Fundamentos** > Aplicación > Equipo e IA > Implementación > Cierre' -->

# ¿Qué es SDD para Docs?

Adaptamos prácticas estructuradas de código a la creación de documentación. 

- **Especificaciones (Specs) primero:** En `SPECS_REGISTRY.md`, cada documento define su propósito y límite antes de escribirse.
  *¿Por qué?* Evita el desvío de alcance ("scope creep"). Establece un contrato claro sobre qué contenido pertenece a dónde.
- **SSOT (Single Source of Truth):** Cada regla vive en un solo lugar.
  *¿Por qué?* Elimina la desactualización silenciosa. Si un dato cambia, se actualiza una vez, previniendo versiones contradictorias.
- **Validación Determinista:** Uso de scripts (ej. `check_docs.py`).
  *¿Por qué?* Mecaniza la higiene (enlaces rotos, duplicaciones). Libera al humano para que revise valor, no formato.

---

<!-- _header: '**Fundamentos** > Aplicación > Equipo e IA > Implementación > Cierre' -->

# Hallazgos Propios (Experimentos Cerrados)

- **Un gate que falla en silencio no gobierna.** En un experimento de este proyecto, el hook de enforcement resolvía el intérprete de Python y, si no lo encontraba, dejaba pasar la edición sin avisar — nunca llegó a ejecutarse en ninguna de las celdas del experimento.
  *Hallazgo transferible:* un control de gobernanza mal diseñado puede fallar abierto justo donde más hace falta.
- **Declarar "no sirve" en vez de forzar un resultado.** En otro experimento el instrumento de medición tocó el techo de su propio diseño (12 de 12 PASS en calibración): el protocolo exige registrar **NO APTO** y rediseñar, no maquillar la medición para que dé un resultado presentable.

---

<!-- _header: 'Fundamentos > **Aplicación** > Equipo e IA > Implementación > Cierre' -->

# Casos de uso (I)

**Gestión y gobierno**
- OKRs, Roadmaps, historias de usuario: cocrear el roadmap de equipo, área, compañía
- Informes de gestión: a comité, dirección, otras áreas; resultados de revisión de herramientas y plataformas
- Auditorías y políticas: informes y procesos con formato estándar; Política de Gobierno de IA, Seguridad, Comunidades

---

<!-- _header: 'Fundamentos > **Aplicación** > Equipo e IA > Implementación > Cierre' -->

# Casos de uso (II)

**Conocimiento compartido**
- Presentaciones: compartir conocimiento de manera colaborativa
- Conocimiento general: wikis, repositorios Git

**Desarrollo con IA**
- Prompts, skills, plugins: conocimiento cocreado para agentes

---

<!-- _header: 'Fundamentos > **Aplicación** > Equipo e IA > Implementación > Cierre' -->

# Dato, Información, Conocimiento y Sabiduría

La jerarquía DIKW, aplicada a documentos

- **Dato:** cifra, letra, palabra, token
- **Información:** datos con su contexto y organización (quién, qué, dónde, cuándo)
- **Conocimiento:** información integrada con experiencia (cómo), permite actuar
- **Sabiduría:** comprensión profunda (por qué); juicio para evaluar; aplicado a decisión/estrategia; visión de futuro

Dato (en el mundo) -----> Información -----> Conocimiento (en el agente)

*SDD interviene en el primer salto: specs y SSOT son el contexto que convierte dato en información confiable.*

---

<!-- _header: 'Fundamentos > Aplicación > **Equipo e IA** > Implementación > Cierre' -->

# Beneficios para el Trabajo en Equipo

- **Colaboración asíncrona:** El versionado (Git) permite trabajar en paralelo.
  *¿Por qué?* Deja un rastro de cada cambio y el motivo de cada decisión en el historial. No hay ediciones fantasma.
- **Propagación Controlada:** Atributo `deriva_de` en las specs.
  *¿Por qué?* Si un origen cambia (ej. Catálogo de Servicios), la regla obliga a revisar sus derivados, garantizando que el impacto fluya y nada quede obsoleto.
- **Alineación sin ambigüedades:** La tabla SSOT indica dónde va cada cosa.
  *¿Por qué?* Elimina el debate de "dónde pongo este nuevo control" y evita esparcir conocimiento en anexos sin conexión.

---

<!-- _header: 'Fundamentos > Aplicación > **Equipo e IA** > Implementación > Cierre' -->

# SDD y la Asistencia por IA (I): el protocolo interno

La IA no opera como un generador libre; actúa gobernada por el protocolo:

- **Lectura obligatoria de Specs:** La IA lee el contrato del documento antes de escribir.
  *¿Por qué?* Corta las alucinaciones de raíz. Limita a la IA a redactar solo lo que el alcance le permite.
- **Reporte de Transparencia:** Cada entrega incluye un bloque `[SDD-Check]`.
  *¿Por qué?* Hace auditable a la IA. Le exige declarar qué validó y qué deuda dejó, en lugar de entregar una "caja negra".
- **Disambiguación:** 
  *¿Por qué?* Previene que la IA adivine la intención del usuario. Si hay duda, el protocolo le prohíbe asumir y la obliga a detenerse y preguntar.

---

<!-- _header: 'Fundamentos > Aplicación > **Equipo e IA** > Implementación > Cierre' -->

# SDD y la Asistencia por IA (II): hallazgos externos

Un estudio de CHI 2026 con 30 personas en 14 equipos [R53] confirma dos decisiones del protocolo:

- **Control manual, no iniciativa autónoma.** Los equipos rechazan intervenciones de IA fuera de foco o no pedidas: las aceptaron con mucha menor frecuencia que las que ellos mismos dispararon.
  *¿Por qué?* Es el mismo principio que Disambiguación aplicado a la iniciativa: el protocolo hace que la IA pare y pregunte en vez de actuar sola.
- **El protocolo se comparte, el agente no.** Los equipos no tratan a la IA como un miembro más: el perfil/configuración del agente es territorio de quien lo creó, pero lo que ese agente produce sí se comparte y reutiliza.
  *¿Por qué?* Es la misma separación que ya aplica este proyecto: `AGENTS.md` (el protocolo que gobierna al asistente) es fijo por diseño; sus salidas (`.md` versionados) son las que circulan y se comparten en equipo.

---

<!-- _header: 'Fundamentos > Aplicación > Equipo e IA > **Implementación** > Cierre' -->

# Antecedentes de Industria (I): precedentes

- **Docs as Code** [R51]: desde 2013 (comunidad Write the Docs) y consolidado en 2017 (*Docs Like Code*, Anne Gentle), trata la documentación como el código — versionada en Git, revisada, validada en CI.
  *¿Por qué importa?* Es el precedente directo del paradigma `.md` exclusivo de este proyecto: la industria ya validó tratar el documento como artefacto versionado.
- **DITA** [R52]: desde 2005 (estándar OASIS), define alcance y gobernanza **antes** de escribir, por tópico. Antecedente histórico de "spec antes de redactar" — se cita solo por eso, sin profundizar.

---

<!-- _header: 'Fundamentos > Aplicación > Equipo e IA > **Implementación** > Cierre' -->

# Antecedentes de Industria (II): el aporte propio

- **La spec-antes-de-escribir es un aporte propio de este proyecto.** Ni Docs as Code ni DITA exigen un contrato de propósito+incluye/excluye por documento como `SPECS_REGISTRY.md`; eso se suma acá, inspirado en la disciplina *spec-first* que la industria ya usa para generación de código [R10].
  *¿Por qué distinguirlo?* No reclamamos adopción de industria para "spec de alcance por documento" tal como la hace este proyecto — sí para "doc versionado y validado como código" y para "estructura definida antes de escribir". Lo primero es la extensión que este trabajo propone.

---

<!-- _header: 'Fundamentos > Aplicación > Equipo e IA > **Implementación** > Cierre' -->

# El Paradigma ".md" Exclusivo y Exportación

Trabajamos internamente y versionamos *únicamente* archivos de texto plano (`.md`).

- **Edición exclusiva en texto plano:** 
  Los formatos binarios (`.docx`, `.pdf`) no se llevan con el control de versiones. Git en `.md` permite ver con precisión quirúrgica qué palabra cambió.
  La IA Generativa se lleva muy bien con el formato markdown y los humanos también pueden leerlo.
- **Skill de Exportación (`md-to-docx`):**
  *¿Por qué?* Separa el contenido de la presentación visual. Cuando el contenido está listo, la IA usa este skill para inyectar la plantilla corporativa oficial y generar el `.docx` publicado, manteniendo el repositorio limpio.

---

<!-- _header: 'Fundamentos > Aplicación > Equipo e IA > **Implementación** > Cierre' -->

# El Ciclo de Vida de un Documento Normativo

1. **Spec:** Se define el rol y los límites. (*Para acordar qué haremos*)
2. **Aprobación:** Se ratifica el alcance. (*Para no redactar en vano*)
3. **Edición (Humano/IA):** Se redacta referenciando el SSOT. (*Para evitar duplicar texto*)
4. **Validación:** Checks automáticos en el commit. (*Para garantizar higiene antes de fusionar*)
5. **Cierre:** Se asientan cambios en `CHANGELOG.md`. (*Para mantener trazabilidad futura*)
6. **Construcción y Exportación:** Se invoca el skill `md-to-docx`. (*Para generar el entregable final con el formato corporativo oficial, listo para publicar*)

---

<!-- _header: 'Fundamentos > Aplicación > Equipo e IA > **Implementación** > Cierre' -->

# ¿Cuándo aplicar SDD?

**Aplicar cuando el documento...**
- Es normativo o de referencia: lo va a leer y citar más de una persona
- Va a cambiar con el tiempo y necesita historial de por qué cambió
- Tiene varios autores o se edita con IA sin supervisión línea a línea
- Su contenido se referencia desde otros documentos (riesgo de desactualización)

**No es necesario cuando...**
- Es una nota efímera, un borrador descartable o uso personal
- Es un documento de una sola vez, sin reuso ni derivados
- El costo de definir spec supera el valor de lo que se va a escribir

---

<!-- _header: 'Fundamentos > Aplicación > Equipo e IA > Implementación > **Cierre**' -->

# Conclusión (I): un sistema que se autocorrige

SDD no es una promesa — ya mostró que se autocorrige:

- Detectó un gate que fallaba en silencio.
- Declaró **NO APTO** en vez de forzar un resultado presentable.
- Cada entrega deja rastro auditable (`[SDD-Check]`).

Eso es lo que distingue un sistema vivo de un documento estático: **se audita a sí mismo, en público.**

---

<!-- _header: 'Fundamentos > Aplicación > Equipo e IA > Implementación > **Cierre**' -->

# Conclusión (II): próximo paso

Adoptar SDD en el proyecto de Gobierno de IA transforma documentos estáticos en un **sistema vivo**:

- **Confiable:** las validaciones evitan contradicciones normativas.
- **Auditable:** se sabe el cuándo, quién y por qué de cada cambio.
- **Potenciado por IA:** el asistente redacta y audita bajo reglas estrictas.

**Próximo paso:** aplicar el protocolo a [documento/área concreta] y correr `check_docs.py` como gate de aceptación.
