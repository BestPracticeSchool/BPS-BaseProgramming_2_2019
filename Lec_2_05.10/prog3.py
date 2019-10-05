minimum_age = 14 # и меньше --- не даем доступ
#от 14 до 18 --- неполный доступ к сервису
#больше 18 лет --- полный доступ 


age = int( input("Enter your age: ") )

if age <= minimum_age:
    print("BLOCKED!")
    print("U SHALL NOT PASS!")
    print("AGE ERROR!")
elif age  >= minimum_age and age < 18:
    print("PARTIAL PAGE!")
    print("PARTIAL WELCOME!")
else:
    print("FULL PAGE!")
    print("FULL WELCOME!")

