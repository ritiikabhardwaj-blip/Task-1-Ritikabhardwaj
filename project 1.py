# TO-DO LIST PROJECT
# DecodeLabs Python Project 1

tasks = []

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    # Add Task
    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            count = 1
            for task in tasks:
                print(count, ".", task)
                count += 1

    # Exit Program
    elif choice == "3":
        print("Exiting To-Do List Program...")
        break

    # Invalid Input
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")