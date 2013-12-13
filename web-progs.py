#!/usr/bin/env python

import urllib
import re

html = urllib.urlopen("http://www.bbc.co.uk/programmes/b036bqq0.xml").read()

print re.findall('[\w]+doctor[\w]+', html)