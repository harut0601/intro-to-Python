import argparse
import datetime

print("Current year: ", datetime.datetime.now())

parser = argparse.ArgumentParser()

parser.add_argument("--num_y")
parser.add_argument("--num_d")

args = parser.parse_args()

print("Given years: " + str(args.num_y))
print("Given days: " + str(args.num_d))

if args.num_y:
    mixed_years = int(datetime.datetime.now().year) - int(args.num_y)
    print("Final year: " + str(mixed_years))
else:
    print("Final year: Null")
    
if args.num_d:
    mixed_days = int(datetime.datetime.now().day) - int(args.num_d)
    print("Final day: " + str(mixed_days))
else:
    print("Final day: Null")



