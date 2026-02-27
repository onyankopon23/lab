import unittest
from src.lab2.caesar import encrypt_caesar, decrypt_caesar

class CaesarTestCase(unittest.TestCase):
    def test_examples_from_statement(self):
        self.assertEqual(encrypt_caesar("PYTHON"), "SBWKRQ")
        self.assertEqual(encrypt_caesar("python"), "sbwkrq")
        self.assertEqual(encrypt_caesar("Python3.6"), "Sbwkrq3.6")
        self.assertEqual(encrypt_caesar(""), "")

        self.assertEqual(decrypt_caesar("SBWKRQ"), "PYTHON")
        self.assertEqual(decrypt_caesar("sbwkrq"), "python")
        self.assertEqual(decrypt_caesar("Sbwkrq3.6"), "Python3.6")
        self.assertEqual(decrypt_caesar(""), "")

    def test_round(self):
        self.assertEqual(encrypt_caesar("XYZ", shift=3), "ABC")
        self.assertEqual(encrypt_caesar("xyz", shift=3), "abc")

        self.assertEqual(decrypt_caesar("ABC", shift=3), "XYZ")
        self.assertEqual(decrypt_caesar("abc", shift=3), "xyz")

    def test_shift_zero(self):
        self.assertEqual(encrypt_caesar("AbZz", shift=0), "AbZz")

        self.assertEqual(decrypt_caesar("AbZz", shift=0), "AbZz")

    def test_non_letters(self):
        self.assertEqual(encrypt_caesar("cr7 < messi_10 !!!!", shift=5),"hw7 < rjxxn_10 !!!!")
        self.assertEqual(encrypt_caesar("67???!", shift=5),"67???!" )

        self.assertEqual(decrypt_caesar("hw7 < rjxxn_10 !!!!", shift=5),"cr7 < messi_10 !!!!")
        self.assertEqual(decrypt_caesar("67???!", shift=5),"67???!")
