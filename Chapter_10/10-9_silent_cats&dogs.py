def cats_and_dogs(filename):
	try: 
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		pass
	else:
		print(contents.title())

filenames = ['dogs.txt', 'cats.txt']
for filename in filenames:
	cats_and_dogs(filename)