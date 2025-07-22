from sqlalchemy import Column, Integer, String
from database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    task_body = Column(String(500))
    due_day = Column(Integer)
    due_month = Column(String(10))
    due_year = Column(Integer)