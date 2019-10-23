def fib_loop(n):
    fib1 = 0
    fib2 = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n+1):
            fib1, fib2 = fib2, fib1 + fib2 

    return fib2 
for i in range(0,10):
    print(fib_loop(i))


def fib_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n-2) + fib_rec(n-1)

print("RECURSION F!")
for i in range(0,10):
    print(fib_rec(i))