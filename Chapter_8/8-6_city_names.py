def city_country(city, country):
	if country == 'usa':
		location = city.title() + ", " + country.upper()
	else:
		location = city.title() + ", " + country.title()
	return location

destination = city_country('santiago', 'chile')
print(destination)

destination = city_country('boston', 'usa')
print(destination)

destination = city_country('curon', 'italy')
print(destination)