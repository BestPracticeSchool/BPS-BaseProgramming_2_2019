for i in range(0, 1000000):
    if i ** (i + 1) > 9999999999:
        print("Near break statement")
        print("Current values of i : ", i)
        continue

print("Outside range based for")
    