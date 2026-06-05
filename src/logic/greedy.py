from logic.utils import distance

def greedy_recommendation(current, asteroids, selected_route):
    """
    Returns the asteroid with the best value/distance ratio.
    Used as a hint system for the player.
    """

    best = None
    best_score = -1

    # Evaluate every available asteroid
    for asteroid in asteroids:

        # Skip already visited asteroids
        if asteroid in selected_route:
            continue

        # Distance from current position
        dist = distance(current, asteroid)

        # Avoid division by zero
        if dist == 0:
            continue

        # Greedy criterion:
        # maximize value obtained per unit of distance
        score = asteroid.value / dist

        # Keep the best candidate found so far
        if score > best_score:
            best_score = score
            best = asteroid

    return best