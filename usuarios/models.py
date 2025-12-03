from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    rol = models.CharField(max_length=14)

    class Meta:
        db_table = 'usuario'
id_usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
id_ubicacion = models.ForeignKey('ubicaciones.Ubicacion', on_delete=models.RESTRICT)
id_categoria = models.ForeignKey('incidencias.Categoria', on_delete=models.RESTRICT)
