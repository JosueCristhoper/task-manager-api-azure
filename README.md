# Global Task & Networking API

Esta es una API REST profesional desarrollada con FastAPI y diseñada para demostrar capacidades de desarrollo backend y despliegue de servicios en la nube. Actualmente, el proyecto funciona como un nodo interactivo donde los usuarios pueden registrar mensajes y expectativas profesionales.

## Caracteristicas
- Documentacion interactiva con Swagger UI para pruebas directas.
- Arquitectura modular con separacion de responsabilidades (routers, schemas, modelos y CRUD).
- Uso de Pydantic v2 para la validacion de datos y tipado fuerte.
- Preparado para integracion con bases de datos PostgreSQL en entornos de produccion.

## Stack Tecnologico
- Python 3.x
- FastAPI
- SQLAlchemy
- SQLite (Entorno de desarrollo)
- Uvicorn

## Instalacion y Uso Local

Para ejecutar este proyecto en su entorno local, siga estos pasos:

1. Clonar el repositorio:
   git clone https://github.com/tu-usuario/task-manager-api-azure.git

2. Crear y activar un entorno virtual:
   python -m venv venv
   En Windows: venv\Scripts\activate
   En macOS/Linux: source venv/bin/activate

3. Instalar las dependencias necesarias:
   pip install -r requirements.txt

4. Iniciar el servidor de desarrollo:
   uvicorn app.main:app --reload

5. Acceder a la documentacion:
   Una vez iniciado el servidor, abra su navegador en http://127.0.0.1:8000/docs para interactuar con los endpoints de la API.

---
Desarrollado por Josue (https://www.linkedin.com/in/josuecristhoper/)