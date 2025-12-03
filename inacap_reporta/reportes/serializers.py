from rest_framework import serializers
from .models import Incidencia, Categoria, Ubicacion

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion 
        fields = '__all__'

class IncidenciaSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(source='id_categoria', read_only=True)
    ubicacion = UbicacionSerializer(source='id_ubicacion', read_only=True)
    
    class Meta:
        model = Incidencia
        fields = ['id_incidencia', 'titulo', 'descripcion', 'fecha_reporte', 
                 'estado', 'urgencia', 'foto', 'categoria', 'ubicacion']