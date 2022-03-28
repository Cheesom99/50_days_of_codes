#PASSWORD VALIDATOR
import re

pattern = re.compile(r"")

while True:
    password = input("Enter your password: ")
    if len(password) < 8:
        print("Password is at least 8 characters long")
    elif re.search(r"\d", password) is None:
        print("Password should contain a digit at least")
    elif re.search(r"[A-Z]", password) is None:
        print("Password should contain an upper case at least")
    elif re.search("[a-z]", password) is None:
        print("Password should contain a lower case at least")
    elif re.match(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}", password):
        pattern = re.compile(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}")
        print("Password Saved")
        break
    else:
        print("Invalid Password")
