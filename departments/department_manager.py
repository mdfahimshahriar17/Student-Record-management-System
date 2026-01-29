import os
import json
from departments.department import Department


class DepartmentManager:
    def __init__(self):
        self.data_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "data", "departments.json")
        )
        self.departments = []
        self.load_departments()

    def load_departments(self):
        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.departments = [Department(**d) for d in data]
        except:
            self.departments = []

    def save_departments(self):
        # Create data folder if it doesn't exist
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)

        data = [d.to_dict() for d in self.departments]
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add_department(self, dept_id, name):
        # duplicate check (id or name)
        for d in self.departments:
            if d.dept_id == str(dept_id).strip() or d.name.lower() == str(name).strip().lower():
                print("Department already exists!")
                return None

        dept = Department(dept_id, name)
        self.departments.append(dept)
        self.save_departments()
        print(f"[Department '{dept.name}' added!]")
        return dept

    def get_department(self, query):
        """dept_id/name partial match -> first match"""
        q = str(query).strip().lower()

        for d in self.departments:
            if q in d.dept_id.lower() or q in d.name.lower():
                return d
        return None

    def exists(self, name_or_id):
        """Exact match only (prevents wrong partial matches)"""
        key = str(name_or_id).strip().lower()
        for d in self.departments:
            if d.dept_id.lower() == key or d.name.lower() == key:
                return True
        return False

    def list_departments(self):
        if not self.departments:
            print("No departments found")
            return

        print("\nDepartments:")
        for d in self.departments:
            print("-", d)
