import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	def setUp(self):
		prompt = "Enter First and Last name of employee."
		self.identity = Employee('Kyle', 'Fu', 10000)

	def test_give_default_raise(self):
		self.identity.give_raise()
		self.assertEqual(self.identity.annual_salary, 15000)

	def test_give_custom_raise(self):
		self.identity.give_raise(10000)
		self.assertEqual(self.identity.annual_salary, 20000)

unittest.main()
