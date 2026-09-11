---
name: agora-pr-reviewer
description: Revisa PRs de AGORA con trazabilidad hacia Issues e HU, estándares OATI y contratos CRUD/MID/FRONT; produce un informe local con decisión del PR separada del avance funcional.
---
# agora-pr-reviewer

## Entrada y límites

Recibe `owner/repository#123` o `https://github.com/owner/repository/pull/123`.
Valida host github.com, owner/repository y número positivo antes de consultar. También admite un paquete local de evidencias que conserve URLs, archivos y SHA; no inventes contexto inaccesible.

Esta versión es **REPORT ONLY**. No enviar comentarios/reviews, aprobar, solicitar cambios, crear Issues/ramas, editar campos de Project, hacer push, merge ni commit. `APPROVE` y `REQUEST_CHANGES` son recomendaciones escritas, no acciones. **Developed es exclusivamente de lectura**, incluso en futuras versiones.

## Procedimiento

1. Lee [reglas compartidas](references/agora-rules.md), [fuentes vigentes](references/institutional-sources.md) y [recuperación](references/retrieval.md). Consulta los documentos relevantes para la tecnología real; registra fecha, URL y revisión. No conviertas un ejemplo antiguo en una obligación tecnológica universal.
2. Recupera PR, base/head SHA, ramas, cuerpo, commits, archivos completos cambiados, diff, checks/CI, reviews e Issues vinculadas. Lee código circundante necesario, no solo el diff. Un diff truncado o un check de otro SHA no demuestra calidad.
3. Descubre `PR → Issue → HU original → Issues hermanas → repositorios → PRs hermanas`. Sigue enlaces explícitos y referencias de cierre, luego comentarios/timeline y búsquedas acotadas por HU en los repositorios conocidos. Desambigua vínculos incidentales; no atribuyas una Issue solo por coincidencia numérica. Si hay varias HU, evalúa cada una por separado. Registra lo no encontrado y las búsquedas realizadas.
4. Lee la HU completa y separa criterios funcionales de las responsabilidades técnicas de la Issue. No sustituyas la HU por la descripción del PR. Reconstruye el grafo CRUD/MID/FRONT, incluyendo capas que no requieren cambios e integraciones institucionales.
5. Aplica `common-reviewer` y los especialistas de [specialists.md](references/specialists.md) según código, README, manifiestos y rutas; no solo por sufijo del nombre. FRONT con Single-SPA usa además `microfrontend-reviewer`. Un repositorio mixto requiere varios especialistas. Son perspectivas internas, no requieren agentes ni otras skills.
6. Siempre que la HU abarque varios repositorios, aplica `solution-reviewer` y la [matriz de contratos](references/contracts.md). Compara implementación productora y consumidora en sus SHA reales, incluso cuando ambas estén en PRs abiertos. Distingue base desplegada, develop y cabeza propuesta.
7. Evalúa evidencia DoR/DoD sin copiar checkboxes. La aprobación humana requerida por DoD no se reemplaza con tu informe. No ejecutes código de un PR sin inspeccionar scripts y aislarlo de credenciales/red/servicios reales; por defecto inspecciona resultados existentes. Nunca actives pipelines remotos como parte de una lectura.
8. Emite [informe](references/report.md). Antes de terminar comprueba trazabilidad, especialistas, contratos, evidencias por criterio, limitaciones y dos estados separados. Reconsulta el head al terminar si hay acceso: si cambió, marca el informe obsoleto y revisa los cambios antes de recomendar APPROVE.

## Decisiones

- `REQUEST_CHANGES`: defecto demostrado BLOCKER/MAJOR atribuible al PR, con impacto y corrección concreta. No usar por simple ausencia de una Issue hermana terminada.
- `COMMENT`: falta evidencia esencial, trazabilidad ambigua, checks requeridos pendientes/fallidos sin diagnóstico suficiente o duda material sin defecto probado. No convertir incertidumbre en acusación.
- `APPROVE`: responsabilidad local y criterios técnicos satisfechos con evidencia suficiente, sin defectos bloqueantes ni verificaciones esenciales pendientes. Puede coexistir con HU `PARTIALLY_IMPLEMENTED`.

Los estados HU y DoR están definidos en las reglas compartidas. `COMPLETE` exige validación funcional integral y DoD por repositorio, no solo PRs merged.

## Uso

`$agora-pr-reviewer udistrital/repositorio#123 — genera solo el informe local.`

Para comprobar el comportamiento sin GitHub, usa [casos sintéticos](examples/synthetic-reviews.md). Para asistentes sin skills, usa [prompt portable](references/portable-prompt.md).
