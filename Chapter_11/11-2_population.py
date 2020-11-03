import unittest
from city_functions import location

class LocationTestCase(unittest.TestCase):

	def test_city_country(self):
		formatted_location = location('san francisco', 'california')
		self.assertEqual(formatted_location, 'San Francisco, California')

	def test_city_country_population(self):
		formatted_location = location('fremont', 'california', 30000)
		self.assertEqual(formatted_location, 'Fremont, California - Population = 30000')

unittest.main()