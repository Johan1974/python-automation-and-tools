import unittest
from band_name_generator import generate_band_name

class TestBandNameGenerator(unittest.TestCase):

    def test_basic_combination(self):
        self.assertEqual(generate_band_name("Utrecht", "Tony"), "Utrecht Tony")

    def test_handles_whitespace(self):
        self.assertEqual(generate_band_name("  Paris  ", "  Luna  "), "Paris Luna")

    def test_empty_input(self):
        self.assertEqual(generate_band_name("", ""), " ")

if __name__ == "__main__":
    unittest.main()
