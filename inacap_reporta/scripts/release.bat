@echo off
REM Script de release para Windows (desarrollo local)
REM Para Railway/Heroku, se usa release.sh

echo 🚀 Iniciando proceso de release...

echo ⏳ Esperando a que la base de datos esté disponible...
timeout /t 2 /nobreak >nul

echo 🔄 Ejecutando migraciones...
python manage.py migrate --noinput

echo 👤 Verificando superusuario...
python manage.py create_superuser_if_not_exists

echo ✅ Release completado exitosamente!

