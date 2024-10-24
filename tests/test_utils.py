import unittest
from euclid_gcd.utils import validate_input

class TestUtils(unittest.TestCase):

    def test_valid_input(self):
        self.assertTrue(validate_input(48, 18))
        self.assertTrue(validate_input(-10, 20))
        self.assertTrue(validate_input(0, 0))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            validate_input("48", 18)  # Geçersiz tip
        with self.assertRaises(ValueError):
            validate_input(48, None)  # None tipi
        with self.assertRaises(ValueError):
            validate_input(48, 18.5)  # Float tip kabul edilmez

if __name__ == '__main__':
    unittest.main()
