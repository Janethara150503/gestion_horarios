from sqlalchemy.orm import Session
from app.configuracion.models import ConfiguracionInstitucion


def obtener_configuracion(db: Session):
    return db.query(ConfiguracionInstitucion).filter(ConfiguracionInstitucion.id == 1).first()


def actualizar_configuracion(db: Session, datos):
    config = obtener_configuracion(db)
    if not config:
        return None
    config.nombre_institucion = datos.nombre_institucion
    config.direccion = datos.direccion
    config.contacto = datos.contacto
    config.dias_operacion = datos.dias_operacion
    config.duracion_sesion_minutos = datos.duracion_sesion_minutos
    db.commit()
    db.refresh(config)
    return config


def actualizar_logo(db: Session, logo_url: str):
    config = obtener_configuracion(db)
    if not config:
        return None
    config.logo_url = logo_url
    db.commit()
    db.refresh(config)
    return config