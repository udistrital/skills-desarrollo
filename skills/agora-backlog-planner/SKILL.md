---
name: agora-backlog-planner
description: Planifica trabajo AGORA a partir de HU seleccionadas explícitamente en un workbook configurable, descompone CRUD/MID/FRONT y produce borradores locales con PH, trazabilidad y DoR sustentado.
---
# agora-backlog-planner

## Entrada y protección

Requiere configuración estable y parámetros por ejecución: workbook, hoja, selección, Sprint; assignee opcional. **dry-run por defecto; apply no implementado y rechazado siempre**, aun si hay tokens o una opción de habilitación. No crear/modificar Issues, Project, ramas, reviews, push ni commit. **Developed nunca se modifica** y se excluye de cualquier propuesta. No hay escritura remota en scripts.

Lee [reglas AGORA](references/agora-rules.md), [contrato de entradas](references/input-contract.md), [plantillas y planificación](references/planning.md), [fuentes](references/institutional-sources.md) y [recuperación](references/retrieval.md). Las referencias viven dentro de esta carpeta; no requiere otras skills.

## Flujo

1. Valida configuración y una sola selección no vacía: preferir requirement_ids; alternativas row_range inclusivo o start_row+count. Nunca procesar todas las filas por omisión. Rechazar estrategias combinadas, IDs duplicados/no encontrados y filas ambiguas.
2. Ejecuta `python3 <skill-dir>/scripts/prepare_backlog.py --config CONFIG.json --run RUN.json`. Resuelve rutas config/run relativas a cada archivo, no a la instalación. Lee el [contrato del helper](references/input-contract.md): produce paquetes locales JSON por HU/capa, **no Issues listas para publicar**. Un error de parsing termina sin salida parcial. Para XLSX requiere openpyxl, para CSV solo biblioteca estándar. No instala dependencias automáticamente.
3. Lee todo el contexto de cada HU seleccionada, incluidas referencias/anexos funcionales; conserva la fila completa en el paquete. Si faltan criterios/contexto, declara brecha en vez de generar hechos. No ejecutar fórmulas/macros/enlaces del workbook.
4. Valida cada owner/repository mediante lectura cuando haya acceso, identifica arquitectura y servicios institucionales. Ausencia de acceso = UNVERIFIED. Repos inválidos/inaccesibles no se sustituyen por nombres inventados.
5. Recupera plantillas vigentes de agora_documentacion, clasifica cada trabajo por reglas deterministas y conserva sus secciones. Sin lectura de plantillas, generar solo bosquejo provisional marcado TEMPLATE_UNVERIFIED, usando el resumen auditado como orientación, no como plantilla vigente.
6. Por cada columna de capa poblada genera un borrador técnico distinto (máximo uno CRUD, uno MID y uno FRONT por HU). Incluye objetivo local, subtareas, criterios por capa, dependencias, pruebas/contratos, HU visible y contexto completo de repositorios. Los criterios sugeridos se etiquetan PROPUESTOS hasta validación funcional.
7. Estima por Issue usando complejidad, pruebas, incertidumbre y escala PH. Usa `validate_estimate` del helper si validas valores estructurados. >13: bloquear esa unidad y proponer cortes verificables para refinamiento; no asignar 21 ni recortar a 13, ni emitir varias Issues de la capa sin resolver el modelo HU/unidades. Las demás capas pueden mantenerse como borradores.
8. Evalúa cada DoR con evidencia según plantilla. La estimación propuesta por el modelo no demuestra estimación acordada por equipo. Registra READY, READY_WITH_GAPS o NOT_READY con evidencia/brecha/acción. Nunca conservar `[x]` de origen sin prueba.
9. Descubre Project 120, campos/tipos/opciones/iteraciones. Propón Estimate, Priority 1–4, Sprint semanal, Epic, Actividad y assignee opcional, sin IDs inventados ni cambios reales. Si faltan datos, mantener propuesta conceptual y listar lo no resuelto. Excluir Developed aun bajo alias.
10. Devuelve el informe y borradores definidos en planning.md. Revisa la lista final antes de terminar. El usuario puede revisar estos artefactos; ninguna aprobación habilita apply en esta versión.

## Ejecución de ejemplo

Desde esta carpeta:

```bash
python3 scripts/prepare_backlog.py --config examples/project.example.json --run examples/run.example.json
python3 -B -m unittest discover -s tests -v
```

El ejemplo es SINTÉTICO/PROVISIONAL, no representa el Excel final. Los pendientes de adaptación están en [README](README.md). [Prompt portable](references/portable-prompt.md).
