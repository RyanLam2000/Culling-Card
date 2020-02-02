from enemy import Enemy

class WaterSlime(Enemy):
    def __init__(self, multiplier = 0):
        super().__init__(4, 10, 'blue', "IceSlime.png", multiplier)