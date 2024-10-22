# Handling user interactions like button clicks:

import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create the main application window
root = tk.Tk()
root.title("Handling Events")

# Create a label widget
label = tk.Label(root, text="Click the Button")
label.pack()

# Create a button widget and bind it to the event handler
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# Run the application
root.mainloop()