from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import User
from .models import Incidencia, Categoria, Ubicacion, Rol

# ==================== ADMIN DE INCIDENCIAS ====================

@admin.register(Incidencia)
class IncidenciaAdmin(admin.ModelAdmin):
    """
    Admin para gestionar todas las incidencias reportadas
    """
    list_display = (
        'id_incidencia',
        'titulo',
        'estado_badge',
        'usuario_badge',
        'urgencia_badge',
        'categoria_badge',
        'ubicacion_badge',
        'fecha_reporte'
    )
    
    list_filter = (
        'estado',
        'urgencia',
        'django_user',
        'id_categoria',
        'id_ubicacion',
        'fecha_reporte'
    )
    
    search_fields = (
        'titulo',
        'descripcion',
        'django_user__username',
        'django_user__first_name',
        'categoria_texto',
        'ubicacion_texto'
    )
    
    readonly_fields = (
        'fecha_reporte',
        'django_user'
    )
    
    fieldsets = (
        ('📋 INFORMACIÓN GENERAL', {
            'fields': ('titulo', 'descripcion', 'urgencia')
        }),
        ('👤 USUARIO QUE REPORTÓ', {
            'fields': ('django_user',),
            'description': 'Usuario que creó este reporte - No se puede modificar'
        }),
        ('🏢 UBICACIÓN', {
            'fields': ('id_ubicacion', 'ubicacion_texto')
        }),
        ('📁 CATEGORÍA', {
            'fields': ('id_categoria', 'categoria_texto')
        }),
        ('⚡ ESTADO', {
            'fields': ('estado', 'fecha_reporte')
        }),
        ('📸 ARCHIVO MULTIMEDIA', {
            'fields': ('foto',)
        })
    )
    
    def has_add_permission(self, request):
        return True
    
    def usuario_badge(self, obj):
        if obj.django_user:
            nombre = obj.django_user.get_full_name() or obj.django_user.username
            return format_html(
                '<span style="background-color: #2196F3; color: white; padding: 5px 10px; border-radius: 3px; font-weight: bold;">👤 {}</span>',
                nombre
            )
        return '❌ Sin usuario'
    usuario_badge.short_description = 'Usuario'
    
    def estado_badge(self, obj):
        colores = {
            'pendiente': '#FF9800',
            'progreso': '#2196F3',
            'resuelto': '#4CAF50',
            'cerrado': '#9C27B0'
        }
        iconos = {
            'pendiente': '⏳',
            'progreso': '⚙️',
            'resuelto': '✅',
            'cerrado': '🔒'
        }
        color = colores.get(obj.estado, '#757575')
        icono = iconos.get(obj.estado, '•')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 5px 10px; border-radius: 3px; font-weight: bold;">{} {}</span>',
            color,
            icono,
            obj.estado.upper()
        )
    estado_badge.short_description = 'Estado'
    
    def urgencia_badge(self, obj):
        colores = {
            'baja': '#4CAF50',
            'media': '#FFC107',
            'alta': '#FF5722'
        }
        iconos = {
            'baja': '🟢',
            'media': '🟡',
            'alta': '🔴'
        }
        color = colores.get(obj.urgencia, '#757575')
        icono = iconos.get(obj.urgencia, '•')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 5px 10px; border-radius: 3px; font-weight: bold;">{} {}</span>',
            color,
            icono,
            obj.urgencia.upper()
        )
    urgencia_badge.short_description = 'Urgencia'
    
    def categoria_badge(self, obj):
        if obj.id_categoria:
            return format_html(
                '<span style="background-color: #9C27B0; color: white; padding: 5px 10px; border-radius: 3px;">📁 {}</span>',
                obj.id_categoria.nombre
            )
        return '❌ Sin categoría'
    categoria_badge.short_description = 'Categoría'
    
    def ubicacion_badge(self, obj):
        if obj.id_ubicacion:
            return format_html(
                '<span style="background-color: #FF5722; color: white; padding: 5px 10px; border-radius: 3px;">📍 {}</span>',
                obj.id_ubicacion.sector
            )
        return '❌ Sin ubicación'
    ubicacion_badge.short_description = 'Ubicación'


# ==================== ADMIN DE CATEGORÍAS ====================

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombre', 'total_incidencias')
    search_fields = ('nombre',)
    
    def has_add_permission(self, request):
        return True
    
    def total_incidencias(self, obj):
        count = Incidencia.objects.filter(id_categoria=obj).count()
        return format_html(
            '<span style="background-color: #2196F3; color: white; padding: 3px 8px; border-radius: 3px; font-weight: bold;">{} reportes</span>',
            count
        )
    total_incidencias.short_description = 'Total Reportes'


# ==================== ADMIN DE UBICACIONES ====================

@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('id_ubicacion', 'sector', 'descripcion', 'total_incidencias')
    search_fields = ('sector', 'descripcion')
    
    def has_add_permission(self, request):
        return True
    
    def total_incidencias(self, obj):
        count = Incidencia.objects.filter(id_ubicacion=obj).count()
        return format_html(
            '<span style="background-color: #FF5722; color: white; padding: 3px 8px; border-radius: 3px; font-weight: bold;">{} reportes</span>',
            count
        )
    total_incidencias.short_description = 'Total Reportes'


