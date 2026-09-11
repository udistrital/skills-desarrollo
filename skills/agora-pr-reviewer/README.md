# agora-pr-reviewer

Revisa calidad local del PR y consistencia de la solución HU. Incluye common, CRUD, MID, frontend, microfrontend y solution reviewers como perspectivas internas.

```text
$agora-pr-reviewer owner/repository#123 — solo informe local
$agora-pr-reviewer https://github.com/owner/repository/pull/123
```

Los identificadores anteriores son ejemplos de formato. Descubre Issues, HU, hermanos y contratos; reporta vacíos de trazabilidad. Entrega APPROVE/COMMENT/REQUEST_CHANGES como recomendación y un estado HU independiente. APPROVE puede coexistir con PARTIALLY_IMPLEMENTED. No tiene script que apruebe PRs ni ejecuta revisiones remotas.

Detalle en `references/specialists.md`, `contracts.md` y `report.md`; ejercicios locales en `examples/synthetic-reviews.md`. No se han revisado PRs AGORA reales para probar esta versión.

## Instalación y portabilidad

Copiar esta carpeta completa a `~/.codex/skills/` o al directorio de skills elegido. No requiere ninguna skill hermana ni archivos fuera de su carpeta. `openai.yaml` conserva la convención del repositorio; `agents/openai.yaml` contiene los mismos metadatos para entornos Codex que usan esa ubicación. Mantener ambas copias iguales.

Para asistentes sin soporte nativo, pegar `references/portable-prompt.md`; si tienen acceso a archivos, adjuntar SKILL.md y las referencias enlazadas para el detalle completo. El prompt portable contiene reglas operativas mínimas y URLs autoritativas.

## Fuentes y mantenimiento

Las referencias locales son procedimientos y resúmenes mínimos, no copias de manuales institucionales. Ver `references/institutional-sources.md` para las lecturas auditadas y enlaces vigentes; refrescar fuentes al ejecutar. Las reglas estables repetidas permiten instalación independiente; mantener términos y estados alineados al actualizar.

Esta versión solo lee GitHub o evidencias locales. No publica resultados, no modifica Developed y no hace commit/push. La ausencia de permisos se refleja como evidencia no verificada. GitHub MCP es opcional; gh es alternativa de lectura, no dependencia del razonamiento.
