import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database.db import Base
from task_enum import TaskStatus

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, nullable=False)
    description = Column(String, nullable=True)
    priority = Column(Integer, nullable=False)
    status = Column(String, default=TaskStatus.pending.value, nullable=False)
    created_date = Column(
    DateTime, default=datetime.datetime.now(), nullable=False
    )
    due_date = Column(DateTime, nullable=False)
