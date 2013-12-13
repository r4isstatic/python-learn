#!/usr/bin/env python

#This creates a class called house. Then it defines two attributes. The second one is private (or 'encapsulated').
#This means that it can't be overwritten from outside the class itself - but it can be referenced by any methods within it.

#Then, there's two methods - the first goes through each of the number of doors, prints 'Slam!', then does something with the private attribute.
#The second allows you to set the value of the attribute inside the class from the outside.

class house:

	def __init__(self, doors=3):
		self.doors = doors

	def slamDoors(self):
		for door in range(self.doors):
			print "SLAM!"
		print "that's a lot of slamming for a house that costs", self.__cost

	def addDoors(self, number):
		self.doors = number		


class castle(house):
	
	def fireCannons(self, number):
		for cannon in range(number):
			print "firing cannon number", cannon, "BOOM!"

	def payMortgage(self):
		print "readying the cannons!"		


class apartment(house):

	def payMortgage(self):
		print "here's your money!"


landlordsProperties = [castle(), apartment()]

for house in landlordsProperties:
	house.payMortgage()
