# Exercise 2: Task List Manager (with separate module)

import tasks

task_list = []

while True:
    command = input("Enter command (add <task>, remove <task>, done): ").strip()

    if command == "done":
        break

    if command.startswith("add "):
        task = command[4:]
        tasks.add_task(task_list, task)
    elif command.startswith("remove "):
        task = command[7:]
        tasks.remove_task(task_list, task)
    else:
        print("Invalid command.")

    print("Current tasks:", task_list)
