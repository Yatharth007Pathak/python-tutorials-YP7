# Drawing Shapes using pygame functions:

import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing Shapes")

# Set the colors
background_color = (255, 255, 255)  # White
circle_color = (255, 0, 0)  # Red
rectangle_color = (0, 255, 0)  # Green

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

    # Draw a circle
    pygame.draw.circle(screen, circle_color, (400, 300), 50)

    # Draw a rectangle
    pygame.draw.rect(screen, rectangle_color, pygame.Rect(100, 100, 200, 100))

    # Update the display
    pygame.display.flip()
