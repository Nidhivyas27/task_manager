from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from schemas import TaskRequest, TaskResponse
from services import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskResponse)
async def create_task(payload: TaskRequest, db: Session = Depends(get_db)):
    return await TaskService.create_task(db, payload)

@router.get("/", response_model=list[TaskResponse])
async def list_tasks(db: Session = Depends(get_db)):
    return await TaskService.list_tasks(db)

@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int, db: Session = Depends(get_db)):
    return await TaskService.get_task(db, task_id)

@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, payload: TaskRequest, db: Session = Depends(get_db)):
    return await TaskService.update_task(db, task_id, payload)

@router.delete("/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    return await TaskService.delete_task(db, task_id)
