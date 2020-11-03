def show_magicians(magicians, great_magicians):
	while magicians:
		add_great = magicians.pop()

		print("The Great " + add_great.title())
		great_magicians.append(add_great)

def make_great(great_magicians):
	print("\nThe following magicians are great: ")
	for name in great_magicians:
		print(name)

magicians = ['doofus', 'joe', 'moe']
great_magicians = []

show_magicians(magicians[:], great_magicians)
make_great(great_magicians)