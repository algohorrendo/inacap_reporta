# Generated migration to create initial superuser
import os
from django.db import migrations
from django.conf import settings


def create_initial_superuser(apps, schema_editor):
    """Crea el superusuario inicial si no existe"""
    # Usar apps.get_model para obtener el modelo User en el contexto de la migración
    User = apps.get_model(settings.AUTH_USER_MODEL)
    
    # Obtener credenciales de variables de entorno con valores por defecto
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@inacap.cl')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'gato1234')
    
    # Verificar si el usuario ya existe
    if not User.objects.filter(username=username).exists():
        # Crear superusuario usando create_superuser del manager
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            first_name=os.environ.get('DJANGO_SUPERUSER_FIRST_NAME', 'Administrador'),
            last_name=os.environ.get('DJANGO_SUPERUSER_LAST_NAME', 'INACAP'),
        )


def reverse_create_superuser(apps, schema_editor):
    """Elimina el superusuario inicial (opcional, para rollback)"""
    User = apps.get_model(settings.AUTH_USER_MODEL)
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
    try:
        user = User.objects.get(username=username)
        if user.is_superuser:
            user.delete()
    except User.DoesNotExist:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),  # Asegurar que auth migrations estén aplicadas
        ('reportes', '0004_usuarioreportador_rol'),
    ]

    operations = [
        migrations.RunPython(create_initial_superuser, reverse_create_superuser),
    ]

