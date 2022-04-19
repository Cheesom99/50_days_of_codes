def first_and_last(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i+1 < len(arr) and arr[i+1] == target:
                i += 1
            return start, i
    return False


arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
target = 5
print("Number", target, "starts and ends at", first_and_last(arr, target))







# def find_start(arr, target):
#     if arr[0] == target:
#         return 0
#     mini, maxi = 0, len(arr)-1
#     while maxi >= mini:
#         mid = (maxi + mini) // 2
#         if target == arr[mid] and arr[mid-1] < target:
#             return mid
#         elif target > arr[mid]:
#             mini = mid + 1
#         else:
#             maxi = mid - 1
#     return -1
#
#
# def first_last(arr, target):
#     if len(arr) == 0:
#         return [-1, -1]
#     start = find_start(arr, target)
#     if start == -1:
#         return [-1, -1]
#     end = start
#     while end + 1 < len(arr) and arr[end + 1] == target:
#         end += 1
#     return start, end
#
#
# print(first_last([2, 4, 5, 5, 5, 5, 5, 7, 9, 9], 5))