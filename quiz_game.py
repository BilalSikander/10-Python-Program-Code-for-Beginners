import tkinter as tk
from tkinter import messagebox

# Sample questions for the quiz
questions = [
    {"question": "What is the capital of France?", "options": ["Berlin", "London", "Paris", "Rome"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
    {"question": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Shark", "Giraffe"], "answer": "Blue Whale"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"], "answer": "William Shakespeare"},
    {"question": "What is the square root of 64?", "options": ["6", "7", "8", "9"], "answer": "8"}
]

# Function to check the selected answer
def check_answer():
    global current_question_index, score
    selected_option = selected_var.get()
    correct_answer = questions[current_question_index]["answer"]

    if selected_option == correct_answer:
        score += 1
        messagebox.showinfo("Correct!", "Well done! That's the correct answer.")
    else:
        messagebox.showwarning("Incorrect", f"Sorry, the correct answer was: {correct_answer}")

    current_question_index += 1
    if current_question_index < len(questions):
        load_question()
    else:
        messagebox.showinfo("Quiz Finished", f"You've completed the quiz! Your score: {score}/{len(questions)}")
        root.quit()

# Function to load a question into the interface
def load_question():
    selected_var.set("")  # Ensure all radio buttons are unchecked
    question_text = questions[current_question_index]["question"]
    options = questions[current_question_index]["options"]

    question_label.config(text=question_text)
    for i in range(4):
        radio_buttons[i].config(text=options[i], value=options[i])

# Initialize the game
current_question_index = 0
score = 0

# Create the main window
root = tk.Tk()
root.title("Quiz Game")

# Create and place the question label
question_label = tk.Label(root, text="", font=('Arial', 16), wraplength=400, justify="center")
question_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

# Variable to hold the selected option
selected_var = tk.StringVar(value="")

# Create and place the radio buttons for options
radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=selected_var, value="", font=('Arial', 14))
    rb.grid(row=i+1, column=0, columnspan=2, padx=20, pady=5, sticky="w")
    radio_buttons.append(rb)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit Answer", font=('Arial', 14), command=check_answer)
submit_button.grid(row=5, column=0, columnspan=2, padx=20, pady=20)

# Load the first question
load_question()

# Run the main loop
root.mainloop()
