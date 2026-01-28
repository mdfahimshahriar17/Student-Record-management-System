class Student:
    def __init__(self, name, roll, email, department):
        self.name = name
        self.roll = roll
        self.email = email
        self.department = department

    
    
    def to_dict(self):
        return{
            "name": self.name,
            "roll": self.roll,
            "email": self.email,
            "department": self.department
        }
    