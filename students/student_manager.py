import os
import json
from students.student import Student


class StudentManager:
    def __init__(self):
        self.data_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "data", "students.json")
        )
        self.students = []
        self.load_students()

    def load_students(self):
        """Read students.json and load into self.students"""
        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.students = [Student(**st_data) for st_data in data]
        except:
            self.students = []

    def save_students(self):
        # Create data folder if it doesn't exist
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)

        data = [s.to_dict() for s in self.students]
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def roll_exists(self, roll):
        """Duplicate roll check"""
        for s in self.students:
            if s.roll == roll:
                return True
        return False

    def add_student(self, roll, name, department, email):
        """Takes roll as user input and does not add if the roll already exists"""
        if self.roll_exists(roll):
            return None

        student = Student(roll, name, department, email)
        self.students.append(student)
        self.save_students()
        return student

    def search_students(self, keyword):
        """Partial match: roll/name/email"""
        k = str(keyword).strip().lower()
        result = []

        for s in self.students:
            if k in str(s.roll) or k in s.name.lower() or k in s.email.lower():
                result.append(s)

        return result

    def get_student(self, roll):
        """Exact roll match"""
        for s in self.students:
            if s.roll == roll:
                return s
        return None

    def remove_student(self, roll):
        """Remove by exact roll"""
        for i, s in enumerate(self.students):
            if s.roll == roll:
                self.students.pop(i)
                self.save_students()
                return True
        return False

    def list_students(self):
        if not self.students:
            print("No students found")
            return

        print("\nRegistered Students:")
        for s in self.students:
            print("-", s)
