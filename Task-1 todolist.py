tasks = []

while True:
    print("\nTo-Do List:")
    if not tasks:
        print("No tasks in the list.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    
    print("\nOptions:")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Remove Task")
    print("4. Quit")
    
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print(f"Task '{task}' added.\n")
    elif choice == '2':
        task_number = int(input("Enter task number to update: "))
        if 0 < task_number <= len(tasks):
            new_task = input("Enter the new task: ")
            tasks[task_number - 1] = new_task
            print(f"Task {task_number} updated to '{new_task}'.\n")
        else:
            print("Invalid task number.\n")
    elif choice == '3':
        task_number = int(input("Enter task number to remove: "))
        if 0 < task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed.\n")
        else:
            print("Invalid task number.\n")
    elif choice == '4':
        break
    else:
        print("Invalid option. Please try again.\n")
