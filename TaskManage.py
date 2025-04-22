from datetime import datetime
import uuid
import json
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
    def __init__(self, json_file="tasks.json"):
        self.tasks = []
        self.json_file = json_file
        self.load_tasks_from_json()

    def add_task(self, task):
        self.tasks.append(task)

    def mark_as_completed(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                print(f"Task ID {task_id} has been marked as completed.")
                return
        print(f"Task ID {task_id} not found.")
    
    def delete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                print(f"Task ID {task_id} has been deleted.")
                return
        print(f"Task ID {task_id} not found.")

    def save_tasks_to_json(self):
        with open(self.json_file, 'w') as file:
            json.dump([task for task in self.tasks], file, default=str, indent=4)
            print(f"Tasks have been saved to {self.json_file}")

    def load_tasks_from_json(self):
        try:
            with open(self.json_file, 'r') as file:
                data = json.load(file)
                for task_data in data:
                    task_data['due_date'] = datetime.strptime(task_data['due_date'], "%Y-%m-%d").date()
                    self.tasks.append(task_data)
                print(f"Tasks have been loaded from {self.json_file}")
        except FileNotFoundError:
            print(f"{self.json_file} not found. Starting with an empty task list.")

    def display_task(self):
        print('not Completed:')
        for task in self.tasks:
            if not task['completed']:
                print(f"Task ID: {task['id']}, Title: {task['title']}, Description: {task['description']}, Due Date: {task['due_date']}")

        print('Completed:')
        for task in self.tasks:
            if task['completed']:
                print(f"Task ID: {task['id']}, Title: {task['title']}, Description: {task['description']}, Due Date: {task['due_date']}")

    def search_task(self, keyword=None, due_date=None):
        results = []

        if keyword:
            results = [task for task in self.tasks if keyword.lower() in task['title'].lower() or keyword.lower() in task['description'].lower()]
        
        if due_date:
            try:
                due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
                results = [task for task in self.tasks if task['due_date'] == due_date]
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD format.")
        
        return results