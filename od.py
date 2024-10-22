# Customizing Widgets by configuring their properties:

import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Customizing Widgets")

# Create a label with custom font and color
label = tk.Label(root, text="Customized Label", font=("Arial", 16), fg="blue")
label.pack()

# Create a button with custom background color
button = tk.Button(root, text="Customized Button", bg="green", fg="white")
button.pack()

# Run the application
root.mainloop()
