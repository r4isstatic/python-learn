#!/usr/bin/env python

#This does an if statement, but checks for particular values (rather than from a set of values)

dinner = raw_input('Please choose Pizza or Spaghetti: ')
if dinner == "Pizza" or dinner == "Spaghetti":
	print "Bon Appetit!"
else:
	print "You can't have", dinner, "for dinner, you fool!"
