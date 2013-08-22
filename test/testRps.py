import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src')

from rps import Rps

class TestRps(unittest.TestCase):

	def setUp(self):
		self.rps = Rps(3)

	def test_rps_player1_wins(self):
		result = self.rps.result('r', 's')
		self.assertEqual(result, 1)
		result = self.rps.result('s', 'p')
		self.assertEqual(result, 1)
		result = self.rps.result('p', 'r')
		self.assertEqual(result, 1)


	def test_rps_player2_wins(self):
		result = self.rps.result('s', 'r')
		self.assertEqual(result, 2)
		result = self.rps.result('p', 's')
		self.assertEqual(result, 2)
		result = self.rps.result('r', 'p')
		self.assertEqual(result, 2)

	def test_rps_random_decision(self):
		self.rps.moves = ['r', 's', 'r', 'p', 's']
		decision = self.rps.decision()
		self.assertTrue(decision in ['r', 'p', 's'])

	def test_rps_specific_decision(self):
		self.rps.moves = ['r', 's', 'p', 'r', 's', 'p', 'r', 's', 'p']
		decision = self.rps.decision()
		self.assertEquals(decision, 'r')

if __name__ == '__main__':
	unittest.main()