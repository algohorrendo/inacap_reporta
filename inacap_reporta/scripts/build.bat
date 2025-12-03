@echo off
REM Script de build para Windows (desarrollo local)
REM Para Railway/Heroku, se usa build.sh

echo 🔨 Iniciando proceso de build...

echo 📦 Instalando dependencias...
pip install -r requirements.txt

echo 📂 Recopilando archivos estáticos...
python manage.py collectstatic --noinput

echo ✅ Build completado exitosamente!

