# Análisis: caso de campo 1 — el método de este repositorio aplicado a un cuerpo documental ajeno (Línea A)

Fecha: 2026-08-30.
Fuente: caso de campo 1 [R40], commit `c3dd480` (2026-08-29), rama `main`. Fuente reservada; extracto saneado de su capa de método en `../fuentes-externas/caso-campo-1/`, con el mapeo de anonimización en su `PROCEDENCIA.md`.
Alcance: Línea A (docs e investigación).

---

## Contexto

El caso es un repositorio de documentación normativa corporativa que adoptó el método de este repositorio en agosto de 2026 y lo viene ejerciendo desde entonces. Al commit analizado tiene 68 commits, 29 specs registradas, 40 entradas de historial de método, constitución propia con cinco principios, gate de commit instalado y un backstop determinista de 1296 líneas con 22 checks.

Lo que lo hace distinto de los cinco casos ya analizados en Línea B es que **no es una implementación de SDD**: es este método, portado, corriendo sobre un objeto de trabajo que no es investigación de método. Es la única aplicación de campo de Línea A conocida fuera de este repositorio.

Este documento lo caracteriza y extrae lo portable. La sección siguiente condiciona todo lo demás.

---

## Procedencia: por qué NO cuenta como linaje

`../software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md` exige que todo caso nuevo declare su procedencia antes de contarse, y su regla 1 dice que un método que hereda la anatomía de otro no agrega un linaje sino una copia. Acá el filtro es más categórico que en cualquier caso anterior.

**La fuente lo declara ella misma.** El docstring de su backstop dice que fue portado desde `tools/check_docs.py` de este repositorio, y enumera qué checks no se portaron y por qué. No hay que inferir la procedencia: está escrita.

**Mismo autor, misma cadena.** Es del autor de este repositorio, igual que el proyecto testigo y que el kit de [R39]. La cadena es este repositorio → caso de campo.

**Arrastra el vocabulario entero.** Su bloque de salida obligatorio es el `[SDD-Check]` de `../AGENTS.md`; su constitución usa la forma invariante + `Enforcement` + `Detalle` de `../CONSTITUTION.md`; su registro usa `ssot_level`, `deriva_de`, `estado` y la regla de propagación tal como están definidos acá. Ninguna coincidencia entre los dos métodos es dato.

**Consecuencia.** MUST NOT sumarse como columna en `../software/CONVERGENCIA-IMPLEMENTACIONES-SDD.md`, y ningún acuerdo entre este documento y aquel método puede leerse como evidencia de invariancia: es autocorrelación por construcción. La fuente además **no reporta ninguna medición**, así que MUST NOT citarse como evidencia de efectividad de ninguna práctica.

**Lo que sí gana el corpus.** Dos cosas que ningún otro caso da. Primero, es la única vez que el método de este repositorio se ejerció sobre un dominio que no es su propia investigación, lo que permite un contraste que en un solo corpus está confundido (§El corpus que agrega). Segundo, y más inmediato: mecanismos que acá están en el backlog como propuestas ya corrieron allá contra un grafo real, y dejaron decisiones de diseño y resultados negativos que no hay que volver a descubrir.

---

## Bajo qué reglas se cita este caso

La organización destinataria no se nombra. Sus documentos y sus áreas internas se nombran **por rol**, nunca por nombre propio —ni siquiera por el nombre saneado que usa el extracto—. Ningún contenido normativo suyo se cita ni se parafrasea.

La distinción que ordena esto, y que conviene tener escrita porque no es obvia: quitar el nombre resuelve la **identificación**, no la **reproducción**. Citar el texto de un documento ajeno sigue siendo reproducirlo aunque no diga de quién es. Por eso la restricción no es «anonimizar y citar libremente» sino dos reglas separadas — no identificar, y no reproducir.

Lo que sí es citable, y es todo lo que este análisis necesita: la capa de método, que es la portada desde acá; y los **datos agregados** sobre su corpus —conteos, fechas, presencia de campos—, que son hechos y no expresión.

Límite declarado: anonimizado no es no-identificable. El vocabulario del dominio y el sector siguen siendo pista. Este documento acepta ese riesgo residual y lo acota no dando ningún detalle del contenido que no sea estructural.

---

## Qué hay adentro

