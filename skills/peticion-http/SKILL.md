---
name: peticion-http
description: Estandariza peticiones HTTP salientes usando github.com/udistrital/utils_oas. Usar cuando se necesite refactorizar, implementar o revisar integraciones HTTP salientes en APIs Go para evitar net/http directo, clientes paralelos, wrappers redundantes y helpers locales de serialización.
---
# Skill: `peticion-http`

Estandarizar peticiones HTTP salientes con `utils_oas`.

## Objetivo

Toda petición HTTP saliente de una API Go debe pasar por `github.com/udistrital/utils_oas`. Este es un lineamiento de arquitectura, no una recomendación opcional.

Aplica a refactorizaciones, APIs nuevas y revisiones repo-wide. Salvo que el usuario limite explícitamente el alcance, revisar todo el repositorio.

Si el usuario menciona un flujo, módulo o archivo puntual pero no dice explícitamente que solo quiere ese alcance, eso no reduce el alcance por defecto: el agente debe asumir revisión repo-wide, usar ese flujo como punto de entrada y después verificar el resto del repositorio.

La migración a `utils_oas` debe forzarse para todos los casos cubiertos por la librería, pero sin romper funcionalidad. Si un caso no puede pasar por `utils_oas`, documentarlo como brecha para corregir en `utils_oas`; no normalizar una solución HTTP paralela permanente.

La preferencia arquitectónica por defecto es: todo por `utils_oas` y, dentro de `utils_oas`, primero `request.*WithContext` cuando preserve el comportamiento.

Si ya existe confirmación explícita del usuario, del equipo o de evidencia previa confiable de que el tag objetivo `v0.5.0-beta.2` sí contiene `GetWithContext`, `PostWithContext`, `PutWithContext`, `PatchWithContext` y `DeleteWithContext`, el agente no puede seguir actuando como si esos símbolos fueran dudosos o ausentes.

Si el usuario corrige la versión objetivo de `utils_oas`, esa corrección prevalece inmediatamente sobre cualquier supuesto previo del agente. No es válido seguir operando, justificando verificaciones o reportando bloqueos sobre `beta.1` cuando el contexto vigente ya fija `v0.5.0-beta.2`.

## Reglas Obligatorias

* Toda petición HTTP saliente debe pasar por `utils_oas`; no se permite transporte HTTP paralelo.
* La migración a `utils_oas` es obligatoria para todos los casos cubiertos por la librería.
* El proyecto debe usar Go `1.25+` y `github.com/udistrital/utils_oas@v0.5.0-beta.2`.
* Ejecutar `go get github.com/udistrital/utils_oas@v0.5.0-beta.2` y `go mod tidy`.
* Escoger explícitamente entre `request` y `requestresponse` según contrato funcional.
* Cruzar el verbo HTTP real con la función equivalente de `utils_oas`.
* Verificar la existencia real de la función `*WithContext` correspondiente en `utils_oas@v0.5.0-beta.2` antes de aceptar cualquier excepción por falta de cobertura.
* Si ya está confirmado que `v0.5.0-beta.2` contiene las funciones `*WithContext`, no aceptar como salida final ningún `request.SendJson`, `request.SendJson2`, `request.GetJson`, `request.GetJsonTest2` o `request.GetJsonWSO2Test` en casos cubiertos.
* Preservar contrato antes/después: endpoint, payload, headers, `Authorization`, timeout, respuesta, destino y errores.
* Propagar `context.Context` cuando la función elegida lo soporte.
* Modificar firmas y call sites para propagar `context.Context` hasta la integración saliente cuando el caso esté cubierto por `request.*WithContext`.
* No usar `net/http`, helpers locales, wrappers tipo `sendjson` ni `requestmanager` como cliente saliente.
* Si `utils_oas` no cubre un caso, documentarlo como brecha para corregir en `utils_oas`.
* No dar por terminada la migración solo porque un helper local ahora delega en `utils_oas`.
* No dejar wrappers locales genéricos o compatibilidades temporales como estado final si `utils_oas` ya cubre el caso.
* Migrar los call sites reales del repositorio, no solo un helper compartido.
* No es válido dejar `helpers/utilidades.go` o archivos equivalentes como puente hacia `utils_oas` para resolver después los call sites.
* Si `helpers/utilidades.go` o un archivo equivalente contiene funciones como `sendJson`, `sendJson3`, `getJson`, `GetJsonTest`, `GetJsonWSO2Test` o variantes que solo envuelven `request.*WithContext`, el agente debe migrar los call sites y eliminar esas funciones; reescribirlas para delegar en `utils_oas` sigue siendo incumplimiento.
* La presencia final de wrappers HTTP genéricos en `helpers/utilidades.go` o equivalentes invalida el cierre como `Estado: completo`, incluso si internamente llaman a `utils_oas`.
* No se acepta cerrar la migración con `request.GetWithContext(context.Background(), ...)` en código productivo; el `ctx` debe ser el de la petición entrante o uno derivado de ese contexto.
* El agente no puede crear `GOMODCACHE`, `GOCACHE`, `GOTMPDIR`, `TMPDIR` ni directorios temporales equivalentes dentro del workspace o del repositorio para validar, compilar o descargar dependencias.
* No se acepta usar `.gomodcache`, `.gocache`, `tmp-go-build`, `tmp`, `cache` o artefactos equivalentes dentro del repositorio como solución operativa temporal.
* Si el entorno impide usar una ruta temporal externa al workspace y la única alternativa sería ensuciar el repo con caches o temporales, el agente debe detener ese intento y reportar bloqueo de infraestructura en lugar de crear esos artefactos.

### Versión y toolchain

* El proyecto debe quedar en Go `1.25` o superior.
* Usar exactamente `github.com/udistrital/utils_oas@v0.5.0-beta.2`.
* No usar `@latest` ni otra versión salvo incompatibilidad documentada.
* No confiar en ninguna copia previa de `utils_oas` ya descargada o cacheada localmente.
* No usar `replace github.com/udistrital/utils_oas => ...` hacia rutas locales, forks locales o checkouts manuales.
* No tomar `vendor/github.com/udistrital/utils_oas` como fuente de verdad para validar versión o símbolos.
* Ejecutar:

```bash
go get github.com/udistrital/utils_oas@v0.5.0-beta.2
go mod tidy
```

Actualizar `go.mod`, directivas `toolchain`, Dockerfile, CI/CD o scripts si fijan una versión inferior.

### Verificación y refresh de la dependencia

Antes de afirmar que una función `*WithContext` no existe o no está disponible en `github.com/udistrital/utils_oas@v0.5.0-beta.2`, el agente debe verificar la dependencia realmente resuelta contra la copia remota.

La fuente de verdad es siempre el tag remoto `v0.5.0-beta.2`. El `GOMODCACHE` local no se puede asumir correcto por defecto. El contenido cacheado puede discrepar del tag remoto.

