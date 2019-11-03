import argparse

parser = argparse.ArgumentParser()

dict1 = {'key1': 13, 'key2': 19, 'key3': 14}

parser.add_argument("key", type=str)
parser.add_argument("value", type=str)

args = parser.parse_args()


dict1[args.key] = args.value
print(dict1)
