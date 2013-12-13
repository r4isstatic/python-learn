#!/usr/bin/env python


try:
	open('fakefile')
except IOError:
	print "Unable to open file"
finally:
	print "cleaning up code here"

print "this is important"