# Variables de Entorno

Este archivo lista todas las variables de entorno que necesitas configurar para el proyecto.

## Variables Requeridas

### SECRET_KEY
Clave secreta de Django. En producción, debe ser una cadena aleatoria y segura.

**Generar una nueva clave:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Ejemplo:**
```
SECRET_KEY=django-insecure-abc123xyz...
```

### DEBUG
Indica si el proyecto está en modo de depuración. En producción debe ser `False`.

**Valores posibles:**
- `True` - Modo desarrollo (muestra errores detallados)
- `False` - Modo producción (oculta errores)

**Ejemplo:**
```
DEBUG=False
```

### ALLOWED_HOSTS
Lista de dominios/hosts permitidos, separados por comas. En Railway, usa tu dominio.

**Ejemplo:**
```
ALLOWED_HOSTS=tu-app.railway.app,localhost,127.0.0.1
```

## Variables de Base de Datos

### DATABASE_URL (Recomendado para Railway)
URL completa de conexión a la base de datos. Railway la proporciona automáticamente cuando conectas un servicio PostgreSQL.

**Formato:**
```
DATABASE_URL=postgresql://usuario:contraseña@host:puerto/nombre_db
```

**Nota:** Si usas `DATABASE_URL`, las siguientes variables se ignoran.

### Variables Individuales (Para desarrollo local)

#### DB_ENGINE
Motor de base de datos a usar.

**Valores posibles:**
- `django.db.backends.mysql` - MySQL
- `django.db.backends.postgresql` - PostgreSQL

**Ejemplo:**
```
DB_ENGINE=django.db.backends.postgresql
```

#### DB_NAME
Nombre de la base de datos.

**Ejemplo:**
```
DB_NAME=inacap_reporta
```

#### DB_USER
Usuario de la base de datos.

**Ejemplo:**
```
DB_USER=postgres
```

#### DB_PASSWORD
Contraseña de la base de datos.

**Ejemplo:**
```
DB_PASSWORD=mi_contraseña_segura
```

#### DB_HOST
Host de la base de datos.

**Ejemplo:**
```
DB_HOST=localhost
```

#### DB_PORT
Puerto de la base de datos.

**Ejemplo para PostgreSQL:**
```
DB_PORT=5432
```

**Ejemplo para MySQL:**
```
DB_PORT=3306
```

## Variables Opcionales

### CORS_ALLOWED_ORIGINS
Lista de orígenes permitidos para CORS, separados por comas.

**Ejemplo:**
```
CORS_ALLOWED_ORIGINS=https://tu-dominio.com,http://localhost:8000
```

## Configuración en Railway

1. Ve a tu proyecto en Railway
2. Selecciona tu servicio web
3. Ve a la pestaña "Variables"
4. Agrega cada variable con su valor
5. Guarda los cambios

Railway aplicará los cambios automáticamente y redesplegará tu aplicación.

## Configuración Local

Para desarrollo local, crea un archivo `.env` en la raíz del proyecto (`inacap_reporta/.env`) con las variables necesarias:

```env
SECRET_KEY=tu-secret-key-local
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_ENGINE=django.db.backends.mysql
DB_NAME=inacap_reporta
DB_USER=root
DB_PASSWORD=admin
DB_HOST=localhost
DB_PORT=3306
```

**Importante:** Agrega `.env` a tu `.gitignore` para no subir información sensible al repositorio.


