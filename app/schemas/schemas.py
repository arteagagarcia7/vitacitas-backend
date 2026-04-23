# Está línea importa la clase BaseModel del módulo pydantic,
# que se usará para definir los esquemas de datos.
from pydantic import BaseModel


# La Clase CrearUsuario hereda de BaseModel, lo que significa
# que es un modelo de datos que se puede usar para validar y
# serializar datos. Esta clase tiene dos atributos: nombre,
# correo y password que son todos de tipo String.
class CrearUsuario(BaseModel):
    nombre: str
    correo: str
    password: str
