# app/routers/tasks.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, database

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

# Dependency para obtener DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Obtener todas las tareas
@router.get("/", response_model=List[schemas.TaskOut])
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

# Crear nueva tarea
@router.post("/", response_model=schemas.TaskOut)
def create_new_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

# Obtener tarea por id
@router.get("/{task_id}", response_model=schemas.TaskOut)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

# Actualizar tarea
@router.put("/{task_id}", response_model=schemas.TaskOut)
def update_existing_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = crud.update_task(db, task_id, task)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

# Eliminar tarea
@router.delete("/{task_id}", response_model=schemas.TaskOut)
def delete_existing_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.delete_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task