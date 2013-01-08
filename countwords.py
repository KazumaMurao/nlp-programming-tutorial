#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

class WordCounter:
	def __init__(self):
		self.wordlist = {}

	def addword(self, s):
		if s in self.wordlist:
			self.wordlist[s] = self.wordlist[s] + 1
		else:
			self.wordlist[s] = 1

	def dispwords(self):
		for key in self.wordlist.keys():
			print key + " " + str(self.wordlist[key])

def main():
	if len(sys.argv) < 2:
		print "usage: python " + sys.argv[0] + " filename"
		return -1
	
	filename = sys.argv[1]
	file = open(filename, "r")

	wc = WordCounter()

	for line in file:
		line = line.strip()
		words = line.split(" ")
		
		for word in words:
			wc.addword(word)

	wc.dispwords()

if __name__ == "__main__":
	main()