import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calorie and BMI Calculator")

        # Gender
        self.gender_label = ttk.Label(root, text="Gender:")
        self.gender_label.grid(column=0, row=0, padx=10, pady=10)
        self.gender_var = tk.StringVar()
        self.gender_dropdown = ttk.Combobox(root, textvariable=self.gender_var)
        self.gender_dropdown['values'] = ("Male", "Female")
        self.gender_dropdown.grid(column=1, row=0, padx=10, pady=10)

        # Age
        self.age_label = ttk.Label(root, text="Age (years):")
        self.age_label.grid(column=0, row=1, padx=10, pady=10)
        self.age_entry = ttk.Entry(root)
        self.age_entry.grid(column=1, row=1, padx=10, pady=10)

        # Height
        self.height_label = ttk.Label(root, text="Height (cm):")
        self.height_label.grid(column=0, row=2, padx=10, pady=10)
        self.height_entry = ttk.Entry(root)
        self.height_entry.grid(column=1, row=2, padx=10, pady=10)

        # Weight
        self.weight_label = ttk.Label(root, text="Weight (kg):")
        self.weight_label.grid(column=0, row=3, padx=10, pady=10)
        self.weight_entry = ttk.Entry(root)
        self.weight_entry.grid(column=1, row=3, padx=10, pady=10)

        # Activity level
        self.activity_label = ttk.Label(root, text="Activity Level:")
        self.activity_label.grid(column=0, row=4, padx=10, pady=10)
        self.activity_var = tk.StringVar()
        self.activity_dropdown = ttk.Combobox(root, textvariable=self.activity_var)
        self.activity_dropdown['values'] = (
            "Sedentary (little or no exercise)",
            "Lightly active (light exercise/sports 1-3 days/week)",
            "Moderately active (moderate exercise/sports 3-5 days/week)",
            "Very active (hard exercise/sports 6-7 days a week)",
            "Super active (very hard exercise/sports and a physical job)"
        )
        self.activity_dropdown.grid(column=1, row=4, padx=10, pady=10)

        # Calculate Buttons
        self.bmi_button = ttk.Button(root, text="Calculate BMI", command=self.calculate_bmi)
        self.bmi_button.grid(column=0, row=5, padx=10, pady=10)

        self.calorie_button = ttk.Button(root, text="Calculate Calories", command=self.calculate_calories)
        self.calorie_button.grid(column=1, row=5, padx=10, pady=10)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get()) / 100  # Convert cm to meters
            bmi = weight / (height ** 2)
            messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for height and weight.")

    def calculate_calories(self):
        try:
            gender = self.gender_var.get()
            age = int(self.age_entry.get())
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            activity_level = self.activity_var.get()

            if gender not in ["Male", "Female"]:
                raise ValueError("Invalid gender")

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
                raise ValueError("Invalid activity level")

            if gender == "Male":
                bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
            else:  # Female
                bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

            calories = bmr * activity_factor
            messagebox.showinfo("Calorie Result", f"Your daily calorie needs are: {calories:.2f} kcal")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please ensure all fields are filled out correctly and are valid numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
