def location(city, country, population=''):
	if population:
		destination = city + ', ' + country + ' - population = ' + str(population)
	else:
		destination = city + ', ' + country
	return destination.title()