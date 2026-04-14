import pygame

class LevelCard:
    def __init__(self, x, y, width, height, title, stars, image_path, unlocked=True):
        self.rect = pygame.Rect(x, y, width, height)
        self.title = title
        self.stars = stars
        self.unlocked = unlocked

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height - 60))

        self.font = pygame.font.SysFont(None, 28)

    def draw(self, screen):
        # Fondo tarjeta
        color = (60, 60, 100) if self.unlocked else (40, 40, 40)
        pygame.draw.rect(screen, color, self.rect, border_radius=10)

        # Imagen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        # Título
        text = self.font.render(self.title, True, (255,255,255))
        screen.blit(text, (self.rect.x + 10, self.rect.y + self.rect.height - 55))

        # Estrellas
        for i in range(3):
            star_color = (255, 215, 0) if i < self.stars else (100, 100, 100)
            pygame.draw.circle(
                screen,
                star_color,
                (self.rect.x + 30 + i*30, self.rect.y + self.rect.height - 20),
                10
            )

        # Bloqueado
        if not self.unlocked:
            lock_text = self.font.render("LOCKED", True, (191,191,191))
            screen.blit(lock_text, (self.rect.x + 20, self.rect.y + 20))

    def is_clicked(self, event):
        if self.unlocked and event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False