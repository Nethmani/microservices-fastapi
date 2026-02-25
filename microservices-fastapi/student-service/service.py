# student-service/service.py
from data_service import StudentMockDataService

class StudentService:
    def __init__(self):
        self.data_service = StudentMockDataService()

    def get_all(self):
        return self.data_service.get_all_students()

    def get_by_id(self, student_id: int):
        return self.data_service.get_student_by_id(student_id)

    def create(self, student_data):
        return self.data_service.add_student(student_data)

    def update(self, student_id: int, student_data):
        return self.data_service.update_student(student_id, student_data)

    def delete(self, student_id: int):
        return self.data_service.delete_student(student_id)
