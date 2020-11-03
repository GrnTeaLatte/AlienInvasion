#Write an if-elif-else chain that determines a person’s
#stage of life. Set a value for the variable age, and then:

age = 12

if age < 12:
	print("This person is a baby")
elif age >= 2 and age < 4:
	print("This person is a toddler")
elif age >= 4 and age < 13:
	print("This person is a kid")
elif age >= 12 and age < 20:
	print("This person is a teenager")
elif age >= 20 andN age < 65:
	print("This person is an adult")
else:
	print("This person is an elder")