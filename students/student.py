from datetime import datetime

class Student:
    def __init__(self, roll, name, department, email):
        self.roll = roll
        self.name = name
        self.department = department
        self.email = email

        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"{self.roll} | {self.name} | {self.department} | {self.email}"

    def to_dict(self):
        return {
            "roll": self.roll,
            "name": self.name,
            "department": self.department,
            "email": self.email,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }