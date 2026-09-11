# Fuentes institucionales y vigencia

Auditadas por lectura `gh api` el 2026-09-11. Árbol de lineamientos_oas consultado: `ee307b6236450e57f81483dda3c552d6d44468c5`. Estos enlaces siguen la rama vigente auditada; descubrir rama por defecto y volver a leer al usar la skill. Registrar SHA/fecha de lo realmente leído. Si hay conflicto entre fuentes, citarlo y resolver aplicabilidad por stack/versión; no prescribir actualizaciones o defectos sin evidencia.

Base: https://github.com/udistrital/lineamientos_oas

| Tema | Fuente relativa a `https://github.com/udistrital/lineamientos_oas/blob/master/` | Regla mínima / uso |
|---|---|---|
| GitFlow | repositorios_institucionales/nombre_branch.md | feature develop→develop; release desde develop, estabilización y retorno master/develop; hotfix desde master y retorno |
| Commits | repositorios_institucionales/etiqueta_commits.md | feat, fix, docs, test, refactor, devops, management; management exclusivo Master/Maintainer |
| Repositorios | repositorios_institucionales/nombre_repos.md | minúsculas negocio_contexto; detectar arquitectura real, incluidos mf modernos |
| README | repositorios_institucionales/contenido_readme.md | propósito, tecnología, entorno, ejecución, tests, CI, modelo y licencia |
| Endpoints | generacion_de_apis/lineamientos-endpoints.md | español sin acentos, minúsculas, guiones, recursos sin verbos CRUD; semántica HTTP y errores |
| Health check | generacion_de_apis/endpoint_validacions.md | revisar mecanismo de salud; ejemplo Beego usa apiStatusLib |
| Datos relacionales | modelo_de_datos/lineamientos_modelos_relacionales.md | nombres singulares snake_case, referencias _id, constraints, activo/fechas; revisar tipos aplicables |
| Mongo | modelo_de_datos/lineamientos_mongo.md | modelado por consultas, referencias/embebidos, índices, convenciones de campos |
| Docker | ambientes_dockerizados/dockerizacion.md | Dockerfile y docker-compose.yml en raíz del componente desplegable |
| QA | qa/definicion.md y qa/requerimiento_pruebas.md | funcional/no funcional, repos/ramas/ambiente, historias y manuales; verificar umbrales vigentes |
| Seguridad | qa/validación_seguridad.md | secretos, identidad/permisos, entradas, APIs/errores, SonarQube, Dependabot, OWASP según riesgo |
| Unit tests Beego | pruebas_unitarias_api_beego/unit_test_beego.md | priorizar lógica personalizada crítica; consultar también crud_test.md y paso_parametro_test_mid.md cuando aplique |
| Single-SPA | single_spa/single_spa.md, single_spa/root_config.md, single_spa/shared.md | ciclo de vida, root/routing, aislamiento e intercambio de datos |
| CI/CD | generacion_de_apis/configuracion_ci_cd.md | configuración por stack, .drone.yml y sonar-project.properties; validar checks del SHA revisado |

Son rutas verificadas, no copias de manuales. Para citarlas construir la URL completa con el prefijo indicado; recuperar documentos adicionales enlazados cuando el cambio lo requiera. Ejemplos antiguos de CORS, versiones o almacenamiento no son exenciones de seguridad. No recoger credenciales en informes aunque la guía QA solicite accesos para otro proceso.

## Plantillas actuales AGORA

Directorio autoritativo: https://github.com/udistrital/agora_documentacion/tree/master/.github/ISSUE_TEMPLATE

| Plantilla | Archivo | Blob auditado |
|---|---|---|
| Analyst | template-for-analyst-.md | 7c8e6a0241f0baf6c09595c1adaa4590d6f0a0eb |
| Developer | template-for-developer-.md | 649d9174affe4a8552c95ce29804546498d5cd7d |
| Developer Plus | template-for-developer-plus.md | 63b50de8ff7896cf6acb6cdb3936445033e84095 |

Analyst: subtareas, criterios, requerimientos; DoR descripción/criterios de análisis-diseño, sin bloqueos y documentación disponible/entendible. DoD criterios, documentación, aprobación SM/líder/SoSM y artefacto satisfactorio.

Developer: subtareas, criterios, requerimientos; DoR refinada/estimada por equipo, detalle funcional/técnico claro, sin bloqueos, dependencias identificadas/resueltas, comprobable dentro del Sprint. DoD desarrollo local, push feature, pruebas funcionales locales, PR develop, criterios, documentación y aprobación SM/líder. Son evidencias a inspeccionar, no acciones autorizadas.

Plus añade escenarios de pruebas, material de apoyo, especificaciones y secciones de lineamientos generales/microclientes/microservicios/modelos/tests; comparte DoR/DoD de Developer. **Las tres plantillas traen DoR premarcado**: reconstruir marcas por evidencia. Plus enlaza `modelo_de_datos/estandar.md`, ausente del árbol auditado; usar `lineamientos_modelos_relacionales.md` y reportar corrección de referencia, conservando la estructura de plantilla.

## Responsabilidades institucionales (contexto AGORA)

- https://github.com/udistrital/autenticacion_mid — autenticación, usuarios y roles institucionales.
- https://github.com/udistrital/configuracion_api — aplicaciones, procesos, perfiles/configuración/permisos.
- https://github.com/udistrital/terceros_crud — terceros/personas/proveedores. MID Terceros: configurable/por descubrir; **no inventar repositorio**.
- https://github.com/udistrital/oikos_api — espacios físicos/dependencias.
- https://github.com/udistrital/parametros_crud — parámetros/catálogos institucionales.
- https://github.com/udistrital/web-components — README verificado: header, sidebar, footer, login y autenticación WSO2; usar responsabilidades compartidas según versión real.
- WSO2 API Gateway: exposición, clientes y control de acceso; reglas operativas AGORA pendientes de precisar, no inventar configuración.

Consultar README/contratos reales de cada servicio involucrado antes de concluir duplicación. Estas responsabilidades son señales de revisión con contexto, no defectos automáticos.

Project: https://github.com/orgs/udistrital/projects/120/views/1 — organización udistrital, número 120. IDs, nombres exactos, opciones/iteraciones y permisos no auditados en esta implementación; se descubren en ejecución. Developed siempre solo lectura.