### La superficie de método, comparada

| | Este repositorio | Caso de campo 1 |
|---|---|---|
| Documentos autorados | 50 | 29 specs registradas |
| Entradas de historial de método | 23 | 40 |
| Backstop | 1021 líneas, 19 checks | 1296 líneas, 22 checks |
| Gate de commit | sí, fail-closed | sí, fail-closed |
| Principios | 7 | 5 |
| Antigüedad de la historia git | 2026-07-31 | 2026-08-18 |

El caso es más chico en documentos y más grande en iteraciones y en tooling. La lectura obvia —hizo más método en menos tiempo— es correcta y tiene una explicación estructural: recibió el protocolo ya formado, así que sus 40 iteraciones no incluyen las que acá se gastaron en inventarlo.

### Los checks: qué se portó y qué es propio

Portados de acá, en algunos casos con parser reescrito: cobertura de spec, campos de spec, ciclos de `deriva_de`, links, rutas en backticks, tabla SSOT, colisión de SSOT, ausencia de emoticones, higiene de archivo, gate instalado, historial de método, precedencia, constitución, campos del bloque de salida, marcador de clarificación y catálogo de referencias.

Propios del caso, sin equivalente acá:

| Check | Qué hace | Portable |
|---|---|---|
| `propagacion` | con contexto de commit, nombra los derivados de un SSOT modificado que quedaron fuera del commit | sí — es `../agenda/MEJORAS-METODO.md` M-16 |
| `normativos` | verifica que el módulo donde vive una regla de la que depende otro check siga siendo importable | sí — encuadra M-31 |
| `gate-reglas` | corre la tabla de regresión que un gate clasificador lleva al lado de sus reglas | sí — es M-34 |
| `skill-adapters` | falla si los adaptadores por asistente divergen de su fuente única | sí — es M-17 |
| `changelog-descripcion` | exige que toda entrada versionada del changelog tenga su descripción completa | patrón, no check: convertir en verificación un MUST que sostenía la disciplina |
| `links-docx` | verifica que los links sobrevivan una exportación a formato ofimático | no — depende de una tubería de publicación que acá no existe |

**Lo que decidió no portar, y es instructivo.** Su docstring declara dos checks nuestros que dejó afuera —los que vigilan que el alcance y los campos de una spec vivan en un solo lugar— con el motivo escrito: su registro **todavía no declara esa regla global**, así que portar el check marcaría como error una columna legítima. Es la conducta correcta y vale registrarla: un verificador sin la regla que lo justifica produce falsos positivos con formato de autoridad.

### Los tres parsers que tuvo que reescribir

No copió el backstop: lo reescribió donde sus convenciones difieren. Las specs viven en tablas y no en viñetas; la tabla SSOT vive en el índice y no en el registro; un SSOT puede no ser Markdown y `deriva_de` admite un sufijo de sección. Es evidencia menor pero directa sobre una pregunta de Línea A: **qué parte del método es transferible y qué parte es convención de forma**. La respuesta de este caso es que la estructura de la regla viaja y la sintaxis no.

---

## Los tres aportes

### 1. El Principio III tiene implementación de referencia

`../CONSTITUTION.md` III (propagación bidireccional del conocimiento) es uno de los dos principios que declaran `Verificador: ninguno`, con M-16 registrado como candidato. El caso implementó ese candidato el 2026-08-25 y lo viene corriendo desde entonces.

El detalle de diseño, la tabla de validación y qué mitad queda abierta están volcados en `../agenda/MEJORAS-METODO.md` M-16 y no se reproducen acá. Lo que corresponde a este documento es el saldo: de los dos `ninguno` de nuestra constitución, uno deja de ser una propuesta sin probar. El otro —integridad del registro experimental— no tiene candidato y sigue sin tenerlo.

La decisión más transferible es la que menos parece técnica: el check emite **WARN y nunca ERROR**, con el motivo escrito de que bloquear un commit por tocar un SSOT enseña a usar `--no-verify`, que es peor que no tener el check.

### 2. Un resultado negativo sobre M-30, antes de ejecutarlo

