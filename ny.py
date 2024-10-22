# Adding various widgets like labels, buttons, and text boxes to our window:

import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Adding Widgets")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Create a button widget
button = tk.Button(root, text="Click Me")
button.pack()

# Create an entry widget (text box)
entry = tk.Entry(root)
entry.pack()

# Run the application
root.mainloop()