# ==================== ADMIN DE ROLES ====================

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    """
    Admin para gestionar Roles: Estudiante y Encargado
    """
    list_display = (
        'nombre_badge',
        'descripcion_corta',
        'total_usuarios_badge',
        'fecha_creacion'
    )
    
    search_fields = (
        'nombre',
        'descripcion'
    )
    
    readonly_fields = (
        'creado',
        'actualizado',
        'usuarios_list'
    )
    
    fieldsets = (
        ('📋 INFORMACIÓN DEL ROL', {
            'fields': ('nombre', 'descripcion')
        }),
        ('👥 USUARIOS ASIGNADOS', {
            'fields': ('usuarios', 'usuarios_list')
        }),
        ('📅 FECHAS', {
            'fields': ('creado', 'actualizado')
        })
    )
    
    filter_horizontal = ('usuarios',)
    
    def has_add_permission(self, request):
        return True
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def nombre_badge(self, obj):
        if obj.nombre == 'estudiante':
            return format_html(
                '<span style="background-color: #9C27B0; color: white; padding: 6px 12px; border-radius: 4px; font-weight: bold; font-size: 14px;">👨‍🎓 ESTUDIANTE</span>'
            )
        elif obj.nombre == 'encargado':
            return format_html(
                '<span style="background-color: #FF5722; color: white; padding: 6px 12px; border-radius: 4px; font-weight: bold; font-size: 14px;">👨‍💼 ENCARGADO</span>'
            )
        return obj.get_nombre_display()
    nombre_badge.short_description = 'Rol'
    
    def descripcion_corta(self, obj):
        if obj.descripcion:
            return obj.descripcion[:50] + "..." if len(obj.descripcion) > 50 else obj.descripcion
        return "-"
    descripcion_corta.short_description = 'Descripción'
    
    def total_usuarios_badge(self, obj):
        count = obj.usuarios.count()
        return format_html(
            '<span style="background-color: #2196F3; color: white; padding: 4px 8px; border-radius: 3px; font-weight: bold;">👥 {} usuarios</span>',
            count
        )
    total_usuarios_badge.short_description = 'Usuarios'
    
    def usuarios_list(self, obj):
        usuarios = obj.usuarios.all()
        if usuarios.exists():
            html = '<table style="width: 100%; border-collapse: collapse; margin-top: 10px;">'
            html += '<tr style="background-color: #f0f0f0; border-bottom: 2px solid #ccc;">'
            html += '<th style="padding: 8px; text-align: left; border: 1px solid #ddd;">👤 Usuario</th>'
            html += '<th style="padding: 8px; text-align: left; border: 1px solid #ddd;">✉️ Email</th>'
            html += '<th style="padding: 8px; text-align: left; border: 1px solid #ddd;">📊 Reportes</th>'
            html += '</tr>'
            
            for usuario in usuarios:
                reportes_count = Incidencia.objects.filter(django_user=usuario).count()
                html += '<tr style="border-bottom: 1px solid #ddd;">'
                html += f'<td style="padding: 8px; border: 1px solid #ddd;"><strong>{usuario.get_full_name() or usuario.username}</strong></td>'
                html += f'<td style="padding: 8px; border: 1px solid #ddd;">{usuario.email}</td>'
                html += f'<td style="padding: 8px; border: 1px solid #ddd; text-align: center;"><strong>{reportes_count}</strong></td>'
                html += '</tr>'
            
            html += '</table>'
            return format_html(html)
        else:
            return format_html('<p style="color: #999;">No hay usuarios asignados a este rol</p>')
    usuarios_list.short_description = 'Usuarios Asignados'
    
    def fecha_creacion(self, obj):
        return obj.creado.strftime('%d/%m/%Y %H:%M')
    fecha_creacion.short_description = 'Creado'


# ==================== ADMIN DE USUARIOS QUE HAN REPORTADO ====================

class UsuarioReportador(User):
    class Meta:
        proxy = True
        verbose_name = 'UsuariosR'
        verbose_name_plural = 'UsuariosR'


