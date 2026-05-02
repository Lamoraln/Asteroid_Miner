from logic.asteroids import Asteroid

def get_level(level):

    if level == 1:
        return {
            "base": Asteroid(1, 5, 0, "Base"),
            "asteroids": [
                Asteroid(3, 2, 20, "A1"),
                Asteroid(6, 3, 30, "A2"),
                Asteroid(5, 6, 25, "A3"),
                Asteroid(2, 7, 15, "A4"),
            ],
            "fuel": 15
        }

    elif level == 2:
        return {
            "base": Asteroid(2, 4, 0, "Base"),
            "asteroids": [
                Asteroid(4, 2, 25, "B1"),
                Asteroid(7, 3, 35, "B2"),
                Asteroid(6, 6, 40, "B3"),
                Asteroid(3, 7, 20, "B4"),
                Asteroid(8, 5, 50, "B5"),
            ],
            "fuel": 20
        }

    elif level == 3:
        return {
            "base": Asteroid(1, 6, 0, "Base"),
            "asteroids": [
                Asteroid(3, 3, 30, "C1"),
                Asteroid(6, 2, 40, "C2"),
                Asteroid(7, 6, 45, "C3"),
                Asteroid(4, 8, 25, "C4"),
                Asteroid(9, 5, 60, "C5"),
                Asteroid(8, 8, 70, "C6"),
            ],
            "fuel": 25
        }