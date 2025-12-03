from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from django.contrib.auth import update_session_auth_hash
import datetime

from .models import Incidencia, Categoria, Ubicacion

@login_required
def api_dashboard_view(request):
    # Puedes ajustar el template si quieres, pero así evita el error
    return render(request, 'reportes/api_dashboard.html')

def is_admin(user):
    return user.is_staff or user.is_superuser


@login_required
def eliminar_incidencia_usuario_view(request, id):
    if request.method != 'POST':
        return HttpResponseForbidden("Método no permitido")
    incidencia = get_object_or_404(
        Incidencia, id_incidencia=id, django_user=request.user
    )
    incidencia.delete()
    return redirect('panel_usuario')


@login_required
def editar_incidencia_usuario_view(request, id):
    incidencia = get_object_or_404(
        Incidencia, id_incidencia=id, django_user=request.user
    )
    if request.method == 'POST':
        incidencia.titulo = request.POST.get('titulo')
        incidencia.categoria_texto = request.POST.get('categoria')
        incidencia.descripcion = request.POST.get('descripcion')
        incidencia.ubicacion_texto = request.POST.get('ubicacion')
        incidencia.urgencia = request.POST.get('urgencia')
        nueva_foto = request.FILES.get('foto')
        if nueva_foto:
            incidencia.foto = nueva_foto
        incidencia.save()
        return redirect('panel_usuario')
    return render(
        request,
        'reportes/panel_usuario/editar_incidencia.html',
        {'incidencia': incidencia}
    )


@csrf_exempt
@require_http_methods(["GET", "POST"])
def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if user.is_staff or user.is_superuser:
                    return redirect("panel_administracion")
                return redirect("panel_usuario")
            return render(
                request,
                "reportes/login/login.html",
                {"error": "Usuario o contraseña incorrectos"}
            )
    return render(request, "reportes/login/login.html")


def registro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not all([username, email, first_name, password1, password2]):
            return render(
                request,
                'reportes/registro/registro.html',
                {'error': 'Todos los campos son obligatorios'}
            )
        if password1 != password2:
            return render(
                request,
                'reportes/registro/registro.html',
                {'error': 'Las contraseñas no coinciden'}
            )
        if len(password1) < 4:
            return render(
                request,
                'reportes/registro/registro.html',
                {'error': 'La contraseña debe tener al menos 4 caracteres'}
            )
        if User.objects.filter(username=username).exists():
            return render(
                request,
                'reportes/registro/registro.html',
                {'error': 'Este nombre de usuario ya existe'}
            )
        if User.objects.filter(email=email).exists():
            return render(
                request,
                'reportes/registro/registro.html',
                {'error': 'Este email ya está registrado'}
            )

        try:
            User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                first_name=first_name,
                is_staff=False,
                is_superuser=False,
                is_active=True
            )
            messages.success(request, 'Cuenta creada exitosamente')
            return redirect('login')
        except Exception as e:
            return render(
                request,
                'reportes/registro/registro.html',
                {'error': f'Error al crear cuenta: {e}'}
            )
    return render(request, 'reportes/registro/registro.html')


def principal_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.is_staff or request.user.is_superuser:
        return redirect('panel_administracion')
    return redirect('panel_usuario')


@login_required
def panel_usuario_view(request):
    if request.user.is_staff or request.user.is_superuser:
        return redirect('panel_administracion')
    incidencias = Incidencia.objects.filter(django_user=request.user)
    return render(
        request,
        'reportes/panel_usuario/panel_usuario.html',
        {'incidencias': incidencias}
    )


@login_required
@user_passes_test(is_admin)
def panel_administracion_view(request):
    incidencias = Incidencia.objects.all()
    pendientes = incidencias.filter(estado='pendiente').count()
    return render(
        request,
        'reportes/panel_administracion/panel_administracion.html',
        {
            'incidencias': incidencias,
            'pendientes': pendientes
        }
    )


