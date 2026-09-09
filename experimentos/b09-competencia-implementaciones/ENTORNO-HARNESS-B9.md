# Entorno de harness de B-09

> Que puede hacer cada harness, verificado. Las reglas del experimento viven en
> [`EXPERIMENTO-B9-competencia-implementaciones.md`](EXPERIMENTO-B9-competencia-implementaciones.md);
> aca solo esta como se ejerce el harness y con que evidencia.

**Documento vivo:** se actualiza hasta el sello inicial de B-09; desde el sello queda
congelado y pasa a ser testigo de lo que se sello. Toda afirmacion de este documento MUST
declarar su procedencia — ver la seccion siguiente.

## Como leer la procedencia

Cada afirmacion lleva una de estas cuatro marcas. La distincion no es prolijidad: una
lectura por omision presentada como verificada es por donde se cuela una premisa falsa al
sello.

| marca | significa |
|---|---|
| **[bin]** | leido de la ayuda del binario instalado, con fecha. Es lo mas fuerte que hay aca |
| **[doc]** | documentacion oficial vigente a la fecha indicada, con URL |
| **[inf]** | inferido, tipicamente por omision en la documentacion. **No es verificado** y MUST confirmarse empiricamente en Fase 0.A antes de que algo dependa de ello |
| **[contra]** | las fuentes oficiales se contradicen. Se registran todas y no se elige por preferencia |

## Claude Code

### Aislamiento entre reps

