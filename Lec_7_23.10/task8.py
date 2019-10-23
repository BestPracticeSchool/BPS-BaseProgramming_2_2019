print("FOR LOOP BASED GENERATOR OF DICTIONARIES")
my_dict = {}
for i in range(1, 20):
    my_dict[(i+1, i+2, i**3)] = [i, i+1, i+2]
print(my_dict)

print("DICT COMPREHENSION")

my_new_dict = {(i+1, i+2, i**3):[i, i+1, i+2] for i in range(1,20) }
print(my_new_dict)