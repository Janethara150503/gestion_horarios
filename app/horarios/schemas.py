from pydantic import BaseModel, field_validator, model_validator
from datetime import time

DIAS_VALIDOS = {"lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"}


class HorarioClaseBase(BaseModel):
    grupo_id: int
    materia_id: int
    docente_id: int
    aula_id: int
    periodo_id: int
    dia_semana: str
    hora_inicio: time
    hora_fin: time
    activo: bool = True

    @field_validator("dia_semana")
    @classmethod
    def validar_dia(cls, valor):
        valor_normalizado = valor.strip().lower()
        if valor_normalizado not in DIAS_VALIDOS:
            raise ValueError(f"dia_semana debe ser uno de: {', '.join(sorted(DIAS_VALIDOS))}")
        return valor_normalizado

    @model_validator(mode="after")
    def validar_rango_horario(self):
        if self.hora_fin <= self.hora_inicio:
            raise ValueError("hora_fin debe ser posterior a hora_inicio")
        return self


class HorarioClaseCreate(HorarioClaseBase):
    pass


class HorarioClaseOut(HorarioClaseBase):
    id: int

    class Config:
        from_attributes = True