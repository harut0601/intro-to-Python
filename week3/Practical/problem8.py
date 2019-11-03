import argparse

parser = argparse.ArgumentParser()

parser.add_argument("set3")

set2 = {"pig", "cow", "horse", "dog"}

args = parser.parse_args()

new_set = set2.copy()

new_set.remove(args.set3)

print(set2)
print(new_set)