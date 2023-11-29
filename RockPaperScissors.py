import random
# best practices when importing modules is to place them at the top

# need two variables
user_wins = 0
computer_wins = 0

# Storing the list of values in the "options" variable
options = ["rock", "paper", "scissors"]

# while loop to let user input rock, paper, scissors and Q for quit
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
# creating a list Anything encapsulated in square brackets.
# if user input is inside the list is any of the three strings below.
    if user_input not in options:
        continue
# continue just asks the question again until correct input or quit is given.

    random_number = random.randint(0, 2)
# rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer Picked", computer_pick + ".")

# this creates the winning conditions for either the user or computer
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")

        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You Lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")


