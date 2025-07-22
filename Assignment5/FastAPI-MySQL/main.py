from fastapi import FastAPI, status, Depends, HTTPException
from pydantic import BaseModel
from typing import Annotated
from sqlalchemy.orm import Session

import models
from database import engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Pydantic model for creating todos (request body)
class TodoCreate(BaseModel):
    task_body: str
    due_day: int
    due_month: str
    due_year: int

# Pydantic model for response (if needed)
class TodoBase(TodoCreate):
    id: int

    class Config:
        orm_mode = True

# Database dependency shortcut
db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/todos/", status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoCreate, db: db_dependency):
    try:
        db_todo = models.Todo(**todo.model_dump())  # Unpack validated fields
        db.add(db_todo)
        db.commit()
        return {"detail": "Todo added successfully"}
    except Exception as e:
        print(f"Error occurred: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/todos", status_code=status.HTTP_200_OK)
async def get_todos(db: db_dependency):
    return db.query(models.Todo).all()

@app.put("/todos/{todo_id}", response_model=TodoBase, status_code=status.HTTP_200_OK)
async def update_todo(
    todo_id: int,
    todo_request: TodoCreate,
    db: db_dependency
):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()

    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    db_todo.task_body = todo_request.task_body
    db_todo.due_day = todo_request.due_day
    db_todo.due_month = todo_request.due_month
    db_todo.due_year = todo_request.due_year

    db.commit()
    db.refresh(db_todo)

    return db_todo

@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int, db: db_dependency):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()

    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(db_todo)
    db.commit()

    return None  # Ensures no response body is returned
