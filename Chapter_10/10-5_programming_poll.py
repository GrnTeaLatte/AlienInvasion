filename = 'programming_reasons.txt'


prompt = "\nWhy do you like programming? "

while True:
	message = input(prompt)

	if message == 'exit':
		break

	with open(filename, 'a') as file_object:
			print("\nIs there another reason you like programming? \nEnter another reason or enter 'exit' to quit.")
			file_object.write(message + "\n")
qu