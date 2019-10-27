#solution2
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text")

args = parser.parse_args()

middle_letter = len(args.text)/2
first_letter = int(middle_letter-1)
last_letter = int(middle_letter+2)
new_string = args.text[first_letter:last_letter]
print("The old string: " + args.text)
print("Middle 3 charecters:", args.text[first_letter:last_letter])
upper = new_string.upper()
string1 = args.text.replace(new_string, upper)
print("The new string: ", string1)