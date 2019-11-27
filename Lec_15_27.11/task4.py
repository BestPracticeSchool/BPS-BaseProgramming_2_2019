def dangerFunc(a:int):
    assert ( a <= 10),"A has too big value"
    print("Hello form dangerFunc!!!")


sample = int(input()) 
try:
    dangerFunc(sample)
except AssertionError as a_err:
    print(a_err)
    print("Try another 'sample' value!")

try:
    with open("file.log") as f:
        f.read()
except FileNotFoundError as f_err:
    print("COuld not found file: ", f_err)