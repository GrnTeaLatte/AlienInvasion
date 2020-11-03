pizza_toppings = input("Please enter requested pizza toppings.")

toppings = ""
while toppings != 'quit':
	toppings = input(pizza_toppings)
	print("Adding " + toppings + " to your pizza.")
