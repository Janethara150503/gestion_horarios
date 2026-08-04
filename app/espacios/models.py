from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base


class Edificio(Base):
    __tablename__ = "edificios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False)
    direccion = Column(Text, nullable=True)

    aulas = relationship("Aula", back_populates="edificio")


class Aula(Base):
    __tablename__ = "aulas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    edificio_id = Column(Integer, ForeignKey("edificios.id"), nullable=False)
    capacidad = Column(Integer, nullable=False)
    tipo = Column(String(50), nullable=True)
    equipo = Column(Text, nullable=True)

    edificio = relationship("Edificio", back_populates="aulas")