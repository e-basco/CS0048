import sys
import os


def pause():
    input("Press Enter to continue")

def clear():
    os.system('cls' if os.name =='nt' else 'clear')


def main():
    tasks = []
    while True:
        user_input = input("To-Do List:\n"
        "1. Add Task\n"
        "2. Remove Task\n"
        "3. View Tasks\n"
        "4. Exit\n" \
        "Enter your choice(1-4): ")

        if user_input == "1":
            add_task(tasks)
            pause()
            clear()
        elif user_input == "2":
            remove_task(tasks)
            pause()
            clear()
        elif user_input == "3":
            view_task(tasks)
            pause()
            clear()
        else:
            sys.exit("Goodbye. Thank you!")


def add_task(tasks):
    tasks.append(input("Add task: "))
    print("Task Added.")


def remove_task(tasks): 
    tasks.remove(input("Remove task: "))
    print("Task Removed")

def view_task(tasks):
    i = 1
    print("View Task/s:")
    for task in tasks:
        print(f"{i}. {task}")
        i += 1
    print()

if __name__ == "__main__":
    main()