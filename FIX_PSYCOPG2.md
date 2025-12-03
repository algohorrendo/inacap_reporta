# 🔧 Fix: Error de psycopg2 con Python 3.13

## Problema

Render está usando Python 3.13.4 y `psycopg2-binary==2.9.9` no es compatible.

**Error:**
```
Error loading psycopg2 module: undefined symbol: _PyInterpreterState_Get
```

## Solución: Forzar Python 3.11 en Render

El archivo `runtime.txt` especifica Python 3.11.0, pero Render lo está ignorando.

### En Render Dashboard:

1. Ve a tu servicio: https://dashboard.render.com/web/srv-d4nq2ic9c44c73d3c1fg
2. Settings → **Environment**
3. Busca o agrega variable:
   - **Key:** `PYTHON_VERSION`
   - **Value:** `3.11.0`
4. Guarda

### Alternativa: Actualizar psycopg2

Ya actualicé `requirements.txt` para usar `psycopg2-binary>=2.9.10`.

Pero la mejor solución es **forzar Python 3.11** como está en `runtime.txt`.

