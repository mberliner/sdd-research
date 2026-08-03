# Guia de Inicio: Proyecto de Investigacion con SDD y Asistentes IA

| Creacion | Version | Owner | ssot_level |
|----------|---------|-------|------------|
| 2026-03-18 | 0.4 | proyecto SDD | operativo |

---

## Concepto central

Cada asistente IA necesita dos cosas para ser util en un proyecto de analisis: **contexto** (que es este proyecto, quienes, para que) y **reglas operativas** (como generar, validar, no duplicar). SDD formaliza ambas en documentos que el asistente lee antes de actuar.

---

## Documentos fundacionales al inicio (orden de creacion)

### 1. `INSTRUCCIONES_IA.md` (o `CLAUDE.md`, `GEMINI.md`, etc.)

Protocolo de comportamiento del asistente. Es el primer archivo que lee cualquier IA al iniciar sesion.

Contenido minimo:
- Punteros a los SSOTs principales (no replica contenido)
- Protocolo de consulta de fuentes: cuando hay una fuente interna, leerla ANTES de responder con conocimiento general
- Protocolo SDD: leer la spec del doc antes de generarlo o modificarlo
- Reglas globales: estilo, formato, que esta prohibido
- Ultima actualizacion / currentDate

Regla critica: este archivo NO contiene contenido sustantivo. Solo apunta a los SSOTs donde vive ese contenido. Si el contenido ya existe en un SSOT, agregar solo el puntero.

---

### 2. `CONTEXTO.md`

SSOT del "quien, que, por que, estado actual". Todo actor, objetivo e iniciativa del proyecto vive aqui.

Contenido minimo:
- Proposito del proyecto (2-3 parrafos)
- Actores clave y sus roles
- Estado actual por pilar, tema o frente de trabajo
- Nombres canonicos del dominio (glosario de terminos)
- Fecha de ultima actualizacion

Sin esto, el asistente inventa contexto o usa terminos inconsistentes entre sesiones.

---

### 3. `00-INDEX.md`

Mapa del repositorio. Dos secciones obligatorias:

**Tabla SSOT** — el contrato de no-duplicacion:

| Concepto | SSOT (doc autoritativo) | Quien referencia |
|----------|------------------------|-----------------|
| Glosario del dominio | `CONTEXTO.md` | todos |
| Metricas del proyecto | `metricas/METRICAS.md` | reportes, dashboards |

**Inicio rapido** — orden sugerido de lectura para un asistente o colaborador nuevo.

---

### 4. `SPECS_REGISTRY.md`

Registro de specs por documento. Antes de generar o modificar cualquier doc, el asistente lee la spec de ese doc.

Estructura de cada entrada:

| Campo | Descripcion |
|-------|-------------|
| `path` | Ruta relativa del documento |
| `proposito` | Una linea: para que existe |
| `audiencia` | A quien esta dirigido |
| `ssot_level` | SSOT / derivado / operativo |
| `incluye` | Que DEBE tener |
| `excluye` | Que NO debe tener |
| `deriva_de` | Si es derivado: el SSOT origen |
| `owner` | Quien es responsable |
| `validacion` | Checks antes de dar el doc por bueno |
| `estado` | Activo / Borrador / Deprecado |

Campo `ssot_level`:
- `SSOT`: este doc ES la fuente autoritativa del concepto
- `derivado`: resume o sintetiza otro SSOT (campo `deriva_de` indica cual)
- `operativo`: guias de proceso, plantillas, indices de navegacion

Regla de propagacion: al modificar un SSOT, listar sus derivados y verificar si necesitan actualizacion.

---

### 5. `fuentes/INDICE_FUENTES.md`

Indice de todas las fuentes del proyecto con tabla de dispatch por tema.

**Tabla dispatch** (la mas importante):

| Tema consultado | Fuente a leer primero |
|-----------------|----------------------|
| Marco regulatorio del dominio | `fuentes/norma_X.txt` |
| Metricas externas de referencia | `fuentes/reporte_Y.txt` |

**Tabla de fuentes**: archivo, categoria, descripcion breve.

El asistente usa la tabla dispatch antes de responder: si el tema tiene fuente interna, lee la fuente primero, no responde desde conocimiento general.

---

## Estructura de directorios recomendada

```
proyecto/
|
+-- INSTRUCCIONES_IA.md       # Protocolo para Claude/Gemini/etc.
+-- CONTEXTO.md               # SSOT de actores, objetivos, estado
+-- 00-INDEX.md               # Navegacion + tabla SSOT
+-- SPECS_REGISTRY.md         # Registro de specs por documento
|
+-- fuentes/
|   +-- INDICE_FUENTES.md     # Dispatch por tema + tabla de fuentes
|   +-- documento_externo.txt # Fuentes convertidas a .txt
|   +-- documento_externo.pdf # Fuentes originales
|
+-- 01-tema-principal/        # Documentos por pilar o tema
|   +-- DOC_SSOT_1.md
|   +-- DOC_DERIVADO.md
|
+-- normativa/                # Si hay marcos regulatorios o politicas
    +-- POLITICA_X.md
```

