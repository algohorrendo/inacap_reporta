# 🚀 Configuración para Render

## 📋 Comandos para Render

### Opción 1: Con Root Directory configurado (Recomendado)

Si configuras el **Root Directory** como `inacap_reporta` en Render:

#### Build Command:
```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

#### Start Command:
```bash
gunicorn inacap_reporta.wsgi --log-file -
```

#### Start Command (con variables de entorno):
```bash
gunicorn inacap_reporta.wsgi
```

---

### Opción 2: Sin Root Directory (Desde la raíz del repo)

Si NO configuras Root Directory y todo está en la raíz:

#### Build Command:
```bash
cd inacap_reporta && pip install -r requirements.txt && python manage.py collectstatic --noinput
```

#### Start Command:
```bash
cd inacap_reporta && gunicorn inacap_reporta.wsgi --log-file -
```

---

## 🔄 Release Command (Importante)

Render también necesita un **Release Command** para ejecutar migraciones y crear el superusuario automáticamente.

### Con Root Directory configurado:
```bash
python manage.py migrate --noinput && python manage.py create_superuser_if_not_exists
```

### Sin Root Directory:
```bash
cd inacap_reporta 
```

---

## 📍 Configuración en Render Dashboard

1. Ve a tu servicio web en Render
2. Settings → **Build Command**: Usa uno de los Build Command de arriba
3. Settings → **Start Command**: Usa uno de los Start Command de arriba
4. Settings → **Advanced** → **Release Command**: Usa uno de los Release Command de arriba

---

## ⚙️ Configuración Recomendada

### 1. Root Directory
En Settings → Root Directory, configura: `inacap_reporta`

### 2. Environment
- **Python Version**: `3.11.0` (según runtime.txt)

### 3. Build Command
```
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

### 4. Start Command
```
gunicorn inacap_reporta.wsgi
```

### 5. Release Command
```
python manage.py migrate --noinput && python manage.py create_superuser_if_not_exists
```

---

## 🔐 Variables de Entorno Necesarias

Agrega estas variables en Render → Environment:

- `SECRET_KEY` - Tu clave secreta de Django
- `DEBUG` - `False` para producción
- `ALLOWED_HOSTS` - Tu dominio de Render (ej: `tu-app.onrender.com`)
- `DATABASE_URL` - Se configurará automáticamente si conectas PostgreSQL
- `DJANGO_SUPERUSER_USERNAME` - (Opcional, default: `admin`)
- `DJANGO_SUPERUSER_EMAIL` - (Opcional, default: `admin@inacap.cl`)
- `DJANGO_SUPERUSER_PASSWORD` - (Opcional, default: `gato1234`)

---

## ✅ Verificación

Después del primer deploy:
1. Verifica que el build fue exitoso
2. Revisa los logs del Release Command para confirmar migraciones
3. Revisa que el superusuario se haya creado
4. Accede a `/admin/` con las credenciales por defecto


