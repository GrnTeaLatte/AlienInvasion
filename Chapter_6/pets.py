pets = {
	'levi': {
		'kind': 'cocker spaniel',
		'owner': 'audrey'
	},
	'umbra': {
		'kind': 'domestic shorthair',
		'owner': 'kyle'
	},
	'auggie': {
		'kind': 'australian shepherd mix',
		'owner': 'audrey'
	}
}

for pet, pet_details in pets.items():
	print("\nPet Name: " + pet.title())
	kind = pet_details['kind']
	owner = pet_details['owner']

	print("\tKind: " + kind.title())
	print("\tOwner: " + owner.title())
