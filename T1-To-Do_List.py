class operations:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task removed successfully!")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task}")

    def update_task(self, task_index, new_task):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task index.")

def menu():
    todo_list = operations()
    while True:
        print("*"*22)
        print("\tTo-Do List")
        print("*"*22)
        print("\t1. Add Task")
        print("\t2. Remove Task")
        print("\t3. Display Tasks")
        print("\t4. Update Task")
        print("\t5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter task index to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            index = int(input("Enter task index to update: ")) - 1
            new_task = input("Enter new task: ")
            todo_list.update_task(index, new_task)
        elif choice == "5":
            print("Thanks for using...")
            break
        else:
            print("Invalid choice. Please try again.")

To_Do_List=menu()
