#!/usr/bin/env python

class DinnerError(Exception):
	pass

def makeDinner():
	userinput = raw_input("Please choose a dinner item: ")
	if userinput == "ice cream":
		raise DinnerError ("Not nutritious enough")
	if userinput == "computer":
		raise DinnerError ("Not a dinner item")

try:
	makeDinner()		
except DinnerError, explanation:
	print "Error:", explanation