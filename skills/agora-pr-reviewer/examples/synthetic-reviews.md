# Casos exclusivamente SINTÉTICOS

Estos casos son ejercicios de comportamiento, no requisitos ni PRs reales. Completar evidencia local positiva significa que todos los criterios locales y checks requeridos en head están demostrados; no implica cierre funcional.

| Entrada sintética | Evidencia | Resultado esperado |
|---|---|---|
| CRUD listo, MID consumidor pendiente | HU y contrato acordado enlazados; evidencia local positiva; MID Issue pendiente confirmada | PR APPROVE; HU PARTIALLY_IMPLEMENTED; consumidor PENDING |
| MID consume respuesta CRUD incorrecta | Contrato acordado/CRUD devuelve `data`; MID usa `items` sin transformar | MAJOR THIS_PR_DEFECT; REQUEST_CHANGES; HU IN_PROGRESS |
| MID correcto, FRONT incompatible | MID cumple contrato acordado `data`; FRONT abierto usa `items` | MID APPROVE con evidencia local positiva; defecto atribuido a FRONT; HU PARTIALLY_IMPLEMENTED |
| PR correcto; otras dos capas sin implementar | Criterios locales comprobados y hermanos identificados | APPROVE no equivale a COMPLETE |
| PR sin HU original | Solo “closes #7”; Issue #7 no contiene localizador HU; búsquedas acotadas no resuelven | COMMENT; trazabilidad UNVERIFIED; no inventar HU |
| PR sin productor accesible | MID usa `items`; CRUD privado no legible y contrato no disponible | COMMENT por evidencia esencial; no inventar MISMATCH |
| PR antiguo aprobado | Head cambió y CI corresponde al anterior | COMMENT hasta revisar cambios y checks actuales |

Ensayo manual: entregar solo entradas/evidencias al asistente con SKILL.md, pedir informe y comprobar dos decisiones independientes, clasificación y ausencia de acciones remotas. Para un ensayo de código real se deben aportar archivos mínimos de ambos extremos y sus referencias; esta tabla no acredita una revisión real.
