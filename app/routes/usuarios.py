# Esta línea de código importa la clase APIRouter del módulo fastapi,
# que se utiliza para crear rutas y manejar solicitudes en la
# aplicación web. HTTPException del módulo fastapi, que
# se utiliza para manejar excepciones HTTP y devolver respuestas de error
# adecuadas cuando ocurren errores en las rutas de la API.
from fastapi import APIRouter, HTTPException

# Esta línea de código importa la clase SesionLocal desde el módulo database,
# que se utilizará para crear sesiones de bd.
from app.database import SesionLocal

# Esta línea de código importa la clase Usuario desde el módulo models, que es
# un modelo de datos que representa la tabla de usuarios en la base de datos.
from app.models.models import Usuario

# Esta línea de código importa la clase CrearUsuario desde el módulo schemas,
# que es un modelo de datos que se utiliza para validar los datos de entrada
# al crear un nuevo usuario a través de la API.
from app.schemas.schemas import CrearUsuario


# Esta línea de código importa la función hash_password desde el módulo
# security, que se utiliza para hashear las contraseñas de los usuarios de
# manera segura antes de almacenarlas en la base de datos.
from app.utils.security import hash_password


# Esta línea de código importa la función verify_password desde el módulo
# security, que se utiliza para verificar si una contraseña en texto plano
# coincide con una contraseña hasheada almacenada en la base de datos.
from app.utils.security import verify_password

# Esta línea de código importa la función create_access_token desde el
# módulo security, que se utiliza para crear tokens de acceso JWT
# (JSON WEB TOKENS) el cual se utilizará para autenticar a los usuarios
# en la aplicación y permitirles acceder a recursos protegidos después de
# iniciar sesión correctamente.
from app.core.security import create_access_token


# Esta línea de código crea una instancia de APIRouter y la asigna a la
# variable router. Esta instancia se utilizará para definir las rutas
# relacionadas con los usuarios en la aplicación.
router = APIRouter()


# Estas líneas definen una ruta GET en la URL "/usuarios". Cuando se accede
# a esta ruta, la función obtener_usuarios() se ejecuta. Dentro de la función,
# se crea una nueva sesión de bd. Luego, se realiza una consulta a la tabla de
# usuarios utilizando db.query(Usuario).all(), lo que devuelve una lista de
# todos los usuarios registrados en la bd. Después de obtener los usuarios
# se cierra la sesión de la bd y devuelve la lista de usuarios como respuesta
# a la solicitud GET.


@router.get("/usuarios")
def obtener_usuarios():
    db = SesionLocal()

    usuarios = db.query(Usuario).all()

    db.close()

    return usuarios


# Estas líneas definen una ruta POST en la URL "/usuarios". Cuando se accede a
# esta ruta, la función crear_usuario() se ejecuta. Esta función recibe un
# objeto de tipo CrearUsuario, que es un modelo de datos definido en el módulo
# schemas. Dentro de la función, se crea una nueva sesión de base de datos
# utilizando SesionLocal(). Luego, se crea una instancia de la clase Usuario
# utilizando los datos recibidos en el objeto CrearUsuario. Esta nueva
# instancia se agrega a la sesión de base de datos, se confirma la
# transacción con db.commit(), y se actualiza la instancia con db.refresh().
# Finalmente, se cierra la sesión de base de datos y se devuelve el nuevo
# usuario creado.
@router.post("/usuarios")
def crear_usuario(usuario: CrearUsuario):
    db = SesionLocal()

    nuevo_usuario = Usuario(
        nombre=usuario.nombre,
        correo=usuario.correo,
        password=hash_password(usuario.password)
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    db.close()

    return nuevo_usuario

# Estas líneas definen una ruta POST en la URL "/login".


@router.post("/login")
def login(usuario: CrearUsuario):
    db = SesionLocal()

    usuario_db = db.query(Usuario).filter(
        Usuario.correo == usuario.correo).first()

    if not usuario_db:
        db.close()
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    if not verify_password(usuario.password, usuario_db.password):
        db.close()
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    access_token = create_access_token(
        data={"sub": usuario_db.correo}
    )

    db.close()

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# Estas líneas define una ruta PUT en la URL "/usuarios/{id}". Cuando se
# accede a esta ruta, la función actualizar_usuario() se ejecuta. Esta
# función recibe un id que se extrae de la URL y un objeto de tipo
# CrearUsuario. Dentro de la función, se crea una nueva sesión de base de
# datos utilizando SesionLocal(). Luego, se realiza una consulta a la tabla
# de usuarios para encontrar el usuario con el id utilizando
# db.query(Usuario).filter(Usuario.id == id).first(). Si no se encuentra
# ningún usuario con ese id, se cierra la sesión de base de datos y se
# devuelve un mensaje de error indicando que el usuario no fue encontrado.
# Pero si lo encuentra, se actualizan los atributos nombre y correo del usuario
# con los datos recibidos en el objeto CrearUsuario. Luego, se confirma la
# transacción con db.commit(), se actualiza la instancia del usuario con
# db.refresh(), se cierra la sesión de base de datos y se devuelve el usuario
# actualizado.
@router.put("/usuarios/{id}")
def actualizar_usuario(id: int, usuario: CrearUsuario):
    db = SesionLocal()

    usuario_db = db.query(Usuario).filter(Usuario.id == id).first()

    if not usuario_db:
        db.close()
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    usuario_db.nombre = usuario.nombre
    usuario_db.correo = usuario.correo

    db.commit()
    db.refresh(usuario_db)
    db.close()

    return usuario_db


# Estas líneas define una ruta DELETE en la URL "/usuarios/{id}". Cuando se
# accede a esta ruta, la función eliminar_usuario() se ejecuta. Esta función
# recibe un parámetro id que se extrae de la URL. Dentro de la función, se
# crea una nueva sesión de base de datos utilizando SesionLocal(). Luego, se
# realiza una consulta a la tabla de usuarios para encontrar el usuario con el
# id. Utilizando db.query(Usuario).filter(Usuario.id == id).first(), se
# obtiene el primer usuario que coincide con el id indicado. Si no se
# encuentra ningún usuario con ese id, se cierra la sesión de base de
# datos y se devuelve un mensaje de error indicando que el usuario no fue
# encontrado. Pero si lo encuentra,se elimina el usuario de la base de datos
# utilizando db.delete(usuario),se confirma la transacción con db.commit(),
# se cierra la sesión de base de datos y se devuelve un mensaje de confirmación
# indicando que el usuario fue eliminado.
@router.delete("/usuarios/{id}")
def eliminar_usuario(id: int):
    db = SesionLocal()

    usuario = db.query(Usuario).filter(Usuario.id == id).first()

    if not usuario:
        db.close()
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(usuario)
    db.commit()
    db.close()

    return {"mensaje": "Usuario eliminado"}
