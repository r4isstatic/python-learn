#!/usr/bin/env python

#This creates a class called house. Then it defines two attributes. The second one is private (or 'encapsulated').
#This means that it can't be overwritten from outside the class itself - but it can be referenced by any methods within it.

#Then, there's two methods - the first goes through each of the number of doors, prints 'Slam!', then does something with the private attribute.
#The second allows you to set the value of the attribute inside the class from the outside.

class house:

	doors = 2
	__cost = 120000

	def slamDoors(self):
		for door in range(self.doors):
			print "SLAM!"
		print "that's a lot of slamming for a house that costs", self.__cost

	def addDoors(self, number):
		self.doors = number		

myHouse  = house()

myHouse.addDoors(22)

myHouse.slamDoors()

