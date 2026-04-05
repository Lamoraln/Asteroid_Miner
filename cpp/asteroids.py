class Asteroid:
    def __init__(self, x, y, value, name):
        self.x = x
        self.y = y
        self.value = value
        self.name = name

    def __repr__(self):
        return f"{self.name}(V={self.value})"