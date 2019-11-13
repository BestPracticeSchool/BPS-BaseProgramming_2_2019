import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo" , help="echo for inserting message")
parser.add_argument("another_echo", help="another echo for inserting message")
args = parser.parse_args()
print(args.echo)
print(args.another_echo)

