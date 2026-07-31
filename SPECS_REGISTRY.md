# SPECS REGISTRY

Registro central de specs del proyecto `SDD`.

## Norma de interpretacion
- `MUST`: obligatorio.
- `SHOULD`: recomendado fuerte; si no se cumple, debe justificarse.
- `MAY`: opcional.

## Precedencia
1. `CONSTITUTION.md` MUST prevalecer sobre todo lo demas: declara los invariantes no-negociables. Si una regla de este registro entra en conflicto con un principio, se ajusta la regla, no el principio.
2. Este archivo (`SPECS_REGISTRY.md`) MUST prevalecer para alcance y validacion por documento.
3. `AGENTS.md` SHOULD regir la ejecucion diaria.
4. El criterio del asistente MAY usarse solo cuando no haya conflicto con 1, 2 y 3.

Division de trabajo: `CONSTITUTION.md` declara **que nunca cede** (invariante; cambia por enmienda versionada). Este registro declara **como se aplica hoy** (alcance por documento, convenciones de forma, exenciones; cambia sin enmienda).

## Reglas globales
- Todo cambio documental MUST mapearse a una spec registrada.
- Si un documento no tiene spec, se MUST crear spec minima antes de modificar contenido.
- El nivel de detalle de cada spec SHOULD seguir la tabla de profundidad (ver sección siguiente).
- Los checks de validacion MAY ejecutarse manualmente (contexto sin CI).
- Sin emoticones en documentos de contenido.
- Fechas en formato YYYY-MM-DD.
- No duplicar contenido entre SSOTs: referenciar, no repetir.
- **Alcance de un documento: un solo lugar (regla operativa del Principio I).** Los campos `proposito`, `incluye`, `excluye` y `validacion` MUST vivir unicamente en este registro. Ningun otro documento los reproduce ni los parafrasea:
  - `00-INDEX.md` responde *donde esta cada archivo* (ruta de lectura y ubicacion), no *que contiene cada doc* ni *quien es SSOT de que tema* — esa tabla vive aca, acoplada a la regla de propagacion. Su tabla de estructura MUST declarar rol (`SSOT` / `derivado` / `operativo`), no proposito.
  - El encabezado de un documento MAY llevar **una** linea de identidad para quien lo abre suelto; MUST NOT enumerar `incluye`/`excluye` ni criterios de validacion.
  - Motivo: el 2026-07-31 se midio la divergencia real — 11 filas de `00-INDEX.md` repetian el `proposito` del registro y 5 ya habian derivado (perdiendo, entre otras cosas, la procedencia de `ROADMAP-MEJORAS-SDD.md` y el alcance «contexto del repositorio» de `AGENTS.md`).
  - Migracion: los encabezados de documentos preexistentes SHOULD limpiarse de forma oportunista al tocarlos, no en una reescritura masiva.
- Ortografía: el contenido en español MUST usar ortografía correcta con tildes y signos (acentos, "ñ", apertura de interrogación/exclamación). Aplica a documentos nuevos y a todo documento que se edite. Excepciones: identificadores técnicos, rutas, nombres de archivo y claves de los bloques normativos (ej. campos del `[SDD-Check]` y nombres de campo de spec como `validacion`, `proposito`) MUST conservarse sin tildes por estabilidad grep-able. Los documentos preexistentes sin tildes SHOULD migrarse de forma oportunista al tocarlos, no en una reescritura masiva.

## Campo ssot_level
- `SSOT`: fuente autoritativa del concepto.
- `derivado`: sintetiza un SSOT. MUST incluir campo `deriva_de` apuntando al SSOT de origen.
- `operativo`: guia, indice o plantilla.

Campo `deriva_de`: en specs con `ssot_level: derivado`, indica el archivo SSOT de origen. Habilita trazabilidad de propagacion.

Regla de propagacion:
- Si cambia un SSOT, sus derivados MUST revisarse y el resultado SHOULD registrarse en la entrega.
- Si un resultado responde una pregunta abierta de un SSOT, MUST propagarse **primero al SSOT y después a sus derivados**. La regla anterior sólo cubre la dirección descendente; el conocimiento producido por una ejecución entra por abajo.
- **Cerrar un experimento MUST disparar esta misma revisión**, aunque `experimentos/` esté exento de spec propia: la exención es de *spec*, no de *propagación*. Sin esta regla el cierre no modifica ningún SSOT y por lo tanto no dispara nada — que es lo que ocurrió con B-07 (2026-07-28), cuyo resultado dejó cuatro documentos afirmando lo contrario durante un día. Procedimiento mecánico en `templates/RESULTADO-EXPERIMENTO.md`, sección «Propagacion».

## Campo `estado`
- `Activo` (default — no requiere marcarlo): spec vigente y en uso.
- `Borrador`: spec propuesta, pendiente de aprobacion.
- `Deprecado`: el documento fue eliminado o archivado.

Regla: al deprecar un documento, marcar su spec con `estado: Deprecado` antes de archivar.

## Profundidad de spec

| Nivel | Campos | Aplicar a |
|-------|--------|-----------|
| Minima | `path`, `proposito`, `ssot_level`, `owner`, `validacion` | indices, plantillas, operativos simples |
| Estandar | minima + `incluye`, `excluye` | SSOTs simples, derivados |
| Extendida | estandar + `refresh`, requisitos con `[ ]` | SSOTs criticos con multiples derivados |

`owner` ausente MUST leerse como `proyecto SDD` (unico owner mientras el repo sea de un solo equipo). Se escribe explicito solo cuando difiere del default; asi el campo no se vuelve ruido repetido en 25 specs.

