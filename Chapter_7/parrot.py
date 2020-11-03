message = input("Tell me somethihng, and I will repeat it back to you: ")
print(message)

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

age = input("How old are you? ")
age = int(age)



# Letting the user choose when to quit
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
	message = input(prompt)

	if message != 'quit':
		print(message)

#Using a Flag
#Flag: variable acting as signal to program 
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)



