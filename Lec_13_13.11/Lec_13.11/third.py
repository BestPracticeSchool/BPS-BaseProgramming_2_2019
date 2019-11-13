import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the following string")
args = parser.parse_args()
print(args.echo)