cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

#checking for Equality
car = 'bmw'
car == 'bmw'
True

car = 'audi'
car == 'bmw'
False

#ignoring case when checking for equality
car = 'Audi'
car == 'audi'
False

car = 'Audi'
car.lower() == 'audi'
True

car = 'Audi'
car.lower() == 'audi'
True

print(car)


