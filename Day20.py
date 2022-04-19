# PIG LATIN
def pig_latin(word):
    pig_dict = []
    for x in word.split(" "):
        pig_wrd = x[1:] + x[0] + "ay"
        pig_dict.append(pig_wrd)
    print(" ".join(pig_dict))


pig_latin("you are good")
pig_latin("i am great")
