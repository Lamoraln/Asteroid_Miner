import pygame

def statistics_loop(screen):
    """
    Displays the mission history stored in route_history.txt.
    Press ESC to return to the main menu.
    """

    font = pygame.font.SysFont(None, 32)

    # Load saved missions
    try:
        with open("data/route_history.txt", "r") as file:
            routes = file.readlines()
    except:
        routes = []

    while True:

        # Background
        screen.fill((25, 20, 40))

        # Screen title
        title = font.render(
            "MISSION HISTORY",
            True,
            (255, 255, 255)
        )
        screen.blit(title, (50, 50))

        # Show the last 10 saved missions
        recent_routes = routes[-10:]

        for i, route in enumerate(recent_routes):

            txt = font.render(
                route.strip(),
                True,
                (255, 255, 255)
            )

            screen.blit(
                txt,
                (50, 120 + i * 40)
            )

        # Navigation hint
        info = font.render(
            "Press ESC to return",
            True,
            (200, 200, 200)
        )

        screen.blit(info, (50, 650))

        # Event handling
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit"

            if (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_ESCAPE
            ):
                return "menu"

        pygame.display.flip()