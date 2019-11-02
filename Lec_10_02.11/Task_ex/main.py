import rest as r

items = [
    {
        "name":"MyItem",
        "price": 150.22
    },
    {
        "name":"AnotherName",
        "price": 13.99
    }
]


print(r.get_name(items, "MyItem"))
print(r.get_name(items, "MyItem2"))
r.post_name(items, "MyItem2")
print(r.get_name(items, "MyItem2"))
items = r.delete_name(items, "MyItem2")
print(r.get_name(items, "MyItem2"))
# Содержится ли объект с именем name в items
# Добавить объект с именем name в items
# Удалить объект с именем name из items
print(dir(r))