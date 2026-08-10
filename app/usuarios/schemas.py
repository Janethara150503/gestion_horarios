from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class RolBase(BaseModel):
    nombre: str


class RolOut(RolBase):
    id: int

    class Config:
        from_attributes = True


class UsuarioCreate(BaseModel):
    nombre_completo: str
    correo: EmailStr
    password: str
    rol_id: int


class UsuarioOut(BaseModel):
    id: int
    nombre_completo: str
    correo: EmailStr
    activo: bool
    creado_en: datetime
    rol: RolOut

    class Config:
        from_attributes = True


class UsuarioLogin(BaseModel):
    correo: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class DocenteCreate(BaseModel):
    usuario_id: int
    especialidad: Optional[str] = None


class DocenteOut(BaseModel):
    id: int
    usuario_id: int
    especialidad: Optional[str] = None
    usuario: Optional["UsuarioOut"] = None

    class Config:
        from_attributes = True

class EstudianteCreate(BaseModel):
    usuario_id: int
    grupo_id: int


class EstudianteOut(BaseModel):
    id: int
    usuario_id: int
    grupo_id: int
    usuario: Optional["UsuarioOut"] = None

    class Config:
        from_attributes = True

class UsuarioActualizarRol(BaseModel):
    rol_id: int


class UsuarioActualizarEstado(BaseModel):
    activo: bool