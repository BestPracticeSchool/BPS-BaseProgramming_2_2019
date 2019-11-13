import argparse

parser = argparse.ArgumentParser()
parser.add_argument("num", help="squared argument num", type=int)
args = parser.parse_args()
print(args.num ** 2)