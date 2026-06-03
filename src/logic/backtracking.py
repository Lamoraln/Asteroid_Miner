from logic.utils import distance

nodes_explored = 0


def backtracking_route(base, asteroids, fuel):

    global nodes_explored
    nodes_explored = 0

    best_route = []
    best_value = 0

    def backtrack(
        current,
        remaining,
        fuel_left,
        current_route,
        current_value
    ):
        global nodes_explored

        nodes_explored += 1

        nonlocal best_route
        nonlocal best_value

        # ----------------------------------
        # PODA
        # ----------------------------------

        remaining_value = sum(
            asteroid.value
            for asteroid in remaining
        )

        if current_value + remaining_value <= best_value:
            return

        # ----------------------------------
        # ACTUALIZAR MEJOR SOLUCIÓN
        # ----------------------------------

        if current_value > best_value:

            best_value = current_value

            best_route = current_route.copy()

        # ----------------------------------
        # EXPLORAR SIGUIENTES ASTEROIDES
        # ----------------------------------

        for asteroid in remaining:

            dist_to_asteroid = distance(
                current,
                asteroid
            )

            fuel_after_move = (
                fuel_left
                - dist_to_asteroid
            )

            # combustible insuficiente
            if fuel_after_move < 0:
                continue

            # debe poder regresar a base
            dist_back = distance(
                asteroid,
                base
            )
            

            if fuel_after_move < dist_back:
                continue

            new_remaining = [
                a
                for a in remaining
                if a != asteroid
            ]

            backtrack(
                asteroid,
                new_remaining,
                fuel_after_move,
                current_route + [asteroid],
                current_value + asteroid.value
            )

    backtrack(
        base,
        asteroids,
        fuel,
        [],
        0
    )

    return (
        best_route,
        best_value,
        nodes_explored
    )