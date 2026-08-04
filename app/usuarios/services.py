from sqlalchemy.orm import Session
from app.usuarios.models import Usuario, Rol
from app.usuarios.schemas import UsuarioCreate
from app.core.security import hash_password, verify_password


def obtener_usuario_por_correo(db: Session, correo: str):
    return db.query(Usuario).filter(Usuario.correo == correo).first()


def crear_usuario(db: Session, usuario_data: UsuarioCreate):
    password_hasheado = hash_password(usuario_data.password)
    nuevo_usuario = Usuario(
        nombre_completo=usuario_data.nombre_completo,
        correo=usuario_data.correo,
        password_hash=password_hasheado,
        rol_id=usuario_data.rol_id,
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario


def autenticar_usuario(db: Session, correo: str, password: str):
    usuario = obtener_usuario_por_correo(db, correo)
    if not usuario:
        return None
    if not verify_password(password, usuario.password_hash):
        return None
    if not usuario.activo:
        return None
    return usuario

def crear_docente(db: Session, datos):
    from app.usuarios.models import Docente
    nuevo = Docente(**datos.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def crear_estudiante(db: Session, datos):
    from app.usuarios.models import Estudiante
    nuevo = Estudiante(**datos.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo