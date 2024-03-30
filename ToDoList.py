def display_menu():
    print("\n===== To-Do List Application =====")
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. Display Tasks")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the task to add: ")
    tasks.append(task)
    print("Task added successfully.")

def edit_task(tasks):
    index = int(input("Enter the index of the task to edit: "))
    if 0 <= index < len(tasks):
        new_task = input("Enter the new task: ")
        tasks[index] = new_task
        print("Task edited successfully.")
    else:
        print("Invalid index. Task not found.")

def delete_task(tasks):
    index = int(input("Enter the index of the task to delete: "))
    if 0 <= index < len(tasks):
        del tasks[index]
        print("Task deleted successfully.")
    else:
        print("Invalid index. Task not found.")

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            edit_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            display_tasks(tasks)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
