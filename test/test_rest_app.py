import unittest
from src.rest_app import SumOfAllNumbers

class TestSumOfAllNumbers(unittest.TestCase):

    def test_get(self):
        expected = {'total':[10000000]}
        self.assertEqual(SumOfAllNumbers.get(self),expected)