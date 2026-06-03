import pygame
from ui.button import Button

background = pygame.image.load("assets/menu_background.jpg")
background = pygame.transform.scale(background, (1200, 700))
def menu_loop(screen):
    button = Button("START", 425, 350, 350, 60)
    stats_button = Button("STATISTICS", 425, 420, 350, 60)

    while True:
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(background, (0, 0))

        button.update(mouse_pos)
        button.draw(screen)

        stats_button.update(mouse_pos)
        stats_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if button.is_clicked(event):
                return "level_select"

            if stats_button.is_clicked(event):
                return "statistics"

        pygame.display.flip()