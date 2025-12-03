#!/bin/bash
# Script de build para Railway/Heroku
# Este script se ejecuta automáticamente durante el despliegue

set -e  # Salir si hay algún error

echo "🔨 Iniciando proceso de build..."

# Instalar dependencias
echo "📦 Instalando dependencias..."
pip install -r requirements.txt

# Recopilar archivos estáticos
echo "📂 Recopilando archivos estáticos..."
python manage.py collectstatic --noinput

echo "✅ Build completado exitosamente!"


