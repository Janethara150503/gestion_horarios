from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.notificaciones import services, schemas
from app.core.dependencies import obtener_usuario_actual

router = APIRouter(prefix="/notificaciones", tags=["notificaciones"])


@router.get("/", response_model=list[schemas.NotificacionOut])
def listar_mis_notificaciones(db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
    return services.listar_mis_notificaciones(db, usuario.id)


@router.get("/no-leidas", response_model=list[schemas.NotificacionOut])
def listar_no_leidas(db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
    return services.listar_no_leidas(db, usuario.id)


@router.put("/{notificacion_id}/vista", response_model=schemas.NotificacionOut)
def marcar_vista(notificacion_id: int, db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
    return services.marcar_vista(db, notificacion_id, usuario.id)


@router.put("/{notificacion_id}/leida", response_model=schemas.NotificacionOut)
def marcar_leida(notificacion_id: int, db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
    return services.marcar_leida(db, notificacion_id, usuario.id)