import unittest

# def ifEnhanceAnd(l):
# 	for x in range(len(l)):
# 		line=int(x)
# 		x=l[x]
# 		if "if" in x:
# 			t=x[x.find("if")+len("if"):-1].split("and")
# 			for i in range(len(t)):
# 				t[i]="("+t[i].strip()+")"
# 			for i in range(len(t)):
# 				l[line]=inline_addition(t," and ")
# 			l[line ]="if"+l[line]+":"
#
# 	return l

class testingCodeEnhancer(unittest.TestCase):
	"""docstring for testingCodeEnhancer"""
	def __init__(self, arg):
		super(testingCodeEnhancer, self).__init__()
		self.arg = arg

	def setup(self):
		testStringOr  = ['if 5>3 or 3>4:']
		testStringAnd = ['if 5>3 and 4>3:']

	def testingIfEnhanceAnd(self):
		
