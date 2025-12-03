# 🔧 Solución: Error 400 Bad Request en Render

## Problema
Error 400 al intentar acceder a las páginas en Render:
```
127.0.0.1 - - [03/Dec/2025:00:40:33 -0300] "GET / HTTP/1.1" 400 143
```

## Causa
El error 400 generalmente se debe a:
1. **ALLOWED_HOSTS** no configurado correctamente
2. **CSRF_TRUSTED_ORIGINS** no incluye el dominio de Render
3. Configuraciones de seguridad demasiado estrictas (cookies seguras)

## Solución Aplicada

### 1. Agregado CSRF_TRUSTED_ORIGINS
```python
CSRF_TRUSTED_ORIGINS = os.environ.get(
    'CSRF_TRUSTED_ORIGINS',
    'https://inacap-reporta.onrender.com,http://localhost:8000'
).split(',')
```

### 2. Mejorado ALLOWED_HOSTS
Ahora maneja correctamente el caso cuando es '*'

### 3. Ajustadas configuraciones de seguridad
Desactivadas temporalmente cookies seguras para evitar errores:
- `SESSION_COOKIE_SECURE = False`
- `CSRF_COOKIE_SECURE = False`

## Variables de Entorno en Render

Asegúrate de tener configuradas estas variables en Render → Environment:

```
ALLOWED_HOSTS=inacap-reporta.onrender.com,*.onrender.com
CSRF_TRUSTED_ORIGINS=https://inacap-reporta.onrender.com
DEBUG=False
```

## Verificación

Después de hacer commit y push:
1. Render hará nuevo deploy automáticamente
2. Verifica que las páginas carguen sin error 400
3. Verifica que el login funcione correctamente

