from logic.asteroids import Asteroid

def get_level(level):

    if level == 1:
        return {
            "base": Asteroid(1, 5, "silver", "Base"),
            "asteroids": [

                Asteroid(3, 3, "silver", "S1"),
                Asteroid(4, 5, "silver", "S2"),
                Asteroid(2, 7, "silver", "S3"),

                Asteroid(5, 2, "gold", "G1"),
                Asteroid(6, 4, "gold", "G2"),

                Asteroid(8, 2, "diamond", "D1"),

                Asteroid(8, 7, "diamond", "D2"),

                Asteroid(10, 5, "dark_matter", "DM1")
            ],
            "fuel": 18
        }

    elif level == 2:
        return {
            "base": Asteroid(1, 5, "silver", "Base"),
            "asteroids": [

                Asteroid(2,2,"silver","S1"),
                Asteroid(3,4,"silver","S2"),
                Asteroid(2,8,"silver","S3"),
                Asteroid(4,7,"silver","S4"),

                Asteroid(5,2,"gold","G1"),
                Asteroid(6,4,"gold","G2"),
                Asteroid(5,8,"gold","G3"),

                Asteroid(8,2,"diamond","D1"),
                Asteroid(9,5,"diamond","D2"),
                Asteroid(8,8,"diamond","D3"),

                Asteroid(11,3,"dark_matter","DM1"),
                Asteroid(11,7,"dark_matter","DM2")
            ],
            "fuel": 25
        }

    elif level == 3:
        return {
            "base": Asteroid(1,5,"silver","Base"),
            "asteroids":[

                Asteroid(2,2,"silver","S1"),
                Asteroid(2,4,"silver","S2"),
                Asteroid(3,7,"silver","S3"),
                Asteroid(4,8,"silver","S4"),
                Asteroid(5,6,"silver","S5"),

                Asteroid(6,2,"gold","G1"),
                Asteroid(7,4,"gold","G2"),
                Asteroid(7,7,"gold","G3"),
                Asteroid(8,6,"gold","G4"),

                Asteroid(9,2,"diamond","D1"),
                Asteroid(10,4,"diamond","D2"),
                Asteroid(9,8,"diamond","D3"),
                Asteroid(10,7,"diamond","D4"),

                Asteroid(12,3,"dark_matter","DM1"),
                Asteroid(12,6,"dark_matter","DM2"),
                Asteroid(13,8,"dark_matter","DM3")
            ],
            "fuel": 32
        }