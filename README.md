# INACAP Reporta

Sistema de reporte de incidencias desarrollado con Django para la gestión de problemas y solicitudes en INACAP.

## 📋 Descripción

INACAP Reporta es una aplicación web que permite a los usuarios reportar incidencias y problemas, y a los administradores gestionarlas de manera eficiente. El sistema incluye:

- ✅ Sistema de autenticación de usuarios
- ✅ Reporte de incidencias con categorización y niveles de urgencia
- ✅ Panel de administración para gestión de incidencias
- ✅ Panel de usuario para seguimiento de reportes
- ✅ Sistema de roles (Estudiante/Encargado)
- ✅ Carga de imágenes como evidencia
- ✅ API REST para integraciones

## 🚀 Características Principales

### Para Usuarios (Estudiantes)
- Crear y gestionar reportes de incidencias
- Ver estado de sus reportes
- Editar reportes pendientes
- Perfil de usuario personalizable
- Categorización por tipo de problema
- Niveles de urgencia: Baja, Media, Alta, Crítica

### Para Administradores
- Panel completo de administración
- Gestión de todas las incidencias
- Cambio de estado de incidencias
- Eliminación de reportes
- Estadísticas de incidencias
- Filtrado y búsqueda

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 4.1.7
- **Base de Datos**: MySQL / PostgreSQL
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **API**: Django REST Framework
- **Servidor**: Gunicorn (producción)

## 📦 Instalación

### Prerrequisitos

- Python 3.11 o superior
- MySQL o PostgreSQL
- pip

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/inacap_reporta.git
   cd inacap_reporta
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv env
   
   # Windows
   env\Scripts\activate
   
   # Linux/Mac
   source env/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   cd inacap_reporta
   pip install -r requirements.txt
   ```

4. **Configurar base de datos**
   
   Crear una base de datos MySQL:
   ```sql
   CREATE DATABASE inacap_reporta;
   ```
   
   O configura las variables de entorno para PostgreSQL (ver `VARIABLES_ENTORNO.md`)

5. **Configurar variables de entorno**
   
   Crear archivo `.env` en la carpeta `inacap_reporta/`:
   ```env
   SECRET_KEY=tu-secret-key-aqui
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DB_ENGINE=django.db.backends.mysql
   DB_NAME=inacap_reporta
   DB_USER=root
   DB_PASSWORD=tu-password
   DB_HOST=localhost
   DB_PORT=3306
   ```

6. **Ejecutar migraciones**
   ```bash
   python manage.py migrate
   ```

7. **Crear superusuario**
   ```bash
   python manage.py createsuperuser
   ```

8. **Recopilar archivos estáticos**
   ```bash
   python manage.py collectstatic
   ```

9. **Ejecutar servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

   La aplicación estará disponible en `http://localhost:8000`

## 📁 Estructura del Proyecto

```
inacap_reporta-main/
├── inacap_reporta/          # Proyecto Django principal
│   ├── inacap_reporta/      # Configuración del proyecto
│   │   ├── settings.py      # Configuración
│   │   ├── urls.py          # URLs principales
│   │   └── wsgi.py          # Configuración WSGI
│   ├── reportes/            # Aplicación principal
│   │   ├── models.py        # Modelos de datos
│   │   ├── views.py         # Vistas
│   │   ├── urls.py          # URLs de la app
│   │   ├── templates/       # Plantillas HTML
│   │   └── static/          # Archivos estáticos (CSS, JS)
│   ├── media/               # Archivos subidos por usuarios
│   ├── manage.py            # Script de gestión Django
│   ├── requirements.txt     # Dependencias Python
│   ├── Procfile             # Configuración para Railway/Heroku
│   └── runtime.txt          # Versión de Python
├── env/                     # Entorno virtual (ignorado por Git)
├── README.md                # Este archivo
├── .gitignore              # Archivos ignorados por Git
└── RAILWAY.md              # Guía de despliegue en Railway
```

## 🌐 Despliegue

### Railway

El proyecto está configurado para desplegarse fácilmente en Railway. Consulta el archivo `RAILWAY.md` para instrucciones detalladas.

### Variables de Entorno

Para más información sobre las variables de entorno necesarias, consulta `VARIABLES_ENTORNO.md`.

## 👥 Roles y Permisos

### Estudiante
- Crear reportes de incidencias
- Ver sus propios reportes
- Editar reportes pendientes
- Ver perfil personal

### Encargado/Administrador
- Todas las funciones de Estudiante
- Ver todos los reportes
- Cambiar estado de incidencias
- Eliminar reportes
- Panel de administración completo

## 🔧 Configuración

### Base de Datos

El proyecto soporta tanto MySQL como PostgreSQL. Para cambiar de base de datos, modifica la variable `DB_ENGINE` en el archivo `.env` o en las variables de entorno.

### Archivos Estáticos

En producción, los archivos estáticos se sirven usando WhiteNoise. En desarrollo, Django los sirve automáticamente.

### Media Files

Las imágenes de las incidencias se almacenan en la carpeta `media/incidencias/`. Para producción, se recomienda usar un servicio de almacenamiento en la nube como AWS S3 o Cloudinary.

## 📝 API REST

El proyecto incluye una API REST usando Django REST Framework. Los endpoints están disponibles en `/api/`.

## 🐛 Solución de Problemas

### Error de conexión a la base de datos
- Verifica que la base de datos esté creada
- Confirma las credenciales en las variables de entorno
- Asegúrate de que el servicio de base de datos esté ejecutándose

### Archivos estáticos no se cargan
- Ejecuta `python manage.py collectstatic`
- Verifica la configuración de WhiteNoise en `settings.py`

### Error 500 en producción
- Revisa los logs del servidor
- Verifica que `DEBUG=False` en producción
- Confirma que `ALLOWED_HOSTS` incluya tu dominio

## 📄 Licencia

Este proyecto es privado y pertenece a INACAP.

## 👨‍💻 Desarrollo

Para contribuir al proyecto, por favor sigue estas guías:

1. Crea una rama para tu feature
2. Realiza tus cambios
3. Crea un Pull Request
4. Espera la revisión

## 📞 Contacto

Para preguntas o soporte, contacta al equipo de desarrollo.

---

Desarrollado con ❤️ para INACAP


