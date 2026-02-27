import unittest
from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere

class VigenreTestCase(unittest.TestCase):
    def test_examples_from_statement(self):
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(encrypt_vigenere("python", "a"), "python")
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")

        self.assertEqual(decrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(decrypt_vigenere("python", "a"), "python")
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")

    def test_round_keyword(self):
        self.assertEqual(encrypt_vigenere("AAAAAA", "B"), "BBBBBB")

        self.assertEqual(decrypt_vigenere("BBBBBB", "B"), "AAAAAA")

    def test_empty(self):
        self.assertEqual(encrypt_vigenere("", "LEMON"), "")

        self.assertEqual(decrypt_vigenere("", "LEMON"), "")

    def test_non_letters(self):
        self.assertEqual(encrypt_vigenere("cr7 < messi_10 !!!!", "KEY"),"mv7 < kowqs_10 !!!!")
        self.assertEqual(encrypt_vigenere("67???!", "KEY"),"67???!")

        self.assertEqual(decrypt_vigenere("mv7 < kowqs_10 !!!!", "KEY"),"cr7 < messi_10 !!!!")
        self.assertEqual(decrypt_vigenere("67???!", "KEY"),"67???!")
