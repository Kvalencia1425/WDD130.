import unittest
from caloriecalcu import CalculatorApp

class TestCalculatorApp(unittest.TestCase):

    def setUp(self):
        self.app = CalculatorApp(None)

    def test_calculate_bmi(self):
        self.assertEqual(self.app.calculate_bmi_value(70, 170), 24.22)
        self.assertEqual(self.app.calculate_bmi_value(50, 150), 22.22)
        self.assertIsNone(self.app.calculate_bmi_value(70, 0))
        self.assertIsNone(self.app.calculate_bmi_value(0, 170))

    def test_calculate_calorie_needs(self):
        self.assertEqual(self.app.calculate_calorie_needs("Male", 25, 180, 75, "Sedentary (little or no exercise)"), 2016.62)
        self.assertEqual(self.app.calculate_calorie_needs("Female", 30, 160, 60, "Lightly active (light exercise/sports 1-3 days/week)"), 1942.01)
        self.assertIsNone(self.app.calculate_calorie_needs("Other", 25, 180, 75, "Sedentary (little or no exercise)"))
        self.assertIsNone(self.app.calculate_calorie_needs("Male", 25, 180, 75, "Invalid activity level"))

if __name__ == "__main__":
    unittest.main()
