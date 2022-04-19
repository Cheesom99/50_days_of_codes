# Rock Paper Scissors game
import random

options = ["rock", "paper", "scissors"]
you_counts = 0
comp_counts = 0

while True:
    your_input = input("Type rock, paper or scissors or Q to quit: ").lower()

    if your_input == "q":
        print("You quit")
        break

    computer = options[random.randint(0, 2)]
    print("Computer picks", computer)

    if your_input == "scissors" and computer == "paper":
        print("User wins")
        you_counts += 1
    elif your_input == "rock" and computer == "scissors":
        print("User wins")
        you_counts += 1
    elif your_input == "paper" and computer == "rock":
        print("User wins")
        you_counts += 1
    elif your_input == computer:
        print("A draw")
    else:
        print("Computer wins")
        comp_counts += 1


print("\nUser won", you_counts, "times")
print("Computer won", comp_counts, "times")
