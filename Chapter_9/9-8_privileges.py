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

class Privileges():
	def __init__(self, privileges):
		self.privileges = privileges
	def show_privileges(self):
		if self.privileges == 'admin':
			permissions = "can"
		elif self.privileges != 'admin':
			permissions = "cannot"
		message = "\nThis user " + permissions + " add posts."
		message += "\nThis user " + permissions + " delete posts."
		message += "\nThis user " + permissions + " ban users."
		print(message)

class Admin(User):
	def __init__(self, first_name, last_name, age, gender, privileges):
		super().__init__(first_name, last_name, age, gender)
		self.privileges = Privileges(privileges)
	#def show_privileges(self):
			#print(message)

first_user = Admin('audrey', 'fu', 31, 'female', 'user')

first_user.describe_user()
first_user.greet_user()

first_user.privileges.show_privileges()