M-30 propone rotar `../historial/sdd.md` por período. El caso llegó al mismo problema sin coordinación —su historial tiene 40 entradas y ~1800 líneas, y tampoco tiene regla de rotación— y además **ya probó y descartó la variante alternativa**: mantener un índice de entradas. Ese índice llegó a estar trece iteraciones atrasado y apuntando a un archivo eliminado.

Detalle y consecuencia para la reserva 3 de M-30, en `../agenda/MEJORAS-METODO.md`.

Lo que pertenece a este documento es la parte que no es sobre historiales: cuando ese defecto apareció, **ningún check lo vio**, y las dos razones son nuestras también. Su recordatorio de propagación no lo detectó porque el documento no declaraba `deriva_de` de nada —un recordatorio de propagación es tan bueno como el grafo que lee—, y su check de rutas ignora las referencias en backticks sin barra, que es exactamente la decisión de diseño de nuestro `check_backtick_paths`. Los dos huecos son de diseño, están razonados, y juntos dejaron pasar un archivo borrado.

### 3. Dos huecos que el caso iluminó en nuestro propio backstop

El check `normativos` del caso existe para que un import roto no apague en silencio al check que depende de él. Aplicado como pregunta a nuestro backstop, el 2026-08-30 se verificó que **renombrar el título de la tabla SSOT del registro deja dos checks en no-op y el backstop sale 0 ERROR**. El hueco, y el hecho de que el patrón ya estaba aplicado dos veces en nuestro propio código sin estar declarado, están en M-31.

El check `gate-reglas` expone el segundo: varios de nuestros checks no verifican, **clasifican**, y ninguno tiene una tabla de casos que pruebe que siguen clasificando como declaran. En M-34.

---

## Lo que NO es novedad, aunque lo parezca

Conviene dejarlo escrito porque fue una lectura preliminar errónea de este mismo análisis. El caso declara en el campo `Verificador:` de cada principio **qué mitad del invariante ve el check y cuál no**, y su §Límite honesto aclara que no quedarse sin `ninguno` no significa estar cubierto.

Eso no es un refinamiento a importar: es una práctica de `../CONSTITUTION.md`, donde los siete principios ya declaran su mitad cubierta y su mitad humana, y el §Límite honesto ya distingue cobertura parcial de sustantiva. El caso la heredó.

Lo que sí es dato —y es un dato débil, del tipo que la procedencia permite— es que la práctica **sobrevivió al transporte**: se portó a otro dominio sin degradarse a una lista de nombres de check. Es una observación sobre robustez de la convención, no evidencia de nada.

---

## El corpus que agrega a Línea A

`../agenda/BACKLOG-INVESTIGACION.md` #15 declaraba que el único corpus de Línea A con estructura de iteración era este repositorio, con 23 entradas. Con el caso, Línea A pasa a **63 iteraciones** repartidas en dos corpus que comparten método y difieren en dominio.

Qué habilita eso, y qué no:

- **Habilita** el contraste que el ítem #14 necesita. En un solo corpus, «lo que cuesta el protocolo» y «lo que cuesta investigar sobre el protocolo» están confundidos y no hay forma de separarlos. Con un segundo corpus donde el objeto de trabajo es un cuerpo normativo, el contraste es la única estimación disponible. El ítem 18 del backlog lo recoge.
- **No habilita** ninguna afirmación sobre SDD en general. Los dos corpus son del mismo autor: sumarlos no toca la autocorrelación declarada en §Procedencia, la agrava dándole más `n`. Todo resultado es sobre **este** método ejercido por **este** autor en dos dominios, y eso MUST escribirse en el resultado, no en una nota al pie.
- **No habilita** citar contenido: lo medible son datos agregados por iteración.

---

## Conclusiones para Línea A

### C1. Un mecanismo propuesto acá ya corrió allá, y eso cambia el costo de decidirlo

M-16 dejó de ser una propuesta de diseño para pasar a ser una portación con tres decisiones ya tomadas y una prueba de discriminación ya corrida. Es lectura obligatoria antes de implementarlo, y su parte abierta —la mitad ascendente, contra el campo `Derivados a revisar`— queda identificada como tal.

### C2. El resultado negativo vale más que la implementación

De todo lo que el caso aporta, lo más caro de conseguir por cuenta propia es lo que **no funcionó**: un índice de historial mantenido a mano se atrasa trece iteraciones. M-30 puede escribir su regla sabiendo cuál de las dos variantes ya falló, y por qué falló —obligación manual sin gate—, sin gastar un semestre en comprobarlo.

