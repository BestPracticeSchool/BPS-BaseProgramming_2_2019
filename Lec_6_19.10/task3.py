def my_func(a, b ,c):
    summ = a + b + c
    return summ 

def another_func(a, b, c):
    print(a, b ,c) 
    #return None 
    return 10
    

def yet_another_function():
    print("I'M EMPTY!")
    #return None
    

result = my_func(1,2,3)
print(result)
print(my_func(2,3,4))


result2 = another_func(2,3,4)
print(result2)
print(another_func(4,5,6))
yet_another_function()

print(type(my_func(2,3,4)))

print(type(  yet_another_function  ))
print( dir(yet_another_function))

a = yet_another_function

a()