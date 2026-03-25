# app/schemas.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    # cambiamos string por ejemplos reales de guia al usuario
    title: str = Field(..., example="Tu Nombre (Ej: María García / Tech Solutions)")
    description: Optional[str] = Field(None, example="Me parece una API genial, ¡espero aprender mucho de Azure!")

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    # Esto es por si alguien quiere editar su mensaje
    title: Optional[str] = Field(None, example="Nombre Actualizado")
    description: Optional[str] = Field(None, example="Nueva reseña o comentario")
    completed: Optional[bool] = Field(None, example=True)

class TaskOut(TaskBase):
    id: int
    completed: bool

    # Añadimos el atributo nuevo para la fecha
    created_at: datetime

    model_config = {
        "from_attributes": True
    }