## Docs excluidos del registro (no necesitan spec)
- Archivos fuente originales (.pdf, .docx, .xlsx, .pptx)
- Reportes auto-generados (.conversion_report.json)
- Notas de sesion sin estructura formal
- Contenido en `experimentos/` **generado desde templates** (los templates si tienen spec): diseños de experimento (`EXPERIMENTO-*.md`) y resultados (`RESULTADO-EXPERIMENTO-*.md`). La exención es de **spec propia**, no de **propagación**: cerrar un experimento MUST disparar la revisión de la seccion «Regla de propagacion».
  - **Los runbooks de método NO estan exentos (aclarado 2026-07-30).** Un runbook (`PRUEBA-*.md`) vive en `experimentos/` pero **no deriva de ningun template**: es un documento autorado de protocolo de medicion, con definicion operacional, roles y fases. Al no ser generado desde template, la exencion de arriba no lo alcanza y MUST tener spec registrada. Hueco detectado el 2026-07-30: los dos runbooks de B-07 estaban sin spec y se venian modificando, contra la regla global «todo cambio documental MUST mapearse a una spec registrada». Criterio para clasificar un `.md` de `experimentos/`: ¿su estructura la fija un template del proyecto? Exento. ¿La fija su autor? Necesita spec.
- Codigo de verificacion en `tools/`: no es pieza documental autorada (Principio IV habla de documentos). Su contrato de uso se declara en `AGENTS.md` §Al cerrar una iteracion; lo que verifica y lo que MUST NOT pretender verificar vive en su docstring.
- Repositorios externos clonados (vendored) en `fuentes-externas/` — material fuente de referencia, no autorado por el proyecto. La version analizada se ancla en `REFERENCIAS.md`; el analisis propio si tiene spec (ver `software/ANALISIS-SPEC-KIT.md`).

## Tabla SSOT

| Linea | Concepto | SSOT | Quien referencia |
|------|----------|------|------------------|
| Comun | Principios no-negociables de la investigacion | `CONSTITUTION.md` | `AGENTS.md`, `SPECS_REGISTRY.md`, `00-INDEX.md`, `README.md` |
| Comun | Mejoras al metodo SDD del repositorio | `MEJORAS-METODO.md` | `06-BACKLOG-INVESTIGACION-FUTURA.md`, `historial/sdd.md` |
| Comun | Modelo dual SDD | `MARCO-COMPARATIVO-DOS-LINEAS.md` | `README.md`, `00-INDEX.md`, planes de linea |
| Comun | SDD adaptativo y circuitos de aprendizaje | `SDD-ADAPTATIVO-VS-CASCADA.md` | `docs-y-investigacion/LINEAS-INVESTIGACION.md`, `software/LINEAS-INVESTIGACION.md` |
| Comun | Referencias [Rxx] | `REFERENCIAS.md` | todos los docs con citas `[Rxx]` |
| Comun | Frameworks/proyectos lideres | `PROYECTOS-LIDERES-Y-FRAMEWORKS.md` | `LINEAS-INVESTIGACION.md` de ambas lineas |
| Comun | Tendencias y estadistica | `ESTADISTICAS-TENDENCIAS-EVOLUCION.md` | `06-BACKLOG`, `MARCO-COMPARATIVO-DOS-LINEAS.md`, `ESCENARIOS-QUE-JUSTIFICAN-SDD.md` |
| Comun | Escenarios que justifican SDD | `ESCENARIOS-QUE-JUSTIFICAN-SDD.md` | `README.md`, `00-INDEX.md`, `MARCO-COMPARATIVO-DOS-LINEAS.md` |
| Comun | Implementacion pragmatica sin CI | `IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md` | `PLAN-PRUEBAS.md` de ambas lineas |
| Docs/Investigacion | Agenda linea A | `docs-y-investigacion/LINEAS-INVESTIGACION.md` | `PLAN-PRUEBAS.md`, `NECESIDADES-Y-METRICAS.md` linea A |
| Docs/Investigacion | Metricas linea A | `docs-y-investigacion/NECESIDADES-Y-METRICAS.md` | `PLAN-PRUEBAS.md` linea A |
| Docs/Investigacion | Plan experimental linea A | `docs-y-investigacion/PLAN-PRUEBAS.md` | `00-INDEX.md` global y de linea; `experimentos/` de linea A al cerrar |
| Software | Agenda linea B | `software/LINEAS-INVESTIGACION.md` | `PLAN-PRUEBAS.md`, `NECESIDADES-Y-METRICAS.md` linea B |
| Software | Metricas linea B | `software/NECESIDADES-Y-METRICAS.md` | `PLAN-PRUEBAS.md` linea B |
| Software | Plan experimental linea B | `software/PLAN-PRUEBAS.md` | `00-INDEX.md` global y de linea; `software/LINEAS-INVESTIGACION.md`; `experimentos/` (disenos y resultados B-06/B-07) |
| Software | Protocolo de medicion de B-07 (el «como») | `experimentos/PRUEBA-REGENERABILIDAD-B7.md` (metrica primaria) y `experimentos/PRUEBA-OBSERVACIONAL-B7.md` (corpus observacional) | `experimentos/RESULTADO-EXPERIMENTO-B7.md`; enmiendas y bitacora del repo de datos `experimentosdd-b7/` |

## Specs registradas (MVP)

