# NUMBER OF PLATFORMS REQUIRED
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
empty = []
count = 0
i = 0
curr = 1
while count < len(arr):
    for time in arr:
        if time in range(arr[i], dep[i]):
            empty.append(time)
    if len(empty) > curr:
        curr = len(empty)
    else:
        curr = curr
    empty.clear()
    i += 1
    count += 1
print('A total number of', curr, 'tracks are needed')









'''
def findPlatform(arr, dep, n):
    arr.sort()
    dep.sort()

    plat_needed = 1  # we need one platform at the moment
    result = 1  # result is one
    i = 1
    j = 0

    # Similar to merge in
    # merge sort to process
    # all events in sorted order
    while i < n and j < n:  # while i and j is smaller than the len(arr)

        # If next event in sorted
        # order is arrival,
        # increment count of
        # platforms needed
        if arr[i] <= dep[j]:  # if arrival is next

            plat_needed += 1  # we need an extra platform
            i += 1  # look at the next departure time

        # Else decrement count
        # of platforms needed
        elif arr[i] > dep[j]:  # elif departure is next

            plat_needed -= 1  # we need fewer platforms
            j += 1  # check next departure

        # Update result if needed
        if plat_needed > result:
            result = plat_needed

    return result


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)
print("Minimum Number of Platforms Required = ",
      findPlatform(arr, dep, n))
'''

