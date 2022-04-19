# Guess the number in the range
import random

num_limit = int(input("The upper boundary of your guess: "))
secret_no = random.randint(0, num_limit)
tries = 0
max_limit = 3

while tries < max_limit:
    guess = int(input("Input guess: "))
    tries += 1
    if guess == secret_no:
        print("You are correct!")
        print("You got it in " + f"{tries}" + " guesses")
        break
    elif guess < secret_no:
        print("Your guess is quite small, increase it")
    elif guess > secret_no:
        print("Your guess is quite big, reduce it")

print("You have run out of guesses")
