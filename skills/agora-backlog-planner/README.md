# agora-backlog-planner

Convierte selección explícita de HU en plan técnico CRUD/MID/FRONT. El helper extrae y valida paquetes; el asistente construye los borradores finales con las plantillas actuales, estimaciones razonadas y DoR con evidencia.

```text
$agora-backlog-planner — usa project.json y run.json, genera borradores dry-run
```

Desde esta carpeta:

```bash
python3 scripts/prepare_backlog.py --config examples/project.example.json --run examples/run.example.json
python3 -B -m unittest discover -s tests -v
```

Python 3.10+; CSV no necesita paquetes. XLSX requiere openpyxl 3.x disponible en el entorno; el helper no instala dependencias. Tests XLSX se omiten con aviso cuando falta openpyxl. Solo JSON para configuración/ejecución. Los ejemplos son SINTÉTICOS/PROVISIONALES. `apply` falla incluso con una bandera enable_writes.

## Al recibir el Excel real

Confirmar hoja, fila de encabezados, nombres/formatos y tipos, ID estable, enlaces HU/anexos, presencia de tres columnas de repositorio y reglas de celdas vacías/combinadas/fórmulas. Ajustar `mapping.columns` en configuración; nunca reemplazarlo por una sola Repository_to_use. Confirmar semántica de Priority, Epic/Actividad, Sprint/assignee y capacidad. Validar localizador HU compartible, criterios originales y evidencia DoR; crear fixtures anonimizados solo si está autorizado.

Descubrir campos/tipos/IDs/opciones/iteraciones de Project 120 al ejecutar. No se fijan IDs internos. Aún faltan contrato operativo WSO2 y repositorio MID Terceros. Ninguno de estos pendientes habilita escrituras.

## Instalación y portabilidad

Copiar esta carpeta completa a `~/.codex/skills/` o al directorio de skills elegido. No requiere ninguna skill hermana ni archivos fuera de su carpeta. `openai.yaml` conserva la convención del repositorio; `agents/openai.yaml` contiene los mismos metadatos para entornos Codex que usan esa ubicación. Mantener ambas copias iguales.

Para asistentes sin soporte nativo, pegar `references/portable-prompt.md`; si tienen acceso a archivos, adjuntar SKILL.md y las referencias enlazadas para el detalle completo. El prompt portable contiene reglas operativas mínimas y URLs autoritativas.

## Fuentes y mantenimiento

Las referencias locales son procedimientos y resúmenes mínimos, no copias de manuales institucionales. Ver `references/institutional-sources.md` para las lecturas auditadas y enlaces vigentes; refrescar fuentes al ejecutar. Las reglas estables repetidas permiten instalación independiente; mantener términos y estados alineados al actualizar.

Esta versión solo lee GitHub o evidencias locales. No publica resultados, no modifica Developed y no hace commit/push. La ausencia de permisos se refleja como evidencia no verificada. GitHub MCP es opcional; gh es alternativa de lectura, no dependencia del razonamiento.
