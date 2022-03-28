# https://www.geeksforgeeks.org/smallest-difference-pair-values-two-unsorted-arrays/
import sys
a = [23, 55, 11, 45, 57, 45]
b = [29, 20, 72, 60]
a = sorted(a)
b = sorted(b)
mini = sys.maxsize
i = 0
j = 0
while i < len(a) and j < len(b):
    if abs(a[i]-b[j]) < mini:
        mini = abs(a[i]-b[j])
    if a[i] > b[j]:
        j += 1
    else:
        i += 1
print(mini)
