#! /usr/bin/env python

from collections import Counter

def nGram(n, items):
	length = len(items)

	if length <= n:   
		return -1

	nextChoices = []
	lastN = items[-n:]             # last n items
	for i in range(length - n):
		currN = items[i:i+n] 
		if  currN == lastN:
			nextChoices.append(items[i+n]) # for every sequence equal to the last n items, save the next item in a list
	
	if nextChoices: 
		frequencies = Counter(nextChoices)            # get the frequency for each distinct saved item
		return max(frequencies, key=frequencies.get)  # return the item with the highest frequency
	else:
		return -1
	