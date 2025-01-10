import unittest
from Palindrome import is_palindrome

class PalindromeTest(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("a"))  # Single character
        self.assertTrue(is_palindrome("aa"))
        self.assertTrue(is_palindrome("a b a"))
        self.assertTrue(is_palindrome("An Na"))
        self.assertTrue(is_palindrome(" "))  # Single space
        self.assertTrue(is_palindrome(""))  # Empty string
        self.assertTrue(is_palindrome("Able was I saw Elba"))
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("abc@cba"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("ab"))
        self.assertFalse(is_palindrome("a b"))
        self.assertFalse(is_palindrome("A man"))
        self.assertFalse(is_palindrome("A man a plan a canal Panama")) # Complex string
        self.assertFalse(is_palindrome("12345"))
        self.assertFalse(is_palindrome("hello@world"))

if __name__ == "__main__":
    unittest.main()