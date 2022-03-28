# 3 sum closest
import sys


def closest_three_sum(arr, x):
    closest_sum = sys.maxsize  # assigning the max value in the system to a variable
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):  # using a triple nested loop to iterate through...
            for k in range(j + 1, len(arr)):  # ...every possible combination of three numbers

                if abs(x - closest_sum) > abs(x - (arr[i] + arr[j] + arr[k])):
                    closest_sum = (arr[i] + arr[j] + arr[k])
    return closest_sum


print(closest_three_sum([10, -5, -10, 0], 5))
