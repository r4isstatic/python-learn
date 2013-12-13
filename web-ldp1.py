#!/usr/bin/env python

import urllib
import re

# html = urllib.urlopen("http://jshawl.com/python-playground/").read()

html = urllib.urlopen("https://api.live.bbc.co.uk/ldp-core/creative-works?about=5e519ba4-2594-4118-a641-cdf75cd8ce46").read()

# print re.findall('[\w]+@[\w.]+', html)

print html