---

## Reglas operativas para el asistente IA

### Antes de trabajar con cualquier documento del proyecto
1. Verificar en `00-INDEX.md` (tabla SSOT) cual es el documento autoritativo del concepto.
2. Usar ese documento como base, independientemente de que otros archivos esten disponibles o haya referenciado el usuario.
3. No asumir que un archivo encontrado en cualquier directorio es el oficial sin verificar la tabla SSOT primero.

Esta regla aplica a cualquier accion: leer, comparar, editar, analizar, citar.

### Antes de generar o modificar un documento
1. Leer la entrada en `SPECS_REGISTRY.md` para ese doc.
2. Verificar que la solicitud esta dentro del alcance (incluye/excluye).
3. Si el doc no tiene spec: proponer spec minima (5 campos) y esperar aprobacion antes de proceder.
4. Si la solicitud viola la spec: senalar el conflicto y esperar instruccion. No proceder ni proponer alternativas sin aprobacion explicita.

### Antes de responder sobre un tema del dominio
1. Verificar la tabla dispatch en `fuentes/INDICE_FUENTES.md`.
2. Si hay match: leer la fuente indicada antes de responder.
3. No responder con conocimiento general cuando existe fuente interna relevante.

### Post-generacion
1. Verificar checks de validacion de la spec del doc.
2. Si el doc modificado es un SSOT: listar sus derivados (campo `deriva_de` en otras specs) y verificar si necesitan actualizacion.

---

## Principios de arquitectura de conocimiento

| Principio | Descripcion |
|-----------|-------------|
| Un concepto, un SSOT | Cada concepto tiene un unico doc autoritativo. Los demas referencian, no repiten |
| Specs antes de generar | No se genera un documento sin spec aprobada |
| Fuentes primero | Si existe fuente interna, el asistente la lee antes de usar conocimiento general |
| INSTRUCCIONES_IA no contiene contenido | Solo punteros a SSOTs, no replica contenido |
| Versionado gradual | Version menor a 1.0 hasta aprobacion formal por el owner |
| Nombres canonicos | Un glosario en CONTEXTO.md, referenciado por todos |

---

## Secuencia de inicio desde cero

```
Dia 1 — Fundaciones
  1. Crear CONTEXTO.md  (quien, que, por que, actores, nombres canonicos)
  2. Crear INSTRUCCIONES_IA.md  (punteros + reglas + protocolo SDD)
  3. Crear SPECS_REGISTRY.md  (vacio, con la estructura de campos)
  4. Crear 00-INDEX.md  (estructura inicial, tabla SSOT con los primeros docs)

Dia 2 — Fuentes
  5. Convertir fuentes a .txt y depositar en fuentes/
  6. Crear fuentes/INDICE_FUENTES.md  con tabla dispatch por tema

A partir de ahi — Documentos del proyecto
  7. Antes de crear cada doc: agregar su spec en SPECS_REGISTRY.md
  8. Generar el doc con el asistente (que ya tiene las reglas y el contexto)
  9. Actualizar 00-INDEX.md con el nuevo SSOT o referencia
```

---

## Por que este metodo funciona para proyectos de investigacion con IA

El problema central al trabajar con asistentes en proyectos de analisis: el asistente no sabe que ya existe, inventa contexto, duplica informacion y usa nombres inconsistentes entre sesiones. SDD resuelve esto con tres mecanismos:

1. **Contexto declarativo** (CONTEXTO.md + fuentes): el asistente sabe que existe antes de responder.
2. **Contrato de generacion** (SPECS_REGISTRY): el asistente sabe que debe y no debe generar.
3. **Protocolo de no-duplicacion** (tabla SSOT en 00-INDEX.md): el asistente sabe donde vive cada concepto.

El resultado es un repositorio donde cualquier asistente nuevo puede orientarse en 5 minutos leyendo INSTRUCCIONES_IA → CONTEXTO → 00-INDEX, y actuar de forma coherente con lo que ya existe.

---

## Referencias internas

- Modelo SDD dual (docs e investigacion vs. software): `../comun/MARCO-COMPARATIVO-DOS-LINEAS.md`
- Implementacion pragmatica sin CI: `../comun/IMPLEMENTACION-INICIAL-CONTEXTO-ACTUAL.md`
- Anti-patron cascada encubierta y circuitos de aprendizaje: `../comun/SDD-ADAPTATIVO-VS-CASCADA.md`
- Registro de specs: `../SPECS_REGISTRY.md`
