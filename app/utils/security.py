# Esta línea de código importa la clase CryptContext del módulo
# passlib.context, que se utiliza para manejar el hashing de contraseñas
# de manera segura en la aplicación.
from passlib.context import CryptContext


# Esta línea de código define un objeto pwd_context utilizando la clase
# CryptContext. Se le asigna
# CryptContext(schemes=["bcrypt"], deprecated="auto"), lo que indica que
# se utilizará el algoritmo de hashing bcrypt para las contraseñas, y que
# cualquier algoritmo de hashing que esté marcado como obsoleto se manejará
# automáticamente. Este objeto se utilizará para realizar el hashing y la
# verificación de contraseñas en la aplicación.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Estas líneas de código definen dos funciones: hash_password y
# verify_password. La función hash_password toma una contraseña
# en texto plano como entrada y devuelve su versión hasheada utilizando
# el objeto pwd_context.
def hash_password(password: str):
    return pwd_context.hash(password)

# La función verify_password toma una contraseña en texto plano y una
# contraseña hasheada como entrada, y devuelve un valor booleano que indica
# si la contraseña en texto plano coincide con la contraseña hasheada
# utilizando el método verify del objeto pwd_context.


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)
