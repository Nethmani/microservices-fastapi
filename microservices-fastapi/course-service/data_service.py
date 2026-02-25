from models import Course

class CourseMockDataService:
    def __init__(self):
        self.courses = [
            Course(id=1, title="Intro to Programming", code="CS101", credits=3),
            Course(id=2, title="Database Systems", code="IT202", credits=3),
            Course(id=3, title="Software Engineering", code="SE303", credits=4),
        ]
        self.next_id = 4

    def get_all(self):
        return self.courses

    def get_by_id(self, course_id: int):
        return next((c for c in self.courses if c.id == course_id), None)

    def add(self, course_data):
        new_course = Course(id=self.next_id, **course_data.dict())
        self.courses.append(new_course)
        self.next_id += 1
        return new_course

    def update(self, course_id: int, course_data):
        course = self.get_by_id(course_id)
        if course:
            update_data = course_data.dict(exclude_unset=True)
            for k, v in update_data.items():
                setattr(course, k, v)
            return course
        return None

    def delete(self, course_id: int):
        course = self.get_by_id(course_id)
        if course:
            self.courses.remove(course)
            return True
        return False
