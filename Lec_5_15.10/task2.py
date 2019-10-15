# Хэш-таблица - неупорядоченное множество пар ключ:значение с уникальным ключом.

my_set = set()
print(my_set)

my_set = set([10,12,13,1,2,3,4,5,6,5,4,3,2,1, "Hello","Hello", "Jose"])
print(my_set, type(my_set))

#print(my_set[0])

print(dir(my_set))
my_set.add(8888)
print(my_set)