#!/usr/bin/env python

#This uses the regex module again, and prints out just the things which are surrounding the @ and .com, i.e the email addresses and nothing else.

import re

print re.findall('\w+@\w+\.com','email1 is jessieshawl@sweep.com and email2 is bob@bobstemps.com')