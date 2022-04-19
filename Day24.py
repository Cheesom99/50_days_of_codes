# SECRET MESSAGE
import string

sample = "Hello world".lower()
new_sample = ""

alpha = string.ascii_lowercase

for i in sample:
    if i.isalpha():
        new_ind = 25 - alpha.index(i)
        new_sample += alpha[new_ind]
    else:
        new_sample += i
print(new_sample)
