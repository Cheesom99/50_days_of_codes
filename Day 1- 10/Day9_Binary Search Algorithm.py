#BINARY SEARCH ALGORITHM
nums = (12, 5, 67, 78, 33, 44, 36, 90, 21, 17)
num_sort = sorted(nums)
key = int(input("What number are you looking for? "))


def bin_search_alg(num_sort, key):
    mini = 0
    maxi = len(num_sort) - 1
    while maxi >= mini:
        midi = (maxi + mini) // 2
        if key > num_sort[midi]:
            mini = midi + 1
        elif key < num_sort[midi]:
            maxi = midi - 1
        else:
            return midi
    return None


res = bin_search_alg(num_sort, key)

if res is None:
    print("The number", key, "is not in the array")
else:
    print("The number", key, "in in position", res)


