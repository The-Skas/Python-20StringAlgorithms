import pdb
# Duplicate characters in a str
# 
class InvalidTypeException(Exception):
	pass

class StringsQ(object):
	def __init__(self):
		pass

	"""
	A private class method for input sanitization
	"""
	@staticmethod
	def _checkInput(aStr):
		error_msg = "The parameter needs to be of type: 'str' \n\tinstead it is of type: "+str(type(aStr).__name__)
		if(isinstance(aStr,str) == False):
			raise InvalidTypeException(error_msg)
		elif( not aStr):
			raise InvalidTypeException("Parameter was an empty string.")
	
	@staticmethod
	def _dict_of_character_count(self,dict, str, i):
		value = dict.get(str[i],0)
		dict[str[i]] = value + 1

	@classmethod
	def get_duplicate_chars(self,aStr):
		# Make sure type is 'str'
		self._checkInput(aStr)

		duplicate_chars = ""

		for i in xrange(0,len(aStr)):
			for j in xrange(i, len(aStr)):
				if(aStr[i] == aStr[j] and i != j):
					duplicate_chars += aStr[i]

		return duplicate_chars
		# Make sure it returns a str
		# 
	
	@classmethod	
	def are_anagrams(self,str1,str2):
		import re 

		map(self._checkInput, [str1,str2])

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
		def dict_of_character_count(dict, str, i):
				value = dict.get(str[i],0)
				dict[str[i]] = value + 1

		for x in xrange(len(str1)):
			dict_of_character_count(dict1_CharacterCount, str1, x)
			dict_of_character_count(dict2_CharacterCount, str2, x)

		del dict_of_character_count

		for key1,value1 in dict1_CharacterCount.iteritems():
			value2 = dict2_CharacterCount.get(key1,0)
			if(value1 != value2):
				return False

		return True
		# Now 
	

	@classmethod
	def get_first_unique_character(self, aStr):
		self._checkInput(aStr)

		aStr = aStr.lower() 

		# Omg i'm making these these list comprehensions 
		# look ugly :O
		aStr_count_dict = {}
		[self._dict_of_character_count(self,aStr_count_dict, aStr, i) for i in range(len(aStr))]

		for char in aStr:
			if(aStr_count_dict[char] == 1):
				return char

		return ""





if __name__ == '__main__':

	a = StringsQ()

	print StringsQ.get_first_unique_character("Saywhat")

