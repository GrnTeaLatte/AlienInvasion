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

class Admin(User):
	def __init__(self, first_name, last_name, age, gender, privileges):
		super().__init__(first_name, last_name, age, gender)
		self.privileges = privileges
	def show_privileges(self):
			print("This user has " + str(self.privileges) + " privileges.")

first_user = Admin('audrey', 'fu', 31, 'female', ['can delete post', 'can add post', 'can ban user'])

first_user.describe_user()
first_user.greet_user()

first_user.show_privileges()

