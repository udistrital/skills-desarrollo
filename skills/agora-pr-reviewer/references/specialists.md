# Especialistas internos

Siempre documenta qué perspectivas se aplicaron y evidencia de arquitectura. Inspecciona únicamente el alcance del PR y dependencias necesarias; registra problemas preexistentes separadamente. Ningún especialista autoriza modificaciones.

## common-reviewer — siempre

- Issue asociada, HU original, criterios de aceptación por capa, alcance y posibles cambios ajenos a la HU. Contrastar DoR y DoD actuales, no presumir que checks marcados son prueba.
- GitFlow: feature desde develop y hacia develop; release desde develop, estabilización sin features y retorno a master/develop; hotfix desde producción con retorno de la corrección. Comprobar grafo/merge-base si disponible; el nombre de rama no prueba origen. Detectar nombre real de producción y excepciones documentadas.
- Commits: prefijos institucionales verificados en fuentes; `management` reservado a Master/Maintainer. Si el rol no es visible, marcar no verificado. No atribuir incumplimiento a commits heredados de base.
- Cambios, pruebas significativas (casos negativos y regresiones), resultados CI para head actual, checks requeridos y calidad/SonarQube. Un check ausente no es PASS. Separar fallo funcional de fallo de infraestructura.
- README: propósito, tecnologías/versiones, variables sin valores secretos, ejecución local/Docker, pruebas, CI, modelo y licencia según aplique. Contratos/documentación actualizados con el cambio.
- Seguridad: secretos/tokens/API keys/certificados, autenticación, autorización del lado servidor, roles/permisos, acceso a objetos de terceros, entradas, inyección/XSS, CORS, sesiones, errores sin filtraciones, configuración y dependencias. Contrastar alertas SonarQube/Dependabot y exposición real. No repetir secretos en el informe; indicar ubicación y remediación.
- Verificar necesidad de QA funcional/no funcional y evidencia de seguridad vigente. La revisión de código no suplanta la aprobación del equipo de Seguridad ni autoriza pruebas activas sobre servicios reales.
- Límites institucionales: localizar duplicaciones y citar evidencia, responsabilidad y excepción documentada. No declarar defecto solo por existir un modelo local con nombre parecido.

## crud-reviewer

Revisar persistencia, esquema relacional o Mongo realmente usado, migraciones up/down y compatibilidad con datos existentes, constraints/índices, consultas/paginación, acceso a datos, DTO/modelos, validación y serialización. Contrastar convenciones de datos aplicables, sin imponer tipos de PostgreSQL a Mongo.

Comprobar endpoints y semántica REST, códigos HTTP/errores, permisos, documentación OpenAPI vs implementación, tests, Docker/configuración y health check acorde al stack. No ejecutar migraciones contra bases reales.

**¿Quién consume este contrato nuevo o modificado?** Localizar MID/cliente y versión. Si no hay consumidor, registrar `PENDING`/`UNVERIFIED` como estado de solución. Una API entregada conforme al contrato acordado para desarrollo paralelo puede recibir APPROVE.

## mid-reviewer

Revisar orquestación, reglas de negocio derivadas de HU, transformaciones y validación; integración CRUD y servicios institucionales; WSO2 cuando corresponda; propagación de identidad/permisos, errores y cancelación/timeouts, resiliencia e idempotencia según operación. Verificar reintentos sin duplicar efectos y pruebas de fallos upstream.

Leer el contrato CRUD real (rutas, structs/DTO, OpenAPI y serialización) y cada llamada MID. Comparar también el contrato expuesto al FRONT. No asumir que nombres de structs iguales implican JSON igual. Localizar transformaciones y envelopes. Si falta repositorio upstream, señalar evidencia faltante.

## frontend-reviewer

Seguir escenarios de usuario y criterios de HU, consumo MID/API real, request/response, validación de formularios, estados loading/vacío/error/reintento, permisos visibles y rutas protegidas, accesibilidad aplicable (teclado, etiquetas, foco), mantenibilidad y pruebas de interacción. Ocultar un botón no reemplaza autorización del servidor. No aprobar una pantalla solo porque compila o usa mocks.

## microfrontend-reviewer — adicional a frontend

Detectar Single-SPA en package.json, exports/bootstrap/mount/unmount, entrypoints, configuración de build e import maps. Comprobar montaje repetido y limpieza de listeners/suscripciones/DOM al desmontar, routing/base path y coordinación con root-config; dependencias compartidas/versiones, aislamiento de estilos/estado, bundles duplicados y contratos de comunicación.

Inspeccionar uso real de `udistrital/web-components`: login, header/footer/menu/sidebar y WSO2, integración de roles. Detectar shell o autenticación duplicados; comprobar si corresponde al root/shared o a una excepción de transición. No exigir la estructura exacta de otro microfrontend.

## solution-reviewer — HU multirrepositorio

Dibujar ruta real `FRONT → MID → CRUD` y servicios institucionales (puede omitir capas). Para cada arista comparar matriz de contratos, versión requerida y entrega real. Buscar consumidor ausente, endpoint no usado, Issues desactualizadas respecto al código, PRs paralelos, campos/tipos/nulabilidad, transformación faltante, permisos, errores/status y paginación incompatibles.

Clasificar cada observación: `THIS_PR_DEFECT`, `OTHER_REPO_PENDING`, `PARALLEL_DEPENDENCY`, `UNVERIFIED`. Indicar repo responsable y consecuencia para HU. Un contrato incompatible asumido por este PR sí puede bloquearlo; el simple trabajo paralelo no. No adjudicar culpa si todavía falta definir el contrato: pedir resolución mediante COMMENT.