Por defecto, cualquier copia previa de `utils_oas` en `GOMODCACHE` debe tratarse como no confiable. No basta con que `go list -m` reporte `v0.5.0-beta.2`; el agente debe intentar eliminar toda copia previa y rehidratar desde el tag objetivo antes de aceptar que la verificación quedó cerrada.

Para minimizar contaminación del estado local, la verificación debe preferir un `GOMODCACHE` temporal aislado en `/tmp` o ruta efímera equivalente. El objetivo es que la inspección de `utils_oas` no dependa del cache histórico de la máquina.

#### Flujo preferido: cache temporal aislado

Siempre que el entorno lo permita, verificar `utils_oas` con un cache nuevo y efímero:

```bash
# Paso 0: crear cache temporal aislado
export GOMODCACHE="$(mktemp -d /tmp/utils-oas-modcache.XXXXXX)"

# Paso 1: descargar explícitamente la versión remota en el cache temporal
GOMODCACHE="$GOMODCACHE" go get github.com/udistrital/utils_oas@v0.5.0-beta.2

# Paso 2: aplicar cambios al módulo del proyecto
GOMODCACHE="$GOMODCACHE" go mod tidy

# Paso 3: verificar versión resuelta en el cache temporal
GOMODCACHE="$GOMODCACHE" go list -m github.com/udistrital/utils_oas
GOMODCACHE="$GOMODCACHE" go list -m -json github.com/udistrital/utils_oas

# Paso 4: verificar símbolos en el cache temporal
rg -n "func (GetWithContext|PostWithContext|PutWithContext|PatchWithContext|DeleteWithContext)" "$GOMODCACHE"/github.com/udistrital/utils_oas*
```

Este flujo es preferible al uso del `GOMODCACHE` global porque evita que sobreviva cualquier estado local previo para esta verificación.

#### Validación remota explícita (si descarga local falla)

Si no se puede descargar el módulo localmente (bloqueo de proxy, permisos, etc.), confirmar el tag remoto directamente desde GitHub:

```bash
# Verificar símbolos en el tag remoto v0.5.0-beta.2
curl -s https://raw.githubusercontent.com/udistrital/utils_oas/v0.5.0-beta.2/request/request.go | grep -E "func (GetWithContext|PostWithContext|PutWithContext|PatchWithContext|DeleteWithContext)"
```

Si aparecen las funciones en la salida, el tag remoto las contiene. Un fallo local indica problema de entorno/caché, no ausencia en el tag.

#### Flujo estándar: limpiar, descargar y verificar

Si no es viable usar un cache temporal aislado, el agente **debe ejecutar en primer lugar** una limpieza exhaustiva del cache local y luego traer la copia remota verificada:

```bash
# Paso 1: Borrar cualquier copia local de utils-oas del cache
go clean -modcache

# Paso 2: Descargar explícitamente la versión remota
go get github.com/udistrital/utils_oas@v0.5.0-beta.2

# Paso 3: Aplicar cambios a go.mod
go mod tidy
```

Después de este flujo, el `GOMODCACHE` local debe quedar reconstruido desde cero con la versión remota `v0.5.0-beta.2`, sin residuo operativo de descargas anteriores ni caché obsoleto para esa librería.

Este flujo no es opcional cuando el entorno permite escritura y salida de red y no fue posible usar cache temporal aislado. Si el agente no lo ejecuta, no puede afirmar que verificó fielmente el contenido del tag.

#### Flujo alternativo en entornos restringidos (cache de solo lectura)

Si el entorno no permite escribir en `GOMODCACHE` (permisos de solo lectura, proxy bloqueado, etc.), ejecutar en su lugar:

```bash
# Forzar proxy directo y omitir sumas de seguridad para este módulo
export GOPROXY=direct
export GONOSUMDB=github.com/udistrital/utils_oas

# Verificar versión resuelta actualmente
go list -m github.com/udistrital/utils_oas
go list -m -json github.com/udistrital/utils_oas
```

La versión reportada **debe ser exactamente** `v0.5.0-beta.2`. Si es anterior (p. ej. `v0.5.0-alpha.x`, `v0.4.x`) o posterior, la resolución local está desalineada.

Además, la salida JSON no debe contener `Replace` apuntando a una ruta local ni evidencias de resolución desde un checkout manual o desde `vendor/`. Si aparece `Replace`, la garantía de usar la versión remota queda invalidada.

Este flujo alternativo no equivale a la misma garantía del flujo estándar. Solo permite continuar de forma restringida y reportando `Estado: incompleto` mientras no se pueda demostrar que el cache fue limpiado y reconstruido desde el tag remoto.

#### Verificación de símbolos

Con la copia ya descargada en el cache temporal aislado o, en su defecto, en el cache reconstruido, verificar que las funciones `*WithContext` existan realmente:

```bash
# Ubicación del cache usado para verificar
echo "$GOMODCACHE"

# Buscar símbolos
rg -n "func (GetWithContext|PostWithContext|PutWithContext|PatchWithContext|DeleteWithContext)" "$GOMODCACHE"/github.com/udistrital/utils_oas*
```

Los símbolos `GetWithContext`, `PostWithContext`, `PutWithContext`, `PatchWithContext` y `DeleteWithContext` **deben aparecer** en la salida. Si no aparecen:

* El cache contiene una versión antigua sin esos símbolos, o
* La descarga no se completó, o
* El tag remoto `v0.5.0-beta.2` no contiene esos símbolos (brecha remota).

#### Condiciones para proceder con confianza

* Se verificó primero usando un `GOMODCACHE` temporal aislado o, si no fue viable, se ejecutó `go clean -modcache` antes de descargar de nuevo la dependencia.
* Se ejecutó `go get github.com/udistrital/utils_oas@v0.5.0-beta.2` sobre el cache usado para verificar.
* La versión mostrada por `go list -m github.com/udistrital/utils_oas` en el cache usado para verificar es **exactamente** `v0.5.0-beta.2`.
* La salida de `go list -m -json github.com/udistrital/utils_oas` no contiene `Replace` hacia rutas locales ni resolución fuera del cache usado para verificar.
* Los cinco símbolos `*WithContext` están presentes en el cache usado para verificar.
* `go build ./...` completa sin errores (o puede ejecutarse al menos sobre los archivos refactorizados).

#### Manejo de bloqueos ambientales

Si después de intentar limpieza + descarga el entorno sigue bloqueado:

