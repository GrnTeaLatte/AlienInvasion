favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
 	'edward': 'ruby',
	'phil': 'python',
}

print("Sarah's favorite language is " +
	favorite_languages['sarah'].title() +
	".")


for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title() + ".")

for name in favorite_languages.keys():
	print(name.title())

# can also write: for name in favorite_languages:

# definining new list to use with favorite_languages:
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print(" Hi " + name.title() + ", I see your favorite language is " + 
			favorite_languages[name].title() + "!")

	#checking if name is in list
	if 'erin' not in favorite_languages.keys():
		print("Erin, please take our poll!")


# looping through a dictionary's keys in order:

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

# looping through all values in a dictionary:

print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

# for no repitition: a set

for language in set(favorite_languages.values()):
	print(language.title())


favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
 	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())




