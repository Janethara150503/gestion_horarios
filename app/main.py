from fastapi import FastAPI
from app.usuarios.routes import router as usuarios_router
from app.academico.routes import router as academico_router

app = FastAPI(title="Sistema de Gestion de Horarios y Espacios Academicos")

app.include_router(usuarios_router)
app.include_router(academico_router)


@app.get("/")
def root():
    return {"mensaje": "API del Sistema de Gestion de Horarios funcionando correctamente"}