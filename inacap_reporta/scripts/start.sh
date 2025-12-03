#!/bin/bash
# Script de inicio que ejecuta migraciones y crea superusuario antes de iniciar el servidor
# Este script se ejecuta en cada inicio del servicio

set -e

echo "🚀 Iniciando aplicación..."

# Ejecutar migraciones (solo si la base de datos está disponible)
echo "🔄 Ejecutando migraciones..."
python manage.py migrate --noinput || echo "⚠️  Error en migraciones, continuando..."

# Crear superusuario si no existe (solo la primera vez)
echo "👤 Verificando superusuario..."
python manage.py create_superuser_if_not_exists || echo "⚠️  Error al crear superusuario, continuando..."

# Iniciar servidor
echo "🌐 Iniciando servidor Gunicorn..."
PORT=${PORT:-10000}
exec gunicorn inacap_reporta.wsgi --log-file - --bind 0.0.0.0:$PORT

