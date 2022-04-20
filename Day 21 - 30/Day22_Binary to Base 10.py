# converting binary to base ten
def bin_to_dec(num):
    list_num = [int(i) for i in str(num)]
    pos = 0
    power = len(list_num) - 1
    res_list = []
    while pos < len(list_num):
        res_list.append(list_num[pos] * 2 ** power)
        pos += 1
        power += -1
    print(sum(res_list))


bin_to_dec(int(input(": ")))
bin_to_dec(int(input(": ")))
bin_to_dec(int(input(": ")))