# Protocolo de aceptación HU

## Inventario funcional

Transcribir o resumir fielmente cada criterio HU con ID original; si no hay IDs, asignar claves locales AC-1… y conservar texto/fuente. Para cada uno registrar pasos, precondiciones, rol, resultado esperado, evidencia observada, versión/ambiente y responsable de validación. No inventar criterios oficiales; propuestas adicionales se registran aparte.

| Criterio / escenario HU | Fuente / versión | Repos/Issues responsables | Evidencia funcional / fecha / ambiente / SHA | Esperado vs observado | PASS/FAIL/UNVERIFIED/N/A | Justificación / siguiente acción |
|---|---|---|---|---|---|---|

PASS requiere evidencia que cubra el criterio completo y roles/escenarios aplicables; un test unitario aislado puede no cubrirlo. FAIL requiere resultado observado incompatible. UNVERIFIED indica evidencia ausente, inaccesible, obsoleta o insuficiente; no es acusación de defecto. N/A exige razón fundada en alcance HU y evidencia de su exclusión, no decisión arbitraria para cerrar.

Si criterio contiene varios escenarios, evaluar cada uno; un PASS parcial no satisface el conjunto. Contrastar anexos funcionales y cambios de alcance autorizados. Si hay conflicto de versiones de HU, detener recomendación de aceptación y mostrar diferencia a resolver.

## DoD independiente por Issue/repositorio

Obtener DoD real de Issue/plantilla y contexto de equipo. Developer/Plus auditadas piden desarrollo local, push feature, pruebas funcionales locales, PR develop, criterios cumplidos, documentación y aprobación SM/líder. Analyst tiene DoD de artefacto/documentación/criterios/aprobación SM/líder/SoSM. La existencia de una rama/PR solo prueba ese ítem, no tests ni aprobación humana.

| Capa | Repo / Issue / PR / SHA | Ítem DoD original | Estado | Evidencia / fecha | Brecha / acción |
|---|---|---|---|---|---|

No colapsar todas las Issues en un checkbox “DoD cumplido”. No usar como prueba el checkbox por sí solo ni tu propia decisión APPROVE para aprobación de líder. Conservar ítems no aplicables con justificación. DoR se reevalúa con nueva evidencia para registrar evolución del Sprint; no exigir retrospectivamente que estuviera READY si ahora está validado.

## Contratos y funcionalidad integrada

Mapear dependencias reales, incluyendo capas sin cambios que proveen contratos existentes. Comparar método, path, path/query params, payloads/envelopes, campos/tipos/nullability, status/errores, paginación, auth y permisos. Registrar pruebas de cadena FRONT→MID→CRUD y servicios institucionales cuando intervengan. Entorno de mocks o SHA anterior = alcance limitado; pruebas locales aisladas no prueban despliegue integrado.

Aplicar fuentes OATI según stack: GitFlow/documentación, endpoints/modelos, Docker/health, tests/QA, Single-SPA y CI/CD. Seguridad: secretos, inputs, autenticación/roles/autorización, errores/API, dependencias/SonarQube/Dependabot y OWASP según exposición. Si se requiere validación formal de Seguridad para la entrega objetivo, solicitar evidencia existente, no atribuirla al asistente. Distinguir aceptación Sprint de autorización de despliegue productivo.

## Decisión reproducible

1. ¿HU original y todos sus criterios están identificados? Si no: NOT_ACCEPTED / cobertura desconocida.
2. ¿Todos los criterios aplicables tienen PASS y evidencia vigente suficiente? Si no: NOT_ACCEPTED, indicando FAIL o UNVERIFIED.
3. ¿DoD por Issue y contratos/dependencias necesarios están satisfechos? Si no: NOT_ACCEPTED; distinguir implementación pendiente de validación pendiente.
4. ¿Existe evidencia funcional integral de la versión objetivo y controles de seguridad exigibles? Si no: NOT_ACCEPTED, sin declarar defectos no probados.
5. Si todo se cumple: ACCEPTED; si además quedan observaciones no bloqueantes, ACCEPTED_WITH_OBSERVATIONS. Las observaciones no pueden ser criterios/DoD obligatorios incumplidos.

Asignar además estado HU según agora-rules.md. Si todas las capas están implementadas pero falta QA, IMPLEMENTED_PENDING_VALIDATION + NOT_ACCEPTED. Si CRUD listo y MID/FRONT pendientes, PARTIALLY_IMPLEMENTED + NOT_ACCEPTED. Si todos los criterios/DoD/contratos están validados, COMPLETE + ACCEPTED (o ACCEPTED_WITH_OBSERVATIONS).

## Salida local

1. HU ID, enlace original/localizador, versión y Sprint objetivo; alcance y fecha de corte.
2. Grafo de repositorios/Issues/PRs con SHA, fuentes y vínculos confirmados/inferidos/faltantes.
3. Matriz de aceptación por criterio/escenario.
4. Matrices DoD por Issue, DoR contextual y contratos por arista.
5. Evidencia funcional/CI/QA/seguridad disponible y faltante; mocks y limitaciones explícitos.
6. Hallazgos BLOCKER/MAJOR/MINOR/SUGGESTION con ubicación/evidencia, requisito o fuente, impacto, corrección y repo responsable. Distinguir THIS_PR_DEFECT si se demuestra, OTHER_REPO_PENDING, PARALLEL_DEPENDENCY y UNVERIFIED. Este informe no emite ni registra reviews.
7. **Acceptance outcome:** ACCEPTED | ACCEPTED_WITH_OBSERVATIONS | NOT_ACCEPTED, con evidencia que sustenta la elección.
8. **HU implementation status:** NOT_STARTED | IN_PROGRESS | PARTIALLY_IMPLEMENTED | IMPLEMENTED_PENDING_VALIDATION | COMPLETE, con razón independiente.
9. Acciones concretas para cierre y responsable propuesto, sin modificar Issues/Project. Developed no se actualiza.

Lista final: cada criterio original aparece; cada repo/Issue tiene DoD; cada dependencia tiene resultado; evidencia corresponde a versión objetivo; aprobación humana no inventada; incertidumbre visible; cero escrituras remotas.
