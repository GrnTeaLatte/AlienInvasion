numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for number in numbers:
	if '1' in number:
		print(number + 'st')
	elif '2' in number:
		print(number + 'nd')
	elif '3' in number:
		print(number + 'rd')
	else:
		print(number + 'th')
