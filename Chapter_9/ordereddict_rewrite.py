from collections import OrderedDict

glossary = OrderedDict()

glossary['variable'] = '2'
glossary['set'] = '4'
glossary['dictionary'] = '6'
glossary['loop'] = '8'
glossary['if statement'] = '10'

for term, meaning in glossary.items():
	print("\nTerm: " + term)
	print("\nMeaning: " + meaning)
