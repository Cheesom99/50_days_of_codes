# N0 NUMERALS
numerals = {
    "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
    "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten"
}
new_phrase = []
phrase = "He has 8 cows, 10 dogs and 1 horse"
for i in phrase.split():
    if i not in numerals:
        new_phrase.append(i)
    else:
        new_phrase.append(numerals[i])
print(" ".join(new_phrase))








# for i in sentence:
#     if i not in numerals:
#         sen += i
#     else:
#         sen += numerals[i]
# print(sen)