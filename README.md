VitaCitas - API

VitaCitas será una aplicación que permitirá la gestón de citas médicas. Actualmente se encuentra en construcción el backend el cual se está desarrollando con FastApi.
Con este proyecto busco seguir fortaleciendo mi aprendizaje en el mundo del desarrollo y consolidarme como un desarrollador de software, especializado en el backend.


Caracteristicas actuales del proyecto:
* Permite el registro de usuarios, también la validación de lo que se ha guardado en la base de datos por medio de los Endpoint de usuarios.
* Simulación de un inicio de sesión con los usuarios creados previamente por medio del Endpoint login.
* Encriptación de contraseñas por medio de token y autenticación basada en JWT.
* CRUD de recursos y protección de rutas (aun en desarrollo).


Tecnologías Utilizadas:
* Lenguaje: Python.
* Framework: FastApi.
* Base de datos: PostgreSQL.
* Hashing de contraseñas: Libreria Passlib.
* JWT: Python-Jose.


¿Cómo funciona el sistema de autenticación?
Se implemento JSON Web Tokens para la implementación de la autenticación. En el Endpoing /login, el usuario completa su nombre, correo y contraseña; y al ejecutarse el sistema genera un token. El cliente tendrá un token por cada petición que realice. 


¿Cómo instalar y ejecutar el proyecto?

* Primero clona el repocitorio:
git clone *** 
cd ***

* Crea un entorno virtual:
python -m venv venv 
source venv/bin/activate (Si usas Linux o Mac)
venv\Scripts\activate (Si usas Windows)

* Instala las dependencias:
pip install -r requirements.txt

* Configura las variables de entorno:
Crear archivo .env con lo siguiente:
SECRET_KEY=tu_clave_secreta
DATABASE_URL=tu_conexion_postgresql

* Ejecuta el servidor:
uvicorn main:app --reload

* Ingresa a la documentación interactiva:
http://127.0.0.1:8000/docs


¿Cuál es el estado actual del proyecto?
El proyecto aún está en desarrollo, cuenta con una autenticación funcional y base para expansión a un sistema completo de agendamento de citas.
Proximamente se desarrollará los roles de usuario, el refresh de tokens, creación e integración del frontend usando vue.js, y despliegue en la nube.

Autor:
Carlos Andrés Arteaga
Desarrollador en aprendizaje constante enfocado en backend y aplicaciones web.