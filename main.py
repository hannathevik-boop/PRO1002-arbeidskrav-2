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
