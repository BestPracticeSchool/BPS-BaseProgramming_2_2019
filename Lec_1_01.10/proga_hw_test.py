# Задача 1. (ТЕСТОВАЯ) Слабенько.
# Название: Тестовая задача

# Условие: На вход программе подается 2 целых числа A,B>0.
# Подсчитать сумму квадратов чисел A и B.

# Входные данные : 2 числа (каждое на новой строке)
# Выходные данные : 1 число (сумма вида A^2 + B^2)

# Пример:
#Вход                          # Вывод
# 3
# 4                            25



# 6
# 8                           100


# 2
# 1                          5 

A = int( input() ) # --> str
B = int( input() )
print( A**2 + B**2 )