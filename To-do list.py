import os

# File to save tasks
TASKS_FILE = "tasks.txt"

# Load tasks from the file
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

# Save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display the tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

# Add a task
def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added to the list.")

# Remove a task
def remove_task(tasks):
    try:
        task_id = int(input("Enter the task number to remove: "))
        if task_id <= 0 or task_id > len(tasks):
            print("Invalid task number.")
        else:
            removed_task = tasks.pop(task_id - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed from the list.")
    except ValueError:
        print("Please enter a valid number.")

# Mark a task as completed
def mark_completed(tasks):
    try:
        task_id = int(input("Enter the task number to mark as completed: "))
        if task_id <= 0 or task_id > len(tasks):
            print("Invalid task number.")
        else:
            completed_task = tasks.pop(task_id - 1)
            save_tasks(tasks)
            print(f"Task '{completed_task}' marked as completed and removed from the list.")
    except ValueError:
        print("Please enter a valid number.")

# Main function to run the application
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as completed")
        print("5. Exit")
        
        try:
            choice = int(input("Choose an option (1-5): "))
            
            if choice == 1:
                display_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                remove_task(tasks)
            elif choice == 4:
                mark_completed(tasks)
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()
