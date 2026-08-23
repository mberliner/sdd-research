# Constitución del proyecto

**Versión:** 0.2.3 | **Ratificada:** 2026-07-31 | **Última enmienda:** 2026-08-22

## Preámbulo

- **Qué es:** lista curada de los principios no-negociables de esta **investigación**. No es documentación de referencia ni protocolo de ejecución diaria: es lo que nunca cede.
- **Cómo se usa:** leer antes de proponer una spec, un documento o un cambio de método. Si una spec o una decisión de redacción entra en conflicto con un principio, **se ajusta la spec, no el principio**.
- **Alcance:** cada principio declara un **invariante** estable y autocontenido. El detalle operativo (que evoluciona) vive en el SSOT referenciado en `Detalle:`. La constitución nunca duplica ese detalle: solo declara el invariante y apunta. Cada principio declara además, en `Verificador:`, qué check determinista lo cubre — o `ninguno`, cuando nada mecánico lo cubre.
- **Qué NO es:** no contiene convenciones de forma ni de léxico —eso vive en `CONVENCIONES.md`— ni el protocolo paso a paso del asistente, que vive en `AGENTS.md`. Ninguno de los dos requiere enmienda constitucional para cambiar.

## Principios

### I. SSOT único por tema

Toda pieza de información normativa —regla, definición, cifra, tabla, convención— vive en exactamente un documento, su SSOT; cualquier otro documento que la necesite la referencia, nunca la reproduce. El mismo invariante rige dentro de un documento: un detalle compartido por varias secciones se declara una vez y las secciones lo referencian. Qué documento es SSOT de qué tema es detalle operativo: vive en la tabla SSOT del registro.

- **Enforcement:** checks de post-generación de `AGENTS.md`; revisión editorial.
- **Verificador:** `ssot-collision`, `normative-block`, `ssot-table`, `scope-home`, `excluded-field` de `tools/check_docs.py` — los dos primeros señalan candidatos a duplicación para que un humano los mire; no afirman que la haya.
- **Detalle:** `SPECS_REGISTRY.md` (tabla SSOT, campo `ssot_level`, alcance por documento); `CONVENCIONES.md` (la clase «convención»: léxico y forma); `00-INDEX.md` (navegación: dónde está cada archivo).

### II. Trazabilidad de afirmación a fuente

Ninguna afirmación factual externa se sostiene sola: cita una referencia `[Rxx]` del catálogo. Una cifra sin fuente es una opinión con formato de dato. Las referencias se anclan a la versión consultada; cuando la fuente cambia de versión, el análisis declara contra qué corte fue hecho.

- **Enforcement:** checks de post-generación de `AGENTS.md`; campo `validacion` de cada spec.
- **Verificador:** `referencias` de `tools/check_docs.py` — verifica que toda `[Rxx]` citada exista en el catálogo, no que toda afirmación factual esté citada. La mitad que importa sigue siendo humana.
- **Detalle:** `REFERENCIAS.md`.

### III. Propagación bidireccional del conocimiento

Un cambio en un SSOT obliga a revisar sus derivados, y un resultado que responde una pregunta abierta de un SSOT sube **primero al SSOT y después a sus derivados**. La dirección ascendente no es opcional: el conocimiento producido por una ejecución entra por abajo. Cerrar un experimento dispara esta revisión aunque el experimento esté exento de spec propia — la exención es de *spec*, no de *propagación*.

- **Enforcement:** sección «Propagacion» de `templates/RESULTADO-EXPERIMENTO.md` (tres checks); campo `Derivados a revisar` del bloque `[SDD-Check]`.
- **Verificador:** `ninguno` — candidato registrado como `M-16` en `agenda/MEJORAS-METODO.md`.
- **Detalle:** `SPECS_REGISTRY.md` (regla de propagación), `comun/SDD-ADAPTATIVO-VS-CASCADA.md` (por qué el circuito es bidireccional).

### IV. Documento autorado, spec registrada

Toda pieza documental autorada por el proyecto está gobernada por una spec registrada antes de escribirse o modificarse. El documento deriva de la spec, no al revés; cuando el documento diverge, se reconcilia la spec (las specs son vivas). Lo exento del registro se declara explícitamente y por criterio, no por omisión.

- **Enforcement:** protocolo previo de `AGENTS.md`; lista de exenciones con su criterio en `SPECS_REGISTRY.md`.
- **Verificador:** `spec-coverage`, `spec-fields`, `deriva-cycle` de `tools/check_docs.py` — es el principio mejor cubierto: el check falla si un documento autorado no tiene spec ni exención declarada.
- **Detalle:** `SPECS_REGISTRY.md`.

### V. Integridad del registro experimental

