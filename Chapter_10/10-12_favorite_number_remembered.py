import json

filename = 'favorite_number.py'
try:
	with open(filename) as f_obj:
		favorite_number = json.load(f_obj)
except FileNotFoundError:
	favorite_number = input("What is your favorite number?")
	with open(filename, 'w') as f_obj:
		json_dump(favorite_number, f_obj)
		print("We'll remember your favorite number when you come back.")
else:
	print("Welcome back, your favorite number is: " + favorite_number)
