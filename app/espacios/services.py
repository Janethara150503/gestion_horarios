from sqlalchemy.orm import Session
from app.espacios.models import Edificio, Aula
from app.espacios import schemas


def crear_edificio(db: Session, datos: schemas.EdificioCreate):
    nuevo = Edificio(**datos.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def listar_edificios(db: Session):
    return db.query(Edificio).all()


def crear_aula(db: Session, datos: schemas.AulaCreate):
    nueva = Aula(**datos.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


def listar_aulas(db: Session):
    return db.query(Aula).all()