### C3. Un backstop puede reportar salud sobre un check que ya no corre

Verificado en nuestro propio código el 2026-08-30. La clase de defecto —el mecanismo correcto que los casos nuevos no adoptan— está nombrada en `../fuentes-externas/sdd-first/docs/PATRONES.md` y tiene instancia acá. Candidata en M-31.

### C4. La estructura de la regla viaja; la sintaxis, no

Los tres parsers reescritos son la evidencia más limpia que el corpus tiene sobre transferibilidad del método. Es dato menor y confundido —mismo autor—, pero es direccional y barato: lo que hubo que reescribir fue el reconocedor de forma, no la regla.

### C5. Lo que NO conviene traer

- **Su check de exportación a formato ofimático**, que depende de una tubería de publicación inexistente acá.
- **Su constitución de cinco principios.** Difiere de la nuestra por el dominio, no por mejora: no tiene principio de separación método/contenido —lo difirió a una enmienda y lo dejó como norma de proceso— ni de integridad del registro experimental, porque no corre experimentos. Adoptar su recorte sería perder dos invariantes que acá sí tienen objeto.
- **Su acuerdo con nuestro método como respaldo.** Es la tentación obvia y hay que decirlo dos veces: un repositorio que recibió este protocolo y lo reproduce no confirma nada del protocolo.

---

[SDD-Check]
- Spec leida: SI (spec registrada en `../SPECS_REGISTRY.md` para este doc, dada de alta en la misma iteracion)
- Incluye/Excluye verificado: SI - no se cita ni parafrasea contenido normativo del caso, no se nombra la organizacion ni sus areas, las decisiónes de adopcion se remiten a `../agenda/MEJORAS-METODO.md` y los diseños de experimento a `../agenda/BACKLOG-INVESTIGACION.md`, y la lectura cruzada de convergencia queda en su SSOT
- Validaciones aplicadas: version anclada en `../REFERENCIAS.md` [R40] con commit `c3dd480` y fecha; procedencia resuelta antes de la lectura, con la particularidad de que la fuente declara ella misma la portacion en el docstring de su backstop; ninguna coincidencia se presenta como convergencia y la advertencia esta escrita dos veces, en §Procedencia y en C5; la fuente no reporta medición y eso queda dicho; documentos y areas nombrados por rol, sin nombre propio ni saneado; cifras citadas son conteos y fechas del corpus; cada mecanismo citado se verifica en `../fuentes-externas/caso-campo-1/`; refs internas verificadas con `../tools/check_docs.py`; sin emoticones; fechas YYYY-MM-DD
- SSOT afectado: ninguno (doc operativo)
- Derivados a revisar: `../agenda/MEJORAS-METODO.md` (M-16, M-17 y M-30 anotados con evidencia de campo; M-31 y M-34 dados de alta) y `../agenda/BACKLOG-INVESTIGACION.md` (items 17 y 18 dados de alta; inventario de corpus de #15 corregido) - los dos ya modificados en esta misma iteracion, no solo señalados
- Cobertura: completa - las cinco conclusiónes mapean a secciones de caracterizacion, y las cuatro accionables tienen ID de destino ya creado
- Deuda arrastrada: la viabilidad contractual de publicar aprendizajes derivados del caso, aun anonimizados, no fue verificada por este analisis y es previa a cualquier difusion fuera de este repositorio; la mitad ascendente de M-16 sigue sin implementacion en ningun lado; el §Limite honesto de `../CONSTITUTION.md` sigue declarando dos `Verificador: ninguno` y este documento no lo modifica
- Riesgos/reservas: el analisis lee la capa de metodo del caso, no la ejecuta, asi que las capacidades descritas son las declaradas por su codigo y su historial y no verificadas por corrida - con una excepcion, el hueco de C3, que si se verifico ejecutando nuestro propio backstop; la fuente es del mismo autor y recibio este protocolo, con sesgo de confirmacion estructural y no solo probable; anonimizado no es no-identificable y el riesgo residual de reidentificacion por vocabulario de dominio queda aceptado y declarado; el extracto saneado no entra a git, asi que la verificabilidad de las citas depende de una copia local
