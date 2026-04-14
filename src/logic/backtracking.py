from logic.utils import distance

def backtracking_route(base, asteroids, fuel):

    best_solution = {
        "route": [],
        "value": 0
    }

    def backtrack(current, remaining, fuel_left, current_value, route):

        # Verificar si puede volver a la base
        dist_to_base = distance(current, base)

        if dist_to_base <= fuel_left:
            if current_value > best_solution["value"]:
                best_solution["value"] = current_value
                best_solution["route"] = route + [base]

        # Explorar siguientes asteroides
        for i, a in enumerate(remaining):
            dist_to_a = distance(current, a)
            dist_back = distance(a, base)

            # Poda: no alcanza combustible para ir y volver
            if dist_to_a + dist_back > fuel_left:
                continue

            # Llamada recursiva
            backtrack(
                a,
                remaining[:i] + remaining[i+1:],  # quitar el asteroide actual
                fuel_left - dist_to_a,
                current_value + a.value,
                route + [a]
            )

    # Iniciar desde la base
    backtrack(base, asteroids, fuel, 0, [base])

    return best_solution["route"], best_solution["value"]