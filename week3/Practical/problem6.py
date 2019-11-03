import argparse

parser = argparse.ArgumentParser()

list4 = ["Hi", 1, True, 7]

list5 = list4.copy()

parser.add_argument("new_value1", type=int)

args = parser.parse_args()

new_value = args.new_value1
list5.remove(new_value)

print(f"The old list: {list4}")
print(f"The new list: {list5}")

