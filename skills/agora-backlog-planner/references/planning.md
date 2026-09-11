# Planificación y borradores

## Selección de plantilla

Consultar directorio y leer contenido vigente; guardar URL/blob/fecha. Selección por naturaleza del trabajo, por Issue:

1. Analyst si el entregable es análisis/diseño/documentación de solución sin implementación productiva.
2. Developer Plus si hay implementación y al menos una necesidad comprobada de contrato entre repositorios, migración/modelo de datos, integración institucional/WSO2, decisión arquitectónica/Single-SPA, escenario de seguridad o especificación de pruebas detallada.
3. Developer para implementación acotada con criterios claros y sin disparadores Plus.

No clasificar todas como Plus solo por pertenecer a una HU multirrepositorio: comprobar si el trabajo cambia el contrato o requiere esa especificación. Informar señal usada y confianza. Si no se sabe si el entregable es diseño o código, marcar CLASSIFICATION_UNCERTAIN y bosquejar opciones sin presumir plantilla final. Revalidar si cambia el catálogo remoto; estas reglas seleccionan categorías, no IDs eternos.

Mantener secciones reales de plantilla (subtareas, criterios, requerimientos, DoR/DoD y extras Plus). Eliminar metadatos YAML de plantilla del cuerpo de Issue, preservando su clasificación como propuesta. Reemplazar instrucciones vacías con contenido evidenciado o una brecha visible; no dejar `No aplica` cuando existan requerimientos reales. Reconstruir checkboxes DoR según evidencia; DoD empieza sin marcar salvo evidencia ya existente.

## Responsabilidades por capa

- CRUD: persistencia/esquema/migraciones, constraints, validación de datos, contrato CRUD y errores, pruebas de consultas/persistencia, documentación y salud. No trasladar aquí reglas de negocio del MID sin justificación.
- MID: reglas de HU, orquestación/transformation, consumo CRUD e institucional, contrato para FRONT, permisos/validación y fallos upstream; escenarios de integración.
- FRONT: escenarios funcionales, formularios, consumo MID, estados loading/vacío/error, accesibilidad y permisos UI. Si Single-SPA, ciclo de vida/routing e integración con shell compartido, sin duplicar login/menu institucional.

Conservar el mismo propósito funcional y especificar descripción, criterios y pruebas distintos. No inventar endpoints/DTO; contratos desconocidos son entregables por definir. Distinguir dependencia de contrato de dependencia de despliegue; trabajo paralelo puede usar contrato acordado y mocks identificados, pero no se declara integrado hasta probar extremos reales.

## Traza visible en cada borrador

```markdown
### Historia de Usuario de origen
**HU:** HU-ID
**Detalle funcional:** [Consultar HU original](URL_CONFIRMADA)
```

Si no hay URL directa, mostrar `**Referencia funcional:** workbook URL/ruta; hoja; HU ID; fila/referencia` (no un enlace falso). Marcar accesibilidad pendiente si solo existe ruta local. Falta de traza completa bloquea creación real futura, sin impedir mostrar borrador con advertencia.

Añadir `### Contexto de la solución` con CRUD/MID/FRONT presentes y sus owner/repository; `### Issues relacionadas` con URLs existentes o `pendiente de creación (clave local HU:CAPA)`. Añadir dependencia, razón, contrato/evidencia y estado. Nunca fabricar números #123 para propuestas. Cuando existan Issues en una futura versión, resolver claves locales a URLs y proponer actualización recíproca idempotente conservando el enlace HU.

## Campos y Sprint

Leer configuración, HU y parámetros de ejecución. Por cada campo registrar concepto, valor propuesto, origen/razón, nombre/ID/tipo descubierto, opción/iteración resuelta o UNVERIFIED. Priority solo 1–4 antes de mapear a opción real, sin suponer qué significa cada número. Epic/Actividad desde HU/mapeo, no inventados. Sprint consume valor solicitado y valida fechas/duración semanal. Assignee opcional; no inferir capacidad sin datos. No incluir Developed en la tabla de cambios, solo como contexto si es relevante.

## Informe dry-run final

- Fuente workbook/hoja, selección efectiva (IDs y filas) y advertencia de ejemplos sintéticos.
- Grafo HU → paquetes/Issues CRUD/MID/FRONT → repositorios → feature branch propuesta desde develop → PR futuro (sin crear ninguno).
- Por Issue: título propuesto con HU/capa; plantilla con fuente y confianza; cuerpo completo por plantilla; criterios locales trazados a criterios HU; pruebas; dependencias y enlaces de solución.
- Estimate por Issue, justificación y certeza; >13 como DECOMPOSE sin valor asignado y con propuesta de cortes para refinamiento.
- DoR: ítem → estado → evidencia/fecha → brecha → próxima acción; estado global. Criterios de equipo no se dan por probados mediante estimación IA.
- Mapeo de campos y propuestas conceptuales, sin Developed; faltantes de permisos/opciones/capacidad.
- Problemas BLOCKER/MAJOR/MINOR/SUGGESTION, supuestos y pendientes; distinguir error del workbook, insuficiencia funcional y dato GitHub no verificado.
- Resumen: borradores generados, unidades bloqueadas para futura creación, siguiente refinamiento. Ningún borrador es Issue real.

## Guarded apply futuro (solo diseño)

No existe interruptor habilitable en esta versión. Una implementación futura requerirá código nuevo y autorización explícita para acciones concretas, plan revisable completo, traza accesible, DoR/brechas visibles, estimaciones válidas, campos descubiertos y lista permitida que excluya Developed por nombre e ID. Antes de crear: buscar duplicados por HU/capa/repositorio. Registrar resultados parciales, reanudar por identificadores reales y actualizar hermanos sin recrear Issues; no borrar automáticamente para revertir errores. MCP/CLI serán adaptadores separados de la planificación.

## Lista final

- Selección única validada, todas y solo las HU pedidas; Excel provisional identificado.
- Contexto completo y traza visible en cada borrador; ninguna URL/Issue inventada.
- Repositorios existentes o estado UNVERIFIED, máximo un borrador por capa, cuerpos especializados.
- Plantilla leída y clasificación explicada; criterios distinguibles entre HU y propuesta.
- PH válidos o descomposición; DoR real sin marcas heredadas y DoD sin pruebas fabricadas.
- Dependencias/contratos, Priority, Sprint, Epic, Actividad y assignee gestionados con origen.
- Developed excluido; dry-run y cero escrituras; apply rechazado.
