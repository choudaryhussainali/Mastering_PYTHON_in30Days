# project_todo_list.py
"""
📌 Simple To-Do List App
-------------------------
This project demonstrates:
- Lists and dictionaries
- Functions
- Loops
- File handling (JSON)
- Exception handling
- Modular code structure
"""

import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"


# Function to load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


# Function to save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks yet!")
    else:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✔" if task["done"] else "❌"
            print(f"{i}. {task['title']} [{status}]")


# Function to add a new task
def add_task(tasks):
    title = input("\n🆕 Enter task title: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("✅ Task added successfully!")
    else:
        print("⚠ Task title cannot be empty!")


# Function to mark a task as done
def mark_task_done(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("\n✔ Enter task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            save_tasks(tasks)
            print("✅ Task marked as done!")
        else:
            print("⚠ Invalid task number!")
    except ValueError:
        print("⚠ Please enter a valid number!")


# Function to delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("\n🗑 Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"✅ Task '{removed['title']}' deleted!")
        else:
            print("⚠ Invalid task number!")
    except ValueError:
        print("⚠ Please enter a valid number!")


# Main program loop
def main():
    tasks = load_tasks()

    while True:
        print("\n===== 📌 TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("➡ Enter your choice (1-5): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
