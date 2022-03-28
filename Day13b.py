def has_pair(list3, summed):
    complements = set()
    for num in list3:
        if summed - num in list3:
            return True
        complements.add(summed-num)
    return False


print(has_pair([1, 3, 4, 6, 10, 11, 16], 20))
print(has_pair([2, 4, 6, 7, 15, 17, 19], 20))
