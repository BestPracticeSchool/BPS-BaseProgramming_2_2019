names  = []
while True:
    name = input("Enter name: ")
    if name != "EXIT":
        names.append(name)
    else:
        break

with open("names.txt", "w") as f:
    f.write("Name" + "\t" + "Surname" + "\t" + "Age" + "\n")
    for name in names:
        f.write(name+'\n')


#NAME   SURNAME   AGE   OPTIONS
# .CSV  COMMA SEP VALUES
# 123 - 123 - 123 - 412412 - 423
