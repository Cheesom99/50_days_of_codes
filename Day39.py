def single_digit(n):
    if len(str(n)) == 1:
        return n
    else:
        curr = [int(x) for x in str(n)]
        n = sum(curr)
        if len(str(n)) == 1:
            return n
    return single_digit(n)


print(single_digit(99999))
print(single_digit(1234))
print(single_digit(785))
