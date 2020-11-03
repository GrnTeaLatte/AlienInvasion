alien_color = 'green'

if 'green' in alien_color:
	print("Player earned 5 points")
if 'red' in alien_color:
	print("No output")

alien_color = 'red'

if 'green' in alien_color:
	print("Player earned 5 points")
else:
	print("Player earned 10 points")

alien_color = 'blue'

if 'green' in alien_color:
	print("Player earned 5 points")
elif 'blue' in alien_color:
	print("Player earned 10 points")
elif 'red' in alien_color:
	print("Player earned 5 points")
else:
	print("Player earned 10 points")
