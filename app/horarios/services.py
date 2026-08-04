from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from fastapi import HTTPException, status
from app.horarios.models import HorarioClase
from app.horarios import schemas


def existe_solapamiento(db: Session, datos: schemas.HorarioClaseCreate):
    condicion_solapamiento = and_(
        HorarioClase.periodo_id == datos.periodo_id,
        HorarioClase.dia_semana == datos.dia_semana,
        HorarioClase.activo == True,
        HorarioClase.hora_inicio < datos.hora_fin,
        HorarioClase.hora_fin > datos.hora_inicio,
        or_(
            HorarioClase.aula_id == datos.aula_id,
            HorarioClase.docente_id == datos.docente_id,
        ),
    )
    return db.query(HorarioClase).filter(condicion_solapamiento).first()


def crear_horario(db: Session, datos: schemas.HorarioClaseCreate):
    choque = existe_solapamiento(db, datos)
    if choque:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                f"Choque de horario detectado: ya existe una clase el {choque.dia_semana} "
                f"de {choque.hora_inicio} a {choque.hora_fin} que usa la misma aula o el mismo docente."
            ),
        )

    nuevo = HorarioClase(**datos.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def listar_horarios(db: Session):
    return db.query(HorarioClase).filter(HorarioClase.activo == True).all()