rivers = {
	'nile': 'egypt',
	'colorado river': 'colorado',
	'amazon': 'south america'
}

for river, location in rivers.items():
	print("The " + river.title() + " runs through " + location.title() + ".")

for river in rivers:
	print(river.title())

for location in rivers.values():
	print(location.title())