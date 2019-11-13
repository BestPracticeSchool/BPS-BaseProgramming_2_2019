import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase values", action="store_true")
parser.add_argument("square", help="squared value", type=int)
args = parser.parse_args()
answer = args.square ** 2
if args.verbose:
    print("OK!")
    print("the square of {} is {}".format(args.square, answer))
else:
    print(answer)