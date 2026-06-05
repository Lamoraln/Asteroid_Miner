import pygame


class LevelCard:
    """
    UI card representing a game level.

    Displays:
    - Level thumbnail
    - Level title
    - Star rating
    - Locked/unlocked status
    """

    def __init__(
        self,
        x,
        y,
        width,
        height,
        title,
        stars,
        image_path,
        unlocked=True
    ):
        # Card area
        self.rect = pygame.Rect(
            x,
            y,
            width,
            height
        )

        self.title = title
        self.stars = stars
        self.unlocked = unlocked

        # Level preview image
        self.image = pygame.image.load(
            image_path
        )

        self.image = pygame.transform.scale(
            self.image,
            (
                width,
                height - 60
            )
        )

        # Card font
        self.font = pygame.font.SysFont(
            None,
            28
        )

    def draw(self, screen):
        """
        Draws the level card.
        """

        # Different color if level is locked
        card_color = (
            (60, 60, 100)
            if self.unlocked
            else (40, 40, 40)
        )

        # Card background
        pygame.draw.rect(
            screen,
            card_color,
            self.rect,
            border_radius=10
        )

        # Level image
        screen.blit(
            self.image,
            (
                self.rect.x,
                self.rect.y
            )
        )

        # Level title
        title_surface = self.font.render(
            self.title,
            True,
            (255, 255, 255)
        )

        screen.blit(
            title_surface,
            (
                self.rect.x + 10,
                self.rect.y + self.rect.height - 55
            )
        )

        # Draw star rating
        for i in range(3):

            star_color = (
                (255, 215, 0)
                if i < self.stars
                else (100, 100, 100)
            )

            pygame.draw.circle(
                screen,
                star_color,
                (
                    self.rect.x + 30 + i * 30,
                    self.rect.y + self.rect.height - 20
                ),
                10
            )

        # Locked label
        if not self.unlocked:

            lock_surface = self.font.render(
                "LOCKED",
                True,
                (191, 191, 191)
            )

            screen.blit(
                lock_surface,
                (
                    self.rect.x + 20,
                    self.rect.y + 20
                )
            )

    def is_clicked(self, event):
        """
        Returns True when the card is clicked
        and the level is unlocked.
        """

        return (
            self.unlocked
            and event.type == pygame.MOUSEBUTTONDOWN
            and self.rect.collidepoint(event.pos)
        )