@admin.register(UsuarioReportador)
class UsuarioReportadorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_completo',
        'username_display',
        'email_display',
        'total_reportes_badge',
        'estado_usuario',
        'ultimo_reporte',
        'ver_reportes_link'
    )
    
    list_filter = (
        'is_active',
        'date_joined'
    )
    
    search_fields = (
        'username',
        'first_name',
        'last_name',
        'email'
    )
    
    readonly_fields = (
        'username',
        'email',
        'date_joined',
        'last_login',
        'total_reportes_readonly',
        'reportes_del_usuario'
    )
    
    fieldsets = (
        ('👤 INFORMACIÓN PERSONAL', {
            'fields': ('username', 'first_name', 'last_name', 'email')
        }),
        ('📊 REPORTES', {
            'fields': ('total_reportes_readonly', 'reportes_del_usuario'),
            'description': 'Total de reportes realizados por este usuario'
        }),
        ('📅 FECHAS', {
            'fields': ('date_joined', 'last_login')
        })
    )
    
    def has_add_permission(self, request):
        return True
    
    def has_delete_permission(self, request, obj=None):
        return True
    
    def nombre_completo(self, obj):
        nombre_completo = obj.get_full_name() or obj.username
        return format_html(
            '<span style="font-weight: bold; color: #1976D2;">{}</span>',
            nombre_completo
        )
    nombre_completo.short_description = 'Nombre Completo'
    
    def username_display(self, obj):
        return format_html(
            '<span style="color: #424242;">@{}</span>',
            obj.username
        )
    username_display.short_description = 'Username'
    
    def email_display(self, obj):
        return format_html(
            '<a href="mailto:{}">{}</a>',
            obj.email,
            obj.email
        )
    email_display.short_description = 'Email'
    
    def total_reportes_badge(self, obj):
        count = Incidencia.objects.filter(django_user=obj).count()
        if count > 0:
            return format_html(
                '<span style="background-color: #4CAF50; color: white; padding: 5px 10px; border-radius: 3px; font-weight: bold;">📊 {} reportes</span>',
                count
            )
        return format_html(
            '<span style="background-color: #9E9E9E; color: white; padding: 5px 10px; border-radius: 3px;">Sin reportes</span>'
        )
    total_reportes_badge.short_description = 'Total Reportes'
    
    def total_reportes_readonly(self, obj):
        count = Incidencia.objects.filter(django_user=obj).count()
        return format_html(
            '<strong>{}</strong> reportes realizados',
            count
        )
    total_reportes_readonly.short_description = 'Total de Reportes'
    
    def reportes_del_usuario(self, obj):
        reportes = Incidencia.objects.filter(django_user=obj).order_by('-fecha_reporte')
        if reportes.exists():
            html = '<table style="width: 100%; border-collapse: collapse; margin-top: 10px;">'
            html += '<tr style="background-color: #f0f0f0; border-bottom: 2px solid #ccc;">'
            html += '<th style="padding: 8px; text-align: left; border: 1px solid #ddd;">📋 Título</th>'
            html += '<th style="padding: 8px; text-align: left; border: 1px solid #ddd;">⚡ Estado</th>'
            html += '<th style="padding: 8px; text-align: left; border: 1px solid #ddd;">📁 Categoría</th>'
            html += '<th style="padding: 8px; text-align: left; border: 1px solid #ddd;">📅 Fecha</th>'
            html += '</tr>'
            
            for reporte in reportes:
                colores_estado = {
                    'pendiente': '#FF9800',
                    'progreso': '#2196F3',
                    'resuelto': '#4CAF50',
                    'cerrado': '#9C27B0'
                }
                color_estado = colores_estado.get(reporte.estado, '#757575')
                
                html += '<tr style="border-bottom: 1px solid #ddd;">'
                html += f'<td style="padding: 8px; border: 1px solid #ddd;"><strong>{reporte.titulo}</strong></td>'
                html += f'<td style="padding: 8px; border: 1px solid #ddd;"><span style="background-color: {color_estado}; color: white; padding: 4px 8px; border-radius: 3px;">{reporte.estado.upper()}</span></td>'
                html += f'<td style="padding: 8px; border: 1px solid #ddd;">{reporte.id_categoria.nombre if reporte.id_categoria else "N/A"}</td>'
                html += f'<td style="padding: 8px; border: 1px solid #ddd;">{reporte.fecha_reporte.strftime("%d/%m/%Y %H:%M")}</td>'
                html += '</tr>'
            
            html += '</table>'
            return format_html(html)
        else:
            return format_html('<p style="color: #999;">Este usuario no tiene reportes</p>')
    
    reportes_del_usuario.short_description = 'Reportes Realizados'
    
    def estado_usuario(self, obj):
        if obj.is_active:
            return format_html(
                '<span style="background-color: #4CAF50; color: white; padding: 5px 10px; border-radius: 3px; font-weight: bold;">✅ Activo</span>'
            )
        else:
            return format_html(
                '<span style="background-color: #F44336; color: white; padding: 5px 10px; border-radius: 3px; font-weight: bold;">❌ Inactivo</span>'
            )
    estado_usuario.short_description = 'Estado'
    
    def ultimo_reporte(self, obj):
        ultimo = Incidencia.objects.filter(django_user=obj).order_by('-fecha_reporte').first()
        if ultimo:
            return format_html(
                '<span title="{}">{}</span>',
                ultimo.fecha_reporte,
                ultimo.fecha_reporte.strftime('%d/%m/%Y %H:%M')
            )
        return '-'
    ultimo_reporte.short_description = 'Último Reporte'
    
    def ver_reportes_link(self, obj):
        count = Incidencia.objects.filter(django_user=obj).count()
        if count > 0:
            return format_html(
                '<a class="button" href="/admin/reportes/incidencia/?django_user__id__exact={}" style="background-color: #417690; color: white; padding: 5px 10px; border-radius: 3px; text-decoration: none;">Ver reportes →</a>',
                obj.id
            )
        return '-'
    ver_reportes_link.short_description = 'Acciones'
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset