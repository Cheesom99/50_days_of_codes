#SYMBOLS
symbols = """!@#$%^&*(';")?.:"""
string = "#le%&t*(s *g()o"
new_str = ""

for i in string:
    if i not in symbols:
        new_str += i
print(new_str)
