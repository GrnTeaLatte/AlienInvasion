favorite_places = {
	'audrey': ['home', 'london', 'amsterdam'],
	'kyle': ['with bundo', 'with auggie', 'with umbra'],
	'umbra': ['pillow', 'blanket', 'windowsill']
}

for person, places in favorite_places.items():
	print("\n" + person.title() + "'s favorite places are: ")
	for place in places:
		print("\t" + place.title())
