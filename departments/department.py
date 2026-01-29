class Department:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.descrition = description

    def __str__(self):
        return self.name