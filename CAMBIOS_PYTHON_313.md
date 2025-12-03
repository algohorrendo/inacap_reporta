# ✅ Cambios para Python 3.13

## Problema resuelto:
`psycopg2-binary` no es compatible con Python 3.13.

## Solución aplicada:

### 1. `inacap_reporta/requirements.txt`
- ❌ Eliminado: `psycopg2-binary==2.9.9`
- ✅ Agregado: `psycopg[binary]>=3.2.0` (compatible con Python 3.13)
- ✅ Actualizado: `Django>=4.2.0,<5.0` (soporta psycopg3)

### 2. `render.yaml`
- ✅ Configurado: `PYTHON_VERSION=3.13`

### 3. Eliminado `runtime.txt` de la raíz
- Render usará Python 3.13 según `render.yaml`

## ¿Por qué funciona?
- `psycopg3` (psycopg[binary]) es compatible con Python 3.13
- Django 4.2+ soporta psycopg3 nativamente
- El backend `django.db.backends.postgresql` detecta automáticamente psycopg3

## Próximo paso:
Hacer commit y push. Render usará Python 3.13 automáticamente.

