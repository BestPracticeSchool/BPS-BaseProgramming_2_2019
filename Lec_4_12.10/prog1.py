#Коллекции. Часть 1

a_int = 10
b_float = 23.5
c_bool = True
q_str = "Hello"

#print( a_int + b_float )

# Упорядоченные коллекции

#["MyString1", "MyString2", "MyString3"]
#    0             1            2
#МЕШОК, ВЕРНИ ЭЛЕМЕНТ, ЖИВУЩИЙ ПО ИНДЕКСУ 2 ----> "MyString3"
#МЕШОК, ВЕРНИ ЭЛЕМЕНТ, ЖИВУЩИЙ ПО ИНДЕКСУ 3 --- > "Error OUT OF RANGE"

# Реализация массива
# 1. Списки

myList = list()
myList2 = []

#print( myList == myList2)

values_list = [10, -20 , 30, 500, 1000]
print(values_list)

print(values_list[0], values_list[1])
print("Last elemnt is : ", values_list[4])
print("New last element: ", values_list[-1])


values_list.append(300)
print("List after append : ", values_list)

values_list.pop()
print("List after deleted: ", values_list)

print( dir(values_list) )

print("The index : ", values_list.index(1000))
values_list.append(10)
values_list.append(10)

print("The new list: ", values_list)
print("The count works: ", values_list.count(10))






# 2. Кортежи