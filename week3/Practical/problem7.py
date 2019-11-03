import argparse

parser = argparse.ArgumentParser()

set1 = {"pig", "cow", "horse", "dog"}

parser.add_argument("new")

args = parser.parse_args()

set1.add(args.new)

print(set1)
