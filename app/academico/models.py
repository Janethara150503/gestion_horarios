from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base


class PeriodoAcademico(Base):
    __tablename__ = "periodos_academicos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    activo = Column(Boolean, default=True)

    grupos = relationship("Grupo", back_populates="periodo")


class Programa(Base):
    __tablename__ = "programas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), unique=True, nullable=False)
    descripcion = Column(Text, nullable=True)

    materias = relationship("Materia", back_populates="programa")
    grupos = relationship("Grupo", back_populates="programa")


class Materia(Base):
    __tablename__ = "materias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    programa_id = Column(Integer, ForeignKey("programas.id"), nullable=False)
    creditos = Column(Integer, nullable=True)

    programa = relationship("Programa", back_populates="materias")


class Grupo(Base):
    __tablename__ = "grupos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    programa_id = Column(Integer, ForeignKey("programas.id"), nullable=False)
    periodo_id = Column(Integer, ForeignKey("periodos_academicos.id"), nullable=False)

    programa = relationship("Programa", back_populates="grupos")
    periodo = relationship("PeriodoAcademico", back_populates="grupos")