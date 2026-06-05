import pygame

# Game states
from states.menu import menu_loop
from states.level_select import level_select_loop
from states.game import game_loop
from states.stadistics import statistics_loop


# Initialize Pygame
pygame.init()

# Create game window
screen = pygame.display.set_mode((1200, 700))

# Initial state
state = "menu"
selected_level = None

running = True

# Main game loop
while running:

    # Main menu
    if state == "menu":
        state = menu_loop(screen)

    # Statistics screen
    elif state == "statistics":
        state = statistics_loop(screen)

    # Level selection screen
    elif state == "level_select":
        state, selected_level = level_select_loop(screen)

    # Gameplay screen
    elif state == "game":
        state = game_loop(
            screen,
            selected_level
        )

    # Close application
    elif state == "quit":
        running = False


# Shut down Pygame
pygame.quit()