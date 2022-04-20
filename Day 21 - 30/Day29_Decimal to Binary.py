def only_int(num):
    num_list = []
    while num > 0:
        if num % 2 == 0:
            num_list.insert(0, 0)  # if num is even, insert 0 at index 0 in num_list
        elif num % 2 != 0:
            num_list.insert(0, 1)   # if num is odd, insert 1 at index 0 in num_list
        num = num // 2  # updates num
    str_list = [str(nums) for nums in num_list]
    return "".join(str_list)


print(only_int(5))


# import math
# sentence = 'can is good%'
# puncs = """!@#$%^&"*()?"""
# punc_no = ""
# for i in sentence:
#     if i not in puncs:
#         punc_no += i
# char_len = len(punc_no.replace(" ", ""))
# word_list = punc_no.split(" ")
# print(word_list)
# word_len = len(word_list)
# print(math.ceil(char_len / word_len))