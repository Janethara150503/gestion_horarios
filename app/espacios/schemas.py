from pydantic import BaseModel
from typing import Optional


class EdificioBase(BaseModel):
    nombre: str
    direccion: Optional[str] = None


class EdificioCreate(EdificioBase):
    pass


class EdificioOut(EdificioBase):
    id: int

    class Config:
        from_attributes = True


class AulaBase(BaseModel):
    nombre: str
    edificio_id: int
    capacidad: int
    tipo: Optional[str] = None
    equipo: Optional[str] = None


class AulaCreate(AulaBase):
    pass


class AulaOut(AulaBase):
    id: int
    edificio: EdificioOut

    class Config:
        from_attributes = True