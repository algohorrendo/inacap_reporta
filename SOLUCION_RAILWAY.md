# Solución de Error "error creating build plan with nixpack"

Si estás recibiendo este error en Railway, sigue estos pasos:

## 🔧 Solución 1: Configurar Root Directory en Railway

El problema más común es que Railway no sabe dónde está tu proyecto Django.

### Pasos:

1. Ve a tu proyecto en Railway
2. Selecciona el servicio web (no la base de datos)
3. Ve a la pestaña **"Settings"**
4. Busca la sección **"Root Directory"**
5. Configura: `inacap_reporta` (la subcarpeta donde está tu proyecto)
6. Guarda los cambios
7. Haz un nuevo deploy

## 🔧 Solución 2: Mover archivos de configuración

Si la Solución 1 no funciona, también puedes configurar Railway manualmente:

### En Railway Dashboard:

1. **Build Command:**
   ```
   cd inacap_reporta && pip install -r requirements.txt && python manage.py collectstatic --noinput
   ```

2. **Start Command:**
   ```
   cd inacap_reporta && gunicorn inacap_reporta.wsgi --log-file -
   ```

3. **Release Command:**
   ```
   cd inacap_reporta && python manage.py migrate --noinput && python manage.py create_superuser_if_not_exists
   ```

## 🔧 Solución 3: Simplificar la estructura

Si sigues teniendo problemas, otra opción es que Railway detecte automáticamente el proyecto.

### Verificar que estos archivos existan:

- ✅ `inacap_reporta/requirements.txt` - Debe existir
- ✅ `inacap_reporta/manage.py` - Debe existir  
- ✅ `inacap_reporta/Procfile` - Debe existir
- ✅ `inacap_reporta/runtime.txt` - Debe existir

## 📋 Configuración Recomendada en Railway

### Root Directory
```
inacap_reporta
```

### Build Command (si Root Directory está configurado)
```
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

### Start Command (si Root Directory está configurado)
```
gunicorn inacap_reporta.wsgi --log-file -
```

### Release Command (si Root Directory está configurado)
```
python manage.py migrate --noinput && python manage.py create_superuser_if_not_exists
```

## ⚠️ Notas Importantes

1. **Root Directory** es la configuración más importante - debe apuntar a `inacap_reporta`

2. Si usas **Root Directory**, los comandos NO necesitan `cd inacap_reporta` porque ya estás en esa carpeta

3. El archivo `Procfile` debe estar dentro de `inacap_reporta/` y NO necesita `cd`

## 🆘 Si Nada Funciona

1. Elimina el servicio actual en Railway
2. Crea un nuevo servicio
3. Conecta tu repositorio de GitHub
4. Configura el **Root Directory** ANTES del primer deploy
5. Agrega las variables de entorno
6. Conecta la base de datos PostgreSQL
7. Haz el deploy

## 📞 Verificar Logs

Si el build falla, revisa los logs en Railway:
- Ve a tu servicio
- Pestaña "Deployments"
- Click en el deployment fallido
- Revisa los logs de "Build" y "Deploy"

Los logs te dirán exactamente qué está fallando.


