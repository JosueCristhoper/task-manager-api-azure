# Global Task & Networking API

Esta es una API REST profesional desarrollada con FastAPI, diseñada para demostrar capacidades de arquitectura backend, persistencia de datos y despliegue escalable en la nube. Actualmente, funciona como un nodo interactivo de networking donde los usuarios pueden registrar mensajes y expectativas profesionales.

## Caracteristicas
- Documentacion Interactiva: Swagger UI integrada para pruebas de endpoints en tiempo real.
- Arquitectura Modular: Separacion clara de responsabilidades (Routers, Schemas, Modelos y CRUD).
- Validacion Robusta: Uso de Pydantic v2 para asegurar la integridad de los datos.
- Persistencia en la Nube: Integracion completa con PostgreSQL (Azure Database for PostgreSQL Flexible Server).
- Seguridad: Gestion de credenciales mediante variables de entorno (python-dotenv).
- Despliegue Cloud: Alojado en Azure App Service con flujo de CI/CD via GitHub Actions.

## Stack Tecnologico
- Lenguaje: Python 3.13+
- Framework: FastAPI
- ORM: SQLAlchemy (PostgreSQL Driver: psycopg2)
- Base de Datos: PostgreSQL (Azure)
- Servidor ASGI: Uvicorn
- Cloud: Microsoft Azure

## Instalacion y Uso Local

Si desea ejecutar este proyecto localmente conectado a la base de datos cloud:

1. Clonar el repositorio:
   git clone https://github.com/JosueCristhoper/task-manager-api-azure.git

2. Crear y activar un entorno virtual:
   python -m venv venv
   # En Windows:
   venv\Scripts\activate

3. Instalar dependencias:
   pip install -r requirements.txt

4. Configurar variables de entorno:
   Crear un archivo llamado `.env` en la raiz del proyecto con el siguiente formato:
   ```text
   DB_USER=tu_usuario
   DB_PASSWORD=tu_contraseña
   DB_HOST=tu_host_azure
   DB_PORT=5432
   DB_NAME=postgres
   ```

5. Iniciar el servidor:
   uvicorn app.main:app --reload

6. Acceder a la documentacion:
   Visita http://127.0.0.1:8000/docs para interactuar con la API.

---
Desarrollado por Josue (https://www.linkedin.com/in/josuecristhoper/)