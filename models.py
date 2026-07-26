class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def mark_done(self):
        self.done = True

    def show_task(self):
        if self.done:
            print(f"[Done] {self.title}")
        else:
            print(f"[Todo] {self.title}")

    def to_dic(self):
        return {
            "title": self.title,
            "done": self.done
        }
    
import json

FILE_NAME = "tasks.json"


def load_tasks():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            task_data = json.load(file)

        tasks = []

        for data in task_data:
            task = Task(data["title"])
            task.done = data["done"]
            tasks.append(task)

        return tasks

    except FileNotFoundError:
        return []

def save_tasks(tasks):
    task_data = []

    for task in tasks:
        task_data.append(task.to_dic())

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(task_data, file, ensure_ascii=False, indent=4)


def add_tasks(tasks):
    title = input("Your title is: ").strip()

    if not title:
        print("Task title cannot be empty")
        return

    new_task = Task(title)
    tasks.append(new_task)

    save_tasks(tasks)

    print("Task added successfully")

def show_tasks(tasks):
    if not tasks:
        print("please enter a valid task")
        return
    for index,task in enumerate(tasks, start=1):
        print(f"{index}.", end="")
        task.show_task()

def mark_task_done(tasks):
    if not tasks:
        print("please enter a valid task")
        return

    show_tasks(tasks)

    try:
        number = int(input("choose a task number"))
        index = number - 1

        if index < 0 or index >= len(tasks):
            print("Invalid number")
            return

        selected_task = tasks[index]
        selected_task.mark_done()

        save_tasks(tasks)

        print("Task marked as done. ")

    except ValueError:
        print("Please enter a valid number")

def delete_tasks(tasks):
    if not tasks:
        print("please enter a valid task")
        return

    show_tasks(tasks)

    try:
        number  = int(input("choose a task: "))
    except ValueError:
        print("please eneter a valid number")
        return

    index = number - 1

    if index < 0 or index >= len(tasks):
        print("Invalid task number")
        return

    delete_task = tasks.pop(index)

    save_tasks(tasks)

    print(f'Task"{delete_task.title}" deleted successfully.')

def edit_tasks(tasks):
    if not tasks:
        print("please enter a valid task")
        return

    show_tasks(tasks)

    try:
        number  = int(input("choose a task: "))
    except ValueError:
        print("please eneter a valid number")
        return
    
    index = number - 1

    if index < 0 or index >= len(tasks):
        print("Invalid data")
        return

    new_task = input("New task is: ")
    if not new_task:
        print("Task title cannot be empty")
        return
    tasks[index].title = new_task

    save_tasks(tasks)

    print("edit successfully")

def search_tasks(tasks):
    if not tasks:
        print("please enter a valid task")
        return

    search_task = input("Search: ").lower().strip()

    if not search_task:
        print("Search keyword cannot be empty")
        return

    found = False

    for index, task in enumerate(tasks, start=1):
        if search_task in task.title.lower():
           print(f"{index}.", end="")
           task.show_task()
           found = True

    if not found:
        print("Cannot found it")
        return

def menu():
    print("\n==== OOP Todo Manager =====")
    print("1. Add task")
    print("2. Show task")
    print("3. mark task")
    print("4. Delete task")
    print("5. Edit task")
    print("6. Search task")
    print("7. Exit")



def main():

    tasks = load_tasks()

    while True:    
        menu()   
        choice = input("choose a option: ").strip()
        if choice == "1":
            add_tasks(tasks)
            
                
        elif choice == "2":
            show_tasks(tasks)
                
               
        elif choice == "3":
            mark_task_done(tasks)
    
        elif choice == "4":
            delete_tasks(tasks)
               
                
        elif choice == "5":
            edit_tasks(tasks)
                
                
        elif choice == "6":
            search_tasks(tasks)
                
                
        elif choice == "7":
            print("Bye bye")
           
            break
        else:
            print("please enter a valid number")
    
        input("\nPress Enter to return to the menu...")

main()

