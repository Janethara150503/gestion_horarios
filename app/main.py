from fastapi import FastAPI

app = FastAPI(title="Sistema de Gestion de Horarios y Espacios Academicos")

@app.get("/")
def root():
    return {"mensaje": "API del Sistema de Gestion de Horarios funcionando correctamente"}