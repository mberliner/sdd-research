# Análisis: sdd-first y su relación con nuestra investigación SDD (Línea B)

Fecha: 2026-08-15.
Fuente: sdd-first v0.1.0, commit `ebfbd67` (2026-08-14), rama `main`, árbol limpio [R39]. Clon vendored en `../fuentes-externas/sdd-first/`.
Alcance: Línea B (software).

---

## Contexto

sdd-first es un andamiaje SDD instalable: se clona una vez, se siembra dentro de otro proyecto con `core/sdd_init.py` y después se descarta. Lo que deja en el proyecto destino es una constitución, un registro de specs, un gate que bloquea editar código sin spec vigente declarada, un pipeline determinista de verificación y siete skills servidas a cuatro asistentes desde una fuente única. Todo se parametriza en `.sdd/config.yaml`. Se desarrolla usando su propio método: 25 specs propias, `historial/sdd.md` por iteración y bloque `[SDD-Check]` en el commit de cierre.

Este documento lo caracteriza y lo mapea contra nuestro protocolo (`../AGENTS.md`, `../SPECS_REGISTRY.md`) con el mismo instrumento de ocho filas que `ANALISIS-SPEC-KIT.md`, `ANALISIS-SUPERPOWERS.md` y `ANALISIS-OPENSPEC.md`. La diferencia con esos tres está en la sección siguiente y condiciona todo lo que viene después: **esta fuente no es externa**.

---

## Procedencia: por qué NO cuenta como linaje

`CONVERGENCIA-IMPLEMENTACIONES-SDD.md` exige que todo caso nuevo declare su procedencia antes de contarse, y su regla 1 dice que un método que hereda la anatomía de otro no agrega un linaje sino una copia. Aplicado acá, el filtro no deja lugar a duda.

**Mismo autor y misma cadena.** sdd-first es del autor de este repositorio. Su núcleo generaliza el tooling del proyecto testigo: `core/check_traceability.py`, `core/sdd_gate.py` y `core/check_constitution.py` son los mismos scripts que `../agenda/MEJORAS-METODO.md` registra en la columna «Origen» como provenientes del testigo (M-01, M-02). La cadena es este repositorio → testigo → kit, y el testigo ya estaba declarado como un solo linaje junto con este repositorio.

**Arrastra vocabulario que nació acá.** Su `AGENTS.md` y sus plantillas exigen el bloque `[SDD-Check]`, que es el protocolo de entrega de `../AGENTS.md`. Su registro de specs tiene una columna `Formato` con valores `hibrido` y `casero`: ese par es el factor experimental de B-07 (`../experimentos/EXPERIMENTO-B7-formato-hibrido.md`), acuñado en este repositorio. Su constitución usa la forma invariante + `Enforcement` + `Detalle` de `../CONSTITUTION.md`. Ninguna de las tres es una coincidencia que se pueda contar como convergencia.

**Arrastra también la difusión desde Spec Kit que ya teníamos declarada.** Sus playbooks `analyze` y `clarify` dicen en su primera línea «adaptado de `/speckit.analyze`» y «adaptado de `/speckit.clarify`» — las dos prácticas que `ANALISIS-SPEC-KIT.md` (C1, C2) ya declaró adoptadas por este proyecto. El kit es descendiente de dos casos del corpus, no un punto nuevo.

