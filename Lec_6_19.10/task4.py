def h_func( another_func):
    print("I'M H FUNC")
    print('BEFORE another_func()')
    another_func()
    print("AFTER another_func()")
    return 200

def m_func():
    print("I'M MIDDLE FUNC")
    print("I'M WORKING!")

h_func(m_func)

func_list = [h_func, m_func]