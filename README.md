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
    └── peticion-http/
        ├── SKILL.md
        ├── openai.yaml
        └── references/
            └── portable-prompt.md
```

## Skills disponibles

| Skill | Descripción | Ruta |
|---|---|---|
| `peticion-http` | Estandariza peticiones HTTP salientes en APIs Go usando `github.com/udistrital/utils_oas`. | `skills/peticion-http/` |

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

## Skill incluida: `peticion-http`

Esta skill está orientada a repositorios Go y obliga a estandarizar integraciones HTTP salientes usando `github.com/udistrital/utils_oas`.

Archivos principales:

- `skills/peticion-http/SKILL.md`
- `skills/peticion-http/openai.yaml`
- `skills/peticion-http/references/portable-prompt.md`

## Cómo agregar una nueva skill

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
