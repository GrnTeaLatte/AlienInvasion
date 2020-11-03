class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	def describe_restaurant(self):
		print(self.restaurant_name.title() + " is a " + self.cuisine_type + " restaurant with great views.")
	def open_restaurant(self):
		print(self.restaurant_name.title() + " is open now.") 

my_restaurant = Restaurant('sala thai', 'modern fusion')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()