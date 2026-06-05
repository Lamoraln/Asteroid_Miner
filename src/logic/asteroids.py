import pygame

class Asteroid:
    """
    Represents a mineable asteroid in the game.

    Each asteroid stores:
    - Position in the map
    - Asteroid type
    - Unique name
    - Resource value
    - Display image
    """

    # Resource value associated with each asteroid type
    VALUES = {
        "silver": 50,
        "gold": 100,
        "diamond": 150,
        "dark_matter": 250
    }

    # Load and scale images only once.
    # These class attributes are shared by all asteroid objects,
    # reducing memory usage and loading time.
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
        """
        Creates a new asteroid.

        Parameters:
            x             -> horizontal position
            y             -> vertical position
            asteroid_type -> silver, gold, diamond or dark_matter
            name          -> unique asteroid identifier
        """

        # Map coordinates
        self.x = x
        self.y = y

        # Asteroid information
        self.type = asteroid_type
        self.name = name

        # Automatically assign value and image
        # according to asteroid type
        self.value = self.VALUES[asteroid_type]
        self.image = self.IMAGES[asteroid_type]