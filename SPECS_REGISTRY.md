# SPECS REGISTRY

Registro central de specs del proyecto `SDD`.

## Norma de interpretación
- `MUST`: obligatorio.
- `SHOULD`: recomendado fuerte; si no se cumple, debe justificarse.
- `MAY`: opcional.

## Precedencia
1. `CONSTITUTION.md` MUST prevalecer sobre todo lo demás: declara los invariantes no-negociables. Si una regla de este registro entra en conflicto con un principio, se ajusta la regla, no el principio.
2. Este archivo (`SPECS_REGISTRY.md`) MUST prevalecer para alcance y validación por documento.
3. `AGENTS.md` SHOULD regir la ejecución diaria.
4. El criterio del asistente MAY usarse solo cuando no haya conflicto con 1, 2 y 3.

División de trabajo: `CONSTITUTION.md` declara **qué nunca cede** (invariante; cambia por enmienda versionada). Este registro declara **cómo se aplica hoy** (alcance por documento, convenciones de forma, exenciónes; cambia sin enmienda).

## Reglas globales
- Todo cambio documental MUST mapearse a una spec registrada.
- Si un documento no tiene spec, se MUST crear spec mínima antes de modificar contenido.
- El nivel de detalle de cada spec SHOULD seguir la tabla de profundidad (ver sección siguiente).
- Los checks de validación MAY ejecutarse manualmente (contexto sin CI).
- Sin emoticones en documentos de contenido.
- Fechas en formato YYYY-MM-DD.
- No duplicar contenido entre SSOTs: referenciar, no repetir.
- **Alcance de un documento: un solo lugar (regla operativa del Principio I).** Los campos `proposito`, `incluye`, `excluye` y `validacion` MUST vivir únicamente en este registro. Ningún otro documento los reproduce ni los parafrasea:
  - Todo `00-INDEX.md` (raíz o de línea) responde *dónde está cada archivo* (ruta de lectura y ubicación), no *qué contiene cada doc*. Solo el `00-INDEX.md` de raíz declara además *quién es SSOT de qué tema*, en su tabla de rol (`SSOT` / `derivado` / `operativo`) — spec propia, tabla chica y estable (ver sección `00-INDEX.md` de este registro). `docs-y-investigacion/00-INDEX.md` y `software/00-INDEX.md` MUST NOT reproducir esa clasificación ni `estado` — su contenido es más grande y rota más, y ya se desincronizó una vez (M-14); ver su spec propia.
  - El encabezado de un documento MAY llevar **una** línea de identidad para quien lo abre suelto; MUST NOT enumerar `incluye`/`excluye` ni criterios de validación.
  - Motivo: el 2026-07-31 se midió la divergencia real — 11 filas de `00-INDEX.md` repetían el `proposito` del registro y 5 ya habían derivado (perdiendo, entre otras cosas, la procedencia de `historial/ROADMAP-MEJORAS-SDD.md` y el alcance «contexto del repositorio» de `AGENTS.md`).
  - Migración: los encabezados de documentos preexistentes SHOULD limpiarse de forma oportunista al tocarlos, no en una reescritura masiva.
- **Un experimento, una carpeta (desde 2026-08-22).** Todo documento de `experimentos/` MUST vivir en una subcarpeta por experimento, nombrada `<id en minúscula sin guión><guión><nombre corto>` — `a04-conducta-agente`, `b06-circuito-testigo`, `b07-formato-hibrido`. El nombre corto sale del título del documento de diseño, no se inventa. Un experimento nuevo abre su carpeta desde su primer documento. Motivo: `experimentos/` mezclaba diez archivos de tres experimentos en un solo plano y la pertenencia sólo se leía del sufijo del nombre. La carpeta **no** cambia qué necesita spec: la exención de §Docs excluidos sigue atada al prefijo del nombre de archivo (`EXPERIMENTO-*`, `RESULTADO-EXPERIMENTO-*`), así que un documento autorado no queda exento por estar dentro de una carpeta de experimento.
- Ortografía: el contenido en español MUST usar ortografía correcta con tildes y signos (acentos, "ñ", apertura de interrogación/exclamación). Aplica a documentos nuevos y a todo documento que se edite. Excepciones: identificadores técnicos, rutas, nombres de archivo y claves de los bloques normativos (ej. campos del `[SDD-Check]` y nombres de campo de spec como `validacion`, `proposito`) MUST conservarse sin tildes por estabilidad grep-able. Los documentos preexistentes sin tildes SHOULD migrarse de forma oportunista al tocarlos, no en una reescritura masiva.

## Campo ssot_level
- `SSOT`: fuente autoritativa del concepto.
- `derivado`: sintetiza un origen verificable. MUST incluir campo `deriva_de` apuntando a ese origen.
- `operativo`: guía, índice o plantilla.

Campo `deriva_de`: en specs con `ssot_level: derivado`, indica el archivo de origen. Habilita trazabilidad de propagación. El origen MUST tener spec registrada en este documento con `ssot_level: SSOT` o `ssot_level: derivado` — nunca `operativo` ni un documento sin entrada. Se permite derivado-de-derivado (cadena de más de un salto) cuando cada eslabón sintetiza una faceta distinta de su origen y lo declara explícitamente en `proposito` (p. ej. que/como/valores); no se permite para evitar clasificar un documento como su verdadero rol. Ejemplo vigente: `experimentos/b07-formato-hibrido/EXPERIMENTO-B7-formato-hibrido.md` (que) -> `experimentos/b07-formato-hibrido/PRUEBA-REGENERABILIDAD-B7.md` (como) -> `experimentos/b07-formato-hibrido/PREREG-B7.md` (valores). Motivo del cambio: relevamiento de M-13 (`agenda/MEJORAS-METODO.md`), que encontró cadenas legitimas de más de un salto ya en uso y ningún caso de más de dos.

Regla de propagación:
- Si cambia un SSOT, sus derivados MUST revisarse y el resultado SHOULD registrarse en la entrega.
- Si un resultado responde una pregunta abierta de un SSOT, MUST propagarse **primero al SSOT y después a sus derivados**. La regla anterior sólo cubre la dirección descendente; el conocimiento producido por una ejecución entra por abajo.
- **Cerrar un experimento MUST disparar esta misma revisión**, aunque `experimentos/` esté exento de spec propia: la exención es de *spec*, no de *propagación*. Sin esta regla el cierre no modifica ningún SSOT y por lo tanto no dispara nada — que es lo que ocurrió con B-07 (2026-07-28), cuyo resultado dejó cuatro documentos afirmando lo contrario durante un día. Procedimiento mecánico en `templates/RESULTADO-EXPERIMENTO.md`, sección «Propagacion».

## Campo `estado`
- `Activo` (default — no requiere marcarlo): spec vigente y en uso.
- `Borrador`: spec propuesta, pendiente de aprobación.
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
- Contenido en `experimentos/` **generado desde templates** (los templates si tienen spec): diseños de experimento (`EXPERIMENTO-*.md`) y resultados (`RESULTADO-EXPERIMENTO-*.md`). La exención es de **spec propia**, no de **propagación**: cerrar un experimento MUST disparar la revisión de la sección «Regla de propagación».
  - **Los runbooks de método NO están exentos (aclarado 2026-07-30).** Un runbook (`PRUEBA-*.md`) vive en `experimentos/` pero **no deriva de ningún template**: es un documento autorado de protocolo de medición, con definición operacional, roles y fases. Al no ser generado desde template, la exención de arriba no lo alcanza y MUST tener spec registrada. Hueco detectado el 2026-07-30: los dos runbooks de B-07 estaban sin spec y se venian modificando, contra la regla global «todo cambio documental MUST mapearse a una spec registrada». Criterio para clasificar un `.md` de `experimentos/`: ¿su estructura la fija un template del proyecto? Exento. ¿La fija su autor? Necesita spec.
  - **Excepcion dentro de la excepción (aclarado 2026-08-03, M-13; extendida a `RESULTADO-EXPERIMENTO-*.md` el 2026-08-22): un documento exento citado como `deriva_de` por otro documento MUST tener entrada minima** (`path`, `proposito`, `ssot_level: SSOT`, `owner`, `validacion`) en este registro, aunque conserve la exención de `incluye`/`excluye` detallados. Motivo: `deriva_de` MUST apuntar a un origen con `ssot_level` verificable (ver §Campo ssot_level); un documento sin entrada no lo tiene, aunque el resto del repositorio lo trate en prosa como SSOT. La exención de spec **detallada** para plantillas de experimento se mantiene; lo que deja de existir es la exención de **entrada** cuando ese documento funciona como origen de otro.
