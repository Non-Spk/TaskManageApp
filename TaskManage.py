class Task:
    def __init__(self, title: str, description: str, due_date: str, completed=False):
        self.id = self.generate_id()
        self.title = title
        self.description = description
        self.due_date = due_date 
        self.completed = completed

    def generate_id(self):
        import uuid
        return str(uuid.uuid4())