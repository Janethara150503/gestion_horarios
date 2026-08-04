from pydantic import BaseModel
from typing import Optional
from datetime import date


class PeriodoAcademicoBase(BaseModel):
    nombre: str
    fecha_inicio: date
    fecha_fin: date
    activo: bool = True


class PeriodoAcademicoCreate(PeriodoAcademicoBase):
    pass


class PeriodoAcademicoOut(PeriodoAcademicoBase):
    id: int

    class Config:
        from_attributes = True


class ProgramaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None


class ProgramaCreate(ProgramaBase):
    pass


class ProgramaOut(ProgramaBase):
    id: int

    class Config:
        from_attributes = True


class MateriaBase(BaseModel):
    nombre: str
    programa_id: int
    creditos: Optional[int] = None


class MateriaCreate(MateriaBase):
    pass


class MateriaOut(MateriaBase):
    id: int
    programa: ProgramaOut

    class Config:
        from_attributes = True


class GrupoBase(BaseModel):
    nombre: str
    programa_id: int
    periodo_id: int


class GrupoCreate(GrupoBase):
    pass


class GrupoOut(GrupoBase):
    id: int
    programa: ProgramaOut
    periodo: PeriodoAcademicoOut

    class Config:
        from_attributes = True