### CONSTITUTION.md
- `path`: `CONSTITUTION.md`
- `proposito`: SSOT de los invariantes no-negociables de la investigacion — lo que ninguna spec, protocolo ni decision de redaccion puede contradecir.
- `ssot_level`: `SSOT`
- `owner`: proyecto SDD
- `incluye`:
  - preambulo: que es, como se usa, alcance y que NO es
  - principios, cada uno con invariante autocontenido + `Enforcement` + `Detalle` (SSOT donde vive el detalle operativo)
  - governance: precedencia de fuentes, versionado semver, fase pre-1.0, procedimiento de enmienda, limite honesto del enforcement
- `excluye`:
  - convenciones de forma (fechas, ortografia, nomenclatura) — viven en este registro
  - el protocolo paso a paso del asistente — vive en `AGENTS.md`
  - el detalle operativo de cada principio — vive en el SSOT que el principio referencia en `Detalle:`
- `validacion`:
  - [ ] cada principio declara un invariante autocontenido, sin duplicar el detalle que referencia
  - [ ] cada principio tiene `Enforcement` y `Detalle` con SSOT existente
  - [ ] version, fecha de ratificacion y de ultima enmienda presentes y coherentes con `historial/sdd.md`
  - [ ] la precedencia declarada coincide con la de este registro y la de `AGENTS.md`
  - [ ] ningun documento activo contradice un principio vigente

### README.md
- `path`: `README.md`
- `proposito`: entrada y navegacion del proyecto.
- `ssot_level`: `operativo`
- `tono`: humano y descriptivo — es el primer contacto con el proyecto, no un documento tecnico.
- `incluye`:
  - proposito del repo
  - enlaces a documentos nucleares
- `excluye`:
  - detalle metodologico profundo
- `validacion`:
  - [ ] links internos vigentes
  - [ ] no contradice SSOTs
  - [ ] tono narrativo, sin lenguaje normativo (MUST/SHOULD/MAY)

### 00-INDEX.md
- `path`: `00-INDEX.md`
- `proposito`: indice de navegacion global — responde donde esta cada archivo y en que orden leerlo.
- `ssot_level`: `operativo`
- `incluye`:
  - ruta de lectura recomendada con links a documentos nucleares
  - links a `CONSTITUTION.md`, `SPECS_REGISTRY.md` y `AGENTS.md`
  - estructura del proyecto: tabla directorio/archivo → **rol** (`SSOT` / `derivado` / `operativo`)
- `excluye`:
  - alcance de cada documento (`proposito`/`incluye`/`excluye`/`validacion`) — vive en este registro
  - mapa tema → SSOT — vive en la tabla SSOT de este registro
  - definiciones conceptuales extensas
- `validacion`:
  - [ ] enlaces vigentes
  - [ ] links a `CONSTITUTION.md`, `AGENTS.md` y `SPECS_REGISTRY.md` presentes
  - [ ] la tabla de estructura declara rol, no proposito
  - [ ] sin duplicacion de SSOT

### MARCO-COMPARATIVO-DOS-LINEAS.md
- `path`: `MARCO-COMPARATIVO-DOS-LINEAS.md`
- `proposito`: SSOT de diferencias entre linea A y linea B.
- `ssot_level`: `SSOT`
- `incluye`:
  - necesidades y riesgos por linea
  - metricas por linea
- `excluye`:
  - resultados de experimentos concretos
- `validacion`:
  - [ ] separacion explicita A/B
  - [ ] no mezcla metrica de lineas

### ESCENARIOS-QUE-JUSTIFICAN-SDD.md
- `path`: `ESCENARIOS-QUE-JUSTIFICAN-SDD.md`
- `proposito`: SSOT del catálogo de problemas y escenarios (modos de fallo) que justifican adoptar SDD hoy.
- `ssot_level`: `SSOT`
- `owner`: proyecto SDD
- `incluye`:
  - causas raíz transversales
  - escenarios por línea A, línea B y transversales
  - mapa escenario → eje SDD que lo mitiga
- `excluye`:
  - cifras cuantitativas (viven en `ESTADISTICAS-TENDENCIAS-EVOLUCION.md` — referencia)
  - dinámica de cascada/feedback loops (vive en `SDD-ADAPTATIVO-VS-CASCADA.md` — referencia)
- `validacion`:
  - [ ] cada afirmación externa tiene `[Rxx]`
  - [ ] no duplica cifras de `ESTADISTICAS` ni el tratamiento de cascada de `SDD-ADAPTATIVO` — referencia
  - [ ] escenarios separados por línea A / B / transversal
  - [ ] no contradice SSOTs activos

### PROYECTOS-LIDERES-Y-FRAMEWORKS.md
- `path`: `PROYECTOS-LIDERES-Y-FRAMEWORKS.md`
- `proposito`: SSOT de frameworks y proyectos de referencia.
- `ssot_level`: `SSOT`
- `incluye`:
  - referencias de docs/investigacion y software
  - marcos transversales
- `excluye`:
  - estadistica de adopcion
- `validacion`:
  - [ ] cada bloque enlaza [Rxx]

### ESTADISTICAS-TENDENCIAS-EVOLUCION.md
- `path`: `ESTADISTICAS-TENDENCIAS-EVOLUCION.md`
- `proposito`: SSOT de datos cuantitativos y tendencias.
- `ssot_level`: `SSOT`
- `incluye`:
  - cifras y su referencia [Rxx]
  - implicaciones por linea
- `excluye`:
  - decisiones operativas finas
- `validacion`:
  - [ ] cifras con fuente [Rxx]
  - [ ] fecha de consulta indicada

### IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md
- `path`: `IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md`
- `proposito`: SSOT de adopcion pragmatica en contexto sin CI.
- `ssot_level`: `SSOT`
- `incluye`:
  - decisiones de enfoque
  - roadmap 0-90 dias
  - criterio para escalar tooling
