#!/usr/bin/env python

#This is an example of recursion.
#we define a variable called 'number', which we'll pass the value 5 into at the end.
#the code then checks to see if the number = 1, in which case it stops
#at first, though, the number is 5, so it returns (i.e. sets 'factorial') to be number*that number - 1
#and then loops.

def factorial(number):
	if number == 1:
		return 1
	else:
		return number*factorial(number-1)

print "factorial is" factorial(5)