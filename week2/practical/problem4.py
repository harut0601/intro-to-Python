import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--age")
args = parser.parse_args()

print("Happy Birthday, you are already", args.age, "years old!")