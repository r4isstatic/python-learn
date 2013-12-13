#!/usr/bin/env python

import urllib
import urllib2
from cookielib import CookieJar

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

formValues = {
	"username":"user",
	"password":"pass"
}

data = urllib.urlencode(formValues)

response = opener.open("http://jshawl.com/python-playground/login.php", data)

#print response.read()

secure = opener.open("http://jshawl.com/python-playground/protected2.php")
print secure.read()