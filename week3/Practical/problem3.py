import argparse

parser = argparse.ArgumentParser()

list2 = [0, 'hi', 2, 100, 300, 2]

parser.add_argument("new_value", type=int)

args = parser.parse_args()

print("The given list:", list2)
print(f"Number of {args.new_value}'s: ", list2.count(args.new_value))