- `excluye`:
  - detalle de resultados experimentales
- `validacion`:
  - [ ] contexto sin CI explicito
  - [ ] criterios de evolucion definidos

### REFERENCIAS.md
- `path`: `REFERENCIAS.md`
- `proposito`: SSOT de bibliografia y enlaces [Rxx].
- `ssot_level`: `SSOT`
- `incluye`:
  - catalogo [Rxx]
- `excluye`:
  - interpretacion extensa
- `validacion`:
  - [ ] ids [Rxx] sin duplicados
  - [ ] enlaces legibles

### docs-y-investigacion/LINEAS-INVESTIGACION.md
- `path`: `docs-y-investigacion/LINEAS-INVESTIGACION.md`
- `proposito`: SSOT de agenda de investigacion linea A.
- `ssot_level`: `SSOT`
- `validacion`:
  - [ ] hipotesis explicitas
  - [ ] preguntas accionables

### docs-y-investigacion/NECESIDADES-Y-METRICAS.md
- `path`: `docs-y-investigacion/NECESIDADES-Y-METRICAS.md`
- `proposito`: SSOT de metricas linea A.
- `ssot_level`: `SSOT`
- `validacion`:
  - [ ] metrica con definicion
  - [ ] umbral inicial definido

### docs-y-investigacion/PLAN-PRUEBAS.md
- `path`: `docs-y-investigacion/PLAN-PRUEBAS.md`
- `proposito`: SSOT experimental linea A.
- `ssot_level`: `SSOT`
- `validacion`:
  - [ ] experimento con criterio de exito
  - [ ] enlace a templates

### software/LINEAS-INVESTIGACION.md
- `path`: `software/LINEAS-INVESTIGACION.md`
- `proposito`: SSOT de agenda de investigacion linea B.
- `ssot_level`: `SSOT`
- `validacion`:
  - [ ] hipotesis explicitas
  - [ ] cubre contrato, pruebas, IA

### software/NECESIDADES-Y-METRICAS.md
- `path`: `software/NECESIDADES-Y-METRICAS.md`
- `proposito`: SSOT de metricas linea B.
- `ssot_level`: `SSOT`
- `validacion`:
  - [ ] metricas DORA y requisitos
  - [ ] riesgos y mitigaciones

### software/PLAN-PRUEBAS.md
- `path`: `software/PLAN-PRUEBAS.md`
- `proposito`: SSOT experimental linea B.
- `ssot_level`: `SSOT`
- `validacion`:
  - [ ] metrica primaria por experimento
  - [ ] criterio de adopcion definido

### docs-y-investigacion/00-INDEX.md y software/00-INDEX.md
- `path`: `docs-y-investigacion/00-INDEX.md`
- `path`: `software/00-INDEX.md`
- `proposito`: indice de navegacion de su linea — pregunta central, gobernanza aplicable y lectura sugerida.
- `ssot_level`: `operativo`
- `validacion`:
  - [ ] links vigentes
  - [ ] direccionan a SSOT de su linea

### templates/EXPERIMENTO.md y templates/RESULTADO-EXPERIMENTO.md
- `path`: `templates/EXPERIMENTO.md`
- `path`: `templates/RESULTADO-EXPERIMENTO.md`
- `proposito`: plantillas para disenar y cerrar experimentos — fijan los campos minimos y el procedimiento de propagacion; los documentos generados desde ellas quedan exentos de spec propia.
- `ssot_level`: `operativo`
- `validacion`:
  - [ ] campos minimos para ejecutar y cerrar experimentos
  - [ ] `EXPERIMENTO.md` incluye la seccion «Definicion operacional» (obligatoria desde 2026-07-28, ver `experimentos/RESULTADO-EXPERIMENTO-B7.md` Hallazgo 7)
  - [ ] el criterio de exito se enuncia solo contra metricas que la propia prueba produce, con comprobacion de satisfacibilidad
  - [ ] `RESULTADO-EXPERIMENTO.md` incluye la seccion «Propagacion» con el grep de deuda declarada y la tabla de triaje (obligatoria desde 2026-07-29)
  - [ ] `EXPERIMENTO.md` incluye «Documentos que esperan este resultado»; su contraparte en el cierre es «Propagacion»
  - [ ] la deuda no resuelta migra a `06-BACKLOG-INVESTIGACION-FUTURA.md` antes de cerrar, no queda atada al siguiente cierre

### SPECS_REGISTRY.md
- `path`: `SPECS_REGISTRY.md`
- `proposito`: SSOT del registro central de specs — alcance y validacion por documento.
- `ssot_level`: `SSOT`
- `owner`: proyecto SDD
- `validacion`:
  - [ ] todos los .md activos tienen spec registrada
  - [ ] specs minimas tienen al menos 5 campos

### AGENTS.md
- `path`: `AGENTS.md`
- `proposito`: SSOT del protocolo operativo y contexto del repositorio para asistentes IA (estandar cross-asistente).
- `ssot_level`: `SSOT`
- `owner`: proyecto SDD
- `incluye`:
  - orden de lectura previo a cualquier cambio (constitucion -> indice -> spec del doc)
  - protocolo durante el cambio y disambiguacion
  - checks de post-generacion y bloque `[SDD-Check]`
  - cierre de iteracion (registro, historial, commit)
  - criterios de calidad, ciclo de vida de specs, «Que NO hacer», excepciones, convenciones
- `excluye`:
  - invariantes y su justificacion — viven en `CONSTITUTION.md` (se citan por principio)
  - regla de propagacion, tabla SSOT y alcance por documento — viven en este registro
  - convenciones de forma (fechas, ortografia, emoticones) — viven en este registro
