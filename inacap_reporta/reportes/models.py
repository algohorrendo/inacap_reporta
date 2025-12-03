from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)


    class Meta:
        db_table = 'categoria'
    
    def __str__(self):
        return self.nombre


class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    sector = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        db_table = 'ubicacion'
    
    def __str__(self):
        return self.sector


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    rol = models.CharField(max_length=14)


    class Meta:
        db_table = 'usuario'
    
    def __str__(self):
        return self.nombre


class Incidencia(models.Model):
    # Definir choices para estado
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('progreso', 'En Progreso'),
        ('resuelto', 'Resuelto'),
        ('cerrado', 'Cerrado'),
    ]
    
    id_incidencia = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200, default='Sin título')  # Agregamos título
    descripcion = models.CharField(max_length=400)
    fecha_reporte = models.DateTimeField(default=timezone.now)
    imagen = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')
    
    # Campos existentes
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_ubicacion = models.ForeignKey(Ubicacion, models.DO_NOTHING, db_column='id_ubicacion')
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria')
    
    # Nuevo campo para conectar con Django auth
    django_user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    
    # Campos adicionales que necesitamos
    urgencia = models.CharField(max_length=10, default='media')
    ubicacion_texto = models.CharField(max_length=100, blank=True, null=True)  # Para ubicación en texto
    categoria_texto = models.CharField(max_length=50, blank=True, null=True)   # Para categoría en texto
    
    # ← AGREGAR ESTA LÍNEA AQUÍ:
    foto = models.ImageField(upload_to='incidencias/', blank=True, null=True)


    class Meta:
        db_table = 'incidencia'
        ordering = ['-fecha_reporte']
    
    def __str__(self):
        return f"{self.titulo} - {self.django_user.username if self.django_user else 'Sin usuario'}"


class Respuesta(models.Model):
    id_respuesta = models.AutoField(primary_key=True)
    comentario = models.CharField(max_length=350)
    fecha = models.DateTimeField()
    id_incidencia = models.ForeignKey(Incidencia, models.DO_NOTHING, db_column='id_incidencia')
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')


    class Meta:
        db_table = 'respuesta'


# ==================== MODELO ROL ====================

class Rol(models.Model):
    """
    Modelo para gestionar Roles de usuarios
    Categorías: Estudiante o Encargado
    """
    CATEGORIAS = [
        ('estudiante', 'Estudiante'),
        ('encargado', 'Encargado'),
    ]
    
    nombre = models.CharField(
        max_length=50,
        choices=CATEGORIAS,
        unique=True,
        help_text="Categoría del rol"
    )
    descripcion = models.TextField(
        blank=True,
        help_text="Descripción del rol"
    )
    usuarios = models.ManyToManyField(
        User,
        related_name='roles',
        blank=True,
        help_text="Usuarios asignados a este rol"
    )
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.get_nombre_display()} ({self.usuarios.count()} usuarios)"
    
    def get_nombre_display(self):
        """Obtiene el nombre legible del rol"""
        return dict(self.CATEGORIAS).get(self.nombre, self.nombre)


# ==================== SIGNAL: Asignar rol automáticamente ====================

@receiver(post_save, sender=User)
def asignar_rol_usuario(sender, instance, created, **kwargs):
    """
    Signal que asigna automáticamente un rol cuando se crea un usuario
    - SuperUser o Staff → ENCARGADO
    - Usuario normal → ESTUDIANTE
    """
    if created:
        try:
            if instance.is_staff or instance.is_superuser:
                # Es Encargado
                rol = Rol.objects.get(nombre='encargado')
                rol.usuarios.add(instance)
            else:
                # Es Estudiante
                rol = Rol.objects.get(nombre='estudiante')
                rol.usuarios.add(instance)
        except Rol.DoesNotExist:
            # Si los roles no existen aún, no hace nada
            pass