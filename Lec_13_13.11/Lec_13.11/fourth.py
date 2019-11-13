import argparse

parser = argparse.ArgumentParser()
parser.add_argument("num", help="squared argument num")
args = parser.parse_args()
print(int(args.num) ** 2)