Un experimento se pre-registra antes de producir su dato: hipótesis, definición operacional y criterio de éxito quedan sellados. Toda enmienda posterior al sello se fecha, se motiva y declara la dirección del sesgo si se conoce. Ninguna hipótesis se formula ni se reescribe después de ver el resultado que la evalúa. Ningún cierre excede el techo de conclusión que su diseño permite.

- **Enforcement:** régimen de sellado y enmiendas de los runbooks; campo `validacion` de las specs de `experimentos/`.
- **Verificador:** `ninguno` — el sellado es una promesa sobre el orden temporal entre pensar y ver, y nada mecánico de este repositorio lo observa.
- **Detalle:** `templates/EXPERIMENTO.md`, `templates/RESULTADO-EXPERIMENTO.md`, `docs-y-investigacion/PLAN-PRUEBAS.md` y `software/PLAN-PRUEBAS.md`.

### VI. Separación método y contenido

Los cambios al método SDD de este repositorio —protocolo del asistente, registro de specs, templates, esta constitución— no son hallazgos de investigación y no se registran como tales: se rigen por esta constitución y se asientan en el historial. Simétricamente, un hallazgo de investigación no modifica el método por sí solo: lo propone, y la adopción es una decisión explícita y fechada.

- **Enforcement:** entrada obligatoria en el historial al cambiar método; revisión de post-generación.
- **Verificador:** `metodo-historial` de `tools/check_docs.py` — corre solo con contexto de commit (modo `--staged`, que invoca el gate `tools/githooks/pre-commit`) y falla si un commit que toca método no asienta una entrada nueva, y arriba, en el historial. Cubre la mitad enunciable del principio; que el cambio esté **bien clasificado** como método y no como hallazgo, y la dirección simétrica —que un hallazgo no mueva el método sin decisión explícita y fechada—, siguen siendo humanas. En un árbol sin git el principio vuelve a no tener verificador.
- **Detalle:** `historial/sdd.md`, `historial/ROADMAP-MEJORAS-SDD.md`.

### VII. Preguntar antes que interpretar

Ante ambigüedad de una spec o de una solicitud, el asistente pregunta; no elige una lectura y sigue. La incertidumbre puntual que no bloquea el resto del trabajo se marca en el borrador de forma grep-able y se resuelve antes de considerar el documento activo. Una solicitud que contradice una spec detiene el trabajo y se explicita: no se procede ni se proponen alternativas sin aprobación.

- **Enforcement:** secciones «Disambiguación» y «Excepciones» de `AGENTS.md`.
- **Verificador:** `clarificacion` de `tools/check_docs.py` — falla si un documento que el registro declara `Activo` conserva un marcador con su pregunta escrita. Cubre la mitad enunciable del principio: que la incertidumbre marcada se resuelva. Que el asistente haya preguntado en vez de interpretar —el caso en que nunca hubo marcador— no lo observa nada.
- **Detalle:** `AGENTS.md`.

## Governance

- **Precedencia:** un principio constitucional prevalece sobre cualquier spec, protocolo o decisión de redacción. El orden completo de fuentes es: esta constitución → `SPECS_REGISTRY.md` → `AGENTS.md` → criterio del asistente. El protocolo del asistente referencia esta constitución pero no la contiene: si se cambia de asistente, la constitución sigue vigente.
- **Versionado semver:** MAJOR remueve o redefine un principio; MINOR agrega un principio o sección; PATCH aclara redacción sin cambiar el invariante.
- **Fase pre-1.0:** el proyecto está en fase pre-madura; MUST NOT declararse `1.0.0` hasta alcanzar madurez sostenida. Mientras tanto la serie es `0.y.z`: lo que tras `1.0.0` sería MAJOR o MINOR sube `y` (`0.y.0`); lo que sería PATCH sube `z` (`0.0.z`).
- **Procedimiento de enmienda:**
  1. Subir la versión según la regla de arriba y actualizar "Última enmienda".
  2. Registrar el cambio en `historial/sdd.md` (qué principio, por qué).
  3. Revisar los SSOTs referenciados por el principio afectado y propagar.
  4. Verificar que ningún documento activo contradiga el principio nuevo o modificado.
- **Límite honesto:** el repositorio no tiene CI. La verificación determinista que existe —`tools/check_docs.py`, que desde el 2026-08-15 corre además en cada commit vía `tools/githooks/pre-commit`— cubre **cinco de los siete** principios: I, II, VI y VII de forma parcial, IV de forma sustantiva. Los otros dos declaran `Verificador: ninguno` y su cumplimiento depende enteramente de que una persona lo mire. El gate se puede saltear con `git commit --no-verify` y se puede desconectar borrando `core.hooksPath`; lo segundo lo detecta el check `gate`, lo primero no lo detecta nada. Ningún verificador, además, juzga **adecuación**: que un documento tenga spec registrada no dice que la spec lo describa bien. Un principio puede violarse sin que nada lo detecte, y el campo `Verificador:` existe para que se sepa cuál.
