# 🔧 Solución: Error psycopg2 con Python 3.13

## Problema

Render está usando **Python 3.13.4** pero:
- `psycopg2-binary==2.9.9` no es compatible con Python 3.13
- El proyecto está configurado para Python 3.11.0

## Solución: Forzar Python 3.11 en Render

El archivo `runtime.txt` está en `inacap_reporta/runtime.txt` pero Render necesita que esté en la **raíz** del repositorio O configurar manualmente.

### Opción 1: Mover runtime.txt a la raíz (Recomendado)

Render busca `runtime.txt` en la raíz del repositorio.

### Opción 2: Configurar Python 3.11 en Render Dashboard

1. Ve a: https://dashboard.render.com/web/srv-d4nq2ic9c44c73d3c1fg
2. Settings → **Environment**
3. Busca "Python Version" o agrega variable:
   - **Key:** `PYTHON_VERSION`
   - **Value:** `3.11.0`
4. Guarda

### Opción 3: Actualizar psycopg2-binary

Ya actualicé a `psycopg2-binary>=2.9.10`, pero la mejor solución es usar Python 3.11.

