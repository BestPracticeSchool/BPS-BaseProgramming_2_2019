import argparse

parser = argparse.ArgumentParser()
parser.parse_args()


print(dir(parser.parse_args()))
print(type(parser.parse_args()))