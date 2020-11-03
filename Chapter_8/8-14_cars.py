def make_car(manufacturer, model_name, **keyword):
	details = {}
	details['manufacturer'] = manufacturer
	details['model_name'] = model_name
	for key, value in keyword.items():
		details[key] = value
	return details

car_details = make_car('bmw', '335i', 
					color = 'blue',
					tow_package = True)

print(car_details)



