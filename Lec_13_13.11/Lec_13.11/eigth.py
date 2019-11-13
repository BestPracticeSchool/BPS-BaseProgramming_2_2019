import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase the number", type=int)
args = parser.parse_args()

if args.verbose:
    print("ok!")
    print(args.verbose + 1)