# ⚡ Configuración Rápida para Railway

## 📍 Paso 1: Configurar Root Directory (IMPORTANTE)

1. En Railway Dashboard, selecciona tu servicio web
2. Ve a **Settings** → **Root Directory**
3. Configura: `inacap_reporta`
4. Guarda

## 📍 Paso 2: Configurar Comandos Manualmente (Opcional)

Si prefieres configurar los comandos manualmente:

### Build Command:
```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

### Start Command:
```bash
gunicorn inacap_reporta.wsgi --log-file -
```

### Release Command (en Settings → Deploy):
```bash
python manage.py migrate --noinput && python manage.py create_superuser_if_not_exists
```

## ✅ Con Root Directory configurado, NO necesitas `cd inacap_reporta` en los comandos

Railway ya estará ejecutando los comandos dentro de la carpeta `inacap_reporta/`.

