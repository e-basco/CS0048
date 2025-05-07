import sys
import os


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
        print (f"Ans: {calculate(user_input)}")
        pause()
        clear()



def calculate(user_input):
    if user_input == "1":
        return operation("+")
    elif user_input == "2":
        return operation("-")
    elif user_input == "3":
        return operation("*")
    elif user_input == "4":
        return operation("/")
    else:
        sys.exit("Goodbye. Thank you!")
    

    
def operation(operator):
    x = int(input("x: "))
    y = int(input("y: "))

    if operator == "+":
        return x + y
    if operator == "-":
        return x - y
    if operator == "*":
        return x * y
    if operator == "/":
        if y == 0:
            return "Divisor can't be zero"
        else:
            return x / y

def temperature_converter():
    while True:
        user_input = input("Celcius & Farenheit Conversion\n"
        "a. Convert Celcius to Farenheit\n"
        "b. Convert Farenheit to Celcius\n"
        "c. Exit\n"
        "Enter your choice(a-c): ")
        print(f"Ans: {convert_temp(user_input)}")
        pause()
        clear()

def convert_temp(user_input):
    if user_input.lower() == "a":
        return celcius_to_fareheit()
    elif user_input.lower() == "b":
        return farenheit_to_celcius()
    else:
        sys.exit("Goodbye. Thank You!")


def celcius_to_fareheit():
    input_celcius = int(input("Input: "))
    return 9/5 * input_celcius + 32


def farenheit_to_celcius():
    input_celcius = int(input("Input: "))
    return 5/9 * (input_celcius - 32)

if __name__ == "__main__":
    simple_calculator()