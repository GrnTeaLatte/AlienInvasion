message = input("\nPlease enter your age: ")
age = int(message)

if age < 3:
	print("\nYour ticket is free.")
elif age >= 3 and age <= 12:
	print("\nYour ticket is $10.")
else:
	print("\nYour ticket is $15.")
