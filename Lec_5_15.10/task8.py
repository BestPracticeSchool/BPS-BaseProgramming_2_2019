nums = {"Milky Way":1000, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "machete":7, "Ricardo":69}

keys_list = list(nums.keys())
keys_list.sort()

print("M" < "m")
print(ord("m"), ord("M"))

print("######sorted keys output####################")
for key in keys_list:
    print(key, nums[key])


print("##################sorted values output#######################")
values_list = list(nums.values())
values_list.sort()

for value in values_list:
    print(value)