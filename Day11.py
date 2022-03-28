# PHONE NUMBER VALIDATOR
import re

phone_num = input("Phone Number: ")
pattern = r"080|070"

match = re.match(pattern, phone_num)
if len(phone_num) == 11 and match:
    print("Valid phone number")
else:
    print("Invalid phone number")
