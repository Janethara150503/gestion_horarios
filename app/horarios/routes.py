from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.horarios import services, schemas
from app.core.dependencies import requiere_rol, obtener_usuario_actual

router = APIRouter(prefix="/horarios", tags=["horarios"])


@router.post("/", response_model=schemas.HorarioClaseOut)
def crear_horario(
    datos: schemas.HorarioClaseCreate,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_rol("coordinador")),
):
    return services.crear_horario(db, datos)


@router.get("/", response_model=list[schemas.HorarioClaseOut])
def listar_horarios(db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
    return services.listar_horarios(db)