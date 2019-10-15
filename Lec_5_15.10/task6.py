my_dict = {}
my_dict = dict()

my_dict = {"Alice":22, "Bob":23}
print(my_dict["Alice"] + my_dict["Bob"])

my_dict["Nick"] = 28
print(my_dict)

print(my_dict.keys())
print(my_dict.values())

print(my_dict.items())

for k,v in my_dict.items():
    print(k, v)