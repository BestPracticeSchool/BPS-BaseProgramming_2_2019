group1 = set(["Nick","Andrew","Jose","Anna","Helga","Maria Ivanovna"])
group2 = set(["Andrew", "Anna","Bob","Alice", "Boromir","Jose"])

total_unique = group1.union(group2)
print(group1, len(group1))
print(group2, len(group2))
print(total_unique, len(total_unique))


unique_unique = group1.intersection(group2)
print(unique_unique, len(unique_unique))

unique_unique_2 = group2.intersection(group1)
print(unique_unique_2, len(unique_unique_2))

unique_list = list(unique_unique)
print(unique_list)