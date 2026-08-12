from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.usuarios.routes import router as usuarios_router
from app.academico.routes import router as academico_router
from app.espacios.routes import router as espacios_router
from app.horarios.routes import router as horarios_router
from app.solicitudes.routes import router as solicitudes_router
from app.notificaciones.routes import router as notificaciones_router
from app.configuracion.routes import router as configuracion_router

app = FastAPI(title="Sistema de Gestion de Horarios y Espacios Academicos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(usuarios_router)
app.include_router(academico_router)
app.include_router(espacios_router)
app.include_router(horarios_router)
app.include_router(solicitudes_router)
app.include_router(notificaciones_router)
app.include_router(configuracion_router)


@app.get("/")
def root():
    return {"mensaje": "API del Sistema de Gestion de Horarios funcionando correctamente"}