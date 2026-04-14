import pygame

def game_loop(screen, level):
    font = pygame.font.SysFont(None, 40)

    while True:
        screen.fill((0,0,0))

        text = font.render(f"LEVEL {level}", True, (255,255,255))
        screen.blit(text, (300, 250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "level_select"

        pygame.display.flip()