- Codigo de verificacion en `tools/`: no es pieza documental autorada (Principio IV habla de documentos). Su contrato de uso se declara en `AGENTS.md` §Al cerrar una iteracion; lo que verifica y lo que MUST NOT pretender verificar vive en su docstring.
- Repositorios externos clonados (vendored) en `fuentes-externas/` — material fuente de referencia, no autorado por el proyecto. La versión analizada se ancla en `REFERENCIAS.md`; el análisis propio si tiene spec (ver `software/ANALISIS-SPEC-KIT.md`).

## Tabla SSOT

| Linea | Concepto | SSOT | Quien referencia |
|------|----------|------|------------------|
| Comun | Principios no-negociables de la investigación | `CONSTITUTION.md` | `AGENTS.md`, `SPECS_REGISTRY.md`, `00-INDEX.md`, `README.md` |
| Comun | Mejoras al método SDD del repositorio | `agenda/MEJORAS-METODO.md` | `agenda/BACKLOG-INVESTIGACION.md`, `historial/sdd.md` |
| Comun | Modelo dual SDD | `comun/MARCO-COMPARATIVO-DOS-LINEAS.md` | `README.md`, `00-INDEX.md`, planes de línea |
| Comun | SDD adaptativo y circuitos de aprendizaje | `comun/SDD-ADAPTATIVO-VS-CASCADA.md` | `docs-y-investigacion/LINEAS-INVESTIGACION.md`, `software/LINEAS-INVESTIGACION.md` |
| Comun | Referencias [Rxx] | `REFERENCIAS.md` | todos los docs con citas `[Rxx]` |
| Comun | Frameworks/proyectos lideres | `comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md` | `LINEAS-INVESTIGACION.md` de ambas líneas |
| Comun | Tendencias y estadística | `comun/ESTADISTICAS-TENDENCIAS-EVOLUCION.md` | `BACKLOG-INVESTIGACION`, `comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md` |
| Comun | Escenarios que justifican SDD | `comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md` | `00-INDEX.md`, `comun/MARCO-COMPARATIVO-DOS-LINEAS.md` |
| Comun | Implementacion pragmatica sin CI | `comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md` | `PLAN-PRUEBAS.md` de ambas líneas |
| Docs/Investigacion | Agenda línea A | `docs-y-investigacion/LINEAS-INVESTIGACION.md` | `PLAN-PRUEBAS.md`, `NECESIDADES-Y-METRICAS.md` línea A |
| Docs/Investigacion | Necesidades, métricas y riesgos línea A | `docs-y-investigacion/NECESIDADES-Y-METRICAS.md` | `PLAN-PRUEBAS.md` línea A, `comun/MARCO-COMPARATIVO-DOS-LINEAS.md` |
| Docs/Investigacion | Plan experimental línea A | `docs-y-investigacion/PLAN-PRUEBAS.md` | `00-INDEX.md` global y de línea; `experimentos/` de línea A al cerrar |
| Docs/Investigacion | Hipotesis, métricas y criterio de éxito de A-04 (el «que») | `experimentos/a04-conducta-agente/EXPERIMENTO-A4-protocolo-conducta.md` | `experimentos/a04-conducta-agente/PRUEBA-PISO-RUIDO-A4.md`, `docs-y-investigacion/PLAN-PRUEBAS.md` |
| Docs/Investigacion | Protocolo de medición del piso de ruido de A-04, pasadas 1 y 1b (el «como») | `experimentos/a04-conducta-agente/PRUEBA-PISO-RUIDO-A4.md` | `experimentos/a04-conducta-agente/RESULTADO-EXPERIMENTO-A4.md`; sello, sondas y bitacora del repo de datos `experimentosdd-a4/` |
| Software | Invariantes del método SDD entre implementaciones independientes | `software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md` | `software/ANALISIS-SPEC-KIT.md`, `software/COMPARATIVA-SPECKIT-VS-TESTIGO.md` |
| Software | Analisis de la metodologia GitHub Spec Kit | `software/ANALISIS-SPEC-KIT.md` | `software/COMPARATIVA-SPECKIT-VS-TESTIGO.md`, `software/RELACION-FR-VS-SC-Y-COBERTURA.md` |
| Software | Agenda línea B | `software/LINEAS-INVESTIGACION.md` | `PLAN-PRUEBAS.md`, `NECESIDADES-Y-METRICAS.md` línea B |
| Software | Necesidades, métricas y riesgos línea B | `software/NECESIDADES-Y-METRICAS.md` | `PLAN-PRUEBAS.md` línea B, `comun/MARCO-COMPARATIVO-DOS-LINEAS.md` |
| Software | Plan experimental línea B | `software/PLAN-PRUEBAS.md` | `00-INDEX.md` global y de línea; `software/LINEAS-INVESTIGACION.md`; `experimentos/` (diseños y resultados B-06/B-07) |
| Software | Hipotesis, métricas y criterio de éxito de B-07 (el «que») | `experimentos/b07-formato-hibrido/EXPERIMENTO-B7-formato-hibrido.md` | `experimentos/b07-formato-hibrido/PRUEBA-REGENERABILIDAD-B7.md`, `experimentos/b07-formato-hibrido/PRUEBA-OBSERVACIONAL-B7.md` |
| Software | Protocolo de medición de B-07 (el «como») | `experimentos/b07-formato-hibrido/PRUEBA-REGENERABILIDAD-B7.md` (métrica primaria) y `experimentos/b07-formato-hibrido/PRUEBA-OBSERVACIONAL-B7.md` (corpus observacional) | `experimentos/b07-formato-hibrido/RESULTADO-EXPERIMENTO-B7.md`; enmiendas y bitacora del repo de datos `experimentosdd-b7/` |

## Specs registradas (MVP)

### CONSTITUTION.md
- `path`: `CONSTITUTION.md`
- `proposito`: SSOT de los invariantes no-negociables de la investigacion — lo que ninguna spec, protocolo ni decision de redaccion puede contradecir.
- `ssot_level`: `SSOT`
- `owner`: proyecto SDD
- `incluye`:
  - preambulo: que es, como se usa, alcance y que NO es
  - principios, cada uno con invariante autocontenido + `Enforcement` + `Verificador` + `Detalle` (SSOT donde vive el detalle operativo)
  - governance: precedencia de fuentes, versionado semver, fase pre-1.0, procedimiento de enmienda, limite honesto del enforcement
- `excluye`:
  - convenciones de forma (fechas, ortografia, nomenclatura) — viven en este registro
  - el protocolo paso a paso del asistente — vive en `AGENTS.md`
  - el detalle operativo de cada principio — vive en el SSOT que el principio referencia en `Detalle:`
- `validacion`:
  - [ ] cada principio declara un invariante autocontenido, sin duplicar el detalle que referencia
  - [ ] cada principio tiene `Enforcement` y `Detalle` con SSOT existente
  - [ ] cada principio declara `Verificador` con checks que `tools/check_docs.py` emite, o `ninguno` (verificado por el check `constitucion`)
  - [ ] versión, fecha de ratificacion y de ultima enmienda presentes y coherentes con `historial/sdd.md`
  - [ ] la precedencia declarada coincide con la de este registro y la de `AGENTS.md`
  - [ ] ningún documento activo contradice un principio vigente

