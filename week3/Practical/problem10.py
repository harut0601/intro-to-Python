import argparse

parser = argparse.ArgumentParser()

parser.add_argument("set3")

set2 = {"pig", "cow", "horse", "dog"}

args = parser.parse_args()

new_set = set2.copy()
if args.set3 in set2:
    new_set.remove(args.set3)
    print(new_set)
print(f"old set: {set2}")
