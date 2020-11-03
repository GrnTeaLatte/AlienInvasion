cities = {
	'beaufort': {
		'country': 'usa',
		'population': '234',
		'fact': 'huge water bugs'
	}, 
	'taipei': {
		'country': 'taiwan',
		'population': '456',
		'fact': 'hot and humid but good food'
	},
	'london': {
		'country': 'england',
		'population': '766',
		'fact': 'fish and chips ftw'
	}
}

for city, information in cities.items():
	country = information['country']
	population = information['population']
	fact = information['fact']
	
	print("\n" + city.title() + " is located in " + country.title() + ". \nIt has a population of " + population.title() + " people. \nAn interesting fact about " + city.title() + " is that it has " + fact + ".")