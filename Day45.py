# ROMAN TO ARABIC
def rom_to_arabic(rom):
    codes = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    rom = rom.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX")
    rom = rom.replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
    num = 0
    for i in rom:
        if i in codes:
            num += codes[i]
    return num


print(rom_to_arabic(input(": ").upper()))
