from django.db import models

class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    sector = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'ubicacion'
id_usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
id_ubicacion = models.ForeignKey('ubicaciones.Ubicacion', on_delete=models.RESTRICT)
id_categoria = models.ForeignKey('incidencias.Categoria', on_delete=models.RESTRICT)