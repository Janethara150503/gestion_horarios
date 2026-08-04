from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.espacios import services, schemas
from app.core.dependencies import requiere_rol, obtener_usuario_actual

router = APIRouter(prefix="/espacios", tags=["espacios"])


@router.post("/edificios", response_model=schemas.EdificioOut)
def crear_edificio(
    datos: schemas.EdificioCreate,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_rol("coordinador")),
):
    return services.crear_edificio(db, datos)


@router.get("/edificios", response_model=list[schemas.EdificioOut])
def listar_edificios(db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
    return services.listar_edificios(db)


@router.post("/aulas", response_model=schemas.AulaOut)
def crear_aula(
    datos: schemas.AulaCreate,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_rol("coordinador")),
):
    return services.crear_aula(db, datos)


@router.get("/aulas", response_model=list[schemas.AulaOut])
def listar_aulas(db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
    return services.listar_aulas(db)