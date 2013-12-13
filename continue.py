#!/usr/bin/env python

#The continue statement basically resets the for loop - so it prints 'this is before', reaches the continue and then goes back to the beginning.

for i in range(2):
	print "this is before continue"
	continue
	print "this is after the continue statement"