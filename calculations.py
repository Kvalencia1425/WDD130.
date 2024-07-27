# calculations.py

def calculate_bmi(weight, height):
    try:
        height = height / 100  # Convert cm to meters
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except:
        return None

def calculate_calorie_needs(gender, age, height, weight, activity_level):
    try:
        if gender not in ["Male", "Female"]:
            return None

        if activity_level == "Sedentary (little or no exercise)":
            activity_factor = 1.2
        elif activity_level == "Lightly active (light exercise/sports 1-3 days/week)":
            activity_factor = 1.375
        elif activity_level == "Moderately active (moderate exercise/sports 3-5 days/week)":
            activity_factor = 1.55
        elif activity_level == "Very active (hard exercise/sports 6-7 days a week)":
            activity_factor = 1.725
        elif activity_level == "Super active (very hard exercise/sports and a physical job)":
            activity_factor = 1.9
        else:
            return None

        if gender == "Male":
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else:  # Female
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

        calories = bmr * activity_factor
        return round(calories, 2)
    except:
        return None
