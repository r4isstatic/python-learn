#!/usr/bin/env python

#This imports the regular expression module, and prints out the characters in between the a and e in the word 'apple'

import re

print re.search('a(.*)e', 'apple').group(1)