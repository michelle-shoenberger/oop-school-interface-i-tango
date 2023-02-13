from classes.person import Person
import os, csv  

class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id

    @classmethod
    def all_staff(cls):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/staff.csv")
        lst = []
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                lst.append(Staff(**dict(row)))
        return lst