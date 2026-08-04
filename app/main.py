from fastapi import FastAPI
from app.usuarios.routes import router as usuarios_router

app = FastAPI(title="Sistema de Gestion de Horarios y Espacios Academicos")

app.include_router(usuarios_router)


@app.get("/")
def root():
    return {"mensaje": "API del Sistema de Gestion de Horarios funcionando correctamente"}