class User():
	def __init__(self, first_name, last_name, age, gender):
		self.first = first_name
		self.last = last_name
		self.age = age
		self.gender = gender
	def describe_user(self):
		print(self.first.title() + " " + self.last.title() + " is " + str(self.age) + " year old " + self.gender.title() + "." )
	def greet_user(self):
		print("Welcome, " + self.first.title() + " " + self.last.title() + "!")

first_user = User('audrey', 'fu', 31, "female")

first_user.describe_user()
first_user.greet_user()