# Contrato configurable de entrada — EXAMPLE / PROVISIONAL

No existe Excel definitivo. Los nombres de examples son solo demostrativos, no letras/columnas institucionales finales. JSON se usa para evitar dependencia YAML; es compatible conceptualmente con el esquema YAML solicitado. El helper acepta JSON, no YAML.

## Configuración estable

`github.organization`, `project_number`, `templates_repository`; `estimation.allowed_points` debe ser exactamente [1,2,3,5,8,13]; `project_fields.developed_is_read_only` debe ser true. No admite banderas para habilitar escrituras. `mapping.header_row` es número físico 1-based; `mapping.columns` mapea conceptos a encabezados reales únicos. Requeridos: requirement_id, description, crud_repository, mid_repository, front_repository. Opcionales: hu_source_link, epic, activity, priority y más contexto. No usar Repository_to_use. `services.terceros_mid_repository` permanece null hasta identificación explícita.

Mapear siempre las tres columnas de repositorio aunque haya celdas vacías. Validar esquema/encabezados aunque se seleccionen pocas filas; solo generar paquetes para la selección explícita. El contexto completo incluye todas las columnas con encabezado. Celdas con contenido sin encabezado son error, para no perder contexto silenciosamente.

## Parámetros por ejecución

- `workbook`: ruta local CSV UTF-8 o XLSX, relativa al JSON de ejecución o absoluta.
- `sheet`: nombre exacto (también etiqueta de la hoja exportada CSV).
- `workbook_source`: URL/ruta de origen opcional; una ruta local más hoja/ID/fila sirve como localizador, pero no garantiza acceso de desarrolladores.
- `selection`: exactamente una de `{requirement_ids: ["HU-034"]}`, `{row_range: {start: 53, end: 61}}`, `{start_row: 53, count: 5}`. Números físicos 1-based incluyendo encabezado; count cuenta filas físicas. No saltar vacías dentro de rango: reportarlas como error para evitar selección inesperada.
- `sprint`: título/identificador solicitado, no ID GitHub supuesto.
- `assignee`: login opcional; asignación y capacidad quedan por validar.
- `mode`: omitido equivale a dry-run; cualquier otro modo falla, incluido apply.

IDs: texto no vacío, únicos en workbook y selección. IDs con ceros deben venir como texto; no reconstruir formatos de Excel. Rechazar fórmulas en filas seleccionadas y en columna ID (también fuera de selección, para validar unicidad), celdas combinadas que afecten datos seleccionados y encabezados duplicados. No evaluar fórmulas ni usar resultados cacheados como actuales. Otras filas se leen solo para resolver selección/identidad, nunca se convierten en borradores.

## Salida del helper

JSON a stdout, no archivos remotos: mode, synthetic (solo ejemplo), source, selection, requirements. Por HU: ID, descripción, full_context, localizador original, repositorios, paquetes de capa, gaps. Cada paquete tiene clave local `HU:CAPA`, repositorio, responsabilidad guía, referencias hermanas locales, Estimate null y campos conceptuales. No inventa subtareas, criterios, plantilla, PH, DoR o IDs GitHub. El agente completa esas decisiones siguiendo planning.md; esta separación evita convertir extracción mecánica en planificación ficticia.

La traza tiene tipo DIRECT_LINK o COMPOSITE_REFERENCE. Sin URL HU directa se compone workbook_source (o ruta), hoja, ID y fila. Con ruta local se advierte ACCESSIBILITY_UNVERIFIED; para creación real futura debe demostrarse que los desarrolladores pueden localizar y leer la HU. Sin localizador reconstruible, TRACEABILITY_MISSING bloquea creación y se muestra en dry-run.

`validate_estimate(value)` acepta enteros institucionales o devuelve DECOMPOSE para entero >13; rechaza bool, floats y otros valores. La descomposición es decisión de refinamiento, no saturación numérica.

## Dependencia opcional

Python 3.10+; XLSX usa openpyxl 3.x instalado en el entorno por su responsable. CSV y tests básicos no necesitan paquetes. Fallar con mensaje específico si openpyxl no está; no convertir automáticamente el archivo ni cambiar selección. XLSX no habilita macros, no calcula fórmulas y se abre solo lectura.
