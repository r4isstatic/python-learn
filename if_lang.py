#!/usr/bin/env python

#This does an if statement, but tests it against a known set of values, rather than a number.

language = raw_input('Please enter a programming language: ')

if language in ['C++','python','Java']:
	print language, "is great!"
