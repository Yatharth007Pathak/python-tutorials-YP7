# Handling keyboard and mouse inputs in the game loop:

import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Handling Input")

# Set the background color
background_color = (255, 255, 255)  # White

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the state of all keyboard keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        print("Left arrow key pressed")
    if keys[pygame.K_RIGHT]:
        print("Right arrow key pressed")

    # Get the position of the mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()
    print(f"Mouse position: ({mouse_x}, {mouse_y})")

    # Fill the screen with the background color
    screen.fill(background_color)

    # Update the display
    pygame.display.flip()