import datetime

from pydantic import BaseModel, ConfigDict


class TaskRequest(BaseModel):
    task: str
    description: str | None
    priority: int
    status: str
    due_date: str

    model_config = ConfigDict(from_attributes=True)


class TaskResponse(BaseModel):
    id: int
    task: str
    description: str | None
    priority: int
    status: str
    created_date: datetime.datetime
    due_date: datetime.datetime

    model_config = ConfigDict(from_attributes=True)

    @staticmethod
    def from_model(data) -> "TaskResponse":
        return TaskResponse(
            id=data.id,
            task=data.task,
            description=data.description,
            priority=data.priority,
            status=data.status,
            created_date=data.created_date,
            due_date=data.due_date,
        )
