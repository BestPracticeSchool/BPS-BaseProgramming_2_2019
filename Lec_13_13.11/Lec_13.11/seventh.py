import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbos", help="kek", action="store_true")
args = parser.parse_args()
if args.verbos:
    print("OK!")