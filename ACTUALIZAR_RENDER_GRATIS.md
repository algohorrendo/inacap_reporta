# 💰 Configuración de Render GRATIS (Sin Release Command)

Como el Release Command es de pago, usaremos un script de inicio que ejecute las migraciones y cree el superusuario automáticamente.

## ✅ Configuración SIN Release Command

### Build Command:
```
cd inacap_reporta && pip install -r requirements.txt && python manage.py collectstatic --noinput
```

### Start Command:
```
cd inacap_reporta && bash scripts/start.sh
```

**O si prefieres todo en una línea:**

```
cd inacap_reporta && python manage.py migrate --noinput && python manage.py create_superuser_if_not_exists && gunicorn inacap_reporta.wsgi
```

---

## 📋 Pasos para Actualizar en Render

### 1. Actualizar Build Command

1. Ve a: https://dashboard.render.com/web/srv-d4nq2ic9c44c73d3c1fg
2. Click en **"Settings"**
3. Busca **"Build Command"**
4. Cambia a:

```
cd inacap_reporta && pip install -r requirements.txt && python manage.py collectstatic --noinput
```

5. **IMPORTANTE:** Elimina las migraciones y crear superusuario del Build Command
6. Click en **"Save Changes"**

---

### 2. Actualizar Start Command

1. En la misma página de **Settings**
2. Busca **"Start Command"**
3. Cambia a una de estas opciones:

**Opción A (usando script - recomendado):**
```
cd inacap_reporta && bash scripts/start.sh
```

**Opción B (todo en una línea):**
```
cd inacap_reporta && python manage.py migrate --noinput && python manage.py create_superuser_if_not_exists && gunicorn inacap_reporta.wsgi
```

4. Click en **"Save Changes"**

---

## ⚠️ Importante

- Las migraciones se ejecutarán en **cada inicio** del servicio (pero solo aplicarán las nuevas)
- El superusuario solo se creará **si no existe** (gracias al comando `create_superuser_if_not_exists`)
- Esto funciona perfectamente en el plan GRATIS de Render

---

## 🎯 Resumen Rápido

**Build Command:**
```
cd inacap_reporta && pip install -r requirements.txt && python manage.py collectstatic --noinput
```

**Start Command:**
```
cd inacap_reporta && python manage.py migrate --noinput && python manage.py create_superuser_if_not_exists && gunicorn inacap_reporta.wsgi
```

---

## ✅ Verificación

Después de guardar los cambios, Render hará un nuevo deploy. En los logs deberías ver:

1. ✅ Build exitoso
2. ✅ Migraciones ejecutadas
3. ✅ Superusuario creado (o mensaje de que ya existe)
4. ✅ Servidor iniciado

---

**No necesitas shell ni Release Command. Todo funciona con el plan GRATIS.**

