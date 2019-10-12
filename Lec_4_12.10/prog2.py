temper = [10, 2, -200, 1, 3000]
temper[2] = 200 # СПИСКИ ИЗМЕНЯЕМЫЕ
print(temper)


temper.append(23.5)
temper.append(True)
temper.append(None)
temper.append("HELLO")
print(temper)

a = [3, 4, 5]
temper.append( a ) # Вложенность списков
print(temper)


# Индексация

print(temper[0],temper[-1], temper[2])

print(temper[-1][1]) # Вложенная индексация

print(temper[0], temper[1], temper[2], temper[3], temper[4] )
# Срезы
print( temper[0:5])
print( temper[2:])
print(temper[:5])
print(temper)
print( temper[0:7:2])

print( temper[::-1] )


# Итерирование
print("FOR LOOP HERE")
for i in temper:
    print(i)


# Длина списка
print("LENGTH FUNCTION")
print(len( temper )) 
