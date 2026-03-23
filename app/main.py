# app/main.py
from fastapi import FastAPI
from .routers import messages
from .database import engine, Base

# Generación de tablas en la base de datos
Base.metadata.create_all(bind=engine)

description = """
## Bienvenido a mi Nodo de Conexion en la Nube

Esta es una API REST profesional diseñada para demostrar el uso de FastAPI y el despliegue de servicios en Azure.

### Instrucciones de uso
1. Registro de visitas: Dirigete a POST /messages/, pulsa en "Try it out", completa los campos con tu nombre y algun comentario, y finalmente haz clic en "Execute" para guardar los datos.
2. Consulta de la comunidad: En GET /messages/, pulsa en "Try it out" y luego en "Execute" para visualizar todos los mensajes registrados por otros visitantes en tiempo real.
3. Persistencia: Al ejecutar las peticiones, los datos se almacenan de forma permanente en una base de datos PostgreSQL alojada en Azure.

Stack Tecnico: Python | FastAPI | SQLAlchemy | PostgreSQL | Azure App Service.
"""

app = FastAPI(
    title="Global Task & Networking API",
    description=description,
    version="1.1.0",
    contact={
        "name": "Josue",
        "url": "https://www.linkedin.com/in/josuecristhoper/",
    }
)

app.include_router(messages.router)

@app.get("/", tags=["Status"])
def root():
    return {
        "status": "online",
        "message": "API desplegada con exito. Visita /docs para interactuar."
    }