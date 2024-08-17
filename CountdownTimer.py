import tkinter as tk
from tkinter import messagebox
import time

# Function to start the countdown timer
def start_timer():
    try:
        minutes = int(minutes_entry.get())
        seconds = int(seconds_entry.get())
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter valid numbers for minutes and seconds.")
        return

    total_seconds = minutes * 60 + seconds
    countdown(total_seconds)

# Function to update the timer display and handle countdown
def countdown(total_seconds):
    if total_seconds <= 0:
        timer_label.config(text="00:00")
        messagebox.showinfo("Time's Up!", "The countdown has finished.")
        return

    minutes, seconds = divmod(total_seconds, 60)
    timer_label.config(text=f"{minutes:02}:{seconds:02}")
    
    # Update every second
    root.after(1000, countdown, total_seconds - 1)

# Create the main window
root = tk.Tk()
root.title("Countdown Timer")

# Create and place the minutes label and entry
minutes_label = tk.Label(root, text="Minutes:", font=('Arial', 14))
minutes_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

minutes_entry = tk.Entry(root, width=5, font=('Arial', 14))
minutes_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place the seconds label and entry
seconds_label = tk.Label(root, text="Seconds:", font=('Arial', 14))
seconds_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')

seconds_entry = tk.Entry(root, width=5, font=('Arial', 14))
seconds_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the start button
start_button = tk.Button(root, text="Start Timer", font=('Arial', 14), command=start_timer)
start_button.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

# Create and place the timer label
timer_label = tk.Label(root, text="00:00", font=('Arial', 48))
timer_label.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

# Run the main loop
root.mainloop()
