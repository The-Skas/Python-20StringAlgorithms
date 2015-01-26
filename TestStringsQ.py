from stringsq import *
import unittest

class TestStringsQ(unittest.TestCase):

	def setup(self):
		pass

	def test_get_duplicate_chars(self):
		should_return_an_empty_string = get_duplicate_chars("heyo")
		self.assertEqual("", should_return_an_empty_string)

		should_return_l = get_duplicate_chars("hello")
		self.assertEqual("l", should_return_l)

		should_return_r = get_duplicate_chars("rawr")
		self.assertEqual("r", should_return_r)

		should_return_l = get_duplicate_chars("hello")
		self.assertEqual("l", should_return_l)

		self.assertRaises(TypeError, get_duplicate_chars,None)

		self.assertRaises(TypeError, get_duplicate_chars, "")
	

	
	def test_are_anagrams(self):
		"""
		Format of tuples is as follows

			(tuple2 : str1, tuple2 : str2, tuple3 : True/False)

			tuple2: string1 passed into the anagram method.
			tuple2: string2 passed into the anagram method.
			tuple3: the assertion of either True/False.

		"""
		anagram_input = (
				# Assert True
				("Hello", "olelH", 	   True),
				("Cool" , "looC",  	   True),
				("cool" , "looC",  	   True), #capitals shouldnt make a difference
				("Cool" , "looC",  	   True),
				("He1rr", "1rRhe",	   True),
				("  " , " ",	   	   True),
				("Army " , "Mary ",	   True),
				("Ar m y " , "M a ry ",True),
				# Assert False
				("Ar m y " , "M aary ",False),
				("Ar m y " , "M aary ",False),
			)

		def msg(x,y):
			return "Str1: "+x+" - Str2: "+y

		# Skas: Omg i'm making these these list comprehensions 
		# look ugly :0. Laziness Prevails!
		
		[self.assertEqual(condition, are_anagrams(x, y), msg(x, y)) \
			for x, y, condition in anagram_input] 

		del msg

	def test_get_first_unique_character(self):
		"""
		Format of tuples is as follows

			(tuple1 : string, tuple2 : char1)

			tuple1: String to be passed into the method
			tuple2: Character that should be returned

		"""
		unique_input_equals = (
				# When unique characters found
				("Hello",   "h"),
				("ehlol",   "e"),
				(" ",       " "), 
				("+!man",   "+"),
				# When Unique Chars NOT found
				("hh", 		 ""),
				("!!hhkk",   ""),
				("hkkkkh!!", "")
			)
		
		#
		unique_input_not_equals = (
				("Hello",   "e"),
				("hhelo",   "l"),
				("!!", "!"),
				("Hello", "H") 
			)

		# Runs a test on all the inputs
		# 	Skas: I know it looks ugly :{ ! Just doing it for the sake of learning!
		
		# Assert Equal
		[self.assertEqual(get_first_unique_character(input_str), result_char) \
			for input_str,result_char in unique_input_equals] 

		# Assert Not Equal
		[self.assertNotEqual(get_first_unique_character(input_str), result_char) \
			for input_str,result_char in unique_input_not_equals]  


if __name__ == '__main__':
	unittest.main()
