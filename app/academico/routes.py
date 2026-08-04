from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.academico import services, schemas
from app.core.dependencies import requiere_rol, obtener_usuario_actual

router = APIRouter(prefix="/academico", tags=["academico"])


# Periodos academicos
@router.post("/periodos", response_model=schemas.PeriodoAcademicoOut)
def crear_periodo(
    datos: schemas.PeriodoAcademicoCreate,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_rol("coordinador")),
):
    return services.crear_periodo(db, datos)


@router.get("/periodos", response_model=list[schemas.PeriodoAcademicoOut])
def listar_periodos(db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
    return services.listar_periodos(db)


# Programas
@router.post("/programas", response_model=schemas.ProgramaOut)
def crear_programa(
    datos: schemas.ProgramaCreate,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_rol("coordinador")),
):
    return services.crear_programa(db, datos)


@router.get("/programas", response_model=list[schemas.ProgramaOut])
def listar_programas(db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
    return services.listar_programas(db)


# Materias
@router.post("/materias", response_model=schemas.MateriaOut)
def crear_materia(
    datos: schemas.MateriaCreate,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_rol("coordinador")),
):
    return services.crear_materia(db, datos)


@router.get("/materias", response_model=list[schemas.MateriaOut])
def listar_materias(db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
    return services.listar_materias(db)


# Grupos
@router.post("/grupos", response_model=schemas.GrupoOut)
def crear_grupo(
    datos: schemas.GrupoCreate,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_rol("coordinador")),
):
    return services.crear_grupo(db, datos)


@router.get("/grupos", response_model=list[schemas.GrupoOut])
def listar_grupos(db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
    return services.listar_grupos(db)