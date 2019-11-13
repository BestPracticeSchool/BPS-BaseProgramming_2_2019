import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="Squared this value and printing", type=int)
args = parser.parse_args()
answer = args.square ** 2
print(answer)