# esta línea de código importa la función create_engine del
# módulo sqlalchemy, que va a ser utilizada para crear una
# conexión a la base de datos.
from sqlalchemy import create_engine

# esta línea de código importa sessionmaker del módulo
# sqlalchemy.orm, que va a ser utilizada para crear una clase
# de sesión para interactuar con la base de datos.
from sqlalchemy.orm import sessionmaker

# esta línea de código importa declarative_base del módulo
# sqlalchemy.ext.declarative, que se va a utilizar para crear
# una clase base para definir los modelos de datos que
# representarán las tablas de la base de datos.
from sqlalchemy.ext.declarative import declarative_base

from dotenv import load_dotenv
import os

load_dotenv()

# esta línea de código crea una clase base llamada DATABASE_URL
# que se le asigna la URL de conexión a la base de datos PostgreSQL.
# Esta URL incluye el nombre de usuario y la contraseña para acceder
# a la base de datos, así como el nombre de la base de datos a la que
# se va a conectar.
DATABASE_URL = os.getenv("DATABASE_URL")

# esta línea de código crea un motor de base de datos utilizando la URL
# de conexión definida en DATABASE_URL. Este motor es el responsable de
# gestionar la conexión a la base de datos y ejecutar las consultas SQL.
engine = create_engine(DATABASE_URL)

# esta línea de código crea una clase base llamada SesionLocal utilizando
# la función sessionmaker. Esta clase se utilizará para crear sesiones
# que permitan interactuar con la base de datos.
SesionLocal = sessionmaker(bind=engine)

# esta línea de código crea una clase base llamada Base utilizando la función
# declarative_base. Esta clase se utilizará como base para definir los
# modelos de datos que representarán las tablas de la base de datos.
Base = declarative_base()