**Consecuencia.** MUST NOT sumarse como columna en `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, y ningún acuerdo entre este documento y aquel método puede leerse como evidencia de invariancia: es autocorrelación. Lo que sí tiene es el interés que la regla 1 admite explícitamente para los casos que no suman linaje — madurez y ergonomía de un método conocido —, y por eso su lugar es este análisis individual.

**Lo que gana el corpus a cambio.** Es el único caso donde el método de este linaje está **ejecutado por código de punta a punta**, con un pipeline que sale VERDE o ROJO. Sirve como banco de pruebas de mecanismos que acá siguen siendo prosa, incluidos los que ya fallaron. Esa es la única lectura que este documento sostiene.

---

## Qué hay adentro

### Las tres capas de enforcement

`../fuentes-externas/sdd-first/docs/SDD-ENFORCEMENT.md` es su SSOT y declara tres capas, la misma arquitectura que `../agenda/MEJORAS-METODO.md` M-01 dice haber portado del testigo:

| Capa | Mecanismo | Qué garantiza |
|------|-----------|---------------|
| Gate de autoría (preventivo) | `core/sdd_gate.py`, disparado antes de editar código | Que exista una spec vigente declarada en `.sdd/current-spec`, registrada y con FR escritos |
| Backstop determinista | `core/check_traceability.py` en el pipeline | Estructura de la spec, consistencia disco↔registro, cobertura FR→test en specs `active` |
| Capa semántica | Skills `analyze` (read-only) y `clarify` (≤5 preguntas) | Adecuación: si la spec describe *bien* el cambio |

El límite es el mismo que `AGENTS.md` declara acá para `check_docs.py`: presencia y forma, no adecuación.

### Artefactos generados, no escritos

`CONSTITUTION.md`, `SPEC-000-naming.md`, el workflow de CI y todo el *wiring* de los gates se generan con `core/render.py` desde `.sdd/config.yaml` y `templates/wiring/`. Editarlos a mano está prohibido por su `AGENTS.md`. La entrada de historial del 2026-08-14 documenta por qué: el wiring existía duplicado y derivó en silencio — un bloque de 37 líneas sobrevivió una spec entera en una rama inalcanzable, y el sync lo borró sin que nadie lo buscara.

### Skills multi-asistente desde una fuente

Dos lugares editables por skill —el playbook en `docs/playbooks/` (contenido, agnóstico de asistente) y el `SKILL.md` fuente en `.agents/skills/` (wrapper)— y de ahí `core/gen_skill_adapters.py` genera los formatos de Claude Code y opencode; Codex y Antigravity leen la fuente directo. Sin symlinks, a propósito: se degradan en Windows sin Developer Mode (`../fuentes-externas/sdd-first/docs/SKILLS-MULTITOOL.md`).

### Actualización de instalaciones derivadas

`core/sdd_update.py` propaga versiones nuevas del kit a un proyecto ya instalado: muestra el plan sin escribir salvo `--apply`, nunca pisa una plantilla editada y deja la versión nueva como `<archivo>.kit-new` para fusionar a mano. Es propagación de método a través de una frontera de repositorios, con detección de conflictos.

---

## El rasgo que más aporta: el enforcement declarado se verifica como cableado

Es el aporte con menos equivalente en el corpus y el que toca de frente una deuda medida de este proyecto.

Cada principio de su constitución declara en el config, además del invariante, la tool que lo hace cumplir y —opcionalmente— el **paso del pipeline** que la activa. `core/check_constitution.py` verifica que ese paso exista y esté cableado en `pipeline.steps`; el paso `constitution` corre *después* de los pasos de enforcement, para verificar que hayan corrido y no solo que estén declarados. Su SPEC-020 dice por qué se escribió: el mapa tool→paso vivía hardcodeado, lo que no estaba en él «pasaba en silencio», y declarar un principio nuevo sobre esa base habría producido «un enforcement decorativo en la constitución del propio kit — el fallo que el kit existe para evitar».

El mecanismo no impide un principio sin mecanización: la omite explícitamente. Su Principio IV declara `enforcement: AGENTS.md` y ningún `step`, y el comentario del config dice que eso significa un enforcement que el pipeline no activa. Lo que el diseño produce no es enforcement universal sino **visibilidad de qué principio tiene mecanismo y cuál depende de que alguien se acuerde**.

Contraste directo con este repositorio: los siete principios de `../CONSTITUTION.md` declaran `Enforcement:`, y los siete nombran prosa — «checks de post-generación de `AGENTS.md`», «revisión editorial», «campo `validacion` de cada spec». Ninguno nombra algo que corra. `../tools/check_docs.py` existe y verifica bastante, pero ningún principio lo nombra y nada verifica que la relación entre principio y verificador sea otra cosa que una intención escrita.

Y hay evidencia propia de que la distinción no es teórica: la prioridad alta #4 de `../agenda/BACKLOG-INVESTIGACION.md` documenta que el gate del testigo **falló abierto en silencio durante todo B-07** —sin intérprete, `exit 0`— y se creyó activo durante todo el diseño. sdd-first es la respuesta de ingeniería a ese hallazgo: la rama fail-closed del hook de Claude Code, el adaptador de Antigravity que traduce cualquier excepción a `deny` porque ese CLI es fail-open, el `deny` total servido desde archivo cuando no hay intérprete, el bootstrap automático de los hooks de git al correr el pipeline. Es la deuda #4 pagada en un repositorio de código; acá sigue abierta como pregunta de investigación.

---

## Mapeo: sdd-first vs. nuestro protocolo SDD

Se usa el instrumento v1, las mismas ocho filas fijadas el 2026-05-24, sin agregar ni redefinir ninguna. Recordatorio de la sección de procedencia: las coincidencias de esta tabla **no** son convergencia, porque los dos lados son el mismo linaje. Lo que la tabla muestra es dónde el mismo método, al pasar a código, se quedó igual y dónde tuvo que cambiar.

| Concepto | sdd-first | Nuestro proyecto |
|----------|-----------|------------------|
| Fuente de autoridad no-negociable | `CONSTITUTION.md` **generado** desde `.sdd/config.yaml`, con `check_constitution.py` verificando forma y cableado del enforcement declarado; precedencia principio > spec > implementación | `../CONSTITUTION.md` > `../SPECS_REGISTRY.md` > `../AGENTS.md`, escritos a mano, con enforcement declarado en prosa |
| Lenguaje normativo | `MUST:` / `SHOULD:` / `MAY:` como keyword inicial obligatoria de cada FR, verificada por script; sin referencia a RFC 2119 | `MUST`/`SHOULD`/`MAY` al inicio de sentencia (`../AGENTS.md`) [R04], verificación humana |
| Manejo de ambigüedad | Skill `clarify`, hasta 5 preguntas dirigidas grabadas en `## Clarifications` de la propia spec; **sin marcador `[NEEDS CLARIFICATION]`** (0 ocurrencias en el clon). El `AGENTS.md` obliga a consultar ante duda de qué spec aplica | `[NEEDS CLARIFICATION: ...]` grep-able + MUST preguntar en lugar de interpretar (Principio VII) |
| Validación de consistencia | Tres capas: gate preventivo `sdd_gate.py`, backstop `check_traceability.py` + `check_constitution.py` en `core/pipeline.py` (VERDE/ROJO, pasos declarados en config), y skill `analyze` por juicio | Backstop determinista `../tools/check_docs.py` (ERROR/WARN) + bloque `[SDD-Check]` por entrega; sin capa preventiva |
| Trazabilidad requisito a verificador | Tabla *Coverage mapping* obligatoria en specs `hibrido` + `active`, y desde su SPEC-024 el script exige que el **ID del FR aparezca como token completo dentro del test**, no solo que el archivo exista | Campo `Cobertura` del `[SDD-Check]`, en prosa, sin verificador |
| Circuito de aprendizaje | Sobre las specs (entrada de `historial/sdd.md` por iteración, `[SDD-Check]` en el commit de cierre), sobre el método propio (`docs/IDEAS.md` de ideas pre-spec que se promueven a spec con puntero) y hacia afuera (`sdd_update.py` propaga a instalaciones derivadas) | Sobre las specs: propagación bidireccional (Principio III) y `Deuda arrastrada`, ambas manuales; `../agenda/MEJORAS-METODO.md` cumple el papel de `IDEAS.md` |
| Registro de specs | `specs/SPECS_REGISTRY.md` central por capacidad, con `Estado`, `Iteración` y `Formato`, más un **grafo tipado de relaciones entre specs** (seis campos en tres pares simétricos) cuya reciprocidad y coherencia de estado verifica el script | `../SPECS_REGISTRY.md` central por documento, con `estado`, `ssot_level` y `deriva_de`; reciprocidad no verificada |
| Personalización | `.sdd/config.yaml` como único punto de parametrización (dominio, principios, capas, pasos, palabras vetadas, umbrales), adaptadores de lenguaje por contrato (`adapters/CONTRACT.md`) y generación de skills para cuatro asistentes | Niveles de profundidad de spec y `ssot_level`; tooling propio Claude-only, que es lo que `../agenda/MEJORAS-METODO.md` M-03 declara incoherente |

