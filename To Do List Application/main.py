import time

def wait(x):
    time.sleep(x)

class ToDo:
    def __init__(self):
        self.tasks = []
    
    def add_task(self,task):
        self.tasks.append({"task":task, "completed":False})

    def mark_as_complete(self,index):
        index-=1
        if index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"Task {self.tasks[index]} is marked as complete.")
        else:
            print("Invalid Index.")

    def display_tasks(self):
        if not self.tasks:
            print("No Tasks Found.")
        else:
            print("Task List: ")
            for index, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{index+1}. {task['task']} - {status}")

def main():
    todo_list = ToDo()
    print("\nTo-Do App")
    while True:
        print("\n1. Add a new task")
        print("2. Mark a task as completed")
        print("3. Display all tasks")
        print("4. Quit the app")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            task = input("Enter the Task: ")
            todo_list.add_task(task)
            
        elif choice == "2":
            index = int(input("Enter the index of the task u want to mark as Done: "))
            todo_list.mark_as_complete(index)

        elif choice == "3":
            todo_list.display_tasks()
            wait(3)
            
        elif choice == "4":
            print("Exiting will erase all of your saved tasks.")
            ans = input("Confirm to Exit (y/n): ")
            if ans.strip().lower()=="y":
                print("Exiting...")
                wait(3)
                break
            else:
                continue

        else:
            print("Invalid Input.")
            
        wait(1)

if __name__ == "__main__":
    main()