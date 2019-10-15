days = 0
names = set()
while days < 2:
    print("This is day ", days+1, "students")
    day_names = set()
    while True:
        name = input("Enter name of student: ")
        if name == "EXIT":
            break
    
        day_names.add(name)
    if days == 0:
        names = names.union(day_names)
    else:
        names = names.intersection(day_names)


    days = days + 1

names_list = list(names)
names_list.sort()

for name in names_list:
    print(name)