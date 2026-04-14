import pygame

class TitleCard:
    """Un diseño de tarjeta de título estático (no reactivo al hover)
       basado en el diseño del botón 'Miner'."""
    def __init__(self, text, center_x, center_y, font_size=55):
        self.text = text
        
        # Fuente (Arial Black es muy similar)
        self.font = pygame.font.SysFont("Arial Black", font_size)
        
        # Calcular el tamaño del texto para definir la caja
        text_w, text_h = self.font.size(self.text)
        
        # Definir el tamaño de la caja (un poco más grande que el texto)
        # Ajusta el padding si lo necesitas (por ejemplo, 30, 20)
        box_padding_w = 40
        box_padding_h = 30
        self.rect = pygame.Rect(0, 0, text_w + box_padding_w, text_h + box_padding_h)
        self.rect.center = (center_x, center_y) # Centrar la caja

        # Colores Estilo "MINER" (Amarillo -> Naranja)
        self.color_top = (255, 240, 50)     # Amarillo brillante
        self.color_bottom = (255, 100, 0)   # Naranja saturado
        self.color_extrusion = (130, 40, 0) # Profundidad

        # Colores del Marco/Caja (Diseño espacial)
        self.box_bg = (30, 30, 50)          # Fondo oscuro
        self.box_border = (60, 60, 90)      # Borde gris-azul

    def create_gradient_text(self, text, t_color, b_color):
        text_surf = self.font.render(text, True, (255, 255, 255)).convert_alpha()
        w, h = text_surf.get_size()
        gradient = pygame.Surface((w, h)).convert_alpha()
        
        for i in range(h):
            r = t_color[0] + (b_color[0] - t_color[0]) * i // h
            g = t_color[1] + (b_color[1] - t_color[1]) * i // h
            b = t_color[2] + (b_color[2] - t_color[2]) * i // h
            pygame.draw.line(gradient, (r, g, b), (0, i), (w, i))
            
        gradient.blit(text_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        return gradient

    def draw(self, screen):
        # 1. Dibujar la CAJA (Contenedor)
        # Sombra externa
        pygame.draw.rect(screen, (10, 10, 20), (self.rect.x + 4, self.rect.y + 4, self.rect.w, self.rect.h), border_radius=12)
        # Fondo y borde principal
        pygame.draw.rect(screen, self.box_bg, self.rect, border_radius=12)
        pygame.draw.rect(screen, self.box_border, self.rect, width=3, border_radius=12)

        # 2. Dibujar EXTRUSIÓN del texto (Profundidad 3D)
        text_x = self.rect.centerx - self.font.size(self.text)[0] // 2
        text_y = self.rect.centery - self.font.size(self.text)[1] // 2
        
        depth = 6
        for i in range(depth):
            depth_surf = self.font.render(self.text, True, self.color_extrusion)
            screen.blit(depth_surf, (text_x, text_y + i))

        # 3. Dibujar FRENTE del texto (Degradado Amarillo-Naranja)
        text_main = self.create_gradient_text(self.text, self.color_top, self.color_bottom)
        screen.blit(text_main, (text_x, text_y))