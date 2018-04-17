# ICS3U
# Assignment 2: Logo
# <your name>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
pygame.init()

# Define some colours
# Colours are defined using RGB values
DARKGREY = (17, 46, 19)
WHITE = (255, 255, 255)
GREEN = (127, 235, 130)
BROWN = (64, 62, 26)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
# Set the screen size (please don't change this)

SCREENWIDTH = 400
SCREENHEIGHT = 400

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)


# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Logo")

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # --- Game logic goes here
    # There should be none for a static image
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(RED)

    # Queue different shapes and lines to be drawn
    pygame.draw.ellipse(screen, BLACK, [50, 7, 375, 375], 0)
    pygame.draw.ellipse(screen, WHITE, [15, 15, 375, 375], 0)
    pygame.draw.ellipse(screen, RED, [100, 100, 200, 200], 0)
    pygame.draw.ellipse(screen, WHITE, [125, 125, 150, 150], 0)
    pygame.draw.rect(screen , RED, [100 , 0 , 25 , 200], 0)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
