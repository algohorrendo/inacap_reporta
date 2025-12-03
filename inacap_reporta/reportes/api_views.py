from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.db.models import Count, Avg, Q
from django.utils import timezone
from datetime import timedelta
from .serializers import IncidenciaSerializer
from .models import Incidencia, Categoria

class IncidenciaViewSet(viewsets.ModelViewSet):
    serializer_class = IncidenciaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Incidencia.objects.all()
        return Incidencia.objects.filter(django_user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(django_user=self.request.user)


@api_view(['GET'])
@permission_classes([])  # Permitir acceso sin autenticación REST, verificamos manualmente
def dashboard_stats(request):
    """Endpoint para obtener estadísticas del dashboard"""
    # Verificar autenticación y permisos manualmente (usando autenticación de sesión de Django)
    if not request.user.is_authenticated:
        return Response({'error': 'No autenticado'}, status=status.HTTP_401_UNAUTHORIZED)
    if not request.user.is_staff:
        return Response({'error': 'No autorizado'}, status=status.HTTP_403_FORBIDDEN)
    
    # Incidencias por mes (últimos 12 meses)
    from django.db.models.functions import TruncMonth
    incidencias_por_mes = Incidencia.objects.annotate(
        mes=TruncMonth('fecha_reporte')
    ).values('mes').annotate(
        total=Count('id_incidencia')
    ).order_by('mes')[:12]
    
    meses = []
    totales = []
    for item in incidencias_por_mes:
        meses.append(item['mes'].strftime('%Y-%m') if item['mes'] else 'N/A')
        totales.append(item['total'])
    
    # Incidencias por categoría
    incidencias_por_categoria = Incidencia.objects.values(
        'id_categoria__nombre', 'categoria_texto'
    ).annotate(
        total=Count('id_incidencia')
    )
    
    categorias = []
    categoria_totales = []
    for item in incidencias_por_categoria:
        cat_name = item['categoria_texto'] or item['id_categoria__nombre'] or 'Sin categoría'
        categorias.append(cat_name)
        categoria_totales.append(item['total'])
    
    # Tiempo promedio de resolución (en días)
    incidencias_resueltas = Incidencia.objects.filter(estado='resuelto')
    tiempos_resolucion = []
    
    for incidencia in incidencias_resueltas:
        # Calcular tiempo desde fecha_reporte hasta ahora (o fecha de cambio a resuelto)
        # Como no hay campo fecha_resolucion, usamos fecha_reporte como aproximación
        # En producción, deberías agregar un campo fecha_resolucion
        tiempo = (timezone.now() - incidencia.fecha_reporte).days
        if tiempo > 0:
            tiempos_resolucion.append(tiempo)
    
    tiempo_promedio = sum(tiempos_resolucion) / len(tiempos_resolucion) if tiempos_resolucion else 0
    
    # Incidencias por estado
    incidencias_por_estado = Incidencia.objects.values('estado').annotate(
        total=Count('id_incidencia')
    )
    
    estados = []
    estado_totales = []
    for item in incidencias_por_estado:
        estados.append(item['estado'])
        estado_totales.append(item['total'])
    
    # Incidencias por urgencia
    incidencias_por_urgencia = Incidencia.objects.values('urgencia').annotate(
        total=Count('id_incidencia')
    )
    
    urgencias = []
    urgencia_totales = []
    for item in incidencias_por_urgencia:
        urgencias.append(item['urgencia'])
        urgencia_totales.append(item['total'])
    
    return Response({
        'incidencias_por_mes': {
            'meses': meses,
            'totales': totales
        },
        'incidencias_por_categoria': {
            'categorias': categorias,
            'totales': categoria_totales
        },
        'tiempo_promedio_resolucion': round(tiempo_promedio, 2),
        'incidencias_por_estado': {
            'estados': estados,
            'totales': estado_totales
        },
        'incidencias_por_urgencia': {
            'urgencias': urgencias,
            'totales': urgencia_totales
        },
        'total_incidencias': Incidencia.objects.count(),
        'incidencias_pendientes': Incidencia.objects.filter(estado='pendiente').count(),
        'incidencias_resueltas': Incidencia.objects.filter(estado='resuelto').count(),
    })