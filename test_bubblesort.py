import unittest
from bubblesort import bubblesort

class TestBubblesort(unittest.TestCase):

    def test_bubblesort_range(self):
        test_input = [0, 1, 2, 3, 4, 5]
        expected_output = [0, 1, 2, 3, 4, 5]
        self.assertEqual(bubblesort(test_input), expected_output)

    def test_bubblesort_reverse_range(self):
        test_input = [5, 4, 3, 2, 1, 0]
        expected_output = [0, 1, 2, 3, 4, 5]
        self.assertEqual(bubblesort(test_input), expected_output)
