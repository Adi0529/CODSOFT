class Task:
    def __init__(self, name, status='Incomplete'):
        self.name = name
        self.status = status

class List:
    def __init__(self):
        self.tasks=[]

    def add(self, task):
        self.tasks.append(task)

    def display(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task.name} - {task.status}")

    def update(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.status = 'Complete'
            print(f"Updated status of {task.name} to Complete.")
        else:
            print("Invalid task index.")

    def edit(self, task_index, new_name):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.name = new_name
            print(f"Updated task name to '{new_name}'.")
        else:
            print("Invalid task index.")

todo_list = List()
while True:
    print("\n===toDolist====")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Update Task Status")
    print("4. Edit Task")
    print("5. Exit")

    choice = input("Enter your choice:")

    if choice == '1':
        task_name = input("Enter task name: ")
        new_task = Task(task_name)
        todo_list.add(new_task)
        print(f"Task '{new_task.name}' added successfully.")

    elif choice == '2':
        print("\n===== Current Tasks =====")
        todo_list.display()

    elif choice == '3':
        task_index = int(input("Enter the task index to mark as complete: "))
        todo_list.update(task_index)

    elif choice == '4':
        task_index = int(input("Enter the task index to edit: "))
        new_name = input("Enter the new task name: ")
        todo_list.edit(task_index, new_name)

    elif choice == '5':
        print("Exiting To-Do List application.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
        