* No se pudo crear o usar `GOMODCACHE` temporal en `/tmp`: reportar bloqueo de filesystem o sandbox; continuar solo con evidencia secundaria y sin cerrar como completo,
* Cache de módulos de solo lectura: reportar al administrador del entorno; proceder solo si `go list -m` reporta `v0.5.0-beta.2` y los símbolos están presentes, pero el trabajo no puede cerrarse como completo,
* Proxy bloqueado o sin salida: reportar como bloqueo de red; proceder solo si la versión y símbolos están en cache existente, pero el trabajo no puede cerrarse como completo,
* Ambos bloques persisten: no cerrar la migración hasta que se resuelva; registrar como dependencia de infraestructura.

No se acepta una excepción por "falta de cobertura" sin haber verificado que `go list -m` reporte `v0.5.0-beta.2` y que los cinco símbolos `*WithContext` existan en el `GOMODCACHE` local.

Tampoco se acepta como verificación suficiente decir que “ya estaba descargada la versión correcta” o que “el cache parecía actualizado”. La verificación válida exige limpieza previa y redescarga, salvo bloqueo ambiental documentado.

Tampoco se acepta como garantía que el proyecto compile contra una copia local “equivalente”, un `replace` temporal o una copia en `vendor/`. La garantía válida exige que la resolución efectiva del módulo provenga del tag remoto `v0.5.0-beta.2` descargado al cache usado para verificar.

La opción preferida no es limpiar el cache global sino evitarlo: crear un cache temporal aislado y hacer allí la verificación. Si el agente usa directamente el `GOMODCACHE` histórico sin intentar aislamiento, la verificación queda por debajo del estándar esperado.

En el tag remoto `v0.5.0-beta.2`, el archivo `request/request.go` del repositorio `github.com/udistrital/utils_oas` contiene efectivamente las funciones `GetWithContext`, `PostWithContext`, `PutWithContext`, `PatchWithContext` y `DeleteWithContext`. Por lo tanto, si la verificación local no las encuentra, debe considerarse una inconsistencia del entorno o del cache local, no una falta de cobertura en el tag remoto.

Si aun después de esa verificación el agente concluye que no encuentra `PostWithContext`, `PutWithContext`, `PatchWithContext` o `DeleteWithContext`, debe tratarlo primero como inconsistencia de entorno o de resolución local, no como ausencia real del tag. Mientras esa inconsistencia no se resuelva, no puede cerrar el trabajo ni conservar `SendJson` como solución final.


### Prohibido

No dejar ni introducir transporte HTTP saliente por:

* `http.NewRequest`, `http.Client`, `http.DefaultClient`, `client.Do(...)`
* `http.Get`, `http.Post`, `http.Put`, `http.Delete`
* helpers internos de transporte HTTP
* wrappers tipo `sendjson`, `SendJSON`, `SendJson`, `SendRequest`, `DoRequest`, `CallAPI`
* `requestmanager` como cliente saliente
* imports con alias innecesarios, por ejemplo `utils "github.com/udistrital/utils_oas/..."`

Se permiten capas `service`, `provider`, `repository`, `client` o `adapter` solo si no implementan transporte propio y delegan directamente en `utils_oas`.

No es aceptable cumplir el skill dejando wrappers genéricos locales como `getJson`, `GetJsonTest`, `sendJson`, `sendJson3`, `getXml` o equivalentes si `utils_oas` ya expone la función necesaria. En esos casos el agente debe modificar los call sites del repositorio para llamar a `utils_oas` directamente y luego eliminar el wrapper.

Tampoco es aceptable conservar esos wrappers en `helpers/utilidades.go` reimplementados como pass-through hacia `request.GetWithContext`, `request.PostWithContext`, `request.PutWithContext`, `request.PatchWithContext` o `request.DeleteWithContext`. Si el caso está cubierto, el wrapper debe desaparecer del código productivo.

Tampoco es aceptable presentar eso como “primera fase” o “compatibilidad temporal” si el caso ya está cubierto por `request.*WithContext`.

### Migración obligatoria controlada

Forzar la migración no significa cambiar el contrato funcional. Preservar y comparar antes/después:

* verbo HTTP real
* endpoint, path params y query params
* payload y serialización efectiva
* headers relevantes y `Authorization`
* `context.Context`, cancelación y deadlines cuando aplique
* formato de respuesta esperado
* mapeo a estructura destino
* semántica de errores relevante
* limpieza o transformación posterior, por ejemplo `LimpiezaRespuestaRefactor`

Si falta una capacidad en `utils_oas` para conservar ese contrato, registrar brecha de `utils_oas`.

Prioridad por defecto:

* intentar primero migrar a `request.GetWithContext`, `request.PostWithContext`, `request.PutWithContext`, `request.PatchWithContext` o `request.DeleteWithContext`,
* solo usar otra función de `utils_oas` cuando migrar a `request.*WithContext` rompa un comportamiento real o no cubra el caso,
* si no se usa `request.*WithContext`, documentar explícitamente la razón y la función alternativa elegida.

Esto implica cambiar los archivos consumidores necesarios. No basta con adaptar un helper central y dejar el resto del repositorio llamando funciones locales obsoletas.

Una migración no está completa mientras el repositorio siga dependiendo de wrappers genéricos para llegar a `utils_oas`.

Cuando el caso esté cubierto por `request.*WithContext`, ese debe ser el destino final obligatorio de la migración.

No se permite diferir a una fase posterior la eliminación de wrappers o la migración de call sites cuando el caso ya está cubierto por `request.*WithContext`.

No se permite alegar “falta de cobertura” de `request.*WithContext` sin verificar primero la existencia real de la función correspondiente en `github.com/udistrital/utils_oas@v0.5.0-beta.2`.
### Auditoría repo-wide obligatoria

Antes de cerrar la migración como completa, el agente debe ejecutar una auditoría textual repo-wide para detectar remanentes no migrados:

```bash
# Buscar uso directo de net/http en código productivo
grep -r "net/http" --include="*.go" . | grep -v "import" | grep -v "comment" | grep -v "/tests/" | grep -v "_test.go"

# Buscar wrappers locales obsoletos en código productivo
grep -r "SendJson\|SendJson2\|GetJson\|GetJsonTest\|GetJsonTest2\|GetJsonWSO2Test" --include="*.go" . | grep -v "comment" | grep -v "/tests/" | grep -v "_test.go"

# Buscar context.Background() o context.TODO() en integraciones HTTP
grep -r "context\.Background\|context\.TODO" --include="*.go" . | grep -v "test" | grep -v "main" | grep -v "bootstrap"

# Buscar requestmanager como cliente saliente en código productivo
grep -r "requestmanager\." --include="*.go" . | grep -v "comment" | grep -v "/tests/" | grep -v "_test.go"
```

Si aparecen resultados en estas búsquedas, la migración no está completa. El agente debe:

* Migrar los call sites encontrados a `request.*WithContext` o `requestresponse.*` según corresponda,
* Propagar `context.Context` desde el controller/handler hasta la integración,
* Eliminar wrappers locales si ya no son necesarios,
* Documentar excepciones solo si hay brecha real en `utils_oas`.

