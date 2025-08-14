import json
import os
from datetime import datetime

FILE_NAME = "habits.json"

# Load data
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {}

# Save data
def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

# Add a new habit
def add_habit():
    habit = input("Enter new habit name: ").strip()
    data = load_data()
    if habit in data:
        print("Habit already exists!")
    else:
        data[habit] = {"created": str(datetime.today().date()), "history": []}
        save_data(data)
        print(f"Habit '{habit}' added!")

# Mark habit as done today
def mark_habit():
    data = load_data()
    if not data:
        print("No habits to mark.")
        return
    print("\nYour Habits:")
    for i, habit in enumerate(data.keys(), 1):
        print(f"{i}. {habit}")
    choice = int(input("Choose habit number to mark as done: ")) - 1
    habit_name = list(data.keys())[choice]
    today = str(datetime.today().date())
    if today in data[habit_name]["history"]:
        print("Already marked for today!")
    else:
        data[habit_name]["history"].append(today)
        save_data(data)
        print(f"Habit '{habit_name}' marked as done for today!")

# View habit progress
def view_habits():
    data = load_data()
    if not data:
        print("No habits found.")
        return
    for habit, details in data.items():
        print(f"\n📌 {habit} (Created: {details['created']})")
        print(f"   Completed Days: {len(details['history'])}")
        print(f"   History: {', '.join(details['history']) if details['history'] else 'No progress yet'}")

# Menu
def menu():
    while True:
        print("\n=== Habit Tracker Menu ===")
        print("1. Add Habit")
        print("2. Mark Habit Done")
        print("3. View Habits")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_habit()
        elif choice == "2":
            mark_habit()
        elif choice == "3":
            view_habits()
        elif choice == "4":
            print("Goodbye! Keep building habits! 💪")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
