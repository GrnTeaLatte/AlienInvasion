class User():
	def __init__(self, first_name, last_name, age, gender):
		self.first = first_name
		self.last = last_name
		self.age = age
		self.gender = gender
		self.login_attempts = 0 
	def describe_user(self):
		print(self.first.title() + " " + self.last.title() + " is " + str(self.age) + " year old " + self.gender.title() + "." )
	def greet_user(self):
		print("Welcome, " + self.first.title() + " " + self.last.title() + "!")
	def increment_login_attempts(self):
		self.login_attempts += 1
	def reset_login_attempts(self):
		self.login_attempts = 0 

first_user = User('audrey', 'fu', 31, 'female')

first_user.describe_user()
first_user.greet_user()

second_user = User('kyle', 'cheung', 29, 'male')

second_user.increment_login_attempts()
print(second_user.login_attempts)

second_user.increment_login_attempts()
print(second_user.login_attempts)

second_user.reset_login_attempts()
print(second_user.login_attempts)