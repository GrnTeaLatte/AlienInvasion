# Using break to Exit a Loop
#The break statement directs the flow of your program; you can use it to control which lines of code are executed and which aren’t, so the program only
#executes code that you want it to, when you want it to. 

prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "

#A loop that starts with while True u will run forever unless it reaches a break statement
while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")
