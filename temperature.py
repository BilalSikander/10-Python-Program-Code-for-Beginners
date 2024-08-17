import tkinter as tk
from tkinter import ttk

# Function to convert temperature
def convert_temperature():
    try:
        temp = float(entry.get())
        from_unit = from_var.get()
        to_unit = to_var.get()

        if from_unit == to_unit:
            result = temp
        elif from_unit == 'Celsius':
            if to_unit == 'Fahrenheit':
                result = (temp * 9/5) + 32
            elif to_unit == 'Kelvin':
                result = temp + 273.15
        elif from_unit == 'Fahrenheit':
            if to_unit == 'Celsius':
                result = (temp - 32) * 5/9
            elif to_unit == 'Kelvin':
                result = (temp - 32) * 5/9 + 273.15
        elif from_unit == 'Kelvin':
            if to_unit == 'Celsius':
                result = temp - 273.15
            elif to_unit == 'Fahrenheit':
                result = (temp - 273.15) * 9/5 + 32

        result_label.config(text=f"Result: {result:.2f} {to_unit}")
    except ValueError:
        result_label.config(text="Invalid input! Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create and place the widgets
entry_label = tk.Label(root, text="Enter Temperature:", font=('Arial', 14))
entry_label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root, font=('Arial', 14))
entry.grid(row=0, column=1, padx=10, pady=10)

from_var = tk.StringVar(value='Celsius')
to_var = tk.StringVar(value='Fahrenheit')

from_label = tk.Label(root, text="From:", font=('Arial', 14))
from_label.grid(row=1, column=0, padx=10, pady=10)

from_menu = ttk.Combobox(root, textvariable=from_var, values=['Celsius', 'Fahrenheit', 'Kelvin'], font=('Arial', 14), state='readonly')
from_menu.grid(row=1, column=1, padx=10, pady=10)

to_label = tk.Label(root, text="To:", font=('Arial', 14))
to_label.grid(row=2, column=0, padx=10, pady=10)

to_menu = ttk.Combobox(root, textvariable=to_var, values=['Celsius', 'Fahrenheit', 'Kelvin'], font=('Arial', 14), state='readonly')
to_menu.grid(row=2, column=1, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert", font=('Arial', 14), command=convert_temperature)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

result_label = tk.Label(root, text="Result:", font=('Arial', 14))
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()
