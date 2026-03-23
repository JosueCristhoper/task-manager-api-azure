# app/routers/messages.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, database

router = APIRouter(
    prefix="/messages",
    tags=["Community Messages"]
)

# Dependency para obtener DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Obtener todos los mensajes
@router.get("/", response_model=List[schemas.TaskOut])
def read_messages(db: Session = Depends(get_db)): # Nombre cambiado
    return crud.get_tasks(db)

# Crear nuevo mensaje
@router.post("/", response_model=schemas.TaskOut)
def create_new_message(task: schemas.TaskCreate, db: Session = Depends(get_db)): # Nombre cambiado
    return crud.create_task(db, task)

# Obtener mensaje por id
@router.get("/{message_id}", response_model=schemas.TaskOut) # Cambiado a message_id
def read_message(message_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, message_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Message not found") # Texto cambiado
    return db_task

# Actualizar mensaje
@router.put("/{message_id}", response_model=schemas.TaskOut)
def update_existing_message(message_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = crud.update_task(db, message_id, task)
    if not db_task:
        raise HTTPException(status_code=404, detail="Message not found") # Texto cambiado
    return db_task

# Eliminar mensaje
@router.delete("/{message_id}", response_model=schemas.TaskOut)
def delete_existing_message(message_id: int, db: Session = Depends(get_db)):
    db_task = crud.delete_task(db, message_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Message not found") # Texto cambiado
    return db_task