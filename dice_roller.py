# This is a dice rolling program. It will simulate a dice roll and return the outcome
# M N Makola(Beginner Projects No 1)


import random

# Create a start varible that will let the computer know when the user wants to play
start = False

# A function to control the start variable
def start():
    user = input(f"\nStart Dice Roller [Y/N]: ").lower()

    global start
    if user == "y":
        print("\n\t\t\tWelcome to the Dice Roller\n")
        start = True

    else:
        print("Ending Program")
        start = False

# A while loop that keeps running until user stops the loop by inputing N for no.
def main():
    while start:
        user = input(f"\n1. Roll Dice \n2. Exit \nResponse: ")

        if user == "1":       
            print(f"\n[1st Dice: {random.randint(1,6)} / 2nd Dice: {random.randint(1,6)}]\n")

        elif user == "2":
            print("\nThank you for playing\n")
            break

        else:
            print("\nInvalid Choice. Enter 1 or 2!\n")

# Call the start function
start()

main()
