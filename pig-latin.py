#!/usr/bin/env python

#This takes an input from the user, stores it in the variable called 'word', then prints the second character of the variable onwards, then takes the first character, prints it at the end, and adds 'ay'.

word = raw_input('Please enter your word to be translated! :')
print word[1:] + word[0] + 'ay'