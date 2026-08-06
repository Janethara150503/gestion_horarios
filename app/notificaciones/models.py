from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class Notificacion(Base):
    __tablename__ = "notificaciones"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    mensaje = Column(Text, nullable=False)
    tipo = Column(String(50), nullable=False)
    vista = Column(Boolean, default=False)
    leida = Column(Boolean, default=False)
    creado_en = Column(DateTime(timezone=True), server_default=func.now())
    vista_en = Column(DateTime(timezone=True), nullable=True)
    leida_en = Column(DateTime(timezone=True), nullable=True)
    referencia_id = Column(Integer, nullable=True)

    usuario = relationship("Usuario")