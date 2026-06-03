import pygame
import json
import subprocess

from logic.asteroids import Asteroid
from logic.levels import get_level
from logic.utils import distance
from logic.backtracking import backtracking_route
from logic.greedy import greedy_recommendation

WIDTH, HEIGHT = 800, 600

def game_loop(screen, level):

    # ---------- CONFIG LEVEL ----------
    level_data = get_level(level)
    base = level_data["base"]
    nodes_explored = 0
    optimal_value = 0
    efficiency = 0

    asteroids = level_data["asteroids"]

    fuel = level_data["fuel"]

    # ---------- ESTADO ----------
    selected_route = []
    current = base
    fuel_left = fuel
    total_value = 0
    finished = False
    stars = 0
    greedy_target = None
    mission_failed = False

    font = pygame.font.SysFont(None, 30)
    
    small_font = pygame.font.SysFont(None, 24)

    hovered_asteroid = None

    def to_screen(a):
        return (a.x * 80 + 50, a.y * 60)

    
            # ---------- DIBUJAR BASE ----------
    base_img = pygame.image.load("assets/base.png")
    base_img = pygame.transform.scale(base_img, (120, 120))
    # ---------- LOOP ----------
    
    while True:
        screen.fill((10, 10, 30))


        base_pos = to_screen(base)

        screen.blit(
            base_img,
            (
                base_pos[0] - base_img.get_width() // 2,
                base_pos[1] - base_img.get_height() // 2
            )
        )

        # ---------- DIBUJAR ASTEROIDES ----------
        for a in asteroids:
            pos = to_screen(a)

            screen.blit(
                a.image,
                (
                    pos[0] - a.image.get_width() // 2,
                    pos[1] - a.image.get_height() // 2
                )
            )

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
                # MOSTRAR PISTA GREEDY
                if event.key == pygame.K_h:

                    greedy_target = greedy_recommendation(
                        current,
                        asteroids,
                        selected_route
                    )
                    
                # FINALIZAR NIVEL
                if event.key == pygame.K_RETURN and not finished:

                    dist_back = distance(current, base)

                    if fuel_left < dist_back:

                        stars = 0 
                        cpp_message = ""
                        finished = True
                        mission_failed = True

                    else:

                        fuel_left -= dist_back
                        selected_route.append(base)

                        optimal_route, optimal_value, nodes_explored = backtracking_route(
                            base,
                            asteroids,
                            fuel
                        )
                        
                        if optimal_value > 0:
                            efficiency = round(
                                (total_value / optimal_value) * 100,
                                1
                            )
                        else:
                            efficiency = 0

                        ratio = (
                            total_value / optimal_value
                            if optimal_value > 0
                            else 0
                        )

                        if ratio < 0.5:
                            stars = 0
                        elif ratio < 0.7:
                            stars = 1
                        elif ratio < 1:
                            stars = 2
                        else:
                            stars = 3

                        route_data = []

                        for asteroid in selected_route:

                            if asteroid.name == "Base":
                                continue

                            route_data.append({
                                "name": asteroid.name,
                                "type": asteroid.type,
                                "value": asteroid.value
                            })

                        game_data = {
                            "level": level,
                            "resources": total_value,
                            "stars": stars,
                            "route": route_data
                        }

                        with open(
                            "data/game_state.json",
                            "w"
                        ) as file:

                            json.dump(
                                game_data,
                                file,
                                indent=4
                            )

                        result = subprocess.run(
                            ["./cpp/asteroid_engine"],
                            capture_output=True,
                            text=True
                        )
                        
                        try:

                            with open(
                                "data/output.json",
                                "r"
                            ) as file:

                                output_data = json.load(file)

                                cpp_message = (
                                    output_data.get(
                                        "route_saved",
                                        ""
                                    )
                                )

                        except Exception as e:

                            print(e)

                        print(result.stdout)

                        if result.stderr:
                            print(result.stderr)

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

                    if distance_point(mouse, to_screen(a)) < 25:

                        dist = distance(current, a)
                        if fuel_left >= dist:
                            
                            selected_route.append(a)
                            fuel_left -= dist
                            total_value += a.value
                            current = a

        # ---------- UI ----------
        fuel_text = font.render(f"Fuel: {round(fuel_left,2)}", True, (255,255,255))
        value_text = font.render(f"Value: {total_value}", True, (255,255,255))
        info_text = font.render("Press ENTER to finish", True, (200,200,200))
        hint_text = font.render("Press H to get a hint", True, (200,200,200))
        screen.blit(fuel_text, (10, 10))
        screen.blit(value_text, (10, 40))
        screen.blit(info_text, (10, 70))
        screen.blit(hint_text, (10, 100))

        # ---------- RESULTADOS ----------
        if finished:
            
            if mission_failed:

                fail_text = font.render(
                    "INSUFFICIENT FUEL - MISSION FAILED",
                    True,
                    (255,0,0)
                )

                screen.blit(
                    fail_text,
                    (430,600)
                )

            else:

                result_text = font.render(
                    f"You Win Stars: {stars}",
                    True,
                    (255,215,0)
                )
                
                stats = [
                    f"Player Value: {total_value}",
                    f"Optimal Value: {optimal_value}",
                    f"Efficiency: {efficiency}%",
                    f"Nodes Explored: {nodes_explored}"
                ]

                for i, text in enumerate(stats):

                    txt = small_font.render(
                        text,
                        True,
                        (255,255,255)
                    )

                    screen.blit(
                        txt,
                        (430, 700 + i * 25)
                    )

                screen.blit(result_text,(430,600))

            exit_text = font.render("Press ESC to return", True, (200,200,200))
            screen.blit(exit_text, (430, 650))
            if cpp_message:

                saved_text = font.render(
                    f"Saved Route: {cpp_message}",
                    True,
                    (255,255,255)
                )

                screen.blit(
                    saved_text,
                    (430,700)
                )
            
        mouse_pos = pygame.mouse.get_pos()

        hovered_asteroid = None

        for a in asteroids:

            pos = to_screen(a)

            rect = a.image.get_rect(center=pos)

            if rect.collidepoint(mouse_pos):
                hovered_asteroid = a
                break
            
            
        if hovered_asteroid:

            dist = distance(current, hovered_asteroid)

            score = hovered_asteroid.value / max(dist, 0.1)

            pygame.draw.rect(
                screen,
                (30,30,30),
                (520,20,250,110)
            )

            pygame.draw.rect(
                screen,
                (255,255,255),
                (520,20,250,110),
                2
            )

            lines = [
                f"Type: {hovered_asteroid.type}",
                f"Value: {hovered_asteroid.value}",
                f"Distance: {round(dist,2)}",
                f"Greedy Score: {round(score,2)}"
            ]

            for i, text in enumerate(lines):

                txt = small_font.render(
                    text,
                    True,
                    (255,255,255)
                )

                screen.blit(
                    txt,
                    (530,30 + i*22)
                )
                
        if greedy_target:

            pos = to_screen(greedy_target)

            pygame.draw.circle(
                screen,
                (0,255,0),
                pos,
                30,
                3
            )

            hint = font.render(
                "GREEDY RECOMMENDATION",
                True,
                (0,255,0)
            )

            screen.blit(
                hint,
                (500,150)
            )

        pygame.display.flip()


# ---------- UTIL ----------
def distance_point(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2) ** 0.5