### README.md
- `path`: `README.md`
- `proposito`: entrada y navegacion del proyecto.
- `ssot_level`: `operativo`
- `tono`: humano y descriptivo — es el primer contacto con el proyecto, no un documento tecnico.
- `incluye`:
  - propósito del repo y por que corre en dos líneas
  - un puñado de enlaces de entrada: índice, constitucion, las dos líneas, protocolo y registro
- `excluye`:
  - detalle metodologico profundo
  - el listado de documentos y directorios del repo — vive en `00-INDEX.md`; el README remite, no lo reproduce
- `validacion`:
  - [ ] links internos vigentes
  - [ ] no contradice SSOTs
  - [ ] tono narrativo, sin lenguaje normativo (MUST/SHOULD/MAY)
  - [ ] no enumera el contenido del repo — remite a `00-INDEX.md`

### 00-INDEX.md
- `path`: `00-INDEX.md`
- `proposito`: indice de navegacion global — responde donde esta cada archivo y en que orden leerlo.
- `ssot_level`: `operativo`
- `incluye`:
  - ruta de lectura recomendada: una sola tabla con orden, link y **rol** (`SSOT` / `derivado` / `operativo`)
  - links a `CONSTITUTION.md`, `SPECS_REGISTRY.md` y `AGENTS.md`
  - tabla complementaria con el resto de la estructura: directorios y operativos que no están en la ruta
- `excluye`:
  - alcance de cada documento (`proposito`/`incluye`/`excluye`/`validacion`) — vive en este registro
  - mapa tema → SSOT — vive en la tabla SSOT de este registro
  - definiciones conceptuales extensas
- `validacion`:
  - [ ] enlaces vigentes
  - [ ] links a `CONSTITUTION.md`, `AGENTS.md` y `SPECS_REGISTRY.md` presentes
  - [ ] ambas tablas declaran rol, no propósito
  - [ ] ningún documento aparece en las dos tablas — la ruta y el resto de la estructura son disjuntas
  - [ ] sin duplicacion de SSOT

### comun/MARCO-COMPARATIVO-DOS-LINEAS.md
- `path`: `comun/MARCO-COMPARATIVO-DOS-LINEAS.md`
- `proposito`: SSOT de diferencias entre linea A y linea B.
- `ssot_level`: `SSOT`
- `incluye`:
  - tesis del modelo dual
  - eje diferencial A vs B: objetivo principal, artefactos SDD más utiles, familia de métricas
  - punteros al SSOT donde vive el detalle de cada línea
- `excluye`:
  - necesidades operativas, métricas concretas, umbrales y riesgos por línea — viven en `docs-y-investigacion/NECESIDADES-Y-METRICAS.md` y `software/NECESIDADES-Y-METRICAS.md`
  - modos de fallo y escenarios por línea — viven en `comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md`
  - frameworks y herramientas concretas por línea — viven en `comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md`
  - resultados de experimentos concretos
- `validacion`:
  - [ ] separacion explicita A/B
  - [ ] nombra la familia de métricas de cada línea, no las métricas — esas se referencian
  - [ ] cada eje de la tabla contrasta las dos líneas; ninguno describe una sola

### comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md
- `path`: `comun/ESCENARIOS-QUE-JUSTIFICAN-SDD.md`
- `proposito`: SSOT del catálogo de problemas y escenarios (modos de fallo) que justifican adoptar SDD hoy.
- `ssot_level`: `SSOT`
- `owner`: proyecto SDD
- `incluye`:
  - causas raíz transversales
  - escenarios por línea A, línea B y transversales
  - mapa escenario → eje SDD que lo mitiga
- `excluye`:
  - cifras cuantitativas (viven en `comun/ESTADISTICAS-TENDENCIAS-EVOLUCION.md` — referencia)
  - dinámica de cascada/feedback loops (vive en `comun/SDD-ADAPTATIVO-VS-CASCADA.md` — referencia)
- `validacion`:
  - [ ] cada afirmación externa tiene `[Rxx]`
  - [ ] no duplica cifras de `ESTADISTICAS` ni el tratamiento de cascada de `SDD-ADAPTATIVO` — referencia
  - [ ] escenarios separados por línea A / B / transversal
  - [ ] no contradice SSOTs activos

### comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md
- `path`: `comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md`
- `proposito`: SSOT de frameworks y proyectos de referencia.
- `ssot_level`: `SSOT`
- `incluye`:
  - referencias de docs/investigación y software
  - marcos transversales
- `excluye`:
  - estadística de adopcion
- `validacion`:
  - [ ] cada bloque enlaza [Rxx]

### comun/ESTADISTICAS-TENDENCIAS-EVOLUCION.md
- `path`: `comun/ESTADISTICAS-TENDENCIAS-EVOLUCION.md`
- `proposito`: SSOT de datos cuantitativos y tendencias.
- `ssot_level`: `SSOT`
- `incluye`:
  - cifras y su referencia [Rxx]
  - implicaciones por línea
- `excluye`:
  - decisiónes operativas finas
- `validacion`:
  - [ ] cifras con fuente [Rxx]
  - [ ] fecha de consulta indicada

### comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md
- `path`: `comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md`
- `proposito`: SSOT de adopcion pragmatica en contexto sin CI.
- `ssot_level`: `SSOT`
- `incluye`:
  - decisiónes de enfoque
  - roadmap 0-90 dias
  - criterio para escalar tooling
- `excluye`:
  - detalle de resultados experimentales
  - los campos del bloque `[SDD-Check]` — son SSOT de `AGENTS.md`; aca se referencia
- `validacion`:
  - [ ] contexto sin CI explicito
  - [ ] criterios de evolucion definidos
  - [ ] no enumera los campos del `[SDD-Check]` — referencia a `AGENTS.md`

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

### docs-y-investigación/LINEAS-INVESTIGACION.md
- `path`: `docs-y-investigacion/LINEAS-INVESTIGACION.md`
- `proposito`: SSOT de agenda de investigacion linea A.
- `ssot_level`: `SSOT`
- `validacion`:
  - [ ] hipótesis explicitas
  - [ ] preguntas accionables

### docs-y-investigación/NECESIDADES-Y-METRICAS.md
- `path`: `docs-y-investigacion/NECESIDADES-Y-METRICAS.md`
- `proposito`: SSOT de necesidades operativas, metricas, umbrales y riesgos de la linea A.
- `ssot_level`: `SSOT`
- `incluye`:
  - necesidades operativas de la línea
  - métricas nucleo con definición
  - umbrales iniciales sugeridos
  - riesgos de la línea y su mitigacion
- `excluye`:
  - el contraste con la línea B — vive en `comun/MARCO-COMPARATIVO-DOS-LINEAS.md`
- `validacion`:
  - [ ] métrica con definición
  - [ ] umbral inicial definido
  - [ ] no describe la línea B — el contraste se referencia

### docs-y-investigación/PLAN-PRUEBAS.md
- `path`: `docs-y-investigacion/PLAN-PRUEBAS.md`
- `proposito`: SSOT experimental linea A.
- `ssot_level`: `SSOT`
- `validacion`:
  - [ ] experimento con criterio de éxito
  - [ ] enlace a templates

### software/LINEAS-INVESTIGACION.md
- `path`: `software/LINEAS-INVESTIGACION.md`
- `proposito`: SSOT de agenda de investigacion linea B.
- `ssot_level`: `SSOT`
- `validacion`:
  - [ ] hipótesis explicitas
  - [ ] cubre contrato, pruebas, IA

