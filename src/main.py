import pygame
from states.menu import menu_loop
from states.level_select import level_select_loop
from states.game import game_loop

pygame.init()
screen = pygame.display.set_mode((1200, 700))

state = "menu"
selected_level = None

running = True

while running:
    if state == "menu":
        state = menu_loop(screen)

    elif state == "level_select":
        state, selected_level = level_select_loop(screen)

    elif state == "game":
        state = game_loop(screen, selected_level)

    elif state == "quit":
        running = False

pygame.quit()