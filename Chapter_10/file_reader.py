with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())

# Accessing files from different folders
'''
with open('text_files/filename.txt') as file_object:
'''

# Absolute file path
'''
file_path = '/home/ehmatthes/other_files/text_files/filename.txt' 
with open(file_path) as file_object:
'''

# Reading line by line

filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())


# Making a list of lines from a file

filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())