### software/NECESIDADES-Y-METRICAS.md
- `path`: `software/NECESIDADES-Y-METRICAS.md`
- `proposito`: SSOT de necesidades operativas, metricas, umbrales y riesgos de la linea B.
- `ssot_level`: `SSOT`
- `incluye`:
  - necesidades operativas de la línea
  - métricas tecnicas con definición y su relación con DORA
  - riesgos de la línea y su mitigacion
- `excluye`:
  - el contraste con la línea A — vive en `comun/MARCO-COMPARATIVO-DOS-LINEAS.md`
- `validacion`:
  - [ ] métricas DORA y requisitos
  - [ ] riesgos y mitigaciones
  - [ ] no describe la línea A — el contraste se referencia

### software/PLAN-PRUEBAS.md
- `path`: `software/PLAN-PRUEBAS.md`
- `proposito`: SSOT experimental linea B.
- `ssot_level`: `SSOT`
- `validacion`:
  - [ ] métrica primaria por experimento
  - [ ] criterio de adopcion definido

### docs-y-investigación/00-INDEX.md y software/00-INDEX.md
- `path`: `docs-y-investigacion/00-INDEX.md`
- `path`: `software/00-INDEX.md`
- `proposito`: indice de navegacion de su linea — pregunta central, gobernanza aplicable y lectura sugerida.
- `ssot_level`: `operativo`
- `excluye`:
  - el `proposito` de cada documento listado — vive en este registro; junto a cada link va a lo sumo un puntero breve de que tipo de contenido es, no una síntesis de que dice
  - el campo `estado` de cada documento listado — vive en este registro; anotarlo aca crea una segunda fuente que puede desincronizarse (motivo: `software/00-INDEX.md` quedo con "Estado: Borrador" para `DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md` cuando el registro ya declaraba `Activo`, detectado 2026-08-03, M-14)
  - el campo `ssot_level`/rol (`SSOT`/`derivado`/`operativo`) de cada documento listado — vive en la tabla SSOT y en el campo `ssot_level` de este registro; mismo riesgo de desincronizacion que `estado` (ver `Detalle` del Principio I en `CONSTITUTION.md`)
- `validacion`:
  - [ ] links vigentes
  - [ ] direccionan a SSOT de su línea
  - [ ] las descripciones junto a cada link no parafrasean el `proposito` registrado del documento enlazado
  - [ ] ningún link anota `estado`
  - [ ] ningún link ni tabla anota `ssot_level`/rol

### templates/EXPERIMENTO.md y templates/RESULTADO-EXPERIMENTO.md
- `path`: `templates/EXPERIMENTO.md`
- `path`: `templates/RESULTADO-EXPERIMENTO.md`
- `proposito`: plantillas para disenar y cerrar experimentos — fijan los campos minimos y el procedimiento de propagacion; los documentos generados desde ellas quedan exentos de spec propia.
- `ssot_level`: `operativo`
- `validacion`:
  - [ ] campos minimos para ejecutar y cerrar experimentos
  - [ ] `EXPERIMENTO.md` incluye la sección «Definicion operacional» (obligatoria desde 2026-07-28, ver `experimentos/b07-formato-hibrido/RESULTADO-EXPERIMENTO-B7.md` Hallazgo 7)
  - [ ] el criterio de éxito se enuncia solo contra métricas que la propia prueba produce, con comprobacion de satisfacibilidad
  - [ ] `RESULTADO-EXPERIMENTO.md` incluye la sección «Propagacion» con el grep de deuda declarada y la tabla de triaje (obligatoria desde 2026-07-29)
  - [ ] `EXPERIMENTO.md` incluye «Documentos que esperan este resultado»; su contraparte en el cierre es «Propagacion»
  - [ ] la deuda no resuelta migra a `agenda/BACKLOG-INVESTIGACION.md` antes de cerrar, no queda atada al siguiente cierre

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
  - orden de lectura previo a cualquier cambio (constitucion -> índice -> spec del doc)
  - protocolo durante el cambio y disambiguacion
  - checks de post-generacion y bloque `[SDD-Check]`
  - cierre de iteracion (registro, historial, commit)
  - criterios de calidad, ciclo de vida de specs, «Que NO hacer», excepciónes, convenciones
- `excluye`:
  - invariantes y su justificación — viven en `CONSTITUTION.md` (se citan por principio)
  - regla de propagación, tabla SSOT y alcance por documento — viven en este registro
  - convenciones de forma (fechas, ortografia, emoticones) — viven en este registro
- `validacion`:
  - [ ] orden de lectura arranca por `CONSTITUTION.md`
  - [ ] protocolo pre/durante/post generacion presente
  - [ ] bloque `[SDD-Check]` definido
  - [ ] referencia a `SPECS_REGISTRY.md` y a `CONSTITUTION.md`
  - [ ] no reproduce la regla de propagación ni el alcance por documento — referencia
  - [ ] precedencia declarada coincide con la de este registro y la de `CONSTITUTION.md`

### CLAUDE.md
- `path`: `CLAUDE.md`
- `proposito`: adaptador de Claude Code al protocolo; importa `AGENTS.md` via `@AGENTS.md` sin duplicar contenido.
- `ssot_level`: `operativo`
- `owner`: proyecto SDD
- `validacion`:
  - [ ] no duplica contenido — solo importa `AGENTS.md`
  - [ ] línea `@AGENTS.md` presente

### agenda/BACKLOG-INVESTIGACION.md
- `path`: `agenda/BACKLOG-INVESTIGACION.md`
- `proposito`: backlog priorizado de **preguntas abiertas** de investigacion para ambas lineas A y B — se cierran con evidencia, no con una edicion.
- `ssot_level`: `operativo`
- `owner`: proyecto SDD
- `incluye`:
  - preguntas de investigación con prioridad (alta / media / exploratoria)
  - anti-patrones y hallazgos metodologicos que abren preguntas nuevas
  - criterio de priorizacion
- `excluye`:
  - cambios al método del repositorio (protocolo, registro, constitucion, templates, tooling) — viven en `agenda/MEJORAS-METODO.md`, aprobados o propuestos
  - resultados de experimentos (viven en `experimentos/`)
- `validacion`:
  - [ ] items tienen prioridad asignada
  - [ ] criterio de priorizacion presente
  - [ ] ningún item es una tarea de método con decisión tomada — esos migran a `agenda/MEJORAS-METODO.md`
  - [ ] los items con contraparte de método la referencian por ID (`M-NN`)

### agenda/MEJORAS-METODO.md
- `path`: `agenda/MEJORAS-METODO.md`
- `proposito`: backlog de cambios al **metodo** SDD del repositorio (protocolo, registro, constitucion, templates, tooling de verificacion), con prioridad, origen y estado.
- `ssot_level`: `operativo`
- `owner`: proyecto SDD
- `incluye`:
  - criterio de separacion respecto de `agenda/BACKLOG-INVESTIGACION.md` (operativa del Principio VI)
  - tabla de estado: ID `M-NN`, prioridad, estado (`Propuesta`/`Aprobada`/`Hecha`/`Descartada`), origen, destino
  - detalle por mejora: que resuelve, de donde se porta, requisitos de diseño y reservas
- `excluye`:
  - preguntas de investigación — viven en `agenda/BACKLOG-INVESTIGACION.md`
  - el registro cronológico de lo ya aplicado — vive en `historial/sdd.md`
  - el análisis historico cerrado de 2026-03-01 — vive en `historial/ROADMAP-MEJORAS-SDD.md` (cerrado, no se reabre)
- `validacion`:
  - [ ] cada item tiene ID, prioridad, estado y destino
  - [ ] cada item declara su origen (testigo, referencia `[Rxx]`, fase del historial)
  - [ ] los items `Hecha` referencian la fase de `historial/sdd.md` que los cerro
  - [ ] no duplica preguntas de investigación — referencia por sección

