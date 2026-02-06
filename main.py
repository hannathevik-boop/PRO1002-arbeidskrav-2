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
    
# Exercise 3: Simple Class and Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


student = Student("Hanna", 29, "s12345")
student.greet()
print("Student ID:", student.student_id)

# Exercise 6: JSON Settings Handler

import json

try:
    with open("settings.json", "r") as file:
        settings = json.load(file)

    print("Current settings:", settings)

    key = input("Which setting do you want to change? ")
    if key in settings:
        new_value = input("Enter new value: ")

        # Convert to int if original value is int
        if isinstance(settings[key], int):
            new_value = int(new_value)

        settings[key] = new_value

        with open("settings.json", "w") as file:
            json.dump(settings, file, indent=2)

        print("Settings updated:", settings)
    else:
        print("Setting not found.")

except FileNotFoundError:
    print("settings.json file not found.")
except ValueError:
    print("Invalid value type.")
except Exception as e:
    print("An error occurred:", e)
