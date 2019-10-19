# ОНО
# АННА
# ТОТ 

def isPalindrome(message):
    if message == message[::-1]:
        return True
    return False 


while True:
    user = input()
    if user == "EXIT":
        break 
    else:
        if isPalindrome(user):
            print("YESSS")
        else:
            print("NOOO")

print("ALLES")