Esta auditoría no es opcional salvo que el usuario limite explícitamente el alcance a un archivo o flujo específico.

Los hallazgos en `tests/` o `*_test.go` no invalidan por sí solos el cierre del skill sobre código productivo. Deben clasificarse aparte como seguimiento de tests, y solo vuelven `Estado: incompleto` si rompen compilación, `go test`, o dejan sin validar cambios de firmas necesarios.
## Selección de Capa

`request` y `requestresponse` son capas distintas dentro de `utils_oas`; no son equivalentes.

### Usar `request`

Usar `request` cuando sea la capa que conserva el contrato heredado:

* el consumidor pasa un `target`
* la función decodifica en ese `target`
* el MID conserva patrón `map[string]interface{}` -> `LimpiezaRespuestaRefactor`
* endpoints legacy, WSO2, XML o respuestas no homogéneas
* se necesita menor riesgo funcional al reemplazar helpers antiguos
* el contrato real es compatible con timeout fijo de `30s`, `xray.BeginSegmentSec` y `xray.UpdateSegment`

Patrón heredado típico:

```go
var response map[string]interface{}
err := request.SendJson(url, "POST", &response, body)
LimpiezaRespuestaRefactor(response, &destino)
```

Funciones verificadas en `v0.5.0-beta.2` del paquete `request`:

* `request.GetWithContext(ctx, url, target)`
* `request.PostWithContext(ctx, url, body, target)`
* `request.PutWithContext(ctx, url, body, target)`
* `request.PatchWithContext(ctx, url, body, target)`
* `request.DeleteWithContext(ctx, url, target)`

### Contrato operativo de `request.*WithContext`

Usar estas funciones con su comportamiento real, no por analogía:

* `request.GetWithContext(ctx, url, target)`
  firma: `(context.Context, string, any) (int, error)`. Hace `GET`, envía `Accept: application/json, application/xml, text/xml`, usa `http.Client{Timeout: 30 * time.Second}`, falla en status fuera de `200..226`, decodifica XML si `Content-Type` contiene `xml`, en otro caso decodifica JSON en `target`, y retorna `(status, err)`.
* `request.PostWithContext(ctx, url, body, target)`
  firma: `(context.Context, string, any, any) (int, error)`. Hace `POST`, serializa `body` como JSON si `body != nil`, envía `Content-Type: application/json` y `Accept: application/json`, usa timeout fijo de `30s`, falla en status fuera de `200..226`, decodifica JSON en `target`, y retorna `(status, err)`.
* `request.PutWithContext(ctx, url, body, target)`
  firma: `(context.Context, string, any, any) (int, error)`. Hace `PUT`, serializa `body` como JSON si `body != nil`, envía `Content-Type: application/json` y `Accept: application/json`, usa timeout fijo de `30s`, falla en status fuera de `200..226`, decodifica JSON en `target`, y retorna `(status, err)`.
* `request.PatchWithContext(ctx, url, body, target)`
  firma: `(context.Context, string, any, any) (int, error)`. Hace `PATCH`, serializa `body` como JSON si `body != nil`, envía `Content-Type: application/json` y `Accept: application/json`, usa timeout fijo de `30s`, falla en status fuera de `200..226`, decodifica JSON en `target`, y retorna `(status, err)`.
* `request.DeleteWithContext(ctx, url, target)`
  firma: `(context.Context, string, any) (int, error)`. Hace `DELETE`, envía `Accept: application/json`, usa timeout fijo de `30s`, falla en status fuera de `200..226`, decodifica JSON en `target`, y retorna `(status, err)`.

Errores relevantes del contrato:

* si la librería no puede construir la request, retorna error envuelto;
* si el status no está entre `200` y `226`, retorna `unexpected status code: <status>`;
* si falla la decodificación del body, retorna un error envuelto sobre `request.ErrResponseDecode`;
* `PostWithContext`, `PutWithContext`, `PatchWithContext` y `DeleteWithContext` intentan decodificar JSON siempre que el status sea exitoso; una respuesta `204 No Content` o un body vacío puede romper compatibilidad si el consumidor hoy acepta ese caso sin decode.

### Uso correcto para refactorizar

* usar `target` del tipo que ya espera el código consumidor,
* si el código actual valida `status == 200`, adaptar esa lógica al contrato nuevo: `err == nil` ya implica `2xx`,
* si el flujo actual depende de revisar el status exacto `200/201/...`, usar el `status` retornado por la función nueva,
* si el código actual hacía `map[string]interface{}` + `LimpiezaRespuestaRefactor`, conservar ese patrón usando `target` compatible y luego aplicar la limpieza,
* si el flujo actual depende de `204 No Content`, body vacío o éxito sin payload decodificable, no asumir compatibilidad automática con `PostWithContext`, `PutWithContext`, `PatchWithContext` o `DeleteWithContext`; validar o documentar excepción,
* si el flujo actual dependía de headers custom además de `Accept` o `Content-Type`, no asumir que `request.*WithContext` los conserva,
* si la respuesta no es JSON/XML compatible con estas funciones, documentar excepción real.

### Tabla de reemplazo directa

Usar esta tabla como regla práctica de refactorización:

* `request.GetJsonTest2(url, &target)` -> `request.GetWithContext(ctx, url, &target)`
* `request.GetJson(url, &target)` -> `request.GetWithContext(ctx, url, &target)`
* `request.GetJsonWSO2Test(url, &target)` -> `request.GetWithContext(ctx, url, &target)` solo si el contrato real sigue siendo compatible; si no, excepción documentada
* `request.SendJson(url, "POST", &target, body)` -> `request.PostWithContext(ctx, url, body, &target)`
* `request.SendJson(url, "PUT", &target, body)` -> `request.PutWithContext(ctx, url, body, &target)`
* `request.SendJson(url, "PATCH", &target, body)` -> `request.PatchWithContext(ctx, url, body, &target)`
* `request.SendJson2(url, "POST", &target, body)` -> `request.PostWithContext(ctx, url, body, &target)`

Reglas:

* no migrar por nombre de helper sino por verbo HTTP real,
* si el código actual usa `SendJson` con un verbo distinto, migrar a la variante `*WithContext` del verbo real,
* si no existe variante `*WithContext` compatible con el contrato real, documentar excepción puntual,
* para `DELETE`, reemplazar cualquier helper histórico equivalente por `request.DeleteWithContext(ctx, url, &target)` cuando haya cobertura.

También existen funciones históricas como `request.GetJson`, `request.GetJsonTest2`, `request.GetJsonWSO2Test`, `request.SendJson` y `request.SendJson2`.

Estas funciones históricas no son ruta normal de migración. Deben tratarse solo como excepción documentada. El destino final esperado de migración es `request.*WithContext`.

