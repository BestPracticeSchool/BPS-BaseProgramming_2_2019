print(2,3,4,4,5,5,5,5,1,1,1)


# RANGE CONTINUES ARGUMETNS
# TUPLE BASED
def my_func_with_cont(*args):
    print(type(args))
    for i in args:
        print(i)


my_func_with_cont(1,2,3,4,5,6,87,2,4,6,3,67543,123)

# DICT BASED

def my_func_with_cont_2(**kwargs):
    print(type(kwargs))
    print(kwargs)

my_func_with_cont_2( a = 1, b = 2, c = 3, t = 100)




# RESUME

def total(num1, num2, *args, **kwargs):
    pass 