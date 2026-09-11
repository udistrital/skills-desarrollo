# skills-desarrollo

Repositorio de skills reutilizables para asistentes de IA orientados a tareas de desarrollo de software.

Cada skill vive en su propia carpeta dentro de `skills/` y, como base, incluye:

- `SKILL.md`: instrucciones principales de la skill.
- `openai.yaml`: metadatos y prompt auxiliar para entornos OpenAI/Codex.
- `references/portable-prompt.md`: versión portable para asistentes sin soporte nativo de skills.

## Objetivo

Centralizar skills reutilizables para tareas técnicas frecuentes, de forma que puedan instalarse, copiarse o adaptarse en distintos asistentes sin duplicar instrucciones.

## Estructura del repositorio

```text
skills-desarrollo/
├── README.md
├── .gitignore
└── skills/
    ├── agora-pr-reviewer/
    ├── agora-backlog-planner/
    ├── agora-story-validator/
    └── peticion-http/
        ├── SKILL.md
        ├── openai.yaml
        └── references/
            └── portable-prompt.md
```

## Skills disponibles

| Skill | Descripción | Ruta |
|---|---|---|
| `peticion-http` | Estandariza peticiones HTTP salientes en APIs Go usando. | `skills/peticion-http/` |
| `agora-pr-reviewer` | Revisa PRs, trazabilidad HU y contratos entre capas; solo informe local. | [Documentación](skills/agora-pr-reviewer/README.md) |
| `agora-backlog-planner` | Planifica HU seleccionadas con mapeo provisional de Excel y dry-run. | [Documentación](skills/agora-backlog-planner/README.md) |
| `agora-story-validator` | Valida aceptación de HU con evidencia por criterio y DoD por repositorio. | [Documentación](skills/agora-story-validator/README.md) |

## Requisitos mínimos por skill

Cada skill publicada en este repositorio debe incluir como mínimo:

```text
nombre-skill/
├── SKILL.md
├── openai.yaml
└── references/
    └── portable-prompt.md
```

## Instalación

### Clonar el repositorio completo

```bash
git clone https://github.com/udistrital/skills-desarrollo.git
cd skills-desarrollo
```

### Instalar una skill en Codex

Para instalar una sola skill en el entorno local de Codex:

```bash
mkdir -p ~/.codex/skills
cp -r skills/peticion-http ~/.codex/skills/
```

### Instalar varias skills en Codex

Para copiar todas las skills disponibles del repositorio:

```bash
mkdir -p ~/.codex/skills
cp -r skills/* ~/.codex/skills/
```

### Uso sin instalación

Si el asistente no soporta skills nativas, usar alguno de estos archivos:

- `skills/<nombre-skill>/SKILL.md`
- `skills/<nombre-skill>/references/portable-prompt.md`

## Uso

### En Codex

Después de instalar la skill, invocarla por su nombre:

```text
Usa la skill peticion-http para revisar este repositorio.
```

Si el entorno soporta nombres con prefijo, también puede llamarse como:

```text
$peticion-http
```

### En Claude Code u otros asistentes con soporte similar

Copiar la carpeta de la skill al directorio de skills del asistente y luego llamarla por nombre según el mecanismo del entorno.

### En ChatGPT, Copilot u otros asistentes sin soporte nativo

1. Abrir `SKILL.md` o `references/portable-prompt.md`.
2. Copiar el contenido.
3. Pegarlo en el chat.
4. Indicar el repositorio, archivo o problema a trabajar.

Ejemplo:

```text
Usa esta skill para revisar y refactorizar las peticiones HTTP salientes del repositorio.
No cierres la tarea hasta cumplir las reglas y criterios definidos.
```


## Agregar una nueva skill

Crear la estructura base:

```bash
mkdir -p skills/nueva-skill/references
touch skills/nueva-skill/SKILL.md
touch skills/nueva-skill/openai.yaml
touch skills/nueva-skill/references/portable-prompt.md
```

Luego:

1. Documentar la nueva skill.
2. Agregarla a la tabla de `Skills disponibles`.
3. Verificar que el nombre de carpeta, el `name:` del `SKILL.md` y cualquier referencia invocable usen exactamente el mismo identificador.

## Convención de nombres

Usar nombres en minúscula y separados por guiones:

- `peticion-http`
- `migracion-go`
- `revision-angular`
- `auditoria-sql`
- `documentacion-issues`

## Recomendaciones antes de publicar nuevas versiones

- Verificar que cada skill tenga sus tres archivos base.
- Confirmar que los nombres invocables coincidan con el nombre de carpeta.
- Evitar referencias rotas en README o prompts.
- Mantener ejemplos de instalación y uso actualizados.

## Uso de las skills AGORA

```text
$agora-pr-reviewer owner/repository#123 — genera un informe local
$agora-backlog-planner — usa project.json y run.json para las HU seleccionadas
$agora-story-validator HU-ID — valida con su enlace o localizador configurado
```

Estos identificadores son ejemplos de formato. La entrada del revisor es una PR; el validador también puede partir de una Issue para descubrir la HU. La HU es la fuente funcional y cada Issue describe trabajo específico de CRUD, MID o FRONT. La aprobación recomendada de una PR es independiente de la aceptación de la HU completa.

Las tres skills son independientes y solo producen artefactos locales. No escriben en GitHub; **Developed siempre es solo lectura**. El planificador rechaza `apply` por código. Las plantillas y lineamientos se consultan desde sus repositorios autoritativos; no se fijan IDs internos de Project. El Excel final aún no existe: la configuración y los datos de ejemplo están marcados como provisionales/sintéticos.

Cada skill AGORA incluye `agents/openai.yaml` además del `openai.yaml` de esta convención, con contenido idéntico para compatibilidad de metadatos Codex. No necesita instalar las otras dos ni `peticion-http`.

### Comprobación local del planificador

```bash
python3 skills/agora-backlog-planner/scripts/prepare_backlog.py \
  --config skills/agora-backlog-planner/examples/project.example.json \
  --run skills/agora-backlog-planner/examples/run.example.json
python3 -B -m unittest discover -s skills/agora-backlog-planner/tests -v
```

La extracción CSV usa biblioteca estándar; XLSX necesita `openpyxl` 3.x. El helper produce paquetes para planificación, no cuerpos finales de Issues; la skill completa descripción, plantilla, criterios, estimación y DoR mediante evidencia. Los ejercicios de revisión y aceptación están en los respectivos directorios `examples/` y son ensayos manuales, no validaciones de PRs/HU reales.

Pendientes de adopción: workbook definitivo y localizadores HU compartibles, opciones/tipos reales de Project 120, capacidad/asignaciones, repositorio MID Terceros y reglas operativas WSO2 específicas de AGORA. El detalle de adaptación del Excel está en el README del planificador.
