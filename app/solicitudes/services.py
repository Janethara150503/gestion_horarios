from sqlalchemy.orm import Session
from datetime import datetime, time as time_type
from fastapi import HTTPException, status
from app.solicitudes.models import SolicitudCambio
from app.horarios.models import ExcepcionHorario
from app.solicitudes import schemas
from app.notificaciones.services import crear_notificacion
from app.usuarios.models import Docente


def crear_solicitud(db: Session, docente_id: int, datos: schemas.SolicitudCambioCreate):
    nueva = SolicitudCambio(
        horario_clase_id=datos.horario_clase_id,
        docente_id=docente_id,
        fecha_afectada=datos.fecha_afectada,
        motivo=datos.motivo,
        estado="pendiente",
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


def listar_solicitudes_pendientes(db: Session):
    return db.query(SolicitudCambio).filter(SolicitudCambio.estado == "pendiente").all()


def listar_mis_solicitudes(db: Session, docente_id: int):
    return db.query(SolicitudCambio).filter(SolicitudCambio.docente_id == docente_id).all()


def resolver_solicitud(db: Session, solicitud_id: int, coordinador_id: int, datos: schemas.SolicitudCambioResolver):
    solicitud = db.query(SolicitudCambio).filter(SolicitudCambio.id == solicitud_id).first()

    if not solicitud:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Solicitud no encontrada")

    if solicitud.estado != "pendiente":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Esta solicitud ya fue resuelta anteriormente",
        )

    solicitud.coordinador_id = coordinador_id
    solicitud.respuesta_coordinador = datos.respuesta_coordinador
    solicitud.resuelto_en = datetime.utcnow()

    if datos.aprobar:
        nueva_excepcion = ExcepcionHorario(
            horario_clase_id=solicitud.horario_clase_id,
            fecha=solicitud.fecha_afectada,
            aula_id=datos.aula_id,
            docente_id=datos.docente_id,
            hora_inicio=time_type.fromisoformat(datos.hora_inicio) if datos.hora_inicio else None,
            hora_fin=time_type.fromisoformat(datos.hora_fin) if datos.hora_fin else None,
            motivo=f"Solicitud aprobada: {solicitud.motivo}",
            creado_por=coordinador_id,
        )
        db.add(nueva_excepcion)
        db.commit()
        db.refresh(nueva_excepcion)

        solicitud.estado = "aprobada"
        solicitud.excepcion_generada_id = nueva_excepcion.id
    else:
        solicitud.estado = "rechazada"
    db.commit()
    db.refresh(solicitud)

    docente = db.query(Docente).filter(Docente.id == solicitud.docente_id).first()
    if docente:
        if solicitud.estado == "aprobada":
            mensaje = f"Tu solicitud de cambio para el {solicitud.fecha_afectada} fue aprobada."
            tipo = "solicitud_aprobada"
        else:
            mensaje = f"Tu solicitud de cambio para el {solicitud.fecha_afectada} fue rechazada."
            tipo = "solicitud_rechazada"

        crear_notificacion(
            db=db,
            usuario_id=docente.usuario_id,
            mensaje=mensaje,
            tipo=tipo,
            referencia_id=solicitud.id,
        )

    return solicitud