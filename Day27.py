def dejavu(letters):
    new_set = set(letters)
    if len(letters) == len(new_set):
        print("Unique")
    else:
        print("Deja Vu")


dejavu(input(""))
dejavu(input(""))