No deben mantenerse por conveniencia si `request.*WithContext` conserva el comportamiento.

Si el usuario o el equipo ya confirmó que el tag objetivo sí expone `PostWithContext`, `PutWithContext`, `PatchWithContext` y `DeleteWithContext`, `request.SendJson` y `request.SendJson2` quedan prohibidos como estado final salvo incompatibilidad funcional concreta, localizada y demostrada sobre el contrato del endpoint, no sobre un problema de cache o resolución del módulo.

No usar como justificación válida:

* “en este entorno no apareció el símbolo”
* “el autocomplete no lo mostró”
* “compiló con `SendJson` entonces lo dejé así”
* “ya estaba cacheada otra copia de la librería”

Esas situaciones describen un problema de entorno, no una razón técnica para conservar funciones históricas.

### Usar `requestresponse`

Usar `requestresponse` cuando el endpoint tenga respuesta JSON institucional homogénea y el parser esté validado endpoint por endpoint:

* devuelve `interface{}`
* obliga a pasar parser
* valida status HTTP, JSON y estructura esperada
* encaja con formatos tipo `Success`, `Status`, `Message`, `Data`

Ejemplo:

```go
data, err := requestresponse.Post(url, body, requestresponse.ParseResponseFormato1)
```

No migrar a `requestresponse` a ciegas. Validar si aplica `ParseResponseFormato1`, `ParseResponseFormato2` u otro parser; pueden fallar si el shape cambia o si `Status` viene como string vs número.

`requestresponse` también debe tratarse como excepción justificada frente a `request.*WithContext` cuando el parser o la validación institucional sean necesarios para preservar el contrato del consumidor.

No debe usarse `requestresponse` solo para evitar tocar call sites o para conservar wrappers locales existentes.

## Cruce Verbo-Función

La validación no es solo "usa `utils_oas`"; debe cruzar el verbo real con la función equivalente de la capa elegida.

### En `request`

* `GET`: `request.GetWithContext`
* `POST`: `request.PostWithContext`
* `PUT`: `request.PutWithContext`
* `PATCH`: `request.PatchWithContext`
* `DELETE`: `request.DeleteWithContext`

Las funciones históricas `request.GetJson`, `request.GetJsonTest2`, `request.GetJsonWSO2Test`, `request.SendJson` y `request.SendJson2` solo pueden quedar por excepción documentada.

Prohibición nominal en casos cubiertos:

* para `GET`, no dejar `request.GetJson`, `request.GetJsonTest2` ni `request.GetJsonWSO2Test` como estado final si `request.GetWithContext` cubre el caso,
* para `POST`, no dejar `request.SendJson` ni `request.SendJson2` como estado final si `request.PostWithContext` cubre el caso,
* para `PUT`, `PATCH` y `DELETE`, no dejar equivalentes históricos si la variante `*WithContext` cubre el caso.

### En `requestresponse`

* `GET`: `requestresponse.Get`
* `POST`: `requestresponse.Post`
* `PUT`: `requestresponse.Put`
* `DELETE`: `requestresponse.Delete`
* `PATCH`: documentar brecha si se necesita y no existe equivalente en la capa

### Reglas de cruce

* No migrar un `GET` a una función POST.
* No migrar un `POST` o helper `Send*` de escritura a una función GET.
* No decidir por el nombre del helper; inspeccionar el verbo HTTP efectivo.
* Si un helper `Send*` realmente hace POST, cruzarlo con `request.PostWithContext` salvo excepción documentada.
* No migrar `request.SendJson` + `LimpiezaRespuestaRefactor` a `requestresponse.Post` sin validar y preservar el formato exacto de respuesta.
* No dejar funciones históricas o `requestresponse` si `request.*WithContext` preserva el comportamiento.
* No conservar wrappers locales de compatibilidad si ya se puede llamar a `utils_oas` directamente.
* No dejar `request.GetJson`, `request.GetJsonTest2`, `request.GetJsonWSO2Test`, `request.SendJson` o `request.SendJson2` como solución final si existe cobertura con `request.*WithContext`.

## Context y Headers

Desde `v0.5.0-beta.2`, preferir funciones con `context.Context` cuando la capa y el caso lo soporten.

Reglas:

* el `ctx` debe venir de la capa llamadora
* si la ejecución nace de una petición HTTP entrante, el `ctx` debe provenir de esa petición, por ejemplo `c.Ctx.Request.Context()` o el contexto propagado desde controller/handler
* no crear `context.Background()` o `context.TODO()` dentro de integraciones salvo bootstrap o pruebas
* propagar cancelación, deadlines, trazabilidad y metadatos existentes
* modificar firmas de funciones y call sites si hace falta para que el `ctx` llegue hasta `request.*WithContext`
* no degradar a firma antigua sin justificar compatibilidad, `Authorization`, parser, XML, WSO2 o brecha de la capa elegida

Si una función del repositorio realiza o coordina una salida HTTP cubierta por `request.*WithContext`, debe aceptar `context.Context` directa o indirectamente. No usar `context.Background()` como atajo para evitar tocar firmas.

En flujos request/response, no basta con "pasar un contexto"; debe ser el contexto de la petición que llegó al servicio. Si el controller, handler o endpoint ya expone un `ctx`, ese es el que debe atravesar service, helper, repository o provider hasta `request.*WithContext`.

Patrón explícitamente inválido en código productivo:

```go
status, err := request.GetWithContext(context.Background(), url, &target)
```

Si aparece ese patrón fuera de pruebas, bootstrap o un borde ya controlado por un `ctx` superior, la migración no está completa.

Patrón esperado en integraciones nacidas de una petición entrante:

```go
func (s *Service) Operacion(ctx context.Context, ...) error {
    status, err := request.GetWithContext(ctx, url, &target)
    if err != nil {
        return err
    }
    _ = status
    return nil
}
```

En `v0.5.0-beta.2`, `request.*WithContext` no recibe headers explícitos ni permite inyectar un `http.Client` custom. Si la integración depende de `Authorization`, otros headers, transporte custom, timeout distinto de `30s` o comportamiento especial de cliente, usar otra función de `utils_oas` que preserve comportamiento o registrar brecha para corregir en `utils_oas`.

La ausencia de soporte de headers en `request.*WithContext` no autoriza volver a `net/http` ni a helpers locales permanentes.

## Brechas y Excepciones

Una excepción solo es válida si:

1. `utils_oas@v0.5.0-beta.2` no cubre el caso real.
2. La limitación técnica queda documentada.
3. La excepción queda localizada.
4. Se explica por qué no fue posible usar `utils_oas`.
5. El equipo responsable la aprueba.
6. El caso queda registrado como brecha o requerimiento de evolución de `utils_oas`.

No es válida una excepción basada únicamente en:

