import pygame

from ui.level_card import LevelCard
from ui.title_card import TitleCard
from ui.button import Button


# Background image
background = pygame.image.load(
    "assets/background2.png"
)

background = pygame.transform.scale(
    background,
    (1200, 700)
)


def level_select_loop(screen):
    """
    Level selection screen.

    Responsibilities:
    - Display available levels
    - Handle level selection
    - Return the chosen level
    """

    # Create level cards
    levels = [
        LevelCard(
            90, 200,
            330, 330,
            "Cinturón",
            2,
            "assets/level1.jpg",
            True
        ),

        LevelCard(
            430, 200,
            330, 330,
            "Nebulosa",
            3,
            "assets/level2.png",
            True
        ),

        LevelCard(
            770, 200,
            330, 330,
            "Cometas",
            0,
            "assets/level3.png",
            True
        ),
    ]

    # Screen title
    title = TitleCard(
        "LEVEL SELECT",
        center_x=600,
        center_y=100,
        font_size=55
    )
    back_button = Button(
    "BACK",
    30,
    620,
    200,
    50
    )

    # Main loop
    while True:

        # Draw background
        screen.blit(
            background,
            (0, 0)
        )

        # Draw title
        title.draw(screen)

        # Draw all available levels
        for level in levels:
            level.draw(screen)

        # Handle events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit", None
            
            if back_button.is_clicked(event):
                return "menu", None

            # Check if a level card was clicked
            for index, level in enumerate(levels):

                if level.is_clicked(event):

                    return (
                        "game",
                        index + 1
                    )
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit", None

            if back_button.is_clicked(event):
                return "menu", None

            for i, lvl in enumerate(levels):

                if lvl.is_clicked(event):
                    return "game", i + 1
        mouse_pos = pygame.mouse.get_pos()

        back_button.update(mouse_pos)
        
        for lvl in levels:
            lvl.draw(screen)

        back_button.draw(screen)

        pygame.display.flip()
        
