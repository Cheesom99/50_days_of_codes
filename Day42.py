def prime_range(lower_value, upper_value):
    print(f"The prime numbers in the range of {lower_value} and {upper_value} are: ")
    for number in range(lower_value, upper_value + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                print(number, end=", ")


prime_range(3, 23)
