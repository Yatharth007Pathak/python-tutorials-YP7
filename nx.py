"""
tkinter is the standard Python interface to the Tk GUI toolkit. 
It provides a set of tools to create graphical user interfaces (GUIs) for Python applications. 
tkinter is included with Python, so you don't need to install it separately.

Key Features of tkinter:
Widgets: Provides various widgets such as buttons, labels, text boxes, and menus to build your GUI.
Layout Management: Offers different geometry managers (pack, grid, place) for arranging widgets.
Event Handling: Supports event-driven programming with event binding and callbacks.
Customization: Allows customization of widget appearance and behavior.
"""

# Creating a Simple Window using tkinter:

import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Simple Tkinter Window")
root.geometry("400x300")  # Width x Height

# Run the application
root.mainloop()
