def make_sandwiches(*items):
	print("\nMaking a sandwich with ")
	for item in items:
		print("- " + item)

make_sandwiches('beef')
make_sandwiches('tomatoes','mozzarella')
make_sandwiches('tomatoes', 'lettuce', 'egg', 'cheese')

