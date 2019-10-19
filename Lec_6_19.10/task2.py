def my_func(a, b): # ОПЕРАТОР ЯВНОГО ОПРЕДЕЛЕНИЯ ФУНКЦИИ
    return a**2 - b**2

def my_func_non_return(c, d):
    print(c,d) 
    print("HEY! I'm inside this function!")


#ВЫЗОВ ФУНКЦИИ
result = my_func(10, 15)
result2 = my_func(11,12)
result3 = my_func(10,100)
print(result, result2, result3)

my_func_non_return(10, 200)




