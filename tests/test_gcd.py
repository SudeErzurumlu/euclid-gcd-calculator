import unittest
from euclid_gcd.gcd import euclid_gcd

class TestEuclidGCD(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(euclid_gcd(48, 18), 6)
        self.assertEqual(euclid_gcd(54, 24), 6)
        self.assertEqual(euclid_gcd(101, 103), 1)  # Asal sayılar

    def test_zero(self):
        self.assertEqual(euclid_gcd(0, 0), 0)  # GCD(0, 0) özel bir durum
        self.assertEqual(euclid_gcd(0, 10), 10)
        self.assertEqual(euclid_gcd(10, 0), 10)

    def test_negative_numbers(self):
        self.assertEqual(euclid_gcd(-48, 18), 6)
        self.assertEqual(euclid_gcd(48, -18), 6)
        self.assertEqual(euclid_gcd(-48, -18), 6)

    def test_same_numbers(self):
        self.assertEqual(euclid_gcd(20, 20), 20)

if __name__ == '__main__':
    unittest.main()
