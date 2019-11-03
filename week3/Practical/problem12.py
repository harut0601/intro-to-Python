import argparse

parser = argparse.ArgumentParser()

set3 = {7, 3, 5, 10, 250, 80, 45}

parser.add_argument("number", type=int)

args = parser.parse_args()


max_set = max(set3)
min_set = min(set3)

if args.number < max_set and args.number > min_set:
    print(True)
else:
    print(False)


