import unittest
from euclid_gcd.gcd import euclid_gcd

class TestEuclidGCD(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(euclid_gcd(48, 18), 6)  # Testing GCD of two positive numbers
        self.assertEqual(euclid_gcd(54, 24), 6)  # Another positive pair
        self.assertEqual(euclid_gcd(101, 103), 1)  # Testing with prime numbers

    def test_zero(self):
        self.assertEqual(euclid_gcd(0, 0), 0)  # Special case: GCD(0, 0)
        self.assertEqual(euclid_gcd(0, 10), 10)  # GCD of zero and a positive number
        self.assertEqual(euclid_gcd(10, 0), 10)  # GCD of a positive number and zero

    def test_negative_numbers(self):
        self.assertEqual(euclid_gcd(-48, 18), 6)  # GCD with a negative number
        self.assertEqual(euclid_gcd(48, -18), 6)  # Another case with negative
        self.assertEqual(euclid_gcd(-48, -18), 6)  # GCD of two negative numbers

    def test_same_numbers(self):
        self.assertEqual(euclid_gcd(20, 20), 20)  # GCD of two identical numbers

if __name__ == '__main__':
    unittest.main()
