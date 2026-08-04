from sqlalchemy.orm import Session
from app.academico.models import PeriodoAcademico, Programa, Materia, Grupo
from app.academico import schemas


# Periodos academicos
def crear_periodo(db: Session, datos: schemas.PeriodoAcademicoCreate):
    nuevo = PeriodoAcademico(**datos.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def listar_periodos(db: Session):
    return db.query(PeriodoAcademico).all()


# Programas
def crear_programa(db: Session, datos: schemas.ProgramaCreate):
    nuevo = Programa(**datos.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def listar_programas(db: Session):
    return db.query(Programa).all()


# Materias
def crear_materia(db: Session, datos: schemas.MateriaCreate):
    nuevo = Materia(**datos.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def listar_materias(db: Session):
    return db.query(Materia).all()


# Grupos
def crear_grupo(db: Session, datos: schemas.GrupoCreate):
    nuevo = Grupo(**datos.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def listar_grupos(db: Session):
    return db.query(Grupo).all()