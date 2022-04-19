#GP CALCULATOR
no_of_courses = int(input("Number of courses offered: "))
count = 0
course = []
grade = []
unit_load = []
res = []
while count < no_of_courses:
    course.append(input("Course Title: "))
    grade.append(input("Grade: ").upper())
    unit_load.append(int(input("Unit load of course: ")))
    count += 1

for x in range(no_of_courses):
    if grade[x] == "A":
        grade[x] = 5
    elif grade[x] == "B":
        grade[x] = 4
    elif grade[x] == "C":
        grade[x] = 3
    elif grade[x] == "D":
        grade[x] = 2
    elif grade[x] == "E":
        grade[x] = 1
    else:
        grade[x] = 0
    res.append(grade[x] * unit_load[x])

total_units = 0
for z in unit_load:
    total_units = z + total_units

ovr = 0
for num in res:
    ovr = num + ovr

gpa = ovr/total_units
print("You have a GP of ", round(gpa, 2))
