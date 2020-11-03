from random import randint



x = randint(1, 6)
#sprint(x)



class Die():
	def __init__(self, sides = 6):
		self.sides = sides

	def roll_die(self):
		print(randint(1, self.sides))

six_die = Die(6)
six_die.roll_die()

ten_die = Die(10)
ten_die.roll_die()

