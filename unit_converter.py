#WEEK 7 - UNIT CONVERTER - KURT VALENCIA

import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry, FloatEntry


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Unit Converter")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create labels for the converter category
    lbl_category = Label(frm_main, text="Please select conversion category")
    btn_length = Button(frm_main, text="1. Length Converter")
    btn_temp = Button(frm_main, text="2. Temperature Converter")
    btn_weight = Button(frm_main, text="3. Weight Converter")
    btn_volume = Button(frm_main, text="4. Volume Converter")
   

    lbl_category.grid(      row=0, column=0, padx=3, pady=2)
    btn_length.grid(      row=1, column=0, padx=3, pady=2)
    btn_temp.grid(     row=2, column=0, padx=3, pady=2)
    btn_weight.grid(      row=3, column=0, padx=3, pady=2)
    btn_volume.grid(      row=4, column=0, padx=3, pady=2)

    def populate_length_window():

        length_window = tk.Toplevel()
        length_window.title("Length Converter")

        # Populate the window with labels, buttons, etc.
        lbl_category = Label(length_window, text="You may select unit  conversion")
        btn_m_to_km = Button(length_window, text="1. Meter to Kilometer")
        btn_m_to_ft = Button(length_window, text="2. Meter to Feet")
        btn_cm_to_in = Button(length_window, text="3. Centimeter to Inches")

        # Grid the widgets in the window
        lbl_category.grid(row=0, column=0, padx=3, pady=2)
        btn_m_to_km.grid(row=1, column=0, padx=3, pady=2)
        btn_m_to_ft.grid(row=2, column=0, padx=3, pady=2)
        btn_cm_to_in.grid(row=3, column=0, padx=3, pady=2)

        #window that converts m to km
        def populate_meter_to_kilometer_window():

                meter_to_kilometer_window = tk.Toplevel()
                meter_to_kilometer_window.title("Convert Meter to Kilometer")

                lbl_measurement = Label(meter_to_kilometer_window, text="Please enter length in meters:")
                ent_measurement = FloatEntry(meter_to_kilometer_window, width=5, lower_bound=1, upper_bound=9999)
                lbl_km = Label(meter_to_kilometer_window, text="M to KM:")
                txt_km = Label(meter_to_kilometer_window, width=5, anchor="e")
                lbl_km_units = Label(meter_to_kilometer_window, text="kilometers")
                btn_clear = Button(meter_to_kilometer_window ,text="Clear")

                lbl_measurement.grid(      row=0, column=0, padx=3, pady=2, sticky="e")
                ent_measurement.grid(      row=0, column=1, padx=3, pady=2, sticky="w")

                lbl_km.grid(   row=3, column=0, padx=3, pady=2, sticky="e")
                txt_km.grid(   row=3, column=1, padx=3, pady=2, sticky="w")
                lbl_km_units.grid(row=3, column=2, padx=0, pady=2, sticky="w")
                btn_clear.grid(    row=4, column=3, padx=3, pady=2)

                def clear():
                    """Clear all the inputs and outputs."""
                    btn_clear.focus()
                    ent_measurement.clear()
                    txt_km.config(text="")
                    ent_measurement.focus()

                def calculate(event):

                    try:
                        # Get the user input.
                        length = ent_measurement.get()

                        # Compute 
                        km = convert_meter_to_km(length)

                        txt_km.config(text=f"{km:.2f}")

                    except ValueError:
                        # When the user deletes all the digits in one
                        # of the number entries, clear the result.
                        txt_km.config(text="")   
                            
                ent_measurement.bind("<KeyRelease>", calculate)
                btn_clear.config(command=clear)
                ent_measurement.focus()
                meter_to_kilometer_window.mainloop()

        #Window convert M to Ft
        def populate_m_to_ft_window():

            m_to_ft_window = tk.Toplevel()
            m_to_ft_window.title("Convert Meter to Feet")

            lbl_measurement = Label(m_to_ft_window, text="Please enter length in meters:")
            ent_measurement = FloatEntry(m_to_ft_window, width=5, lower_bound=1, upper_bound=9999)
            lbl_ft = Label(m_to_ft_window, text="M to FT:")
            txt_ft = Label(m_to_ft_window, width=5, anchor="e")
            lbl_ft_units = Label(m_to_ft_window, text="ft")
            btn_clear = Button(m_to_ft_window ,text="Clear")

            lbl_measurement.grid(      row=0, column=0, padx=3, pady=2, sticky="e")
            ent_measurement.grid(      row=0, column=1, padx=3, pady=2, sticky="w")

            lbl_ft.grid(   row=3, column=0, padx=3, pady=2, sticky="e")
            txt_ft.grid(   row=3, column=1, padx=3, pady=2, sticky="w")
            lbl_ft_units.grid(row=3, column=2, padx=0, pady=2, sticky="w")
            btn_clear.grid(    row=4, column=3, padx=3, pady=2)

            def clear():
                """Clear all the inputs and outputs."""
                btn_clear.focus()
                ent_measurement.clear()
                txt_ft.config(text="")
                ent_measurement.focus()

            def calculate_m_to_ft(event):

                try:
                    # Get the user input.
                    length = ent_measurement.get()

                    # Compute 
                    ft = convert_meter_to_ft(length)

                    txt_ft.config(text=f"{ft:.2f}")

                except ValueError:
                    # When the user deletes all the digits in one
                    # of the number entries, clear the result.
                    txt_ft.config(text="")   
                        
            ent_measurement.bind("<KeyRelease>", calculate_m_to_ft)
            btn_clear.config(command=clear)
            ent_measurement.focus()

            m_to_ft_window.mainloop()

        #Window Convert CM to Inches
        def populate_cm_to_inch_window():

            cm_to_inch_window = tk.Toplevel()
            cm_to_inch_window.title("Convert Centimeter to Inch")

            lbl_measurement = Label(cm_to_inch_window, text="Please enter length in centimeters:")
            ent_measurement = FloatEntry(cm_to_inch_window, width=5, lower_bound=1, upper_bound=9999)
            lbl_inch = Label(cm_to_inch_window, text="CM to IN:")
            txt_inch = Label(cm_to_inch_window, width=5, anchor="e")
            lbl_inch_units = Label(cm_to_inch_window, text="inches")
            btn_clear = Button(cm_to_inch_window,text="Clear")

            lbl_measurement.grid(      row=0, column=0, padx=3, pady=2, sticky="e")
            ent_measurement.grid(      row=0, column=1, padx=3, pady=2, sticky="w")

            lbl_inch.grid(   row=3, column=0, padx=3, pady=2, sticky="e")
            txt_inch.grid(   row=3, column=1, padx=3, pady=2, sticky="w")
            lbl_inch_units.grid(row=3, column=2, padx=0, pady=2, sticky="w")
            btn_clear.grid(    row=4, column=3, padx=3, pady=2)

            def clear():
                """Clear all the inputs and outputs."""
                btn_clear.focus()
                ent_measurement.clear()
                txt_inch.config(text="")
                ent_measurement.focus()

            def calculate(event):

                try:
                    # Get the user input.
                    length = ent_measurement.get()

                    # Compute 
                    inch = convert_cm_to_in(length)

                    txt_inch.config(text=f"{inch:.2f}")

                except ValueError:
                    # When the user deletes all the digits in one
                    # of the number entries, clear the result.
                    txt_inch.config(text="")   
                        
            ent_measurement.bind("<KeyRelease>", calculate)
            btn_clear.config(command=clear)
            ent_measurement.focus()

            cm_to_inch_window.mainloop()

        btn_m_to_km.config(command=populate_meter_to_kilometer_window)
        btn_m_to_ft.config(command=populate_m_to_ft_window)
        btn_cm_to_in.config(command=populate_cm_to_inch_window)

        length_window.mainloop()

   # Temperature converter     
    def populate_temp_window():

        temp_window = tk.Toplevel()
        temp_window.title("Temperature Converter")

        # Populate the window with labels, buttons, etc.
        lbl_category = Label(temp_window, text="Please select unit conversion")
        btn_cel_to_fah = Button(temp_window, text="1. Celsius to Fahrenheit")
        btn_fah_to_cel = Button(temp_window, text="2. Fahrenheit to Celsius")

        # Grid the widgets in the window
        lbl_category.grid(row=0, column=0, padx=3, pady=2)
        btn_cel_to_fah.grid(row=1, column=0, padx=3, pady=2)
        btn_fah_to_cel.grid(row=2, column=0, padx=3, pady=2)

        #window convert celsius to fahrenheit
        def populate_celsius_to_fahrenheit_window():

            cel_to_fah_window = tk.Toplevel()
            cel_to_fah_window.title("Convert Celsius to Fahrenheit")

            lbl_measurement = Label(cel_to_fah_window, text="Please enter temperature in celsius °C:")
            ent_measurement = FloatEntry(cel_to_fah_window, width=5, lower_bound=1, upper_bound=9999)
            lbl_fah = Label(cel_to_fah_window, text="Celsius °C to Fahrenheit °F:")
            txt_fah = Label(cel_to_fah_window, width=5, anchor="e")
            lbl_fah_units = Label(cel_to_fah_window, text="°F")
            btn_clear = Button(cel_to_fah_window,text="Clear")

            lbl_measurement.grid(      row=0, column=0, padx=3, pady=2, sticky="e")
            ent_measurement.grid(      row=0, column=1, padx=3, pady=2, sticky="w")

            lbl_fah.grid(   row=3, column=0, padx=3, pady=2, sticky="e")
            txt_fah.grid(   row=3, column=1, padx=3, pady=2, sticky="w")
            lbl_fah_units.grid(row=3, column=2, padx=0, pady=2, sticky="w")
            btn_clear.grid(    row=4, column=3, padx=3, pady=2)

            def clear():
                """Clear all the inputs and outputs."""
                btn_clear.focus()
                ent_measurement.clear()
                txt_fah.config(text="")
                ent_measurement.focus()

            def calculate(event):

                try:
                    # Get the user input.
                    temp = ent_measurement.get()

                    # Compute 
                    fah = convert_celsius_to_fahrenheit(temp)

                    txt_fah.config(text=f"{fah:.2f}")

                except ValueError:
                    # When the user deletes all the digits in one
                    # of the number entries, clear the result.
                    txt_fah.config(text="")   
                        
            ent_measurement.bind("<KeyRelease>", calculate)
            btn_clear.config(command=clear)
            ent_measurement.focus()

            cel_to_fah_window.mainloop()
        
        #Window convert fahrenheit to celsius
        def populate_fah_to_cel_window():

            fah_to_cel_window = tk.Toplevel()
            fah_to_cel_window.title("Convert Farenheit to Celsius")

            lbl_measurement = Label(fah_to_cel_window, text="Please enter temperature in Fahrenheit °F:")
            ent_measurement = FloatEntry(fah_to_cel_window, width=5, lower_bound=1, upper_bound=9999)
            lbl_cel = Label(fah_to_cel_window, text="Fahrenheit °F to Celsius °C :")
            txt_cel = Label(fah_to_cel_window, width=5, anchor="e")
            lbl_cel_units = Label(fah_to_cel_window, text="°C")
            btn_clear = Button(fah_to_cel_window,text="Clear")

            lbl_measurement.grid(      row=0, column=0, padx=3, pady=2, sticky="e")
            ent_measurement.grid(      row=0, column=1, padx=3, pady=2, sticky="w")

            lbl_cel.grid(   row=3, column=0, padx=3, pady=2, sticky="e")
            txt_cel.grid(   row=3, column=1, padx=3, pady=2, sticky="w")
            lbl_cel_units.grid(row=3, column=2, padx=0, pady=2, sticky="w")
            btn_clear.grid(    row=4, column=3, padx=3, pady=2)

            def clear():
                """Clear all the inputs and outputs."""
                btn_clear.focus()
                ent_measurement.clear()
                txt_cel.config(text="")
                ent_measurement.focus()

            def calculate(event):

                try:
                    # Get the user input.
                    temp = ent_measurement.get()

                    # Compute 
                    cel = convert_fahrenheit_to_celsius(temp)

                    txt_cel.config(text=f"{cel:.2f}")

                except ValueError:
                    # When the user deletes all the digits in one
                    # of the number entries, clear the result.
                    txt_cel.config(text="")   
                        
            ent_measurement.bind("<KeyRelease>", calculate)
            btn_clear.config(command=clear)
            ent_measurement.focus()

            fah_to_cel_window.mainloop()

        btn_cel_to_fah.config(command=populate_celsius_to_fahrenheit_window)
        btn_fah_to_cel.config(command=populate_fah_to_cel_window)

        temp_window.mainloop()

    def populate_weight_window():

        weight_window = tk.Toplevel()
        weight_window.title("Weight Converter")

        # Populate the window with labels, buttons, etc.
        lbl_category = Label(weight_window, text="Please select unit conversion")
        btn_kg_to_lbs = Button(weight_window, text="1. Kilograms to Pounds")
        btn_lbs_to_kg = Button(weight_window, text="2. Pounds to Kilograms")

        # Grid the widgets in the window
        lbl_category.grid(row=0, column=0, padx=3, pady=2)
        btn_kg_to_lbs.grid(row=1, column=0, padx=3, pady=2)
        btn_lbs_to_kg.grid(row=2, column=0, padx=3, pady=2)


        def populate_kg_to_lbs_window():

            kg_to_lbs_window = tk.Toplevel()
            kg_to_lbs_window.title("Convert Kilogram to Pound")

            lbl_measurement = Label(kg_to_lbs_window, text="Please enter weight in kilogram")
            ent_measurement = FloatEntry(kg_to_lbs_window, width=5, lower_bound=1, upper_bound=9999)
            lbl_lbs = Label(kg_to_lbs_window, text="Kilogram to Pound:")
            txt_lbs = Label(kg_to_lbs_window, width=5, anchor="e")
            lbl_lbs_units = Label(kg_to_lbs_window, text="lbs")
            btn_clear = Button(kg_to_lbs_window,text="Clear")

            lbl_measurement.grid(      row=0, column=0, padx=3, pady=2, sticky="e")
            ent_measurement.grid(      row=0, column=1, padx=3, pady=2, sticky="w")

            lbl_lbs.grid(   row=3, column=0, padx=3, pady=2, sticky="e")
            txt_lbs.grid(   row=3, column=1, padx=3, pady=2, sticky="w")
            lbl_lbs_units.grid(row=3, column=2, padx=0, pady=2, sticky="w")
            btn_clear.grid(    row=4, column=3, padx=3, pady=2)

            def clear():
                """Clear all the inputs and outputs."""
                btn_clear.focus()
                ent_measurement.clear()
                txt_lbs.config(text="")
                ent_measurement.focus()

            def calculate(event):

                try:
                    # Get the user input.
                    weight = ent_measurement.get()

                    # Compute 
                    lbs = convert_kg_to_lbs(weight)

                    txt_lbs.config(text=f"{lbs:.2f}")

                except ValueError:
                    # When the user deletes all the digits in one
                    # of the number entries, clear the result.
                    txt_lbs.config(text="")   
                        
            ent_measurement.bind("<KeyRelease>", calculate)
            btn_clear.config(command=clear)
            ent_measurement.focus()

            kg_to_lbs_window.mainloop()

        btn_kg_to_lbs.config(command=populate_kg_to_lbs_window)
        btn_lbs_to_kg.config(command=populate_kg_to_lbs_window)

        def populate_lbs_to_kg_window():

            lbs_to_kg_window = tk.Toplevel()
            lbs_to_kg_window.title("Convert Pound to Kilogram")

            lbl_measurement = Label(lbs_to_kg_window, text="Please enter weight in pound:")
            ent_measurement = FloatEntry(lbs_to_kg_window, width=5, lower_bound=1, upper_bound=9999)
            lbl_kg = Label(lbs_to_kg_window, text="Kilogram to Pound:")
            txt_kg = Label(lbs_to_kg_window, width=5, anchor="e")
            lbl_kg_units = Label(lbs_to_kg_window, text="kg")
            btn_clear = Button(lbs_to_kg_window,text="Clear")

            lbl_measurement.grid(      row=0, column=0, padx=3, pady=2, sticky="e")
            ent_measurement.grid(      row=0, column=1, padx=3, pady=2, sticky="w")

            lbl_kg.grid(   row=3, column=0, padx=3, pady=2, sticky="e")
            txt_kg.grid(   row=3, column=1, padx=3, pady=2, sticky="w")
            lbl_kg_units.grid(row=3, column=2, padx=0, pady=2, sticky="w")
            btn_clear.grid(    row=4, column=3, padx=3, pady=2)

            def clear():
                """Clear all the inputs and outputs."""
                btn_clear.focus()
                ent_measurement.clear()
                txt_kg.config(text="")
                ent_measurement.focus()

            def calculate(event):

                try:
                    # Get the user input.
                    weight = ent_measurement.get()

                    # Compute 
                    kg = convert_lbs_to_kg(weight)

                    txt_kg.config(text=f"{kg:.2f}")

                except ValueError:
                    # When the user deletes all the digits in one
                    # of the number entries, clear the result.
                    txt_kg.config(text="")   
                        
            ent_measurement.bind("<KeyRelease>", calculate)
            btn_clear.config(command=clear)
            ent_measurement.focus()

            lbs_to_kg_window.mainloop()

        btn_kg_to_lbs.config(command=populate_kg_to_lbs_window)
        btn_lbs_to_kg.config(command=populate_lbs_to_kg_window)
        
       
        weight_window.mainloop()

    def populate_volume_window():

        volume_window = tk.Toplevel()
        volume_window.title("Volume Converter")

        # Populate the window with labels, buttons, etc.
        lbl_category = Label(volume_window, text="Please select unit conversion")
        btn_gal_to_lit = Button(volume_window, text="1. Gallon to Liter")
        btn_lit_to_gal = Button(volume_window, text="2. Liter to Gallon")

        # Grid the widgets in the window
        lbl_category.grid(row=0, column=0, padx=3, pady=2)
        btn_gal_to_lit.grid(row=1, column=0, padx=3, pady=2)
        btn_lit_to_gal.grid(row=2, column=0, padx=3, pady=2)


        def populate_gal_to_lit_window():

            gal_to_lit_window = tk.Toplevel()
            gal_to_lit_window.title("Convert Gallon to Liter")

            lbl_measurement = Label(gal_to_lit_window, text="Please enter volume in gallon")
            ent_measurement = FloatEntry(gal_to_lit_window, width=5, lower_bound=1, upper_bound=9999)
            lbl_lit = Label(gal_to_lit_window, text="Gallon to Liter:")
            txt_lit = Label(gal_to_lit_window, width=5, anchor="e")
            lbl_lit_units = Label(gal_to_lit_window, text="liter")
            btn_clear = Button(gal_to_lit_window,text="Clear")

            lbl_measurement.grid(      row=0, column=0, padx=3, pady=2, sticky="e")
            ent_measurement.grid(      row=0, column=1, padx=3, pady=2, sticky="w")

            lbl_lit.grid(   row=3, column=0, padx=3, pady=2, sticky="e")
            txt_lit.grid(   row=3, column=1, padx=3, pady=2, sticky="w")
            lbl_lit_units.grid(row=3, column=2, padx=0, pady=2, sticky="w")
            btn_clear.grid(    row=4, column=3, padx=3, pady=2)

            def clear():
                """Clear all the inputs and outputs."""
                btn_clear.focus()
                ent_measurement.clear()
                txt_lit.config(text="")
                ent_measurement.focus()

            def calculate(event):

                try:
                    # Get the user input.
                    volume = ent_measurement.get()

                    # Compute 
                    lit = convert_gallon_to_liter(volume)

                    txt_lit.config(text=f"{lit:.2f}")

                except ValueError:
                    # When the user deletes all the digits in one
                    # of the number entries, clear the result.
                    txt_lit.config(text="")   
                        
            ent_measurement.bind("<KeyRelease>", calculate)
            btn_clear.config(command=clear)
            ent_measurement.focus()

            gal_to_lit_window.mainloop()

        btn_gal_to_lit.config(command=populate_gal_to_lit_window)
        btn_lit_to_gal.config(command=populate_gal_to_lit_window)

        def populate_lit_to_gal_window():

            lit_to_gal_window = tk.Toplevel()
            lit_to_gal_window.title("Convert Gallon to Liter")

            lbl_measurement = Label(lit_to_gal_window, text="Please enter volume in liter:")
            ent_measurement = FloatEntry(lit_to_gal_window, width=5, lower_bound=1, upper_bound=9999)
            lbl_gal = Label(lit_to_gal_window, text="Liter to Gallon:")
            txt_gal = Label(lit_to_gal_window, width=5, anchor="e")
            lbl_gal_units = Label(lit_to_gal_window, text="gallon")
            btn_clear = Button(lit_to_gal_window,text="Clear")

            lbl_measurement.grid(      row=0, column=0, padx=3, pady=2, sticky="e")
            ent_measurement.grid(      row=0, column=1, padx=3, pady=2, sticky="w")

            lbl_gal.grid(   row=3, column=0, padx=3, pady=2, sticky="e")
            txt_gal.grid(   row=3, column=1, padx=3, pady=2, sticky="w")
            lbl_gal_units.grid(row=3, column=2, padx=0, pady=2, sticky="w")
            btn_clear.grid(    row=4, column=3, padx=3, pady=2)

            def clear():
                """Clear all the inputs and outputs."""
                btn_clear.focus()
                ent_measurement.clear()
                txt_gal.config(text="")
                ent_measurement.focus()

            def calculate(event):

                try:
                    # Get the user input.
                    volume = ent_measurement.get()

                    # Compute 
                    gal = convert_liter_to_gallon(volume)

                    txt_gal.config(text=f"{gal:.2f}")

                except ValueError:
                    # When the user deletes all the digits in one
                    # of the number entries, clear the result.
                    txt_gal.config(text="")   
                        
            ent_measurement.bind("<KeyRelease>", calculate)
            btn_clear.config(command=clear)
            ent_measurement.focus()

            lit_to_gal_window.mainloop()

        btn_gal_to_lit.config(command=populate_gal_to_lit_window)
        btn_lit_to_gal.config(command=populate_lit_to_gal_window)

        volume_window.mainloop()

    btn_length.config(command=populate_length_window)
    btn_temp.config(command=populate_temp_window)
    btn_weight.config(command=populate_weight_window)
    btn_volume.config(command=populate_volume_window)

#Functions that Converts the units
def convert_meter_to_km(meter):

    kilometers = meter/1000

    return kilometers

def convert_meter_to_ft(meter):

    ft = meter * 3.28084

    return ft

def convert_cm_to_in(centimeter):
    inches = centimeter / 2.54

    return inches

def convert_celsius_to_fahrenheit(celsius):

    fahrenheit = ((9/5) * celsius) + 32

    return fahrenheit

def convert_fahrenheit_to_celsius(fahrenheit): 

    celsius = (fahrenheit - 32 ) * 5/9

    return celsius

def convert_kg_to_lbs(weight):
    lbs = weight * 2.205

    return lbs

def convert_lbs_to_kg(weight):

    kg = weight / 2.205

    return kg

def convert_gallon_to_liter(volume):

    liter = volume * 3.785

    return liter

def convert_liter_to_gallon(volume):

    gallon = volume / 3.785

    return gallon

if __name__ == "__main__":
    main()
