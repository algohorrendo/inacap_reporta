#!/bin/bash
# Script de release para Railway
# Este script se ejecuta automáticamente después del build y antes de iniciar el servidor

set -e  # Salir si hay algún error

echo "🚀 Iniciando proceso de release..."

# Esperar a que la base de datos esté lista (importante en Railway)
echo "⏳ Esperando a que la base de datos esté disponible..."
sleep 2

# Ejecutar migraciones
echo "🔄 Ejecutando migraciones..."
python manage.py migrate --noinput

# Crear superusuario automáticamente si no existe
echo "👤 Verificando superusuario..."
python manage.py create_superuser_if_not_exists

echo "✅ Release completado exitosamente!"



