favorite_numbers = {
	'kyle': '24',
	'audrey': '4',
	'nathan': '15',
	'derek': '57',
	'auggie': '6'
}

print("Kyle's favorite number is " + favorite_numbers['kyle'] + ".")
print("\nAudrey's favorite number is " + favorite_numbers['audrey'] + ".")
print("\nNathan's favorite number is " + favorite_numbers['nathan'] + ".")
print("\nDerek's favorite number is " + favorite_numbers['derek'] + ".")
print("\nAuggie's favorite number is " + favorite_numbers['auggie'] + ".")



favorite_numbers = {
	'kyle': ['24', '4'],
	'audrey': ['4', '2', '53'],
	'nathan': ['15', '34', '25'],
	'derek': ['57', '3'],
	'auggie': ['6', '34']
}

for name, favorite_number in favorite_numbers.items():
	print("\n" + name.title() + "'s favorite numbers are: ")
	for number in favorite_number:
		print("\t" + number)
