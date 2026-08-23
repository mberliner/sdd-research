# Template de Experimento

## Metadata
- ID:
- Linea: docs-investigacion | software
- Fecha inicio:
- Responsable:

## Hipotesis

## Diseno
- Grupo control:
- Grupo tratamiento:
- Muestra:
- Duracion:

## Sello

> Sección obligatoria. Declara qué componentes este experimento mantiene constantes y **cómo** se sostiene cada uno. Es la mitad mecanizable del Principio V (`CONSTITUTION.md`): no observa el orden entre pensar y ver, pero sí que el objeto sellado siga siendo el mismo objeto. Origen y evidencia: `historial/sdd.md`, «El sello del experimento pasa a resolverse por escalones».

Por cada componente sellado MUST resolverse, **en este orden**:

1. **Eliminarlo como variable.** ¿Puede construirse la corrida de modo que el desvío sea imposible, no sólo improbable? Si sí, se hace acá y no queda nada que vigilar después.
2. **Verificarlo en corrida.** Lo que no se pudo eliminar MUST tener un verificador que lo comprueba en cada rep y detiene ante divergencia.
3. **Declararlo sin verificador.** Lo que no admite ninguna de las dos MUST quedar escrito como límite del experimento, con su motivo. No es un cajón de derrota: es la diferencia entre un límite conocido y una sorpresa.

El orden no es decorativo. Un desvío eliminado por construcción no puede ocurrir; uno vigilado ocurre y se detecta **después** de ocurrido, que en una tanda ya corrida puede significar re-correrla entera.

| componente | qué queda sellado (valor o identificador) | escalón | mecanismo | qué hace el verificador si diverge |
|---|---|---|---|---|
| tratamiento | | | | |
| entorno de ejecución | | | | |
| fixture / workspace | | | | |

Qué entra en la tabla: lo que este documento declara sellado explícitamente, ni más ni menos. Enumerar de más convierte el verificador en fuente de falsos bloqueos; enumerar de menos deja el hueco donde estaba.

**Tratamiento que es material versionado de un repositorio**: el sello MUST identificarlo **por commit, no por ruta**, y la corrida MUST entregarlo extrayéndolo de ese commit, no copiándolo del árbol de trabajo. No congela nada — el repositorio sigue trabajando y la pasada sigue entregando lo sellado. Una pasada que necesite un tratamiento distinto es una **pasada distinta**, con su enmienda fechada. Residuo de otra clase, que ningún verificador arregla y MUST declararse aparte: si el artefacto evoluciona durante una pasada larga, el resultado describe una versión que ya no es la vigente — eso es vigencia externa, no atribución.

**La prevención no vuelve prescindible el verificador; le cambia el rol.** Un mecanismo de eliminación es en sí mismo algo sellado: una variable de entorno que una versión nueva deja de respetar, un tag que se movió, una extracción que falló en silencio. Sin comprobación no se distingue «funcionó» de «dejó de funcionar sin avisar». Donde el escalón 1 alcanza, el escalón 2 sobrevive como heartbeat barato.

**El verificador MUST detener y explicitar; MUST NOT elegir.** Abortar es lo correcto para un rep suelto. Para una tanda a mitad de camino, la decisión —re-correr la pasada, o contarla con la confusión declarada— es de diseño y no la toma un script.

## Metricas
- Primaria:
- Secundarias:

## Documentos que esperan este resultado

> Quién afirma **hoy** algo que este experimento puede volver falso. Se declara al abrir, cuando pensarlo todavía es barato; el check 3 de «Propagacion» en `RESULTADO-EXPERIMENTO.md` lo verifica al cerrar y captura además lo escrito después.

| documento | que afirma hoy | que lo cambiaria |
|---|---|---|

SHOULD — cada documento listado debe declarar la espera en su propio `Deuda arrastrada`, nombrando el ID de este experimento. Es lo que lo vuelve recuperable por grep al cerrar, aunque esta tabla quede desactualizada.

## Definicion operacional

> Sección obligatoria. Origen: `experimentos/b07-formato-hibrido/RESULTADO-EXPERIMENTO-B7.md`, Hallazgo 7 — B-07 fijó *qué* medir pero no *cómo*, y acumuló ocho enmiendas post-hoc al runbook. Toda decisión que quede acá sin responder se decidirá **después de ver los datos**, que es cuando ya no es neutral.

Por cada métrica declarada arriba, MUST responderse antes de la primera corrida:

- **Denominador**: ¿sobre qué universo se calcula? ¿Es fijo entre grupos o puede variar? Un denominador variable puede **beneficiar** al grupo que produjo menos.
- **Aislamiento de la medición**: ¿en qué entorno se mide y qué garantiza que no arrastra estado del entorno de producción del dato?
- **Validación del instrumento**: ¿qué resultado sobre un control conocido demuestra que el instrumento discrimina? MUST correrse **antes** de puntuar.
- **Granularidad de reporte**: ¿en qué unidad se reporta y coincide con la unidad de la métrica? Si no coincide, ¿quién construye el puente, con qué insumos y en qué momento?
- **Admisibilidad de reconciliaciones**: si al medir aparece un desajuste de nomenclatura o forma, ¿bajo qué criterio MAY repararse para seguir midiendo, y qué MUST NOT repararse nunca? Si se reconcilia, MUST reportarse la variante cruda **y** la reconciliada, con el criterio primario sobre la cruda.
- **Regla de agregación**: si hay más de una celda o grupo, ¿el veredicto se emite por celda o agregado? MUST justificarse; agregar unidades no comparables invalida la lectura.
- **Tratamiento del empate**: un empate MUST declararse **no concluyente**, no como refutación de la hipótesis.
- **Independencia entre métricas**: ¿alguna métrica está determinada por otra? Una métrica derivada MUST NOT computarse como evidencia adicional — duplicaría la primaria.
- **Quién mide**: ¿el rol que puntúa tiene acceso a información que podría sesgarlo? Si el diseño es ciego, ¿qué ve exactamente y qué no?

## Criterio de exito

> MUST enunciarse **sólo** contra las métricas que esta prueba produce. B-07 terminó con un criterio **no evaluable** por mezclar secundarias de un experimento más amplio con las de la prueba efectivamente ejecutada.

- Condición:
- Métricas que la componen (MUST estar todas en «Metricas» de arriba):
- Comprobación de satisfacibilidad: ¿existe algún resultado posible del diseño que cumpla la condición? Si no, el criterio MUST reformularse antes de correr.

## Riesgos

## Plan de captura de datos

## Referencias
