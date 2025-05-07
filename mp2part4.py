import sys
import random
import os


def pause():
    input("Press Enter to continue")

def clear():
    os.system('cls' if os.name =='nt' else 'clear')


def main():
    while True:
        user_input = input("Welcome to Number Guessing Game:\n"
        "a. Play Number Guessing Game\n"
        "b. Exit\n"
        "Enter your choice(a/b): ")
        if user_input.lower() == "a":
            result = play()
            print(result)
            pause()
            clear()

        else:
            sys.exit("Thank you for playing!")


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

if __name__ == "__main__":
    main()