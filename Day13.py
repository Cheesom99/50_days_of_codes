def pairs(list1, summed):
    mini = 0
    maxi = len(list1)-1
    while mini < maxi:
        if list1[mini] + list1[maxi] < summed:
            mini = mini + 1
        elif list1[mini] + list1[maxi] > summed:
            maxi = maxi - 1
        else:
            return True
    return False


print(pairs([1, 3, 4, 6, 10, 11, 16], 20))  # returns True
print(pairs([2, 4, 6, 7, 15, 17, 19], 20))  # returns False
