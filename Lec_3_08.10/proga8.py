hybrid = 0

for i in range(0, 1000001):
    if i % 2 == 0:
        hybrid += i
    else:
        hybrid += i ** 2

print(hybrid)