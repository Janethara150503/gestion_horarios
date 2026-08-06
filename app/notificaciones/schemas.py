from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class NotificacionOut(BaseModel):
    id: int
    usuario_id: int
    mensaje: str
    tipo: str
    vista: bool
    leida: bool
    creado_en: datetime
    vista_en: Optional[datetime] = None
    leida_en: Optional[datetime] = None
    referencia_id: Optional[int] = None

    class Config:
        from_attributes = True