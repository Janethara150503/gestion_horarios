from sqlalchemy import Column, Integer, String, Time, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class HorarioClase(Base):
    __tablename__ = "horarios_clase"

    id = Column(Integer, primary_key=True, index=True)
    grupo_id = Column(Integer, ForeignKey("grupos.id"), nullable=False)
    materia_id = Column(Integer, ForeignKey("materias.id"), nullable=False)
    docente_id = Column(Integer, ForeignKey("docentes.id"), nullable=False)
    aula_id = Column(Integer, ForeignKey("aulas.id"), nullable=False)
    periodo_id = Column(Integer, ForeignKey("periodos_academicos.id"), nullable=False)
    dia_semana = Column(String(20), nullable=False)
    hora_inicio = Column(Time, nullable=False)
    hora_fin = Column(Time, nullable=False)
    activo = Column(Boolean, default=True)

    grupo = relationship("Grupo")
    materia = relationship("Materia")
    docente = relationship("Docente")
    aula = relationship("Aula")
    periodo = relationship("PeriodoAcademico")


class ExcepcionHorario(Base):
    __tablename__ = "excepciones_horario"

    id = Column(Integer, primary_key=True, index=True)
    horario_clase_id = Column(Integer, ForeignKey("horarios_clase.id"), nullable=False)
    fecha = Column(Date, nullable=False)
    aula_id = Column(Integer, ForeignKey("aulas.id"), nullable=True)
    docente_id = Column(Integer, ForeignKey("docentes.id"), nullable=True)
    hora_inicio = Column(Time, nullable=True)
    hora_fin = Column(Time, nullable=True)
    motivo = Column(String(255), nullable=True)
    creado_por = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    horario_clase = relationship("HorarioClase")
    aula = relationship("Aula")
    docente = relationship("Docente")
    creador = relationship("Usuario")