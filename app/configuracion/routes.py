import os
import uuid
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from app.database import get_db
from app.configuracion import services, schemas
from app.core.dependencies import requiere_rol

router = APIRouter(prefix="/configuracion", tags=["configuracion"])

CARPETA_LOGOS = "app/static/logos"
EXTENSIONES_PERMITIDAS = {".png", ".jpg", ".jpeg", ".gif", ".webp"}


@router.get("/", response_model=schemas.ConfiguracionOut)
def obtener_configuracion(
    db: Session = Depends(get_db),
    usuario=Depends(requiere_rol("admin")),
):
    config = services.obtener_configuracion(db)
    if not config:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Configuracion no encontrada")
    return config


@router.get("/publica", response_model=schemas.ConfiguracionOut)
def obtener_configuracion_publica(db: Session = Depends(get_db)):
    config = services.obtener_configuracion(db)
    if not config:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Configuracion no encontrada")
    return config


@router.put("/", response_model=schemas.ConfiguracionOut)
def actualizar_configuracion(
    datos: schemas.ConfiguracionUpdate,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_rol("admin")),
):
    actualizado = services.actualizar_configuracion(db, datos)
    if not actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Configuracion no encontrada")
    return actualizado


@router.post("/logo", response_model=schemas.ConfiguracionOut)
def subir_logo(
    archivo: UploadFile = File(...),
    db: Session = Depends(get_db),
    usuario=Depends(requiere_rol("admin")),
):
    extension = os.path.splitext(archivo.filename)[1].lower()
    if extension not in EXTENSIONES_PERMITIDAS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Formato de imagen no permitido. Usa PNG, JPG, GIF o WEBP.",
        )

    os.makedirs(CARPETA_LOGOS, exist_ok=True)

    nombre_archivo = f"{uuid.uuid4().hex}{extension}"
    ruta_completa = os.path.join(CARPETA_LOGOS, nombre_archivo)

    with open(ruta_completa, "wb") as buffer:
        contenido = archivo.file.read()
        buffer.write(contenido)

    url_publica = f"/static/logos/{nombre_archivo}"

    actualizado = services.actualizar_logo(db, url_publica)
    if not actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Configuracion no encontrada")
    return actualizado
