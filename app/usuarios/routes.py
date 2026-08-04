from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.usuarios import services, schemas
from app.core.security import crear_access_token

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