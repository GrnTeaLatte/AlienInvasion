# Importing multiple classes from a module

from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())


# Importing an entire module

import car

my_beetle = car.Car('volkswagon', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

# Importing all classes from a module (NOT RECOMMENDED)

from module_name import*

# better to import entire module and using this syntax:

module_name.class_name