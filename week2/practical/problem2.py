import argparse

parser = argparse.ArgumentParser()

parser.add_argument("user_name", type=str)
args = parser.parse_args()
print("Welcome,", args.user_name, "!")