* cache viejo
* `GOMODCACHE` desalineado
* autocompletado del editor
* imports rotos por resolución local transitoria
* falta de limpieza/redescarga del módulo
* incapacidad del asistente para ubicar símbolos ya confirmados en el tag objetivo

Formato mínimo:

```text
Ubicación:
Caso:
Motivo técnico:
Por qué utils_oas no cubre el caso:
Capacidad faltante en utils_oas:
Impacto:
Alternativa temporal:
Versión evaluada de utils_oas:
Aprobación:
```

Ejemplos de brecha: binarios, `multipart/form-data`, streaming, retries/circuit breaker no soportados, headers requeridos no expuestos, timeout o transporte custom no expuesto, `204 No Content` incompatible con decode obligatorio, `PATCH` en `requestresponse`.

Si una integración no queda en `request.*WithContext`, registrar además:

```text
Se intentó migrar a request.*WithContext: Sí/No
Razón para no usar request.*WithContext:
Función alternativa de utils_oas elegida:
Riesgo de la migración directa:
Acción futura recomendada:
```

Si la función alternativa elegida es histórica, registrar además:

```text
Función histórica remanente:
Por qué request.*WithContext no sirve todavía:
Qué faltaría ajustar para migrar después:
Ubicación exacta de cada uso remanente:
```

Además, si la razón es “la función `*WithContext` no existe” o “no está disponible”, registrar obligatoriamente:

```text
Función WithContext buscada:
Versión verificada de utils_oas:
Archivo o paquete verificado:
Resultado de la verificación:
Comando usado para verificar GOMODCACHE:
```

No se acepta una excepción de cobertura sin esa evidencia.

No es suficiente afirmar “en este entorno no expone esos símbolos”. El agente debe dejar evidencia verificable de la resolución local del módulo y del contenido observado en `GOMODCACHE`.

Si fue necesario refrescar la dependencia, registrar además:

```text
Se ejecutó refresh de modcache: Sí/No
Resultado después del refresh:
¿El GOMODCACHE quedó alineado con v0.5.0-beta.2?: Sí/No
```

Si no fue posible ejecutar limpieza + redescarga, registrar además:

```text
¿Por qué no pudo limpiarse el modcache?:
¿Por qué no pudo redescargarse desde el tag remoto?:
¿Qué evidencia indirecta quedó disponible?:
```

Ese registro es obligatorio por cada uso remanente. No basta con una justificación general del repositorio.

Si además sobrevive un wrapper local temporal, registrar:

```text
Wrapper local remanente:
Motivo por el que no pudo eliminarse aún:
Plan para eliminarlo:
```

Si el caso ya estaba cubierto por `request.*WithContext`, ese wrapper remanente debe tratarse como incumplimiento, no como transición válida.

### Regla de reporte

Si queda aunque sea una excepción abierta, una función histórica remanente, un wrapper temporal, un `ctx` mal propagado o una validación requerida sin ejecutar, el agente no puede presentar el trabajo como “completado”, “refactorizado” o “cerrado”.

Debe reportarlo explícitamente como migración parcial o incompleta y listar:

```text
Estado: incompleto
Bloqueos o excepciones abiertas:
Verificaciones faltantes:
Archivos o usos remanentes:
Siguiente acción concreta:
```

Solo se puede usar lenguaje de cierre completo cuando se cumple todo el `Definition of Done`.

El agente tampoco puede presentar como “cumplido el skill” una migración correcta pero acotada a uno o pocos flujos si no hubo límite de alcance explícito del usuario y todavía no existe verificación repo-wide de remanentes.

## Procedimiento

### 1. Descubrir

Buscar repo-wide:

* `net/http`, `http.NewRequest`, `http.Client`, `client.Do(`, `http.Get(`, `http.Post(`, `http.Put(`, `http.Delete(`
* `Authorization`, `Content-Type`, `Accept`
* `json.NewEncoder(`, `json.NewDecoder(`, `io.ReadAll(`
* `CallAPI`, `DoRequest`, `SendRequest`, `Fetch`, `RestClient`, `NewClient`
* `sendjson(`, `SendJSON(`, `SendJson(`

Revisar archivos `http.go`, `request.go`, `client.go`, `consumer.go`, `provider.go`, `integration.go`, `fetch.go`, además de `go.mod` y `go.sum`.

### 2. Inventariar

Por integración registrar: archivo, función, servicio, endpoint, verbo, payload, response esperado, headers, `Authorization`, implementación actual, capa elegida, función `utils_oas`, riesgo funcional y brecha si existe.

Si existe un helper local intermedio, registrarlo solo como estado transitorio a eliminar, no como destino final de la migración.

### 3. Refactorizar

1. Identificar contrato actual.
2. Actualizar Go y `utils_oas`.
3. Intentar primero migrar a `request.*WithContext`.
4. Verificar explícitamente que la función `*WithContext` correspondiente exista en `v0.5.0-beta.2` inspeccionando la dependencia realmente resuelta.
5. Limpiar `GOMODCACHE` y redescargar explícitamente `utils_oas@v0.5.0-beta.2` salvo bloqueo ambiental documentado.
6. Si hay duda de caché o resolución, repetir limpieza + descarga y volver a verificar.
7. Si el cache local estaba desalineado respecto del tag remoto, forzar la corrección del `GOMODCACHE` hasta que coincida con `v0.5.0-beta.2`.
8. Si no es viable, justificar y elegir otra función de `utils_oas`.
9. Cruzar verbo real con función equivalente.
10. Reemplazar cliente/helper local por llamada directa a `utils_oas` en los call sites necesarios.
11. Modificar firmas y call sites para propagar `ctx` hasta `request.*WithContext` cuando el caso esté cubierto.
12. Preservar contrato funcional.
13. Eliminar wrappers redundantes y compatibilidades temporales que ya no sean necesarias.
14. Validar imports sin alias innecesarios.
15. Confirmar que no se creó ningún cache ni temporal de Go dentro del workspace; si el entorno solo permite esa opción, detenerse y reportar el bloqueo en vez de usarla.

Resultado explícitamente no aceptable:

* concentrar la migración en `helpers/utilidades.go` y dejarlo como punto central de paso hacia `utils_oas`,
* reemplazar GET por `request.GetWithContext(context.Background(), ...)` sin propagar `ctx`,
* dejar `request.SendJson` o `request.SendJson2` en escrituras solo porque "en este entorno" no aparecieron los símbolos nuevos sin adjuntar evidencia del módulo realmente resuelto y, si aplica, del refresh del `GOMODCACHE`.

Patrones mínimos de refactorización:

```go
status, err := request.GetWithContext(ctx, url, &target)
if err != nil {
    // manejar error
}
```

```go
status, err := request.PostWithContext(ctx, url, body, &target)
if err != nil {
    // manejar error
}
```

