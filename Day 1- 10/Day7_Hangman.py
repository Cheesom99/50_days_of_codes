import random
from Day7_list import nigerian_states


def get_state():
    state = random.choice(nigerian_states)
    return state.upper()


def play(state):
    state_complete = "_" * len(state)
    guessed = False
    guessed_states = []
    tries = 3
    print("Let's play")
    print(display(tries))
    print(state_complete)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess the Nigerian state: ").upper()
        if len(guess) == len(state) and guess.isalpha():
            if guess != state:
                print(guess, "is not the state")
                tries -= 1
                guessed_states.append(guess)
            elif guess in guessed_states:
                print("You have guessed this state before")
            else:
                guessed = True
                state_complete = state
        else:
            print("Not valid guess")
        print(display(tries))
        print(state_complete)
        print("\n")

    if guessed:
        print("Congrats, you guessed the state! You win!")
    else:
        print("You ran out of tries. The state was", state)


def display(tries):
    stages = [" ", "1 live left", "2 lives left", "3 lives left"]
    return stages[tries]


state = get_state()
play(state)
