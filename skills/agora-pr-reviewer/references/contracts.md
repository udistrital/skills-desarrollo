# Comparación de contratos

Construye una fila por operación y por discrepancia, no una conclusión global sin evidencia.

| Arista / operación | Productor repo@SHA archivo:línea | Consumidor repo@SHA archivo:línea | Dimensión | Esperado por HU/contrato acordado | Valor productor | Valor consumidor | Resultado | Responsable / impacto |
|---|---|---|---|---|---|---|---|---|

Dimensiones obligatorias cuando apliquen: método HTTP, path/version/base URL, path params, query params (nombres/defaults/codificación), request body, response body/envelope, campos, tipos, nullability/ausencia, status codes, errores, paginación (offset/page/limit/total), autenticación y autorización. Registra `N/A` con motivo, no omitas silenciosamente dimensiones.

Resultados: `MATCH`, `MISMATCH`, `PENDING`, `UNVERIFIED`. La inspección estática MATCH no equivale a prueba de integración PASS. Identifica mocks, OpenAPI desactualizado y diferencias entre código y documentación; la implementación demuestra conducta y HU/contrato acordado demuestra intención.

Si ambos PRs existen: compara sus heads y compatibilidad con las versiones que convivirán durante despliegue. Si solo existe un extremo: declara el otro PENDING (pendiente confirmado) o UNVERIFIED (sin acceso/evidencia). No construyas respuestas hipotéticas como si fueran reales. Para atribuir MISMATCH al PR actual, identifica el contrato requerido/acordado que rompe; de otro modo informa conflicto a resolver.

Ejemplo SINTÉTICO: CRUD@a devuelve `{data: [{id: 1}]}`; MID@b accede `body.items`. Sin transformación, el resultado no es compatible aunque ambos usen GET /objetos. Si MID@b es el PR revisado y el CRUD/contrato acordado requiere `data`, el hallazgo es MAJOR/THIS_PR_DEFECT. Si MID aún no existe, se registra consumidor PENDING y no un defecto CRUD.
