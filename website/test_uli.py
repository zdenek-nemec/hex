import unittest

from uli import Uli


class UliTest(unittest.TestCase):
    def test_empty_uli(self):
        uli = Uli("")
        self.assertEqual(False, uli.is_valid())

    def test_short_uli(self):
        for value in ["01", "01000000000"]:
            uli = Uli(value)
            self.assertEqual(False, uli.is_valid())

    def test_uli_type(self):
        test_cases = [
            ("010000000000", ["CGI"]),
            ("020000000000", ["SAI"]),
            ("030000000000", ["SAI", "CGI"]),
            ("040000000000", ["RAI"]),
            ("050000000000", ["RAI", "CGI"]),
            ("060000000000", ["RAI", "SAI"]),
            ("070000000000", ["RAI", "SAI", "CGI"]),
            ("080000000000", ["TAI"]),
            ("090000000000", ["TAI", "CGI"]),
            ("0A0000000000", ["TAI", "SAI"]),
            ("0B0000000000", ["TAI", "SAI", "CGI"]),
            ("0C0000000000", ["TAI", "RAI"]),
            ("0D0000000000", ["TAI", "RAI", "CGI"]),
            ("0E0000000000", ["TAI", "RAI", "SAI"]),
            ("0F0000000000", ["TAI", "RAI", "SAI", "CGI"]),
            ("110000000000", ["ECGI", "CGI"]),
            ("120000000000", ["ECGI", "SAI"]),
            ("130000000000", ["ECGI", "SAI", "CGI"]),
            ("140000000000", ["ECGI", "RAI"]),
            ("150000000000", ["ECGI", "RAI", "CGI"]),
            ("160000000000", ["ECGI", "RAI", "SAI"]),
            ("170000000000", ["ECGI", "RAI", "SAI", "CGI"]),
            ("180000000000", ["ECGI", "TAI"]),
            ("190000000000", ["ECGI", "TAI", "CGI"]),
            ("1A0000000000", ["ECGI", "TAI", "SAI"]),
            ("1B0000000000", ["ECGI", "TAI", "SAI", "CGI"]),
            ("1C0000000000", ["ECGI", "TAI", "RAI"]),
            ("1D0000000000", ["ECGI", "TAI", "RAI", "CGI"]),
            ("1E0000000000", ["ECGI", "TAI", "RAI", "SAI"]),
            ("1F0000000000", ["ECGI", "TAI", "RAI", "SAI", "CGI"])
        ]
        for value, expected_fields in test_cases:
            uli = Uli(value)
            self.assertEqual(sorted(expected_fields), sorted(uli._fields), f"{value}")


if __name__ == "__main__":
    unittest.main()
