import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password
def generate_password():
    length = int(length_entry.get())
    
    if length <= 0:
        messagebox.showwarning("Invalid Length", "Password length must be greater than 0.")
        return

    # Collect character types based on user selection
    characters = ""
    if lowercase_var.get():
        characters += string.ascii_lowercase
    if uppercase_var.get():
        characters += string.ascii_uppercase
    if digits_var.get():
        characters += string.digits
    if special_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("No Characters Selected", "Please select at least one character type.")
        return

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Display the password
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place the length label and entry
length_label = tk.Label(root, text="Password Length:", font=('Arial', 14))
length_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

length_entry = tk.Entry(root, width=10, font=('Arial', 14))
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place the checkbuttons for character types
lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

lowercase_cb = tk.Checkbutton(root, text="Include Lowercase", variable=lowercase_var, font=('Arial', 12))
lowercase_cb.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky='w')

uppercase_cb = tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var, font=('Arial', 12))
uppercase_cb.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky='w')

digits_cb = tk.Checkbutton(root, text="Include Digits", variable=digits_var, font=('Arial', 12))
digits_cb.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky='w')

special_cb = tk.Checkbutton(root, text="Include Special Characters", variable=special_var, font=('Arial', 12))
special_cb.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky='w')

# Create and place the generate button
generate_button = tk.Button(root, text="Generate Password", font=('Arial', 14), command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=20)

# Create and place the result entry
result_label = tk.Label(root, text="Generated Password:", font=('Arial', 14))
result_label.grid(row=6, column=0, padx=10, pady=10, sticky='e')

result_entry = tk.Entry(root, width=50, font=('Arial', 14))
result_entry.grid(row=6, column=1, padx=10, pady=10)

# Run the main loop
root.mainloop()
