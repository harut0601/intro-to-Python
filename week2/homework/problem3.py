import argparse

parser = argparse.ArgumentParser()

parser.add_argument("string1")
parser.add_argument("new")

args = parser.parse_args()

print( "The given string: ", args.string1)
print("The USA/usa count is: ", args.string1.lower().count("usa"))
the_new_string = args.string1.replace('usa', args.new).replace('USA',args.new)

print(the_new_string)