- `validacion`:
  - [ ] orden de lectura arranca por `CONSTITUTION.md`
  - [ ] protocolo pre/durante/post generacion presente
  - [ ] bloque `[SDD-Check]` definido
  - [ ] referencia a `SPECS_REGISTRY.md` y a `CONSTITUTION.md`
  - [ ] no reproduce la regla de propagacion ni el alcance por documento — referencia
  - [ ] precedencia declarada coincide con la de este registro y la de `CONSTITUTION.md`

### CLAUDE.md
- `path`: `CLAUDE.md`
- `proposito`: adaptador de Claude Code al protocolo; importa `AGENTS.md` via `@AGENTS.md` sin duplicar contenido.
- `ssot_level`: `operativo`
- `owner`: proyecto SDD
- `validacion`:
  - [ ] no duplica contenido — solo importa `AGENTS.md`
  - [ ] linea `@AGENTS.md` presente

### 06-BACKLOG-INVESTIGACION-FUTURA.md
- `path`: `06-BACKLOG-INVESTIGACION-FUTURA.md`
- `proposito`: backlog priorizado de **preguntas abiertas** de investigacion para ambas lineas A y B — se cierran con evidencia, no con una edicion.
- `ssot_level`: `operativo`
- `owner`: proyecto SDD
- `incluye`:
  - preguntas de investigacion con prioridad (alta / media / exploratoria)
  - anti-patrones y hallazgos metodologicos que abren preguntas nuevas
  - criterio de priorizacion
- `excluye`:
  - cambios al metodo del repositorio (protocolo, registro, constitucion, templates, tooling) — viven en `MEJORAS-METODO.md`, aprobados o propuestos
  - resultados de experimentos (viven en `experimentos/`)
- `validacion`:
  - [ ] items tienen prioridad asignada
  - [ ] criterio de priorizacion presente
  - [ ] ningun item es una tarea de metodo con decision tomada — esos migran a `MEJORAS-METODO.md`
  - [ ] los items con contraparte de metodo la referencian por ID (`M-NN`)

### MEJORAS-METODO.md
- `path`: `MEJORAS-METODO.md`
- `proposito`: backlog de cambios al **metodo** SDD del repositorio (protocolo, registro, constitucion, templates, tooling de verificacion), con prioridad, origen y estado.
- `ssot_level`: `operativo`
- `owner`: proyecto SDD
- `incluye`:
  - criterio de separacion respecto de `06-BACKLOG-INVESTIGACION-FUTURA.md` (operativa del Principio VI)
  - tabla de estado: ID `M-NN`, prioridad, estado (`Propuesta`/`Aprobada`/`Hecha`/`Descartada`), origen, destino
  - detalle por mejora: que resuelve, de donde se porta, requisitos de diseño y reservas
- `excluye`:
  - preguntas de investigacion — viven en `06-BACKLOG-INVESTIGACION-FUTURA.md`
  - el registro cronologico de lo ya aplicado — vive en `historial/sdd.md`
  - el analisis historico cerrado de 2026-03-01 — vive en `ROADMAP-MEJORAS-SDD.md` (cerrado, no se reabre)
- `validacion`:
  - [ ] cada item tiene ID, prioridad, estado y destino
  - [ ] cada item declara su origen (testigo, referencia `[Rxx]`, fase del historial)
  - [ ] los items `Hecha` referencian la fase de `historial/sdd.md` que los cerro
  - [ ] no duplica preguntas de investigacion — referencia por seccion

### ROADMAP-MEJORAS-SDD.md
- `path`: `ROADMAP-MEJORAS-SDD.md`
- `proposito`: analisis comparativo de mejoras SDD identificadas desde el proyecto "Transformacion AI-Native Org".
- `ssot_level`: `operativo`
- `estado`: `Activo` como **registro historico cerrado** (2026-06-01): documenta el analisis de 2026-03-01 y no recibe items nuevos. Las mejoras de metodo vivas van a `MEJORAS-METODO.md`.
- `owner`: proyecto SDD
- `validacion`:
  - [ ] mejoras tienen prioridad y archivo destino identificado
  - [ ] fuente de comparacion identificada
  - [ ] el aviso de cierre y de temporalidad del contenido en presente sigue visible al inicio
  - [ ] no se agregaron items posteriores a 2026-06-01

### SDD-ADAPTATIVO-VS-CASCADA.md
- `path`: `SDD-ADAPTATIVO-VS-CASCADA.md`
- `proposito`: SSOT del anti-patron "cascada encubierta" en SDD y del diseño de circuitos de aprendizaje para mantener specs vivas y adaptativas.
- `ssot_level`: `SSOT`
- `owner`: proyecto SDD
- `incluye`:
  - definicion y señales de alarma de cascada encubierta
  - mecanismos de feedback loop: tipos, cadencia, disparadores
  - comparativa SDD vs cascada: que evitar y que es indiferente hoy
  - señales de salud del circuito de aprendizaje
  - implicaciones por linea A y B
- `excluye`:
  - implementacion de herramientas CI (ver `IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md`)
  - resultados de experimentos concretos
  - comparativa de frameworks o proyectos lideres (ver `PROYECTOS-LIDERES-Y-FRAMEWORKS.md`)
- `validacion`:
  - [ ] anti-patron "cascada encubierta" definido con criterio observable
  - [ ] al menos un mecanismo de feedback loop con cadencia sugerida
  - [ ] comparativa SDD/cascada tiene columna "que evitar" y "que es indiferente"
  - [ ] implicaciones diferenciadas por linea A y B