```go
status, err := request.PutWithContext(ctx, url, body, &target)
if err != nil {
    // manejar error
}
```

```go
status, err := request.PatchWithContext(ctx, url, body, &target)
if err != nil {
    // manejar error
}
```

```go
status, err := request.DeleteWithContext(ctx, url, &target)
if err != nil {
    // manejar error
}
```

Al adaptar código legado:

* no envolver estas llamadas en nuevos helpers genéricos,
* no reemplazar `status == 200` por nada ambiguo; decidir explícitamente si basta `err == nil` o si se necesita revisar el status exacto,
* si antes se usaba `GetJsonTest2` para obtener `(status, err)`, migrar a la misma forma con `GetWithContext`,
* si antes se usaba `SendJson` para POST/PUT/PATCH, migrar a `PostWithContext`, `PutWithContext` o `PatchWithContext` según el verbo real.
* si se actualizan firmas usadas por tests, ajustar los tests necesarios para que el repo siga validando, pero no tratar usos de `net/http` dentro de tests como incumplimiento automático del objetivo productivo.

### 4. Verificar

Comprobar:

* toda salida HTTP usa `utils_oas`
* no queda `net/http` saliente ni helpers redundantes
* cada integración intentó primero `request.*WithContext`
* cada integración cubierta por `request.*WithContext` terminó en `request.*WithContext` o dejó excepción documentada
* cada integración eligió capa y función por verbo real
* contrato antes/después equivalente
* no quedaron wrappers locales genéricos haciendo de pass-through hacia `utils_oas`
* los call sites reales quedaron migrados y no dependen de compatibilidades temporales innecesarias
* no quedaron `request.GetJson`, `request.GetJsonTest2`, `request.GetJsonWSO2Test` o `request.SendJson` en casos cubiertos por `request.*WithContext`
* no quedó código productivo usando `context.Background()` o `context.TODO()` para invocar `request.*WithContext` en lugar de propagar `ctx`
* en flujos iniciados por una petición entrante, `request.*WithContext` recibe el `ctx` de esa petición o uno derivado de él
* toda excepción por falta de cobertura fue verificada contra la versión real `v0.5.0-beta.2`
* no se dejó `SendJson` o `SendJson2` por problemas de cache, IDE, autocompletado o resolución local
* se verificó primero con `GOMODCACHE` temporal aislado o, si no fue viable, con limpieza de `GOMODCACHE` y redescarga de `utils_oas@v0.5.0-beta.2`
* si hubo duda de caché o versión resuelta, se repitió limpieza + descarga y se revalidaron los símbolos
* si el `GOMODCACHE` local estaba desalineado, quedó corregido o quedó bypassed por verificación en cache temporal aislado consistente con `v0.5.0-beta.2`
* brechas documentadas
* Go `1.25+` y `utils_oas@v0.5.0-beta.2`
* no quedó `helpers/utilidades.go` o equivalente funcionando como puente hacia `utils_oas`
* no quedó una “segunda fase” pendiente para migrar call sites ya cubiertos por `request.*WithContext`
* el proyecto compila contra la implementación real resuelta de `utils_oas`
* no se crearon artefactos temporales de Go dentro del workspace para validación; si el entorno obligaba a ello, el agente debió detenerse y reportar el bloqueo sin crear esos artefactos

Además, verificar explícitamente con búsqueda textual repo-wide que no queden usos remanentes indebidos de:

```text
request.GetJson(
request.GetJsonTest2(
request.GetJsonWSO2Test(
request.SendJson(
```

Si alguno permanece, debe quedar asociado a una excepción documentada por uso.

Si permanece cualquier uso histórico o excepción abierta, el reporte final debe decir explícitamente que el trabajo quedó incompleto.

Auditoría mínima obligatoria repo-wide antes de cerrar, salvo alcance explícitamente limitado por el usuario:

```bash
rg -n "request\\.(GetJson|GetJsonTest2|GetJsonWSO2Test|SendJson|SendJson2)\\(" . -g '!**/*_test.go' -g '!tests/**'
rg -n "http\\.(NewRequest|Get|Post|Put|Delete)\\(" . -g '!**/*_test.go' -g '!tests/**'
rg -n "http\\.Client|client\\.Do\\(" . -g '!**/*_test.go' -g '!tests/**'
rg -n "context\\.(Background|TODO)\\(" . -g '!**/*_test.go' -g '!tests/**'
rg -n "(sendjson|SendJSON|SendJson|getXml|GetXml|DoRequest|CallAPI)" . -g '!**/*_test.go' -g '!tests/**'
rg -n "net/http|http\\.(NewRequest|Get|Post|Put|Delete)|http\\.Client|client\\.Do\\(" tests . -g '**/*_test.go'
rg -n "\\.(gomodcache|gocache)$|tmp-go-build|tmp/go-build" .
```

La primera tanda define cumplimiento sobre código productivo. La segunda es inventario de tests y artefactos temporales. Si esta auditoría no se ejecuta, el skill no puede reportarse como cumplido.

Ejecutar, salvo bloqueo documentado:

```bash
go vet ./...
go fmt ./... && git diff --exit-code || (echo "Go fmt detected formatting issues! Please run 'go fmt' to format your code." && exit 1)
go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest
golangci-lint run --out-format=checkstyle --timeout=5m > lint_report.xml || true
cat lint_report.xml
```

## Definition of Done

