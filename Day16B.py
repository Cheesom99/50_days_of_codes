def sum_of_two(a, b, z):
    sums = []
    for x in a:
        for y in b:
            sums.append(x + y)
    if z in sums:
        return True
    else:
        return False


print(sum_of_two([1, 2, 3], [10, 20, 30, 40], 42))


arrays = [10, 20, 30, 40]
print(arrays.index(20))