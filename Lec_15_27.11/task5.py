def dangerFunc(a:int):
    assert ( a <= 10),"A has too big value"
    print("Hello form dangerFunc!!!")


sample = int(input()) 
try:
    dangerFunc(sample) #--- >1
    with open("file.log") as f:
        f.read()
except AssertionError as a_err:
    print(a_err)
    print("Try another 'sample' value!") # --- >2
except FileNotFoundError as f_err:
    print("COuld not found file: ", f_err)

# --->3