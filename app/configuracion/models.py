from sqlalchemy import Column, Integer, String
from app.database import Base


class ConfiguracionInstitucion(Base):
    __tablename__ = "configuracion_institucion"

    id = Column(Integer, primary_key=True, index=True)
    nombre_institucion = Column(String(150), nullable=False, default="Mi Institucion")
    direccion = Column(String(255), nullable=True)
    contacto = Column(String(150), nullable=True)
    dias_operacion = Column(String(100), nullable=False, default="sabado,domingo")
    duracion_sesion_minutos = Column(Integer, nullable=False, default=60)
    logo_url = Column(String(500), nullable=True)