Lectura del mapeo: el método sobrevive el pasaje a código en siete de las ocho filas sin cambiar de idea, y cambia en una — el manejo de ambigüedad, donde el marcador `[NEEDS CLARIFICATION]` desapareció y quedó solo la sesión de `## Clarifications`. Como los dos lados son el mismo linaje, la fila informativa es esa: **el instrumento que este proyecto adoptó de Spec Kit no sobrevivió su propia implementación**, y el kit no declara por qué.

---

## Conclusiones para Línea B

### C1. Un principio con `Enforcement:` en prosa no es verificable, y eso es corregible hoy

Los siete principios de `../CONSTITUTION.md` nombran como enforcement documentos y revisiones humanas. sdd-first muestra la alternativa barata: que el principio nombre un verificador ejecutable cuando exista, y que declare explícitamente su ausencia cuando no. La versión chica y aplicable acá no requiere ningún pipeline: basta con que cada principio declare qué check de `../tools/check_docs.py` lo cubre, o `ninguno` si nada lo cubre, y que `check_docs.py` verifique que los nombrados existen. **Candidata**, no cambio aprobado — se propone como `M-15` en `../agenda/MEJORAS-METODO.md`.

### C2. La cobertura verificada por token es la brecha más concreta

Nuestro campo `Cobertura` es prosa que el autor de la entrega escribe sobre sí mismo. Su SPEC-024 cierra exactamente el hueco equivalente del lado del código —un requisito «verde» sobre un test que en realidad prueba otra cosa— exigiendo que el ID del FR aparezca como token completo en el archivo de test, con el cuidado explícito de no usar substring (`FR-1` dentro de `FR-10`). La traducción documental es directa: un derivado declarado en `Derivados a revisar` podría verificarse contra el disco y contra la tabla SSOT. **Candidata** (`M-16`), con la reserva de que en un repo documental el vínculo requisito→verificador no tiene un análogo tan limpio como FR→test.

