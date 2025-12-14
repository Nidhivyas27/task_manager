import datetime
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models import Task
from schemas import TaskRequest, TaskResponse
from task_enum import TaskStatus


class TaskService:

    @staticmethod
    async def create_task(db: Session, payload: TaskRequest) -> TaskResponse:
        task = Task(
            task=payload.task,
            description=payload.description,
            priority=payload.priority,
            status=payload.status or TaskStatus.pending.value,
            due_date=datetime.datetime.strptime(payload.due_date, "%d/%m/%Y %H:%M:%S"),
        )
        db.add(task)
        db.commit()
        db.refresh(task)

        return TaskResponse.from_model(task)

    @staticmethod
    async def list_tasks(db: Session) -> list[TaskResponse]:
        tasks = db.query(Task).all()

        return [TaskResponse.from_model(t) for t in tasks]

    @staticmethod
    async def get_task(db: Session, task_id: int) -> TaskResponse:
        task = db.query(Task).filter(Task.id == task_id).first()

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found",
            )

        return TaskResponse.from_model(task)

    @staticmethod
    async def update_task(
        db: Session, task_id: int, payload: TaskRequest
    ):
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            return None

        task.task = payload.task
        task.description = payload.description
        task.priority = payload.priority
        task.status = payload.status
        task.due_date = datetime.datetime.fromtimestamp(payload.due_date)

        db.commit()
        db.refresh(task)

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found",
            )

        return TaskResponse.from_model(task)

    @staticmethod
    async def delete_task(db: Session, task_id: int) -> dict:
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found",
            )

        db.delete(task)
        db.commit()

        return {"message": "Task deleted successfully"}
