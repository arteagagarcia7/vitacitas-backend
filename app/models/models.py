# esta línea de código importa las clases Column, Integer y String del
# módulo sqlalchemy, se usarán para definir las columnas
# de la tabla en la base de datos.
from sqlalchemy import Column, Integer, String

# en está línea de código se importa la clase Base desde dabase.py, que
# es la clase base para definir los modelos de datos que representarán las
# tablas de la base de datos.
from app.database import Base

# en estas líneas de código se define la clase Usuario, que hereda Base. Esta
# clase representa la tabla llamada Usuario en la base de datos. La clase
# tiene cuatro atributos: id, nombre, correo y password, que corresponden a
# las columnas de la tabla. id es la clave primaria y se indexa; nombre es un
# String y correo es un String único, es decir que no pueden haber dos usuarios
# con el mismo correo en la base de datos. Y password es un String que
# almacenará la contraseña hasheada del usuario.


class Usuario(Base):
    # __tablename__ es un atibuto que asigna el nombre real de la tabla en
    # la bd.
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    correo = Column(String, unique=True)
    password = Column(String)
