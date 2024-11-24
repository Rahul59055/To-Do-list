# To-Do List Application

This is a simple Python-based To-Do List application that allows users to manage their tasks. The program saves tasks to a text file (`tasks.txt`) and provides an interface to view, add, remove, and mark tasks as completed.

## Features

- **Load tasks**: Loads tasks from the `tasks.txt` file.
- **Display tasks**: Shows the current list of tasks.
- **Add task**: Allows the user to add new tasks to the list.
- **Remove task**: Allows the user to remove a task from the list by its number.
- **Mark task as completed**: Marks a task as completed by removing it from the list.
- **Persistent storage**: Saves tasks to the `tasks.txt` file, ensuring they persist between program runs.

## Requirements

- Python 3.x
- A text editor to view and edit the `tasks.txt` file (optional).

## Installation

1. Install Python from the [official website](https://www.python.org/downloads/) if not already installed.
2. No additional libraries are required, as this program uses Python's built-in modules.

## How to Use

1. **Running the Program**: Simply run the Python script.
   ```bash
   python todo_list.py
   ```
## Screenshots
![Screenshot 2024-11-24 195053](https://github.com/user-attachments/assets/685be320-3b99-426f-b331-b05fb7a9b36e)

   
## OUTPUT

**To-Do List Application**
1. Show tasks
2. Add task
3. Remove task
4. Mark task as completed
5. Exit

- **Choose an option (1-5):**  1

   **Your To-Do List:**
     1. Buy groceries
     2. Walk the dog

- **Choose an option (1-5):**  2<br>
     * **Enter the task you want to add:**  Finish homework<br>
     * Task 'Finish homework' added to the list.

- **Choose an option (1-5):**  3<br>
     * **Enter the task number to remove:**  1<br>
     * Task 'Buy groceries' removed from the list.

- **Choose an option (1-5):**  4<br>
     * **Enter the task number to mark as completed:**  2<br>
     * Task 'Walk the dog' marked as completed and removed from the list.

- **Choose an option (1-5):**  5<br>
     * Goodbye!
