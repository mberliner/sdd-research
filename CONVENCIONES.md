# Convenciones

> **SSOT de léxico y forma.** Cómo se lee y cómo se escribe todo documento del proyecto.

Transversal a la cadena de precedencia de `CONSTITUTION.md` §Governance, no un eslabón de
ella: autoritativo sólo en materia de forma y léxico. Ante choque con una regla de alcance
o de procedimiento, gana la otra.

## Norma de interpretación

| Término | Significado |
|---|---|
| `MUST` | obligatorio |
| `SHOULD` | recomendado fuerte; si no se cumple, debe justificarse |
| `MAY` | opcional |

Colocación. Dos formas admitidas:

- Enunciado normativo suelto (viñeta, ítem, criterio): `MUST — <enunciado>`.
- Predicado dentro de una oración: `<sujeto> MUST <verbo>` (ej. "Todo cambio documental MUST
  mapearse a una spec registrada").

El término en glosario o citado como palabra es mención, no uso: no lleva ninguna de las dos
formas.

## Forma de los documentos

- Markdown como formato fuente; secciones cortas y escaneables.
- Fechas en formato YYYY-MM-DD.
- Sin emoticones en documentos de contenido.
- Ortografía: el contenido en español MUST usar ortografía correcta con tildes y signos
  (acentos, "ñ", apertura de interrogación/exclamación). Aplica a documentos nuevos y a todo
  documento que se edite. Excepciones: identificadores técnicos, rutas, nombres de archivo y
  claves de los bloques normativos (ej. campos del `[SDD-Check]` y nombres de campo de spec
  como `validacion`, `proposito`) MUST conservarse sin tildes por estabilidad grep-able. Los
  documentos preexistentes sin tildes SHOULD migrarse de forma oportunista al tocarlos, no en
  una reescritura masiva.

## Citas a fuentes externas

Las fuentes externas no viven en este repositorio, y se citan de forma que cualquiera las
encuentre sin tener la copia local de quien escribió.

- Repositorio de código: `[Rxx]` más `<repo>:<ruta>`, donde `<repo>` es el nombre del
  repositorio en la URL que registra `REFERENCIAS.md` (ej. `[R39]`,
  `sdd-first:templates/docs/SPEC-FORMAT.md`).
- Commit: la cita no lo repite. Se resuelve en este orden: el que declare el encabezado de la
  sección o del documento que cita; si no hay, el que `REFERENCIAS.md` asigne a ese material;
  si tampoco, el último corte registrado en `REFERENCIAS.md`. Una cita que necesite fijar otro
  commit lo escribe en línea: `<repo>@<commit>:<ruta>`.
- Repositorio hermano —del mismo autor, sin entrada en `REFERENCIAS.md`—: la misma forma
  `<repo>:<ruta>`, sin `[Rxx]`. Repositorios hermanos admitidos: `investigaIA`,
  `experimentosdd-a4`, `experimentosdd-b7`. Sumar uno es editar esta línea, que es de donde
  `tools/check_docs.py` toma la lista.
- Paper, documento o página: sólo `[Rxx]`. La versión (ej. `v2` de arXiv) la lleva
  `REFERENCIAS.md`.
- Fuente reservada, no pública: `[Rxx]` sin ruta.
- MUST NOT citarse una copia local —clon, enlace del sistema de archivos, descarga— aunque
  exista en la máquina de quien escribe: no la tiene nadie más.
- Registro fechado —`historial/`, `experimentos/` y los bloques `[SDD-Check]` de entregas
  anteriores dentro de cualquier documento— conserva la forma de cita de su momento, prosa
  incluida («clon vendored»), y no se reescribe. Única excepción: fuera de `historial/` y
  `experimentos/`, una ruta a copia local se reescribe aunque esté en un bloque viejo, porque
  el check no distingue bloques.
- `tools/check_docs.py` verifica esta sección (check `ruta-externa`): ninguna ruta a copia
  local, ni en código ni en prosa, y ningún `<repo>` que no esté en `REFERENCIAS.md` o en la
  lista de hermanos. Exentos `historial/` y `experimentos/`.

## Nombres

- Documentos: mayúsculas, separados por guión (ej. `PLAN-PRUEBAS.md`).
- Carpetas de `experimentos/`: `<id en minúscula sin guión><guión><nombre corto>`, donde el
  nombre corto sale del título del documento de diseño y no se inventa. Cuándo corresponde
  abrir una, y qué necesita spec adentro: `SPECS_REGISTRY.md` §Reglas globales.

## Mensajes de commit

- `docs: <resumen imperativo corto>` (ej. `docs: align PLAN-PRUEBAS with SSOT metrics`).
- Sin firma de asistente.
- Cadencia: `AGENTS.md` §Al cerrar una iteración.
