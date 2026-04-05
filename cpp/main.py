from asteroids import Asteroid
from greedy import greedy_route

def main():
    # Base
    base = Asteroid(0, 0, 0, "Base")

    # Asteroides de prueba
    asteroids = [
        Asteroid(2, 3, 10, "A1"),
        Asteroid(5, 1, 25, "A2"),
        Asteroid(6, 4, 30, "A3"),
        Asteroid(1, 7, 15, "A4"),
        Asteroid(8, 2, 40, "A5"),
    ]

    fuel = 10

    route, total_value, fuel_left = greedy_route(base, asteroids, fuel)

    print("\n--- RESULTADOS GREEDY ---")
    print("Ruta:")
    for r in route:
        print(f" -> {r}")

    print(f"\nValor total recolectado: {total_value}")
    print(f"Combustible restante: {round(fuel_left,2)}")

if __name__ == "__main__":
    main()