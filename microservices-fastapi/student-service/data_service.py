# student-service/data_service.py
from models import Student

class StudentMockDataService:
    def __init__(self):
        self.students = [
            Student(id=1, name="John Doe", age=20, email="john@example.com", course="Computer Science"),
            Student(id=2, name="Jane Smith", age=22, email="jane@example.com", course="Information Technology"),
            Student(id=3, name="Bob Johnson", age=21, email="bob@example.com", course="Software Engineering"),
        ]
        self.next_id = 4

    def get_all_students(self):
        return self.students

    def get_student_by_id(self, student_id: int):
        return next((s for s in self.students if s.id == student_id), None)

    def add_student(self, student_data):
        new_student = Student(id=self.next_id, **student_data.dict())
        self.students.append(new_student)
        self.next_id += 1
        return new_student

    def update_student(self, student_id: int, student_data):
        student = self.get_student_by_id(student_id)
        if student:
            update_data = student_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(student, key, value)
            return student
        return None

    def delete_student(self, student_id: int):
        student = self.get_student_by_id(student_id)
        if student:
            self.students.remove(student)
            return True
        return False
