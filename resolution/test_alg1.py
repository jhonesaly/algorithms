import unittest
from alg1 import count_vog_con


class TestCountVogCon(unittest.TestCase):

    def test_function_vowels_only(self):
        test_input = 'aeiouAEIOU'
        expected_output = (10, 0)
        self.assertEqual(count_vog_con(test_input), expected_output)

    def test_function_consoants_only(self):
        test_input = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
        expected_output = (0, 42)
        self.assertEqual(count_vog_con(test_input), expected_output)

    def test_function_mixed_characters(self):
        test_input = 'Hello, world!!!'
        expected_output = (3, 7)
        self.assertEqual(count_vog_con(test_input), expected_output)
