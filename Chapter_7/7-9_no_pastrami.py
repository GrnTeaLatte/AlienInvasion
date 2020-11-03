sandwich_orders = ['reuben', 'tuna melt', 'grilled cheese', 'pastrami', 'pastrami', 'pastrami']

finished_sandwiches = []

print("\nWe are out of pastrami.")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	requests = sandwich_orders.pop()

	print("I made your " + requests.title() + " sandwich.")
	finished_sandwiches.append(requests)


print("\nThe following sandwiches have been made: ")
for orders in finished_sandwiches:
	print(orders.title()) 