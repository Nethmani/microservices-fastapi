# student- service/main.py
from fastapi import FastAPI, HTTPException, status
from models import Student, StudentCreate, StudentUpdate
from service import StudentService
from typing import List
app = FastAPI(title="Student Microservice", version="1.0.0")
# Initialize service
student_service = StudentService()

@app.get("/")
def read_root():
 return {"message": "Student Microservice is running"}
@app.get("/api/students", response_model=List[Student])
def get_all_students():
 """Get all students"""
 return student_service.get_all()

@app.get("/api/students/{student_id}", response_model=Student)
def get_student(student_id: int):
 """Get a student by ID"""
 student = student_service.get_by_id(student_id)
 if not student:
  raise HTTPException(status_code=404, detail="Student not found")
 return student

@app.post("/api/students", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate):
 """Create a new student"""
 return student_service.create(student)

@app.put("/api/students/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentUpdate):
 """Update a student"""
 updated_student = student_service.update(student_id, student)
 if not updated_student:
  raise HTTPException(status_code=404, detail="Student not found")
 return updated_student

@app.delete("/api/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
 """Delete a student"""
 success = student_service.delete(student_id)
 if not success:
  raise HTTPException(status_code=404, detail="Student not found")
 return None