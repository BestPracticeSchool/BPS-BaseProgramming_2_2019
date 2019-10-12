# 2. Кортежи

my_tuple = tuple()
my_tuple2 = ()
print(my_tuple2)
me = [1]



me2 = (1,)

print(type(me), me)
print(type(me2), me2)

temp = (1,2,3,4,5,6,7,8,10)

print( temp[0], temp[-1], temp[3])

for j in temp:
    print(j)

print(temp[::-1])

temp = temp + temp
print(temp)
print( dir(temp))
print(sum(temp))
print(len(temp))