import json

favorite_number = input("What is your favorite number?")

filename = 'favorite_number.py'
with open(filename, 'w') as f_obj:
	json.dump(favorite_number, f_obj)


with open(filename) as f_obj:
	username = json.load(f_obj)
	print("I know your favorite number! It's " + favorite_number + "!")

