from fastapi import FastAPI, HTTPException, status
from typing import List
from models import Course, CourseCreate, CourseUpdate
from service import CourseService

app = FastAPI(title="Course Microservice", version="1.0.0")
svc = CourseService()

@app.get("/")
def root():
    return {"message": "Course Microservice is running"}

@app.get("/api/courses", response_model=List[Course])
def get_all():
    return svc.get_all()

@app.get("/api/courses/{course_id}", response_model=Course)
def get_one(course_id: int):
    course = svc.get_by_id(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.post("/api/courses", response_model=Course, status_code=status.HTTP_201_CREATED)
def create(course: CourseCreate):
    return svc.create(course)

@app.put("/api/courses/{course_id}", response_model=Course)
def update(course_id: int, course: CourseUpdate):
    updated = svc.update(course_id, course)
    if not updated:
        raise HTTPException(status_code=404, detail="Course not found")
    return updated

@app.delete("/api/courses/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(course_id: int):
    ok = svc.delete(course_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Course not found")
    return None
