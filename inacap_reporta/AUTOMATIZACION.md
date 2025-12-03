# Guía de Automatización

Este documento explica cómo funciona la automatización del build, migraciones y creación de superusuario.

## 🔄 Proceso Automatizado

El proyecto está configurado para automatizar los siguientes procesos durante el despliegue:

### 1. Build (Compilación)
- Instalación de dependencias (`pip install -r requirements.txt`)
- Recopilación de archivos estáticos (`collectstatic`)

### 2. Release (Pre-lanzamiento)
- Ejecución automática de migraciones (`migrate`)
- Creación automática de superusuario si no existe

### 3. Deploy (Despliegue)
- Inicio del servidor web con Gunicorn

## 📋 Configuración en Railway

Railway ejecutará automáticamente estos comandos en el siguiente orden:

1. **Build Phase**: Instalación de dependencias y recopilación de archivos estáticos
2. **Release Phase**: Migraciones y creación de superusuario
3. **Deploy Phase**: Inicio del servidor web

### Archivos de Configuración

- **`Procfile`**: Define los comandos de release y web
- **`railway.json`**: Configuración específica de Railway (si es necesario)

## 🔐 Variables de Entorno para Superusuario

Para configurar el superusuario automáticamente, agrega estas variables de entorno en Railway:

| Variable | Descripción | Requerido | Valor por Defecto |
|----------|-------------|-----------|-------------------|
| `DJANGO_SUPERUSER_USERNAME` | Nombre de usuario del admin | No | `admin` |
| `DJANGO_SUPERUSER_EMAIL` | Email del admin | No | `admin@inacap.cl` |
| `DJANGO_SUPERUSER_PASSWORD` | Contraseña del admin | **Sí (Recomendado)** | Se genera aleatoria |
| `DJANGO_SUPERUSER_FIRST_NAME` | Nombre del admin | No | `Administrador` |
| `DJANGO_SUPERUSER_LAST_NAME` | Apellido del admin | No | `INACAP` |

### Ejemplo de Configuración

En Railway, agrega estas variables en la sección "Variables":

```
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@inacap.cl
DJANGO_SUPERUSER_PASSWORD=TuContraseñaSegura123!
DJANGO_SUPERUSER_FIRST_NAME=Administrador
DJANGO_SUPERUSER_LAST_NAME=INACAP
```

⚠️ **IMPORTANTE**: Si no configuras `DJANGO_SUPERUSER_PASSWORD`, se generará una contraseña aleatoria que aparecerá en los logs. Deberás guardarla para poder iniciar sesión.

## 🛠️ Comando Personalizado

El proyecto incluye un comando de gestión personalizado:

### `create_superuser_if_not_exists`

Este comando crea un superusuario automáticamente solo si no existe uno.

**Uso manual:**
```bash
python manage.py create_superuser_if_not_exists
```

**Características:**
- Solo crea un superusuario si no existe ninguno
- Lee las credenciales de variables de entorno
- Genera una contraseña aleatoria si no se proporciona una
- Es seguro ejecutarlo múltiples veces

## 📝 Scripts Incluidos

### Para Linux/Mac (Railway/Heroku)
- `scripts/build.sh`: Script de build
- `scripts/release.sh`: Script de release

### Para Windows (Desarrollo local)
- `scripts/build.bat`: Script de build
- `scripts/release.bat`: Script de release

## 🔍 Verificar que Funciona

Después de desplegar en Railway:

1. **Verifica los logs del Build**
   - Deberías ver: "📦 Instalando dependencias..."
   - Deberías ver: "📂 Recopilando archivos estáticos..."

2. **Verifica los logs del Release**
   - Deberías ver: "🔄 Ejecutando migraciones..."
   - Deberías ver: "👤 Verificando superusuario..."
   - Deberías ver: "✅ Superusuario creado exitosamente!" o "⚠️ Ya existe un superusuario"

3. **Prueba iniciar sesión**
   - Ve a `/admin/`
   - Usa las credenciales que configuraste

## 🐛 Solución de Problemas

### El superusuario no se crea

1. Verifica que las variables de entorno estén configuradas
2. Revisa los logs del release phase en Railway
3. Verifica que no haya errores en la conexión a la base de datos

### Las migraciones fallan

1. Verifica que la base de datos esté configurada correctamente
2. Asegúrate de que `DATABASE_URL` esté configurada en Railway
3. Revisa los logs para ver el error específico

### El build falla

1. Verifica que todas las dependencias estén en `requirements.txt`
2. Revisa que la versión de Python sea compatible
3. Verifica los logs de build para más detalles

## 📚 Más Información

- Ver `RAILWAY.md` para instrucciones de despliegue
- Ver `VARIABLES_ENTORNO.md` para todas las variables de entorno


