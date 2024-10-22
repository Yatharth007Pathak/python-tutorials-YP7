"""
pygame is a Python library used for creating video games and multimedia applications. It provides functionalities for handling graphics, 
sound, and input, making it a popular choice for game development and other interactive applications.

Key Features of pygame:
Graphics: Draw shapes, display images, and handle various graphical operations.
Sound: Play sounds and music using built-in functions.
Input Handling: Capture and respond to keyboard, mouse, and joystick inputs.
Game Loop: Easily create a game loop for handling continuous updates and rendering.
"""

# Creating a Simple Pygame Window and handling a simple event loop:

import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Pygame Window")

# Set the background color
background_color = (0, 0, 0)  # Black

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with the background color
    screen.fill(background_color)

    # Update the display
    pygame.display.flip()
