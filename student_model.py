class Student:
    def __init__(self, roll_no, name, department):
        self.roll_no = roll_no
        self.name = name
        self.department = department

    def to_dict(self):
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "department": self.department
        }
