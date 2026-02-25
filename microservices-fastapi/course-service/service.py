from data_service import CourseMockDataService

class CourseService:
    def __init__(self):
        self.data = CourseMockDataService()

    def get_all(self):
        return self.data.get_all()

    def get_by_id(self, course_id: int):
        return self.data.get_by_id(course_id)

    def create(self, course_data):
        return self.data.add(course_data)

    def update(self, course_id: int, course_data):
        return self.data.update(course_id, course_data)

    def delete(self, course_id: int):
        return self.data.delete(course_id)
