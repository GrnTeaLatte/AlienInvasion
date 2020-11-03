class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	def describe_restaurant(self):
		print(self.restaurant_name.title() + " is a " + self.cuisine_type + " restaurant with great views.")
	def open_restaurant(self):
		print(self.restaurant_name.title() + " is open now.") 

my_restaurant = Restaurant('sala thai', 'traditional Thai')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


your_restaurant = Restaurant('le moose cafe', 'French Thai fusion')
your_restaurant.describe_restaurant()

his_restaurant = Restaurant('vons', 'Korean fried chicken')
his_restaurant.describe_restaurant()

her_restaurant = Restaurant('din ding', 'Cantonese dim sum')
her_restaurant.describe_restaurant()

