#!/usr/bin/env python

#This imports the 'os' module and uses two of its functions to change the directory and then make a new one inside that.
import os
os.chdir('/Users/r4isstatic/Desktop')
print os.getcwd()
os.makedirs('dir-created-python')
