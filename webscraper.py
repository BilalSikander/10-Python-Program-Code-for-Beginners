import tkinter as tk
from tkinter import scrolledtext
import requests
from bs4 import BeautifulSoup

# Function to scrape headlines from a given URL
def scrape_headlines():
    url = url_entry.get()
    if not url:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please enter a URL.")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Clear previous results
        result_text.delete(1.0, tk.END)
        
        # Find all headlines (this part may vary depending on the website structure)
        headlines = soup.find_all(['h1', 'h2', 'h3'])
        if not headlines:
            result_text.insert(tk.END, "No headlines found.")
            return
        
        # Display the headlines
        for headline in headlines:
            result_text.insert(tk.END, f"{headline.get_text(strip=True)}\n\n")
    
    except requests.RequestException as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Simple Web Scraper")

# Create and place the URL entry
url_label = tk.Label(root, text="Enter URL:", font=('Arial', 14))
url_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

url_entry = tk.Entry(root, width=50, font=('Arial', 14))
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place the scrape button
scrape_button = tk.Button(root, text="Scrape Headlines", font=('Arial', 14), command=scrape_headlines)
scrape_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create and place the scrolled text area to display results
result_text = scrolledtext.ScrolledText(root, width=80, height=20, font=('Arial', 12))
result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()
