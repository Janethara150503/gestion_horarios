from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.solicitudes import services, schemas
from app.core.dependencies import requiere_rol
from app.usuarios.models import Docente

router = APIRouter(prefix="/solicitudes", tags=["solicitudes"])


def obtener_docente_actual(usuario, db: Session):
    docente = db.query(Docente).filter(Docente.usuario_id == usuario.id).first()
    if not docente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Este usuario no tiene un registro de docente asociado",
        )
    return docente


@router.post("/", response_model=schemas.SolicitudCambioOut)
def crear_solicitud(
    datos: schemas.SolicitudCambioCreate,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_rol("docente")),
):
    docente = obtener_docente_actual(usuario, db)
    return services.crear_solicitud(db, docente.id, datos)


@router.get("/mias", response_model=list[schemas.SolicitudCambioOut])
def listar_mis_solicitudes(
    db: Session = Depends(get_db),
    usuario=Depends(requiere_rol("docente")),
):
    docente = obtener_docente_actual(usuario, db)
    return services.listar_mis_solicitudes(db, docente.id)


@router.get("/pendientes", response_model=list[schemas.SolicitudCambioOut])
def listar_pendientes(
    db: Session = Depends(get_db),
    usuario=Depends(requiere_rol("coordinador")),
):
    return services.listar_solicitudes_pendientes(db)


@router.put("/{solicitud_id}/resolver", response_model=schemas.SolicitudCambioOut)
def resolver_solicitud(
    solicitud_id: int,
    datos: schemas.SolicitudCambioResolver,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_rol("coordinador")),
):
    return services.resolver_solicitud(db, solicitud_id, usuario.id, datos)