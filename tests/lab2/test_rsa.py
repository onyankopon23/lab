import unittest
from src.lab2.rsa import is_prime, gcd, multiplicative_inverse, generate_keypair, encrypt, decrypt

class RsaCaseTest(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(8))

    def test_gcd(self):
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(3, 7), 1)

    def test_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)

    def test_generate_keypair(self):
        keys = generate_keypair(17, 19)
        self.assertEqual(keys[0][1], keys[1][1])
        self.assertEqual(keys[0][1], 17 * 19)

    def test_encrypt_decrypt(self):
        keys = generate_keypair(17, 19)

        message = "cr7 < messi!"
        encrypted = encrypt(keys[1], message)
        decrypted = decrypt(keys[0], encrypted)

        self.assertEqual(decrypted, message)

