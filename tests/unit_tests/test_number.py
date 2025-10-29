import unittest
from sandbox.number import Number

class TestNumber(unittest.TestCase):
    def test_number_decadic_default(self):
        my_number = Number("42")
        self.assertEqual(str(my_number), "42 base 10")
        self.assertEqual(my_number.get(), "42")

    def test_number_decadic_specified(self):
        my_number = Number("42", 10)
        self.assertEqual(str(my_number), "42 base 10")
        self.assertEqual(my_number.get(), "42")

# TODO
# Test with different bases (e.g., binary, octal, hexadecimal).
# Test with invalid base values (e.g., negative, zero, or unsupported bases).
# Test with invalid number strings for the given base.
# Test with very large numbers.
# Test with negative numbers (if supported).
# Test the behavior when no arguments are provided (if allowed).
# Test the string representation for various bases.
# Test the get() method for different input types and bases.
# Test equality and comparison if implemented.


if __name__ == "__main__":
    unittest.main()
