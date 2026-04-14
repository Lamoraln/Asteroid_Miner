import pygame

class Button:
    def __init__(self, text, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        
        # Colores Estilo "MINER" (Amarillo -> Naranja)
        self.color_top = (255, 240, 50)     # Amarillo brillante
        self.color_bottom = (255, 100, 0)   # Naranja saturado
        self.color_extrusion = (130, 40, 0) # Marrón rojizo para profundidad
        
        # Colores del Marco/Caja
        self.box_bg = (30, 30, 50)          # Fondo de la caja oscuro
        self.box_border = (60, 60, 90)      # Borde de la caja
        self.box_highlight = (100, 100, 150)# Brillo del borde
        
        # Fuente (Arial Black es la más similar por defecto)
        self.font = pygame.font.SysFont("Arial Black", 45)
        self.is_hovered = False

    def create_gradient_text(self, text, t_color, b_color):
        """Genera el texto con degradado vertical."""
        text_surf = self.font.render(text, True, (255, 255, 255)).convert_alpha()
        w, h = text_surf.get_size()
        gradient = pygame.Surface((w, h)).convert_alpha()
        
        for i in range(h):
            # Mezcla de colores según la altura
            r = t_color[0] + (b_color[0] - t_color[0]) * i // h
            g = t_color[1] + (b_color[1] - t_color[1]) * i // h
            b = t_color[2] + (b_color[2] - t_color[2]) * i // h
            pygame.draw.line(gradient, (r, g, b), (0, i), (w, i))
            
        gradient.blit(text_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        return gradient

    def draw(self, screen):
        # 1. Dibujar la CAJA (Contenedor)
        # Sombra de la caja
        pygame.draw.rect(screen, (10, 10, 20), (self.rect.x + 4, self.rect.y + 4, self.rect.w, self.rect.h), border_radius=12)
        # Fondo y borde principal
        pygame.draw.rect(screen, self.box_bg, self.rect, border_radius=12)
        border_color = self.box_highlight if self.is_hovered else self.box_border
        pygame.draw.rect(screen, border_color, self.rect, width=3, border_radius=12)

        # 2. Preparar el TEXTO
        text_x = self.rect.centerx - self.font.size(self.text)[0] // 2
        text_y = self.rect.centery - self.font.size(self.text)[1] // 2
        
        # Ajuste si hay hover (el texto "pulsa" hacia arriba)
        offset = 2 if self.is_hovered else 0
        current_y = text_y - offset

        # 3. Dibujar EXTRUSIÓN del texto (Profundidad 3D)
        depth = 6
        for i in range(depth):
            depth_surf = self.font.render(self.text, True, self.color_extrusion)
            screen.blit(depth_surf, (text_x, current_y + i))

        # 4. Dibujar FRENTE del texto (Degradado Amarillo-Naranja)
        # Aclarar ligeramente en hover
        t_col = (255, 255, 150) if self.is_hovered else self.color_top
        b_col = (255, 150, 50) if self.is_hovered else self.color_bottom
        
        text_main = self.create_gradient_text(self.text, t_col, b_col)
        screen.blit(text_main, (text_x, current_y))

    def update(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False