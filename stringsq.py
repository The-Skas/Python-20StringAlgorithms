"""
	This file is my attempt to go through string algorithms most frequently
	encountered in programming interviews.

	*article these questions are based on: 
		http://javarevisited.blogspot.co.uk/2015/01/top-20-string-coding-interview-question-programming-interview.html

	@author: The-Skas
"""

class InvalidTypeException(Exception):
	pass

def _checkInput(aStr):
	"""
		Common checks to make sure the parameter passed to a method
			is a string.
	"""
	error_msg = "The parameter needs to be of type: 'str' \n\tinstead it is of type: "+str(type(aStr).__name__)
	if(isinstance(aStr,str) == False):
		raise InvalidTypeException(error_msg)
	elif( not aStr):
		raise InvalidTypeException("Parameter was an empty string.")


def _dict_of_character_count(dict, str, i):
	""" Builds a dictionary of character count from a string. 
		The method is intended to be used with list comprehensions.
	"""
	value = dict.get(str[i],0)
	dict[str[i]] = value + 1


def get_duplicate_chars(aStr):
	"""
		gets a String of duplicate characters from the arguement.

		return: 
			*-Returns a String of duplicate characters from the arguement
			!-Otherwise, Returns an empty string ("")

	"""
	_checkInput(aStr)

	duplicate_chars = ""

	for i in xrange(0,len(aStr)):
		for j in xrange(i, len(aStr)):
			if(aStr[i] == aStr[j] and i != j):
				duplicate_chars += aStr[i]

	return duplicate_chars


def are_anagrams(str1,str2):
	"""
		Returns True if the two strings passed are anagrams.
			False otherwise.

		str1 -- a string.
		str2 -- another string.
		returns: True/False.
	"""
	import re 

	map(_checkInput, [str1,str2])

	# Strips anythings thats not a number, a word or underscore from the parameters
	str1 = re.sub("\W+", '', str1)
	str2 = re.sub("\W+", '', str2)

	# Make sure its lower case and strip it of spaces
	str1 = str1.lower().strip()
	str2 = str2.lower().strip()

	if (len(str1) != len(str2)):
		return False

	dict1_CharacterCount = {}
	dict2_CharacterCount = {}

	#this method is created for the sake of modularity.

	for x in xrange(len(str1)):
		_dict_of_character_count(dict1_CharacterCount, str1, x)
		_dict_of_character_count(dict2_CharacterCount, str2, x)

	for key1,value1 in dict1_CharacterCount.iteritems():
		value2 = dict2_CharacterCount.get(key1,0)
		if(value1 != value2):
			return False

	return True
	# Now 


def get_first_unique_character(aStr):
	"""
		Returns the first unique character found in a String
			(the character should only occur once).

		aStr -- a String

		returns: 
			*-a single Character if a unique character is found
			!-otherwise returns an empty string.
	"""
	_checkInput(aStr)

	aStr = aStr.lower() 

	# Omg i'm making these these list comprehensions 
	# look ugly :O
	aStr_count_dict = {}
	[_dict_of_character_count(aStr_count_dict, aStr, i) for i in range(len(aStr))]

	for char in aStr:
		if(aStr_count_dict[char] == 1):
			return char

	return ""





if __name__ == '__main__':
	print "Yeeehaw!"

