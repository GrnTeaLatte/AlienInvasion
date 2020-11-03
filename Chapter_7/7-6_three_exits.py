prompt = "\nPlease enter your age: "
prompt += "\nEnter 'quit' to exit. "

active = True

while active: 
	age = input(prompt)

	if age == 'quit':
		active = False
		break
	age = int(age)

	if age < 3:
		print("\nYour ticket is free.")
	elif age >= 3 and age <= 12:
		print("\nYour ticket is $10.")
	else:
		print("\nYour ticket is $15.")
