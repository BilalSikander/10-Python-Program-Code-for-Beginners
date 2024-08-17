import tkinter as tk
from tkinter import messagebox, simpledialog

# Initialize the contact book as a dictionary
contacts = {}

# Function to add a new contact
def add_contact():
    name = simpledialog.askstring("Input", "Enter the contact's name:")
    if name:
        if name in contacts:
            messagebox.showwarning("Duplicate Entry", "This contact already exists.")
        else:
            phone = simpledialog.askstring("Input", f"Enter the phone number for {name}:")
            if phone:
                contacts[name] = phone
                listbox.insert(tk.END, name)
                messagebox.showinfo("Success", f"Contact {name} added successfully.")
            else:
                messagebox.showwarning("Input Error", "Phone number cannot be empty.")

# Function to delete a selected contact
def delete_contact():
    selected_contact = listbox.curselection()
    if selected_contact:
        name = listbox.get(selected_contact)
        confirmation = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete {name}?")
        if confirmation:
            listbox.delete(selected_contact)
            del contacts[name]
            messagebox.showinfo("Success", f"Contact {name} deleted successfully.")
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")

# Function to search for a contact
def search_contact():
    name = simpledialog.askstring("Search", "Enter the contact's name:")
    if name:
        if name in contacts:
            messagebox.showinfo("Search Result", f"{name}: {contacts[name]}")
        else:
            messagebox.showwarning("Not Found", "Contact not found.")
    else:
        messagebox.showwarning("Input Error", "Name cannot be empty.")

# Create the main window
root = tk.Tk()
root.title("Basic Contact Book")

# Create and place the buttons
add_button = tk.Button(root, text="Add Contact", width=20, font=('Arial', 14), command=add_contact)
add_button.grid(row=0, column=0, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Contact", width=20, font=('Arial', 14), command=delete_contact)
delete_button.grid(row=1, column=0, padx=10, pady=10)

search_button = tk.Button(root, text="Search Contact", width=20, font=('Arial', 14), command=search_contact)
search_button.grid(row=2, column=0, padx=10, pady=10)

# Create and place the listbox to display contacts
listbox = tk.Listbox(root, height=10, width=50, font=('Arial', 14))
listbox.grid(row=0, column=1, rowspan=3, padx=10, pady=10)

# Run the main loop
root.mainloop()
