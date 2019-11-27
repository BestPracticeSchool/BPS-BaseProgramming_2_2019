my_value = 225
current = int(input())
if current > my_value:
    raise Exception("Current value bigger than my_value limit!!!!")

assert (current < my_value), "Assertion kek. Current bigger than my_val"