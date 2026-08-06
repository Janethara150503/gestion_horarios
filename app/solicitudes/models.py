from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class SolicitudCambio(Base):
    __tablename__ = "solicitudes_cambio"

    id = Column(Integer, primary_key=True, index=True)
    horario_clase_id = Column(Integer, ForeignKey("horarios_clase.id"), nullable=False)
    docente_id = Column(Integer, ForeignKey("docentes.id"), nullable=False)
    fecha_afectada = Column(Date, nullable=False)
    motivo = Column(Text, nullable=False)
    estado = Column(String(20), default="pendiente", nullable=False)
    respuesta_coordinador = Column(Text, nullable=True)
    excepcion_generada_id = Column(Integer, ForeignKey("excepciones_horario.id"), nullable=True)
    coordinador_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    creado_en = Column(DateTime(timezone=True), server_default=func.now())
    resuelto_en = Column(DateTime(timezone=True), nullable=True)

    horario_clase = relationship("HorarioClase")
    docente = relationship("Docente")
    excepcion_generada = relationship("ExcepcionHorario")
    coordinador = relationship("Usuario")