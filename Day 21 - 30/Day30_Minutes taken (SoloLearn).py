my_name = "Obi"
no_workers = 2
minutes = 20
name = "Grant Obum Jacks Emma"
names = name.split()
names.insert(0, my_name)
names_sorted = sorted(names)
my_name_index = names_sorted.index(my_name)
minutes_taken = ((my_name_index // no_workers)+1) * minutes
print(minutes_taken)
