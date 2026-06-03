import pygame

def statistics_loop(screen):

    font = pygame.font.SysFont(None, 32)

    try:

        with open(
            "data/route_history.txt",
            "r"
        ) as file:

            routes = file.readlines()

    except:

        routes = []

    while True:

        screen.fill((25,20,40))

        title = font.render(
            "MISSION HISTORY",
            True,
            (255,255,255)
        )

        screen.blit(
            title,
            (50,50)
        )

        recent_routes = routes[-10:]

        for i, route in enumerate(recent_routes):

            txt = font.render(
                route.strip(),
                True,
                (255,255,255)
            )

            screen.blit(
                txt,
                (50,120 + i * 40)
            )

        info = font.render(
            "Press ESC to return",
            True,
            (200,200,200)
        )

        screen.blit(
            info,
            (50,650)
        )

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    return "menu"

        pygame.display.flip()