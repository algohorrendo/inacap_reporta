from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)

    class Meta:
        db_table = 'categoria'

class Incidencia(models.Model):
    id_incidencia = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=400)
    fecha_reporte = models.DateTimeField()
    estado = models.CharField(
        max_length=10,
        choices=[
            ('pendiente', 'Pendiente'),
            ('en_proceso', 'En Proceso'),
            ('resuelta', 'Resuelta'),
            ('rechazada', 'Rechazada'),
        ],
        default='pendiente'
    )
    id_usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    id_ubicacion = models.ForeignKey('ubicaciones.Ubicacion', on_delete=models.RESTRICT)
    id_categoria = models.ForeignKey('incidencias.Categoria', on_delete=models.RESTRICT)

    class Meta:
        db_table = 'incidencia'

class Respuesta(models.Model):
    id_respuesta = models.AutoField(primary_key=True)
    respuesta = models.CharField(max_length=350)
    fecha = models.DateTimeField()
    id_incidencia = models.ForeignKey('incidencias.Incidencia', on_delete=models.CASCADE)
    id_usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)

    class Meta:
        db_table = 'respuesta'

