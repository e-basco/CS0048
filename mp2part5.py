import sys
import os


def pause():
    input("Press Enter to continue")

def clear():
    os.system('cls' if os.name =='nt' else 'clear')

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
            print(calculate_average(grades))
            pause()
            clear()
        else:
            sys.exit("Thank you!")


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
    student_grade_calculator()