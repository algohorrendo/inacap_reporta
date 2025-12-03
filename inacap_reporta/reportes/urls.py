from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import api_views


router = DefaultRouter()
router.register(r'incidencias', api_views.IncidenciaViewSet, basename='incidencia')


urlpatterns = [
    path('', views.principal_view, name='principal'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('panel_usuario/', views.panel_usuario_view, name='panel_usuario'),
    path('usuario/editar/<int:id>/', views.editar_incidencia_usuario_view, name='editar_incidencia_usuario'),
    path('usuario/eliminar/<int:id>/', views.eliminar_incidencia_usuario_view, name='eliminar_incidencia_usuario'),
    path('panel_administracion/', views.panel_administracion_view, name='panel_administracion'),
    path('reporte_incidencia/', views.reporte_incidencia_view, name='reporte_incidencia'),
    path('detalle_incidencias/<int:id>/', views.detalle_incidencias_view, name='detalle_incidencias'),
    path('incidencia/eliminar/<int:id>/', views.eliminar_incidencia_view, name='eliminar_incidencia'),
    path('incidencia/cambiar_estado/<int:id>/', views.cambiar_estado_view, name='cambiar_estado_incidencia'),
    path('api/', include(router.urls)),
    path('api-dashboard/', views.api_dashboard_view, name='api_dashboard'),
    # ==================== RUTAS DE PERFIL ====================
    path('perfil/', views.perfil, name='perfil'),
    # Rutas usadas en las tablas del perfil
    path('perfil/reporte/<int:id>/', views.detalle_incidencias_view, name='ver_reporte'),
    path('perfil/reporte/<int:id>/editar/', views.editar_incidencia_usuario_view, name='editar_reporte'),
    path('perfil/reporte/nuevo/', views.reporte_incidencia_view, name='crear_reporte'),

path('actualizar_perfil/', views.actualizar_perfil, name='actualizar_perfil'),
path('cambiar_contraseña/', views.cambiar_contraseña, name='cambiar_contraseña'),
]
