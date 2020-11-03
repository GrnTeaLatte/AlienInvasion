pizzas = ['cheese', 'hawaiian', 'hamburger']
friend_pizzas = pizzas[:]

pizzas.append('pepperoni')
friend_pizzas.append('sausage')


print("My favorite pizzas are: ")
for pizza in pizzas:
	print(pizza)

print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
	print(pizza)

