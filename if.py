#!/usr/bin/env python

#This takes the user's input, stores it in 'name', then runs some tests - if the length is shorter than 5, if it's equal to, and if it equals 'Jesse'.

name = raw_input('Please type in your name: ')

if len(name) < 5:
	print "Your name is too short!"
elif len(name) == 5:
	print "Your name is the perfect length!"
	if name == "Jesse":
		print "Hey, Jesse!"
else:
	print "You have a long name!"
