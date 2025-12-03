# 🔧 Guía: Actualizar Render SIN usar Shell

## ✅ Paso 1: Actualizar Build Command

1. Ve a: https://dashboard.render.com/web/srv-d4nq2ic9c44c73d3c1fg
2. Haz clic en **"Settings"** (Configuración)
3. Busca la sección **"Build Command"**
4. **BORRA todo** y pega esto:

```
cd inacap_reporta && pip install -r requirements.txt && python manage.py collectstatic --noinput
```

5. Haz clic en **"Save Changes"** (Guardar cambios)

---

## ✅ Paso 2: Configurar Release Command

1. En la misma página de **Settings**
2. Ve hacia abajo y busca **"Advanced"**
3. Expande la sección **"Advanced"**
4. Busca **"Release Command"**
5. Pega esto:

```
cd inacap_reporta && python manage.py migrate --noinput && python manage.py create_superuser_if_not_exists
```

6. Haz clic en **"Save Changes"**

---

## ✅ Paso 3: (Opcional) Configurar Root Directory

Para simplificar los comandos:

1. En **Settings**, busca **"Root Directory"**
2. Escribe: `inacap_reporta`
3. Si haces esto, los comandos se simplifican a:

   **Build Command:**
   ```
   pip install -r requirements.txt && python manage.py collectstatic --noinput
   ```

   **Release Command:**
   ```
   python manage.py migrate --noinput && python manage.py create_superuser_if_not_exists
   ```

4. Haz clic en **"Save Changes"**

---

## ✅ Paso 4: Verificar Variables de Entorno

Asegúrate de tener estas variables en **Settings → Environment**:

- `SECRET_KEY` - (Debes tenerla configurada)
- `DEBUG` - `False`
- `ALLOWED_HOSTS` - `inacap-reporta.onrender.com`
- `DATABASE_URL` - (Se configura automáticamente con PostgreSQL)

---

## ✅ Paso 5: Trigger Manual Deploy

Después de guardar los cambios:

1. Ve a la pestaña **"Manual Deploy"**
2. O simplemente haz un pequeño cambio y push a GitHub (Render detectará automáticamente)

---

## 🎯 Resumen de Cambios Necesarios

### Build Command (ACTUALIZAR):
```
cd inacap_reporta && pip install -r requirements.txt && python manage.py collectstatic --noinput
```

### Release Command (AGREGAR):
```
cd inacap_reporta && python manage.py migrate --noinput && python manage.py create_superuser_if_not_exists
```

---

## ⚠️ IMPORTANTE

El Build Command actual tiene esto (ESTÁ MAL):
```
... && python manage.py migrate --noinput && python manage.py create_superuser_if_not_exists
```

**DEBES ELIMINAR** esas dos partes del Build Command y ponerlas en el Release Command.

---

## 📸 Ruta Rápida

1. https://dashboard.render.com/web/srv-d4nq2ic9c44c73d3c1fg
2. Click en **Settings**
3. Actualiza **Build Command** (elimina migraciones)
4. Ve a **Advanced** → Agrega **Release Command**
5. Guarda todo

¡Eso es todo! No necesitas shell, todo se hace desde el dashboard web.


