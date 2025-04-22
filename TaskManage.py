from datetime import datetime
import uuid
class Task:
    def __init__(self, title: str, description: str, due_date: str, completed=False):
        self.id = self.generate_id()
        self.title = title
        self.description = description
        try:
            self.due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Due date must be in YYYY-MM-DD format")
        self.completed = completed

    def generate_id(self):
        return str(uuid.uuid4())
    
    def create_task(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "completed": self.completed
        }
    

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def mark_as_completed(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                print(f"Task ID {task_id} has been marked as completed.")
                return
        print(f"Task ID {task_id} not found.")

    def display_task(self):
        print('not Completed:')
        for task in self.tasks:
            if not task.completed:
                print(f"Task ID: {task.id}, Title: {task.title}, Description: {task.description}, Due Date: {task.due_date}")

        print('Completed:')
        for task in self.tasks:
            if task.completed:
                print(f"Task ID: {task.id}, Title: {task.title}, Description: {task.description}, Due Date: {task.due_date}")
