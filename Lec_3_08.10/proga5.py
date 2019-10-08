n = int(input())
i = 0

damage = 0
while i < n:
    damage += i ** 2
    damage_yad = int(input("Enter dopolnitelny damage: "))
    damage += damage_yad 
    i = i + 1

print("Total damage is : ", damage)

    