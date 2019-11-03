import argparse

parser = argparse.ArgumentParser()

list4 = ["Hi", 1, True, 7]

parser.add_argument("new_value", type=int)

args = parser.parse_args()

new_value1 = args.new_value
list4.remove(new_value1)

print(list4)

