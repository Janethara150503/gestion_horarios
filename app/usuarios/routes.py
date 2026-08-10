from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.usuarios import services, schemas
from app.core.security import crear_access_token
from app.core.dependencies import obtener_usuario_actual, requiere_rol
router = APIRouter(prefix="/usuarios", tags=["usuarios"])


@router.post("/registro", response_model=schemas.UsuarioOut)
def registrar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    usuario_existente = services.obtener_usuario_por_correo(db, usuario.correo)
    if usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un usuario registrado con ese correo",
        )
    return services.crear_usuario(db, usuario)


@router.post("/login", response_model=schemas.Token)
def login(credenciales: schemas.UsuarioLogin, db: Session = Depends(get_db)):
    usuario = services.autenticar_usuario(db, credenciales.correo, credenciales.password)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contraseña incorrectos",
        )
    token = crear_access_token(data={"sub": usuario.correo, "rol": usuario.rol.nombre})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/yo", response_model=schemas.UsuarioOut)
def obtener_mi_perfil(usuario=Depends(obtener_usuario_actual)):
    return usuario

@router.post("/docentes", response_model=schemas.DocenteOut)
def crear_docente(
    datos: schemas.DocenteCreate,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_rol("coordinador")),
):
    return services.crear_docente(db, datos)


@router.post("/estudiantes", response_model=schemas.EstudianteOut)
def crear_estudiante(
    datos: schemas.EstudianteCreate,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_rol("coordinador")),
):
    return services.crear_estudiante(db, datos)
@router.get("/estudiantes/yo", response_model=schemas.EstudianteOut)
def obtener_mi_estudiante(
    db: Session = Depends(get_db),
    usuario=Depends(requiere_rol("estudiante")),
):
    from app.usuarios.models import Estudiante
    estudiante = db.query(Estudiante).filter(Estudiante.usuario_id == usuario.id).first()
    if not estudiante:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Este usuario no tiene un registro de estudiante asociado",
        )
    return estudiante

@router.get("/docentes", response_model=list[schemas.DocenteOut])
def listar_docentes(
    db: Session = Depends(get_db),
    usuario=Depends(requiere_rol("coordinador")),
):
    from app.usuarios.models import Docente
    return db.query(Docente).all()

@router.get("/estudiantes", response_model=list[schemas.EstudianteOut])
def listar_estudiantes(
    db: Session = Depends(get_db),
    usuario=Depends(requiere_rol("coordinador")),
):
    from app.usuarios.models import Estudiante
    return db.query(Estudiante).all()