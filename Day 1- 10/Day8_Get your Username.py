email = input("Email Address: ").strip()
user = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print("Your username is", user + " and your domain is", domain)
