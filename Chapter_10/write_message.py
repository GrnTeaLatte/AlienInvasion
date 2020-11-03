# Writing to a file

filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")

'''
The second argument, 'w', tells Python that we want to open the  le in write mode. You can open a file
in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows you to read and write to the file ('r+'). 
If you omit the mode argument, Python opens the  le in read-only mode by default.
'''

'''

Python can only write strings to a text file. 
If you want to store numerical data in a text file, you’ll have to convert the data to string format  
first using the str() functNion.
'''

with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")