### C3. M-02 tiene un resultado negativo ajeno que MUST incorporar antes de implementarse

`../agenda/MEJORAS-METODO.md` M-02 está **Aprobada** y describe su diseño incluyendo «chequeo de mtime: la spec MUST haberse editado después de declararse». Ese criterio se implementó en sdd-first y falló en las dos direcciones: bloqueó flujo legítimo (trabajar una spec en varios commits, `git checkout`, `clone`, el propio ciclo stash/restore de `pre-commit`, que renueva mtimes) y no detuvo a nadie, porque un `touch` lo satisfacía. Se reemplazó por un criterio de **contenido**: la spec debe existir, figurar en el registro con estado `draft` o `active`, y tener al menos un requisito con texto propio además del keyword — los placeholders de la plantilla no cuentan. Implementar M-02 con el diseño escrito hoy es repetir un error ya pagado. **Cambio de contenido en M-02**, no de estado: sigue Aprobada, con la nota incorporada.

### C4. El gate documental tiene tres modos de falla ya identificados, gratis

Además del mtime, sdd-first documenta tres cosas que M-02 va a encontrar: que el gate debe fallar **cerrado** y cómo hacerlo en un harness que es fail-open por diseño; que la escritura por `Bash` escapa a cualquier hook `PreToolUse` porque no declara `file_path`, y que la respuesta correcta es correr la capa al commit en vez de parsear la línea de comandos; y que un reset post-commit evita que una spec quede «vigente» indefinidamente por descuido. Los tres son transferibles a un `.sdd/current-doc` sin cambiar nada. **Lectura** que acompaña a C3.

### C5. La incoherencia que M-03 declara ya está resuelta del otro lado

M-03 dice que este proyecto investiga SDD multi-asistente y su tooling es Claude-only. sdd-first sirve siete skills a cuatro asistentes desde una fuente única con un generador de 4 KB, y el modelo de capas —playbook agnóstico como SSOT del contenido, wrapper fino por asistente, adaptadores generados y committeados con cabecera «NO EDITAR A MANO»— es exactamente lo que M-03 propone. No hay que diseñarlo: hay que decidir si se porta. **Candidata** (`M-17`), con la reserva de que acá no hay generador y portarlo trae la dependencia de Python que hoy solo tiene `check_docs.py`.

### C6. Lo que NO conviene traer

- **Su relación con la ambigüedad.** El kit dejó caer `[NEEDS CLARIFICATION]` sin declarar por qué. Acá el marcador es Principio VII y está en uso; el hecho de que la implementación del propio linaje lo haya perdido es una observación sobre el kit, no un argumento para removerlo.
- **El pipeline completo.** `../CONSTITUTION.md` describe un repositorio documental sin CI y `M-07` mantiene esa premisa bajo revisión. Un pipeline de diez pasos con `pytest`, `ruff` y `mypy` no tiene objeto acá; lo portable es el patrón de declarar el enforcement y verificar que corrió, no el motor.
- **El kit como instalación.** `core/sdd_init.py` siembra un andamiaje pensado para un proyecto de software con `source_roots`. Este repositorio no tiene código de producto, y su modo `none` —solo gobernanza y specs— no está probado para un repo documental de 44 documentos con registro por documento y niveles SSOT.
- **Su acuerdo con nuestro método como respaldo.** Vale repetirlo porque es la tentación obvia: que un kit escrito por el mismo autor reproduzca siete de ocho filas no confirma nada del método. Es la misma trampa que `CONVERGENCIA-IMPLEMENTACIONES-SDD.md` corrigió al descontar al testigo del conteo de linajes.

---

[SDD-Check]
- Spec leida: SI (spec registrada en `../SPECS_REGISTRY.md` para este doc)
- Incluye/Excluye verificado: SI - no se toca la lectura cruzada de convergencia (remitida a `CONVERGENCIA-IMPLEMENTACIONES-SDD.md`), no se re-analiza ningun otro framework, no se toman decisiones de adopcion (las candidatas van a `../agenda/MEJORAS-METODO.md` como M-15/M-16/M-17 en estado Propuesta)
- Validaciones aplicadas: version anclada en `../REFERENCIAS.md` [R39] con commit `ebfbd67` y estado del arbol declarado; procedencia resuelta antes de la lectura y con conclusion explicita de que NO suma linaje, con tres clases de evidencia (mismo autor y misma cadena de tooling, vocabulario propio de este repo, difusion desde Spec Kit ya declarada); ninguna coincidencia del mapeo se presenta como convergencia y la advertencia esta escrita dos veces, en el encabezado de la tabla y en C6; la fuente no reporta ninguna medicion y eso queda dicho; cada rasgo citado declara su archivo de origen en el clon vendored; mapeo corrido sobre el instrumento v1 sin agregar ni redefinir filas; refs internas verificadas con `../tools/check_docs.py`; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: ninguno (doc operativo). `software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md` recibe una fila de procedencia que registra el caso como no-linaje, sin cambiar ningun veredicto ni el conteo de cuatro linajes
- Derivados a revisar: `../agenda/MEJORAS-METODO.md` (M-02 incorpora el resultado negativo de C3; M-15/M-16/M-17 dadas de alta como Propuesta); `../agenda/BACKLOG-INVESTIGACION.md` prioridad alta #4 (el fail-closed que la pregunta pide ya tiene una implementacion de referencia; la pregunta sigue abierta porque nadie midio su costo operativo) - señalado, sin modificar
- Cobertura: completa - las seis conclusiónes mapean a filas del mapeo o a secciones de caracterizacion, y cada una declara si es lectura, candidata o cambio; las tres candidatas tienen ID de destino en `../agenda/MEJORAS-METODO.md`
- Deuda arrastrada: la de `CONVERGENCIA-IMPLEMENTACIONES-SDD.md` sigue intacta y este documento no la toca (Kiro sin leer, dimension «como llega el metodo al agente» sin veredicto, corpus observacional de OpenSpec sin dar de alta, tercer eje propuesto y sin cerrar); se agrega una propia: **por que el kit dejo caer `[NEEDS CLARIFICATION]` no esta declarado en la fuente y este analisis no lo resuelve**; y M-15/M-16/M-17 quedan en Propuesta, sin aprobacion
- Riesgos/reservas: el analisis lee documentos, specs, config e historial del clon, sin correr `sdd_init.py` ni el pipeline, asi que las capacidades descritas son las declaradas por la fuente y no verificadas por ejecucion; la fuente es del mismo autor que este repositorio, con sesgo de confirmacion estructural y no solo probable, y por eso ninguna de sus coincidencias se cuenta como evidencia; el clon vendored es un directorio de trabajo vivo, no un snapshot congelado, asi que la lectura vale para el commit declarado y puede desactualizarse sin aviso
