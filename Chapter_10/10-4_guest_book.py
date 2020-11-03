filename = 'guest_book.txt'

prompt = "\nPlease enter your name: "

while True:
	message = input(prompt)

	if message == 'exit':
		break

	with open(filename, 'a') as file_object:
			print("Hello " + message.title() + "!\nEnter another name or enter 'exit' to quit.")
			file_object.write(message + "\n")



 