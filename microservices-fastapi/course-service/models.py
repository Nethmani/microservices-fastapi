from pydantic import BaseModel
from typing import Optional

class Course(BaseModel):
    id: int
    title: str
    code: str
    credits: int

class CourseCreate(BaseModel):
    title: str
    code: str
    credits: int

class CourseUpdate(BaseModel):
    title: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
