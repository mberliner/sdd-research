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

## Nombres

- Documentos: mayúsculas, separados por guión (ej. `PLAN-PRUEBAS.md`).
- Carpetas de `experimentos/`: `<id en minúscula sin guión><guión><nombre corto>`, donde el
  nombre corto sale del título del documento de diseño y no se inventa. Cuándo corresponde
  abrir una, y qué necesita spec adentro: `SPECS_REGISTRY.md` §Reglas globales.

## Mensajes de commit

- `docs: <resumen imperativo corto>` (ej. `docs: align PLAN-PRUEBAS with SSOT metrics`).
- Sin firma de asistente.
- Cadencia: `AGENTS.md` §Al cerrar una iteración.
