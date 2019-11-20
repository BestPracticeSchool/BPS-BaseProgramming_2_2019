def div(a,b):
    return a/b


try:
    a, b = int(input()), int(input())
    print(div(a,b))
except ZeroDivisionError as err:
    print("The error was found: ", err)
except ValueError as v_err:
    print("Try to use numbers: ", v_err)