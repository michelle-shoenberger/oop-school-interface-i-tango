from classes.student import Student
from classes.staff import Staff

class School:
    def __init__(self, name, address=None):
        self.name = name
        self.address = address
        self.staff = Student.all_students()
        self.students = Staff.all_staff()
