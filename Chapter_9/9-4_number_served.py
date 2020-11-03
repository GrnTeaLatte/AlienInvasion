class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 9
	def describe_restaurant(self):
		print(self.restaurant_name.title() + " is a " + self.cuisine_type + " restaurant with great views.")
	def open_restaurant(self):
		print(self.restaurant_name.title() + " is open now.")
	def customers_served(self):
		print(str(self.number_served) + " satisfied customers served.")  
	def set_number_served(self, served):
		self.number_served = served
	def increment_served(self, number):
		self.number_served += number 



my_restaurant = Restaurant('sala thai', 'modern fusion')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.set_number_served(23)
my_restaurant.customers_served()

my_restaurant.increment_served(345)
my_restaurant.customers_served()




