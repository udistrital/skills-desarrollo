# peticion-http

Skill orientada a repositorios Go para estandarizar peticiones HTTP salientes usando `github.com/udistrital/utils_oas`.

## Qué hace

- Revisa integraciones HTTP salientes existentes.
- Detecta uso directo de `net/http` y wrappers locales redundantes.
- Guía la migración hacia `utils_oas`.
- Exige consistencia en verbos, contexto, headers, manejo de errores y cobertura repo-wide cuando aplique.

## Archivos de la skill

- `SKILL.md`: reglas e instrucciones principales.
- `openai.yaml`: metadatos y configuración para entornos OpenAI/Codex.
- `references/portable-prompt.md`: prompt portable para asistentes sin soporte nativo de skills.

## Instalación en Codex

Desde la raíz de este repositorio:

```bash
mkdir -p ~/.codex/skills
cp -r skills/peticion-http ~/.codex/skills/
```

## Uso

Ejemplo de invocación:

```text
Usa la skill peticion-http para revisar este repositorio.
```

O, si el entorno soporta referencia directa:

```text
$peticion-http
```

## Cuándo usarla

Úsala cuando necesites refactorizar, implementar o revisar integraciones HTTP salientes en APIs Go y debes hacer uso de `utils_oas` como estándar.
