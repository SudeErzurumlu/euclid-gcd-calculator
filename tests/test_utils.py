# tests/test_utils.py
import unittest
from euclid_gcd.utils import validate_input

class TestUtils(unittest.TestCase):

    def test_valid_input(self):
        self.assertTrue(validate_input(48, 18))  # Valid input test

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            validate_input("48", 18)  # Invalid type
        with self.assertRaises(ValueError):
            validate_input(-48, 18)  # Negative number
