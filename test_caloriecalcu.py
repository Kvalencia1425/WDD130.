import unittest
import calculations

class TestCalculations(unittest.TestCase):

    def test_calculate_bmi(self):
        self.assertEqual(calculations.calculate_bmi(70, 170), 24.22)
        self.assertEqual(calculations.calculate_bmi(50, 150), 22.22)
        self.assertIsNone(calculations.calculate_bmi(70, 0))
        self.assertIsNone(calculations.calculate_bmi(0, 170))

    def test_calculate_calorie_needs(self):
        self.assertEqual(calculations.calculate_calorie_needs("Male", 25, 180, 75, "Sedentary (little or no exercise)"), 2016.62)
        self.assertEqual(calculations.calculate_calorie_needs("Female", 30, 160, 60, "Lightly active (light exercise/sports 1-3 days/week)"), 1942.01)
        self.assertIsNone(calculations.calculate_calorie_needs("Other", 25, 180, 75, "Sedentary (little or no exercise)"))
        self.assertIsNone(calculations.calculate_calorie_needs("Male", 25, 180, 75, "Invalid activity level"))

if __name__ == "__main__":
    unittest.main()
