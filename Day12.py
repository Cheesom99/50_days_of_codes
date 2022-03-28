question = input("Do you wanna go on an adventure? Y or N ").upper()
if question != "Y":
    print("Bye!!!")
    quit()
else:
    user = input("What is your name? ")
    print("Welcome,", user, "to the most exciting adventure")


def success(name):
    print(name + ", you are a winner")


answer = input("We move. Do you move left or right? L/R/Q for Left/Right?Quit. ").upper()
if answer == "L":
    print("You start on the shores of Madagascar")
    answer = input("Will you swim across or wait for a boat? S for swim, W to wait. ").upper()
    if answer == "S":
        answer = input("SHARK!!! Swim faster or hide? Pick SW or H. ").upper()
        if answer == "SW":
            print("Lunch for the sharks. You LOSE!!!")
        elif answer == "H":
            print("A submarine came to your rescue")
            answer = input("Join the ship crew or not? YES to join, N0 to leave. ").lower()
            if answer == "yes":
                print("You now have a place to lay your head")
                answer = input("Kill the ship crew or nay. kill or nay ").lower()
                if answer == "kill":
                    print("You successfully kill all and take their loot.")
                    success(name=user)
                elif answer == "nay":
                    print("The crew members kill you instead. You LOSE!!! ")
                    quit()
                else:
                    print("Wrong option. YOU LOSE!!!")
                    quit()
            elif answer == "no":
                print("You die of starvation. lol. You LOSE!!!")
            else:
                print("Wrong option. YOU LOSE!!!")
                quit()
        else:
            print("Wrong option. YOU LOSE!!!")
            quit()
    elif answer == "W":
        print("You were robbed and killed, you lose!!!")
        quit()
    else:
        print("Wrong input. You quit")
elif answer == "R":
    print("You start in the Namibian deserts")
    answer = input("Search for Food(food) or Water(water)").upper()
    if answer == "FOOD":
        print("You did not find food")
        answer = input("Things are looking gloomy, Sell yourself as a slave or commit suicide (Slave/suicide) ").upper()
        if answer == "SUICIDE":
            print("Lunch for the sharks. You LOSE!!!")
            quit()
        elif answer == "SLAVE":
            print("You are sold to the richest man in Namibia")
            answer = input("Kill(k) him or not(nope). ").lower()
            if answer == "nope":
                print("The rich man dies and you succeed him. ")
                success(name=user)
                answer = input("Kill the ship crew or nay. k or nope ").lower()
            elif answer == "k":
                print("lol. you be wicked person oo. You LOSE!!!")
                quit()
            else:
                print("Wrong option. YOU LOSE!!!")
                quit()
        else:
            print("Wrong option. YOU LOSE!!!")
            quit()
    elif answer == "W":
        print("No water here. You DIE!!!")
        quit()
    else:
        print("Wrong input. You quit")
        quit()
else:
    print("Wrong option. YOU LOSE!!!")
    quit()
