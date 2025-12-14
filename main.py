from fastapi import FastAPI
from database.db import engine, Base
from router import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")
app.include_router(router)


@app.get("/")
def health():
    return {"status": "running"}