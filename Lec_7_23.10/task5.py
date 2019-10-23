def sum_of_seq(*args):
    return sum(args)/1000 ** 0.5
print("Def func res: ", sum_of_seq(20,30,400,60,70))


res = lambda *args: sum(args)/1000 ** 0.5
print("Lambda res: ",res(20,30,400, 60, 70))