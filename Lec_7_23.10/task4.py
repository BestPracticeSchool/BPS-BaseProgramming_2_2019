def sum_of_squares(a,b):
    return  a**2 + b**2 - 2*a*b/1000

result = sum_of_squares(2,3)

y = sum_of_squares

x = lambda a,b : a**2 + b**2 - 2*a*b/1000



print("Def func result: ",y(2,3))
print("Lambda result is: ", x(2,3))
for i in range(0,100):
    print((lambda x1, y1: x1**2 + y1**2)(i,2*i))




