import pygame


class Button:
    """
    Custom button with:
    - 3D text effect
    - Vertical gradient
    - Hover animation
    - Mouse click detection
    """

    def __init__(
        self,
        text,
        x,
        y,
        width,
        height
    ):
        self.text = text

        # Button area
        self.rect = pygame.Rect(
            x,
            y,
            width,
            height
        )

        # Button state
        self.is_hovered = False

        # Main font
        self.font = pygame.font.SysFont(
            "Arial Black",
            45
        )

        # Cache text size
        self.text_width, self.text_height = self.font.size(
            self.text
        )

        # Gradient colors
        self.color_top = (255, 240, 50)
        self.color_bottom = (255, 100, 0)

        # 3D depth color
        self.color_extrusion = (130, 40, 0)

        # Container colors
        self.box_bg = (30, 30, 50)
        self.box_border = (60, 60, 90)
        self.box_highlight = (100, 100, 150)

    def create_gradient_text(
        self,
        text,
        top_color,
        bottom_color
    ):
        """
        Creates a text surface with a vertical gradient.
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

        gradient.blit(
            text_surface,
            (0, 0),
            special_flags=pygame.BLEND_RGBA_MULT
        )

        return gradient

    def draw(self, screen):
        """
        Draws the button and its hover effects.
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

        # Main container
        pygame.draw.rect(
            screen,
            self.box_bg,
            self.rect,
            border_radius=12
        )

        border_color = (
            self.box_highlight
            if self.is_hovered
            else self.box_border
        )

        pygame.draw.rect(
            screen,
            border_color,
            self.rect,
            width=3,
            border_radius=12
        )

        # Center text
        text_x = (
            self.rect.centerx
            - self.text_width // 2
        )

        text_y = (
            self.rect.centery
            - self.text_height // 2
        )

        # Small hover animation
        hover_offset = (
            2 if self.is_hovered else 0
        )

        current_y = text_y - hover_offset

        # Draw 3D depth
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
                    current_y + offset
                )
            )

        # Brighter colors on hover
        top_color = (
            (255, 255, 150)
            if self.is_hovered
            else self.color_top
        )

        bottom_color = (
            (255, 150, 50)
            if self.is_hovered
            else self.color_bottom
        )

        front_text = self.create_gradient_text(
            self.text,
            top_color,
            bottom_color
        )

        screen.blit(
            front_text,
            (
                text_x,
                current_y
            )
        )

    def update(self, mouse_pos):
        """
        Updates hover state.
        """

        self.is_hovered = self.rect.collidepoint(
            mouse_pos
        )

    def is_clicked(self, event):
        """
        Returns True when the left mouse button
        clicks inside the button area.
        """

        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )