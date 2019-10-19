message = input()
check = False 
if "a" in message.lower() or "b" in message.lower() or "c" in message.lower():
    check = True

check = False 
while True:
    message = input()
    if message == "EXIT":
        break
    else:
        if "a" in message.lower() or "b" in message.lower() or "c" in message.lower():
            check = True 

#
###
#

check = False
for i in range(0,1000):
    message = input()
    if i // 13 == 0:
        break
    else:
        if "a" in message.lower() or "b" in message.lower() or "c" in message.lower():
            check = True