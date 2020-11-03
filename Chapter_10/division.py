# Exceptions try/except blocks

try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

#Using exceptions to prevent crashes
# Try-except-block

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)

