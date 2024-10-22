# Place: Positions widgets at a specific location.

import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Place Layout")

# Create widgets and place them at specific coordinates
tk.Label(root, text="Label").place(x=50, y=50)
tk.Button(root, text="Button").place(x=100, y=100)

# Run the application
root.mainloop()