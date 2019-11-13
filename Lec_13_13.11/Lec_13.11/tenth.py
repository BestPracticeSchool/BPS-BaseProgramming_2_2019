import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="verbosing value", type=int)
parser.add_argument("square", help="squared value", type=int)
args = parser.parse_args()
answer = args.square ** 2

if args.verbose == 1:
    print("the square of {} is {}".format(args.square, answer))
elif args.verbose == 2:
    print("{}^2 is {}".format(args.square, answer))
else:
    print(answer)