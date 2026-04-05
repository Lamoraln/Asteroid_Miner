from utils import distance

def greedy_route(base, asteroids, fuel):
    route = [base]
    current = base
    total_value = 0
    remaining = asteroids.copy()

    fuel_left = fuel

    while remaining:
        best = None
        best_ratio = 0

        for a in remaining:
            dist_to_a = distance(current, a)
            dist_to_base = distance(a, base)

            # Verificar si puede ir y volver
            if dist_to_a + dist_to_base > fuel_left:
                continue

            ratio = a.value / dist_to_a if dist_to_a != 0 else 0

            if ratio > best_ratio:
                best_ratio = ratio
                best = a

        if best is None:
            break

        # Consumir combustible
        fuel_used = distance(current, best)
        fuel_left -= fuel_used

        route.append(best)
        total_value += best.value
        current = best
        remaining.remove(best)

    # Volver a la base
    fuel_left -= distance(current, base)
    route.append(base)

    return route, total_value, fuel_left