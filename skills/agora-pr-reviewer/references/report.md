# Formato del informe local

1. Identificación: PR URL, repo, base/head SHA, fecha, alcance, fuentes y especialistas aplicados.
2. Trazabilidad: HU ID + enlace original/localizador completo; Issue por capa; repositorios; ramas/PRs y SHA; vínculos confirmados vs inferidos; enlaces ausentes y búsquedas realizadas.
3. Responsabilidad local: criterio técnico → código → prueba/CI → PASS/FAIL/UNVERIFIED/N/A (motivo). DoR y DoD por ítem con evidencia y brechas.
4. Solución: grafo de capas y servicios institucionales; matriz de contratos; pendientes de otras capas, dependencias paralelas, Issues desactualizadas y efecto funcional.
5. Hallazgos ordenados por severidad, sin duplicar el mismo defecto entre especialistas:

| ID | Severidad | Clasificación | Archivo:línea@SHA | Evidencia | HU/criterio o estándar URL | Impacto | Corrección recomendada |
|---|---|---|---|---|---|---|---|

- `BLOCKER`: impide integrar/operar con seguridad, pérdida de datos o fallo crítico demostrado.
- `MAJOR`: incumplimiento funcional/contractual sustancial o riesgo relevante demostrado.
- `MINOR`: defecto acotado que no impide la responsabilidad local.
- `SUGGESTION`: mejora opcional, no una obligación inventada.

Si no hay línea fiable, usa ruta y símbolo; no inventes líneas de diff. Las limitaciones de acceso/CI se registran aparte y pueden exigir COMMENT sin ser un defecto probado.

6. Evidencia disponible y faltante: checks con SHA/fecha, tests ejecutados vs solamente leídos, alcance de QA/seguridad y preguntas concretas.
7. Termina con dos campos independientes y su justificación:

**PR decision:** APPROVE | COMMENT | REQUEST_CHANGES

**HU implementation status:** NOT_STARTED | PARTIALLY_IMPLEMENTED | IN_PROGRESS | IMPLEMENTED_PENDING_VALIDATION | COMPLETE

Estos son resultados de informe; no se publican. Explica qué impide completar la HU aunque el PR sea aprobable. Si HU no puede resolverse, usa IN_PROGRESS como estado provisional basado en el PR existente y declara que no se pudo establecer cobertura total; nunca COMPLETE.
