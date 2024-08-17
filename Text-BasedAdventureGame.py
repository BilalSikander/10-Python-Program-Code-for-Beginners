import tkinter as tk
from tkinter import messagebox

# Game state variables
current_scene = None

# Scenes dictionary containing the game's story and choices
scenes = {
    'start': {
        'text': "You find yourself in a dark forest. There are two paths ahead: one to the left and one to the right.",
        'choices': {
            'Left': 'left_path',
            'Right': 'right_path'
        }
    },
    'left_path': {
        'text': "You walk down the left path and find a beautiful clearing with a mysterious old cabin.",
        'choices': {
            'Enter the cabin': 'cabin',
            'Return to the forest': 'start'
        }
    },
    'right_path': {
        'text': "You follow the right path and come across a raging river. There’s a boat on the shore.",
        'choices': {
            'Take the boat': 'boat',
            'Return to the forest': 'start'
        }
    },
    'cabin': {
        'text': "Inside the cabin, you find an ancient book. As you open it, the room starts to glow.",
        'choices': {
            'Read the book': 'book',
            'Leave the cabin': 'left_path'
        }
    },
    'boat': {
        'text': "You row across the river and reach a small island with a treasure chest.",
        'choices': {
            'Open the chest': 'treasure',
            'Return to the shore': 'right_path'
        }
    },
    'book': {
        'text': "The book reveals the secret to escaping the forest. You are free to leave the forest and live happily ever after!",
        'choices': {}
    },
    'treasure': {
        'text': "The chest contains gold and jewels. You are rich beyond your wildest dreams!",
        'choices': {}
    }
}

def display_scene(scene_key):
    global current_scene
    current_scene = scene_key
    scene = scenes[scene_key]

    # Update the text and choices
    text_var.set(scene['text'])
    for button, choice in zip(choice_buttons, scene['choices'].keys()):
        button.config(text=choice, command=lambda choice=choice: choose_option(scene['choices'][choice]))

    # Hide unused buttons
    for i in range(len(scene['choices']), len(choice_buttons)):
        choice_buttons[i].pack_forget()

def choose_option(next_scene):
    display_scene(next_scene)

# Create the main window
root = tk.Tk()
root.title("Text-Based Adventure Game")

# Create and place the text label
text_var = tk.StringVar()
text_var.set("Welcome to the Text-Based Adventure Game!")
text_label = tk.Label(root, textvariable=text_var, wraplength=400, font=('Arial', 14))
text_label.pack(padx=20, pady=20)

# Create and place the choice buttons
choice_buttons = []
for _ in range(4):
    button = tk.Button(root, text="", font=('Arial', 12), command=lambda: None)
    button.pack(pady=5, padx=20, fill='x')
    choice_buttons.append(button)

# Start the game
display_scene('start')

# Run the main loop
root.mainloop()
