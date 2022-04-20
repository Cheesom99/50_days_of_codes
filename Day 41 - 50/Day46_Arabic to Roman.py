# ARABIC TO ROMAN
arabic = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
i = 12  # length of lists
num = 2022  # changing this number to roman numerals
while num:
    div = num // arabic[i]  # 2467//1000 = 2...467 // 400 = 1
    num %= arabic[i]  # 2467 % 1000 = 467(it becomes num)...467 % 400 = 67(it becomes num)
    while div:
        print(roman[i], end="")  # prints the letters on one line
        div -= 1  # makes the letters to be printed repetitively
    i -= 1