- **[doc]** `CLAUDE_CONFIG_DIR` relocaliza **settings, historial de sesiones y plugins**.
  En Windows, `~/.claude` es `%USERPROFILE%\.claude`.
  (2026-09-09, https://code.claude.com/docs/en/settings)
- **[inf]** Esa lista **no menciona las credenciales**, que segun la misma documentacion
  viven en el almacen de credenciales del sistema. De ahi se seguiria que un directorio de
  configuracion fresco por rep aisla configuracion y plugins **sin** cortar la
  autenticacion — que es exactamente lo que el diseño pide: que la credencial sea lo unico
  que cruza el aislamiento. **Es lectura por omision y MUST verificarse corriendo** antes
  de que el aislamiento dependa de ella.
- **Consecuencia practica, si se confirma**: no haria falta un `HOME` temporal para aislar
  Claude Code; alcanzaria con `CLAUDE_CONFIG_DIR` apuntando a un directorio nuevo por rep.

### Autenticacion

**Elegida: `claude setup-token`** — token de larga duracion contra la suscripcion. Motivo:
las otras dos vias facturan por API, y 30 corridas por harness vuelven eso una decision de
costo y no de plomeria.

- **[bin]** `claude setup-token` — «Set up a long-lived authentication token (requires
  Claude subscription)». (2026-09-09, `claude --help`)
- **[doc]** `ANTHROPIC_API_KEY` — se envia como cabecera `X-Api-Key`; **cuando esta puesta
  se usa en lugar de la suscripcion aunque haya sesion iniciada**. (2026-09-09,
  https://code.claude.com/docs/en/env-vars)
- **[bin]** `apiKeyHelper`, cargable via `--settings`. (2026-09-09, `claude --help`)
- **[bin]** `claude auth login | logout | status` gestiona la sesion interactiva.

### Opciones verificadas, y para que sirven aca

Todas **[bin]**, 2026-09-09, `claude --help`.

| opcion | que hace | para que la queremos |
|---|---|---|
| `-p`, `--print` | salida no interactiva | modo de corrida |
| `--setting-sources <user,project,local>` | elige que fuentes de settings se cargan | segundo cerrojo sobre lo heredado |
| `--plugin-dir <path>` | carga un plugin desde un directorio o `.zip` **solo para esa sesion** | como entra T4; ver mas abajo |
| `--plugin-url <url>` | idem desde un `.zip` remoto | alternativa a la anterior |
| `--settings <file-or-json>` | settings explicitos | inyectar `apiKeyHelper` o permisos |
| `--strict-mcp-config` | ignora toda configuracion MCP que no venga de `--mcp-config` | cerrar una via de fuga mas |
| `--permission-prompts none` | nadie contesta: lo que pediria permiso se deniega solo | a decidir contra el regimen de permisos heredado de A-04 |
| `--tools <lista>` | acota el conjunto de herramientas disponibles | no previsto; anotado por completitud |

### La trampa de `--bare`, y por que NO se usa

**[bin]** `--bare` es «modo minimo: saltea hooks, LSP, sincronizacion de plugins,
atribucion, auto-memoria, prefetches, lecturas de keychain y descubrimiento de
`CLAUDE.md`», y ademas fuerza autenticacion estricta por `ANTHROPIC_API_KEY` o
`apiKeyHelper`.

Parece el regimen ideal de aislamiento y **no sirve**: saltear hooks y sincronizacion de
plugins desactiva el mecanismo por el que T4 se activa. Usarlo para los cinco brazos
mutila a T4; usarlo solo para algunos rompe la igualdad de condiciones entre brazos, que
es lo que hace comparables las celdas. Lo mismo vale para **[bin]** `--safe-mode`, que
desactiva todas las personalizaciones —plugins, hooks y skills incluidos— aunque conserve
auth y permisos normales.

**Regimen adoptado**: directorio de configuracion fresco por rep mas `--setting-sources`
acotado, **igual para los cinco brazos**, sin `--bare` ni `--safe-mode`.

### Como entra T4

**Por `--plugin-dir`, desde un directorio local, y es una desviacion declarada.**

Lo que compra, de una vez: el plugin no queda instalado en el estado del usuario —carga
solo para esa sesion—, el directorio es hasheable, y se evita el canal de distribucion que
no ofrece pin de version.

Lo que cuesta: el autor de Superpowers documenta la instalacion por marketplace del
harness [R37], asi que esta via **no es el canal oficial**. El artefacto es el mismo y lo
que cambia es por donde entra, pero la desviacion MUST acompañar cualquier lectura de un
resultado de T4, y no como nota al pie.

## Antigravity (`agy`)

### Autenticacion — sin via no interactiva confirmada

**[contra]** Tres fuentes oficiales dicen cosas distintas, a 2026-09-09:

| fuente | dice |
|---|---|
| Instalacion y auth (https://www.agy.dev/docs/cli/install) | admite clave de API por variable de entorno para uso headless/CI, con el proveedor de modelo configurado en `~/.gemini/antigravity-cli/settings.json` |
| Modo headless (https://www.agy.dev/docs/cli/headless) | «usa tus credenciales cacheadas; autenticate primero con una sesion interactiva». Sin autenticacion previa, una corrida no interactiva **sale con error** en vez de colgarse |
| Issue #632 del repositorio de `agy`, **abierto** (https://github.com/google-antigravity/antigravity-cli/issues/632) | las variables de entorno **son ignoradas**; exige almacen de credenciales del sistema u OAuth por navegador. Asignado, sin fecha de resolucion |

**Decision tomada**: `agy` se mantiene como segundo harness. Se autentica **una vez de
forma interactiva** y los reps corren contra el almacen de credenciales del sistema. Eso
satisface el criterio de que la credencial sea lo unico que cruza el aislamiento —ese
almacen no lleva configuracion ni plugins—, pero deja la bateria dependiendo de un estado
de maquina que no se sella, y **eso MUST declararse junto a cualquier resultado de ese
harness**.

**Descartada, y no por comodidad**: autenticar por clave de API de Gemini cambiaria el
backend de modelo. Como harness y familia de modelo ya son inseparables por diseño, esa
via cambiaria **cual es** la familia de modelo de esa bateria, que es una variable del
experimento y no un detalle de acceso.

### Modo no interactivo

- **[doc]** `-p` / `--print` / `--prompt` envia un prompt unico y termina; `--output-format`
  (`text`, `json`, `stream-json`), `--input-format`, `--model`, `--effort`, `--agent`.
  (2026-09-09, https://www.agy.dev/docs/cli/headless)

### Aislamiento

- **[doc]** La configuracion vive en `~/.gemini/antigravity-cli/settings.json`, asi que
  responde a `HOME`. (2026-09-09, https://www.agy.dev/docs/cli/install)
- **[inf]** Donde guarda los plugins **no esta documentado**, y no se conoce variable que
  reubique ese directorio. MUST verificarse empiricamente en Fase 0.A: sin eso no se puede
  afirmar que el estado de T4 muere con el rep en este harness.

## Pendientes de verificacion empirica en Fase 0.A

Ninguno se cierra leyendo documentacion, y el sello MUST NOT apoyarse en ellos hasta que
se cierren.

- [ ] que un directorio de configuracion fresco por rep **no** rompe la autenticacion en
      Claude Code — la lectura por omision de arriba
- [ ] que con ese aislamiento un plugin cargado por `--plugin-dir` **no** sobrevive al rep
- [ ] que el inventario de entorno de un rep de `C0` sale efectivamente vacio
- [ ] donde guarda `agy` sus plugins, y si su estado muere con el rep
- [ ] si `agy` autenticado una vez sostiene corridas no interactivas sucesivas sin
      reautenticar
- [ ] que ningun artefacto conservado —transcript, workspace, bitacora— contiene la
      credencial
