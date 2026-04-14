from logic.asteroids import Asteroid
from logic.greedy import greedy_route
from logic.backtracking import backtracking_route

def main():
    base = Asteroid(0, 0, 0, "Base")

    asteroids = [
        Asteroid(2, 3, 10, "A1"),
        Asteroid(5, 1, 25, "A2"),
        Asteroid(6, 4, 30, "A3"),
        Asteroid(1, 7, 15, "A4"),
        Asteroid(8, 2, 40, "A5"),
    ]

    fuel = 25

    # GREEDY
    greedy_r, greedy_val, fuel_left = greedy_route(base, asteroids, fuel)

    # BACKTRACKING
    optimal_r, optimal_val = backtracking_route(base, asteroids, fuel)

    print("\n--- GREEDY ---")
    for r in greedy_r:
        print(f" -> {r}")
    print(f"Valor: {greedy_val}")

    print("\n--- OPTIMO (BACKTRACKING) ---")
    for r in optimal_r:
        print(f" -> {r}")
    print(f"Valor: {optimal_val}")

    # Comparación
    efficiency = (greedy_val / optimal_val) * 100 if optimal_val > 0 else 0

    print("\n--- COMPARACION ---")
    print(f"Eficiencia Greedy: {round(efficiency,2)}%")

if __name__ == "__main__":
    main()