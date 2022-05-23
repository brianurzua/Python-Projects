# This is a class that shows encapsulation

""" 
This class should make use of a private attribute or function.

This class should make use of a protected attribute or function.

Create an object that makes use of protected and private.

Add comments throughout your Python explaining your code.
"""

class ourDog:
	# This is a private attribute
	def __init__(self):
		self.__name = 'itachi'

	# This makes use of the protected and private variables
	def Command(self):
		print("He answers to {}".format(self.__name))

	# This is a setter function, meaning we can change the name by taking it as a parameter.
	def changeName(self, name):
		self.__name = name

D = ourDog()
D.Command()

D.__name = 'Sasuke'
D.Command()

D.changeName('Sasuke') # Use the setter to change name
D.Command()