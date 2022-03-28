# Fibonacci Sequence

no_of_terms = int(input("Enter number of terms: "))
n1, n2 = 0, 1
count = 0
while count < no_of_terms:  #
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
