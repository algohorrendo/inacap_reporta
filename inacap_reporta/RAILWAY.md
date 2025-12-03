# Guía de Despliegue en Railway

Este documento explica cómo desplegar el proyecto INACAP Reporta en Railway.

## Prerrequisitos

1. Una cuenta en [Railway](https://railway.app)
2. Un repositorio Git del proyecto (GitHub, GitLab, etc.)

## Pasos para Desplegar

### 1. Preparar el Repositorio

Asegúrate de que todos los archivos necesarios estén en tu repositorio:
- `Procfile`
- `runtime.txt`
- `requirements.txt`
- `manage.py`
- Todo el código del proyecto

### 2. Crear un Proyecto en Railway

1. Ve a [Railway Dashboard](https://railway.app/dashboard)
2. Click en "New Project"
3. Selecciona "Deploy from GitHub repo" (o tu proveedor de Git)
4. Selecciona tu repositorio

### 3. Configurar la Base de Datos

Railway recomienda usar PostgreSQL. Necesitas:

1. En tu proyecto de Railway, click en "+ New"
2. Selecciona "Database" → "Add PostgreSQL"
3. Railway creará automáticamente una base de datos PostgreSQL

### 4. Configurar Variables de Entorno

En tu servicio web de Railway, ve a la pestaña "Variables" y agrega:

#### Variables Requeridas:

- `SECRET_KEY`: Genera una clave secreta segura (puedes usar: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
- `DEBUG`: Establece en `False` para producción
- `ALLOWED_HOSTS`: Tu dominio de Railway (ejemplo: `tu-app.railway.app`)
- `DATABASE_URL`: Se configura automáticamente si conectas el servicio de PostgreSQL

#### Variables Opcionales:

- `CORS_ALLOWED_ORIGINS`: Dominios permitidos para CORS (separados por comas)

### 5. Conectar la Base de Datos

1. En tu servicio PostgreSQL, ve a la pestaña "Connect"
2. Copia la variable `DATABASE_URL`
3. En tu servicio web, agrega esta variable en "Variables"

Railway debería detectar automáticamente la conexión si ambos servicios están en el mismo proyecto.

### 6. Configurar el Build y Deploy

Railway debería detectar automáticamente que es un proyecto Django. Verifica:

1. **Root Directory**: Debe apuntar a la carpeta `inacap_reporta/` si tu proyecto está en una subcarpeta
2. **Build Command**: Debería ser algo como:
   ```bash
   pip install -r requirements.txt && python manage.py collectstatic --noinput
   ```
3. **Start Command**: Debería usar el Procfile que ya creamos

### 7. Ejecutar Migraciones

Después del primer despliegue:

1. Ve a tu servicio en Railway
2. Click en la pestaña "Deployments"
3. Click en el deployment más reciente
4. Ve a la pestaña "Logs"
5. O usa el CLI de Railway para ejecutar:
   ```bash
   railway run python manage.py migrate
   ```

### 8. Crear un Superusuario (Opcional)

Para acceder al panel de administración:

```bash
railway run python manage.py createsuperuser
```

O usa la terminal de Railway en el dashboard.

## Notas Importantes

### Archivos Estáticos

El proyecto usa WhiteNoise para servir archivos estáticos en producción. Los archivos se recopilan automáticamente durante el build con `collectstatic`.

### Media Files (Imágenes de Incidencias)

Para archivos de media en producción, considera usar un servicio de almacenamiento como:
- AWS S3
- Cloudinary
- Railway Volumes (para archivos persistentes)

### Actualización del Proyecto

Cada vez que hagas push a tu repositorio, Railway desplegará automáticamente los cambios.

## Solución de Problemas

### Error de Base de Datos

- Verifica que `DATABASE_URL` esté configurada correctamente
- Asegúrate de que las migraciones se hayan ejecutado

### Error 500

- Revisa los logs en Railway Dashboard
- Verifica que `DEBUG=False` en producción
- Asegúrate de que `ALLOWED_HOSTS` incluya tu dominio

### Archivos Estáticos no se cargan

- Verifica que `collectstatic` se ejecute durante el build
- Revisa la configuración de WhiteNoise en settings.py

## Soporte

Para más información sobre Railway, visita la [documentación oficial](https://docs.railway.app).


