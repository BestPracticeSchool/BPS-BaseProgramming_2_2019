def my_func(a,b, c = 10):
    summ = a**2 + b**2 + c **4
    return summ , 2


q,e = my_func(3,4,5)
print(q, e)