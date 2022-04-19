def is_valid_subsequence(array, sequence):
    pos = 0
    seq_len = len(sequence)
    for num in array:
        if num == sequence[pos]:
            pos += 1
        if pos == seq_len:
            return True
    return False


print(is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1]))


def is_valid_subsequence1(array, sequence):
    seq_pos = 0
    for num in array:
        if seq_pos == len(sequence):
            return True
        if sequence[seq_pos] == num:
            seq_pos += 1
    return seq_pos == len(sequence)


print(is_valid_subsequence1([5, 1, 22, 25, 6, 8], [1, 2, 6]))