### docs-y-investigacion/GUIA-INICIO-PROYECTO-INVESTIGACION.md
- `path`: `docs-y-investigacion/GUIA-INICIO-PROYECTO-INVESTIGACION.md`
- `proposito`: guia operativa para arrancar un proyecto de investigacion o analisis desde cero usando SDD con asistentes IA.
- `ssot_level`: `operativo`
- `owner`: proyecto SDD
- `incluye`:
  - documentos fundacionales y su contenido minimo
  - estructura de directorios recomendada
  - reglas operativas para asistentes IA
  - principios de arquitectura de conocimiento
  - secuencia de inicio dia a dia
- `excluye`:
  - comparativa de frameworks (ver `PROYECTOS-LIDERES-Y-FRAMEWORKS.md`)
  - metricas y experimentos (ver `docs-y-investigacion/PLAN-PRUEBAS.md`)
  - implementacion sin CI (ver `IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md`)
- `validacion`:
  - [ ] cubre los 5 documentos fundacionales con campos minimos
  - [ ] secuencia de inicio es accionable sin conocimiento previo del repo
  - [ ] no duplica contenido de SSOTs — referencia

### software/ANALISIS-SPEC-KIT.md
- `path`: `software/ANALISIS-SPEC-KIT.md`
- `proposito`: analisis de la metodologia de GitHub Spec Kit y su relacion con nuestra investigacion SDD en Linea B (software).
- `ssot_level`: `operativo`
- `owner`: proyecto SDD
- `incluye`:
  - sintesis del flujo de trabajo de Spec Kit (comandos y artefactos)
  - mapeo Spec Kit vs. protocolo SDD del proyecto
  - conclusiones accionables para Linea B
- `excluye`:
  - desarrollo de la transferencia a Linea A (diferido a backlog)
  - estadistica de adopcion del framework (ver `PROYECTOS-LIDERES-Y-FRAMEWORKS.md`)
  - duplicacion del catalogo de frameworks (referencia, no copia)
- `validacion`:
  - [ ] version analizada anclada en `REFERENCIAS.md` [R10]
  - [ ] mapeo no contradice `AGENTS.md` ni `SPECS_REGISTRY.md`
  - [ ] conclusiones marcadas como candidatas vs. cambios aprobados
  - [ ] no duplica SSOT — referencia

### software/COMPARATIVA-SPECKIT-VS-TESTIGO.md
- `path`: `software/COMPARATIVA-SPECKIT-VS-TESTIGO.md`
- `proposito`: comparacion entre GitHub Spec Kit (toolkit generico) y el proyecto testigo `evaluador-flujo-intent` (ex `agent-test-suite`; instancia que practica SDD) en cinco dimensiones: implementacion de SDD, artefactos, funcionalidad, beneficios y debilidades.
- `ssot_level`: `derivado`
- `deriva_de`: `software/ANALISIS-SPEC-KIT.md`
- `owner`: proyecto SDD
- `incluye`:
  - tabla comparativa por cada una de las cinco dimensiones
  - sintesis de la relacion entre ambos y su conexion con B-06/B-07
- `excluye`:
  - re-analisis del flujo interno de Spec Kit (vive en `ANALISIS-SPEC-KIT.md`, SSOT del que deriva)
  - resultados del experimento B-07 — cerrado 2026-07-28, viven en `experimentos/RESULTADO-EXPERIMENTO-B7.md`; aqui se referencia, no se copia
  - duplicacion del catalogo de frameworks (referencia `PROYECTOS-LIDERES-Y-FRAMEWORKS.md`, no copia)
- `validacion`:
  - [ ] no contradice `software/ANALISIS-SPEC-KIT.md` ni `AGENTS.md`
  - [ ] caracteriza al testigo desde sus artefactos reales, no por inferencia
  - [ ] version de Spec Kit anclada en [R10]
  - [ ] no duplica SSOT — referencia

### software/DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md
- `path`: `software/DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md`
- `proposito`: documento de decision sobre dos vias de integracion de Spec Kit en el proyecto testigo — A (adoptar Spec Kit) vs B (portar /clarify+/analyze y sumar un hook de enforcement determinista) — con esfuerzo, ventajas y desventajas para habilitar la eleccion.
- `ssot_level`: `derivado`
- `deriva_de`: `software/COMPARATIVA-SPECKIT-VS-TESTIGO.md`
- `estado`: `Activo`
- `owner`: proyecto SDD
- `incluye`:
  - definicion de las dos vias A y B
  - comparacion por criterios: funcionalidad, esfuerzo, fit, riesgo, mantenimiento, valor demo
  - dimension nueva: enforcement determinista (PreToolUse hook) ausente en ambos
  - recomendacion condicionada y consecuencias accionables
- `excluye`:
  - re-comparacion descriptiva de 5 dimensiones (vive en `COMPARATIVA-SPECKIT-VS-TESTIGO.md`)
  - re-analisis del flujo interno de Spec Kit (vive en `ANALISIS-SPEC-KIT.md`)
  - resultados de B-07 — cerrado 2026-07-28, viven en `experimentos/RESULTADO-EXPERIMENTO-B7.md`; aqui se referencia, no se copia
- `validacion`:
  - [ ] no duplica las 5 dimensiones de COMPARATIVA — referencia
  - [ ] version de Spec Kit anclada en [R10]
  - [ ] cada via tiene esfuerzo + ventajas + desventajas
  - [ ] la recomendacion es condicionada (cuando A, cuando B)
  - [ ] no contradice `AGENTS.md` ni `SPECS_REGISTRY.md`

