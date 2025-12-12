import unittest
from tip_calculator.calculator import calculate_tip

class TestTipCalculator(unittest.TestCase):

    def test_basic_calculation(self):
        total_tip, total_bill, per_person = calculate_tip(100, 15, 2)
        self.assertAlmostEqual(total_tip, 15)
        self.assertAlmostEqual(total_bill, 115)
        self.assertAlmostEqual(per_person, 57.5)

    def test_zero_tip(self):
        total_tip, total_bill, per_person = calculate_tip(200, 0, 4)
        self.assertAlmostEqual(total_tip, 0)
        self.assertAlmostEqual(total_bill, 200)
        self.assertAlmostEqual(per_person, 50)

    def test_one_person(self):
        total_tip, total_bill, per_person = calculate_tip(80, 10, 1)
        self.assertAlmostEqual(total_tip, 8)
        self.assertAlmostEqual(total_bill, 88)
        self.assertAlmostEqual(per_person, 88)

if __name__ == "__main__":
    unittest.main()
