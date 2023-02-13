import os, csv      
from classes.person import Person


class Student(Person):
    def __init__(self, name, age, role, school_id, password):
        super().__init__(name, age, role, password)
        self.school_id = school_id

    @classmethod
    def all_students(cls):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        lst = []
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                lst.append(Student(**dict(row)))
        return lst