from pydantic import BaseModel


class ConfiguracionOut(BaseModel):
    id: int
    nombre_institucion: str
    direccion: str | None = None
    contacto: str | None = None
    dias_operacion: str
    duracion_sesion_minutos: int
    logo_url: str | None = None

    class Config:
        from_attributes = True


class ConfiguracionUpdate(BaseModel):
    nombre_institucion: str
    direccion: str | None = None
    contacto: str | None = None
    dias_operacion: str
    duracion_sesion_minutos: int