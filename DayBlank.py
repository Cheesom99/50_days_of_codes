import random


def start():
    name = input("Enter name: ")
    course = int(input(f"""welcome {name}, what operation are you interested in :
    	1 addition
    	2 subtraction
    	3 multiplication
    	4 division
    	:  """))  # could use \n to minimise space
    if course == 1:
        addition()
    elif course == 2:
        subtraction()
    elif course == 3:
        multiplication()
    elif course == 4:
        division()
    else:
        print("Try again")


def addition():
    score = 0
    for _ in range(10):
        num_1 = random.randint(0, 20)
        num_2 = random.randint(0, 20)
        answer = num_1 + num_2
        print(f"{num_1} + {num_2}")
        user_answer = int(input("= "))
        if user_answer == answer:
            print("Good")
            score += 1
        else:
            print(f"wrong, the right answer is {answer}")
    print("Your score is", score)


def multiplication():
    num_1 = random.randint(0, 20)
    num_2 = random.randint(0, 20)
    answer = num_1 * num_2
    print(f"{num_1} x {num_2}")
    user_answer = int(input("= "))
    if user_answer == answer:
        print("Good")
        #multiplication()
    else:
        print(f"wrong, the right answer is {answer}")
        #quit()
        #multiplication()


def subtraction():
    num_1 = random.randint(0, 20)
    num_2 = random.randint(0, 20)
    answer = num_1 - num_2
    print(f"{num_1} - {num_2}")
    user_answer = int(input("= "))
    if user_answer == answer:
        print("Good")
        #subtraction()
    else:
        print(f"wrong, the right answer is {answer}")
        #quit()
        #subtraction()


def division():
    num_1 = random.randint(0, 20)
    num_2 = random.randint(0, 20)
    answer = round(num_1 / num_2, 2)
    print(f"{num_1} / {num_2}")
    user_answer = int(input("= "))
    if user_answer == answer:
        print("Good")
        #division()
    else:
        print(f"wrong, the right answer is {answer}")
        #quit()
        #division()


start()
