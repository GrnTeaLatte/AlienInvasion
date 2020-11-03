usernames = ['admin', 'kyle', 'audrey', 'nathan', 'derek']

if usernames: 
	for name in usernames:
		print("Greetings " + name.title() + "!")
		if 'admin' in name:
			print("Hello, " + name.title() + " do you want to see a status report?")
		else:
			print("Hello, " + name.title() + " thank you for logging in again.")
else:
	print("We need to find some users!")
