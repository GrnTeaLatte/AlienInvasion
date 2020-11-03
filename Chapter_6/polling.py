favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
 	'edward': 'ruby',
	'phil': 'python',
}

poll = {
	'jen': 'python',
	'audrey': 'ruby',
	'kyle': 'r',
	'sarah': 'c',
}

for people in poll:
	if people in favorite_languages:
		print(people.title() + " thank you for taking this poll.")
	else:
		print(people.title() + " please take this poll.")