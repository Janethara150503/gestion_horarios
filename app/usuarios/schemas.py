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