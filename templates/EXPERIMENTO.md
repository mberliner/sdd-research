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

## Metricas
- Primaria:
- Secundarias:

## Documentos que esperan este resultado

> Quién afirma **hoy** algo que este experimento puede volver falso. Se declara al abrir, cuando pensarlo todavía es barato; el check 3 de «Propagacion» en `RESULTADO-EXPERIMENTO.md` lo verifica al cerrar y captura además lo escrito después.

| documento | que afirma hoy | que lo cambiaria |
|---|---|---|

SHOULD — cada documento listado debe declarar la espera en su propio `Deuda arrastrada`, nombrando el ID de este experimento. Es lo que lo vuelve recuperable por grep al cerrar, aunque esta tabla quede desactualizada.

## Definicion operacional

> Sección obligatoria. Origen: `experimentos/RESULTADO-EXPERIMENTO-B7.md`, Hallazgo 7 — B-07 fijó *qué* medir pero no *cómo*, y acumuló ocho enmiendas post-hoc al runbook. Toda decisión que quede acá sin responder se decidirá **después de ver los datos**, que es cuando ya no es neutral.

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
