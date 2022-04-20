# Fibonacci Sequence

no_of_terms = int(input("Enter number of terms: "))

# The first numbers are constant: Zero and One
n1, n2 = 0, 1
count = 0
while count < no_of_terms:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
