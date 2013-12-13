#!/usr/bin/env python

#This just imports a single argument from a module, then takes the last thing in the argument supplied when you called the file, and replies in the appropriate way

from sys import argv

if argv[-1] == "purr":
	print "meow!"
if argv[-1] == "bark":
	print "woof!"
