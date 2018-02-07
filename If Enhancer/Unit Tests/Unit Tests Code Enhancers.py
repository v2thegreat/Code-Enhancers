from ifEnhancer import *
import unittest

testStringOr  = ['if 5>3 or 3>4:']
testStringAnd = ['if 5>3 and 4>3:']

correctValueAnd = ['if (5>3) and (4>3):']
correctValueOr = ['if (5>3) or (3>4):']

class testingCodeEnhancer(unittest.TestCase):
	"""docstring for testingCodeEnhancer"""
	def setUp(self):
		self.testStringOr  = ['if 5>3 or 3>4:']
		self.testStringAnd = ['if 5>3 and 4>3:']

		self.correctValueAnd = ['if (5>3) and (4>3):']
		self.correctValueOr = ['if (5>3) or (3>4):']

	def testingIfEnhanceAnd(self):
		self.assertEqual(ifEnhanceAnd(self.testStringAnd), self.correctValueAnd)

	def testingIfEnhanceOr(self):
		self.assertEqual(ifEnhanceOr(self.testStringOr), self.correctValueOr)

if __name__ == '__main__':
    unittest.main()
