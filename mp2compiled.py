import sys
import os
import random


def main():
    while True:
        user_input = input("Main Menu of MP2\n" \
        "1. Simple Calculator\n" 
        "2. Temperature Converter\n" \
        "3. To-do List\n" \
        "4. Number Guessing Game\n" \
        "5. Student Grade Calculator\n" \
        "6. Exit\n"
        "Enter your choice: ")

        if user_input == "1": 
            pause()
            clear()
            simple_calculator()
            pause()
            clear()
        elif user_input == "2":
            pause()
            clear()
            print(temperature_converter())
            pause()
            clear()
        elif user_input == "3":
            pause()
            clear()
            to_do_list()
            pause()
            clear()
        elif user_input == "4":
            pause()
            clear()
            print(number_guessing_game())
            pause()
            clear()
        elif user_input == "5":
            pause()
            clear()
            print(student_grade_calculator())
            pause()
            clear()
        else:
            return()



def pause():
    input("Press Enter to continue")

def clear():
    os.system('cls' if os.name =='nt' else 'clear')

def simple_calculator():
    while True:

        user_input = input("Basic Calculator:\n"
            "1. Add\n"
            "2. Subtract\n"
            "3. Multiply\n"
            "4. Divide\n"
            "5. Exit\n"
            "Enter your choice(1-5): ")
        return calculate(user_input)


def calculate(user_input):
    if user_input == "1":
        print(operation("+"))
    elif user_input == "2":
        print(operation("-"))
    elif user_input == "3":
        print(operation("*"))
    elif user_input == "4":
        print(operation("/"))
    else:
        return("Goodbye. Thank you!")
    

    
def operation(operator):
    x = int(input("x: "))
    y = int(input("y: "))

    if operator == "+":
        return (f"ans: {x + y}")
    if operator == "-":
        return (f"ans: {x - y}")
    if operator == "*":
        return (f"ans: {x * y}")
    if operator == "/":
        if y == 0:
            print ("Divisor can't be zero")
        else:
            return (f"ans: {x / y}")

def temperature_converter():
    while True:
        user_input = input("Celcius & Farenheit Conversion\n"
        "a. Convert Celcius to Farenheit\n"
        "b. Convert Farenheit to Celcius\n"
        "c. Exit\n"
        "Enter your choice(a-c): ")
        return(f"Ans: {convert_temp(user_input)}")


def convert_temp(user_input):
    if user_input.lower() == "a":
        return celcius_to_fareheit()
    elif user_input.lower() == "b":
        return farenheit_to_celcius()
    else:
        return("Goodbye. Thank You!")


def celcius_to_fareheit():
    input_celcius = int(input("Input: "))
    return 9/5 * input_celcius + 32


def farenheit_to_celcius():
    input_celcius = int(input("Input: "))
    return 5/9 * (input_celcius - 32)


def to_do_list():
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
            return("Goodbye. Thank you!")


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


def number_guessing_game():
    while True:
        user_input = input("Welcome to Number Guessing Game:\n"
        "a. Play Number Guessing Game\n"
        "b. Exit\n"
        "Enter your choice(a/b): ")
        if user_input.lower() == "a":
            result = play()
            return(result)

        else:
            return("Thank you for playing!")


def play():
    random_number = random.randint(1, 100)
    while True: 
        user_input = int(input("Guess the number(1-100): "))
        if user_input == random_number:
            return "You got it right!"
        elif user_input >= random_number:
            print("Too high")
            print("Try Again!")
            print()
            pause()
            clear()
        else:
            print("Too low")
            print("Try Again!")
            print()
            pause()
            clear()

grades = {}
def student_grade_calculator():
    while True:
        user_input = input("Student Grade Calculator:\n"
        "a. Add Score\n"
        "b. Calculate Average\n"
        "c. Exit\n"
        "Enter your choice: ")
        if user_input.lower() == "a":
            pause()
            clear()
            add_score(grades)
            pause()
            clear()
        elif user_input.lower() == "b":
            pause()
            clear()
            return(calculate_average(grades))
        else:
            return("Thank you!")


def add_score(grades):
    new_grade = {}
    key = input("Subject: ")
    value = input("Grade: ")
    new_grade[key] = value

    grades.update(new_grade)
    return 

def calculate_average(scores):
    average = 0.0
    for grade in grades:
        average += int(grades[grade])
    return average/len(grades)


if __name__ == "__main__":
    main()