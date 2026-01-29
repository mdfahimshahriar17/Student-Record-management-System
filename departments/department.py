class Department:
    def __init__(self, dept_id, name):
        self.dept_id = str(dept_id).strip()
        self.name = str(name).strip()

    def to_dict(self):
        return {
            "dept_id": self.dept_id,
            "name": self.name
        }

    def __str__(self):
        return f"{self.dept_id} | {self.name}"
