# Phone Book

names = []
phone_nos = []
no_contacts = int(input("Number of contacts to be saved: "))

for i in range(no_contacts):
    names.append(input("Name: "))
    phone_nos.append(input("Phone Number: "))

name_search = input("\nEnter search term: ")

print("Search result:")

if name_search in names:
    pos = names.index(name_search)
    phone_number = phone_nos[pos]
    print("Name: {}, Phone Number: {}".format(name_search, phone_number))
else:
    print("Name Not Found")
