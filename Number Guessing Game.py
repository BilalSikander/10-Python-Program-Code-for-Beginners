import tkinter as tk
from tkinter import messagebox
import random

# Function to start a new game
def start_new_game():
    global number_to_guess, attempts_left
    number_to_guess = random.randint(1, 100)
    attempts_left = 10
    attempts_label.config(text=f"Attempts Left: {attempts_left}")
    guess_entry.delete(0, tk.END)
    guess_entry.config(state=tk.NORMAL)
    submit_button.config(state=tk.NORMAL)

# Function to check the user's guess
def check_guess():
    global attempts_left
    try:
        guess = int(guess_entry.get())
        if guess < 1 or guess > 100:
            messagebox.showwarning("Invalid Input", "Please enter a number between 1 and 100.")
            return
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number.")
        return

    attempts_left -= 1
    attempts_label.config(text=f"Attempts Left: {attempts_left}")

    if guess < number_to_guess:
        result_label.config(text="Too low! Try again.")
    elif guess > number_to_guess:
        result_label.config(text="Too high! Try again.")
    else:
        result_label.config(text=f"Congratulations! You guessed it right. The number was {number_to_guess}.")
        guess_entry.config(state=tk.DISABLED)
        submit_button.config(state=tk.DISABLED)
        return

    if attempts_left == 0:
        result_label.config(text=f"Game Over! The number was {number_to_guess}.")
        guess_entry.config(state=tk.DISABLED)
        submit_button.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Set up the instructions label
instructions_label = tk.Label(root, text="Guess the number between 1 and 100:", font=('Arial', 14))
instructions_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Set up the entry field for the user's guess
guess_entry = tk.Entry(root, font=('Arial', 14))
guess_entry.grid(row=1, column=0, padx=10, pady=10)

# Set up the submit button
submit_button = tk.Button(root, text="Submit Guess", font=('Arial', 14), command=check_guess)
submit_button.grid(row=1, column=1, padx=10, pady=10)

# Set up the attempts label
attempts_label = tk.Label(root, text="Attempts Left: 10", font=('Arial', 14))
attempts_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Set up the result label
result_label = tk.Label(root, text="", font=('Arial', 14))
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Set up the new game button
new_game_button = tk.Button(root, text="New Game", font=('Arial', 14), command=start_new_game)
new_game_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the first game
start_new_game()

# Run the main loop
root.mainloop()
