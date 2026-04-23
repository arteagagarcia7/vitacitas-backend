# Esta línea de código importa la clase FastAPI del módulo fastapi, que es un
# framework web para construir APIs en Python.
from fastapi import FastAPI

# Esta línea de código importa el motor de la base de datos.
from app.database import engine

# Esta línea de código importa la clase Base desde el módulo models, que es la
# clase base para definir los modelos de datos que representarán las tablas de
# la base de datos.
from app.models.models import Base

# Esta línea de código importa el módulo usuarios desde el paquete routes,
# que contiene las rutas relacionadas con los usuarios en la aplicación.
from app.routes import usuarios


# Esta línea de código crea las tablas en la base de datos utilizando el motor
# La función create_all() de SQLAlchemy se utiliza para crear todas las tablas
# definidas en los modelos de datos que heredan de Base. bind=engine indica que
# se debe utilizar el motor de la base de datos definido en engine para crear
# las tablas.
Base.metadata.create_all(bind=engine)

# Esta línea de código crea una instancia de la clase FastAPI y la asigna a la
# variable app. Esta instancia se utiliza para definir las rutas y manejar las
# solicitudes HTTP en la aplicación web.
app = FastAPI()

# Esta línea de código incluye el router de usuarios en la aplicación FastAPI.
app.include_router(usuarios.router)

# Estas líneas de código crean una instancia de FastAPI llamada app, que se
# utilizara para definir las rutas y manejar las solicitudes HTTP. En
# este caso,se define una ruta raíz ("/") que responde a las solicitudes
# GET con un mensaje de bienvenida.


@app.get("/")
def inicio():
    return {"mensaje": "Hola Carlos, tu API funciona 🚀"}
