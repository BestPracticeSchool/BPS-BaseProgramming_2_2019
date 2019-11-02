"""
Return True in case ...
"""
def get_name(items, name):
    for item in items:
        if item['name'] == name:
            return True
    return False 



"""
Return ......
"""
def post_name(items, name):
    item = {"name" : name, "price" : 0.00}
    items.append(item)
    return item 


"""
Return ....
"""
def delete_name(items, name):
    items = [x for x in items if x['name'] != name]
    return items