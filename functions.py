#!/usr/bin/env python

#defining functions. The first one sets two arguments, the %s is a placeholder for a string, then you say how to match them, afterwards.

def madlib(adjective='thirsty',name='adam'):
	print "the %s %s ate all the pizza" % (adjective,name)

# madlib(adjective='hungry',name='adam')

# This next function sets up a dictionary, sets some values, and stores it in 'dict'.
# Then the 'shoppingCart' function prints an item name, then, as the 'dbLookup' function is being used for the avgPrices argument, it takes in all the 'dict' values.
def dbLookup():
	dict = {}
	dict['amazon'] = 100
	dict['ebay'] = 120
	dict['bestBuy'] = 34
	return dict

def shoppingCart(itemName, avgPrices):
	print 'item: ',itemName
	for price in avgPrices:
		print price,'price: ',avgPrices[price]

shoppingCart('computer',dbLookup())

