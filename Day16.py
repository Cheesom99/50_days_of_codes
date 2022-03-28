def sum_two(a, b, z):
    c = []
    for x in a:
        c.append(z - x)
    for y in b:
        if y in c:
            return True
    return False


print(sum_two([1, 2, 3], [10, 20, 30, 40], 42))
print(sum_two([1, 2, 3], [10, 20, 30, 40], 45))
