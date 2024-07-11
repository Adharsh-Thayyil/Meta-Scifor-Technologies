import unittest

def is_palindrome(string):
    return string == string[::-1]
class TestPalindrome(unittest.TestCase):
    def test_palindrome_string(self):
        palindrome = "amma"
        print("Test Palindrome:",palindrome)
        self.assertTrue(is_palindrome(palindrome),"String is not Palindrome")

    def test_non_palindrome_string(self):
        non_palindrome = "amma"
        print("Test Non Palindrome:",non_palindrome)
        self.assertFalse(is_palindrome(non_palindrome),"String is a Palindrome")

if __name__ == '__name__':
    unittest.main()