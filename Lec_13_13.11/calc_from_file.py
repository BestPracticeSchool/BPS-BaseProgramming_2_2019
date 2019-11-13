import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="name of .txt file with numbers", type=str)
args = parser.parse_args()
if args.file:
    nums = tuple()
    try:
        with open(args.file) as f:
            for num in f.readlines():
                num = num.strip()
                nums = nums +(int(num),)
        print(nums)
    except:
        print("File is not found!")
else:
    print("Try to use --help for more information")