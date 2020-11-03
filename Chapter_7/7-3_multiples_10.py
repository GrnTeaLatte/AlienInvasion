number = input("Pick a number from 1 to 100.")
number = int(number)

if number %10 == 0:
	print("This number is a multiple of ten.")
else:
	print("This number is not a multiple of ten.")