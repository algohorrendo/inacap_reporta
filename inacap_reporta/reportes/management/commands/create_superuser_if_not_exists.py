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

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Forzar la actualización del superusuario si ya existe',
        )

    def handle(self, *args, **options):
        # Obtener credenciales de variables de entorno con valores por defecto
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@inacap.cl')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'gato1234')
        force = options.get('force', False)
        
        # Verificar si el usuario ya existe
        try:
            user = User.objects.get(username=username)
            if user.is_superuser:
                if force:
                    # Actualizar el usuario existente
                    user.email = email
                    user.set_password(password)
                    user.first_name = os.environ.get('DJANGO_SUPERUSER_FIRST_NAME', 'Administrador')
                    user.last_name = os.environ.get('DJANGO_SUPERUSER_LAST_NAME', 'INACAP')
                    user.is_staff = True
                    user.is_superuser = True
                    user.save()
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'✅ Superusuario "{username}" actualizado exitosamente!'
                        )
                    )
                    self.stdout.write(f'   Email: {email}')
                    self.stdout.write(
                        self.style.SUCCESS(f'   Usuario: {username} / Contraseña: {password}')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            f'⚠️  Ya existe un superusuario con el nombre "{username}".'
                        )
                    )
                    self.stdout.write(
                        self.style.WARNING(
                            '   Usa --force para actualizar las credenciales.'
                        )
                    )
                    return
            else:
                # El usuario existe pero no es superusuario, convertirlo
                user.is_staff = True
                user.is_superuser = True
                user.email = email
                user.set_password(password)
                user.first_name = os.environ.get('DJANGO_SUPERUSER_FIRST_NAME', 'Administrador')
                user.last_name = os.environ.get('DJANGO_SUPERUSER_LAST_NAME', 'INACAP')
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        f'✅ Usuario "{username}" convertido a superusuario exitosamente!'
                    )
                )
                self.stdout.write(f'   Email: {email}')
                self.stdout.write(
                    self.style.SUCCESS(f'   Usuario: {username} / Contraseña: {password}')
                )
        except User.DoesNotExist:
            # El usuario no existe, crearlo
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
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error: {str(e)}')
            )