* [ ] Todas las peticiones HTTP salientes pasan por `utils_oas`.
* [ ] No quedan clientes HTTP directos ni helpers de transporte redundantes.
* [ ] `utils_oas` está en `v0.5.0-beta.2` y el proyecto en Go `1.25+`.
* [ ] No se confió en ninguna copia previa cacheada de `utils_oas` como evidencia suficiente.
* [ ] No existe `replace` local para `github.com/udistrital/utils_oas`.
* [ ] No se usó `vendor/github.com/udistrital/utils_oas` como fuente de verdad de versión o símbolos.
* [ ] Se ejecutó `go mod tidy`.
* [ ] Se intentó primero verificar `utils_oas` en un `GOMODCACHE` temporal aislado.
* [ ] Si no fue viable el cache temporal aislado, se ejecutó `go clean -modcache` antes de redescargar `utils_oas@v0.5.0-beta.2`, salvo bloqueo ambiental documentado.
* [ ] Se redescargó explícitamente `github.com/udistrital/utils_oas@v0.5.0-beta.2` en el cache usado para verificar, salvo bloqueo ambiental documentado.
* [ ] `go list -m -json github.com/udistrital/utils_oas` no muestra `Replace` ni resolución fuera del cache usado para verificar.
* [ ] Cada integración intentó migrar primero a `request.*WithContext`.
* [ ] Cada integración cubierta por `request.*WithContext` quedó migrada a `request.*WithContext` o dejó excepción documentada.
* [ ] Ninguna escritura `POST`/`PUT`/`PATCH` quedó en `request.SendJson` o `request.SendJson2` por problemas de entorno o resolución local.
* [ ] Si alguna integración no quedó en `request.*WithContext`, la razón quedó documentada.
* [ ] Cada integración eligió `request` o `requestresponse` con justificación.
* [ ] Cada integración cruza correctamente verbo real y función `utils_oas`.
* [ ] Se preservó contrato funcional antes/después.
* [ ] `ctx`, headers y `Authorization` se preservaron o la brecha quedó documentada.
* [ ] Las firmas y call sites necesarios fueron modificados para propagar `ctx` hasta la salida HTTP.
* [ ] No se usó `requestmanager` como cliente saliente.
* [ ] No se usaron alias innecesarios.
* [ ] No quedaron wrappers locales genéricos tipo `getJson`, `GetJsonTest`, `sendJson`, `sendJson3`, `getXml` o equivalentes cuando `utils_oas` ya cubre el caso.
* [ ] No quedaron `request.GetJson`, `request.GetJsonTest2`, `request.GetJsonWSO2Test` o `request.SendJson` cuando el caso estaba cubierto por `request.*WithContext`.
* [ ] Los call sites reales del repositorio quedaron migrados a `utils_oas`.
* [ ] No quedó `helpers/utilidades.go` o equivalente como puente hacia `utils_oas`.
* [ ] No quedó código productivo usando `context.Background()` o `context.TODO()` para llamar `request.*WithContext`.
* [ ] En flujos iniciados por una petición entrante, el `ctx` usado en `request.*WithContext` proviene de esa petición o de un derivado directo.
* [ ] Las brechas de `utils_oas` quedaron documentadas.
* [ ] Si el `GOMODCACHE` local estaba desalineado, se forzó su corrección o se evitó su uso mediante cache temporal aislado consistente con `v0.5.0-beta.2`.
* [ ] Si no fue posible limpiar y redescargar desde el tag remoto, el reporte final declaró `Estado: incompleto`.
* [ ] Se ejecutaron verificaciones técnicas o se documentó el bloqueo.
* [ ] El proyecto compila contra la implementación real de `utils_oas` resuelta localmente.
* [ ] No quedó una segunda fase pendiente para migrar call sites cubiertos por `request.*WithContext`.
* [ ] Se hizo verificación textual repo-wide de usos remanentes de funciones históricas y cualquier remanente quedó justificado por excepción documentada.
* [ ] Si el usuario no limitó el alcance, se ejecutó auditoría repo-wide de remanentes antes del cierre.
* [ ] No se crearon caches ni temporales de Go dentro del workspace o del repositorio durante la ejecución.
* [ ] Si quedaron excepciones o remanentes, el reporte final los declaró explícitamente como trabajo incompleto y no como cierre total.

## Formato de salida obligatorio

El cierre debe incluir siempre estos campos, aunque sea de forma breve:

```text
Alcance asumido:
Estado: completo|incompleto
Integraciones migradas:
Archivos o usos remanentes:
Bloqueos o excepciones abiertas:
Verificaciones ejecutadas:
Siguiente acción concreta:
```

Reglas:

* Si el usuario no limitó el alcance y solo se trabajó un subconjunto del repo, `Estado` debe ser `incompleto`.
* Si no se ejecutó auditoría repo-wide, `Estado` debe ser `incompleto`.
* Si no se ejecutó limpieza de `GOMODCACHE` y redescarga explícita de `utils_oas@v0.5.0-beta.2`, `Estado` debe ser `incompleto`, salvo que el bloqueo ambiental haya quedado documentado; incluso en ese caso sigue siendo `incompleto`.
* Si `go list -m -json github.com/udistrital/utils_oas` muestra `Replace`, una ruta local o una resolución basada en `vendor/`, `Estado` debe ser `incompleto`.
* Si el motivo para dejar funciones históricas fue que el agente “no encontró” símbolos ya confirmados en el tag objetivo, `Estado` debe ser `incompleto` y el resultado debe tratarse como incorrecto.
* Si quedan wrappers temporales, funciones históricas, `context.Background()`/`context.TODO()` productivos o excepciones sin brecha documentada, `Estado` debe ser `incompleto`.
* Hallazgos restringidos a `tests/` o `*_test.go` no obligan por sí solos a `Estado: incompleto` si el código productivo quedó migrado y las verificaciones pedidas por el usuario pasan o quedaron correctamente reportadas.
* Si el agente crea artefactos temporales o caches dentro del workspace o del repositorio, el resultado es incorrecto aunque luego intente limpiarlos; la ejecución debe tratarse como incumplimiento del skill.
* `Archivos o usos remanentes` no puede decir “ninguno” sin evidencia de auditoría repo-wide.

## Modos de Falla

El agente está ejecutando mal este skill si no intenta primero migrar a `request.*WithContext`, no modifica firmas o call sites para propagar `ctx` cuando el caso está cubierto, deja `request.GetJson`, `request.GetJsonTest2`, `request.GetJsonWSO2Test`, `request.SendJson` o `request.SendJson2` como solución final en casos cubiertos por `request.*WithContext`, usa `request.GetWithContext(context.Background(), ...)` en código productivo en vez de propagar el contexto real de la petición, corta la cadena de propagación del `ctx` entre controller/handler y la integración saliente, no hace verificación repo-wide de remanentes de esas funciones históricas, toma un flujo puntual como si fuera alcance total sin límite explícito del usuario, confía en una copia previa cacheada de `utils_oas` sin limpiar `GOMODCACHE` y redescargar desde el tag objetivo cuando el entorno sí lo permitía, acepta un `replace` local o `vendor/` como si eso garantizara la versión remota, toma una falla de IDE, autocompletado o resolución local como si demostrara que `PostWithContext`/`PutWithContext`/`PatchWithContext`/`DeleteWithContext` no existen en el tag ya confirmado, migra todo a una sola capa sin analizar contrato, evita migrar a `utils_oas` por riesgo sin intentar una migración compatible, conserva helpers "por si acaso", convierte `utilidades.go` u otro archivo en una capa de pass-through hacia `utils_oas` y no modifica los call sites reales, deja wrappers locales genéricos como estado final, deja una “segunda fase” pendiente para call sites ya cubiertos por `request.*WithContext`, rompe `Authorization`, ignora `LimpiezaRespuestaRefactor`, usa `requestresponse` sin validar parser, deja código duplicado, acepta una excepción sin brecha de `utils_oas`, conserva llamadas sin `context` sin justificarlo, omite el formato de salida obligatorio, o reporta el trabajo como completado cuando todavía existen excepciones, remanentes o verificaciones obligatorias pendientes.