### historial/ROADMAP-MEJORAS-SDD.md
- `path`: `historial/ROADMAP-MEJORAS-SDD.md`
- `proposito`: analisis comparativo de mejoras SDD identificadas desde el proyecto "Transformacion AI-Native Org".
- `ssot_level`: `operativo`
- `estado`: `Activo` como **registro historico cerrado** (2026-06-01): documenta el analisis de 2026-03-01 y no recibe items nuevos. Las mejoras de metodo vivas van a `agenda/MEJORAS-METODO.md`.
- `owner`: proyecto SDD
- `validacion`:
  - [ ] mejoras tienen prioridad y archivo destino identificado
  - [ ] fuente de comparación identificada
  - [ ] el aviso de cierre y de temporalidad del contenido en presente sigue visible al inicio
  - [ ] no se agregaron items posteriores a 2026-06-01

### comun/SDD-ADAPTATIVO-VS-CASCADA.md
- `path`: `comun/SDD-ADAPTATIVO-VS-CASCADA.md`
- `proposito`: SSOT del anti-patron "cascada encubierta" en SDD y del diseño de circuitos de aprendizaje para mantener specs vivas y adaptativas.
- `ssot_level`: `SSOT`
- `owner`: proyecto SDD
- `incluye`:
  - definición y señales de alarma de cascada encubierta
  - mecanismos de feedback loop: tipos, cadencia, disparadores
  - comparativa SDD vs cascada: que evitar y que es indiferente hoy
  - señales de salud del circuito de aprendizaje
  - implicaciones por línea A y B
- `excluye`:
  - implementacion de herramientas CI (ver `comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md`)
  - resultados de experimentos concretos
  - comparativa de frameworks o proyectos lideres (ver `comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md`)
- `validacion`:
  - [ ] anti-patron "cascada encubierta" definido con criterio observable
  - [ ] al menos un mecanismo de feedback loop con cadencia sugerida
  - [ ] comparativa SDD/cascada tiene columna "que evitar" y "que es indiferente"
  - [ ] implicaciones diferenciadas por línea A y B

### docs-y-investigación/GUIA-INICIO-PROYECTO-INVESTIGACION.md
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
  - comparativa de frameworks (ver `comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md`)
  - métricas y experimentos (ver `docs-y-investigacion/PLAN-PRUEBAS.md`)
  - implementacion sin CI (ver `comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md`)
- `validacion`:
  - [ ] cubre los 5 documentos fundacionales con campos minimos
  - [ ] secuencia de inicio es accionable sin conocimiento previo del repo
  - [ ] no duplica contenido de SSOTs — referencia

### software/ANALISIS-SPEC-KIT.md
- `path`: `software/ANALISIS-SPEC-KIT.md`
- `proposito`: SSOT del analisis de la metodologia de GitHub Spec Kit y su relacion con nuestra investigacion SDD en Linea B (software).
- `ssot_level`: `SSOT`
- `owner`: proyecto SDD
- `incluye`:
  - síntesis del flujo de trabajo de Spec Kit (comandos y artefactos)
  - mapeo Spec Kit vs. protocolo SDD del proyecto
  - conclusiónes accionables para Linea B
- `excluye`:
  - desarrollo de la transferencia a Linea A (diferido a backlog)
  - el veredicto de convergencia entre implementaciones — vive en `software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, su SSOT desde 2026-08-02; aca se referencia
  - estadística de adopcion del framework (ver `comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md`)
  - duplicacion del catalogo de frameworks (referencia, no copia)
- `validacion`:
  - [ ] versión analizada anclada en `REFERENCIAS.md` [R10]
  - [ ] mapeo no contradice `AGENTS.md` ni `SPECS_REGISTRY.md`
  - [ ] conclusiónes marcadas como candidatas vs. cambios aprobados
  - [ ] no duplica SSOT — referencia

### software/ANALISIS-SUPERPOWERS.md
- `path`: `software/ANALISIS-SUPERPOWERS.md`
- `proposito`: analisis de la metodologia de Superpowers [R37] y su relacion con nuestra investigacion SDD en Linea B, con foco en los dos aportes que Spec Kit no tiene: la evaluacion conductual de documentacion y la posicion spec-anchored.
- `ssot_level`: `operativo`
- `owner`: proyecto SDD
- `incluye`:
  - síntesis del flujo de trabajo (skills, artefactos, gates)
  - mapeo Superpowers vs. protocolo SDD del proyecto, sobre el instrumento de ocho filas fijado el 2026-05-24
  - el método de evaluación conductual de documentacion y su portabilidad a este repo
  - conclusiónes accionables para Linea B, marcadas como candidatas o aprobadas
- `excluye`:
  - la lectura cruzada de las tres implementaciones — vive en `software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, su SSOT
  - el diseño del experimento derivado — vive en `experimentos/` cuando exista
  - estadística de adopcion del framework (ver `comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md`)
  - re-análisis del flujo de Spec Kit (vive en `software/ANALISIS-SPEC-KIT.md`)
  - duplicacion del catalogo de frameworks (referencia, no copia)
- `validacion`:
  - [ ] versión analizada anclada en `REFERENCIAS.md` [R37]
  - [ ] toda cifra de la fuente es verificable en el clon vendored, con su archivo de origen declarado
  - [ ] los evals de la fuente se presentan como precedente de método, nunca como evidencia de efectividad
  - [ ] mapeo no contradice `AGENTS.md` ni este registro
  - [ ] conclusiónes marcadas como candidatas vs. cambios aprobados
  - [ ] no duplica SSOT — referencia

### software/ANALISIS-OPENSPEC.md
- `path`: `software/ANALISIS-OPENSPEC.md`
- `proposito`: analisis de la metodologia de OpenSpec [R38] y su relacion con nuestra investigacion SDD en Linea B, con foco en su rasgo sin equivalente en las otras fuentes: la instruccion de metodo servida por herramienta bajo demanda en vez de leida de un documento.
- `ssot_level`: `operativo`
- `owner`: proyecto SDD
- `incluye`:
  - el resultado del filtro de procedencia exigido por `software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, con la evidencia de fechas que lo sostiene y sus limites
  - síntesis del flujo de trabajo (comandos, artefactos, separacion spec vigente / delta)
  - mapeo OpenSpec vs. protocolo SDD del proyecto, sobre el instrumento v1 de ocho filas fijado el 2026-05-24
  - conclusiónes accionables para Linea B, marcadas como lectura, candidatas o aprobadas
- `excluye`:
  - la lectura cruzada de los cuatro casos — vive en `software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, su SSOT
  - estadística de adopcion del framework (ver `comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md`)
  - re-análisis del flujo de Spec Kit (vive en `software/ANALISIS-SPEC-KIT.md`) ni de Superpowers (vive en `software/ANALISIS-SUPERPOWERS.md`)
  - duplicacion del catalogo de frameworks (referencia, no copia)
- `validacion`:
  - [ ] versión analizada anclada en `REFERENCIAS.md` [R38]
  - [ ] la procedencia esta declarada antes de la lectura, con evidencia verificable y con sus limites explicitos
  - [ ] todo rasgo citado declara su archivo de origen en el clon vendored o el comando que lo expone
  - [ ] la fuente no se cita como evidencia de efectividad: no reporta ninguna medición, y eso queda dicho
  - [ ] sus comparaciónes contra otros frameworks se tratan como posicionamiento comercial, no como insumo del mapeo
  - [ ] el mapeo corre sobre el instrumento v1 sin agregar ni redefinir filas
  - [ ] mapeo no contradice `AGENTS.md` ni este registro
  - [ ] conclusiónes marcadas como lectura, candidatas o cambios aprobados
  - [ ] no duplica SSOT — referencia

