data_base = []

while True:
    name = input("Enter your name OR EXIT to quit: ")
    if name == "EXIT":
        print("OVER TIME")
        print("GLAD TO SEE U AGAIN")
        break

    else:
        surname = input("Enter your surname: ")
        email = input("Enter your email: ")

        data_base.append([name, surname, email])

print("#############TOTAL LIST OF USERS##############")
for user in data_base:
    print(user[0], "|||||", user[1],"||||||", user[2])
print("#############################################")
print(data_base)