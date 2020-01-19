import time
import str
import int

class ShortInputException(Exception):
	def __init__(self,length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

class LongInputException(Exception):
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

class UppercaseInputException(Exception):
	def __init__(self,uppercase ):
		Exception.__init__(self)
		self.uppercase = uppercase

uppercases = str.upper(uppercase)

class LowercaseInputException(Exception):
	def __init__(self, lowercase):
		Exception.__init__(self)
		self.lowercase = lowercase 

lowercases = str.lower(lowercase)
		
		

class IntInputException(Exception):
	def __init__(self,  digit):
		Exception.__init__(self)
		self.digit = digit 
		
digits = int(digit)	
		

		
try:
	text = input("Enter a string :").strip('')
	if len(text) < 8:
		raise ShortInputException(len(text), 8)

	if len(text) > 16:
		raise LongInputException(len(text), 16)

	for uppercase in uppercases:
		if text.upper().find(uppercase) != 1:
			raise UppercaseInputException(uppercase)

	for lowercase in lowercases:
		if text.lower().find(lowercase) != 1:
			raise LowercaseInputException(lowercase)
	
	for digit in digits:
		if text.int().find(digit) != 1:
			raise IntInputException(digit)


except UppercaseInputException as ex:
	print("UppercaseInputException: Please contain atleast one Uppercase letter {}". format(ex.uppercase))
except LowercaseInputException as ex:
	print("LowercaseInputException: Please contain atleast one lowercase letter {}". format(ex.lowercase))
except IntInputException as ex:
	print("IntInputException: Please input atleast one number {}". format(ex.digit))
except ShortInputException as ex:
	print("ShortInputException: Your entered string was too small. Should be atleast {}". format(ex.atleast))
except LongInputException as ex:
	print("LongInputException: Your entered string was too long.Should be at least {}". format(ex.atleast))
	
time.sleep(5)
input("Press any key to exit...")