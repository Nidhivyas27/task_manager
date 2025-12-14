import typer
import requests
from rich.console import Console
from rich.table import Table
import datetime

app = typer.Typer(help="Task Management CLI")
console = Console()

API_URL = "http://127.0.0.1:8000"
DATE_FORMAT = "%d/%m/%Y %H:%M:%S"


def validate_date(date_str: str) -> str:
    try:
        datetime.datetime.strptime(date_str, DATE_FORMAT)
        return date_str
    except ValueError:
        raise typer.BadParameter(
            "Invalid date format. Use DD/MM/YYYY HH:MM:SS"
        )


@app.command()
def create(
    task: str,
    due_date: str = typer.Option(
        ...,
        help="Format: DD/MM/YYYY HH:MM:SS",
        callback=lambda v: validate_date(v),
    ),
    priority: int = typer.Option(1, help="1=Low, 2=Medium, 3=High"),
    description: str = typer.Option(None),
    status: str = typer.Option("pending"),
):
    payload = {
        "task": task,
        "description": description,
        "priority": priority,
        "status": status,
        "due_date": due_date,
    }

    response = requests.post(f"{API_URL}/tasks/", json=payload)

    if response.status_code == 200:
        console.print("[green]Task created successfully[/green]")
        console.print(response.json())
    else:
        console.print(f"[red]Error:[/red] {response.text}")


@app.command("list")
def list_tasks():
    response = requests.get(f"{API_URL}/tasks/")

    if response.status_code != 200:
        console.print("[red]Failed to fetch tasks[/red]")
        return

    tasks = response.json()

    table = Table(title="Tasks")
    table.add_column("ID", justify="right")
    table.add_column("Task")
    table.add_column("Priority")
    table.add_column("Status")
    table.add_column("Created Date")
    table.add_column("Due Date")

    for t in tasks:
        table.add_row(
            str(t["id"]),
            t["task"],
            str(t["priority"]),
            t["status"],
            t["created_date"],
            t["due_date"],
        )

    console.print(table)


@app.command()
def get(task_id: int):
    response = requests.get(f"{API_URL}/tasks/{task_id}")

    if response.status_code != 200:
        console.print("[red]Task not found[/red]")
        return

    console.print(response.json())


@app.command()
def update(
    task_id: int,
    task: str,
    due_date: str = typer.Option(
        ...,
        help="Format: DD/MM/YYYY HH:MM:SS",
        callback=lambda v: validate_date(v),
    ),
    priority: int = typer.Option(...),
    description: str = typer.Option(None),
    status: str = typer.Option(...),
):
    payload = {
        "task": task,
        "description": description,
        "priority": priority,
        "status": status,
        "due_date": due_date,
    }

    response = requests.put(f"{API_URL}/tasks/{task_id}", json=payload)

    if response.status_code == 200:
        console.print("[green]Task updated successfully[/green]")
        console.print(response.json())
    else:
        console.print(f"[red]Error:[/red] {response.text}")


@app.command()
def delete(task_id: int):
    response = requests.delete(f"{API_URL}/tasks/{task_id}")

    if response.status_code == 200:
        console.print("[green]Task deleted successfully[/green]")
    else:
        console.print(f"[red]Error:[/red] {response.text}")


if __name__ == "__main__":
    app()
