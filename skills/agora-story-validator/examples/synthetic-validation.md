# Ejercicios SINTÉTICOS de aceptación

No son HU/Issues AGORA reales. Evaluar con datos locales, sin consultar ni escribir GitHub.

| Caso | Evidencia proporcionada | Resultado esperado |
|---|---|---|
| Todas las PRs merged | CI verde pero sin prueba del flujo funcional | NOT_ACCEPTED; IMPLEMENTED_PENDING_VALIDATION |
| CRUD completo, MID/FRONT pendientes | CRUD aprobado y pruebas locales; flujo UI aún no disponible | NOT_ACCEPTED; PARTIALLY_IMPLEMENTED; no invalidar PR CRUD |
| Dos criterios, uno falla | AC-1 consulta PASS; AC-2 edición devuelve 500 | NOT_ACCEPTED; explicar FAIL de AC-2 independientemente de AC-1 |
| Falta aprobación requerida | Criterios funcionales PASS, DoD aprobación líder UNVERIFIED | NOT_ACCEPTED; IMPLEMENTED_PENDING_VALIDATION |
| Completa con mejora opcional | Criterios, DoD, contratos y evidencia integrada PASS; sugerencia de refactor fuera de requisitos | ACCEPTED_WITH_OBSERVATIONS; COMPLETE; seguimiento propuesto |
| Completa | Toda evidencia obligatoria vigente y sin observaciones | ACCEPTED; COMPLETE |
| HU no accesible | Issues merged; vínculo HU devuelve acceso denegado | NOT_ACCEPTED por evidencia insuficiente; no inventar criterios |
| DoR inicial incompleto, resuelto | Dependencia inicialmente pendiente; contrato y prueba actuales PASS, resto DoD/criterios PASS | ACCEPTED; COMPLETE; registrar evolución DoR |
| Contratos heads compatibles, despliegue viejo | FRONT prueba contra MID anterior incompatible | NOT_ACCEPTED; distinguir compatibilidad propuesta de validación real |

Ensayo: preparar el informe por criterio y DoD con estas premisas, comprobar las decisiones y prohibición de escrituras. Son casos de revisión manual, no sustituyen pruebas con HU reales.
