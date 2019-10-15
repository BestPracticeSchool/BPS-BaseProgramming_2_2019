count = 0

user = []
while True:
    if count == 5:
        break
    name = input()
    age = int(input())

    user.append([name, age])

    count += 1

print(user)