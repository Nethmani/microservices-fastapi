# student-service/models.py
from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    id: int
    name: str
    age: int
    email: str
    course: str

class StudentCreate(BaseModel):
    name: str
    age: int
    email: str
    course: str

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    course: Optional[str] = None