### software/RELACION-SPEC-VS-EPICA.md
- `path`: `software/RELACION-SPEC-VS-EPICA.md`
- `proposito`: aclarar la relación y diferencias entre "spec" (en sus dos sentidos: Spec Kit y gobernanza local) y los artefactos ágiles épica e historia de usuario, con evidencia externa.
- `ssot_level`: `derivado`
- `deriva_de`: `software/ANALISIS-SPEC-KIT.md`
- `owner`: proyecto SDD
- `incluye`:
  - distinción de los dos sentidos de "spec" usados en el proyecto
  - jerarquía de artefactos Spec Kit (Spec -> Plan -> Tasks) vs. ágil (Épica -> Historia -> Tarea)
  - tabla comparativa spec / épica / historia
  - síntesis de la discusión externa autoritativa con [Rxx]
- `excluye`:
  - re-análisis del flujo interno de Spec Kit (vive en `ANALISIS-SPEC-KIT.md`, SSOT del que deriva)
  - estadística de adopción de frameworks (ver `PROYECTOS-LIDERES-Y-FRAMEWORKS.md`)
  - duplicación del mapeo Spec Kit vs. protocolo (referencia `ANALISIS-SPEC-KIT.md`, no copia)
- `validacion`:
  - [ ] cada afirmación externa tiene referencia [Rxx]
  - [ ] no contradice `software/ANALISIS-SPEC-KIT.md` ni `AGENTS.md`
  - [ ] distingue explícitamente los dos sentidos de "spec"
  - [ ] no duplica SSOT — referencia

### software/RELACION-FR-VS-SC-Y-COBERTURA.md
- `path`: `software/RELACION-FR-VS-SC-Y-COBERTURA.md`
- `proposito`: aclarar que la relación FR ↔ SC no es 1 a 1 (ejes distintos, cardinalidad N:M) y que la cobertura es muchos-a-muchos entre requisitos y verificadores, no "un test por requisito".
- `ssot_level`: `derivado`
- `deriva_de`: `software/ANALISIS-SPEC-KIT.md`
- `owner`: proyecto SDD
- `incluye`:
  - diferencia de ejes entre FR (contrato construido) y SC (valor observable)
  - cardinalidad N:M FR ↔ SC con ejemplos del testigo (SPEC-008)
  - patrones de cobertura que rompen el 1 a 1 (N FR → 1 verificador, FR sin test ejecutable, FR → N artefactos)
  - criterio de cuándo un requisito obliga a un test vs. revisión/verificación visual
- `excluye`:
  - cardinalidad entre artefactos de alcance spec/épica/historia (vive en `RELACION-SPEC-VS-EPICA.md`)
  - re-análisis del flujo interno de Spec Kit (vive en `ANALISIS-SPEC-KIT.md`, SSOT del que deriva)
- `validacion`:
  - [ ] cada afirmación externa tiene referencia [Rxx]
  - [ ] no contradice `software/ANALISIS-SPEC-KIT.md` ni `AGENTS.md`
  - [ ] distingue explícitamente eje FR vs. eje SC y la naturaleza no-1:1 de la cobertura
  - [ ] no duplica SSOT — referencia

### software/SDD-EN-LEGACY-Y-BROWNFIELD.md
- `path`: `software/SDD-EN-LEGACY-Y-BROWNFIELD.md`
- `proposito`: analisis de cuando y como aplicar SDD / specs retrospectivas a codigo legacy (brownfield) en Linea B, con evidencia externa.
- `ssot_level`: `operativo`
- `estado`: `Borrador`
- `owner`: proyecto SDD
- `incluye`:
  - casos donde la retro-spec paga vs. donde no
  - ventajas, desventajas y riesgos (fosilizar bugs, decay)
  - distincion comportamiento observado vs. deseado (characterization tests)
  - conexion con experimento Linea B
- `excluye`:
  - transferencia a Linea A (diferido a `06-BACKLOG-INVESTIGACION-FUTURA.md`)
  - re-analisis del flujo de Spec Kit (ver `software/ANALISIS-SPEC-KIT.md`)
  - duplicacion del catalogo de frameworks (referencia `PROYECTOS-LIDERES-Y-FRAMEWORKS.md`)
- `validacion`:
  - [ ] cada afirmacion externa tiene `[Rxx]`
  - [ ] distingue comportamiento observado de deseado
  - [ ] no contradice `AGENTS.md` ni `SPECS_REGISTRY.md`
  - [ ] no duplica SSOT — referencia

### experimentos/PRUEBA-REGENERABILIDAD-B7.md
- `path`: `experimentos/PRUEBA-REGENERABILIDAD-B7.md`
- `proposito`: runbook de la **metrica primaria** de B-07 — protocolo paso a paso para medir la regenerabilidad en el diseño 2x2 por traduccion. Es SSOT del **como**, no del que.
- `ssot_level`: `derivado`
- `deriva_de`: `experimentos/EXPERIMENTO-B7-formato-hibrido.md`
- `owner`: proyecto SDD
- `incluye`:
  - definicion operacional de `R1`-`R6` con sus variantes (estricta/refinada, granularidad de test/requisito)
  - protocolo por fases, roles y regimen de sellado por `sha256`
  - enmiendas fechadas post-sello, con su motivo y la direccion del sesgo cuando se conoce
  - reservas de instrumento y modos de fallo comun
