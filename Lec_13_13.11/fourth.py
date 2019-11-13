import argparse 

parser = argparse.ArgumentParser()

parser.add_argument("-s","--square_this_value", help="squared values", type=int)
args = parser.parse_args()
if args.square_this_value :
    print(args.square_this_value ** 2)
else:
    print("This is default message!")