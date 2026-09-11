# agora-story-validator

Valida si una HU puede aceptarse en Sprint review, mediante criterios funcionales, DoD por Issue, contratos entre capas y evidencia integrada.

```text
$agora-story-validator HU-ID — usa su enlace o localizador configurado
$agora-story-validator owner/repository#123 — resuelve la HU desde esta Issue
```

Entrega ACCEPTED, ACCEPTED_WITH_OBSERVATIONS o NOT_ACCEPTED, además del estado de implementación HU. Criterios/DoD obligatorios no verificados impiden aceptación; observaciones solo cubren mejoras no bloqueantes. No rechaza una PR correcta porque falte otra capa.

`references/acceptance.md` define matrices y algoritmo de decisión. `examples/synthetic-validation.md` permite ensayos sin acceso GitHub. Esta primera versión es un flujo operativo Markdown, sin automatizar ni sustituir la evaluación humana/funcional.

## Instalación y portabilidad

Copiar esta carpeta completa a `~/.codex/skills/` o al directorio de skills elegido. No requiere ninguna skill hermana ni archivos fuera de su carpeta. `openai.yaml` conserva la convención del repositorio; `agents/openai.yaml` contiene los mismos metadatos para entornos Codex que usan esa ubicación. Mantener ambas copias iguales.

Para asistentes sin soporte nativo, pegar `references/portable-prompt.md`; si tienen acceso a archivos, adjuntar SKILL.md y las referencias enlazadas para el detalle completo. El prompt portable contiene reglas operativas mínimas y URLs autoritativas.

## Fuentes y mantenimiento

Las referencias locales son procedimientos y resúmenes mínimos, no copias de manuales institucionales. Ver `references/institutional-sources.md` para las lecturas auditadas y enlaces vigentes; refrescar fuentes al ejecutar. Las reglas estables repetidas permiten instalación independiente; mantener términos y estados alineados al actualizar.

Esta versión solo lee GitHub o evidencias locales. No publica resultados, no modifica Developed y no hace commit/push. La ausencia de permisos se refleja como evidencia no verificada. GitHub MCP es opcional; gh es alternativa de lectura, no dependencia del razonamiento.
