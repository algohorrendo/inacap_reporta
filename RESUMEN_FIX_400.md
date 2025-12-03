# ✅ Solución Completa: Error 400 Bad Request

## Cambios Realizados

### 1. Agregado CSRF_TRUSTED_ORIGINS
```python
CSRF_TRUSTED_ORIGINS = [
    'https://inacap-reporta.onrender.com',
    'http://localhost:8000'
]
```

### 2. Mejorado ALLOWED_HOSTS
Ahora maneja correctamente el valor '*' y lista de hosts separados por comas.

### 3. Desactivadas cookies seguras temporalmente
```python
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
```

## Variables de Entorno Recomendadas en Render

Ve a Render → Settings → Environment y agrega:

```
ALLOWED_HOSTS=inacap-reporta.onrender.com,*.onrender.com
CSRF_TRUSTED_ORIGINS=https://inacap-reporta.onrender.com
DEBUG=False
```

## Próximos Pasos

1. Hacer commit de los cambios
2. Push a GitHub
3. Render hará deploy automáticamente
4. Verificar que el error 400 ya no aparezca

## Nota

Si el error persiste, verifica:
- Que las variables de entorno estén configuradas correctamente
- Que el dominio en CSRF_TRUSTED_ORIGINS coincida exactamente con tu URL de Render

