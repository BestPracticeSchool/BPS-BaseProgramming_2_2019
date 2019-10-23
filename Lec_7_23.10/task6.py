# Создать список натуральных чисел от 1 до 1500, в котором чётные числа возведены в квадрат,
# а нечетные - в куб
print("FOR LOOP BASED GENERATOR OF LISTS")
nums = []
for i in range(1,1501):
    if i % 2 == 0:
        nums.append(i**2)
    else:
        nums.append(i**3)
print(nums[:20])

print("LIST COMPREHENSION")
nums_list = [x**2  if x %2 == 0 else x**3 for x in range(1,1501)]
print(nums_list[:20])

a_zero = [[0,1,2] for x in range(1000)]
print(a_zero[:10])