"""
Comando de gestión de Django para crear un superusuario automáticamente
si no existe uno. Usa variables de entorno para configurar las credenciales.
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()


class Command(BaseCommand):
    help = 'Crea un superusuario automáticamente si no existe uno. Usa variables de entorno.'

    def handle(self, *args, **options):
        # Obtener credenciales de variables de entorno con valores por defecto
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@inacap.cl')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'gato1234')
        
        # Verificar si ya existe un superusuario
        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write(
                self.style.WARNING('⚠️  Ya existe un superusuario. No se creará otro.')
            )
            return
        
        try:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
                first_name=os.environ.get('DJANGO_SUPERUSER_FIRST_NAME', 'Administrador'),
                last_name=os.environ.get('DJANGO_SUPERUSER_LAST_NAME', 'INACAP'),
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f'✅ Superusuario "{username}" creado exitosamente!'
                )
            )
            self.stdout.write(f'   Email: {email}')
            self.stdout.write(
                self.style.SUCCESS(f'   Usuario: {username} / Contraseña: {password}')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error al crear superusuario: {str(e)}')
            )
