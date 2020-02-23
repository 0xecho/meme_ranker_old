from django.test import TestCase

from .helpers import two_randint
# Create your tests here.

class RandomGenTestCase(TestCase):


	def test_randints_differ(self):

		rand_ints = two_randint(1000)

		self.assertNotEqual(*rand_ints)

	def test_randints_error(self):

		self.assertRaises(Exception, two_randint, 0)
