import pygame
from ui.button import Button

# Load and scale menu background
background = pygame.image.load("assets/menu_background.jpg")
background = pygame.transform.scale(background, (1200, 700))


def menu_loop(screen):
    """
    Main menu screen.
    Returns the next game state selected by the player.
    """

    # Menu buttons
    start_button = Button("START", 425, 350, 350, 60)
    stats_button = Button("STATISTICS", 425, 420, 350, 60)

    while True:

        # Current mouse position for hover effects
        mouse_pos = pygame.mouse.get_pos()

        # Draw background
        screen.blit(background, (0, 0))

        # Update and draw buttons
        for button in [start_button, stats_button]:
            button.update(mouse_pos)
            button.draw(screen)

        # Handle events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit"

            if start_button.is_clicked(event):
                return "level_select"

            if stats_button.is_clicked(event):
                return "statistics"

        pygame.display.flip()