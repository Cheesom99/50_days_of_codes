# reverse a dictionary mapping
codes = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
rev_codes = {val: key for key, val in codes.items()}
print(rev_codes)
