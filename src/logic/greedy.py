from logic.utils import distance

def greedy_recommendation(current, asteroids, selected_route):

    best = None
    best_score = -1

    for asteroid in asteroids:

        if asteroid in selected_route:
            continue

        dist = distance(current, asteroid)

        if dist == 0:
            continue

        score = asteroid.value / dist

        if score > best_score:
            best_score = score
            best = asteroid

    return best