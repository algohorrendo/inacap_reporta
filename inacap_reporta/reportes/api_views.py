from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import IncidenciaSerializer
from .models import Incidencia

class IncidenciaViewSet(viewsets.ModelViewSet):
    serializer_class = IncidenciaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Incidencia.objects.all()
        return Incidencia.objects.filter(django_user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(django_user=self.request.user)