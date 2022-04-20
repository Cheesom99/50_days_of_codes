# ANAGRAM DETECTOR
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    set_s1 = set(s1)
    set_s2 = set(s2)
    if set_s1 == set_s2:
        return True
    else:
        return False


print(are_anagrams(input(": ").lower(), input(": ").lower()))
print(are_anagrams(input(": ").lower(), input(": ").lower()))
print(are_anagrams(input(": ").lower(), input(": ").lower()))

