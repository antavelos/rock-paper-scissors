#! /usr/bin/env python

import ngram
import random

class Rps:

	def __init__(self, n):
		self.humanScore = 0
		self.computerScore = 0
		self.nFactor = n
		self.moves = []
		self.accepted = 'rps'

	def game(self):
		while True:
			human = raw_input('Your move (r/p/s): ')
			if human not in self.accepted and human not in self.accepted.upper():
				print 'Your move must be one of those letter: r, p s, R, P, S';
				continue
			self.moves.append(human)

			computer = self.decision()
			print 'Computer:          ' + computer
			res = self.result(computer, human)

			if res == 1:
				self.computerScore += 1
			if res == 2:
				self.humanScore += 1

			self.printScore()

	def decision(self):
		nextMove = ngram.nGram(self.nFactor, self.moves)  
		
		if nextMove == -1:
			return random.choice(self.accepted) 
		else:
			return nextMove


	def result(self, play1, play2):
		if play1 == 'r' or play1 == 'R':
			if play2 == 'p' or play2 == 'P':
				return 2
			if play2 == 's' or play2 == 'S':
				return 1

		if play1 == 'p' or play1 == 'P':
			if play2 == 's' or play2 == 'S':
				return 2
			if play2 == 'r' or play2 == 'R':
				return 1

		if play1 == 's' or play1 == 'S':
			if play2 == 'r' or play2 == 'R':
				return 2
			if play2 == 'p' or play2 == 'P':
				return 1
			
	def printScore(self):
		print 'HUMAN vs COMPUTER'
		print '    ' + str(self.humanScore) + '    ' + str(self.computerScore) 
