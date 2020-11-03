sandwich_orders = ['reuben', 'tuna melt', 'grilled cheese']

finished_sandwiches = []

while sandwich_orders:
	requests = sandwich_orders.pop()

	print("I made your " + requests.title() + " sandwich.")
	finished_sandwiches.append(requests)

print("\nThe following sandwiches have been made: ")
for orders in finished_sandwiches:
	print(orders.title()) 