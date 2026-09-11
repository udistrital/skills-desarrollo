# Reglas AGORA estables — copia mínima para instalación independiente

Origen: contrato operativo AGORA proporcionado por OATI para estas skills. Las reglas de PH, selección, estados y Developed son del proyecto; no atribuirlas a lineamientos_oas sin evidencia. Las fuentes cambiantes se consultan por URL en institutional-sources.md.

## Seguridad y trazabilidad

Versión local: lectura de GitHub y artefactos locales únicamente. No Issues, comentarios, reviews, campos, ramas remotas, merge, push ni commits. **Developed pertenece a desarrolladores y jamás se modifica**; su valor no prueba aceptación. No transportar Developed a una propuesta de actualización, aunque sea para conservar el mismo valor. Separar recuperación, razonamiento e intención de mutación; no hay adaptador de escritura en esta versión.

HU = fuente funcional de verdad. Issue = unidad técnica de un repositorio. Cada HU genera cero o una Issue por capa CRUD/MID/FRONT presente; una HU sin capas requiere aclaración. Las descripciones son diferentes por responsabilidad. Mantener HU ID, enlace original o localizador workbook + hoja + ID + fila, todos los repositorios involucrados y referencias hermanas. No inventar IDs ni URLs de Issues futuras. Una tarea >13 PH produce propuesta de descomposición para refinar, no múltiples Issues emitidas automáticamente que contradigan el límite por capa.

## Estimación y planificación

| PH | Referencia aproximada |
|---|---|
| 1 | 1 hora |
| 2 | 3–5 horas |
| 3 | 1 día laboral |
| 5 | 2–3 días laborales |
| 8 | 3–4 días laborales |
| 13 | 5 días laborales |

Solo 1, 2, 3, 5, 8, 13; 13 máximo por Issue. No convertir horas mecánicamente ni prometer tiempos. Explicar complejidad, incertidumbre, pruebas y dependencias. >13 requiere descomposición; estimación sin evidencia queda pendiente. Prioridad conceptual 1–4; no inventar equivalencia urgente/baja sin configuración. Sprint semanal, resuelto contra iteraciones reales; no asignarlo por fecha inferida.

## DoR basado en evidencia

Leer plantilla actual: sus `[x]` iniciales no demuestran nada. Cada ítem: texto original, PASS/FAIL/UNVERIFIED/N/A, evidencia, fecha, brecha y acción. N/A requiere justificación y no se marca cumplido automáticamente.

- READY: todos los ítems aplicables probados, sin bloqueos.
- READY_WITH_GAPS: objetivo y criterios comprensibles/testables, con brechas explícitas sin bloqueo conocido; no oculta dependencias pendientes. Una propuesta de Sprint puede mostrar este estado sin alterar las casillas.
- NOT_READY: bloqueo conocido, falta contexto/criterios esenciales, trazabilidad no reconstruible, o descomposición >13 pendiente.

Reevaluar ante nueva evidencia durante Sprint; conservar qué cambió y por qué. La skill no sustituye refinamiento/estimación del equipo ni aprobación SM/líder.

## Estado de implementación HU (separado de decisión PR)

Aplicar en este orden de evidencia, declarando incertidumbre:
- COMPLETE: todos los criterios funcionales y DoD aplicables por Issue validados; contratos y evidencia integral de la versión objetivo conformes.
- IMPLEMENTED_PENDING_VALIDATION: todas las capas requeridas implementadas, falta evidencia funcional/DoD/validación integrada.
- PARTIALLY_IMPLEMENTED: al menos una capa/responsabilidad completa y otra pendiente.
- IN_PROGRESS: trabajo iniciado sin ninguna responsabilidad completa demostrada, o avance existente con cobertura desconocida (indicar provisional).
- NOT_STARTED: evidencia confirma que ningún trabajo requerido ha empezado; ausencia de acceso no prueba este estado.

## Vocabulario de evidencia

PASS/FAIL/UNVERIFIED/N/A para criterios y DoD. MATCH/MISMATCH/PENDING/UNVERIFIED para contratos. N/A siempre explicado. Distinguir dato observado, inferencia y propuesta. Registrar URL/ruta, SHA/versión, fecha, ambiente y alcance de cada prueba. Merged, aprobado, checkbox o Developed no prueban funcionamiento.
