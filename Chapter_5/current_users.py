current_users = ['one', 'two', 'three', 'four', 'five']
new_users = ['six', 'four', 'eight', 'five', 'ten']

for user in new_users:
	if user in current_users:
		print("You will need a new username.")
	else:
		print("This username is available.")

