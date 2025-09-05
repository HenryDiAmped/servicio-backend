# servicio-backend

**Dentro de la carpeta `servicio-backend` abrimos la terminal o consola:**

1. **Crear el entorno virtual** (en PowerShell se tienen que dar permisos):
     ```bash
     python -m virtualenv venv
2. **Ejecutar si esta en powershell y luego intenta nuevamente crear el entorno virtual**
    ```bash
     Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
3. **Activar el entorno virtual**
    ```bash
     .\venv\Scripts\activate
4. **Instalar paquetes de proyecto**
    ```bash
     pip install -r .\requirements.txt

**Crear una base de datos `Mysql`:**

5. **Crear la BD**
    ```bash
    CREATE DATABASE servicios_db;

**Luego en el proyecto en la carpeta `drf` y luego en `settings.py`:**

6. **Configurar MySQL en Django**:
     ```bash
     DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'servicios_db',        # Nombre de tu base de datos
          'USER': 'root',          # Usuario de MySQL
          'PASSWORD': '',   # Contraseña de MySQL
          'HOST': 'localhost',           # O la IP del servidor MySQL
          'PORT': '3306',                # Puerto de MySQL (default: 3306)
      }
    }
     
**Dentro de la carpeta `servicio-backend` en la terminal o consola:**

7. **Ejecuta la aplicacion de migraciones existentes a la BD**
    ```bash
     python manage.py migrate
8. **Finalmente ejecuta el proyecto en el puerto `8000`**
    ```bash
     python manage.py runserver

# Documentacion
1. PARA GET Y POST:  
http://127.0.0.1:8000/api/servicios/
2. PARA PUT Y DELETE:  
http://127.0.0.1:8000/api/servicios/{id}/
