from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.security import verificar_token
from app.usuarios.services import obtener_usuario_por_correo

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="usuarios/login")


def obtener_usuario_actual(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credenciales_invalidas = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar el token de acceso",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = verificar_token(token)
    if payload is None:
        raise credenciales_invalidas

    correo = payload.get("sub")
    if correo is None:
        raise credenciales_invalidas

    usuario = obtener_usuario_por_correo(db, correo)
    if usuario is None or not usuario.activo:
        raise credenciales_invalidas

    return usuario


def requiere_rol(*roles_permitidos: str):
    def verificador(usuario=Depends(obtener_usuario_actual)):
        if usuario.rol.nombre not in roles_permitidos:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tienes permisos suficientes para esta accion",
            )
        return usuario
    return verificador