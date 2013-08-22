import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src')

import ngram

class TestNgram(unittest.TestCase):

	def test_ngram_negative_n(self):
		with self.assertRaises(Exception):
			ng = ngram.Ngram(-1)

	def test_ngram_not_integer(self):
		with self.assertRaises(Exception):
			ng = ngram.Ngram(1.2)
		with self.assertRaises(Exception):
			ng = ngram.Ngram('3')
	
	def setUp(self):
		self.ngram = ngram.Ngram(3)

	def test_ngram_length_less_than_n(self):
		testList = [1, 2]
		next = self.ngram.getNext(testList)
		self.assertEqual(next, -1)

	def test_ngram_no_available_choice(self):
		testList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		next = self.ngram.getNext(testList)
		self.assertEqual(next, -1)

	def test_ngram_return_a_value(self):
		testList = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3]
		next = self.ngram.getNext(testList)
		self.assertEqual(next, 4)

if __name__ == '__main__':
	unittest.main()