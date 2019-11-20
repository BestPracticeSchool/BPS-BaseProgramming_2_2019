def div(a,b):
    return a/b


try:
    a, b = int(input()), int(input())
    res = div(a,b)
except ZeroDivisionError as err:
    print(err)
    print(div(a, 0.0000000001))
except ValueError as v_err:
    print(v_err)
else:
    print("ELSE WORKING!")
    print("Result is: ", res)
finally:
    print("ALLES DONE!")
    


