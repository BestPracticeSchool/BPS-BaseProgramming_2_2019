i = 12

while i < 10:
    print(i)
    i += 2
    print("INSIDE WHILE ", i)
else:
    print("OUTSIDE WHILE", i)

while True:
    print("First WHILE")
    while True:
        print("SECOND WHILE")
        break
    break