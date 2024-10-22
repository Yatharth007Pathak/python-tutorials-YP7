# Moving a Rectangle with Keyboard Input:

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Moving a Rectangle")

# Rectangle properties
rect_x, rect_y = 300, 200
rect_width, rect_height = 50, 50
rect_speed = 5

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    # Fill the screen with a color
    screen.fill((255, 255, 255))

    # Draw the moving rectangle
    pygame.draw.rect(screen, (0, 0, 255), (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()
