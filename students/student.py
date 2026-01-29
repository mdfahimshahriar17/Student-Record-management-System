class Student:
    def __init__(self, roll, name, department, email):
        self.roll = int(roll)
        self.name = name.strip()
        self.department = department.strip()
        self.email = email.strip().lower()

    def to_dict(self):
        return {
            "roll": self.roll,
            "name": self.name,
            "department": self.department,
            "email": self.email
        }

    def __str__(self):
        return f"{self.roll} | {self.name} | {self.department} | {self.email}"
