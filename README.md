# Task Manager Application

A command-line task management system built with Python that helps users organize their daily tasks efficiently.

## Features

- **Add Tasks**: Create new tasks with title, description, and due date
- **View Tasks**: Display all tasks organized by completion status
- **Mark as Completed**: Update the status of tasks when completed
- **Delete Tasks**: Remove tasks that are no longer needed
- **Search Tasks**: Find tasks by keyword or due date
- **Persistent Storage**: Save and load tasks using JSON for data persistence

## Requirements

- Python 3.6 or higher
- Standard Python libraries (no external dependencies)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Non-Spk/TaskManageApp.git
   ```

2. Run the application:
   ```
   python TaskManage.py
   ```

## Usage

When you run the program, you'll see a menu with the following options:

1. **Add Task**: Add a new task to your list
2. **View Tasks**: Display all your tasks, separated into pending and completed categories
3. **Mark Task as Completed**: Change a task's status to completed
4. **Delete Task**: Remove a task from your list
5. **Search Tasks**: Find tasks by keyword or due date
6. **Exit**: Quit the application

### Adding a Task

To add a new task, select option 1 from the menu and provide:
- Title: A brief name for your task
- Description: Details about the task
- Due Date: The deadline in YYYY-MM-DD format

Each task is automatically assigned a unique ID for reference.

### Viewing Tasks

Tasks are displayed in two categories:
- Pending Tasks: Tasks that need to be completed
- Completed Tasks: Tasks that have been marked as done

### Marking a Task as Completed

Select option 3 and enter the ID of the task you want to mark as completed.

### Deleting a Task

Select option 4 and enter the ID of the task you want to delete.

### Searching Tasks

Select option, then:
- Enter a keyword to search in titles and descriptions (or press Enter to skip)
- Enter a due date in YYYY-MM-DD format (or press Enter to skip)

You can search by keyword, due date, or both.

## Data Storage

All tasks are saved to a `tasks.json` file in the same directory as the application. This file is automatically created the first time you add a task and is loaded each time the application starts.

## Code Structure

- `Task` class: Represents a single task with its properties
- `TaskManager` class: Handles task operations and storage
- CLI interface: Provides a user-friendly command-line interface

## Example

```
==============================
       TASK MANAGER
==============================
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Search Tasks
6. Exit
==============================

Choose an option (1-6): 1

--- ADD NEW TASK ---
Enter task title: Complete project report
Enter task description: Finish the quarterly project report for the team
Enter due date (YYYY-MM-DD): 2025-04-30
Task 'Complete project report' has been added.
Tasks have been saved to tasks.json
```
