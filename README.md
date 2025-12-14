# Task Management API & CLI
A simple Task Management system built using FastAPI, SQLAlchemy, and SQLite, with a Typer-based CLI for interacting with the API from the command line.

This project demonstrates clean separation of concerns using:
- Database layer
- ORM models
- Pydantic schemas
- Service layer
- API routers
- CLI client

Features
- Create, list, retrieve, update, and delete tasks
- SQLite database with SQLAlchemy ORM
- Task priority and status management
- Due date validation
- RESTful API using FastAPI
- Command Line Interface using Typer and Rich

Tech Stack
- Backend API: FastAPI
- ORM: SQLAlchemy
- Database: SQLite
- CLI: Typer, Rich
- HTTP Client: Requests
- Validation: Pydantic

# Project Structure
```
.
├── database/
│   └── db.py
├── models.py
├── schemas.py
├── services.py
├── router.py
├── task_enum.py
├── task_cli.py
├── main.py
├── task.db
├── requirements.txt
└── README.md
```

# Task Status Enum
```
pending
in_progress
completed
```

# Installation
1. Clone the Repository
```
git clone <repository-url>
cd task-manager
```

2. Create Virtual Environment (Recommended)
```
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

3. Install Dependencies
```
pip install -r requirements.txt
```

# Running the API Server
```
uvicorn main:app --reload
```

# Database
- SQLite database file: task.db
- Tables are automatically created on application startup using:
```
Base.metadata.create_all(bind=engine)
```

# API Endpoints
```
| Method | Endpoint           | Description    |
| ------ | ------------------ | -------------- |
| POST   | `/tasks/`          | Create a task  |
| GET    | `/tasks/`          | List all tasks |
| GET    | `/tasks/{task_id}` | Get task by ID |
| PUT    | `/tasks/{task_id}` | Update task    |
| DELETE | `/tasks/{task_id}` | Delete task    |
```

# Task Payload Example
```
{
  "task": "Finish documentation",
  "description": "Write README file",
  "priority": 2,
  "status": "pending",
  "due_date": "20/12/2025 18:00:00"
}
```

# Date format:
- DD/MM/YYYY HH:MM:SS

# Using the CLI
- Create a Task
```
 python cli/task_cli.py create "Submit report" --due-date "25/01/2025 18:30:00" --priority 3 --status pending
 ```

 - List Tasks
 ```
 python task_cli.py list
```

- Get Task by ID
```
python task_cli.py get 1
```

- Update Task
```
python cli/task_cli.py update 1 "Submit report" --due-date "25/01/2025 18:30:00" --priority 3 --status completed
```

Delete Task
```
python task_cli.py delete 1
```

# Validation Rules
- Due Date must follow: DD/MM/YYYY HH:MM:SS
- Priority must be an integer
- Status must be one of:
    - pending
    - in_progress
    - completed
