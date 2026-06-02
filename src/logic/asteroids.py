import pygame

class Asteroid:

    VALUES = {
        "silver": 50,
        "gold": 100,
        "diamond": 150,
        "dark_matter": 250
    }

    IMAGES = {
        "silver": pygame.transform.scale(
            pygame.image.load("assets/asteroid_silver.png"),
            (80, 70)
        ),
        "gold": pygame.transform.scale(
            pygame.image.load("assets/asteroid_gold.png"),
            (80, 70)
        ),
        "diamond": pygame.transform.scale(
            pygame.image.load("assets/asteroid_diamond.png"),
            (80, 70)
        ),
        "dark_matter": pygame.transform.scale(
            pygame.image.load("assets/asteroid_darkm.png"),
            (80, 70)
        )
    }

    def __init__(self, x, y, asteroid_type, name):

        self.x = x
        self.y = y
        self.type = asteroid_type
        self.name = name

        self.value = self.VALUES[asteroid_type]
        self.image = self.IMAGES[asteroid_type]