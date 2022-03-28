word = input("")
new_word = ""
for i in word:
    if i.isalpha() or i.isspace():
        new_word += i
print(new_word[::-1])