### software/ANALISIS-SDD-FIRST.md
- `path`: `software/ANALISIS-SDD-FIRST.md`
- `proposito`: analisis de sdd-first [R39] como caso **del propio linaje** — el metodo de este repositorio llevado a codigo ejecutable en un kit instalable — con foco en que mecanismos de ese kit son portables a un repositorio documental y cuales no.
- `ssot_level`: `operativo`
- `owner`: proyecto SDD
- `incluye`:
  - el resultado del filtro de procedencia exigido por `software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, con la evidencia que lo sostiene y su consecuencia: no suma linaje
  - sintesis del andamiaje (capas de enforcement, artefactos generados desde config, skills multi-asistente, actualizacion de derivados)
  - mapeo sdd-first vs. protocolo SDD del proyecto, sobre el instrumento v1 de ocho filas fijado el 2026-05-24
  - conclusiónes accionables para Linea B y para el metodo del repositorio, marcadas como lectura, candidatas o aprobadas
- `excluye`:
  - la lectura cruzada de los casos de convergencia — vive en `software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, su SSOT
  - las decisiónes de adopcion — viven en `agenda/MEJORAS-METODO.md`
  - re-análisis del flujo de Spec Kit, Superpowers u OpenSpec (viven en sus analisis respectivos)
  - estadística de adopcion de frameworks (ver `comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md`)
- `validacion`:
  - [ ] versión analizada anclada en `REFERENCIAS.md` [R39], con commit y estado del arbol
  - [ ] la procedencia esta declarada antes de la lectura y concluye explicitamente que la fuente NO suma linaje
  - [ ] ninguna coincidencia con el metodo de este repositorio se presenta como convergencia
  - [ ] la fuente no se cita como evidencia de efectividad: no reporta ninguna medición, y eso queda dicho
  - [ ] todo rasgo citado declara su archivo de origen en el clon vendored o el comando que lo expone
  - [ ] el mapeo corre sobre el instrumento v1 sin agregar ni redefinir filas
  - [ ] mapeo no contradice `AGENTS.md` ni este registro
  - [ ] conclusiónes marcadas como lectura, candidatas o cambios aprobados
  - [ ] no duplica SSOT — referencia

### software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md
- `path`: `software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md`
- `proposito`: SSOT de que elementos del metodo SDD son invariantes entre implementaciones independientes y cuales no, leido sobre cuatro casos (Spec Kit, Superpowers, OpenSpec y el proyecto testigo) con un instrumento comun.
- `ssot_level`: `SSOT`
- `owner`: proyecto SDD
- `incluye`:
  - el instrumento de lectura y su procedencia (las ocho filas fijadas el 2026-05-24, anteriores a la incorporación de la tercera y la cuarta implementacion)
  - el conteo por linajes y la procedencia declarada de cada caso, incluidos los limites de cada declaracion
  - veredicto por fila (converge / parcial / diverge) sobre los cuatro casos, con las divergencias reportadas con el mismo peso que las convergencias
  - las dimensiones observadas que el instrumento v1 no cubre, registradas sin veredicto
  - la caracterización del testigo sobre ese instrumento, derivada de sus artefactos reales
  - que se puede y que no se puede inferir de la convergencia observada
  - el procedimiento de incorporación de un caso nuevo: filtro de linaje, tratamiento de las dimensiones que el instrumento no cubre, y regla de versionado del instrumento
- `excluye`:
  - la caracterización individual de cada implementacion (vive en `software/ANALISIS-SPEC-KIT.md`, `software/ANALISIS-SUPERPOWERS.md` y `software/ANALISIS-OPENSPEC.md`; se referencia, no se copia)
  - la comparación pareada Spec Kit vs. testigo en cinco dimensiones (vive en `software/COMPARATIVA-SPECKIT-VS-TESTIGO.md`)
  - decisiónes de adopcion (viven en `agenda/MEJORAS-METODO.md`)
  - estadística de adopcion de frameworks (ver `comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md`)
- `validacion`:
  - [ ] el instrumento declara su versión y su fecha, y es anterior a los casos que lee
  - [ ] ninguna fila se agrega ni se redefine después de leer los casos: ampliar el instrumento MUST abrir versión nueva y re-correr todos los casos
  - [ ] todo caso incorporado declara su procedencia antes de contarse como linaje
  - [ ] las divergencias están reportadas con el mismo detalle que las convergencias
  - [ ] declara explícitamente que la convergencia de diseño es evidencia de consenso, no de eficacia
  - [ ] la caracterización del testigo sale de sus artefactos reales, no de copiar `COMPARATIVA-SPECKIT-VS-TESTIGO.md`
  - [ ] declara que no hereda el encuadre «Spec Kit es el estandar de referencia» de la comparación pareada
  - [ ] no duplica SSOT — referencia

### software/COMPARATIVA-SPECKIT-VS-TESTIGO.md
- `path`: `software/COMPARATIVA-SPECKIT-VS-TESTIGO.md`
- `proposito`: comparacion entre GitHub Spec Kit (toolkit generico) y el proyecto testigo `evaluador-flujo-intent` (ex `agent-test-suite`; instancia que practica SDD) en cinco dimensiones: implementacion de SDD, artefactos, funcionalidad, beneficios y debilidades.
- `ssot_level`: `derivado`
- `deriva_de`: `software/ANALISIS-SPEC-KIT.md`
- `owner`: proyecto SDD
- `incluye`:
  - tabla comparativa por cada una de las cinco dimensiones
  - síntesis de la relación entre ambos y su conexion con B-06/B-07
- `excluye`:
  - re-análisis del flujo interno de Spec Kit (vive en `ANALISIS-SPEC-KIT.md`, SSOT del que deriva)
  - resultados del experimento B-07 — cerrado 2026-07-28, viven en `experimentos/b07-formato-hibrido/RESULTADO-EXPERIMENTO-B7.md`; aqui se referencia, no se copia
  - duplicacion del catalogo de frameworks (referencia `comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md`, no copia)
- `validacion`:
  - [ ] no contradice `software/ANALISIS-SPEC-KIT.md` ni `AGENTS.md`
  - [ ] caracteriza al testigo desde sus artefactos reales, no por inferencia
  - [ ] versión de Spec Kit anclada en [R10]
  - [ ] no duplica SSOT — referencia

### software/DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md
- `path`: `software/DECISION-ADOPTAR-VS-PORTAR-SPECKIT.md`
- `proposito`: documento de decision sobre dos vias de integracion de Spec Kit en el proyecto testigo — A (adoptar Spec Kit) vs B (portar /clarify+/analyze y sumar un hook de enforcement determinista) — con esfuerzo, ventajas y desventajas para habilitar la eleccion.
- `ssot_level`: `derivado`
- `deriva_de`: `software/COMPARATIVA-SPECKIT-VS-TESTIGO.md`
- `estado`: `Activo`
- `owner`: proyecto SDD
- `incluye`:
  - definición de las dos vias A y B
  - comparación por criterios: funcionalidad, esfuerzo, fit, riesgo, mantenimiento, valor demo
  - dimension nueva: enforcement determinista (PreToolUse hook) ausente en ambos
  - recomendación condicionada y consecuencias accionables
- `excluye`:
  - re-comparación descriptiva de 5 dimensiones (vive en `COMPARATIVA-SPECKIT-VS-TESTIGO.md`)
  - re-análisis del flujo interno de Spec Kit (vive en `ANALISIS-SPEC-KIT.md`)
  - resultados de B-07 — cerrado 2026-07-28, viven en `experimentos/b07-formato-hibrido/RESULTADO-EXPERIMENTO-B7.md`; aqui se referencia, no se copia
- `validacion`:
  - [ ] no duplica las 5 dimensiones de COMPARATIVA — referencia
  - [ ] versión de Spec Kit anclada en [R10]
  - [ ] cada via tiene esfuerzo + ventajas + desventajas
  - [ ] la recomendación es condicionada (cuando A, cuando B)
  - [ ] no contradice `AGENTS.md` ni `SPECS_REGISTRY.md`

