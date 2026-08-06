from sqlalchemy.orm import Session
from datetime import datetime
from app.notificaciones.models import Notificacion


def crear_notificacion(db: Session, usuario_id: int, mensaje: str, tipo: str, referencia_id: int = None):
    nueva = Notificacion(
        usuario_id=usuario_id,
        mensaje=mensaje,
        tipo=tipo,
        referencia_id=referencia_id,
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


def listar_mis_notificaciones(db: Session, usuario_id: int):
    return (
        db.query(Notificacion)
        .filter(Notificacion.usuario_id == usuario_id)
        .order_by(Notificacion.creado_en.desc())
        .all()
    )


def listar_no_leidas(db: Session, usuario_id: int):
    return (
        db.query(Notificacion)
        .filter(Notificacion.usuario_id == usuario_id, Notificacion.leida == False)
        .order_by(Notificacion.creado_en.desc())
        .all()
    )


def marcar_vista(db: Session, notificacion_id: int, usuario_id: int):
    notificacion = (
        db.query(Notificacion)
        .filter(Notificacion.id == notificacion_id, Notificacion.usuario_id == usuario_id)
        .first()
    )
    if notificacion and not notificacion.vista:
        notificacion.vista = True
        notificacion.vista_en = datetime.utcnow()
        db.commit()
        db.refresh(notificacion)
    return notificacion


def marcar_leida(db: Session, notificacion_id: int, usuario_id: int):
    notificacion = (
        db.query(Notificacion)
        .filter(Notificacion.id == notificacion_id, Notificacion.usuario_id == usuario_id)
        .first()
    )
    if notificacion and not notificacion.leida:
        notificacion.leida = True
        notificacion.leida_en = datetime.utcnow()
        db.commit()
        db.refresh(notificacion)
    return notificacion