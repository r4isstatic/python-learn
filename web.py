#!/usr/bin/env python

import urllib
import re

html = urllib.urlopen("http://jshawl.com/python-playground/").read()

print re.findall('[\w]+@[\w.]+', html)
