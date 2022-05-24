# This is a class that shows abstraction

""" 
Your class should contain at least one abstract method and one regular method.  

Create a child class that defines the implementation of its parents abstract method.

Create an object that utilizes both the parent and child methods.
 
Add comments throughout your Python explaining your code.

"""

from abc import ABC, abstractmethod

# class that contains one abstract method and regular method
class Polygon(ABC):
	def polySides(self, sides):
		print("I am a polygon, I am made of straight lines. I can have {} sides".format(sides))

	@abstractmethod # abstract method
	def Sides(self, sides):
		pass

class Triangle(Polygon):
	# Implementing the Sides function
	def Sides(self, sides):
		print("I'm a triangle, I'm a polygon made of {} sides".format(sides))

obj = Triangle()
obj.polySides(360)
obj.Sides(3)