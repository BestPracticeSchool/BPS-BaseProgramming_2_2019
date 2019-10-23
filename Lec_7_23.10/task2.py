#РЕКУРСИЯ - вызов функции внутри функции
#РЕКУРСИЯ - вызов функции внутри самой себя
#РЕКУРСИЯ - функциональное замыкание


#ФАКТОРИАЛ
# n! = n * (n -1 ) * (n-2) * .... *1
# 0! = 1
# 1! = 1

def factor(n):
    if n <= 1:
        return 1
    else:
        return factor(n-1) * n

#factor(3) -- > 3 <= 1 ? False -- > return 1 * 2 * 3 --- > 6
#factor(2) --- > 2 <= 1? False --- > return 1 * 2
#factor(1) ---> 1<= 1? True ---> return 1

print(factor(100))

def loop_factor(n):
    pass 

