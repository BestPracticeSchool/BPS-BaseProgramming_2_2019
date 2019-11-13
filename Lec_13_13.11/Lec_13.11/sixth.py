import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="smthing")
args = parser.parse_args()
if args.verbosity:
    print("OK!")