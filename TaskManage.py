import json
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
    
    def to_dict(self):
        """Convert task object to dictionary for JSON serialization"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date.strftime("%Y-%m-%d"),  # Convert date to string format
            "completed": self.completed
        }

class TaskManager:
    def __init__(self, json_file="tasks.json"):
        self.tasks = []
        self.json_file = json_file
        self.load_tasks_from_json()

    def add_task(self, task):
        """Add a new task to the task list"""
        task_dict = task.to_dict()
        self.tasks.append(task_dict)
        print(f"Task '{task.title}' has been added.")
        return task_dict

    def mark_as_completed(self, task_id):
        """Mark a task as completed based on its ID"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                print(f"Task ID {task_id} has been marked as completed.")
                return True
        print(f"Task ID {task_id} not found.")
        return False
    
    def delete_task(self, task_id):
        """Delete a task based on its ID"""
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                print(f"Task ID {task_id} has been deleted.")
                return True
        print(f"Task ID {task_id} not found.")
        return False

    def save_tasks_to_json(self):
        """Save all tasks to the JSON file"""
        with open(self.json_file, 'w') as file:
            json.dump(self.tasks, file, indent=4)
            print(f"Tasks have been saved to {self.json_file}")

    def load_tasks_from_json(self):
        """Load tasks from the JSON file"""
        try:
            with open(self.json_file, 'r') as file:
                self.tasks = json.load(file)
                print(f"Tasks have been loaded from {self.json_file}")
        except FileNotFoundError:
            print(f"{self.json_file} not found. Starting with an empty task list.")

    def display_tasks(self):
        """Display all tasks grouped by completion status"""
        pending_tasks = [task for task in self.tasks if not task['completed']]
        completed_tasks = [task for task in self.tasks if task['completed']]
        
        if not self.tasks:
            print("No tasks available.")
            return
        
        print("\n=== PENDING TASKS ===")
        if pending_tasks:
            for task in pending_tasks:
                self._print_task(task)
        else:
            print("No pending tasks.")
            
        print("\n=== COMPLETED TASKS ===")
        if completed_tasks:
            for task in completed_tasks:
                self._print_task(task)
        else:
            print("No completed tasks.")

    def _print_task(self, task):
        """Helper method to print a single task with consistent formatting"""
        print(f"ID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date']}")
        print("-" * 40)

    def search_tasks(self, keyword=None, due_date=None):
        """Search tasks by keyword and/or due date"""
        if not keyword and not due_date:
            return []
            
        results = self.tasks
        
        # Filter by keyword if provided
        if keyword:
            results = [task for task in results 
                      if keyword.lower() in task['title'].lower() 
                      or keyword.lower() in task['description'].lower()]
        
        # Filter by due date if provided
        if due_date:
            try:
                parsed_date = datetime.strptime(due_date, "%Y-%m-%d").date().strftime("%Y-%m-%d")
                results = [task for task in results if task['due_date'] == parsed_date]
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD format.")
                return []
        
        return results

    def display_search_results(self, tasks):
        """Display search results in a formatted way"""
        if not tasks:
            print("No tasks found matching your search criteria.")
            return
            
        print(f"\n=== SEARCH RESULTS: {len(tasks)} TASK(S) FOUND ===")
        for task in tasks:
            self._print_task(task)

    def validate_task_input(self, title, due_date):
        """Validate task input data"""
        if not title.strip():
            print("Error: Title cannot be empty.")
            return False
        
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Error: Due date must be in YYYY-MM-DD format.")
            return False
            
        return True

def display_menu():
    """Display the main menu options"""
    print("\n" + "=" * 30)
    print("       TASK MANAGER")
    print("=" * 30)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Search Tasks")
    print("6. Exit")
    print("=" * 30)

def main():
    manager = TaskManager()

    while True:
        display_menu()

        choice = input("\nChoose an option (1-6): ")

        if choice == '1': 
            print("\n--- ADD NEW TASK ---")
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")

            if manager.validate_task_input(title, due_date):
                try:
                    new_task = Task(title, description, due_date)
                    manager.add_task(new_task)
                    manager.save_tasks_to_json()
                except ValueError as e:
                    print(f"Error: {e}")

        elif choice == '2':
            manager.display_tasks()

        elif choice == '3': 
            print("\n--- MARK TASK AS COMPLETED ---")
            manager.display_tasks()
            task_id = input("\nEnter task ID to mark as completed: ")
            if manager.mark_as_completed(task_id):
                manager.save_tasks_to_json()

        elif choice == '4':
            print("\n--- DELETE TASK ---")
            manager.display_tasks()
            task_id = input("\nEnter task ID to delete: ")
            if manager.delete_task(task_id):
                manager.save_tasks_to_json()

        elif choice == '5':
            print("\n--- SEARCH TASKS ---")
            keyword = input("Enter keyword to search (or press enter to skip): ")
            due_date = input("Enter due date to search (YYYY-MM-DD or press enter to skip): ")

            tasks = manager.search_tasks(keyword, due_date)
            manager.display_search_results(tasks)

        elif choice == '6':
            print("\nExiting Task Manager. Goodbye!")
            break

        else:
            print("\nInvalid option. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()