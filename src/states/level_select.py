import pygame
from ui.level_card import LevelCard
from ui.title_card import TitleCard
background = pygame.image.load("assets/background2.png")
background = pygame.transform.scale(background, (1200, 700))

def level_select_loop(screen):
    # Crear niveles
    levels = [
        LevelCard(90, 200, 330, 330, "Cinturón", 2, "assets/level1.jpg", True),
        LevelCard(430, 200, 330, 330, "Nebulosa", 3, "assets/level2.png", True),
        LevelCard(770, 200, 330, 330, "Cometas", 0, "assets/level3.png", False),
    ]

    font = pygame.font.SysFont(None, 60)

    while True:
        screen.blit(background, (0, 0))

        # Título
        title = TitleCard("LEVEL SELECT", center_x=600, center_y=100, font_size=55)
        title.draw(screen)
        # Dibujar niveles
        for lvl in levels:
            lvl.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit", None

            for i, lvl in enumerate(levels):
                if lvl.is_clicked(event):
                    return "game", i+1

        pygame.display.flip()