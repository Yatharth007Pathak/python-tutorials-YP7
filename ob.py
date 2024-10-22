#Grid: Organizes widgets in a table-like structure.

import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Grid Layout")

# Create widgets and place them in the grid
tk.Label(root, text="Name:").grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)
tk.Button(root, text="Submit").grid(row=1, columnspan=2)

# Run the application
root.mainloop()