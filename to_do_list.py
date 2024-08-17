import tkinter as tk
from tkinter import messagebox

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to remove the selected task
def remove_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to clear all tasks
def clear_tasks():
    tasks_listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Set up the task entry field and the add button
task_entry = tk.Entry(root, width=35, font=('Arial', 14))
task_entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(root, text="Add Task", width=10, font=('Arial', 14), command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

# Set up the listbox to display tasks
tasks_listbox = tk.Listbox(root, height=10, width=50, font=('Arial', 14), selectmode=tk.SINGLE)
tasks_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Set up the remove button
remove_button = tk.Button(root, text="Remove Task", width=12, font=('Arial', 14), command=remove_task)
remove_button.grid(row=2, column=0, padx=10, pady=10)

# Set up the clear button
clear_button = tk.Button(root, text="Clear Tasks", width=12, font=('Arial', 14), command=clear_tasks)
clear_button.grid(row=2, column=1, padx=10, pady=10)

# Run the main loop
root.mainloop()
