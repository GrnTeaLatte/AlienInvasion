import unittest
from city_functions import location

class LocationTestCase(unittest.TestCase):
	def test_city_country(self):
		formatted_location = location('san francisco', 'california')
		self.assertEqual(formatted_location, 'San Francisco, California')

unittest.main()