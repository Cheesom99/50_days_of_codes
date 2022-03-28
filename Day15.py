# PASSWORD GENERATOR
import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%&")


def generate_password():
    pwdlen = random.randint(10, 15)
    random.shuffle(characters)
    password = []
    for _ in range(pwdlen):
        password.append(random.choice(characters))
    random.shuffle(password)
    print("".join(password))


generate_password()
generate_password()
generate_password()
