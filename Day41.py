def is_prime(num, i):
    if num == 0 or num == 1:  # 0 and 1 are not primes
        return False
    if num == i:  # once i becomes == the num, it becomes true
        return True
    if num % i == 0:  # if the num is divisible by i, it is not prime
        return False
    i += 1
    return is_prime(num, i)


print(is_prime(5, 2))  # TRUE
print(is_prime(17, 2))  # TRUE
print(is_prime(49, 2))   # FALSE
