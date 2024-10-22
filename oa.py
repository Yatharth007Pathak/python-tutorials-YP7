# Layout Management: tkinter provides three geometry managers to arrange widgets: pack, grid, and place.

# Pack: Packs widgets into the window in a top-to-bottom manner.

import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Pack Layout")

# Create widgets and pack them
tk.Label(root, text="Label 1").pack(side=tk.TOP)
tk.Button(root, text="Button 1").pack(side=tk.LEFT)
tk.Entry(root).pack(side=tk.BOTTOM)

# Run the application
root.mainloop()