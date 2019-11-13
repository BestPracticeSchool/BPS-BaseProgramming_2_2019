import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="path to file", type=str)
args = parser.parse_args()

if args.file:
    print("Path to file is: ", args.file)
else:
    print("WHAT")