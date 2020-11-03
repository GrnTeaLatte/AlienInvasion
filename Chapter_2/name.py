#Capitalization
#changing case in a string with methods


#A method is an action that Python can perform on a piece of data. The
#dot (.) after name in name.title() tells Python to make the title() method
#act on the variable name. Every method is followed by a set of parentheses,
#because methods often need additional information to do their work.
#That information is provided inside the parentheses. The title() function
#doesn’t need any additional information, so its parentheses are empty. 

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#Concatenation: strings and methods
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

message = ("Hello, " + full_name.title() + "!")
print(message)

#Indent
print("Python")
print("\tPython")

#New Line
print("Languages:\nPython\nC\nJavaScript")

#Stripping whitespace
favorite_language = ' python '
print (favorite_language)
favorite_language = favorite_language.rstrip()
print (favorite_language)
favorite_language = favorite_language.lstrip()
print (favorite_language)
