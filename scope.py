#!/usr/bin/env python

#This sets a variable with the value 'tutsplus'
#Then defines a function, where the variable is replaced with 'envato'
#Without the 'global' statement, the variable has two values - one which was set outside the function and one which is set inside.
#But if, inside the function, we set the variable to be global, then our overwriting of its value will apply everywhere.
variable = 'tutsplus'

def scopeInvestigator():
	global variable
	variable = 'envato'
	print "the variable inside the function is", variable

scopeInvestigator()
print	"the variable outside the function is", variable