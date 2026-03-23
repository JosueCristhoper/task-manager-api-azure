# app/main.py
from fastapi import FastAPI
from .routers import tasks
from .database import engine, Base

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="API profesional para gestionar tareas",
    version="1.0.0"
)

# Incluir rutas
app.include_router(tasks.router)

# Ruta inicial simple
@app.get("/")
def root():
    return {"message": "Bienvenido a Task Manager API 🚀"}