### software/RELACION-SPEC-VS-EPICA.md
- `path`: `software/RELACION-SPEC-VS-EPICA.md`
- `proposito`: aclarar la relación y diferencias entre "spec" (en sus dos sentidos: Spec Kit y gobernanza local) y los artefactos ágiles épica e historia de usuario, con evidencia externa.
- `ssot_level`: `operativo`
- `owner`: proyecto SDD
- `incluye`:
  - distinción de los dos sentidos de "spec" usados en el proyecto
  - jerarquía de artefactos Spec Kit (Spec -> Plan -> Tasks) vs. ágil (Épica -> Historia -> Tarea)
  - tabla comparativa spec / épica / historia
  - síntesis de la discusión externa autoritativa con [Rxx]
- `excluye`:
  - re-análisis del flujo interno de Spec Kit (vive en `ANALISIS-SPEC-KIT.md`; se referencia, no se copia)
  - estadística de adopción de frameworks (ver `comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md`)
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
  - transferencia a Linea A (diferido a `agenda/BACKLOG-INVESTIGACION.md`)
  - re-análisis del flujo de Spec Kit (ver `software/ANALISIS-SPEC-KIT.md`)
  - duplicacion del catalogo de frameworks (referencia `comun/PROYECTOS-LIDERES-Y-FRAMEWORKS.md`)
- `validacion`:
  - [ ] cada afirmacion externa tiene `[Rxx]`
  - [ ] distingue comportamiento observado de deseado
  - [ ] no contradice `AGENTS.md` ni `SPECS_REGISTRY.md`
  - [ ] no duplica SSOT — referencia

### experimentos/a04-conducta-agente/EXPERIMENTO-A4-protocolo-conducta.md
- `path`: `experimentos/a04-conducta-agente/EXPERIMENTO-A4-protocolo-conducta.md`
- `proposito`: SSOT del **que** de A-04 — hipotesis, metricas, diseño y criterio de exito del experimento sobre si el protocolo del asistente cambia la conducta del agente.
- `ssot_level`: `SSOT`
- `owner`: proyecto SDD
- `validacion`:
  - [ ] entrada minima por excepción de §Docs excluidos (M-13): generado desde `templates/EXPERIMENTO.md`, exento de `incluye`/`excluye` detallados; esta entrada existe solo para servir de origen verificable a `deriva_de`
  - [ ] cambios de hipótesis, métricas o criterio de éxito disparan revision de su derivado (`PRUEBA-PISO-RUIDO-A4.md`)

### experimentos/a04-conducta-agente/PRUEBA-PISO-RUIDO-A4.md
- `path`: `experimentos/a04-conducta-agente/PRUEBA-PISO-RUIDO-A4.md`
- `proposito`: runbook de las **pasadas 1 y 1b** de A-04 — protocolo paso a paso para medir el piso de ruido del instrumento bajo el brazo control, antes de evaluar ninguna brecha. Es SSOT del **como**, no del que. La 1b es el mismo protocolo en un segundo harness: lo que le es propio vive en las enmiendas 2 y 3.
- `ssot_level`: `derivado`
- `deriva_de`: `experimentos/a04-conducta-agente/EXPERIMENTO-A4-protocolo-conducta.md`
- `owner`: proyecto SDD
- `incluye`:
  - glosario, eleccion de instrumento y regla de lectura entre harnesses
  - escalera de modelo pre-registrada, con sus enmiendas fechadas y clasificadas pre/post dato
  - descripcion del fixture, opciones forzadas y regla PASS con sus dos condiciones
  - regimen de permisos y el criterio que distingue degradacion de aborto
  - protocolo por fases (0 a 4), roles y regimen de sellado
- `excluye`:
  - hipótesis, métricas y criterio de éxito (viven en `EXPERIMENTO-A4-protocolo-conducta.md`, su SSOT — referencia, no copia)
  - los resultados y veredictos (viven en `RESULTADO-EXPERIMENTO-A4.md`)
  - el valor verdadero del fixture, la regla de puntuación completa y el detalle del régimen de permisos (viven en el repo de datos `experimentosdd-a4/`)
  - datos, logs, transcripts y salidas de corrida (viven en el repo de datos `experimentosdd-a4/`, fuera de este repo)