@login_required
def reporte_incidencia_view(request):
    if request.user.is_staff or request.user.is_superuser:
        return redirect('panel_administración')

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        categoria = request.POST.get('categoria')
        descripcion = request.POST.get('descripcion')
        ubicacion = request.POST.get('ubicacion')
        urgencia = request.POST.get('urgencia')
        foto = request.FILES.get('foto')
        hora_local_str = request.POST.get('hora_local')

        try:
            fecha_local = datetime.datetime.strptime(
                hora_local_str, '%Y-%m-%d %H:%M:%S'
            )
        except (ValueError, TypeError):
            fecha_local = timezone.now()

        if not all([titulo, categoria, descripcion, ubicacion, urgencia]):
            return render(
                request,
                'reportes/reporte_incidencias/reporte_incidencia.html',
                {'error': 'Todos los campos son obligatorios'}
            )

        try:
            categoria_obj, _ = Categoria.objects.get_or_create(
                nombre=categoria.title(),
                defaults={'nombre': categoria.title()}
            )
            ubicacion_obj, _ = Ubicacion.objects.get_or_create(
                sector=ubicacion,
                defaults={
                    'sector': ubicacion,
                    'descripcion': f'Ubicación: {ubicacion}'
                }
            )
            incidencia = Incidencia.objects.create(
                titulo=titulo,
                descripcion=descripcion,
                fecha_reporte=fecha_local,
                estado='pendiente',
                django_user=request.user,
                id_categoria=categoria_obj,
                id_ubicacion=ubicacion_obj,
                urgencia=urgencia,
                ubicacion_texto=ubicacion,
                categoria_texto=categoria,
                foto=foto
            )
            return render(
                request,
                'reportes/reporte_incidencias/reporte_incidencia.html',
                {
                    'success': True,
                    'mensaje': (
                        f'Incidencia #{incidencia.id_incidencia} '
                        'reportada exitosamente'
                    )
                }
            )
        except Exception as e:
            return render(
                request,
                'reportes/reporte_incidencias/reporte_incidencia.html',
                {'error': f'Error al crear la incidencia: {e}'}
            )

    return render(request, 'reportes/reporte_incidencias/reporte_incidencia.html')


@login_required
def detalle_incidencias_view(request, id):
    incidencia = get_object_or_404(Incidencia, id_incidencia=id)
    if (
        not (request.user.is_staff or request.user.is_superuser)
        and incidencia.django_user != request.user
    ):
        return redirect('panel_usuario')
    return render(
        request,
        'reportes/detalle_incidencias/detalle_incidencias.html',
        {'incidencia': incidencia}
    )


@login_required
@user_passes_test(is_admin)
def eliminar_incidencia_view(request, id):
    if request.method != 'POST':
        return HttpResponseForbidden("Método no permitido")
    incidencia = get_object_or_404(Incidencia, id_incidencia=id)
    incidencia.delete()
    return redirect('panel_administracion')


@login_required
@user_passes_test(is_admin)
def cambiar_estado_view(request, id):
    if request.method != 'POST':
        return HttpResponseForbidden("Método no permitido")
    incidencia = get_object_or_404(Incidencia, id_incidencia=id)
    nuevo_estado = request.POST.get('estado')
    if nuevo_estado in ['pendiente', 'resuelto']:
        incidencia.estado = nuevo_estado
        incidencia.save()
    return redirect('panel_administracion')


# ==================== PERFIL ====================

@login_required
def perfil(request):
    reportes = Incidencia.objects.filter(
        django_user=request.user
    ).order_by('-fecha_reporte')

    total_reportes = reportes.count()
    reportes_pendientes = reportes.filter(estado='pendiente').count()
    reportes_resueltos = reportes.filter(estado='resuelto').count()

    context = {
        'reportes': reportes,
        'total_reportes': total_reportes,
        'reportes_pendientes': reportes_pendientes,
        'reportes_resueltos': reportes_resueltos,
    }
    return render(request, 'reportes/perfil/perfil.html', context)


@login_required
def actualizar_perfil(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '').strip()
        user.last_name = request.POST.get('last_name', '').strip()
        user.email = request.POST.get('email', '').strip()

        if User.objects.filter(email=user.email).exclude(id=user.id).exists():
            messages.error(request, '❌ Este email ya está en uso')
            return redirect('perfil')

        user.save()
        messages.success(request, '✅ Perfil actualizado correctamente')

    return redirect('perfil')


@login_required
def cambiar_contraseña(request):
    
    if request.method == 'POST':
        user = request.user
        password_actual = request.POST.get('password_actual', '')
        password_nueva = request.POST.get('password_nueva', '')
        password_confirmar = request.POST.get('password_confirmar', '')

        # 1) Verificar contraseña actual
        if not user.check_password(password_actual):
            messages.error(request, '❌ La contraseña actual es incorrecta')
            return redirect('perfil')

        # 2) Verificar que las nuevas coinciden
        if password_nueva != password_confirmar:
            messages.error(request, '❌ Las contraseñas no coinciden')
            return redirect('perfil')

        # 3) Verificar longitud mínima
        if len(password_nueva) < 8:
            messages.error(
                request,
                '❌ La contraseña debe tener al menos 8 caracteres'
            )
            return redirect('perfil')

        # 4) Guardar nueva contraseña
        user.set_password(password_nueva)
        user.save()
        update_session_auth_hash(request, user)
        messages.success(request, '✅ Contraseña cambiada correctamente')
        return redirect('perfil')

    return redirect('perfil')