- `excluye`:
  - hipotesis, metricas y criterio de exito (viven en `EXPERIMENTO-B7-formato-hibrido.md`, su SSOT — referencia, no copia)
  - los resultados y veredictos (viven en `RESULTADO-EXPERIMENTO-B7.md`)
  - el protocolo del corpus observacional (vive en `PRUEBA-OBSERVACIONAL-B7.md`, su hermano)
  - datos, logs y salidas de corrida (viven en el repo de datos `experimentosdd-b7/`, fuera de este repo)
- `validacion`:
  - [ ] cada metrica tiene definicion operacional y unidad de reporte
  - [ ] toda enmienda post-sello esta fechada, motivada, y declara la direccion del sesgo si se conoce
  - [ ] no redefine hipotesis ni criterio — referencia a su SSOT
  - [ ] toda cifra citada del artefacto es verificable en el corte declarado, no en el texto vigente
  - [ ] el techo de conclusion declarado no se excede

### experimentos/PREREG-B7.md
- `path`: `experimentos/PREREG-B7.md`
- `proposito`: pre-registro de B-07 — fija y congela los **valores** de entrada de la prueba de regenerabilidad (constantes, PROMPT, fronteras in-spec, mapeo de tests) que la Fase 0.7 sella como tag. Es SSOT de los inputs, no del que ni del como.
- `ssot_level`: `derivado`
- `deriva_de`: `experimentos/PRUEBA-REGENERABILIDAD-B7.md`
- `estado`: `Activo`
- `owner`: proyecto SDD
- `incluye`:
  - ciclo de vida y regimen de congelamiento (que puede ajustarse y hasta cuando)
  - constantes de modelo y `K`, PROMPT de regeneracion y de reparacion
  - definicion operativa de `R2`, lista de contratos `R4`, mapeo de tests
  - notas de ambiente fechadas, pre-primer `RUN`, con su clase (congelado vs atestiguado)
- `excluye`:
  - hipotesis, metricas y criterio de exito (viven en `EXPERIMENTO-B7-formato-hibrido.md`)
  - el procedimiento por fases (vive en `PRUEBA-REGENERABILIDAD-B7.md`, su SSOT)
  - resultados y veredictos (viven en `RESULTADO-EXPERIMENTO-B7.md`)
- `validacion`:
  - [ ] cada input declara su clase: congelado en `vN` o atestiguado por ambiente
  - [ ] ningun ajuste posterior al primer `RUN` de Fase 2 — los hallazgos van como reserva al resultado
  - [ ] toda nota de ambiente esta fechada y declara si toca el sello
  - [ ] no redefine hipotesis, metricas ni procedimiento — referencia a sus SSOT
  - [ ] alta de spec el 2026-07-31: documento sellado, la spec describe lo que ya existe y MUST NOT usarse para reescribirlo

### experimentos/PRUEBA-OBSERVACIONAL-B7.md
- `path`: `experimentos/PRUEBA-OBSERVACIONAL-B7.md`
- `proposito`: runbook del **corpus observacional** de B-07 — protocolo paso a paso para medir `H1` (cobertura) y `H3` (fronteras) sobre las 7 specs de los dos brazos. Es SSOT del **como**; hermano del runbook de la metrica primaria.
- `ssot_level`: `derivado`
- `deriva_de`: `experimentos/EXPERIMENTO-B7-formato-hibrido.md`
- `owner`: proyecto SDD
- `incluye`:
  - glosario de brazos, corte observacional y tiers de evidencia
  - reglas criticas de medicion con su justificacion (`N/A` distinto de `0`, el tratamiento no puede ser el instrumento, imposibilidad de cegado, confusion estructural, HARKing)
  - definicion operacional: denominador por anatomia, numerador con clases de verificador, indicador topologico de `H3`, agregacion, empate, variante de sensibilidad y quien mide
  - protocolo por fases (0 a 4), roles y regimen de sellado
  - enmiendas fechadas post-sello y «Documentos que esperan este resultado»
- `excluye`:
  - hipotesis, metricas y criterio de exito (viven en `EXPERIMENTO-B7-formato-hibrido.md`, su SSOT — referencia, no copia)
  - los resultados y veredictos (viven en `RESULTADO-EXPERIMENTO-B7.md`)
  - el protocolo de la metrica primaria (vive en `PRUEBA-REGENERABILIDAD-B7.md`)
  - `H2` como metrica puntuable (degradada a descriptiva el 2026-07-29) y `H4` (cerrada en el resultado)
  - datos, logs, inventarios y salidas de corrida (viven en el repo de datos `experimentosdd-b7/obs/`)
- `validacion`:
  - [ ] seccion «Definicion operacional» presente y completa (obligatoria desde 2026-07-28)
  - [ ] cada metrica declara denominador, numerador y unidad de reporte
  - [ ] ninguna metrica del criterio usa como instrumento una convencion que solo una anatomia contempla (`N/A` distinto de `0`)
  - [ ] toda enmienda post-sello esta fechada, motivada, declara si viaja al extractor, y declara la direccion del sesgo si se conoce
  - [ ] las decisiones de metodo declaran si se tomaron antes o despues de existir el dato afectado
  - [ ] toda cifra citada del artefacto es verificable en el corte declarado, no en el texto vigente
  - [ ] no redefine hipotesis ni criterio — referencia a su SSOT
  - [ ] el techo de conclusion declarado (descriptivo) no se excede

### historial/sdd.md
- `path`: `historial/sdd.md`
- `proposito`: registro cronologico de fases y mejoras completadas al sistema SDD del proyecto.
- `ssot_level`: `operativo`
- `owner`: proyecto SDD
- `validacion`:
  - [ ] cada fase tiene fecha y estado
  - [ ] archivos afectados listados por fase
