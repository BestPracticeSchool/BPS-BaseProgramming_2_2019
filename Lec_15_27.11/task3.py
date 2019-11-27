def dangerFunc(a:int):
    assert ( a <= 10),"A has too big value"
    print("Hello form dangerFunc!!!")


try:
    sample = 13
    dangerFunc(sample) # --->assertionError
except: # --- > catch assertionError --- > except body: pass
    print("Maybe try another value of sample ?")
# --> graceful shtdwn