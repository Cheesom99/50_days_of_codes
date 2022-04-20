#  SMALLEST DIFFERENCE
arr = [56, 89, 65, 30, 12, 87]
arr = sorted(arr)
diff_arr = []
i = 0
j = 1
count = 0
while count < len(arr)-1:
    diff = arr[j]-arr[i]
    diff_arr.append(diff)
    i += 1
    j += 1
    count += 1
print(min(diff_arr))
