import os
print(os.getcwd())


def is_leap(year):
    leap = False

    if year % 4 == 0 and (year % 100 != 0 or year % 400) == 0:
        leap = True
    return leap


print(is_leap(int(input(": "))))
