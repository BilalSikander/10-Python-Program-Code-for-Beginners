import tkinter as tk

# Function to update the expression in the entry field
def update_expression(value):
    current_expression = expression.get()
    expression.set(current_expression + str(value))

# Function to evaluate the final expression
def calculate(event=None):
    try:
        result = eval(expression.get())
        expression.set(result)
    except Exception as e:
        expression.set("Error")

# Function to clear the entry field
def clear(event=None):
    expression.set("")

# Function to handle key presses
def key_pressed(event):
    if event.char.isdigit() or event.char in '+-*/.':
        update_expression(event.char)
    elif event.keysym == 'Return':
        calculate()
    elif event.keysym == 'BackSpace':
        clear()

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Set up the entry field
expression = tk.StringVar()
entry = tk.Entry(root, textvariable=expression, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Bind key presses
root.bind('<Key>', key_pressed)

# Define the buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create and position buttons
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, bd=8, font=('Arial', 18),
                           command=calculate)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, bd=8, font=('Arial', 18),
                           command=lambda t=text: update_expression(t))
    button.grid(row=row, column=col)

# Clear button
clear_button = tk.Button(root, text='C', padx=20, pady=20, bd=8, font=('Arial', 18),
                         command=clear)
clear_button.grid(row=5, column=0, columnspan=4)

# Run the main loop
root.mainloop()
