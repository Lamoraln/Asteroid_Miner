import pygame
from logic.asteroids import Asteroid
from logic.levels import get_level
from logic.utils import distance
from logic.backtracking import backtracking_route

WIDTH, HEIGHT = 800, 600

def game_loop(screen, level):

    # ---------- CONFIG LEVEL ----------
    level_data = get_level(level)
    base = level_data["base"]

    asteroids = level_data["asteroids"]

    fuel = level_data["fuel"]

    # ---------- ESTADO ----------
    selected_route = []
    current = base
    fuel_left = fuel
    total_value = 0
    finished = False
    stars = 0

    font = pygame.font.SysFont(None, 30)

    def to_screen(a):
        return (a.x * 80 + 50, a.y * 60)

    # ---------- LOOP ----------
    while True:
        screen.fill((10, 10, 30))

        # ---------- DIBUJAR BASE ----------
        pygame.draw.circle(screen, (0, 100, 255), to_screen(base), 10)

        # ---------- DIBUJAR ASTEROIDES ----------
        for a in asteroids:
            pygame.draw.circle(screen, (200, 200, 200), to_screen(a), 8)

        # ---------- DIBUJAR RUTA ----------
        prev = base
        for a in selected_route:
            pygame.draw.line(screen, (0, 255, 0), to_screen(prev), to_screen(a), 2)
            prev = a

        # ---------- EVENTOS ----------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:

                # FINALIZAR NIVEL
                if event.key == pygame.K_RETURN and not finished:

                    # regresar a base
                    dist_back = distance(current, base)
                    fuel_left -= dist_back
                    selected_route.append(base)

                    # calcular óptimo
                    optimal_route, optimal_value = backtracking_route(base, asteroids, fuel)

                    ratio = total_value / optimal_value if optimal_value > 0 else 0

                    if ratio < 0.5:
                        stars = 0
                    elif ratio < 0.7:
                        stars = 1
                    elif ratio < 1:
                        stars = 2
                    else:
                        stars = 3

                    print("\n--- RESULTADO ---")
                    print("Jugador:", total_value)
                    print("Óptimo:", optimal_value)
                    print("Estrellas:", stars)

                    finished = True

                # SALIR DEL NIVEL
                if event.key == pygame.K_ESCAPE and finished:
                    return "level_select"

            # CLICK EN ASTEROIDES
            if event.type == pygame.MOUSEBUTTONDOWN and not finished:
                mouse = event.pos

                for a in asteroids:
                    if a in selected_route:
                        continue

                    if distance_point(mouse, to_screen(a)) < 10:

                        dist = distance(current, a)
                        dist_back = distance(a, base)

                        # verificar ida + regreso
                        if fuel_left >= dist + dist_back:
                            selected_route.append(a)
                            fuel_left -= dist
                            total_value += a.value
                            current = a

        # ---------- UI ----------
        fuel_text = font.render(f"Fuel: {round(fuel_left,2)}", True, (255,255,255))
        value_text = font.render(f"Value: {total_value}", True, (255,255,255))
        info_text = font.render("Press ENTER to finish", True, (200,200,200))

        screen.blit(fuel_text, (10, 10))
        screen.blit(value_text, (10, 40))
        screen.blit(info_text, (10, 70))

        # ---------- RESULTADOS ----------
        if finished:
            result_text = font.render(f"Stars: {stars}", True, (255, 215, 0))
            screen.blit(result_text, (350, 250))

            exit_text = font.render("Press ESC to return", True, (200,200,200))
            screen.blit(exit_text, (300, 300))

        pygame.display.flip()


# ---------- UTIL ----------
def distance_point(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2) ** 0.5