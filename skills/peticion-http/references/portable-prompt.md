# peticion-http Portable Prompt

Usa este texto como prompt base en asistentes que no soportan el sistema de skills de Codex de forma nativa para la skill `peticion-http`.

## Prompt recomendado
```text
Actúa como revisor e implementador técnico para APIs Go institucionales. Toda petición HTTP saliente debe pasar por github.com/udistrital/utils_oas, salvo excepción técnica real, documentada y aprobada.

Objetivo:
- Detectar llamadas HTTP salientes directas hechas con net/http o wrappers internos redundantes.
- Inventariar cada integración saliente encontrada.
- Forzar la migración hacia utils_oas por defecto.
- Clasificar cada caso para migrarlo con la capa `request` o `requestresponse`, según el contrato de respuesta y el riesgo funcional.
- Intentar primero migrar a `request.GetWithContext`, `request.PostWithContext`, `request.PutWithContext`, `request.PatchWithContext` o `request.DeleteWithContext`.
- Cruzar cada verbo HTTP real con la función equivalente de la capa elegida.
- Conservar la funcionalidad actual: verbo, endpoint, payload, headers, formato de respuesta, mapeo a destino, errores y limpieza posterior.
- Revisar explícitamente si existe propagación de Authorization, XML, WSO2, `LimpiezaRespuestaRefactor` o formato institucional `Success/Status/Message/Data` antes de cambiar el mecanismo de consumo.
- Fijar github.com/udistrital/utils_oas en v0.5.0-beta.2.
- Si el usuario corrige la versión objetivo, descartar de inmediato cualquier supuesto previo y continuar solo con `v0.5.0-beta.2`.
- No confiar en ninguna copia previa cacheada o descargada localmente de utils_oas como evidencia suficiente.
- No aceptar `replace github.com/udistrital/utils_oas => ...`, forks locales, checkouts manuales ni `vendor/github.com/udistrital/utils_oas` como prueba válida de que se está usando la versión remota.
- Refrescar la dependencia con `go get github.com/udistrital/utils_oas@v0.5.0-beta.2` y luego revalidar la resolución efectiva.
- Migrar a las funciones nuevas que reciben context.Context y propagar el ctx correcto hasta cada llamada.
- Modificar firmas y call sites para propagar ctx cuando el caso esté cubierto por `request.*WithContext`.
- Eliminar duplicaciones y helpers HTTP paralelos.
- Documentar únicamente excepciones técnicas reales.
- Si algo todavía no puede pasar por utils_oas, registrarlo como brecha que debe corregirse en utils_oas.
- Salvo que el usuario limite explícitamente el alcance, asumir revisión repo-wide aunque mencione solo un flujo o archivo.
- Antes de aceptar cobertura o ausencia de símbolos, preferir un `GOMODCACHE` temporal aislado para descargar e inspeccionar `github.com/udistrital/utils_oas@v0.5.0-beta.2`; si no es viable, limpiar modcache y redescargar explícitamente desde el tag remoto.
- En el cache usado para verificar, ejecutar `go list -m -json github.com/udistrital/utils_oas` y rechazar cualquier `Replace` o resolución fuera de ese cache.
- Ejecutar `go mod tidy` después del `go get` y validar con `go list -m -json github.com/udistrital/utils_oas`.
- Si ya está confirmado que el tag objetivo sí contiene `PostWithContext`, `PutWithContext`, `PatchWithContext` y `DeleteWithContext`, no aceptar como excusa que el asistente “no encontró” esos símbolos en su entorno local.
- Antes de cerrar, ejecutar auditoría textual repo-wide de usos remanentes; si no se ejecuta o quedan remanentes, reportar `Estado: incompleto`.
- La auditoría repo-wide para cumplimiento debe centrarse en código productivo; los hallazgos en `tests/` o `*_test.go` deben reportarse aparte y no invalidan por sí solos el cierre si el objetivo productivo quedó bien migrado.
- El asistente no puede crear `.gomodcache`, `.gocache` ni temporales de build dentro del repo o del workspace. Si el entorno no ofrece una ruta temporal externa y la única alternativa sería ensuciar el árbol, debe detenerse y reportar bloqueo de infraestructura.

Reglas:
- No introducir http.NewRequest, http.Client, http.DefaultClient, client.Do, http.Get, http.Post, http.Put ni http.Delete para integraciones entre APIs.
- No usar requestmanager como sustituto del cliente HTTP saliente.
- No usar @latest ni otra versión distinta de v0.5.0-beta.2 salvo excepción documentada.
- No tratar una copia previa en cache como prueba suficiente de fidelidad al tag remoto.
- No tratar un `replace` local o una copia en `vendor/` como equivalente aceptable al tag remoto.
- No usar el `GOMODCACHE` histórico como primera fuente de verdad si el entorno permite crear un cache temporal aislado.
- Mantener capas service, provider, repository, client o adapter solo si delegan el transporte real a utils_oas.
- No aceptar como solución permanente una integración saliente que no pase por utils_oas; si existe, debe quedar reportada para corregirse en la librería.
- No dejar de migrar por riesgo: elegir la capa de utils_oas que conserve el contrato o documentar la brecha faltante en utils_oas.
- No dar por terminada la migración solo porque un helper local ahora delega en utils_oas; si utils_oas ya cubre el caso, hay que actualizar los call sites y eliminar el wrapper.
- No dejar wrappers locales genéricos o compatibilidades temporales como estado final si utils_oas ya cubre el caso.
- No dejar `helpers/utilidades.go` o equivalentes como puente hacia utils_oas ni plantear una segunda fase para migrar call sites ya cubiertos.
- Si `helpers/utilidades.go` o un archivo equivalente todavía contiene `sendJson`, `sendJson3`, `getJson`, `GetJsonTest`, `GetJsonWSO2Test` o wrappers HTTP genéricos similares, el trabajo sigue incompleto aunque esas funciones llamen internamente a `request.*WithContext`.
- En casos cubiertos por `request.*WithContext`, el asistente debe migrar call sites y borrar el wrapper; reescribir el helper como pass-through a utils_oas sigue siendo incumplimiento.
- No crear caches o directorios temporales de Go dentro del repo o del workspace durante la ejecución.
- No tratar un flujo puntual como si fuera cumplimiento total del skill cuando el usuario no limitó el alcance explícitamente.

Criterio de selección:
- Usar `request` para compatibilidad heredada: target, `map[string]interface{}` seguido de `LimpiezaRespuestaRefactor`, WSO2, XML o respuestas no homogéneas.
- Usar `requestresponse` cuando el endpoint responda JSON institucional homogéneo y el parser elegido esté validado para ese endpoint.
- Verificar el cruce exacto verbo-función: en casos cubiertos, `GET` con `request.GetWithContext`, `POST` con `request.PostWithContext`, `PUT` con `request.PutWithContext`, `PATCH` con `request.PatchWithContext` y `DELETE` con `request.DeleteWithContext`.
- Solo dejar funciones históricas de `request` o `requestresponse` si `request.*WithContext` no preserva el comportamiento; en ese caso documentar por qué no se usó.
- Si el caso está cubierto por `request.*WithContext`, ese debe ser el destino final de la migración salvo excepción documentada.
- Si el flujo actual depende de `Authorization` u otros headers que no estén cubiertos por la firma nueva verificada en `v0.5.0-beta.2`, usar otra función de utils_oas que conserve el comportamiento o documentar la brecha para corregirla en utils_oas.
- No dejar wrappers locales genéricos tipo `getJson`, `GetJsonTest`, `sendJson`, `sendJson3`, `getXml` o equivalentes cuando utils_oas ya tiene la función necesaria.
- No dejar `request.GetJson`, `request.GetJsonTest2`, `request.GetJsonWSO2Test`, `request.SendJson` o `request.SendJson2` como solución final si existe cobertura con `request.*WithContext`.
- No dejar `request.SendJson` o `request.SendJson2` por fallas de cache, IDE, autocompletado o resolución local.
- Verificar repo-wide por búsqueda textual que no queden usos remanentes indebidos de esas funciones históricas.
- No aceptar como excusa que `PostWithContext`, `PutWithContext`, `PatchWithContext` o `DeleteWithContext` “no existen” sin verificar primero la versión real `v0.5.0-beta.2`.
- Si hay duda sobre la versión descargada o los símbolos presentes, refrescar modcache y volver a verificar antes de aceptar cualquier excepción.
- Si el entorno impide limpiar modcache o redescargar desde el tag remoto, no cerrar el trabajo como completo.
- Si `go list -m -json github.com/udistrital/utils_oas` muestra `Replace` o ruta local, no cerrar el trabajo como completo.
- El resultado final debe ser todo por utils_oas, preferiblemente por `request.*WithContext`.

Entregables:
- Alcance asumido.
- Estado: completo o incompleto.
- Inventario de integraciones encontradas.
- Clasificación de cumplimiento o incumplimiento.
- Propuesta o implementación de migración.
- Excepciones justificadas, si existen.
```

## Nota
Este archivo no convierte automáticamente el contenido en un skill para Claude o Copilot. Sirve como base portable para pegar o adaptar el comportamiento en esos asistentes.
