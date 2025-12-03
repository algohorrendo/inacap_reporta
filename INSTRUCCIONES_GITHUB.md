# Instrucciones para Subir el Proyecto a GitHub

El repositorio Git local ya está configurado y el commit inicial está listo. Ahora sigue estos pasos para subirlo a GitHub:

## 📋 Pasos para Subir a GitHub

### Opción 1: Usando la Interfaz Web de GitHub (Recomendado)

1. **Crear el repositorio en GitHub**
   - Ve a https://github.com
   - Inicia sesión en tu cuenta
   - Haz clic en el botón "+" en la esquina superior derecha
   - Selecciona "New repository"

2. **Configurar el repositorio**
   - **Repository name**: `inacap_reporta` (o el nombre que prefieras)
   - **Description**: "Sistema de reporte de incidencias para INACAP"
   - **Visibility**: Elige "Public" o "Private" según prefieras
   - ⚠️ **NO marques** "Initialize this repository with a README" (ya tenemos uno)
   - ⚠️ **NO agregues** .gitignore ni licencia (ya los tenemos)
   - Haz clic en "Create repository"

3. **Conectar y subir el código**
   
   GitHub te mostrará las instrucciones. Ejecuta estos comandos en tu terminal:

   ```bash
   # Agregar el repositorio remoto (reemplaza TU_USUARIO con tu usuario de GitHub)
   git remote add origin https://github.com/TU_USUARIO/inacap_reporta.git
   
   # Renombrar la rama a main (si es necesario)
   git branch -M main
   
   # Subir el código
   git push -u origin main
   ```

### Opción 2: Usando GitHub CLI

Si tienes GitHub CLI instalado:

```bash
# Crear el repositorio y conectarlo
gh repo create inacap_reporta --public --source=. --remote=origin --push
```

### Opción 3: Desde el Explorador de Archivos

1. Abre GitHub Desktop si lo tienes instalado
2. Selecciona "Add" → "Add Existing Repository"
3. Navega a la carpeta `inacap_reporta-main`
4. Haz clic en "Publish repository"
5. Sigue las instrucciones

## 🔐 Si te pide autenticación

Si GitHub te pide usuario y contraseña:

### Usar Personal Access Token (Recomendado)

1. Ve a GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Genera un nuevo token con permisos `repo`
3. Usa el token como contraseña cuando Git te lo pida

### O usar SSH

Si prefieres usar SSH:

1. Genera una clave SSH:
   ```bash
   ssh-keygen -t ed25519 -C "tu_email@example.com"
   ```

2. Agrega la clave a GitHub:
   - Copia el contenido de `~/.ssh/id_ed25519.pub`
   - Ve a GitHub → Settings → SSH and GPG keys → New SSH key
   - Pega la clave

3. Cambia la URL del remoto:
   ```bash
   git remote set-url origin git@github.com:TU_USUARIO/inacap_reporta.git
   ```

## ✅ Verificar que todo está bien

Después de hacer push, verifica:

1. Ve a tu repositorio en GitHub
2. Deberías ver todos los archivos
3. El README.md debería aparecer en la página principal

## 📝 Comandos Rápidos

Una vez configurado, para futuras actualizaciones:

```bash
# Ver el estado
git status

# Agregar cambios
git add .

# Hacer commit
git commit -m "Descripción de los cambios"

# Subir a GitHub
git push
```

## 🆘 Solución de Problemas

### Error: "repository not found"
- Verifica que el nombre del repositorio sea correcto
- Asegúrate de tener permisos para escribir en el repositorio

### Error: "Authentication failed"
- Usa un Personal Access Token en lugar de tu contraseña
- O configura SSH

### Error: "fatal: remote origin already exists"
- Elimina el remoto existente: `git remote remove origin`
- Vuelve a agregarlo con el comando anterior

## 🎉 ¡Listo!

Una vez completados estos pasos, tu proyecto estará en GitHub y podrás:
- Compartirlo con otros
- Hacer clonaciones
- Colaborar con otros desarrolladores
- Desplegarlo en Railway (conectar tu repositorio de GitHub)


