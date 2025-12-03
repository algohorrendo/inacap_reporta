#!/bin/bash
set -e

echo "🔨 Building application..."

# Install dependencies (Nixpacks should do this automatically, but just in case)
if [ -f "requirements.txt" ]; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
fi

# Collect static files
echo "📂 Collecting static files..."
cd inacap_reporta
python manage.py collectstatic --noinput

echo "✅ Build completed!"

