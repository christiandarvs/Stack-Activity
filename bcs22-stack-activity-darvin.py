import sys


class TaskManager:
    def __init__(self, task_size):
        self.task_lists = []
        self.task_size = task_size
        self.top = -1

    def add_task(self, task):
        if not self.is_full():
            if task not in self.task_lists:
                self.top += 1
                self.task_lists.append(task)
                return "Task added successfully!\n"
            else:
                return "Task is already in the list...\n"
        else:
            return "You have reached the maximum number of available tasks...\n"

    def is_full(self):
        return self.top == self.task_size - 1

    def is_empty(self):
        return self.top == -1

    def display_tasks(self):
        for x in range(len(self.task_lists)):
            print(f"Task {x + 1}")
            print(self.task_lists[x])

    def mark_as_done(self, index):
        if 0 <= index < len(self.task_lists):
            self.task_lists[index].is_done = True
            print("Task Completed!\n")
        elif self.is_empty():
            print("Task list is empty. Please add a task.\n")
        else:
            print("Invalid index. Please try again.\n")


class Task:
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc
        self.is_done = False

    def __str__(self):
        return f"--------------------\nTitle: {self.title}\nDescription: {self.desc}\nIs Done: {self.is_done}\n--------------------\n"

    def __eq__(self, other):
        return self.title == other.title and self.desc == other.desc


def display_menu():
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Done")
    print("4. Exit Task Manager\n")


def main():
    while True:
        task_size = None
        while task_size is None:
            try:
                task_size = int(input("Enter Number of Tasks: "))
            except ValueError:
                print("Input must be an integer...\n")
        task_manager = TaskManager(task_size)

        while True:
            try:
                display_menu()
                choice = int(input("Enter Choice: "))
                if choice == 1:
                    task_title = input("Enter Task Title: ").lower()
                    task_desc = input("Enter Task Desc: ").lower()
                    print()
                    task = Task(task_title, task_desc)
                    result = task_manager.add_task(task)
                    print(result)
                elif choice == 2:
                    print()
                    print("Displaying Tasks...\n")
                    task_manager.display_tasks()
                elif choice == 3:
                    print("Indexes: [", end=" ")
                    for x in range(task_size):
                        print(x, end=" ")
                    print("]\n")
                    index = int(input("Enter Task Index Number: "))
                    task_manager.mark_as_done(index)
                elif choice == 4:
                    print("Closing Task Manager...\n")
                    sys.exit()
                else:
                    print("Invalid Input\n")
            except ValueError:
                print("Input must be an integer...\n")


if __name__ == "__main__":
    main()
