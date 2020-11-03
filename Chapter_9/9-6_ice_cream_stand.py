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

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type, flavors):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors
	def ice_cream_flavors(self):
		print("These are the ice cream flavors available: " + str(self.flavors))

		
my_restaurant = IceCreamStand('sala thai', 'modern fusion', ['strawberry', 'vanilla', 'mango'])

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.ice_cream_flavors()
 
