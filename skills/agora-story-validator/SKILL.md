---
name: agora-story-validator
description: Valida aceptación de una HU AGORA para revisión o cierre de Sprint con evidencia por criterio, DoD por Issue y consistencia CRUD/MID/FRONT; no confunde PRs aprobados con cumplimiento funcional.
---
# agora-story-validator

## Entrada y límites

Recibe HU ID, enlace HU o `owner/repository#Issue` desde la que pueda resolverse. Un ID aislado necesita un localizador configurado (workbook/documentación) o evidencia suficiente para buscarlo; no adivinar HU por número de Issue. Puede usar exportaciones locales con URL/SHA/fecha.

**Solo informe local**. No cerrar/editar Issues, cambiar Project, enviar reviews, aprobar PRs, crear ramas, hacer push, merge ni commit. **Developed es solo lectura** y no constituye evidencia de aceptación. El resultado es recomendación de aceptación para Sprint review, no aprobación institucional registrada.

## Flujo

1. Lee [reglas AGORA](references/agora-rules.md), [fuentes institucionales](references/institutional-sources.md) y [recuperación de contexto](references/retrieval.md). No depende de las otras skills.
2. Resuelve HU original y lee texto completo, criterios y escenarios, anexos/versiones. Registra localizador visible (URL o workbook/hoja/ID/fila) y versión. Si no se resuelve o los criterios son ambiguos, informa NOT_ACCEPTED por evidencia insuficiente, sin inventar escenarios.
3. Reconstruye `HU → criterios → repositorios CRUD/MID/FRONT → Issues → PRs → pruebas/CI → DoD → contratos → evidencia funcional`. Descubre hermanos por enlaces y búsquedas acotadas. Distingue capa no requerida de capa faltante; conserva estado desconocido si no hay acceso. Los paquetes dry-run del planner pueden orientar, pero no demuestran implementación ni crean Issues reales.
4. Para cada criterio original, identifica repositorios/responsabilidades y pruebas que demuestran su resultado. Aplica [protocolo de aceptación](references/acceptance.md). No sustituir criterios de negocio por criterios técnicos de Issues. No aceptar una colección vacía de criterios como cumplimiento total.
5. Lee plantilla real de cada Issue y evalúa **DoD por Issue/repositorio**, incluyendo aprobación humana y documentación. DoR sirve como contexto histórico: una brecha de inicio resuelta no invalida el cierre; documenta evidencia nueva. Tampoco aprobar cierre porque una Issue esté READY.
6. Compara contratos según [contracts.md](references/contracts.md), usando código de ambos extremos y versiones efectivas en el ambiente de prueba. Incluye Single-SPA/root/web-components y servicios institucionales relevantes; no inventes MID Terceros ni reglas WSO2 operativas. PRs compatibles entre sí pero no desplegados juntos no prueban flujo integrado.
7. Inspecciona tests/CI para SHA correspondiente y evidencia funcional integrada. Registra ambiente, versión, fecha, resultado esperado/observado y procedencia. Mocks prueban partes, no integración institucional completa. No ejecutar código no inspeccionado ni pruebas activas contra servicios reales como parte de esta validación.
8. Emite [informe](references/acceptance.md) con evidencia por decisión, resultado de aceptación y estado HU independiente. Revisa cobertura completa, DoD, contratos, seguridad aplicable y limitaciones. Nunca rechazar un PR técnicamente correcto por trabajo hermano pendiente: esto decide aceptación de HU, no reviews individuales.

## Resultados

- `ACCEPTED`: todos los criterios y DoD aplicables PASS (o N/A justificado), contratos conformes y validación funcional integral suficiente de la versión objetivo, sin bloqueos.
- `ACCEPTED_WITH_OBSERVATIONS`: misma evidencia obligatoria satisfecha; quedan solo observaciones no bloqueantes con responsable y seguimiento propuesto. No usar para ocultar un criterio fallido/no verificado, DoD obligatorio faltante o riesgo de seguridad bloqueante.
- `NOT_ACCEPTED`: criterio/DoD obligatorio FAIL/UNVERIFIED, dependencia necesaria pendiente, incompatibilidad o falta de evidencia funcional/traza. Explica si es incumplimiento demostrado o validación pendiente.

`COMPLETE` solo acompaña aceptación sustentada; PRs merged por sí solos llevan como máximo IMPLEMENTED_PENDING_VALIDATION. Cualquier aprobación SM/líder/Seguridad que se requiera debe estar acreditada por su fuente.

## Uso

`$agora-story-validator HU-ID — valida para revisión de Sprint con evidencia enlazada.`

`$agora-story-validator owner/repository#123 — descubre la HU y genera informe local.`

Práctica local: [ejercicios sintéticos](examples/synthetic-validation.md). [Prompt portable](references/portable-prompt.md).
