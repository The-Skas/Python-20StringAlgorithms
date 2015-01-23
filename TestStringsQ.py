from stringsq import StringsQ
import unittest
import pdb
class TestStringsQ(unittest.TestCase):

	def setUp(self):
		pass

	def testGetDuplicateChars(self):
		should_return_l = StringsQ.getDuplicateChars("hello")
		self.assertEquals(should_return_l, "l")

		should_return_a = StringsQ.getDuplicateChars("mama")
		self.assertEquals(should_return_a, "a")

def main():
    unittest.main()
if __name__ == '__main__':
	main()

	