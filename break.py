#!/usr/bin/env python

#This does a loop, but then tests whether the loop counter has reached 5 - if it has, 'break' stops the loop

for i in range(10):
	print "i =", i
	if i == 5:
		break
print "done looping"