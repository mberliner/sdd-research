# Template de Resultado de Experimento

## Metadata
- ID experimento:
- Fecha cierre:
- Responsable:

## Resultado cuantitativo
- Metrica primaria (baseline -> resultado):
- Metricas secundarias:

## Resultado cualitativo
- Hallazgos:
- Incidentes:

## Decision
- Adoptar | Ajustar | Descartar

## Cambios al marco SDD

## Propagacion

> Sección obligatoria. Origen: al cerrar B-07 (2026-07-28) el `[SDD-Check]` listó tres derivados y los tres se sincronizaron, pero la lista se había armado **de memoria**: cubrió lo cercano y omitió cuatro documentos lejanos —entre ellos un SSOT— que siguieron afirmando "sin evidencia". Cerrar un experimento produce conocimiento nuevo sin modificar ningún SSOT, así que la regla de propagación no se dispara sola.

MUST — antes de dar el experimento por cerrado, correr los **tres** checks. Ninguno basta solo: cada uno cubre el punto ciego de los otros (verificado contra el cierre de B-07, donde el check 3 aislado sólo encuentra la mitad).

**1. El registro central** — exacto, un archivo:

```bash
grep -n "<ID>" SPECS_REGISTRY.md
```

Las clausulas `incluye`/`excluye` suelen justificarse con el estado del experimento ("aun no ejecutado"). El registro es precedencia 2 —bajo `CONSTITUTION.md`— y gobierna el alcance de cada documento: si queda vencida, contradice a todo lo demás.

**2. El SSOT dueño de la hipótesis, y sus derivados** — estructural, sin grep:

Identificar en el diseño del experimento qué SSOT enuncia la hipótesis, y en la tabla SSOT de `SPECS_REGISTRY.md` quién lo referencia. MUST sincronizarse el SSOT **antes** que sus derivados. Este check es el único que ve a los documentos que afirman el estado **sin haberlo declarado como deuda** — que es como `software/LINEAS-INVESTIGACION.md` quedó atrás de su propio derivado al cerrar B-07.

**3. Quien declaró estar esperando** — grep, captura lo lejano:

```bash
grep -rl "Deuda arrastrada.*<ID>" --include="*.md" . | grep -v '^./experimentos/'
```

Funciona porque la convención anti-cascada (B-06) obliga a cada entrega a re-explicitar su deuda: quien esperaba, lo dijo, y lo dijo de forma grep-able. Encuentra documentos que ningún índice conecta con el experimento. Puede traer falsos positivos —el patrón matchea cualquier línea que contenga ambas cosas—: se registran igual en la tabla y se descartan con su justificación.

MUST — de cada archivo devuelto por el check 3, leer **sólo el último** bloque `[SDD-Check]`: los anteriores son registro datado y MUST NOT reescribirse (la deuda se re-explicita hacia adelante, no se corrige hacia atrás). El cierre de la deuda se anota agregando un bloque nuevo.

MUST — volcar el triaje acá, una fila por documento que aparezca en **cualquiera** de los tres checks:

| documento | que afirmaba | estado nuevo | hecho |
|---|---|---|---|

MUST — cada fila termina en sincronizado, o en la justificación de por qué no aplica.
MUST — si algún documento de la lista es SSOT, sincronizarlo **antes** que sus derivados; el conocimiento de un experimento entra por abajo y sube.
SHOULD — contrastar el resultado del check 3 contra la sección «Documentos que esperan este resultado» del pre-registro. Divergencia en cualquier dirección es señal, no error: el grep captura lo escrito después de abrir el experimento; la declaración captura lo que nunca llegó a anotar su deuda.

## Evidencia adjunta

## Deuda arrastrada
<!-- Pendientes diferidos al cerrar. MUST re-explicitarse en el siguiente cierre hasta resolverse (anti-cascada). Marcar cada item como nuevo | arrastrado | resuelto. -->
-

> MUST — todo ítem que quede `nuevo` o `arrastrado` migra a `../agenda/BACKLOG-INVESTIGACION.md`, con fecha y origen, **antes** de dar el experimento por cerrado.
>
> Motivo: "re-explicitarse en el siguiente cierre" ata la deuda a que exista otro experimento. Si no lo hay, muere en silencio — que es exactamente el abandono que la convención anti-cascada quiere evitar. El backlog tiene cadencia propia. Precedente: B-07 ya lo hizo con dos hallazgos, hoy #4 y #5 de Prioridad alta.

## Proximos pasos
