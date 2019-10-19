def my_func(a,b):
    return a ** 2 + b ** 2

print(my_func(3,4))
#print(my_func(10))


# REQUIRED (POSITIONAL) ARGUMETS
def my_first_func(arg1, arg2, arg3):
    total = arg1 ** 2 + arg2 ** 3 + arg3 ** 4
    return total 

print(my_first_func(5,4,6))

# DEFAULT VALUE ARGUMENTS
def my_second_func(arg1, arg2, arg3 = "Hek"):
    total = arg1 + " "+ arg2 + "@" + arg3
    return total 

print(my_second_func("Lol", "Kek", "Name"))
print(my_second_func("Lol", "Kek"))

def my_third_func( arg2, arg1 = 5, arg3 = 12, arg4 = 123):
    return arg1 + arg2  + arg3 + arg4 **3

print(my_third_func(1,2))

def my_f_func(t = 2, p = 4, z = 10):
    return t + z + p
print(my_f_func())


