from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class SolicitudCambioCreate(BaseModel):
    horario_clase_id: int
    fecha_afectada: date
    motivo: str


class SolicitudCambioOut(BaseModel):
    id: int
    horario_clase_id: int
    docente_id: int
    fecha_afectada: date
    motivo: str
    estado: str
    respuesta_coordinador: Optional[str] = None
    excepcion_generada_id: Optional[int] = None
    coordinador_id: Optional[int] = None
    creado_en: datetime
    resuelto_en: Optional[datetime] = None

    class Config:
        from_attributes = True


class SolicitudCambioResolver(BaseModel):
    aprobar: bool
    respuesta_coordinador: Optional[str] = None
    aula_id: Optional[int] = None
    docente_id: Optional[int] = None
    hora_inicio: Optional[str] = None
    hora_fin: Optional[str] = None