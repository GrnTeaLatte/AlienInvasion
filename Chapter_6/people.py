people = {
	'jaustin': {
		'first_name': 'jane',
		'last_name': 'austin',
		'city': 'london'
	},
	'kcheung': {
		'first_name': 'kyle',
		'last_name': 'cheung',
		'city': 'beaufort'
	},
	'audreyfu':{
		'first_name': 'audrey',
		'last_name': 'cheung',
		'city': 'fremont'
	}
}

for username, user_info in people.items():
	print("\nUser Name: " + username)
	full_name = user_info['first_name'] + " " + user_info['last_name']
	location = user_info['city']

	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title() )
