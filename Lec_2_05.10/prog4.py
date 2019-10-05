temp = 21

print("Больше: ", temp > 20)
print("Меньше: ", temp < 25)
print("Больше или равно: ", temp >= 21)
print("Меньше или равно: ", temp <= 1)


print("Проверка на равенство: ", temp == 21)
print("Проверка на НЕравенство: ", temp != 21)


temp_bool = True

if temp_bool and False:
    print("HEY!")
#
#Таблица истинности
print("========AND==========") # Логическое умножение
print("True and True : ", True and True)
print("True and False : ", True and False)
print("False and True : ", False and True)
print("False and False : ", False and False)

print("========OR==========") # Логическое сложение
print("True or True : ", True or True)
print("True or False : ", True or False)
print("False or True : ", False or True)
print("False or False : ", False or False)