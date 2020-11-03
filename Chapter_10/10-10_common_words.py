line = "Row, row, row your boat"
print(line.count('row'))

print(line.lower().count('row'))

def count_words(filename):
	try: 
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + filename + " does not exist."
		print(msg)
	else:
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")


filenames = ["The Adventure of the Devil's Foot - Arthur Conan Doyle.txt", 
"The Adventure of the Red Circle - Arthur Conan Doyle.txt", 
"The Moonstone - Wilkie Collins.txt", "The Shunned House - HP Lovecraft.txt"]
for filename in filenames:
	count_words(filename)
