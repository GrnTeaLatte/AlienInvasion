dinner_group = input("How many people are in your dinner group?")
group = int(dinner_group)

if group > 8:
	print("You will have to wait for a table.")
else:
	print("Your table is ready!")