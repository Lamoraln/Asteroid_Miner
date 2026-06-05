import pygame


class TitleCard:
    """
    Static title card used as a decorative UI element.

    It creates a framed container with a 3D gradient text
    inspired by the game's logo style.
    """

    def __init__(
        self,
        text,
        center_x,
        center_y,
        font_size=55
    ):
        self.text = text

        # Main font used for the title
        self.font = pygame.font.SysFont(
            "Arial Black",
            font_size
        )

        # Measure text size
        self.text_width, self.text_height = self.font.size(
            self.text
        )

        # Container padding
        padding_x = 40
        padding_y = 30

        # Create centered container rectangle
        self.rect = pygame.Rect(
            0,
            0,
            self.text_width + padding_x,
            self.text_height + padding_y
        )

        self.rect.center = (
            center_x,
            center_y
        )

        # Gradient colors
        self.color_top = (255, 240, 50)
        self.color_bottom = (255, 100, 0)

        # 3D depth color
        self.color_extrusion = (130, 40, 0)

        # Card colors
        self.box_bg = (30, 30, 50)
        self.box_border = (60, 60, 90)

    def create_gradient_text(
        self,
        text,
        top_color,
        bottom_color
    ):
        """
        Creates a text surface with a vertical color gradient.
        """

        text_surface = self.font.render(
            text,
            True,
            (255, 255, 255)
        ).convert_alpha()

        width, height = text_surface.get_size()

        gradient = pygame.Surface(
            (width, height)
        ).convert_alpha()

        # Draw gradient line by line
        for y in range(height):

            r = (
                top_color[0]
                + (bottom_color[0] - top_color[0]) * y // height
            )

            g = (
                top_color[1]
                + (bottom_color[1] - top_color[1]) * y // height
            )

            b = (
                top_color[2]
                + (bottom_color[2] - top_color[2]) * y // height
            )

            pygame.draw.line(
                gradient,
                (r, g, b),
                (0, y),
                (width, y)
            )

        # Apply gradient over text
        gradient.blit(
            text_surface,
            (0, 0),
            special_flags=pygame.BLEND_RGBA_MULT
        )

        return gradient

    def draw(self, screen):
        """
        Draws the title card on screen.
        """

        # Shadow
        pygame.draw.rect(
            screen,
            (10, 10, 20),
            (
                self.rect.x + 4,
                self.rect.y + 4,
                self.rect.w,
                self.rect.h
            ),
            border_radius=12
        )

        # Main card
        pygame.draw.rect(
            screen,
            self.box_bg,
            self.rect,
            border_radius=12
        )

        pygame.draw.rect(
            screen,
            self.box_border,
            self.rect,
            width=3,
            border_radius=12
        )

        # Center text inside card
        text_x = (
            self.rect.centerx
            - self.text_width // 2
        )

        text_y = (
            self.rect.centery
            - self.text_height // 2
        )

        # Draw 3D depth effect
        depth = 6

        for offset in range(depth):

            depth_surface = self.font.render(
                self.text,
                True,
                self.color_extrusion
            )

            screen.blit(
                depth_surface,
                (
                    text_x,
                    text_y + offset
                )
            )

        # Draw gradient front text
        title_surface = self.create_gradient_text(
            self.text,
            self.color_top,
            self.color_bottom
        )

        screen.blit(
            title_surface,
            (
                text_x,
                text_y
            )
        )