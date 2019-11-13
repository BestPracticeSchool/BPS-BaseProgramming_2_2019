import argparse

parser = argparse.ArgumentParser()

#python calculate.py -a1=5 -a2=10 -s=+ --- > 15
#python calculate.py -a1=2 s=+ --> 3
#python calculate.py -a1=3 -a2=10 -- > 13
parser.add_argument("-st", "--start", help="start to compile this program", action="store_true")
parser.add_argument("-a1", "--argument1", help="value of first argument in arithm operation", type=int)
parser.add_argument("-a2", "--argument2", help="value of second argument in arithm operation", type=int)
parser.add_argument("-s", "--sign", help="math operation sign ['+', '-', '*', '/']", choices=["+", "-", "*", "/"])

args = parser.parse_args()
if args.start:
    arg1 = args.argument1
    arg2 = args.argument2
    sign = args.sign
    if arg1 is None:
        arg1 = 1
    if arg2 is None:
        arg2 = 1
    if sign is None:
        sign ="+"


    if sign == "+":
        print("The sum operation of {} + {} = {}".format(arg1,arg2, arg1+arg2))
    elif sign == "-":
        print("The sub operation of {} - {} = {}".format(arg1,arg2, arg1-arg2))
    elif sign == "*":
        print("The mult operation of {} * {} = {}".format(arg1,arg2, arg1*arg2))
    elif sign == "/":
        print("The div operation of {} / {} = {}".format(arg1,arg2, arg1 / arg2))
    else:
        print("BAD REQUEST!")
else:
    print("Try to use --help for more information")