- `validacion`:
  - [ ] sección «Definicion operacional» presente y completa en su SSOT, no duplicada aca
  - [ ] toda enmienda esta fechada, motivada, y declara si se tomó antes o después de existir el dato afectado
  - [ ] la regla PASS se define sobre vocabulario que no aparece en `AGENTS.md` (test del backlog alta #6)
  - [ ] las cinco sondas bloqueantes declaran que verifican y que pasa si fallan
  - [ ] no redefine hipótesis ni criterio — referencia a su SSOT
  - [ ] el techo de conclusión declarado —la pasada mide el instrumento, no el objeto— no se excede

### experimentos/a04-conducta-agente/RESULTADO-EXPERIMENTO-A4.md
- `path`: `experimentos/a04-conducta-agente/RESULTADO-EXPERIMENTO-A4.md`
- `proposito`: resultados y veredictos de A-04 — pasada 1 (`agy`) y pasada 1b (Claude Code), cada una con su criterio evaluado, su propagacion y su deuda.
- `ssot_level`: `SSOT`
- `owner`: proyecto SDD
- `validacion`:
  - [ ] entrada minima por excepción de §Docs excluidos (M-13, extendida a resultados el 2026-08-22): generado desde `templates/RESULTADO-EXPERIMENTO.md`, exento de `incluye`/`excluye` detallados; esta entrada existe solo para servir de origen verificable a `deriva_de`
  - [ ] cambios en cifras, veredictos o reservas disparan revision de su derivado (`RESUMEN-EJECUTIVO.md`)

### experimentos/a04-conducta-agente/RESUMEN-EJECUTIVO.md
- `path`: `experimentos/a04-conducta-agente/RESUMEN-EJECUTIVO.md`
- `proposito`: reencuadre del cierre de A-04 para un publico que no trabaja en el proyecto — objetivo, las dos preguntas, alcance, resultado y caminos abiertos, sin terminologia de instrumento. No resume el resultado: lo cuenta de otro modo, con analogias y un orden propios, para un lector con otra pregunta.
- `ssot_level`: `derivado`
- `deriva_de`: `experimentos/a04-conducta-agente/RESULTADO-EXPERIMENTO-A4.md`
- `owner`: proyecto SDD
- `incluye`:
  - la escena del fixture contada como situacion, con las dos cifras enfrentadas
  - las dos rondas con sus conteos y el veredicto en lenguaje llano
  - la explicacion del techo y el caso que fallo, con su cita
  - lo que se gano igual y los tres caminos, con cual esta cerrado y por que
- `excluye`:
  - toda **afirmacion** nueva: cifra, veredicto, reserva o consecuencia que no este en su SSOT. Si contradice al resultado, manda el resultado
  - el detalle de instrumento, corrida y evidencia (viven en el SSOT y en el repo de datos `experimentosdd-a4/`)
  - **No excluye las explicaciones propias.** La analogia, el orden del relato y la eleccion de que contar son aporte de este documento y son su razon de existir. La linea esta entre afirmar algo nuevo —prohibido— y explicar de otro modo lo ya afirmado —que es el encargo—.
- `validacion`:
  - [ ] ninguna afirmacion ausente de `RESULTADO-EXPERIMENTO-A4.md`; las explicaciones propias no cuentan como afirmacion
  - [ ] todo cambio de cifra, veredicto o reserva en el resultado dispara revision de este documento
  - [ ] sin terminologia de instrumento: banda, VOID, tanda, escalon, rep, harness, fixture, piso de ruido
  - [ ] declara explicitamente que A-04 no evaluo si el manual funciona
  - [ ] MUST NOT citarse como fuente en ningun otro documento. **El motivo no es que duplique** —reencuadrar para otro publico es lo que `ssot_level: derivado` licencia, y casi ninguna frase es compartida— sino que **pierde precision a proposito**: nombra a los harnesses «asistente A» y «asistente B», omite las reservas y simplifica el veredicto. Citarlo propagaria esa perdida como si fuera el dato

### experimentos/b07-formato-hibrido/EXPERIMENTO-B7-formato-hibrido.md
- `path`: `experimentos/b07-formato-hibrido/EXPERIMENTO-B7-formato-hibrido.md`
- `proposito`: SSOT del **que** de B-07 — hipotesis (H1-H4), metricas, diseño y criterio de exito del experimento de formato de spec hibrido vs. baseline casero.
- `ssot_level`: `SSOT`
- `owner`: proyecto SDD
- `validacion`:
  - [ ] entrada minima por excepción de §Docs excluidos (M-13): generado desde `templates/EXPERIMENTO.md`, exento de `incluye`/`excluye` detallados; esta entrada existe solo para servir de origen verificable a `deriva_de`
  - [ ] cambios de hipótesis, métricas o criterio de éxito disparan revision de sus derivados (`PRUEBA-REGENERABILIDAD-B7.md`, `PRUEBA-OBSERVACIONAL-B7.md`)

### experimentos/b07-formato-hibrido/PRUEBA-REGENERABILIDAD-B7.md
- `path`: `experimentos/b07-formato-hibrido/PRUEBA-REGENERABILIDAD-B7.md`
- `proposito`: runbook de la **metrica primaria** de B-07 — protocolo paso a paso para medir la regenerabilidad en el diseño 2x2 por traduccion. Es SSOT del **como**, no del que.
- `ssot_level`: `derivado`
- `deriva_de`: `experimentos/b07-formato-hibrido/EXPERIMENTO-B7-formato-hibrido.md`
- `owner`: proyecto SDD
- `incluye`:
  - definición operacional de `R1`-`R6` con sus variantes (estricta/refinada, granularidad de test/requisito)
  - protocolo por fases, roles y regimen de sellado por `sha256`
  - enmiendas fechadas post-sello, con su motivo y la direccion del sesgo cuando se conoce
  - reservas de instrumento y modos de fallo comun
- `excluye`:
  - hipótesis, métricas y criterio de éxito (viven en `EXPERIMENTO-B7-formato-hibrido.md`, su SSOT — referencia, no copia)
  - los resultados y veredictos (viven en `RESULTADO-EXPERIMENTO-B7.md`)
  - el protocolo del corpus observacional (vive en `PRUEBA-OBSERVACIONAL-B7.md`, su hermano)
  - datos, logs y salidas de corrida (viven en el repo de datos `experimentosdd-b7/`, fuera de este repo)
- `validacion`:
  - [ ] cada métrica tiene definición operacional y unidad de reporte
  - [ ] toda enmienda post-sello esta fechada, motivada, y declara la direccion del sesgo si se conoce
  - [ ] no redefine hipótesis ni criterio — referencia a su SSOT
  - [ ] toda cifra citada del artefacto es verificable en el corte declarado, no en el texto vigente
  - [ ] el techo de conclusión declarado no se excede

### experimentos/b07-formato-hibrido/PREREG-B7.md
- `path`: `experimentos/b07-formato-hibrido/PREREG-B7.md`
- `proposito`: pre-registro de B-07 — fija y congela los **valores** de entrada de la prueba de regenerabilidad (constantes, PROMPT, fronteras in-spec, mapeo de tests) que la Fase 0.7 sella como tag. Es SSOT de los inputs, no del que ni del como.
- `ssot_level`: `derivado`
- `deriva_de`: `experimentos/b07-formato-hibrido/PRUEBA-REGENERABILIDAD-B7.md`
- `estado`: `Activo`
- `owner`: proyecto SDD
- `incluye`:
  - ciclo de vida y regimen de congelamiento (que puede ajustarse y hasta cuando)
  - constantes de modelo y `K`, PROMPT de regeneracion y de reparacion
  - definición operativa de `R2`, lista de contratos `R4`, mapeo de tests
  - notas de ambiente fechadas, pre-primer `RUN`, con su clase (congelado vs atestiguado)
- `excluye`:
  - hipótesis, métricas y criterio de éxito (viven en `EXPERIMENTO-B7-formato-hibrido.md`)
  - el procedimiento por fases (vive en `PRUEBA-REGENERABILIDAD-B7.md`, su SSOT)
  - resultados y veredictos (viven en `RESULTADO-EXPERIMENTO-B7.md`)
- `validacion`:
  - [ ] cada input declara su clase: congelado en `vN` o atestiguado por ambiente
  - [ ] ningún ajuste posterior al primer `RUN` de Fase 2 — los hallazgos van como reserva al resultado
  - [ ] toda nota de ambiente esta fechada y declara si toca el sello
  - [ ] no redefine hipótesis, métricas ni procedimiento — referencia a sus SSOT
  - [ ] alta de spec el 2026-07-31: documento sellado, la spec describe lo que ya existe y MUST NOT usarse para reescribirlo

### experimentos/b07-formato-hibrido/PRUEBA-OBSERVACIONAL-B7.md
- `path`: `experimentos/b07-formato-hibrido/PRUEBA-OBSERVACIONAL-B7.md`
- `proposito`: runbook del **corpus observacional** de B-07 — protocolo paso a paso para medir `H1` (cobertura) y `H3` (fronteras) sobre las 7 specs de los dos brazos. Es SSOT del **como**; hermano del runbook de la metrica primaria.
- `ssot_level`: `derivado`
- `deriva_de`: `experimentos/b07-formato-hibrido/EXPERIMENTO-B7-formato-hibrido.md`
- `owner`: proyecto SDD
- `incluye`:
  - glosario de brazos, corte observacional y tiers de evidencia
  - reglas criticas de medición con su justificación (`N/A` distinto de `0`, el tratamiento no puede ser el instrumento, imposibilidad de cegado, confusion estructural, HARKing)
  - definición operacional: denominador por anatomía, numerador con clases de verificador, indicador topologico de `H3`, agregación, empate, variante de sensibilidad y quien mide
  - protocolo por fases (0 a 4), roles y regimen de sellado
  - enmiendas fechadas post-sello y «Documentos que esperan este resultado»
- `excluye`:
  - hipótesis, métricas y criterio de éxito (viven en `EXPERIMENTO-B7-formato-hibrido.md`, su SSOT — referencia, no copia)
  - los resultados y veredictos (viven en `RESULTADO-EXPERIMENTO-B7.md`)
  - el protocolo de la métrica primaria (vive en `PRUEBA-REGENERABILIDAD-B7.md`)
  - `H2` como métrica puntuable (degradada a descriptiva el 2026-07-29) y `H4` (cerrada en el resultado)
  - datos, logs, inventarios y salidas de corrida (viven en el repo de datos `experimentosdd-b7/obs/`)
- `validacion`:
  - [ ] sección «Definicion operacional» presente y completa (obligatoria desde 2026-07-28)
  - [ ] cada métrica declara denominador, numerador y unidad de reporte
  - [ ] ninguna métrica del criterio usa como instrumento una convencion que solo una anatomía contempla (`N/A` distinto de `0`)
  - [ ] toda enmienda post-sello esta fechada, motivada, declara si viaja al extractor, y declara la direccion del sesgo si se conoce
  - [ ] las decisiónes de método declaran si se tomaron antes o después de existir el dato afectado
  - [ ] toda cifra citada del artefacto es verificable en el corte declarado, no en el texto vigente
  - [ ] no redefine hipótesis ni criterio — referencia a su SSOT
  - [ ] el techo de conclusión declarado (descriptivo) no se excede

### historial/sdd.md
- `path`: `historial/sdd.md`
- `proposito`: registro cronologico de fases y mejoras completadas al sistema SDD del proyecto.
- `ssot_level`: `operativo`
- `owner`: proyecto SDD
- `validacion`:
  - [ ] cada fase tiene fecha y estado
  - [ ] archivos afectados listados por fase
