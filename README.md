**PFO 2: Sistema de Gestión de Tareas con API y Base de Datos**
Este proyecto consiste en el desarrollo de una API REST utilizando Flask y SQLite para la gestión de usuarios
y autenticación segura con contraseñas encriptadas (hashing).

**Tecnologías utilizadas**
- Lenguaje: Python
- Framework: Flask
- Base de Datos: SQLite 3
- Seguridad/Hashing: Werkzeug
- Pruebas de API: Thunder Client

  **Instrucciones para Ejecución y Pruebas**
  1. Clonar el repositorio
  2. Crear y activar un entorno virtual
  En Windows:
     python -m venv venv
     .\venv\Scripts\activate
  
3. Instalar las dependencias necesarias
    pip install flask werkzeug
4. Iniciar el servidor API
   python servidor.py
   El servidor se iniciará en http://127.0.0.1:5000

   **Endpoints de la API**
   **Método**             **Endpoint**        **Descripción**                                                            **Cuerpo de ka petición (JSON)**
   
   POST                    /registro         Registra un nuevo usuario con la contraseña encriptada.                      {"usuario": "nombre", "contraseña": "1234"}
   POST                    /login            Verifica las credenciales e inicia sesión.                                   {"usuario": "nombre", "contraseña": "1234"}
   GET                     /tareas           Muestra la interfaz/HTML de bienvenida a la gestión de tareas.                No requiere


   **Capturas de Pruebas exitosas**
   1. Registro de Usuario (POST /registro)
 ![Registro](/assets/registro.png)     


   3. Inicio de Sesión (POST /login)
      
![login](/assets/login.png)

3. Página de Bienvenida (GET /tareas)
   
![tareas](/assets/tareas1.png)

![tareas](/assets/tareas2.png)

  
   **Respuestas conceptuales:**
a)	¿Por qué hashear contraseñas? 
En primer lugar, por Seguridad: Si la base de datos se ve comprometida por una brecha o filtración, las contraseñas no se revelan en texto plano.
Irreversibilidad: El hashing es una función unidireccional. La aplicación verifica si la contraseña ingresada genera el mismo hash que el almacenado sin necesidad de conocer o guardar la clave original.

b)	Ventajas de usar SQLite en este proyecto.
Sin configuración de servidor: SQLite es un motor de base de datos integrado basado en archivos; no requiere instalar o configurar un servicio independiente (como PostgreSQL o MySQL).
Ligero y portátil: Toda la base de datos se almacena en un solo archivo (database.db), lo que simplifica las pruebas locales y la migración del proyecto.
