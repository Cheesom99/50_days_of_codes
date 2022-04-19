# If a number in list A and B can sum up to z
def sum_two(a, b, z):
    c = []
    for x in a:
        c.append(z - x)
    for y in b:
        if y in c:
            return True
    return False


print(sum_two([1, 2, 3], [10, 20, 30, 40], 42))  # returns True, 2+40=42
print(sum_two([1, 2, 3], [10, 20, 30, 40], 45))  # returns False, no two numbers sum to 45
